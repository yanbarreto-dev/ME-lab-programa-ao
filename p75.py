def conectar_api():
    for tentativa in range(1, 4):
        try:
            print(f"Tentativa {tentativa}...")

            # Simulação de falha de conexão
            raise ConnectionError("Falha na conexão.")

        except ConnectionError:
            print("Não foi possível conectar.")

    print("Limite de tentativas atingido.")


conectar_api()