import random
from pymongo import MongoClient

# Conexão com o MongoDB (use suas credenciais)
client = MongoClient("mongodb+srv://garibaldimatheus8:fatec123@clusterprofessor.nbs2qed.mongodb.net/")
db = client["test"]
collection = db["professors"]

# Dados possíveis
titulacoes = ["Especialista", "Mestre", "Doutor", "Pós-Doutor", "Pós-Doutora"]
pes = ["PES I", "PES II", "PES III"]
referencia_letra = ["A", "B", "C", "D", "E", "F", "G", "H"]
courses_ids = ["180", "181", "182"]
status_atividade = ["Ativo", "Inativo"]

# Lista de cidades reais do estado de São Paulo
cidades_sp = [
    "São Paulo", "Campinas", "Santos", "Sorocaba", "São José dos Campos", 
    "Ribeirão Preto", "Bauru", "Guarulhos", "Barueri", "Osasco", 
    "São Bernardo do Campo", "Diadema", "Jundiaí", "Marília", "Presidente Prudente"
]

# Lista de observações possíveis
observacoes = [
    "Pioneiro na área", "Especialista em IA", "Coordena projetos", "Professor visitante", "Líder em pesquisa",
    "Publicou artigos recentes", "Participa de conferências", "Inspira os alunos", "Pesquisador ativo",
    "Profissional renomado", "Consultor externo", "Autor de livros", "Referência acadêmica", 
    "Atua em projetos internacionais", "Reconhecido na área", "Desenvolve novos métodos de ensino", 
    "Forte atuação em extensão", "Promove inovação", "Atua em grupos de pesquisa", "Experiência internacional"
]

# Lista de nomes e sobrenomes reais para geração de professores
nomes = ["Carlos", "Mariana", "Ricardo", "Ana", "João", "Fernanda", "José", "Beatriz", "Gabriel", "Patrícia"]
sobrenomes = ["Silva", "Santos", "Oliveira", "Costa", "Pereira", "Almeida", "Ferreira", "Souza", "Gomes", "Ribeiro"]

# Função para gerar um professor fictício com dados reais
def gerar_professor():
    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)
    nome_completo = f"{nome} {sobrenome}"
    matricula_id = str(random.randint(10000, 99999))
    cidade = random.choice(cidades_sp)
    unidade_id = f"{random.randint(1, 999):03} - {cidade}"
    titulacao = random.choice(titulacoes)
    referencia = f"{random.choice(pes)} - {random.choice(referencia_letra)}"
    lattes = f"http://lattes.cnpq.br/{random.randint(1000000000000, 9999999999999)}"
    
    # Escolhendo de 1 a 3 cursos de forma aleatória
    num_cursos = random.randint(1, 3)
    courses_id = random.sample(courses_ids, num_cursos)
    
    status = random.choice(status_atividade)
    email = f"{nome.lower()}{sobrenome.lower()}@fatec.sp.gov.br"
    notes = random.choice(observacoes)

    return {
        "nome": nome_completo,
        "matriculaId": matricula_id,
        "unidadeId": unidade_id,
        "titulacao": titulacao,
        "referencia": referencia,
        "lattes": lattes,
        "coursesId": courses_id,  # Agora pode ter de 1 a 3 IDs de curso
        "statusAtividade": status,
        "email": email,
        "notes": notes
    }

# Gerar e inserir 10 professores fictícios
professores = [gerar_professor() for _ in range(3)]

# Inserindo no MongoDB
result = collection.insert_many(professores)

# Imprime os IDs dos documentos inseridos
print("Dados inseridos com sucesso. IDs:", result.inserted_ids)
