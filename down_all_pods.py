#####python script for down all pods#####  
#!/bin/python
import os
import subprocess
import re
import sys
exclusions=sys.argv[1:]
print("Excluding these namespaces",exclusions)
namespaces = subprocess.run(["kubectl", "get", "namespaces", "-o", "name"],
                            capture_output="True",
                            timeout=10)
# print(namespaces)
if namespaces.stdout:
    for ns in namespaces.stdout.decode("utf-8").split("\n"):
        ns = ns.replace("namespace/", "")
        if ns in exclusions and re.match(r'^kube-', ns) is not None:
            continue
        pods = subprocess.run(["kubectl", "get", "pods", "-n", ns],
                              capture_output="true",
                              timeout=10)
        if pods.stderr and "No resources found" in pods.stderr.decode("utf-8"):
            print("\n – %s - Namespace Empty" % ns)
        else:
            if ns not in exclusions and re.match(r'^kube-', ns) is None:
                print("\n – %s - Scaling down" % ns)
                scale = subprocess.run([
                    "kubectl", "scale", "deployment", "--all", "--replicas=0",
                    "-n", ns
                ],
                                       timeout=100)
                if scale.returncode == 0:
                    print("✓ %s - Namespace Scaled Down" % ns)
 

