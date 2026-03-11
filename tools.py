def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def subtrair(a, b):
    return a - b

def converter_celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def converter_fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def buscar_produtos(nome):
    produtos = {
    "notebook": 4500,
    "mouse": 80,
    "teclado": 150
}
    return produtos.get(nome, "Produto não encontrado")

def buscar_estoque(nome):
    estoque = {
    "notebook": 5,
    "mouse": 20,
    "teclado": 8
}
    return estoque.get(nome, "Produto não encontrado")

def criar_evento(titulo, data):
    return f"Evento criado: {titulo} - {data}"

def listar_eventos(mostrar_todos=True):
    return [
        {
            "titulo": "Fazer o slide do trabalho do Victor",
            "data": "2026-03-12"
        },
        {
            "titulo": "Dominação mundial",
            "data": "2026-06-07"
        }
    ]

def buscar_clima(cidade):
    clima = {
        "sao paulo": "24°C e nublado",
        "bauru": "30°C e ensolarado",
        "curitiba": "18°C e chuvoso"
    }
    return clima.get(cidade.lower().strip(), "Cidade não encontrada")