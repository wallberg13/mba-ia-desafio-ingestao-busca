from search import search_prompt
from dotenv import load_dotenv

load_dotenv()


def main():

    # Aquele white true feio / padrão para simular um chat infinito.
    while True:
        print("Digite sua pergunta ou 'sair' para encerrar: ")
        question = input("PERGUNTA: ")

        if question.lower() in ["sair", "exit", "quit"]:
            break

        response = search_prompt(question)

        print(f"RESPOSTA: {response}")
        print("=" * 50)
        

if __name__ == "__main__":
    main()