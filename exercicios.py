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
    return message.content

print(perguntar(input("Digite uma pergunta: ")))
