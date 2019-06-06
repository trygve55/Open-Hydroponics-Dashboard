from flask import Flask, jsonify, render_template, make_response, request, abort
from importlib import util

#Check if running on RPi
if util.find_spec("RPi") is not None:
    from modules.gpio_relay import GPIORelay
    from modules.am2302 import AM2302
else:
    from modules.dummy_relay import GPIORelay
    from modules.dummy_sensor import DummySensor as AM2302

###Set up devices start

devices = dict()

devices['relay0'] = GPIORelay(26)
devices['relay1'] = GPIORelay(16)
devices['relay2'] = GPIORelay(20)
devices['relay3'] = GPIORelay(21)
devices['sensor0'] = AM2302(22)

###Set up devices end

###Testing web interface endpoints start

# Create the application instance
app = Flask(__name__, template_folder="templates", static_url_path='/public', static_folder='public') #Sets static public folder
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


#Devices list
@app.route('/api/devices', methods=['get'])
def get_devices():
    devices_list = list()
    for k in devices.keys():
        devices_list.append({
            'name': k,
            'state': devices[k].get_state()
        })

    return jsonify(devices_list), 200

#Device
@app.route('/api/device', methods=['post'])
def device_post():

    data = request.get_json()

    if data['device'] not in devices.keys():
        return 404

    devices[data['device']].set_state(data['state'])

    return jsonify({'state': devices[data['device']].get_state()}), 200

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
    app.run(debug=True, port=8080, host='0.0.0.0')                                          #Disable this line for SSL(HTTPS)

####Runs server end