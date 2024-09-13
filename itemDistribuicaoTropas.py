from pydantic import BaseModel
from uuid import UUID

class ItemDistribuicaoTropas(BaseModel):
    id_territorio: UUID
    tropas: int
