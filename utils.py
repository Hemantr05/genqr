import io
import qrcode
import numpy as np
# from pyzbar.pyzbar import decode


def create_qr(content):
    qr_obj= qrcode.QRCode(  
        version = 1,  
        error_correction = qrcode.constants.ERROR_CORRECT_L,  
        box_size = 10,  
        border = 4,  
    ) 
    qr_obj.add_data(content)
    qr_obj.make(fit=True)
    qr_img = qr_obj.make_image()
    return qr_img

# def decode_qr(image):
#     message = None
#     results = decode(image)
#     if results:
#         for result in results:
#             code_type = result.type
#             if code_type == 'QRCODE':
#                 message = result.data
#     return message

def img2bytes(image):
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    return img_byte_arr