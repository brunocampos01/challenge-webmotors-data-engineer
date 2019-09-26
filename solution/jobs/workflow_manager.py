"""
etl_job.py
"""

import configparser

from pyspark.sql import Row
from pyspark.sql.functions import col
from pyspark.sql.functions import log
from pyspark.sql.functions import trim
from pyspark.sql.functions import split
from pyspark.sql.functions import lower
from pyspark.sql.functions import regexp_replace

from pyspark.sql.session import SparkSession

path_directory = os.path.dirname(os.path.abspath(__file__))
path_config = ''.join(path_directory + '../config/etl_config.ini')

config = configparser.ConfigParser()
config.read(path_config)

PATH_FILES = config['DOC']['PATH_FILES']
PATH_DICT = config['DOC']['PATH_DICT']
SPARK_CONFIG = config['SPARK']['SPARK_CONFIG']


class WorkflowManager(object):
    def __init__(self, spark_config, dataframe: 'Dataframe'):
        self.__spark = SparkSession \
            .builder \
            .config(spark_config) \
            .getOrCreate()

        self.__df = dataframe

    def __del__(self):
        self.__spark.stop()

    def data_cleansing(self, column_words: str) -> 'DataFrame':
        """Pre processing data

        Processing executed in function:
        - Lower case
        - Words start with letters or whitespace
        - Remove whitespaces into start and final words
        - Remove rows empty
        - Transform each row in list and split row by word

        :Args:
            :param column: column's name of Dataframe
        :Returns:
            :return: Dataframe with a word list in each row
        """
        self.__df = self.__df.withColumn(column_words,
                                         lower(col(column_words))) \
            .withColumn(column_words, regexp_replace(str=col(column_words),
                                                     pattern='[^a-z ]',
                                                     replacement='')) \
            .withColumn(column_words, trim(col(column_words))) \
            .filter(self.__df[column_words] != "") \
            .withColumn(column_words, split(column_words, ' '))

        return self

    def load_data(self, path_files):
        """
        Load data from text file format.

        :Args:
            :param path_files: directory where is documents
        Return:
            :return: Spark DataFrame.
        """
        return self.__spark.read.text(path_files)

    def persistence_data(self, path_to_storage: str, format: str, mode: str):
        """Persist word dict

        :Args:
            :param path_to_storage: the path
            :param format: the format used to save
            :param mode: operation when data already exists.

        :Returns:
            :return: a word dict storage
        """
        return self.__df.write.save(path=path_to_storage,
                                    format=format,
                                    mode=mode)

def main():
    """
    Workflow Manager ETL.
    """
    # execute ETL pipeline
    data = extract_data(spark)
    data_transformed = transform_data(data, config['steps_per_floor'])
    load_data(data_transformed)

    # log the success and terminate Spark application
    log.warn('test_etl_job is finished')
    spark.stop()
    return None


def create_test_data(spark, config):
    """Create test data.
    This function creates both both pre- and post- transformation data
    saved as Parquet files in tests/test_data. This will be used for
    unit tests as well as to load as part of the example ETL job.
    :return: None
    """
    # create example data from scratch
    local_records = [
        Row(id=1, first_name='Dan', second_name='Germain', floor=1),
        Row(id=2, first_name='Dan', second_name='Sommerville', floor=1),
        Row(id=3, first_name='Alex', second_name='Ioannides', floor=2),
        Row(id=4, first_name='Ken', second_name='Lai', floor=2),
        Row(id=5, first_name='Stu', second_name='White', floor=3),
        Row(id=6, first_name='Mark', second_name='Sweeting', floor=3),
        Row(id=7, first_name='Phil', second_name='Bird', floor=4),
        Row(id=8, first_name='Kim', second_name='Suter', floor=4)
    ]

    df = spark.createDataFrame(local_records)

    # write to Parquet file format
    (df
     .coalesce(1)
     .write
     .parquet('tests/test_data/employees', mode='overwrite'))

    # create transformed version of data
    df_tf = transform_data(df, config['steps_per_floor'])

    # write transformed version of data to Parquet
    (df_tf
     .coalesce(1)
     .write
     .parquet('tests/test_data/employees_report', mode='overwrite'))

    return None


# entry point for PySpark ETL application
if __name__ == '__main__':
    main()