from fastapi.responses import JSONResponse

def resposta_padrao(data, cache=False):
    return JSONResponse(content={"data": data, "cache": cache})

def resposta_erro(mensagem: str, status_code: int):
    return JSONResponse(content={"detail": mensagem}, status_code=status_code)
