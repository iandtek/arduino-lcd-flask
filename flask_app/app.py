from flask import Flask, render_template, url_for, request, redirect, jsonify, session
import serial

arduino = serial.Serial('/dev/cu.usbmodem14101')

app = Flask(__name__)
# secret key is needed for session
app.secret_key = 'dljsaklqk24e21cjn!Ew@@dsa5'

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/led", methods=['GET'])
def led():
    try:
        session["led_is_on"]
    except:
        session["led_is_on"] = False
    return render_template('led.html',led_is_on=session["led_is_on"])
    
@app.route("/lcd", methods=['GET'])
def lcd():
    try:
        session["message"] = str(request.args.get('message'))
    except:
        session["message"] = ""
    arduino.write(session["message"].encode('ascii')) 
    return render_template('lcd.html',message=session["message"])


@app.route("/led/<int:is_on>")
def turn_led(is_on):
    if is_on:
        print("Turning ON LED") # Add serial logic here
        arduino.write(b'1') 
        session["led_is_on"]  = True
        return redirect('/led')
    else:
        print("Turning OFF LED")
        arduino.write(b'0') 
        session["led_is_on"]  = False  
        return redirect('/led')    

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)