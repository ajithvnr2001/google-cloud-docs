---
url: https://docs.cloud.google.com/dataflow/docs/notebooks/dataframe_api_preprocessing/
title: Preprocessing with the Apache Beam DataFrames API \u00a0|\u00a0 Dataflow ML \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T12:47:17.913326+00:00
---

# Preprocessing with the Apache Beam DataFrames API  |  Dataflow ML  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/notebooks/dataframe_api_preprocessing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Preprocessing with the Apache Beam DataFrames API Stay organized with collections  Save and categorize content based on your preferences. 

[Pandas DataFrames](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html) is one of the most common tools used for data exploration and preprocessing. Pandas is popular because of its ease of use. It has intuitive methods to perform common analytical tasks and data preprocessing. 

[![](https://raw.githubusercontent.com/google/or-tools/main/tools/colab_32px.png)Run in Google Colab](https://colab.research.google.com/github/apache/beam/blob/master/examples/notebooks/beam-ml/dataframe_api_preprocessing.ipynb) |  [![](https://raw.githubusercontent.com/google/or-tools/main/tools/github_32px.png)View source on GitHub](https://github.com/apache/beam/blob/master/examples/notebooks/beam-ml/dataframe_api_preprocessing.ipynb) For rapid execution, Pandas loads all of the data into memory on a single machine (one node). This configuration works well when dealing with small-scale datasets. However, many projects involve datasets that are too big to fit in memory. These use cases generally require parallel data processing frameworks, such as Apache Beam. Beam DataFrames provide a Pandas-like API to declare and define Beam processing pipelines. It provides a familiar interface for machine learning practioners to build complex data-processing pipelines by only invoking standard pandas commands. To learn more about Apache Beam DataFrames, see the [Beam DataFrames overview](https://beam.apache.org/documentation/dsls/dataframes/overview) page.

## Overview

The goal of this example is to explore a dataset preprocessed with the Beam DataFrame API for machine learning model training. This example demonstrates the use of the Apache Beam DataFrames API to perform common data exploration as well as the preprocessing steps that are necessary to prepare your dataset for machine learning model training and inference. This example includes the following steps: 

  * Removing unwanted columns.
  * One-hot encoding categorical columns.
  * Normalizing numerical columns.

In this example, the first section demonstrates how to build and execute a pipeline locally using the interactive runner. The second section uses a distributed runner to demonstrate how to run the pipeline on the full dataset.

## Install Apache Beam

To explore the elements within a `PCollection`, install Apache Beam with the `interactive` component to use the Interactive runner. The DataFrames API methods invoked in this example are available in Apache Beam SDK versions 2.43 and later. Install the latest Apache Beam SDK version.
    
    
    !git clone https://github.com/apache/beam.git
    
    !cd beam/sdks/python && pip3 install -r build-requirements.txt 
    
    %pip install -e beam/sdks/python/.[interactive,gcp]
    

## Local exploration with the Interactive Beam runner

Use the [Interactive Beam](https://beam.apache.org/releases/pydoc/2.20.0/apache_beam.runners.interactive.interactive_beam.html) runner to explore and develop your pipeline. This runner allows you to test the code interactively, progressively building out the pipeline before deploying it on a distributed runner.  This section uses a subset of the original dataset, because the notebook instance has limited compute resources.

### Load the data

To read CSV files into DataFrames, Pandas has the [`pandas.read_csv`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html) function. This notebook uses the Beam [`beam.dataframe.io.read_csv`](https://beam.apache.org/releases/pydoc/current/apache_beam.dataframe.io.html#apache_beam.dataframe.io.read_csv) function, which emulates `pandas.read_csv`. The main difference is that the Beam function returns a deferred Beam DataFrame, whereas the Pandas function returns a standard DataFrame.
    
    
    import os
    
    import numpy as np
    import pandas as pd 
    import apache_beam as beam
    import apache_beam.runners.interactive.interactive_beam as ib
    from apache_beam import dataframe
    from apache_beam.runners.interactive.interactive_runner import InteractiveRunner
    from apache_beam.runners.dataflow import DataflowRunner
    
    # Available options: [sample_1000, sample_10000, sample_100000, full], where
    # sample contains the entire dataset (around 1000000 samples).
    
    source_csv_file = 'gs://apache-beam-samples/nasa_jpl_asteroid/sample_10000.csv'
    
    # Initialize the pipeline.
    p = beam.Pipeline(InteractiveRunner())
    
    beam_df = p | beam.dataframe.io.read_csv(source_csv_file)
    

### Preprocess the data

This example uses the [NASA - Nearest Earth Objects dataset](https://cneos.jpl.nasa.gov/ca/). This dataset includes information about objects in outer space. Some objects are close enough to Earth to cause harm. This dataset compiles the list of NASA certified asteroids that are classified as the nearest earth objects to understand which objects pose a risk. Inspect the dataset columns and their types.
    
    
    beam_df.dtypes
    
    
    
    spk_id                       int64
    full_name                   object
    near_earth_object           object
    absolute_magnitude         float64
    diameter                   float64
    albedo                     float64
    diameter_sigma             float64
    eccentricity               float64
    inclination                float64
    moid_ld                    float64
    object_class                object
    semi_major_axis_au_unit    float64
    hazardous_flag              object
    dtype: object
    

When using Interactive Beam, to bring a Beam DataFrame into local memory as a Pandas DataFrame, use `ib.collect()`.
    
    
    ib.collect(beam_df)
    

The datasets contain the following two types of columns:

  * **Numerical columns:** Use [normalization](https://developers.google.com/machine-learning/data-prep/transform/normalization) to transform these columns so that they can be used to train a machine learning model.
  * **Categorical columns:** Transform those columns with [one-hot encoding](https://developers.google.com/machine-learning/data-prep/transform/transform-categorical) to use them during training. 

Use the standard pandas command `DataFrame.describe()` to generate descriptive statistics for the numerical columns, such as percentile, mean, std, and so on. 
    
    
    with dataframe.allow_non_parallel_operations():
      beam_df_description = ib.collect(beam_df.describe())
    
    beam_df_description
    

Before running any transformations, verify that all of the columns need to be used for model training. Start by looking at the column description provided by the [JPL website](https://ssd.jpl.nasa.gov/sbdb_query.cgi):

  * **spk_id:** Object primary SPK-ID.
  * **full_name:** Asteroid name.
  * **near_earth_object:** Near-earth object flag.
  * **absolute_magnitude:** The apparent magnitude an object would have if it were located at a distance of 10 parsecs.
  * **diameter:** Object diameter (from equivalent sphere) km unit.
  * **albedo:** A measure of the diffuse reflection of solar radiation out of the total solar radiation, measured on a scale from 0 to 1.
  * **diameter_sigma:** 1-sigma uncertainty in object diameter km unit.
  * **eccentricity:** A value between 0 and 1 that refers to how flat or round the asteroid is.
  * **inclination:** The angle with respect to the x-y ecliptic plane.
  * **moid_ld:** Earth Minimum Orbit Intersection Distance au unit.
  * **object_class:** The classification of the asteroid. For a more detailed description, see [NASA object classifications](https://pdssbn.astro.umd.edu/data_other/objclass.shtml).
  * **Semi-major axis au Unit:** The length of half of the long axis in AU unit.
  * **hazardous_flag:** Identifies hazardous asteroids.

The **spk_id** and **full_name** columns are unique for each row. You can remove these columns, because they are not needed for model training.
    
    
    beam_df = beam_df.drop(['spk_id', 'full_name'], axis='columns', inplace=False)
    

Review the number of missing values.
    
    
    ib.collect(beam_df.isnull().mean() * 100)
    
    
    
    /content/beam/sdks/python/apache_beam/dataframe/frame_base.py:145: RuntimeWarning: invalid value encountered in long_scalars
      lambda left, right: getattr(left, op)(right), name=op, args=[other])
    near_earth_object           0.000000
    absolute_magnitude          0.000000
    diameter                   13.111311
    albedo                     13.271327
    diameter_sigma             14.081408
    eccentricity                0.000000
    inclination                 0.000000
    moid_ld                     0.000000
    object_class                0.000000
    semi_major_axis_au_unit     0.000000
    hazardous_flag              0.000000
    dtype: float64
    

Most of the columns do not have missing values. However, the columns **diameter** , **albedo** , and **diameter_sigma** have many missing values. Because these values cannot be measured or derived and aren't needed for training the ML model, remove the columns.
    
    
    beam_df = beam_df.drop(['diameter', 'albedo', 'diameter_sigma'], axis='columns', inplace=False)
    ib.collect(beam_df)
    

### Normalize the data

Normalize the numerical columns so that they can be used to train a model. To standarize the data, you can subtract the mean and divide by the standard deviation. This process is also known as finding the [z-score](https://developers.google.com/machine-learning/data-prep/transform/normalization#z-score). This step improves the performance and training stability of the model during training and inference. First, retrieve both the numerical columns and the categorical columns.
    
    
    numerical_cols = beam_df.select_dtypes(include=np.number).columns.tolist()
    categorical_cols = list(set(beam_df.columns) - set(numerical_cols))
    
    
    
    # Get the numerical columns.
    beam_df_numericals = beam_df.filter(items=numerical_cols)
    
    # Standarize DataFrames with only the numerical columns.
    beam_df_numericals = (beam_df_numericals - beam_df_numericals.mean())/beam_df_numericals.std()
    
    ib.collect(beam_df_numericals)
    
    
    
    /content/beam/sdks/python/apache_beam/dataframe/frame_base.py:145: RuntimeWarning: invalid value encountered in double_scalars
      lambda left, right: getattr(left, op)(right), name=op, args=[other])
    

Next, convert the categorical columns into one-hot encoded variables to use during training.
    
    
    def get_one_hot_encoding(df: pd.DataFrame, categorical_col:list) -> pd.DataFrame:
      beam_df_categorical= beam_df[categorical_col]
      # Get unique values.
      with dataframe.allow_non_parallel_operations():
        unique_classes = pd.CategoricalDtype(ib.collect(beam_df_categorical.unique(as_series=True)))
      # Use `str.get_dummies()` to get the one-hot encoded representation of the categorical columns.
      beam_df_categorical = beam_df_categorical.astype(unique_classes).str.get_dummies()
      # Add a column name prefix to the newly created categorical columns.
      beam_df_categorical = beam_df_categorical.add_prefix(f'{categorical_col}_')
    
      return beam_df_categorical
    
    
    
    for categorical_col in categorical_cols:
      beam_df_categorical = get_one_hot_encoding(df=beam_df, categorical_col=categorical_col)
      beam_df_numericals = beam_df_numericals.merge(beam_df_categorical, left_index = True, right_index = True)
    ib.collect(beam_df_numericals)
    

### Run the pipeline

This section combines the previous steps into a full pipeline implementation, and then visualizes the preprocessed data. Note that the only standard Apache Beam method invoked here is the `pipeline` instance. The rest of the preprocessing commands are based on native pandas methods that are integrated with the Apache Beam DataFrame API.
    
    
    # Specify the location of the source CSV file.
    source_csv_file = 'gs://apache-beam-samples/nasa_jpl_asteroid/sample_10000.csv'
    
    # Initialize the pipeline.
    p = beam.Pipeline(InteractiveRunner())
    
    # Create a deferred Apache Beam DataFrame with the contents of the CSV file.
    beam_df = p | beam.dataframe.io.read_csv(source_csv_file)
    
    # Drop irrelevant columns and columns with missing values.
    beam_df = beam_df.drop(['spk_id', 'full_name','diameter', 'albedo', 'diameter_sigma'], axis='columns', inplace=False)
    
    # Get numerical columns and columns with categorical values.
    numerical_cols = beam_df.select_dtypes(include=np.number).columns.tolist()
    categorical_cols = list(set(beam_df.columns) - set(numerical_cols))
    
    # Normalize the numerical values.
    beam_df_numericals = beam_df.filter(items=numerical_cols)
    beam_df_numericals = (beam_df_numericals - beam_df_numericals.mean())/beam_df_numericals.std()
    
    
    # One-hot encode the categorical values.
    for categorical_col in categorical_cols:
      beam_df_categorical= get_one_hot_encoding(df=beam_df, categorical_col=categorical_col)
      beam_df_numericals = beam_df_numericals.merge(beam_df_categorical, left_index = True, right_index = True)
    
    ib.collect(beam_df_numericals)
    
    
    
    /content/beam/sdks/python/apache_beam/dataframe/frame_base.py:145: RuntimeWarning: invalid value encountered in double_scalars
      lambda left, right: getattr(left, op)(right), name=op, args=[other])
    

## Process the full dataset with the distributed runner

The previous section demonstrates how to build and execute the pipeline locally using the interactive runner. This section demonstrates how to run the pipeline on the full dataset by switching to a distributed runner. For this example, the pipeline runs on [Dataflow](https://cloud.google.com/dataflow/docs/guides/deploying-a-pipeline).
    
    
    PROJECT_ID = "<my-gcp-project>" # @param {type:'string'}
    REGION = "us-central1"
    TEMP_DIR = "gs://<my-bucket>/tmp" # @param {type:'string'}
    OUTPUT_DIR = "gs://<my-bucket>/dataframe-result" # @param {type:'string'}
    

These steps process the full dataset, `full.csv`, which contains approximately one million rows. To materialize the deferred DataFrame, these steps also write the results to a CSV file instead of using `ib.collect()`. To switch from an interactive runner to a distributed runner, update the pipeline options. The rest of the pipeline steps don't change.
    
    
    # Specify the location of the source CSV file (the full dataset).
    source_csv_file = 'gs://apache-beam-samples/nasa_jpl_asteroid/full.csv'
    
    # Build a new pipeline that runs on Dataflow.
    p = beam.Pipeline(DataflowRunner(),
                      options=beam.options.pipeline_options.PipelineOptions(
                          project=PROJECT_ID,
                          region=REGION,
                          temp_location=TEMP_DIR,
                          # To speed up the demo, disable autoscaling.
                          autoscaling_algorithm='NONE',
                          num_workers=10))
    
    # Create a deferred Apache Beam DataFrame with the contents of the CSV file.
    beam_df = p | beam.dataframe.io.read_csv(source_csv_file)
    
    # Drop irrelevant columns and columns with missing values.
    beam_df = beam_df.drop(['spk_id', 'full_name','diameter', 'albedo', 'diameter_sigma'], axis='columns', inplace=False)
    
    # Get numerical columns and columns with categorical values.
    numerical_cols = beam_df.select_dtypes(include=np.number).columns.tolist()
    categorical_cols = list(set(beam_df.columns) - set(numerical_cols))
    
    # Normalize the numerical values. 
    beam_df_numericals = beam_df.filter(items=numerical_cols)
    beam_df_numericals = (beam_df_numericals - beam_df_numericals.mean())/beam_df_numericals.std()
    
    
    # One-hot encode the categorical values. 
    for categorical_col in categorical_cols:
      beam_df_categorical= get_one_hot_encoding(df=beam_df, categorical_col=categorical_col)
      beam_df_numericals = beam_df_numericals.merge(beam_df_categorical, left_index = True, right_index = True
    
    # Write the preprocessed dataset to a CSV file.
    beam_df_numericals.to_csv(os.path.join(OUTPUT_DIR, "preprocessed_data.csv"))
    

Submit and run the pipeline.
    
    
    p.run().wait_until_finish()
    

Wait while the pipeline job runs.

## What's next

This tutorial demonstrated how to analyze and preprocess a large-scale dataset with the Apache Beam DataFrames API. You can now train a model on a classification task using the preprocessed dataset. To learn more about how to get started with classifying structured data, see [Structured data classification from scratch](https://keras.io/examples/structured_data/structured_data_classification_from_scratch/). To continue learning, find another dataset to use with the Apache Beam DataFrames API processing. Think carefully about which features to include in your model and how to represent them.

## Resources

  * [Beam DataFrames overview](https://beam.apache.org/documentation/dsls/dataframes/overview) \- An overview of the Apache Beam DataFrames API.
  * [Differences from pandas](https://beam.apache.org/documentation/dsls/dataframes/differences-from-pandas) \- Reviews the differences between Apache Beam DataFrames and Pandas DataFrames, as well as some of the workarounds for unsupported operations.
  * [10 minutes to Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html) \- A quickstart guide to the Pandas DataFrames.
  * [Pandas DataFrame API](https://pandas.pydata.org/pandas-docs/stable/reference/frame.html) \- The API reference for the Pandas DataFrames.
  * [Data preparation and feature training in ML](https://developers.google.com/machine-learning/data-prep) \- A guideline about data transformation for ML training.

Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2025-10-22 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-22 UTC."],[],[]] 
