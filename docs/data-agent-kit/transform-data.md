---
url: https://docs.cloud.google.com/data-agent-kit/transform-data/
title: Transform data \u00a0|\u00a0 Google Cloud Data Agent Kit \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:16.872532+00:00
---

# Transform data  |  Google Cloud Data Agent Kit  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-agent-kit/transform-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Agent Kit ](https://docs.cloud.google.com/data-agent-kit)
  * [ Guides ](https://docs.cloud.google.com/data-agent-kit/overview)



Send feedback 

#  Transform data Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Data Agent Kit lets you use notebooks for data cleaning, feature engineering, and deep analysis.There are three types of notebooks to choose from.

  * **BigQuery DataFrames notebooks**. These are Python notebooks that let you process massive datasets in BigQuery using familiar pandas and scikit-learn APIs. They support writing code in GoogleSQL for BigQuery in addition to Python.
  * **Managed Apache Spark notebooks with local kernel**. These are Python notebooks that let you create and execute jobs on Managed Service for Apache Spark using its Spark Connect library.

  * **Managed Apache Spark notebooks with remote kernel**. These notebooks enable you to execute your notebook on a remote kernel that runs entirely on Managed Service for Apache Spark. No part of your code is executed locally on your computer. In addition to PySpark, you can write your code in Spark SQL with the help of `%%sparksql` cell magic.




## Before you begin

For BigQuery notebooks, the `bigframes` library must be installed in the same Python virtual environment in which you execute your notebook. When you create a new notebook, the initialization cell contains the following line, which is commented:
    
    
    #%pip install --upgrade bigframes
    

  1. Optional: if you don't have the `bigframes` library installed in your Python virtual environment, remove the comment.

  2. Optional: if you plan to write SQL code in your notebook, install `bigquery-magics`:



    
    
    pip install --upgrade bigquery-magics
    

### Required roles

To get the permissions that you need to execute BigQuery notebooks, ask your administrator to grant you the [BigQuery Studio User](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`) on the project you selected in the extension.

To get the permissions that you need for Managed Service for Apache Spark notebooks, ask your administrator to grant you the following roles on the project:

  * [Dataproc Editor](https://docs.cloud.google.com/dataproc/docs/concepts/iam/iam#dataproc.editor) (`roles/dataproc.editor`)
  * [Dataproc Serverless Editor](https://docs.cloud.google.com/dataproc/docs/concepts/iam/iam#dataproc.serverlessEditor) (`roles/dataproc.serverlessEditor`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined).

## Transform your data

For data in a BigLake or BigQuery table, the extension provides notebook templates to get you started.

**Note:** This guide uses the Data Agent Kit extension, but you can accomplish the same tasks with natural language prompts using the Data Agent Kit plugin with a supported coding agent or CLI.

### Navigate to the table

Navigate to a BigQuery or BigLake table:

  1. Open the command palette by pressing `Ctrl/Cmd-Shift-P`.
  2. Expand the Catalog explorer and find your BigQuery or BigLake.
  3. Right-click the table ID.
  4. From the floating menu, choose **Load in Spark DataFrame** or **Load in BigQuery DataFrame**. A new editor displays information about the table.

You can also find the table using [Universal Search](https://docs.cloud.google.com/data-agent-kit/find-explore-data#universal-search). Click the table ID to open a new editor, click the **Data** tab, and then choose **Load in Spark DataFrame** or **Load in BigQuery DataFrame**.




### Initialize a notebook

After you load the table, a new Jupyter notebook opens in an editor tab containing the necessary code to load your table in your chosen dataframe type.

  1. If you don't have the required library installed in your Python virtual environment, uncomment the pip install line.

  2. Click **Select Kernel** and choose a Python kernel.

For Managed Spark notebooks with remote kernels you must choose a remote Spark kernel.

  3. Run the cell by clicking **▷ Run All** or pressing `Shift+Enter` at the bottom of the cell.

  4. If you are prompted to install missing software, click **Install**.




The cell creates a dataframe containing the data in the selected table.

### Apply data transformations to the DataFrame

Add additional cells to the notebook and write the code to transform your data. For BigQuery DataFrames, you can transform the DataFrame using the [pandas-compatible API provided by BigQuery DataFrames](https://dataframes.bigquery.dev/reference/api/bigframes.pandas.html).

Alternatively, BigQuery DataFrames provides a magics command that you can use to transform a DataFrame by using SQL in a Jupyter notebook. To transform your data using SQL, complete the following steps:

  1. Create and run a cell to activate the Jupyter magics.

`%load_ext bigframes`

  2. Create a SQL cell using the `%%bqsql` magics.




### Save the results

Use one of the many output methods provided by your DataFrames type to save the transformed data to BigQuery or Cloud Storage. For BigQuery DataFrames, output methods include the following:

  * [DataFrame.to_gbq](https://dataframes.bigquery.dev/reference/api/bigframes.pandas.DataFrame.to_gbq.html)
  * [DataFrame.to_csv](https://dataframes.bigquery.dev/reference/api/bigframes.pandas.DataFrame.to_csv.html)
  * [DataFrame.to_parquet](https://dataframes.bigquery.dev/reference/api/bigframes.pandas.DataFrame.to_parquet.html)



For small data, you can export to Arrow or Pandas for further local manipulation and visualization.

  * [DataFrame.to_arrow](https://dataframes.bigquery.dev/reference/api/bigframes.pandas.DataFrame.to_arrow.html)
  * [DataFrame.to_pandas](https://dataframes.bigquery.dev/reference/api/bigframes.pandas.DataFrame.to_pandas.html)



## Clean up

To avoid incurring charges to your Google Cloud account, delete any resources that you created but no longer need.

## What's next

  * [BigQuery DataFrames APIs](https://dataframes.bigquery.dev/reference/index.html).
  * [Introduction to SQL in BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction-sql).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
