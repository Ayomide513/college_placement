from pydantic import BaseModel, Field
from typing import Dict



# defining the root response payload
class HomeResponse(BaseModel):
    """Provides the schema structure for the application homepage.
    """
    message: str = Field(..., description="root_response message for homepage", examples=["we are live","Welcome!"])

class ModelResponse(BaseModel):
    iq: float = Field(..., description="IQ score", example=[3.4,123.9], ge=0, le=300)
