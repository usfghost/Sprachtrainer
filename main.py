import typer

app = typer.Typer()

@app.command()
def deen(word:str):
    print('Translating ' + word + ' from De to En')

@app.command()
def ende(word:str):
    print(word + ' wird übergesetzt von En auf De.')

def translate(src:str, trg:str, word:str):
    print()

if __name__ == '__main__':
    app()