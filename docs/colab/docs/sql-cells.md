---
url: https://docs.cloud.google.com/colab/docs/sql-cells/
title: Use SQL cells \u00a0|\u00a0 Colab Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:02:27.620504+00:00
---

# Use SQL cells  |  Colab Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/sql-cells/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Guides ](https://docs.cloud.google.com/colab/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use SQL cells

This guide describes how to use SQL cells to query data from within a Colab Enterprise notebook.

## Overview

A SQL cell is a code cell for writing, editing, and running SQL queries from within your Colab Enterprise notebook. SQL cells provide an alternative workflow to [IPython Magics for BigQuery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/magics).

### Capabilities

SQL cells provide the following capabilities:

  * **Dry-run support** : SQL statement validation and an approximation of the number of bytes processed by the query
  * **Formatting** : Keyword linting and syntax highlighting
  * **BigQuery DataFrame output variable naming** : Refer to the output variable from within other notebook cells
  * **Variable replacement** : Refer to Python variables and SQL cells to support parameterization and the ability to query the results of a previous query
  * **Result set viewer** : Lightweight tabular result set viewer with pagination for large result sets
  * **Visualization cell integration** : Output from a SQL cell can be used as input for a [visualization cell](https://docs.cloud.google.com/colab/docs/visualization-cells)



### Supported SQL dialect and data source

  * Colab Enterprise SQL cells support GoogleSQL.

  * You can run SQL queries on BigQuery data.




## Limitations

Consider the following limitations when you plan your project:

  * You can run multiple SQL statements in a single SQL cell, but only the results of the last SQL statement are saved to a DataFrame.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the BigQuery, Compute Engine, Dataform, and Agent Platform APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,compute.googleapis.com,dataform.googleapis.com,aiplatform.googleapis.com,&redirect=https%3A//console.cloud.google.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the BigQuery, Compute Engine, Dataform, and Agent Platform APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,compute.googleapis.com,dataform.googleapis.com,aiplatform.googleapis.com,&redirect=https%3A//console.cloud.google.com)




### Required roles

To get the permissions that you need to create a Colab Enterprise notebook, run the notebook's code on a runtime, and use BigQuery data in the notebook, ask your administrator to grant you the following IAM roles on the project: 

  * [BigQuery User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.user) (`roles/bigquery.user`)
  * [Colab Enterprise User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.colabEnterpriseUser) (`roles/aiplatform.colabEnterpriseUser`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

One or more of the required roles includes the `dataform.repositories.list` permission. Users who are granted the `dataform.repositories.list` permission or the [Code Creator (`roles/dataform.codeCreator`)](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeCreator) role in a project can list the names of code assets in that project by using the Dataform API or the Dataform command-line interface (CLI). Non-administrators using BigQuery Studio can only see code assets that they created or that were shared with them. 

## Create a SQL cell

To create a SQL cell in Colab Enterprise, do the following:

  1. In the Google Cloud console, go to the Colab Enterprise **My notebooks** page. 

[Go to My notebooks](https://console.cloud.google.com/agent-platform/colab/notebooks)

  2. In the **Region** menu, select the region that contains your notebook.

  3. Click the notebook that you want to open. If you haven't created a notebook yet, [create a notebook](https://docs.cloud.google.com/colab/docs/create-console-quickstart#create). 

  4. In the toolbar, to add a SQL cell, click the arrow_drop_down **Insert code cell options** menu and select **Add SQL cell**. 

![](https://docs.cloud.google.com/static/colab/images/add-sql-cell.png)

Your SQL cell is added to your notebook.




## Enter and run a query

  1. In your SQL cell, enter a SQL query. For an overview of supported statements and SQL dialects, see [Introduction to SQL in BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction-sql). 

You can refer to Python variables in expressions by enclosing the variable name in braces (`{ }`). For example, if you specified a value in a Python variable named `my_threshold`, you might limit your result set with a query similar to the following: 
         
         SELECT * FROM my_dataset.my_table WHERE x > {my_threshold};
             

  2. Hold the pointer over the SQL cell that you want to run, and then click the ![](https://docs.cloud.google.com/static/colab/images/icon-run-cell.png) **Run cell** button. 




The output of the query is automatically saved as a BigQuery DataFrame with the same name as the title of the SQL cell.

## Interact with the result set

You can interact with the result set as a BigQuery DataFrame or a pandas DataFrame.

You can chain SQL statements using the same SQL cell variable name. For example, you can use BigQuery DataFrames generated by the result set as tables in a following query by enclosing the DataFrame name in braces (`{ }`). See the following example, which references a previous query's output that was saved as a DataFrame named `df`:
    
    
    SELECT * FROM {df};

## What's next

  * [Use visualization cells](https://docs.cloud.google.com/colab/docs/visualization-cells)

  * [Use Gemini to explain and fix errors](https://docs.cloud.google.com/colab/docs/explain-errors)

  * [Use the Data Science Agent](https://docs.cloud.google.com/colab/docs/use-data-science-agent)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
