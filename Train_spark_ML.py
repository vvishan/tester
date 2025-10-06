from pyspark import SparkContext
from pyspark.sql import SparkSession
sc = SparkContext
spark = SparkSession.builder.appName("Test").getOrCreate()
df = spark.createDataFrame([(1,"Alice"),(2,"Bob")], ["id","name"])
df.show()