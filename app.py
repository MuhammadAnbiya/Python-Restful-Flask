#import library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS


#inisiasi object flask
app = Flask(__name__)
#inisiasi object flask_restful
api = Api(app)
#inisiasi object flask_cors
CORS(app)


#inisiasi variabel kosong bertipe dictionary
identitas = {}   #dictionary = json

#membuat class resouse
class contohResource(Resource):
    #method get dan post
    def get(self):
        # response = {"msg" : "Hello World"}
        return identitas
    
    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas[nama] = nama
        identitas[umur] = umur
        response = {"msg" : "Data Berhasil dimasukan "}
        return response
        
        
# setup resourcenya
api.add_resource(contohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)