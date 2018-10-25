from flask import (
	Flask,
	render_template
	)
import connexion

print('Starting')
# Create the application instance
print('Creating app instance')
#app = Flask(__name__, template_folder="templates")

app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

print('Creating default route')
# Create a URL route in our application for "/"
@app.route('/')
def home():
	return render_template('home.html')
	#return "Hello World - This is running from docker. This is using only python image"

@app.route('/contactus')
def contactus():
	return "This is contact us page"
	#return "Hello World - This is running from docker. This is using only python image"

# if we are running in standalone mode, run the application
if __name__ == "__main__":
	print('running app.run')
	app.run(host='0.0.0.0')