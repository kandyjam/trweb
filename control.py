'''
    File name: control.py
    Author: xdtianyu@gmail.com
    Date created: 2015-01-25 09:56:46
    Date last modified: 2015-01-25 12:52:23
    Python Version: 2.7.3
'''

import subprocess

status=False

def show_control():
    s = speed()
    max_speed = 1024.0
    if float(s) > max_speed:
        s = str(max_speed)
    per = float(s)/max_speed*100
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Download Speed Controller</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="static/css/bootstrap.min.css">
  <script src="static/js/jquery.min.js"></script>
  <script src="static/js/bootstrap.min.js"></script>
    <script>
        $(document).ready(function() {
            setInterval(function() {
                $('#speed').load(document.URL + ' #speed');
                }, 3000);
            });
    </script>
    <style>
        .progress {
            position:relative;
        }
        .progress span {
            position:absolute;
            left:0;
            width:100%;
            text-align:center;
            z-index:2;
        }
    </style>
</head>
<body>

<div class="container">
  <h2>Current Speed</h2>
  <div id="speed" class="progress">
    <div class="progress-bar" role="progressbar" aria-valuenow="'''+s+'''" aria-valuemin="0" aria-valuemax="'''+str(max_speed)+'''" style="width:'''+str(per)+'''%">
      <span>'''+s+'''KB/s</span>
    </div>
  </div>
</div>

</body>
</html>
'''

def post(request):
    global status
    
    if status:
        status = False
    else:
        status = True
    return "post"

def speed():
    s = subprocess.Popen(['/root/bin/speed.sh'], stdout=subprocess.PIPE)
    out,error = s.communicate()
    return out
