from flask import Flask, request, jsonify

app = Flask(__name__)

#GET  REQUEST DATA FROM A SPECIFIED RSOURCE
#POST CREATE A RESOURCE
#PUT  UPDATE A RESOURCE
#DELETE DELETE A RESOURCE

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
          "user_id": user_id,
          "name": "john doe",
          "email":"john.doe@exmaple.com"
     }
    
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra

    return jsonify(user_data), 200  

@app.route("create-user", methods= ["POST"])
def create_user():
    data = request.get_json()
    return jsonify(data), 201
  

if __name__ == "__main__":
    app.run(debug = True)