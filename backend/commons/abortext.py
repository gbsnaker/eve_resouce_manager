from flask import abort,make_response,jsonify

#abort(make_response(jsonify(message="Message goes here"), 400))

def abort_json(message,status):
    abort(make_response(jsonify(message=message), status))

def abrot_json_ok(message, status):
    abort(make_response(jsonify(message=message, status=status)),200)