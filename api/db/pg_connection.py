import psycopg2


def get_db_connection():
    conn_string = "host='ec2-23-23-244-83.compute-1.amazonaws.com'" \
                  " dbname='dd3cnd4u4c3vqr' user='yfympzzvvhmvtg'" \
                  " password='69fd0e01d4d5887b0a3e031044a5f7cb87df2abcae7b85d658b8867a16161529'" \
                  " port='5432' "
    conn = psycopg2.connect(conn_string)
    return conn

if __name__ == '__main__':
    conn = get_db_connection()