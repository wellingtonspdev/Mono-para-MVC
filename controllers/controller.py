from fastapi import HTTPException
from models.models import validar_cep, consultar_cep_externo, cep_cache, normalizar_cep

async def buscar_cep(cep: str):
    """Busca dados de um CEP, utilizando cache se disponível."""
    cep = normalizar_cep(cep)

    if not validar_cep(cep):
        raise HTTPException(status_code=400, detail="Formato de CEP inválido")

    if cep in cep_cache:
        return {"data": cep_cache[cep], "cache": True}

    dados_cep = await consultar_cep_externo(cep)
    cep_cache[cep] = dados_cep

    return {"data": dados_cep, "cache": False}

def consultar_cache(cep: str):
    """Consulta o cache local para um CEP específico."""
    cep = normalizar_cep(cep)

    if cep in cep_cache:
        return {"data": cep_cache[cep]}
    else:
        raise HTTPException(status_code=404, detail="CEP não encontrado no cache")

def consultar_todo_cache():
    """Retorna todos os dados armazenados no cache."""
    return {"data": cep_cache}

def calcular_frete(cep_origem: str, cep_destino: str):
    """Calcula uma estimativa simples de frete com base nos dois CEPs."""
    cep_origem = normalizar_cep(cep_origem)
    cep_destino = normalizar_cep(cep_destino)

    if not (validar_cep(cep_origem) and validar_cep(cep_destino)):
        raise HTTPException(status_code=400, detail="Formato de CEP inválido")

    distancia = abs(int(cep_origem[:5]) - int(cep_destino[:5]))
    valor_frete = distancia * 0.1  # Valor fictício por unidade de distância

    return {
        "cep_origem": cep_origem,
        "cep_destino": cep_destino,
        "distancia": distancia,
        "valor_frete": valor_frete
    }
