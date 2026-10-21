---
url: https://docs.cloud.google.com/colab/docs/use-data-science-agent/
title: Use the Data Science Agent \u00a0|\u00a0 Colab Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:30:20.861553+00:00
---

# Use the Data Science Agent  |  Colab Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/use-data-science-agent/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Guides ](https://docs.cloud.google.com/colab/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use the Data Science Agent

This guide describes how you can use the Data Science Agent in Colab Enterprise to help you perform data science tasks in your notebooks.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

This document is intended for data analysts, data scientists, and data developers who work with Colab Enterprise. It assumes you have knowledge of how to write code in a notebook environment.

## Capabilities of the Data Science Agent

The Data Science Agent can help you with tasks ranging from exploratory data analysis to generating machine learning predictions and forecasts. You can use the Data Science Agent for:

  * **Large-scale data processing** : Use BigQuery ML, BigQuery DataFrames, or Managed Service for Apache Spark to perform distributed data processing on large datasets. This lets you efficiently clean, transform, and analyze data that's too large to fit into memory on a single machine.
  * **Generating plans** : Generate and modify a plan to complete a particular task using common tools such as Python, SQL, Apache Spark, and BigQuery DataFrames.
  * **Data exploration** : Explore a dataset to understand its structure, identify potential issues like missing values and outliers, and examine the distribution of key variables.
  * **Data cleaning** : Clean your data. For example, remove data points that are outliers.
  * **Data wrangling** : Convert categorical features into numerical representations using techniques like one-hot encoding or label encoding. Create new features for analysis.
  * **Data analysis** : Analyze the relationships between different variables. Calculate correlations between numerical features and explore distributions of categorical features. Look for patterns and trends in the data.
  * **Data visualization** : Create visualizations such as histograms, box plots, scatter plots, and bar charts that represent the distributions of individual variables and the relationships between them.
  * **Feature engineering** : Engineer new features from a cleaned dataset.
  * **Data splitting** : Split an engineered dataset into training, validation, and testing datasets.
  * **Model training** : Train a model by using the training data in a pandas DataFrame, a [BigQuery DataFrames](https://docs.cloud.google.com/bigquery/docs/use-bigquery-dataframes#train_models), a [PySpark DataFrame](https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrame.html), or by using the BigQuery ML [`CREATE MODEL` statement](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create) with BigQuery tables.
  * **Model optimization** : Optimize a model by using the validation set. Explore alternative models like `DecisionTreeRegressor` and `RandomForestRegressor` and compare their performance.
  * **Model evaluation** : Evaluate model performance on a test dataset using a pandas DataFrame, BigQuery DataFrames, or a PySpark DataFrame. You can also assess model quality and compare models by using BigQuery ML [model evaluation functions](https://docs.cloud.google.com/bigquery/docs/evaluate-overview) for models trained using BigQuery ML.
  * **Model inference** : Perform inference with BigQuery ML trained models, imported models, and remote models using BigQuery ML [inference functions](https://docs.cloud.google.com/bigquery/docs/inference-overview). You can also use the BigQuery DataFrames `model.predict()` method or PySpark [transformers](https://spark.apache.org/docs/latest/ml-pipeline.html#transformers) to make predictions.



## Limitations

  * The Data Science Agent supports the following data sources: 
    * CSV files
    * BigQuery tables
  * The code produced by the Data Science Agent only runs in your notebook's runtime.
  * Your notebook must be in a region supported by the Data Science Agent. See [Locations](https://docs.cloud.google.com/colab/docs/locations).
  * The first time you run the Data Science Agent, you may experience some latency of approximately five to ten minutes. This only occurs once per project during initial setup.
  * Searching for BigQuery tables using the `@mention` function is limited to your current project. Use the table selector to search across projects.
  * The `@mention` function only searches for BigQuery tables. To search for data files that you can upload, use the `+` symbol.
  * PySpark in the Data Science Agent only generates Apache Spark 4.0 code. The Data Science Agent can help you upgrade to Apache Spark 4.0, but users who require earlier versions of Apache Spark shouldn't use the Data Science Agent.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Agent Platform, Dataform, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,dataform.googleapis.com,compute.googleapis.com&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Agent Platform, Dataform, and Compute Engine APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=aiplatform.googleapis.com,dataform.googleapis.com,compute.googleapis.com&redirect=https%3A//console.cloud.google.com)




### Required roles

To get the permissions that you need to use the Data Science Agent in Colab Enterprise, ask your administrator to grant you the [Colab Enterprise User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.colabEnterpriseUser) (`roles/aiplatform.colabEnterpriseUser`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

One or more of the required roles includes the `dataform.repositories.list` permission. Users who are granted the `dataform.repositories.list` permission or the [Code Creator (`roles/dataform.codeCreator`)](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeCreator) role in a project can list the names of code assets in that project by using the Dataform API or the Dataform command-line interface (CLI). Non-administrators using BigQuery Studio can only see code assets that they created or that were shared with them. 

## Reference your data

To enable Colab Enterprise's Data Science Agent to access and work with your data, you can upload a CSV file or reference a BigQuery table.

### CSV file

  1. In the Google Cloud console, go to the Colab Enterprise **My notebooks** page. 

[Go to My notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. In the **Region** menu, select the region that contains your notebook.

  3. Click the notebook that you want to open.

  4. Click the ![](https://docs.cloud.google.com/static/colab/images/icon-gemini.png) **Toggle Gemini in Colab** button to open the chat dialog. 

**Note:** You can move the chat dialog into a separate panel outside the notebook by clicking the dock_to_left **Move to panel** button. 
  5. In the chat dialog, click add_circle_outline **Add files > Upload**. 
  6. If necessary, authorize your Google Account.

Wait a moment for Colab Enterprise to start a runtime and enable file browsing. 

  7. Browse to the location of the file, and then click **Open**. 
  8. Click **OK** to acknowledge that this runtime's files will be deleted when the runtime is deleted. 

The file is uploaded to the **Files** pane, and it appears in the chat window.




### BigQuery table

  1. In the Google Cloud console, go to the Colab Enterprise **My notebooks** page. 

[Go to My notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. In the **Region** menu, select the region that contains your notebook.

  3. Click the notebook that you want to open.

  4. Click the ![](https://docs.cloud.google.com/static/colab/images/icon-gemini.png) **Toggle Gemini in Colab** button to open the chat dialog. 

**Note:** You can move the chat dialog into a separate panel outside the notebook by clicking the dock_to_left **Move to panel** button. 
  5. To reference your data, do one of the following:

     * Choose one or more tables using the table selector:

       1. Click add_circle_outline **Add to Gemini > BigQuery tables**. 
       2. In the **BigQuery tables** window, select one or more tables in your project. You can search for tables across projects and filter tables by using the search bar. 
     * Include a BigQuery table name directly in your prompt. For example: "Help me perform exploratory data analysis and get insights about the data in this table: `PROJECT_ID:DATASET.TABLE`." 

Replace the following:

       * `PROJECT_ID`: your project ID.
       * `DATASET`: the name of the dataset that contains the table that you're analyzing. 
       * `TABLE`: the name of the table that you're analyzing. 
     * Type `@` to search for a BigQuery table in your current project. 
     * In your prompt, use natural language to describe the table that you want to use, and the Data Science Agent references the table that best matches your description. 



## Use the Data Science Agent

To get started using Colab Enterprise's Data Science Agent, do the following:

  1. In the **Gemini** chat dialog, enter a prompt and click send **Send**. To get ideas for prompts, review the Data Science Agent capabilities and see Sample prompts. 

For example, you might enter "Provide an analysis of the data I've uploaded." 

If you haven't already authorized the Data Science Agent, a brief dialog appears while Colab Enterprise authenticates your Google Account to the Data Science Agent. 

  2. Gemini responds to your prompt. The response can include code snippets to run, general advice for your project, next steps for accomplishing your goals, or information about specific problems in your data or code. 

After evaluating the response, you can do the following:

     * If Gemini provides code in its response, you can click: 
       * **Accept** to add the code to your notebook.
       * **Accept and run** to add the code to your notebook and run the code.
       * **Cancel** to delete the suggested code.
     * Ask follow-up questions and continue the discussion as needed.
  3. To close the **Gemini** dialog, click close **Close**. 




## Turn off Gemini in Colab Enterprise

To turn off Gemini in Colab Enterprise for a Google Cloud project, an administrator must turn off the Gemini for Google Cloud API. See [Disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable#disabling). 

To turn off Gemini in Colab Enterprise for a specific user, an administrator needs to revoke the [Gemini for Google Cloud User](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.user) (`roles/cloudaicompanion.user`) role for that user. See [Revoke a single IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#revoke-single-role). 

## Sample prompts

The following sections show examples of the types of prompts that you can use with the Data Science Agent.

### Python prompts

Python code is generated by default unless you use a specific keyword in the prompt such as "BigQuery ML" or "SQL".

  * Investigate and fill missing values by using the k-Nearest Neighbors (KNN) machine learning algorithm.
  * Create a plot of salary by experience level. Use the `experience_level` column to group the salaries, and create a box plot for each group showing the values from the `salary_in_usd` column.
  * Use the XGBoost algorithm to make a model for determining the `class` variable of a particular fruit. Split the data into training and testing datasets to generate a model and to determine the model's accuracy. Create a confusion matrix to show the predictions amongst each class, including all predictions that are correct and incorrect.
  * Forecast `target_variable` from `filename.csv` for the next six months.



### SQL and BigQuery ML prompts

  * Create and evaluate a classification model on `bigquery-public-data.ml_datasets.census_adult_income` using BigQuery SQL.
  * Using SQL, forecast the future traffic of my website for the next month based on `bigquery-public-data.google_analytics_sample.ga_sessions_*`. Then, plot the historical and forecasted values.
  * Group similar customers together to create targeting market campaigns using a KMeans model and BigQuery ML SQL functions. Use three features for clustering. Then visualize the results by creating a series of 2D scatter plots. Use the table `bigquery-public-data.ml_datasets.census_adult_income`.
  * Generate text embeddings in BigQuery ML using the review content in `bigquery-public-data.imdb.reviews`.



For a list of supported models and machine learning tasks, see the [BigQuery ML documentation](https://docs.cloud.google.com/bigquery/docs/bqml-introduction).

### DataFrame prompts

  * Create a pandas DataFrame for the data in `project_id:dataset.table`. Analyze the data for null values, and then graph the distribution of each column using the graph type. Use violin plots for measured values and bar plots for categories.
  * Read `filename.csv` and construct a DataFrame. Run analysis on the DataFrame to determine what needs to be done with values. For example, are there missing values that need to be replaced or removed, or are there duplicate rows that need to be addressed. Use the data file to determine the distribution of the money invested in USD per city location. Graph the top 20 results using a bar graph that shows the results in descending order as Location versus Avg Amount Invested (USD).
  * Create and evaluate a classification model on `project_id:dataset.table` using BigQuery DataFrames.
  * Create a time series forecasting model on `project_id:dataset.table` using BigQuery DataFrames, and visualize the model evaluations.
  * Visualize the sales figures in the past year in BigQuery table `project_id:dataset.table` using BigQuery DataFrames.
  * Find the features that can best predict the penguin species from the table `bigquery-public_data.ml_datasets.penguins` using BigQuery DataFrames.



### PySpark prompts

  * Create and evaluate a classification model on `project_id:dataset.table` using Managed Service for Apache Spark.
  * Group similar customers together to create targeting market campaigns, but first do dimensionality reduction using a PCA model. Use PySpark to do this on table `project_id:dataset.table`.



## Supported regions

To view the supported regions for Colab Enterprise's Data Science Agent, see [Locations](https://docs.cloud.google.com/colab/docs/locations).

## Billing

Data Science Agent pricing is based on your input and output data. For more information, see Agent pricing on the [BigQuery pricing page](https://cloud.google.com/bigquery/pricing).

## VPC Service Controls

The Data Science Agent supports VPC Service Controls. If you would like to use the Data Science Agent in a service perimeter, see [Use VPC Service Controls with Colab Enterprise](https://docs.cloud.google.com/colab/docs/service-controls#data-science-agent).

## Customer-managed encryption keys (CMEK)

The Data Science Agent supports customer-managed encryption keys (CMEK). For more information, see [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/colab/docs/cmek).

## What's next

  * For more information on how to use the Data Science Agent with BigQuery, see [Use the Colab Enterprise Data Science Agent with BigQuery](https://docs.cloud.google.com/bigquery/docs/colab-data-science-agent).

  * Read the [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview).

  * Learn more about [using customer-managed encryption keys (CMEK) with Colab Enterprise](https://docs.cloud.google.com/colab/docs/cmek).

  * For more ways to write and edit code with Gemini assistance, see the following:

    * [Chat about your notebook with Gemini](https://docs.cloud.google.com/colab/docs/chat)
    * [Use code completion and code generation](https://docs.cloud.google.com/colab/docs/use-code-completion)
    * [Explain code cells](https://docs.cloud.google.com/colab/docs/explain-cells)
    * [Explain errors](https://docs.cloud.google.com/colab/docs/explain-errors)
  * Learn [how Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
