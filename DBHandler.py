
from pymongo import MongoClient

from ResponseModel import ResponseModel


class DBHandler(object):
    def __init__(self):
        self.db = self.conectar()
        self.collection = self.db.get_collection('estudiantes')


    def conectar(self):
        client = MongoClient(
            host = 'infsalinas.sytes.net:10450',
            serverSelectionTimeoutMS = 3000,
            username = '2dam11',
            password = 'Y3526088H',
            authSource = '2dam11'
        )
        db = client.get_database('2dam11')
        return db


    def insertarImagen(self, image):
        response = ResponseModel()
        try:
            self.collection = self.db.get_collection('imagenes')
            self.collection.update_one({'_id':image['_id']},{'$push':{'imagenes':image['imagenes']}}, upsert=True)
            response.resultOk = True
            response.data = 'Imagen insertada con exito'
        except Exception as e:
            print(e)

        return response

    def obtenerImagenes(self, _idE):
        response = ResponseModel()
        try:
            self.collection = self.db.get_collection('imagenes')
            imagenes = self.collection.find_one({'_id': _idE})

            if imagenes is None:
                print("ES NONE")
                response.resultOk = False
                response.data = "No hay imagenes"
            else:
                response.resultOk = True
                response.data = str(imagenes)


        except Exception as e:
            print(e)

        return response



    #######################################
    #ESTUDIANTES
    def eliminarEstudiante(self,_idE):
        response = ResponseModel()

        try:
            self.collection = self.db.get_collection('productos')
            self.collection.delete_one({'_id':_idE})
            response.resultOk = True
            response.data = 'Producto eliminado con exito'
        except Exception as e:
            print(e)

        return response

    def obtenerEstudiante(self,_idE):
        response = ResponseModel()
        try:
            self.collection = self.db.get_collection('productos')
            estudiante = self.collection.find_one({'_id':_idE})
            response.resultOk = True
            response.data = str(estudiante)
            if response.data == 'None':
                response.resultOk = False
        except Exception as e:
            print(e)

        return response


    def actualizar(self, estudiante):
        response = ResponseModel()
        print(estudiante['Descripcion'])

        try:
            self.collection = self.db.get_collection('productos')
            self.collection.update_one({'_id':estudiante['_id']},{'$set':estudiante})
            response.resultOk = True
            response.data = 'Producto actualizado con exito'
        except Exception as e:
            print(e)

        return response

    # obtenerLista (en los videos)
    def obtenerEstudiantes(self):
        response = ResponseModel()
        try:
            self.collection = self.db.get_collection('productos')
            listaEstudiantes = []
            coleccion = self.collection.find({})
            for estudiante in coleccion:
                listaEstudiantes.append(estudiante)

            response.resultOk = True
            response.data = str(listaEstudiantes)

        except Exception as e:
            print(e)

        return response

    def insertarEstudiante(self, estudiante):
        response = ResponseModel()
        try:
            self.collection = self.db.get_collection('productos')
            self.collection.insert_one(estudiante)
            response.resultOk = True
            response.data = 'Producto insertado con exito'
        except Exception as e:
            print(e)

        return response