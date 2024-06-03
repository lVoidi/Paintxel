from frontend import FrontApp


def main() -> None:
    """
    Inicializa la interfaz gráfica
    :return: None 
    :rtype: NoneType
    """
    app = FrontApp()
    app.mainloop()


if __name__ == "__main__":
    main()
