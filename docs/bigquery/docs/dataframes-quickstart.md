---
url: https://docs.cloud.google.com/bigquery/docs/dataframes-quickstart/
title: Try BigQuery DataFrames \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:39:36.796813+00:00
---

# Try BigQuery DataFrames  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/dataframes-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Try BigQuery DataFrames

BigQuery DataFrames brings scalable Python analytics and machine learning (ML) to BigQuery. Computations execute in BigQuery with server-side processing, which lets you analyze and model large datasets without being constrained by local or notebook memory. You can use syntax similar to pandas (`bigframes.pandas`) and BigQuery ML (`bigframes.bigquery`) without writing SQL.

Use this quickstart to perform the following analysis and ML tasks by using the [BigQuery DataFrames API](https://dataframes.bigquery.dev/reference/index.html) in a [BigQuery notebook](https://docs.cloud.google.com/bigquery/docs/programmatic-analysis):

  * Create a DataFrame over the `bigquery-public-data.ml_datasets.penguins` public dataset.
  * Calculate the average body mass of a penguin.
  * Clean and prepare a subset of the penguin data for training.
  * Train a [linear regression model](https://dataframes.bigquery.dev/reference/api/bigframes.bigquery.ml.create_model.html) by using `bigframes.bigquery.ml.create_model`.
  * [Evaluate](https://dataframes.bigquery.dev/reference/api/bigframes.bigquery.ml.evaluate.html) the model by using `bigframes.bigquery.ml.evaluate`.



## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. Verify that the BigQuery API is enabled.

[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=bigquery)

If you created a new project, the BigQuery API is automatically enabled.




### Required permissions

To create and run notebooks, you need the following Identity and Access Management (IAM) roles:

  * [BigQuery User (`roles/bigquery.user`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.user)
  * [Notebook Runtime User (`roles/aiplatform.notebookRuntimeUser`)](https://docs.cloud.google.com/vertex-ai/docs/general/access-control#aiplatform.notebookRuntimeUser)
  * [Code Creator (`roles/dataform.codeCreator`)](https://docs.cloud.google.com/dataform/docs/access-control#dataform.codeCreator)



## Create a notebook

Follow the instructions in [Create a notebook from the BigQuery editor](https://docs.cloud.google.com/bigquery/docs/create-notebooks#create-notebook-console) to create a new notebook.

## Try BigQuery DataFrames

Try BigQuery DataFrames by following these steps:

  1. Create a new code cell in the notebook.
  2. Add the following code to the code cell:
         
         import bigframes.pandas as bpd
         
         # Set BigQuery DataFrames options
         # Note: The project option is not required in all environments.
         # On BigQuery Studio, the project ID is automatically detected.
         bpd.options.bigquery.project = your_gcp_project_id
         
         # Use "partial" ordering mode to generate more efficient queries, but the
         # order of the rows in DataFrames may not be deterministic if you have not
         # explictly sorted it. Some operations that depend on the order, such as
         # head() will not function until you explictly order the DataFrame. Set the
         # ordering mode to "strict" (default) for more pandas compatibility.
         bpd.options.bigquery.ordering_mode = "partial"
         
         # Create a DataFrame from a BigQuery table
         query_or_table = "bigquery-public-data.ml_datasets.penguins"
         df = bpd.read_gbq(query_or_table)
         
         # Efficiently preview the results using the .peek() method.
         df.peek()
         

  3. Modify the `bpd.options.bigquery.project = your_gcp_project_id` line to specify your Google Cloud project ID. For example, `bpd.options.bigquery.project = "myProjectID"`.

  4. Run the code cell.

The code returns a `DataFrame` object with data about penguins.

  5. Create a new code cell in the notebook and add the following code:
         
         # Use the DataFrame just as you would a pandas DataFrame, but calculations
         # happen in the BigQuery query engine instead of the local system.
         average_body_mass = df["body_mass_g"].mean()
         print(f"average_body_mass: {average_body_mass}")
         

  6. Run the code cell.

The code calculates the average body mass of the penguins and prints it to the Google Cloud console.

  7. Create a new code cell in the notebook and add the following code:
         
         import bigframes.bigquery as bbq
         from google.cloud import [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest)
         
         # Ensure a dataset exists to store the model
         client = [bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).[Client](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html)(project=bpd.[options](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.external_config.ExternalConfig.html#google_cloud_bigquery_external_config_ExternalConfig_options).[bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).project)
         client.[create_dataset](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.client.Client.html#google_cloud_bigquery_client_Client_create_dataset)("bq_quickstart", exists_ok=True)
         
         # Filter down to the Adelie Penguin species
         adelie_data = df[df.species == "Adelie Penguin (Pygoscelis adeliae)"]
         
         # Drop the columns that are not needed
         adelie_data = adelie_data.drop(columns=["species"])
         
         # Drop rows with nulls to get the training data
         training_data = adelie_data.dropna()
         
         # Train a linear regression model
         model_name = f"{bpd.[options](https://docs.cloud.google.com/python/docs/reference/bigquery/latest/google.cloud.bigquery.external_config.ExternalConfig.html#google_cloud_bigquery_external_config_ExternalConfig_options).[bigquery](https://docs.cloud.google.com/python/docs/reference/bigquery/latest).project}.bq_quickstart.penguin_weight"
         model_metadata = bbq.ml.create_model(
             model_name,
             replace=True,
             options={"model_type": "LINEAR_REG"},
             training_data=training_data.rename(columns={"body_mass_g": "label"}),
         )
         
         # Evaluate the model
         evaluation = bbq.ml.evaluate(model_name)
         print(evaluation)
         

  8. Run the code cell.

The code trains the linear regression model directly in BigQuery and returns the model's evaluation metrics.




## Clean up

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Continue learning about [BigQuery DataFrames](https://docs.cloud.google.com/bigquery/docs/bigquery-dataframes-introduction).
  * Learn how to [visualize graphs using BigQuery DataFrames](https://docs.cloud.google.com/bigquery/docs/dataframes-visualizations).
  * Learn how to [use a BigQuery DataFrames notebook](https://github.com/googleapis/python-bigquery-dataframes/tree/main/notebooks/getting_started/getting_started_bq_dataframes.ipynb).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
