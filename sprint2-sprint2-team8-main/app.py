from flask import Flask, jsonify, request
from plane_controls.controls import arm_plane, disarm_plane, set_elevator_pitch, set_throttle



app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to the drone control API!'})

@app.route('/arm', methods=['GET'])
def arm():
    response = {}
    try:
        arm_plane()
        response['status'] = 'success'
        response['message'] = 'ARM command sent successfully!'
    except Exception as e:
        response['status'] = 'error'
        response['message'] = str(e)
    return jsonify(response)

@app.route('/disarm', methods=['GET'])
def disarm():
    response = {}
    try:
        disarm_plane()
        response['status'] = 'success'
        response['message'] = 'DISARM command sent successfully!'
    except Exception as e:
        response['status'] = 'error'
        response['message'] = str(e)
    return jsonify(response)

@app.route('/throttle', methods=['POST'])
def throttle():
    throttle_percentage = int(request.json['throttle_percentage'])
    response = {}
    try:
        set_throttle(throttle_percentage)
        response['status'] = 'success'
        response['message'] = 'Throttle set successfully!'
        # print('in try block of throttle')
    except Exception as e:
        response['status'] = 'error'
        response['message'] = str(e)
        print('in except block', e)
    return jsonify(response)

@app.route('/elevator_pitch', methods=['POST'])
def elevator_pitch():
    elevator_pitch_percentage = int(request.json['elevator_pitch_percentage'])
    response = {}
    try:
        set_elevator_pitch(elevator_pitch_percentage)
        response['status'] = 'success'
        response['message'] = 'Elevator/pitch set successfully!'
    except Exception as e:
        response['status'] = 'error'
        response['message'] = str(e)
    return jsonify(response)


