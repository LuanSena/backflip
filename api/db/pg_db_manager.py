from api.db import pg_connection


def insert_candidato(nome, idade, cidade, estado, area, subarea, tags, email, telefone, linkedin="0", github="0"):
    try:
        query = """
            insert into candidato (nome, idade, cidade, estado, area, subarea, tags, email, telefone, linkedin, github)
            values ('{nome}', '{idade}', '{cidade}', '{estado}', '{area}', '{subarea}', '{tags}', '{email}', '{telefone}', '{linkedin}', '{github}' );
        """
        conn = pg_connection.get_db_connection()
        cursor = conn.cursor()
        query = query.format(nome=nome,
                                    idade=idade,
                                    cidade=cidade,
                                    estado=estado,
                                    area=area,
                                    subarea=subarea,
                                    tags=tags,
                                    email=email,
                                    telefone=telefone,
                                    linkedin=linkedin,
                                    github=github)
        cursor.execute(query.format(nome=nome,
                                    idade=idade,
                                    cidade=cidade,
                                    estado=estado,
                                    area=area,
                                    subarea=subarea,
                                    tags=tags,
                                    email=email,
                                    telefone=telefone,
                                    linkedin=linkedin,
                                    github=github))
        return True
    except Exception as e:
        print(str(e))
        return False
    finally:
        conn.commit()
        conn.close()
