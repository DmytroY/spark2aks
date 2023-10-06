from pyspark.sql import SparkSession
from src.config import acc, key, container

if __name__ == "__main__":
    spark = SparkSession.builder.appName("jobtest").getOrCreate()

    spark.conf.set(f"fs.azure.account.key.{acc}.blob.core.windows.net", key)
    url = f"wasbs://{container}@{acc}.blob.core.windows.net"

    # extract
    path = url + "/hotels"
    df = spark.read.csv(path,
            header=True,
            nullValue="NA",
            inferSchema=True)
    # transform
    df1 = df.filter(df.Country == "US")
    df1.show()

    #load
    path = url + "/output"
    df1.write.option("header", True).csv(path)

    spark.stop()
    