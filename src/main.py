from pyspark.sql import SparkSession


if __name__ == "__main__":
    spark = SparkSession.builder.appName("jobtest").getOrCreate()

    source_data_path = "abfs://data@styakovd1westeurope.dfs.core.windows.net"
    output_data_path = "abfs://data@styakovd1westeurope.dfs.core.windows.net/output"

    # extract
    df = spark.read.csv(source_data_path + "/hotels",
            header=True,
            nullValue="NA",
            inferSchema=True)
    # transform
    df1 = df.filter(df.Country == "US")
    df1.show()

    #load
    df1.write.option("header", True).csv(output_data_path)

    spark.stop()
    