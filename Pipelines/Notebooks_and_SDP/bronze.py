from pyspark import pipelines as dp

# create the "transactions" table in the Bronze Schema
@dp.table(name="retail_job_lab.bronze.transactions_bronze")
def transactions_bronze():
    return spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load("/Volumes/retail_job_lab/bronze/raw_files/transactions.csv")


# create the "stores" table in the Bronze schema
@dp.table(name="retail_job_lab.bronze.stores_bronze")
def stores_bronze():
    return spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load("/Volumes/retail_job_lab/bronze/raw_files/stores.csv")

# create the "products" table in the Bronze schema
@dp.table(name="retail_job_lab.bronze.products_bronze")
def products_bronze():
    return spark.read.format("csv") \
        .option("header", "true") \
        .option("inferSchema", "true") \
        .load("/Volumes/retail_job_lab/bronze/raw_files/products.csv")