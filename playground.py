from pyspark.sql import SparkSession
from pyspark.sql.functions import sum

# Create the Spark session
spark = SparkSession.builder \
    .appName("MyApp") \
    .config("spark.jars", "/home/jovyan/data/mysql-connector-j-8.3.0.jar,/home/jovyan/data/postgresql-42.7.1.jar") \
    .getOrCreate()

# Connectivity details for the source database, MySQL
url = "jdbc:mysql://mysql:3306/masterclass"
properties = {
    "user": "mysqluser",
    "password": "mysqlpw",
    "driver": "com.mysql.jdbc.Driver"
}

# Read the order_items and products tables as data frames
df1 = spark.read.jdbc(url,"order_items",properties=properties)
df2 = spark.read.jdbc(url,"products",properties=properties)

# Inner join two data frames based on the product_id
joined_df = df1.join(df2,df1.product_id==df2.product_id,"inner").select(df2.product_id,df2.product_name,df1.total_price,df1.quantity)
# In the joined dataframe, aggregate the quantity sold by product_id and compute the total_qty. Store the final result in a new data frame
final_df = joined_df.groupBy("product_id","product_name").agg(sum("quantity").alias("total_qty")).sort("total_qty",ascending=False)

# Connectivity details for the target database, Postgres
url = "jdbc:postgresql://postgres:5432/masterclass"
properties = {
    "user": "postgresuser",
    "password": "postgrespw",
    "driver": "org.postgresql.Driver"
}
table_name = "top_selling_products"

# Finally, write the resulting data frame as a table, top_selling_product, into the target database.
final_df.write.jdbc(url, table_name, properties=properties)
