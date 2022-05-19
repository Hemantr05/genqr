from uuid import UUID, uuid4
from datetime import datetime

from typing import Optional
from pydantic import BaseModel, Field
from firedantic import Model

class ImageInfo(BaseModel):
    image_byte_string: bytes = Field(default_factor=None)

class QRCreation(Model):
    __collection__ = "qr-code-api"
    id: Optional[UUID] = str(uuid4())
    creation: datetime = Field(default_factory=datetime.now)
    image_info: ImageInfo