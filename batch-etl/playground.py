from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("MyApp") \
    .config("spark.jars", "/home/jovyan/data/mysql-connector-j-8.3.0.jar,/home/jovyan/data/postgresql-42.7.1.jar") \
    .getOrCreate()

url = "jdbc:mysql://mysql:3306/masterclass"
properties = {
    "user": "mysqluser",
    "password": "mysqlpw",
    "driver": "com.mysql.jdbc.Driver"
}
table_name = "orders"

df = spark.read.jdbc(url, table_name, properties=properties)
df.show()

url = "jdbc:postgresql://postgres:5432/masterclass"
properties = {
    "user": "postgresuser",
    "password": "postgrespw",
    "driver": "org.postgresql.Driver"
}
table_name = "top_selling_products"

df_summary = spark.read.jdbc(url, table_name, properties=properties)
df_summary.show()