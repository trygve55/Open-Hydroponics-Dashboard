from flask import Flask, jsonify, render_template, make_response, request, abort
from modules.gpio_relay import GPIORelay
import io

###Testing web interface endpoints start

# Create the application instance
app = Flask(__name__, template_folder="module_templates", static_url_path='/public', static_folder='public') #Sets static public folder
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024                         #Sets max file size

###HTTP files start

###REST interface endpoints start
# Load main page
@app.route('/')
def home():
    return render_template('index.html')

###HTTP files end


####REST interface endpoints start

#Test GET
@app.route('/api/test', methods=['get'])
def test_get():

    return jsonify({}), 200


#Test POST
@app.route('/api/test', methods=['post'])
def test_post():

    return jsonify({}), 200


#GPIO test
@app.route('/api/gpio', methods=['post'])
def gpio_post():

    test = GPIORelay(26)
    test.set_state(1)

    return jsonify({}), 200

###REST interface endpoints end


###SSL keys and certs setup start

context = ('pam/server.crt', 'pam/server.key')

###SSL keys and certs setup end


####Runs server start

if __name__ == '__main__':
    config = {
        'flask_debug': False,
        'port': 8080,
        'ssl_port': 8443,
        'ssl': 'auto'
    }

    '''
    server_params = {
        'debug': config.flask_debug
    }'''

    #app.run(debug=True, ssl_context=context, port=8443)                    #Enable this line for SSL(HTTPS)
    app.run(debug=False, port=8080)                                          #Disable this line for SSL(HTTPS)

####Runs server end