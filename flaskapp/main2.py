from flask import Flask
#import logging

app = Flask(__name__)
# file_handler = logging.FileHandler(filename='/home/dev/python/wsgi/error.log')
# file_handler.setLevel(logging.WARNING)
# app.logger.addHandler(file_handler)

@app.route('/')
def index():
	return "hello there I'm working"
        #status = '200 OK'
        #output = "Hello World!"
        #response_headers = [('Content-type', 'text/plain'),
		#('Content-Length', str(len(output)))]
        #start_response(status, response_headers)
        #return [output]
	#raise Exception('Deliberate exception raised')

if __name__ == '__main__':
	app.run(debug=True)
