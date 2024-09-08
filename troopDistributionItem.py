from pydantic import BaseModel
from uuid import UUID

class TroopDistributionItem(BaseModel):
    territory_id: UUID
    troops: int