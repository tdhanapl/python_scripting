import os
file_list = !ls
top =!top -b -n 2 -d1 | grep -i "cpu(s)" | tail -n1 | awk '{print $2}'  | awk -F . '{print $1}'
file_list
top