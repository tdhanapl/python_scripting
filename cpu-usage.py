# Importing the library
import psutil
from flask import Flask, remder_template
app = Flask(__name__)
@app.route("/")
def index():
    cpu_percent = psutil.cpu_percent
    mem_percent = psutil.virtual_memory().percent
    message = None
    if cpu_percent > 75 or mem_percent > 75:
       message = "High CPU or memory utilization detected!"
    return remder_template("index.html", cpu_percent=cpu_percent, mem_percent=mem_percent, message=message)
if __name__ == '_main_':
    app.run(debug=True, host='0.0.0.0')

# Calling psutil.cpu_precent() for 4 seconds
#print('The CPU usage is: ', psutil.cpu_percent(4))
