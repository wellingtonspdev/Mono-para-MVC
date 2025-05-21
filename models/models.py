import re
import httpx
from fastapi import HTTPException

# Cache de CEPs consultados
cep_cache = {}

def validar_cep(cep: str) -> bool:
    """Valida se o CEP tem o formato correto."""
    return re.fullmatch(r"\d{5}-?\d{3}", cep) is not None

def normalizar_cep(cep: str) -> str:
    """Remove hífens do CEP para normalização."""
    return cep.replace("-", "")

async def consultar_cep_externo(cep: str) -> dict:
    """Consulta o CEP na API externa ViaCEP."""
    url = f"https://viacep.com.br/ws/{cep}/json/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            if "erro" in data:
                raise HTTPException(status_code=404, detail="CEP não encontrado")
            return data
        else:
            raise HTTPException(status_code=404, detail="CEP não encontrado")
