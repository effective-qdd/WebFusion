from flask import Flask, render_template, request
import logging
import logging.handlers
import time
import datetime
import json

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.DEBUG)
time_str = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime())
all_log_file_name = time_str + "_webfusion_all.log"
all_log_handler = logging.handlers.TimedRotatingFileHandler(
            all_log_file_name,
            when="midnight",
            atTime=datetime.time(0, 0, 0, 0)
        )
all_log_handler.setFormatter(
   logging.Formatter(
         "[%(asctime)s][%(levelname)s][%(filename)s-%(funcName)s]:%(message)s"
   )
)
log.addHandler(all_log_handler)

@app.route('/')
def index():
   return render_template('index.html', function=add_numbers)

@app.route('/get_info')
def get_info():
   res = {'error_code':0}
   return json.dumps(res)

@app.route('/set_info', methods = ['POST'])
def set_info():
   data = request.get_json()
   res = {'error_code':0, 'data':data}
   return json.dumps(res)

def add_numbers(a, b):
   return a + b

if __name__ == '__main__':
   app.run()