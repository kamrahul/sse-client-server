from flask import Flask,Response, render_template
import time
from flask_cors import CORS,cross_origin
app = Flask(__name__,template_folder="template")
CORS(app)

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name


def get_message():
    '''this could be any function that blocks until data is ready'''
    time.sleep(1.0)
    s = time.ctime(time.time())
    return s

@app.route('/test')
def root():
    #return "details"
    return render_template('/index.html')

@app.route('/stream')
@cross_origin()
def stream():
    def eventStream():
        while True:
            # wait for source data to be available, then push it
            yield 'data: {}\n\n'.format(get_message())
    return Response(eventStream(), mimetype="text/event-stream")


if __name__ == '__main__':
    app.run(port=7001)
