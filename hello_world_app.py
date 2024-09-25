import flet as ft

def main(page: ft.Page):
    page.title = "Olá, Mundo!"
    page.scroll = "adaptive"

    # declaração de variáveis
    nome = ft.TextField(label="Nome")

    page.add(
        ft.Text("Olá, mundo!", size=30, font_family="times new woman", color="red", weight="bold"),
        nome,
        ft.TextButton("Clique aqui",)
        ft.Text(texto)
    )

    page.update()

ft.app(main)    