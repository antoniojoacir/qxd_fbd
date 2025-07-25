from pydantic import BaseModel
from datetime import date
from models.endereco import Endereco
from models.contato import Contato


class Cliente(BaseModel):
    id_cliente: int
    cpf: str
    pnome: str
    unome: str
    data_nasc: date
    contato: Contato
    endereco: Endereco

