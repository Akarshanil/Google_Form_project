import pymongo
from bson import ObjectId
from django.utils import timezone

client =pymongo.MongoClient('mongodb://localhost:27017')
db=client['Googleforms']
col=db['googleformcollection']


class Form:
    def create(self):
        obj=col.insert_one({
            'created':timezone.now()
        })
        return str(obj.inserted_id)
    def find(self,pk):
        query={
            '_id':ObjectId(pk)
        }
        obj=col.find(query).next()
        return obj
    def update(self,pk,form_data):
        query={'_id':ObjectId(pk)}
        updated_vlaue={
            '$set':{
                'form_data':form_data['formData'],
                'updated':timezone.now()
            }
        }
        col.update_one(query,updated_vlaue)
        print('Data is Updated')
    def findall(self):

        return col.find({ 'updated': { '$exists': 'true' } }).sort({ 'updated': -1 })
    def update_response(self,pk,response):
        query={'_id':ObjectId(pk)}
        updated_value={
            '$inc':response

        }
        col.update_one(query,updated_value)


