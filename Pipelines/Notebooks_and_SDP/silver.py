from pyspark import pipelines as dp
from pyspark.sql.functions import col

# creating the "transactions" table in the Silver schema
@dp.table(
    name="transactions_clean",
    catalog="retail_job_lab",
    schema="silver"
)
def transactions_clean():

    return (
        dp.read("transactions_bronze")
        .filter(col("status") == "Completed")
        .dropna(subset=["price_usd"])
        .withColumn("quantity", col("quantity").cast("int"))
        .withColumn("price_usd", col("price_usd").cast("double"))
        .withColumn("total_amount", col("quantity") * col("price_usd"))
    )


# creating the "enriched transactions" table in the Silver schema
@dp.table(
    name="transactions_enriched",
    catalog="retail_job_lab",
    schema="silver"
)
def transactions_enriched():

    stores = dp.read("stores_bronze").drop("city", "state")
    products = dp.read("products_bronze")

    return (
        dp.read("transactions_clean")
        .join(stores, "store_id", "left")
        .join(products, "product_id", "left")
    )