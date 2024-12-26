public:: true

- Библиотека #Python для работы с #Spark
- Импорт pySpark
  ```python
  from pyspark.sql import SparkSession
  from pyspark.sql.functions import split, col
  ```
- Создание сессии 
  ```python
  spark = SparkSession.builder.appName('PySpark').getOrCreate()
  ```
- Создание датаФрейма spark на основе датаФрейма #pandas
  ```python
  dfSpark = spark.createDataFrame(dfPandas)
  ```
- Создание #sparkContext
  ```python
  sc = spark.sparkContext
  ```
- Генерация #RDD объекта
  ```python
  rdd = sc.parallelize(data)
  ```
- Генерируем коллекцию( #list ) из #RDD
  ```python
  rdd.collect()
  ```
- Фильтр. выбрать все значения, которые в квадрате больше 1000
  ```python
  rdd.filter(lambda x: x**2 > 1000)
  ```
- Преобразование #rdd
  ```python
  rdd.map(lambda  x: x * 2)
  ```
- Объединить 2 коллекции
  ```python
  rdd1.union(rdd2)
  ```
- Вывести количество элементов
  ```python
  rdd.count()
  ```
- Сохранить #rdd в текстовый файл (партициями)
  ```python
  rdd.saveAsTextFile('data')
  ```
- Узнать количество партиций, на которые разбит rdd
  ```python
  rdd.getNumPartitions()
  ```
- Показать количество партиций в #df 
  ```python
  df.rdd.getNumPartitions()
  ```
- Изменить количество партиций
  ```python
  rdd.repartition(num)
  ```
- Уменьшение количества партиций до 1
  ```python
  rdd.coalesce(1)
  ```
- Из датафрема в #RDD
  ```python
  df.rdd
  ```
- Описание схемы #df
  ```python
  df.shema
  ```
- Показать колонки
  ```python
  df.columns
  ```
- Показать тип колонок
  ```python
  df.dtypes
  ```
- Основные метрики по данным(среднее, максимальное и т д )
  ```python
  df.describe()
  ```
- Основные метрики по определенным колонкам
  ```python
  df.describe(['column_name', 'column_name'])
  ```
- Выбор определенной колонки
  ```python
  df[['column_name']]
  ```
- Группировка по колонке
  ```python
  df.groupBy('column_name')
  ```
- Количество по значениям в колонке
  ```python
  df.groupBy('column_name').count()
  ```
- Создаёт новую колонку. на основе другой, с помощью функции #split
  ```python
  df.withColumn('name_new_column', split(col('name_column'), ' ')[0])
  ```
- Удаление колонки
  ```python
  df.drop('column_name')
  ```
- Показывает корреляцию между столбцами
  ```python
  df.corr('column_name_1', 'column_name_2')
  ```
- Собирает коллекцию из выбранных колонок
  ```python
  df[['column_name_1', 'column_name_2']].collect()
  ```
- Показывает статистику таблицы
  ```python
  df.summary()
  ```
- Конкатинация столбцов
  ```python
  df.select(concat('id', 'name')).show()
  ```
- Добавление своего в конкатинацию
  ```python
  df.select(concat('id', lit(': '), 'name')).show()
  ```
- Разбить колонку на массив и достать первый элемент
  ```python
  df.select(split('name', 'n').alias('array')).select(col('array')[0]).show()
  ```
- Запись #df в #csv
  ```python
  df.coalesce(1).write.csv('name')
  ```
- Запись #df в #json
  id:: 66f060e1-14d1-4242-86b5-58194a9265db
  ```python
  df.coalesce(1).write.json('name')
  ```
- Запись #df в #parquet
  ```python
  df.coalesce(1).write.parquet('name')
  ```
- Чтение #parquet 
  ```python
  spark.read.parquet('name')
  ```
- Чтение #csv 
  ```python
  spark.read.option('header', 'true').csv('file.csv')
  ```
- Выбрать уникальные значения в колонке
  ```python
  df[['col_name']].distinct()
  ```
- Выбрать строки в которых colName пустой
  ```python
  df.where(col('colName')).isNull()
  ```
- Посчитать среднее в колонке
  ```python
  df.select(avg(col('col_name')))
  ```
- Поменять пустые значения в колонке на value
  ```python
  df.fillna({'col_name': value})
  ```
- Создание df на основе RDD:
  ```python
  persons = [(1, 'Alex'), (2, 'Anna'), (3, 'Denis'), (4, 'Max')]
  rdd = sc.parallelize(persons)
  df = rdd.toDF(['id', 'name'])
  ```
-
- ## Готовый пример
	- Класс для работы с pyspark
	  ```python
	  import os
	  import subprocess
	  import sys
	  import json
	  from spark_tables import tables
	  
	  class my_spark:
	      """Класс для работы со спарком"""
	      
	      def __init__(self, script_name: str, type_config: str = 'full') -> None:
	          
	          self.password_login_json_path = '/home/18398782_omega-sbrf-ru/notebooks/.keys/password_login.json'
	          self.spark_ktab_path = '/home/18398782_omega-sbrf-ru/notebooks/.keys/sc_keytab.keytab'
	          
	          self.username = '!Strometskiy'
	          self.script_name = script_name
	          self.type_config = type_config
	          self.tables = tables
	          
	          with open(self.password_login_json_path) as f:
	              self.spark_login = json.load(f)['spark']['login']
	              '''
	                  Формат json, который лежит в 
	                  {
	                      "spark": {
	                          "login": "18398782_omega-sbrf-ru@DF.SBRF.RU",
	                          "password": ""
	                      },
	                      "omega": {
	                          "login": "18398782",
	                          "passcword": ""
	                      }
	                  }
	              '''
	              
	          self.kinit()
	  
	          sys.path.insert(0, '/usr/sdp/current/spark3-client/python/')
	          sys.path.insert(0, '/usr/sdp/current/spark3-client/python/lib/py4j-0.10.9.3-src.zip')
	          os.environ['SPARK_MAJOR_VERSION'] = '3'
	          os.environ['SPARK_HOME'] = '/usr/sdp/current/spark3-client'
	          python_path = sys.executable
	          os.environ['PYSPARK_DRIVER_PYTHON'] = python_path
	          os.environ['PYSPARK_PYTHON'] = python_path
	          os.environ['PYSPARK_DRIVER'] = python_path
	          os.environ['LD_LIBRARY_PATH'] = '/opt/python/virtualenv/jupyter/lib'
	  
	          from pyspark.sql import functions as func
	          from pyspark import SparkContext, SparkConf, HiveContext, SQLContext 
	          from pyspark.sql import SparkSession
	          
	          try: 
	              self.spark = (SparkSession
	                  .builder
	                  .appName('{}: {}'.format(self.username, self.script_name))
	                  .master("yarn")
	                  .config('spark.executor.cores', '12' if type_config == 'full' else '6')
	                  .config('spark.executor.memory', '20G' if type_config == 'full' else '10G')
	                  .config('spark.executor.memoryOverhead', '10g' if type_config == 'full' else '5g')
	                  .config('spark.driver.memory', '20G' if type_config == 'full' else '10G')
	                  .config('spark.driver.maxResultSize', '40G' if type_config == 'full' else '20G')
	                  .config('spark.hive.mapred.supports.subdirectories', 'true')
	                  .config('spark.hadoop.mapreduce.input.fileinputformat.input.dir.recursive', 'true')
	                  # .config('spark.exclude.nodes', 'pklos-nimb00333.labiac.df.sbrf.ru')
	                  .config('spark.shuffle.service.enabled', 'true')
	                  .config('spark.dynamicAllocation.enabled', 'true')
	                  .config('spark.dynamicAllocation.executorIdleTimeout', '120s')
	                  .config('spark.dynamicAllocation.cachedExecutorIdleTimeout', '600s')
	                  .config('spark.dynamicAllocation.initialExecutors', '6')
	                  .config('spark.dynamicAllocation.minExecutors', '1')
	                  .config('spark.dynamicAllocation.maxExecutors', '10')
	                  .config('mapred.input.dir.recursive', 'true')
	                  .config('spark.port.maxRetries', '150')
	                  .config('spark.sql.parquet.binaryAsString', 'true')
	                  .config('spark.sql.hive.convertMetastoreParquet', 'true')
	                  .config('spark.sql.crossJoin.enabled', 'true')
	                  .config('spark.hadoop.hive.mapred.input.dir.recursive', 'true')
	                  .config('spark.sql.hive.convertMetastoreParquet', 'false')
	                  .config('spark.sql.broadcastTimeout', '36000')
	                  .config('spark.kerberos.access.hadoopFileSystems','hdfs://hdfsgw:8020,hdfs://SDP-16791871-omega-sbrf-ru-RB-CC-Bots-77f255:8020,hdfs://arnsdpsbx:8020')
	                  .config('spark.kerberos.keytab', self.spark_ktab_path)
	                  .config('spark.kerberos.principal', self.spark_login)
	                  .getOrCreate())
	              self.spark.sparkContext.setLogLevel('ERROR')
	          except Exception as e:
	              print (str(e)) 
	  
	          
	      def kinit(self) -> None:
	          """Делает kinit"""
	          subprocess.run(['kinit', '-kt', self.spark_ktab_path, self.spark_login])
	          
	      def get_table(self, my_table_name: str) -> 'pyspark.sql.dataframe.DataFrame':
	          """Возвращает путь до таблицы"""
	          return self.spark.sql('''SELECT * FROM {}'''.format(self.tables[my_table_name]))
	      
	      def get_tables_dict(self, table_name: str = None) -> dict:
	          """Возвращает маппинг таблиц"""
	          
	          if table_name is not None and table_name in self.tables:
	              return {table_name: self.tables[table_name]}
	          
	          return self.tables
	  ```
	  
	  Пример оконки
	  ```python
	  # Найти строку с минимальным временем
	  
	  from pyspark.sql import Window
	  
	  frame.select(
	      select_col_1,
	      select_col_2,
	      ...
	      select_col_n,
	      row_number().over(Window.partitionBy(column_partition).orderBy('sort_column_name')).alias('num_line')
	  ).filter(col('num_line') == 1)
	  ```
	  
	  Агрегация
	  ```python
	  # array_agg и count в spark
	  from pyspark.sql.functions import collect_set, count
	  
	  frame.groupBy(column_partition).agg(collect_set('column_name').alias('name_agg(set)'), count('column_name').alias('name_agg(count)'))
	  ```
	  
	  kinit
	  ```python
	  import subprocess
	  subprocess.run(['kinit', '-kt', '/home/18398782_omega-sbrf-ru/notebooks/.keys/sc_keytab.keytab', '18398782_omega-sbrf-ru@DF.SBRF.RU'])
	  
	  import os
	  os.system("kinit -kt /home/18398782_omega-sbrf-ru/notebooks/.keys/gp_keytab 18398782@OMEGA.SBRF.RU")
	  ```
	  
	  Показать таблицы ЛД
	  ```python
	  sql_spark_context.spark.sql('SHOW DATABASES').toPandas()
	  sql_spark_context.spark.sql('SHOW TABLES IN prx_features_selfservice_sbszh_selfservice_sbszh').toPandas()
	  ```
	  
	  Удаление таблицы
	  ```python
	  sql_spark_context.sqlContext.sql('''DROP TABLE default.maks_click''')
	  ```
	  
	  Запись таблицы
	  ```python
	  frame.write.saveAsTable('default.maks_sms', mode='overwrite', format='parquet')
	  ```
	  
	  Создание спарк таблицы из пандас
	  ```python
	  schema = StructType(fields=[
	      StructField('epk_id', StringType()),
	      StructField('prd', StringType()),
	      StructField('s_prd', StringType()),
	      StructField('subj', StringType()),
	      StructField('s_subj', StringType()),
	      StructField('chnl', StringType()),
	      StructField('created', StringType()),
	      StructField('edu_id', StringType())
	  ])
	  
	  spark_PPRB = sql_spark_context.spark.createDataFrame(thems_PPRB.astype(str), schema=schema)
	  ```
-
-