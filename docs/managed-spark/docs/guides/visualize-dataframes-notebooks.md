---
url: https://docs.cloud.google.com/managed-spark/docs/guides/visualize-dataframes-notebooks/
title: Visualize Spark DataFrames in notebooks \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:22:30.892159+00:00
---

# Visualize Spark DataFrames in notebooks  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/guides/visualize-dataframes-notebooks/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Visualize Spark DataFrames in notebooks Stay organized with collections  Save and categorize content based on your preferences. 

You can interactively explore PySpark DataFrames in Jupyter notebooks, including [Google Cloud Data Agent Kit](https://docs.cloud.google.com/data-agent-kit/overview) (DAK), by using the [`google-colabsqlviz`](https://pypi.org/project/google-colabsqlviz/) Python package with Managed Service for Apache Spark. Built on [`anywidget`](https://anywidget.dev/) and powered by the Data Studio charting engine, `google-colabsqlviz` renders an interactive visualization inside your notebook cell output without plotting code.

When you pass a DataFrame to `google-colabsqlviz`, you can switch between chart and data table views, configure dimensions and metrics, apply aggregations, sort or filter data interactively, and export filtered or aggregated chart data to a new DataFrame:

  * **Multi-engine DataFrame support** : Visualize `pyspark.sql.DataFrame` (including Spark Connect DataFrames), `bigframes.pandas.DataFrame`, and `pandas.DataFrame` objects using one API.
  * **In-kernel and distributed execution** : Although the widget loads the Data Studio charting UI from Google's CDN, your underlying data isn't sent to Data Studio. All aggregations and filters run in your Python kernel or your Managed Service for Apache Spark session, and charts render locally in your notebook client.
  * **Zero environment conflicts** : Optional distributed engines such as `pyspark` and `bigframes` are detected at runtime and aren't upgraded or overwritten when you install `google-colabsqlviz`.



## Before you begin

Rendering PySpark DataFrames over [Spark Connect](https://docs.cloud.google.com/managed-spark/docs/guides/spark-connect-client) with `google-colabsqlviz` is supported in Managed Service for Apache Spark interactive sessions with [serverless runtime version](https://docs.cloud.google.com/managed-spark/docs/concepts/versions/serverless-versions) `3.0` or later.

Follow these instructions to create a notebook in Visual Studio Code (VS Code) with [Data Agent Kit](https://docs.cloud.google.com/data-agent-kit/overview), or use another supported Jupyter notebook environment such as [JupyterLab](https://docs.cloud.google.com/managed-spark/docs/guides/jupyterlab-sessions-serverless):

  1. Set up and configure the Data Agent Kit (DAK): 
     1. [Install the Data Agent Kit extension](https://docs.cloud.google.com/data-agent-kit/install).
     2. [Configure the Data Agent Kit](https://docs.cloud.google.com/data-agent-kit/configure).
     3. [Ensure that you have the required Identity and Access Management (IAM) roles](https://docs.cloud.google.com/data-agent-kit/permissions). The Data Agent Kit will notify you if you are missing required permissions for a task.
  2. Create a notebook: 
     1. In the VS Code activity bar, click **Data Agent Kit** , expand **Apache Spark** , and select **\+ New Spark Notebook**.
     2. To **Select kernel type** , click **Local Kernel**.
     3. To **Select a Serverless Runtime template** , click the name of a listed runtime template. To create a new runtime to select for your notebook, under **Apache Spark** > **Serverless** , click **New runtime** , and then fill in the **Create Serverless Runtime** form.
     4. In the notebook toolbar, click **Select Kernel** , click **Python Environments...** , and then choose your local Python environment.
  3. To install the required [Spark Connect](https://spark.apache.org/docs/latest/spark-connect-overview.html) and [`google-colabsqlviz`](https://pypi.org/project/google-colabsqlviz/) Python packages in your local environment, run the following command in a notebook cell or local terminal:

### Notebook cell
         
         %pip install -U 'google-cloud-spark-connect[interactive,client]'
         

### Local terminal
         
         pip install -U 'google-cloud-spark-connect[interactive,client]'
         




## Load and visualize a dataset

After you start a `ManagedSparkSession` and load a dataset into a `pyspark.sql.DataFrame`, pass the DataFrame to the `explore_dataframe` function to render the interactive visualization. The following example connects to a serverless session and loads the Palmer Penguins dataset (``lakehouse-public-data`.ml_datasets.penguins`) from the [Lakehouse public datasets](https://docs.cloud.google.com/lakehouse/docs/public-datasets):

`google.colabsqlviz.explore_dataframe` also provides a `display` function that you can import to call `display(df)`. This shadows the IPython built-in `display` function to facilitate adding visualizations to notebooks.
    
    
    # Importing managed_spark_connect automatically imports explore_dataframe
    from google.cloud.managed_spark_connect import ManagedSparkSession
    
    spark = (
        ManagedSparkSession.builder.projectId("PROJECT_ID")
        .location("REGION")
        .getOrCreate()
    )
    
    df = spark.read.table("`lakehouse-public-data`.ml_datasets.penguins")
    
    explore_dataframe(df)
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `REGION`: the Managed Service for Apache Spark region for your session (for example, `us-central1`).



When you run the cell, `google-colabsqlviz` inspects the DataFrame schema and renders an interactive visualization widget in the cell output area with a default visualization—for the `penguins` dataset, it renders a scatter chart of average `flipper_length_mm` and `body_mass_g` grouped by `species`.

In the widget toolbar, click **Data** to inspect the underlying DataFrame rows in a paginated table. Select **Split mode** to view the chart and underlying data table together. Click **Chart** to return to the chart view.

![Default scatter chart view in the visualization widget showing average
flipper length and body mass by penguin
species.](https://docs.cloud.google.com/static/managed-spark/docs/images/colabsqlviz-default-view.png)

## Explore and customize charts

You can customize chart types, dimensions, metrics, aggregations, sorting, and filters in the widget interface, and export the resulting data back to a DataFrame in your notebook.

  1. **Select a chart type** : In the configuration settings panel, click the chart type menu and select a chart type, such as **Vertical bar chart**. For a complete list of supported chart types, see [Types of charts in Data Studio](https://docs.cloud.google.com/data-studio/types-of-charts).
  2. **Configure dimensions and metrics** : On the **Setup** tab, configure the fields for the `penguins` DataFrame: 
     * Keep **Dimension** set to `species` to group records by penguin species.
     * Under **Metric - Y axis** , set the metric to `body_mass_g` with aggregation set to **AVG** (**Average**) to calculate the average body mass in grams for each species.
     * Click **Add dimension** and select `island` or `sex` to break down the chart across multiple dimensions, or change the metric aggregation from **AVG** to **MAX** or **SUM**.
  3. **Sort and filter the visualization** : 
     * On the **Setup** tab, under **Sort** , select `body_mass_g` with the **AVG** aggregation and select **Descending** to rank species by highest average body mass.
     * Click **Add filter** in the widget toolbar to filter records by field values (for example, `body_mass_g` greater than or equal to `4000`), or click **Create output dataframe** at the bottom of the widget to export the aggregated chart data or filtered data to a new DataFrame cell. When you update a chart property or filter, `google-colabsqlviz` recomputes the query against your DataFrame and updates the visualization:



![Vertical bar chart and configuration panel in the visualization widget
displaying average body mass by penguin species sorted in descending
order.](https://docs.cloud.google.com/static/managed-spark/docs/images/colabsqlviz-chart-setup.png)

For more information on configuring chart properties, aggregations, and interactive controls in the embedded charting interface, see the following documentation:

  * [Types of charts in Data Studio](https://docs.cloud.google.com/data-studio/types-of-charts)
  * [Explore your data in Data Studio](https://docs.cloud.google.com/data-studio/explore-your-data)
  * [Use visualization cells in Colab Enterprise](https://docs.cloud.google.com/colab/docs/visualization-cells)



## Configure execution for large DataFrames

When you pass a `pyspark.sql.DataFrame` to `explore_dataframe(df)`, `google-colabsqlviz` chooses between two execution strategies based on the size of the DataFrame:

  * **In-memory materialization** (default for smaller DataFrames): If the DataFrame is estimated at `256 MiB` or less and contains at most 5,000,000 rows, `google-colabsqlviz` collects the DataFrame into kernel memory once. Subsequent chart type changes, aggregations, sorting, and filtering run in memory with minimal latency and don't trigger new Spark jobs.
  * **Distributed Spark pushdown** (the default for larger DataFrames): If the DataFrame exceeds the byte or row budget, `google-colabsqlviz` keeps the DataFrame lazy and translates each chart query, filter, sort, and pagination request into a PySpark operation executed on your Managed Service for Apache Spark serverless session. This approach can add additional latency, but lets you visualize much larger DataFrames.



You can adjust or disable the in-memory materialization threshold by setting the `COLABSQLVIZ_PYSPARK_EAGER_MAX_BYTES` environment variable before calling `explore_dataframe(df)`:
    
    
    import os
    
    # Importing managed_spark_connect automatically imports explore_dataframe
    from google.cloud.managed_spark_connect import ManagedSparkSession
    
    # Set to "0" to disable upfront collection and push all chart queries to Spark,
    # or set a custom byte limit, such as str(64 * 1024 * 1024) for 64 MiB.
    os.environ["COLABSQLVIZ_PYSPARK_EAGER_MAX_BYTES"] = "0"
    
    explore_dataframe(df)
    

## What's next

  * Explore [Types of charts in Data Studio](https://docs.cloud.google.com/data-studio/types-of-charts).
  * Learn how to [transform data with Data Agent Kit](https://docs.cloud.google.com/data-agent-kit/transform-data).
  * Learn how to [use the serverless Spark Connect client](https://docs.cloud.google.com/managed-spark/docs/guides/spark-connect-client).
  * Learn how to [use JupyterLab and VS Code for serverless sessions](https://docs.cloud.google.com/managed-spark/docs/guides/jupyterlab-sessions-serverless).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
