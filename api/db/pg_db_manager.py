import psycopg2
import psycopg2.extras
from api.db import pg_connection

from api.resources.candidato.model import Candidato


def insert_candidato(nome, idade, cidade, estado, area, subarea, tags, email, telefone, linkedin="0", github="0",
                     filecontent="", filetype="", filename=""):
    try:
        query = """
            insert into candidato (nome, idade, cidade, estado, area, subarea, tags, email, telefone, linkedin, github, filecontent, filetype, filename, status)
            values ('{nome}', '{idade}', '{cidade}', '{estado}', '{area}', '{subarea}', '{tags}', '{email}',
                    '{telefone}', '{linkedin}', '{github}', '{filecontent}', '{filetype}', '{filename}', 1);
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
                                    github=github,
                                    filecontent=filecontent,
                                    filetype=filetype,
                                    filename=filename))
        return True
    except Exception as e:
        print(str(e))
        return False
    finally:
        conn.commit()
        conn.close()


def update_candidato_status(id: int, status: int, obs):
    query_status = """
                UPDATE candidato SET status = {status} where id = {id};
            """

    query_obs = """
                INSERT INTO 
                        candidato_obs (candidato_id, obs)
                VALUES 
                    ({id}, '{obs}');
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


def update_candidato(candidato):
    try:
        query = """
            UPDATE candidato SET nome = '{nome}', idade = {idade}, cidade = '{cidade}', estado = '{estado}', area = '{area}', subarea = '{subarea}', email = '{email}', telefone = '{telefone}', linkedin = '{linkedin}', github = '{github}'
            WHERE id = {id};
        """
        conn = pg_connection.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query.format(id=candidato.id,
                                    nome=candidato.nome,
                                    idade=candidato.idade,
                                    cidade=candidato.cidade,
                                    estado=candidato.estado,
                                    area=candidato.area,
                                    subarea=candidato.subarea,
                                    email=candidato.email,
                                    telefone=candidato.telefone,
                                    linkedin=candidato.linkedin,
                                    github=candidato.github))
        return True
    except Exception as e:
        print(str(e))
        return False
    finally:
        conn.commit()
        conn.close()


def select_candidatos():
    try:
        conn = pg_connection.get_db_connection()

        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute("SELECT * FROM candidato;")

        candidatos = []

        for row in cursor:
            candidato = map_candidato(row)
            candidatos.append(candidato)

        return candidatos
    except Exception as e:
        print(str(e))
    finally:
        cursor.close()
        conn.close()


def select_candidato_by_id(candidato_id):
    try:
        conn = pg_connection.get_db_connection()

        query = "SELECT * FROM candidato WHERE id = {id};"

        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query.format(id=candidato_id))

        row = cursor.fetchone()
        if row is None:
            return None

        candidato = map_candidato(row)

        return candidato
    except Exception as e:
        print(str(e))
    finally:
        cursor.close()
        conn.close()


def map_candidato(row):
    candidato = Candidato()
    candidato.id = row['id']
    candidato.nome = row['nome'].strip()
    candidato.email = row['email'].strip()
    candidato.idade = row['idade']
    candidato.telefone = row['telefone'].strip()
    candidato.linkedin = row['linkedin'].strip()
    candidato.github = row['github'].strip()
    candidato.cidade = row['cidade'].strip()
    candidato.estado = row['estado'].strip()
    candidato.area = row['area'].strip()
    candidato.subarea = row['subarea'].strip()
    candidato.status = row['status']
    candidato.tags = row['tags'].strip()
    return candidato


def select_candidato_obs(candidato_id):
    try:
        conn = pg_connection.get_db_connection()

        query = "SELECT * FROM candidato_obs WHERE candidato_id = {id};"

        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query.format(id=candidato_id))

        obs_list = []

        for row in cursor:
            obs_list.append(row['obs'].strip())

        return obs_list
    except Exception as e:
        print(str(e))
    finally:
        cursor.close()
        conn.close()
