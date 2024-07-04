from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/version', methods=['GET'])
def version():
    return jsonify({
        "version": "1.0.0",
        "build_sha": "abc57858585",
        "description": "pre-interview technical test"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
