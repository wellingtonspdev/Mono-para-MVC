from fastapi import APIRouter, HTTPException
from controllers.controller import buscar_cep, consultar_cache, consultar_todo_cache, calcular_frete
from views.responses import resposta_padrao, resposta_erro  # corrigido aqui!

router = APIRouter()

@router.get("/cep/{cep}")
async def buscar_cep_api(cep: str):
    try:
        resultado = await buscar_cep(cep)
        return resposta_padrao(resultado["data"], resultado["cache"])
    except HTTPException as e:
        return resposta_erro(e.detail, e.status_code)

@router.get("/cache/{cep}")
async def consultar_cache_api(cep: str):
    try:
        resultado = consultar_cache(cep)
        return resposta_padrao(resultado["data"])
    except HTTPException as e:
        return resposta_erro(e.detail, e.status_code)

@router.get("/cache")
async def consultar_todo_cache_api():
    resultado = consultar_todo_cache()
    return resposta_padrao(resultado["data"])

@router.get("/frete/{cep_origem}/{cep_destino}")
async def calcular_frete_api(cep_origem: str, cep_destino: str):
    try:
        resultado = calcular_frete(cep_origem, cep_destino)
        return resposta_padrao(resultado)
    except HTTPException as e:
        return resposta_erro(e.detail, e.status_code)
from fastapi import APIRouter, HTTPException
from controllers.controller import buscar_cep, consultar_cache, consultar_todo_cache, calcular_frete
from views.responses import resposta_padrao, resposta_erro  # corrigido aqui!

router = APIRouter()

@router.get("/cep/{cep}")
async def buscar_cep_api(cep: str):
    try:
        resultado = await buscar_cep(cep)
        return resposta_padrao(resultado["data"], resultado["cache"])
    except HTTPException as e:
        return resposta_erro(e.detail, e.status_code)

@router.get("/cache/{cep}")
async def consultar_cache_api(cep: str):
    try:
        resultado = consultar_cache(cep)
        return resposta_padrao(resultado["data"])
    except HTTPException as e:
        return resposta_erro(e.detail, e.status_code)

@router.get("/cache")
async def consultar_todo_cache_api():
    resultado = consultar_todo_cache()
    return resposta_padrao(resultado["data"])

@router.get("/frete/{cep_origem}/{cep_destino}")
async def calcular_frete_api(cep_origem: str, cep_destino: str):
    try:
        resultado = calcular_frete(cep_origem, cep_destino)
        return resposta_padrao(resultado)
    except HTTPException as e:
        return resposta_erro(e.detail, e.status_code)
