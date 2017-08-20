import psycopg2
import psycopg2.extras
from api.db import pg_connection

from api.resources.candidato.model import Candidato

import json

def insert_candidato(nome, idade, cidade, estado, area, subarea, tags, email, telefone, linkedin="0", github="0",
                     filecontent="", filetype="", filename="", responsavel=""):
    try:
        query = """
            INSERT INTO candidato (nome, idade, cidade, estado, area, subarea, tags, email, telefone, linkedin, github, filecontent, filetype, filename, responsavel, status)
            VALUES ('{nome}', '{idade}', '{cidade}', '{estado}', '{area}', '{subarea}', '{tags}', '{email}',
            '{telefone}', '{linkedin}', '{github}', '{filecontent}', '{filetype}', '{filename}', '{responsavel}', 1)
            RETURNING id;
        """

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
                                    github=github,
                                    filecontent=filecontent,
                                    filetype=filetype,
                                    filename=filename,
                                    responsavel=responsavel)

        conn = pg_connection.get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query)
                                    
        id_candidato = cursor.fetchone()[0]

        return id_candidato
    except Exception as e:
        print(str(e))

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
            UPDATE candidato SET nome = '{nome}', idade = {idade}, cidade = '{cidade}', estado = '{estado}', area = '{area}', subarea = '{subarea}', email = '{email}', telefone = '{telefone}', linkedin = '{linkedin}', github = '{github}', responsavel = '{responsavel}'
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
                                    github=candidato.github,
                                    responsavel=candidato.responsavel))
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

        query = """
            SELECT id, nome, idade, cidade, estado, area, subarea, tags, email, telefone, linkedin, github, responsavel, status FROM candidato;
        """

        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query)

        candidatos = [ row for row in cursor ]

        query2 = """
            SELECT candidato_id, array_to_json(array_agg(obs)) as list_obs FROM candidato_obs GROUP BY candidato_id;
        """

        cursor2 = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor2.execute(query2)

        obs_dict = { row["candidato_id"]: row for row in cursor2 }

        new_candidatos = []

        for candidato in candidatos:
            list_obs = obs_dict.get(candidato["id"], { "list_obs": [] })["list_obs"]

            new_candidato = dict(candidato)
            new_candidato["obs"] = list_obs
            new_candidatos.append(new_candidato)

        return new_candidatos
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
    candidato.responsavel = row['responsavel']
    candidato.filename = row['filename']
    candidato.filetype = row['filetype']
    candidato.filecontent = row['filecontent']
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
def insert_linkback(hash_candidato, id_candidato):
    try:
        conn = pg_connection.get_db_connection()

        query = """
            INSERT INTO linkback (id_candidato, hash, used) 
            VALUES ('{id}', '{hash}', FALSE);
        """

        cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        cursor.execute(query.format(id=id_candidato, hash=hash_candidato))

    except Exception as e:
        print(str(e))
    finally:
        cursor.close()
        conn.close()