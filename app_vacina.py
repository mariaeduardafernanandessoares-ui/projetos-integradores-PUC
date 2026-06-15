import mysql.connector

def obter_conexao():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="senha",
        database="controle_vacinas_goias"
    )

def salvar_no_banco(paciente_estrutura):
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        comando_sql = """
        INSERT INTO Pacientes (nome, idade, escolaridade, regiao_moradia) 
        VALUES (%s, %s, %s, %s);
        """
        valores = (
            paciente_estrutura["nome"],
            paciente_estrutura["idade"],
            paciente_estrutura["escolaridade"],
            paciente_estrutura["regiao_moradia"]
        )
        cursor.execute(comando_sql, valores)
        conexao.commit()
        print(f"\n[Sucesso] {paciente_estrutura['nome']} foi salvo no MySQL!")
        cursor.close()
        conexao.close()
    except mysql.connector.Error as erro:
        print(f"Erro ao salvar no banco de dados: {erro}")

def gerar_relatorios_analiticos():
    """
    Esta função executa as queries analíticas (JOINs) no MySQL
    e exibe os cruzamentos estatísticos exigidos pelo projeto.
    """
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        
        print("\n=============================================")
        print("      RELATÓRIO ESTATÍSTICO DE BIG DATA      ")
        print("=============================================")
        
        # 1. CORRELAÇÃO: Vacinado x Doente (Eficácia Clínica)
        print("\n[1] Análise de Impacto: Vacinados vs Gravidade de Casos")
        query_eficacia = """
        SELECT p.nome, IFNULL(v.nome_vacina, 'NÃO VACINADO') AS status_vacina, 
               IFNULL(d.nome_doenca, 'Sem registo') AS doenca, IFNULL(rc.gravidade, '-') AS gravidade
        FROM Pacientes p
        LEFT JOIN Aplicacoes_Vacinas av ON p.id_paciente = av.id_paciente
        LEFT JOIN Vacinas v ON av.id_vacina = v.id_vacina
        LEFT JOIN Registros_Casos rc ON p.id_paciente = rc.id_paciente
        LEFT JOIN Doencas d ON rc.id_doenca = d.id_doenca;
        """
        cursor.execute(query_eficacia)
        for (nome, vacina, doenca, gravidade) in cursor.fetchall():
            print(f"Paciente: {nome:<15} | Vacina: {vacina:<15} | Doença: {doenca:<12} | Gravidade: {gravidade}")
            
        # 2. CORRELAÇÃO: Vacinado x Região (Distribuição Geográfica)
        print("\n[2] Cobertura Vacinal por Região de Moradia")
        query_regiao = """
        SELECT p.regiao_moradia, COUNT(av.id_aplicacao) AS total_vacinas
        FROM Pacientes p
        LEFT JOIN Aplicacoes_Vacinas av ON p.id_paciente = av.id_paciente
        GROUP BY p.regiao_moradia;
        """
        cursor.execute(query_regiao)
        for (regiao, total) in cursor.fetchall():
            print(f"Região/Município: {regiao:<30} | Total de Doses Aplicadas: {total}")

        # 3. CORRELAÇÃO: Vacinado x Escolaridade
        print("\n[3] Adesão Vacinal por Nível de Escolaridade")
        query_escolaridade = """
        SELECT p.escolaridade, COUNT(av.id_aplicacao) AS total_vacinas
        FROM Pacientes p
        LEFT JOIN Aplicacoes_Vacinas av ON p.id_paciente = av.id_paciente
        GROUP BY p.escolaridade;
        """
        cursor.execute(query_escolaridade)
        for (escolaridade, total) in cursor.fetchall():
            print(f"Escolaridade: {escolaridade:<25} | Total de Doses Aplicadas: {total}")

        cursor.close()
        conexao.close()
    except mysql.connector.Error as erro:
        print(f"Erro ao gerar relatórios: {erro}")

def menu_principal():
    while True:
        print("\n=============================================")
        print("      SISTEMA DE MONITORIZAÇÃO - GOIÁS       ")
        print("=============================================")
        print("1. Cadastrar Novo Paciente (Entrada -> Memória -> Banco)")
        print("2. Gerar Relatórios Analíticos (Correlações Big Data)")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome do paciente: ")
            idade = int(input("Idade do paciente: "))
            escolaridade = input("Escolaridade: ")
            regiao = input("Região/Bairro de moradia: ")
            
            # Estrutura de dados em memória
            paciente_dict = {
                "nome": nome,
                "idade": idade,
                "escolaridade": escolaridade,
                "regiao_moradia": regiao
            }
            salvar_no_banco(paciente_dict)
            
        elif opcao == '2':
            gerar_relatorios_analiticos()
        elif opcao == '3':
            print("\nSistema encerrado.")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu_principal()