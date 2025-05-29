import pymysql
# import cryptography
# DB_HOST = "149.50.148.48"
# DB_USER = "usuario_remoto"
# DB_PASSWORD = "Territerri%%101"
# DB_NAME = "Detenidos"

DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "rootmichelo"
DB_NAME = "Detenidos"


async def get_connection():
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        print("✅ Conexión exitosa")
        return connection
    except Exception as e:  # 👈 Usamos una excepción general para capturar TODO
        print("❌ Error general al conectar a la base de datos:")
        print(f"Tipo: {type(e).__name__}")
        print(f"Detalle: {e}")
        return None
