from pydantic import BaseModel, Field
from typing import Literal


#Создание модели
class ChatRequest(BaseModel): 
    message: str = Field(min_length=1, max_length=4000) #Задаем валидацию параметру
    conversation_id: str | None = None
    mode: Literal["chat", "rag", "auto"] = "auto"

class ChatResponse(BaseModel):
    answer: str
    model: str

request = ChatRequest(
    message="hello",
    mode="rag"
)

print(request)
print(request.model_dump()) # Serialization