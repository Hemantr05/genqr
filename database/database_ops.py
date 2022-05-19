import os
import firebase_admin
from firebase_admin import credentials, firestore
from firedantic import configure
from models.models import QRCreation, ImageInfo

# cred = credentials.Certificate("test-ec22b-firebase-adminsdk-fezwt-61803c7945.json")
cred = credentials.Certificate(os.environ.get("FIRESTORE_SERVICE_ACCOUNT"))
firebase_admin.initialize_app(cred, {"projectId": cred.project_id})

db = firestore.client()
configure(db)

def firestore_write(img_bytes):
    image_model = ImageInfo(image_byte_string=str(img_bytes))
    resp = QRCreation(image_info=image_model)
    resp.save()
    return resp.id

def firestore_read(id):
    image = QRCreation.find({"id": str(id)})
    print(image)
    # return image
    # .image_info
    # image_bytes = bytes(image, 'utf-8')
    # return image_bytes

def firestore_delete(id):
    db.collection(u'qr-code-api').document(str(id)).delete()




