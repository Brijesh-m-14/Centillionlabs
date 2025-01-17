from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

spark = SparkSession.builder.appName("load-csv").master("local[*]").getOrCreate()

def load_stock(symbol:str):
    df = spark.read\
        .option("header", True)\
        .csv("data/AAPL.csv")

    return df.select(
        df['Date'].cast(DateType()).alias("date"),
        df['Open'].cast(DoubleType()).alias("open"),
        df['Close'].cast(DoubleType()).alias("close")
    )

df = load_stock("AAPL")

date_2 = date_add(df['Date'],2)
date_str = date_2.cast(StringType())
concat_col = concat(date_str,lit("Welcome"))

df.select(df['Date'],concat_col.alias("transformed")).show(truncate=False)

'''df.show()
df.printSchema()'''
'''
df.select(column1, column2, column3).show()

df.select("Date", "Close", "Open").show()'''

'''date_str = df['Date'].cast(StringType()).alias("date")

df.select(df['Date'],date_str).show()'''