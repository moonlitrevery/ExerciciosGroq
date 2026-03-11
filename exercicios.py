import os
import json
from openai import OpenAI
from tools import *
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq()

tools = [
    {
        "type": "function",
        "function": {
            "name": "somar",
            "description": "Soma dois números",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "integer",
                        "description": "Primeiro número"
                    },
                    "b": {
                        "type": "integer",
                        "description": "Segundo número"
                    }
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "multiplicar",
            "description": "Multiplica dois números",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "integer",
                        "description": "Primeiro número"
                    },
                    "b": {
                        "type": "integer",
                        "description": "Segundo número"
                    }
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "dividir",
            "description": "Divide dois números",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "integer",
                        "description": "Primeiro número"
                    },
                    "b": {
                        "type": "integer",
                        "description": "Segundo número"
                    }
                },
                "required": ["a", "b"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "subtrair",
            "description": "Subtrai dois números",
            "parameters": {
                "type": "object",
                "properties": {
                    "a": {
                        "type": "integer",
                        "description": "Primeiro número"
                    },
                    "b": {
                        "type": "integer",
                        "description": "Segundo número"
                    }
                },
                "required": ["a", "b"]
            }   
        }
    },
    {
        "type": "function",
        "function": {
            "name": "converter_celsius_para_fahrenheit",
            "description": "Converte Celsius para Fahrenheit",
            "parameters": {
                "type": "object",
                "properties": {
                    "celsius": {
                        "type": "number",
                        "description": "Temperatura em Celsius"
                    }
                },
                "required": ["celsius"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "converter_fahrenheit_para_celsius",
            "description": "Converte Fahrenheit para Celsius",
            "parameters": {
                "type": "object",
                "properties": {
                    "fahrenheit": {
                        "type": "number",
                        "description": "Temperatura em Fahrenheit"
                    }
                },
                "required": ["fahrenheit"]
            }  
        }
    },
    {
        "type": "function",
        "function": {
            "name": "buscar_produtos",
            "description": "Busca o preço de um produto",
            "parameters": {
                "type": "object",
                "properties": {
                    "nome": {
                        "type": "string",
                        "description": "Nome do produto"
                    }
                },
                "required": ["nome"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "buscar_estoque",
            "description": "Busca o estoque de um produto",
            "parameters": {
                "type": "object",
                "properties": {
                    "nome": {
                        "type": "string",
                        "description": "Nome do produto"
                    }
                },
                "required": ["nome"]
            }   
        }
    },
    {
        "type": "function",
        "function": {
            "name": "criar_evento",
            "description": "Cria um evento",
            "parameters": {
                "type": "object",
                "properties": {
                    "titulo": {
                        "type": "string",
                        "description": "Título do evento"
                    },
                    "data": {
                        "type": "string",
                        "description": "Data do evento"
                    }
                },
                "required": ["titulo", "data"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "listar_eventos",
            "description": "Lista todos os eventos",
            "parameters": {
                "type": "object",
                "properties": {
                    "mostrar_todos": {
                        "type": "boolean",
                        "description": "Se deve mostrar todos os eventos ou apenas os eventos futuros"
                    }
                },
                "required": ["mostrar_todos"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "buscar_clima",
            "description": "Busca o clima de uma cidade",
            "parameters": {
                "type": "object",
                "properties": {
                    "cidade": {
                        "type": "string",
                        "description": "Nome da cidade"
                    }
                },
                "required": ["cidade"]
            }
        }
    }
]

def perguntar(pergunta: str):
    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {"role": "system", "content": "Você é um assistente que decide qual função usar."},
            {"role": "user", "content": pergunta}
        ],
        tools=tools,
        tool_choice="auto",
        temperature=0
    )
    message = response.choices[0].message
    if message.tool_calls:
        tool_call = message.tool_calls[0]
        tool_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

    if tool_name == "somar":
        return somar(**args)
    elif tool_name == "multiplicar":
        return multiplicar(**args)
    elif tool_name == "dividir":
        return dividir(**args)
    elif tool_name == "subtrair":
        return subtrair(**args)
    elif tool_name == "converter_celsius_para_fahrenheit":
        return converter_celsius_para_fahrenheit(**args)
    elif tool_name == "converter_fahrenheit_para_celsius":
        return converter_fahrenheit_para_celsius(**args)
    elif tool_name == "buscar_produtos":
        return buscar_produtos(**args)
    elif tool_name == "buscar_estoque":
        return buscar_estoque(**args)
    elif tool_name == "criar_evento":
        return criar_evento(**args)
    elif tool_name == "listar_eventos":
        return listar_eventos(**args)
    elif tool_name == "buscar_clima":
        return buscar_clima(**args)
    return message.content

print(perguntar(input("Digite uma pergunta: ")))
