import os
import PyPDF2
import re

notas_geradas = []

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the working directory
os.chdir(current_dir)

# Define the folder path that contains the PDF files
pasta = os.path.join(current_dir)

# Iterar sobre cada arquivo na pasta com a extensão .pdf
for filename in os.listdir(pasta):
    if filename.endswith('.pdf'):
        # Abre o arquivo PDF
        with open(os.path.join(pasta, filename), 'rb') as pdf_file:
            # Criar um objeto PDF Reader
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Obter o número de páginas
            num_pages = len(pdf_reader.pages)

            # Iterar através de cada página
            for page in range(num_pages):
                # Obter o conteúdo de texto da página
                page_text = pdf_reader.pages[page].extract_text()
                
            
            pdf_file.close()            
            
            
            nome = page_text.splitlines()[5]
            n_nota = page_text.splitlines()[3]
            n_nota = re.sub(r'\D', '', n_nota) 
          
            
            if nome == "IDENTIFICAÇÃO DO EMITENTE":
               nome = page_text.splitlines()[6]
           
            try:
                
                new_filename = nome + " " + "NF" + " " + n_nota + " " + ".pdf"
                os.rename(os.path.join(pasta, filename), os.path.join(pasta, new_filename))
            
            except Exception as e:
                print(f"Error renaming file {filename}: {str(e)}")

print(notas_geradas)

# Obtenha a nota inicial e final do usuário
nota_inicial = int(input("Digite a nota inicial: "))
nota_final = int(input("Digite a nota final: "))

# Crie a lista de números começando em nota_inicial e terminando em nota_final
nota_totais = list(range(nota_inicial, nota_final + 1))

# Verifique quais números estão faltando
numeros_ausentes = [numero for numero in nota_totais if numero not in notas_geradas]

# Exiba os números ausentes
if numeros_ausentes:
    print("Números ausentes na sequência:", numeros_ausentes)
else:
    print("Nenhum número ausente na sequência")

sair = str(input("Digite qualquer tecla para sair"))

