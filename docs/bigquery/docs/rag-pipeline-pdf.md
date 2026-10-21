---
url: https://docs.cloud.google.com/bigquery/docs/rag-pipeline-pdf/
title: Parse PDFs in a retrieval-augmented generation pipeline \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:12.059067+00:00
---

# Parse PDFs in a retrieval-augmented generation pipeline  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/rag-pipeline-pdf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback 

#  Parse PDFs in a retrieval-augmented generation pipeline Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial guides you through the process of creating a retrieval-augmented generation (RAG) pipeline based on parsed PDF content. 

PDF files, such as financial documents, can be challenging to use in RAG pipelines because of their complex structure and mix of text, figures, and tables. This tutorial shows you how to use the [`AI.CHUNK_DOCUMENT` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-chunk-document) to build a RAG pipeline based on key information extracted from a PDF file. 

## Objectives

This tutorial covers the following tasks: 

  * Create a Cloud Storage bucket and upload a sample PDF file.
  * Use the [`AI.CHUNK_DOCUMENT` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-chunk-document) to parse the PDF contents into chunks and then write that content to a BigQuery table.
  * Generate embeddings from the chunked PDF content, and then write those embeddings to a BigQuery table. Embeddings are numerical representations of the PDF content that enable you to perform semantic search and retrieval on the PDF content.
  * Use the [`VECTOR_SEARCH` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/search_functions#vector_search) on the embeddings to identify semantically similar PDF content.
  * Perform retrieval-augmented generation (RAG) by using the [`AI.GENERATE` function](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-generate) to generate text, using vector search results to augment the prompt input and improve results. 



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [BigQuery](https://cloud.google.com/bigquery/pricing): You incur costs for the data that you process in BigQuery.
  * [Gemini Enterprise Agent Platform](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing): You incur costs for calls to Agent Platform models.
  * [Document AI](https://cloud.google.com/document-ai/pricing): You incur costs for calls to the Document AI API.
  * [Cloud Storage](https://cloud.google.com/storage/pricing): You incur costs for object storage in Cloud Storage.



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

###  Console 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the BigQuery, BigQuery Connection, Vertex AI, Document AI, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,bigqueryconnection.googleapis.com,aiplatform.googleapis.com,documentai.googleapis.com,storage.googleapis.com)

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the BigQuery, BigQuery Connection, Vertex AI, Document AI, and Cloud Storage APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=bigquery.googleapis.com,bigqueryconnection.googleapis.com,aiplatform.googleapis.com,documentai.googleapis.com,storage.googleapis.com)

  8. Make sure that you have the following role or roles on the project: **Storage Admin** , **Document AI Editor** , **BigQuery Admin** , **Project IAM Admin**

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 



###  gcloud 

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the BigQuery, BigQuery Connection, Vertex AI, Document AI, and Cloud Storage APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable bigquery.googleapis.com bigqueryconnection.googleapis.com aiplatform.googleapis.com documentai.googleapis.com storage.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the BigQuery, BigQuery Connection, Vertex AI, Document AI, and Cloud Storage APIs, if any are not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable bigquery.googleapis.com bigqueryconnection.googleapis.com aiplatform.googleapis.com documentai.googleapis.com storage.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: ` roles/storage.admin, roles/documentai.editor, roles/bigquery.admin, roles/resourcemanager.projectIamAdmin `
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.



## Create a dataset

To create a BigQuery dataset, select one of the following options:

### Console

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the left pane, click explore **Explorer** :

![Highlighted button for the Explorer pane.](https://docs.cloud.google.com/static/bigquery/images/explorer-tab.png)

If you don't see the left pane, click last_page **Expand left pane** to open the pane.

  3. In **Explorer** , expand your project, and then click **Datasets**.

  4. On the **Datasets** page, click add **Create dataset**.

  5. In the **Create dataset** pane, do the following:

     * For **Dataset ID** , enter `bqml_tutorial`.

     * For **Data location** , select **US**.

Leave the remaining default settings as they are.

  6. Click **Create dataset**.




### bq

To create a new dataset, use the [`bq mk --dataset` command](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#mk-dataset).

  1. Create a dataset named `bqml_tutorial` with the data location set to `US`:
         
         bq mk --dataset \
           --location=US \
           --description "BigQuery ML tutorial dataset." \
           bqml_tutorial

  2. Confirm that the dataset was created:
         
         bq ls




###  API 

Call the [`datasets.insert`](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets/insert) method with a defined [dataset resource](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets):
    
    
    {
      "datasetReference": {
         "datasetId": "bqml_tutorial"
      }
    }

## Upload the sample PDF to Cloud Storage

To upload the sample PDF to Cloud Storage, follow these steps:

  1. Download the `scf23.pdf` sample PDF by going to <https://www.federalreserve.gov/publications/files/scf23.pdf> and clicking download download.
  2. [Create a Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets).
  3. [Upload](https://docs.cloud.google.com/storage/docs/uploading-objects) the `scf23.pdf` file to the bucket.



## Parse the PDF file into chunks

Use the document processor with the `AI.CHUNK_DOCUMENT` function to parse the PDF file into chunks, and then write that content to a table:

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, run the following statement: 
         
         CREATE or REPLACE TABLE bqml_tutorial.chunked_pdf AS (
           SELECT *
           FROM AI.CHUNK_DOCUMENT('gs://BUCKET_NAME/scf23.pdf', chunk_size => 250)
         );

  3. In the query editor, run the following query to view a subset of the parsed PDF content:
         
         SELECT
           chunk_id,
           start_page,
           end_page,
           content
         FROM `bqml_tutorial.chunked_pdf`
         ORDER BY chunk_id
         LIMIT 3;

The output is similar to the following:
         
         +----------+------------+----------+-------------------------------------------+
         | chunk_id | start_page | end_page | content                                   |
         +----------+------------+----------+-------------------------------------------+
         | 1        | 1          | 1        | OF NORS. • BOARD OF GOVERNO FEDERAL       |
         |          |            |          | RESERVE SYSTEM RESEARCH & ANALYSIS        |
         | 2        | 1          | 7        | # Changes in U.S. Family Finances from    |
         |          |            |          | 2019 to 2022                              |
         |          |            |          |                                           |
         |          |            |          | Evidence from the Survey of Consumer...   |
         | 3        | 3          | 5        | # Changes in U.S. Family Finances from    |
         |          |            |          | 2019 to 2022                              |
         |          |            |          |                                           |
         |          |            |          | ## Contents...                            |
         +----------+------------+----------+-------------------------------------------+
         




## Generate embeddings

Generate embeddings for the parsed PDF content and then write them to a table:

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, run the following statement:
         
         CREATE OR REPLACE TABLE `bqml_tutorial.embeddings` AS (
           SELECT *, AI.EMBED(content, endpoint => 'text-embedding-005').result AS embedding
           FROM bqml_tutorial.chunked_pdf
         );




## Run a vector search

Run a vector search against the parsed PDF content.

The following query takes text input, creates an embedding for that input using the `AI.EMBED` function, and then uses the `VECTOR_SEARCH` function to match the input embedding with the most similar PDF content embeddings. The results are the top ten PDF chunks that are most related to changes in family net worth.

  1. Go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, run the following SQL statement:
         
         SELECT
           distance,
           base.chunk_id AS chunk_id,
           base.start_page AS start_page,
           base.end_page AS end_page,
           base.content
         FROM
           VECTOR_SEARCH(
             TABLE `bqml_tutorial.embeddings`,
             'embedding',
             query_value =>
               AI.EMBED(
                 'Did the typical family net worth increase? If so, by how much?',
                 endpoint => 'text-embedding-005').result,
             top_k => 3,
             OPTIONS => '{"fraction_lists_to_search": 0.01}')
         ORDER BY distance DESC;

The output is similar to the following:
         
         +----------+----------+------------+----------+-----------------------------------+
         | distance | chunk_id | start_page | end_page | content                           |
         +----------+----------+------------+----------+-----------------------------------+
         | 0.608587 | 25       | 17         | 18       | # Net Worth                       |
         |          |          |            |          |                                   |
         |          |          |            |          | 18 Between the first quarter of   |
         |          |          |            |          | 2019 and the first quarter of...  |
         +----------+----------+------------+----------+-----------------------------------+
         | 0.606387 | 29       | 19         | 21       | ## Net Worth                      |
         |          |          |            |          |                                   |
         |          |          |            |          | ## Net Worth by Family            |
         |          |          |            |          | Characteristics...                |
         +----------+----------+------------+----------+-----------------------------------+
         | 0.599438 | 23       | 17         | 21       | # Net Worth                       |
         |          |          |            |          |                                   |
         |          |          |            |          | The net improvements in...        |
         +----------+----------+------------+----------+-----------------------------------+
         




## Generate text augmented by vector search results

Perform a vector search on the embeddings to identify semantically similar PDF content, and then use the `AI.GENERATE` function with the vector search results to augment the prompt input and improve the text generation results. In this case, the query uses information from the PDF chunks to answer a question about the change in family net worth over the past decade.

  1. In the Google Cloud console, go to the **BigQuery** page.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  2. In the query editor, run the following statement:
         
         SELECT
           AI.GENERATE(
             CONCAT('Did the typical family net worth change? How does this compare the SCF survey a decade earlier? Be concise and use the following context:',
                     STRING_AGG(FORMAT("context: %s", base.content), ',\n')
             )
           ).result AS response
         FROM
           VECTOR_SEARCH(
             TABLE `bqml_tutorial.embeddings`,
             'embedding',
             query_value =>
               AI.EMBED(
                 'Did the typical family net worth increase? If so, by how much?',
                 endpoint => 'text-embedding-005').result,
             top_k => 3,
             OPTIONS => '{"fraction_lists_to_search": 0.01}')

The output is similar to the following:
         
         +-------------------------------------------------------------------------+
         | response                                                                |
         +-------------------------------------------------------------------------+
         | Yes, the typical family net worth changed significantly. Between 2019   |
         | and 2022, real median net worth surged by 37% to $192,900.              |
         |                                                                         |
         | This growth contrasts sharply with the period a decade earlier. Between |
         | the 2010 and 2013 SCF surveys, real median net worth actually decreased |
         | by 2%.                                                                  |
         +-------------------------------------------------------------------------+
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




## What's next

  * Learn more about [embeddings and vector search](https://docs.cloud.google.com/bigquery/docs/vector-search-intro).
  * Learn more about performing [semantic search and RAG](https://docs.cloud.google.com/bigquery/docs/vector-index-text-search-tutorial). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
