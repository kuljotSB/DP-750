from pyspark import pipelines as dp
from pyspark.sql.functions import sum, avg, count

# creating the "city by category revenue" table in the Gold schema
@dp.table(name="retail_job_lab.gold.city_category_revenue")
def city_category_revenue():

    df = dp.read("retail_job_lab.silver.transactions_enriched")

    return (
        df.groupBy("city", "category")
        .agg(sum("total_amount").alias("total_revenue"))
    )


# creating the "store performance" table in the Gold Schema
@dp.table(name="retail_job_lab.gold.store_performance")
def store_performance():

    df = dp.read("retail_job_lab.silver.transactions_enriched")

    return (
        df.groupBy("store_name")
        .agg(
            sum("total_amount").alias("total_revenue"),
            avg("total_amount").alias("avg_order_value"),
            count("*").alias("total_transactions")
        )
    )


# creating the "revenue by state" table in the Gold Schema
@dp.table(name="retail_job_lab.gold.state_revenue")
def state_revenue():

    df = dp.read("retail_job_lab.silver.transactions_enriched")

    return (
        df.groupBy("state")
        .agg(sum("total_amount").alias("total_revenue"))
    )