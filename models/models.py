import re
import httpx
from fastapi import HTTPException

cep_cache = {}

def validar_cep(cep: str) -> bool:
    return re.fullmatch(r"\d{5}-?\d{3}", cep) is not None

async def consultar_cep_externo(cep: str) -> dict:
    url = f"https://viacep.com.br/ws/{cep}/json/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            raise HTTPException(status_code=404, detail="CEP não encontrado")
