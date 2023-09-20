import pandas as pd

# Dicionário que contem informações do livro
books = [
{
    'id': 0,
    'name': 'A Fórmula Mágica de Joel Greenblat para Bater o Mercado de Ações',
    'release_year': 2010,
    'author': 'Joel Greenblat'
},
{
    'id': 1,
    'name': 'Os Axiomas de Zurique',
    'release_year': 1985,
    'author': 'Max Gunther'    
},
{
    'id': 2,
    'name': 'Como Desfrutar sua Vida e Seu Trabalho',
    'release_year': 1970,
    'author': 'Dale Carnegie'
}
]

# ---------------------------------- EXTRACT ----------------------------------

# Função que lê o arquivo csv
df = pd.read_csv('Books.csv')
books_id = df['BookID'].tolist()

# Função que faz retornar as informações do dicionário através do ID
def get_book(book_id):
    for book in books:
        if book['id'] == book_id:
            return book
    return None

for book_id in books_id:
    book_info = get_book(book_id)


# --------------------------------- TRANSFORM ---------------------------------

# Dicionário que contem o gênero de cada livro do dicionário books, identificado com o mesmo id
gender_book = [
{'id': 0, 
 'gender': 'Administração/Finanças', 
},
{'id':1,
 'gender':'Finanças'
},
{'id':2,
 'gender': 'Psicologia'
 }
 ]

# Função que compara o id do dicionário gender_book com o id do dicionário books
def equal(book_id):
    for gender_info in gender_book:
        if gender_info['id'] == book_id:
            return gender_info
    return None

# Adiciona o genêro no dicionário books
for book_id in books_id:
    book_info = get_book(book_id)
    gender_info = equal(book_id)
    
    if book_info:
        if gender_info:
            book_info['gender'] = gender_info['gender']
        else:
            print(f'Nenhum gênero encontrado para o ID {book_id}')
            
        print('\n')
    else:
        print(f'Nenhum livro encontrado para o ID do arquivo Books.csv')


# --------------------------------- LOAD ---------------------------------

print(books)



