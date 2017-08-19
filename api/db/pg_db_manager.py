from api.db import pg_connection


def insert_candidato(nome, idade, cidade, estado, area, subarea, tags, email, telefone, linkedin="0", github="0"):
    try:
        query = """
            insert into candidato (nome, idade, cidade, estado, area, subarea, tags, email, telefone, linkedin, github)
            values ('{nome}', '{idade}', '{cidade}', '{estado}', '{area}', '{subarea}', '{tags}', '{email}', '{telefone}', '{linkedin}', '{github}' );
        """
        conn = pg_connection.get_db_connection()
        cursor = conn.cursor()
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


def update_candidato_status(id: int, status: int, obs):
    query_status = """
                UPDATE candidato SET status = {status} where = {id};
            """

    query_obs = """
                INSERT INTO 
                        candidato_obs (candidato_id, obs)
                VALUES 
                    ({id}, "Novo status:{status}, {obs}");
            """
    try:
        conn = pg_connection.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query_status.format(id=id, status=status))

        cursor_obs = conn.cursor()
        cursor_obs.execute(query_obs.format(id=id, status=status, obs=obs))
        return True
    except Exception as e:
        print(str(e))
        return False
    finally:
        conn.commit()
        conn.close()
