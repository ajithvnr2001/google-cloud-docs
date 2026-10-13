---
url: https://docs.cloud.google.com/lakehouse/docs/forecast-demand-customer-feedback-tutorial/
title: Forecast demand from customer feedback using Lakehouse and AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:42.068920+00:00
---

# Forecast demand from customer feedback using Lakehouse and AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/forecast-demand-customer-feedback-tutorial/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Forecast demand from customer feedback using Lakehouse and AI Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to analyze unstructured free-text customer feedback with structured sales data in Lakehouse to evaluate a new product launch.

Imagine you're a data scientist at Froyo, a fictional frozen yogurt company that plans to launch a new flavor called _Midnight Swirl_. Before committing to a global launch, the business needs to answer three questions:

  * What allergens and customer feedback concerns apply to the new flavor?
  * How much demand should the company expect across existing flavors over the next 12 months?
  * How do customer sentiment and repeat-purchase intent compare with forecasted demand?



This tutorial is intended for data analysts, data scientists, and data engineers who are familiar with BigQuery and basic SQL. You complete every step using Cloud Shell and the Google Cloud console.

## Objectives

  * Create a catalog in the [Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs), and then create Apache Iceberg tables that store product, sales, and customer feedback data in your Lakehouse.
  * Use the BigQuery AI functions `AI.CLASSIFY` and `AI.IF` to extract sentiment, topics, and purchase intent from unstructured text stored in an Iceberg table.
  * Use conversational analytics in BigQuery Studio to forecast 12-month demand with `AI.FORECAST` and join the forecast with product and feedback insights.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Lakehouse](https://cloud.google.com/products/biglake/pricing)
  * [BigQuery](https://cloud.google.com/bigquery/pricing), including conversational analytics 
  * [Cloud Storage](https://cloud.google.com/storage/pricing)
  * [Gemini Enterprise Agent Platform](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing), for the Gemini models that AI functions call 



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or [create a Google Cloud project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

**Note:** If you don't plan to keep the resources that you create in this tutorial, create a new project instead of selecting an existing project. After you finish, you can delete the project to remove all resources associated with it.
  2. [Verify that billing is enabled](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#console) for your Google Cloud project.




### Required roles

To get the permissions that you need to complete the tasks in this tutorial, ask your administrator to grant you the following IAM roles on your project: 

  * Create and delete the catalog, namespace, and tables in the Lakehouse runtime catalog: [BigLake Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/biglake#biglake.admin) (`roles/biglake.admin`) 
  * Create and delete a Cloud Storage bucket, and grant the catalog service account access to it: [Storage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) 
  * Create and modify tables from BigQuery: [BigQuery Data Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.dataEditor) (`roles/bigquery.dataEditor`) 
  * Run queries and use conversational analytics in BigQuery Studio: 
    * [BigQuery Studio User ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.studioUser) (`roles/bigquery.studioUser`)
    * [Gemini Data Analytics Stateless Chat User ](https://docs.cloud.google.com/iam/docs/roles-permissions/geminidataanalytics#geminidataanalytics.dataAgentStatelessUser) (`roles/geminidataanalytics.dataAgentStatelessUser`)
    * [Gemini for Google Cloud User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.user) (`roles/cloudaicompanion.user`)
  * Call Gemini models from BigQuery AI functions: [Agent Platform User ](https://docs.cloud.google.com/iam/docs/roles-permissions/aiplatform#aiplatform.user) (`roles/aiplatform.user`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Prepare your environment

Activate Cloud Shell, set environment variables for your resources, and enable the required APIs:

  1. In the Google Cloud console, activate Cloud Shell. If you're prompted, click **Authorize**.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

  2. In Cloud Shell, set environment variables for your project ID, region, bucket name, catalog ID, and namespace so that you can reuse them throughout this tutorial:
         
         export PROJECT_ID=$(gcloud config get-value project)
         export REGION="us-central1"
         export BUCKET_NAME="${PROJECT_ID}-froyo-lakehouse"
         export CATALOG_ID="froyo_catalog"
         export NAMESPACE_ID="froyo_lakehouse"

  3. Enable the required APIs for your project:

     * BigQuery API (`bigquery.googleapis.com`)
     * BigLake API (`biglake.googleapis.com`), which provides access to the Lakehouse runtime catalog
     * Cloud Storage API (`storage.googleapis.com`)
     * Agent Platform API (`aiplatform.googleapis.com`)
     * Conversational Analytics API (`geminidataanalytics.googleapis.com`)
     * Gemini for Google Cloud API (`cloudaicompanion.googleapis.com`)

Enable these APIs in Cloud Shell:
    
    gcloud services enable \
        bigquery.googleapis.com \
        biglake.googleapis.com \
        storage.googleapis.com \
        aiplatform.googleapis.com \
        geminidataanalytics.googleapis.com \
        cloudaicompanion.googleapis.com \
        --project=${PROJECT_ID}




## Create a Cloud Storage bucket

In Cloud Shell, create a Cloud Storage bucket to store your Iceberg table files:
    
    
    gcloud storage buckets create gs://${BUCKET_NAME} \
        --project=${PROJECT_ID} \
        --location=${REGION}

## Create a catalog in the Lakehouse runtime catalog

Using the [Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint), create a catalog in credential vending mode so that the catalog uses its auto-provisioned service account to access your bucket, and you don't need to create a BigQuery connection:

  1. In Cloud Shell, create a multiple-bucket catalog in credential vending mode:
         
         gcloud biglake iceberg catalogs create ${CATALOG_ID} \
             --project=${PROJECT_ID} \
             --catalog-type=biglake \
             --default-location=gs://${BUCKET_NAME} \
             --primary-location=${REGION} \
             --credential-mode=vended-credentials

  2. Grant the catalog's auto-provisioned service account the Storage Object User (`roles/storage.objectUser`) role on your bucket:
         
         CATALOG_SA=$(gcloud biglake iceberg catalogs describe ${CATALOG_ID} \
             --project=${PROJECT_ID} \
             --format='value(biglake-service-account)')
         
         gcloud storage buckets add-iam-policy-binding gs://${BUCKET_NAME} \
             --member="serviceAccount:${CATALOG_SA}" \
             --role="roles/storage.objectUser"

  3. Create a namespace for your tables in the catalog:
         
         gcloud biglake iceberg namespaces create ${NAMESPACE_ID} \
             --project=${PROJECT_ID} \
             --catalog=${CATALOG_ID}




## Create Iceberg tables

Create three Iceberg tables in your catalog and load them with sample data:

  * `products`: Stores the product list, including the new Midnight Swirl flavor and the existing flavor that it's based on.
  * `sales_history`: Stores 24 months of monthly unit sales for the existing flavors, by region.
  * `customer_feedback`: Stores feedback records. Each row pairs structured metadata (`feedback_id`, `submitted_date`, `flavor_name`, and `channel`) with a `comment` `STRING` column that stores unstructured free text.



In BigQuery, you reference Lakehouse tables using the four-part [P.C.N.T. naming structure](https://docs.cloud.google.com/lakehouse/docs/key-concepts#pcnt-naming-structure) (**Project.Catalog.Namespace.Table**).

  1. In Cloud Shell, create the `products`, `sales_history`, and `customer_feedback` tables and populate them with sample data. The script runs each statement in order and takes about a minute to complete:
         
         bq query --project_id=${PROJECT_ID} --location=${REGION} --use_legacy_sql=false << EOF
         -- Product list.
         CREATE TABLE \`${PROJECT_ID}.${CATALOG_ID}.${NAMESPACE_ID}.products\` (
           product_name STRING,
           base_flavor STRING,
           status STRING,
           allergens STRING,
           target_regions STRING);
         
         INSERT INTO \`${PROJECT_ID}.${CATALOG_ID}.${NAMESPACE_ID}.products\` VALUES
           ('Midnight Swirl', 'Classic Chocolate', 'Planned launch',
            'Milk, Soy', 'North America, Europe'),
           ('Classic Chocolate', 'Classic Chocolate', 'In market',
            'Milk, Soy', 'North America, Europe, Asia Pacific'),
           ('Vanilla Bean', 'Vanilla Bean', 'In market',
            'Milk', 'North America, Europe, Asia Pacific'),
           ('Strawberry Swirl', 'Strawberry Swirl', 'In market',
            'Milk', 'North America, Europe, Asia Pacific');
         
         -- Monthly sales history for the flavors that are in market.
         CREATE TABLE \`${PROJECT_ID}.${CATALOG_ID}.${NAMESPACE_ID}.sales_history\` (
           sale_month DATE,
           flavor_name STRING,
           region STRING,
           units_sold INT64);
         
         INSERT INTO \`${PROJECT_ID}.${CATALOG_ID}.${NAMESPACE_ID}.sales_history\`
         WITH
           months AS (
             SELECT sale_month
             FROM UNNEST(GENERATE_DATE_ARRAY(
               '2024-01-01', '2025-12-01', INTERVAL 1 MONTH)) AS sale_month
           ),
           flavors AS (
             SELECT * FROM UNNEST([
               STRUCT('Classic Chocolate' AS flavor_name, 1200 AS base_units),
               ('Vanilla Bean', 1000),
               ('Strawberry Swirl', 800)])
           ),
           regions AS (
             SELECT * FROM UNNEST([
               STRUCT('North America' AS region, 1.0 AS region_factor),
               ('Europe', 0.8),
               ('Asia Pacific', 0.6)])
           )
         SELECT
           m.sale_month,
           f.flavor_name,
           r.region,
           CAST(
             f.base_units * r.region_factor
             -- Two percent month-over-month growth.
             * (1 + 0.02 * DATE_DIFF(m.sale_month, DATE '2024-01-01', MONTH))
             -- Seasonal peak in July.
             * (1 + 0.25 * SIN(2 * ACOS(-1)
                 * (EXTRACT(MONTH FROM m.sale_month) - 4) / 12))
             AS INT64) AS units_sold
         FROM months AS m
         CROSS JOIN flavors AS f
         CROSS JOIN regions AS r;
         
         -- Customer feedback records with unstructured text in the comment column.
         CREATE TABLE \`${PROJECT_ID}.${CATALOG_ID}.${NAMESPACE_ID}.customer_feedback\` (
           feedback_id INT64,
           submitted_date DATE,
           flavor_name STRING,
           channel STRING,
           comment STRING);
         
         INSERT INTO \`${PROJECT_ID}.${CATALOG_ID}.${NAMESPACE_ID}.customer_feedback\` VALUES
           (1, '2025-11-03', 'Midnight Swirl', 'Taste panel',
            "Rich, deep chocolate with a hint of salt. Honestly better than the classic chocolate. I'd order this every week."),
           (2, '2025-11-03', 'Midnight Swirl', 'Taste panel',
            "Loved the dark chocolate swirl, but it was a bit too bitter for my kids."),
           (3, '2025-11-04', 'Midnight Swirl', 'Taste panel',
            "Best froyo I've tried this year. Smooth texture and not too sweet."),
           (4, '2025-11-04', 'Midnight Swirl', 'Taste panel',
            "Great taste. I'd definitely buy it again if it's priced like the other flavors."),
           (5, '2025-11-05', 'Midnight Swirl', 'Taste panel',
            "Does this contain soy? I have a soy allergy so I skipped it. Please label it clearly."),
           (6, '2025-11-05', 'Midnight Swirl', 'Taste panel',
            "Tastes like a premium dessert. The sea salt really makes it."),
           (7, '2025-06-12', 'Classic Chocolate', 'App review',
            "Solid chocolate flavor, my go-to order."),
           (8, '2025-07-02', 'Classic Chocolate', 'App review',
            "It's fine, but a little too sweet compared to other brands."),
           (9, '2025-08-19', 'Classic Chocolate', 'Support email',
            "Consistently good. I wish the cups were bigger for the price."),
           (10, '2025-09-07', 'Classic Chocolate', 'Support email',
            "My chocolate froyo was icy this time and the texture was off."),
           (11, '2025-10-21', 'Classic Chocolate', 'App review',
            "Classic for a reason. Always creamy. I'll keep ordering it."),
           (12, '2025-11-05', 'Classic Chocolate', 'Taste panel',
            "Good but forgettable next to the new dark chocolate sample."),
           (13, '2025-05-14', 'Vanilla Bean', 'App review',
            "Real vanilla flavor, you can see the specks. Love it."),
           (14, '2025-06-30', 'Vanilla Bean', 'App review',
            "Pretty plain. I only order it as a base for toppings."),
           (15, '2025-08-02', 'Vanilla Bean', 'App review',
            "Creamy and simple, perfect for my toddler."),
           (16, '2025-09-15', 'Vanilla Bean', 'Support email',
            "The store was out of vanilla bean two weekends in a row."),
           (17, '2025-06-08', 'Strawberry Swirl', 'App review',
            "Tastes like fresh strawberries. Great in the summer."),
           (18, '2025-07-26', 'Strawberry Swirl', 'App review',
            "Too artificial tasting. Not a fan."),
           (19, '2025-08-11', 'Strawberry Swirl', 'Support email',
            "My favorite flavor. Please never discontinue it."),
           (20, '2025-10-03', 'Strawberry Swirl', 'App review',
            "The price went up, but it's still worth it.");
         EOF

  2. Verify that your catalog lists the `products`, `sales_history`, and `customer_feedback` tables:
         
         gcloud biglake iceberg tables list \
             --project=${PROJECT_ID} \
             --catalog=${CATALOG_ID} \
             --namespace=${NAMESPACE_ID}




## Analyze feedback with AI functions

The `comment` column in the `customer_feedback` table contains unstructured text that you can't aggregate or join directly. Use BigQuery AI functions to extract structured values from each comment and create a new `feedback_insights` table:

  * [`AI.CLASSIFY`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-classify) assigns each comment a sentiment (`positive`, `neutral`, or `negative`) and a primary topic (such as `taste`, `texture`, `price`, or `allergens`) from lists of categories that you define.
  * [`AI.IF`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-if) evaluates a natural-language condition for each comment and returns a `BOOL` value. In this case, the value indicates whether the customer intends to buy the product again.



These managed AI functions use your user credentials to call Gemini, so you don't need to create a remote model or connection.

  1. In Cloud Shell, create and populate the `feedback_insights` table:
         
         bq query --project_id=${PROJECT_ID} --location=${REGION} --use_legacy_sql=false << EOF
         CREATE TABLE \`${PROJECT_ID}.${CATALOG_ID}.${NAMESPACE_ID}.feedback_insights\` (
           feedback_id INT64,
           flavor_name STRING,
           channel STRING,
           comment STRING,
           sentiment STRING,
           topic STRING,
           would_buy_again BOOL);
         
         INSERT INTO \`${PROJECT_ID}.${CATALOG_ID}.${NAMESPACE_ID}.feedback_insights\`
         SELECT
           feedback_id,
           flavor_name,
           channel,
           comment,
           AI.CLASSIFY(
             comment,
             categories => ['positive', 'neutral', 'negative']) AS sentiment,
           AI.CLASSIFY(
             comment,
             categories => ['taste', 'texture', 'price', 'allergens',
                            'availability', 'other']) AS topic,
           AI.IF(
             ('This customer says or implies that they would buy the product ',
              'again. Comment: ', comment)) AS would_buy_again
         FROM \`${PROJECT_ID}.${CATALOG_ID}.${NAMESPACE_ID}.customer_feedback\`;
         EOF

  2. Summarize the feedback metrics for each flavor:
         
         bq query --project_id=${PROJECT_ID} --location=${REGION} --use_legacy_sql=false << EOF
         SELECT
           flavor_name,
           COUNT(*) AS comments,
           COUNTIF(sentiment = 'positive') AS positive,
           COUNTIF(would_buy_again) AS would_buy_again,
           ROUND(COUNTIF(sentiment = 'positive') / COUNT(*), 2) AS positive_share
         FROM \`${PROJECT_ID}.${CATALOG_ID}.${NAMESPACE_ID}.feedback_insights\`
         GROUP BY flavor_name
         ORDER BY positive_share DESC;
         EOF

The output is similar to the following:
         
         +-------------------+----------+----------+-----------------+----------------+
         |    flavor_name    | comments | positive | would_buy_again | positive_share |
         +-------------------+----------+----------+-----------------+----------------+
         | Strawberry Swirl  |        4 |        3 |               2 |           0.75 |
         | Midnight Swirl    |        6 |        4 |               3 |           0.67 |
         | Vanilla Bean      |        4 |        2 |               2 |            0.5 |
         | Classic Chocolate |        6 |        2 |               3 |           0.33 |
         +-------------------+----------+----------+-----------------+----------------+
         




## Forecast demand with conversational analytics

[Conversational analytics](https://docs.cloud.google.com/lakehouse/docs/conversational-analytics) in BigQuery Studio lets you analyze your Iceberg tables using natural language. It retrieves table schemas from the Lakehouse runtime catalog, generates and runs BigQuery SQL (including AI functions such as [`AI.FORECAST`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-ai-forecast)), and returns tables and charts directly in the chat.

### Start a conversation with your tables

  1. In the Google Cloud console, go to the BigQuery **Agents** page.

[Go to Agents](https://console.cloud.google.com/bigquery/agents_hub)

  2. In the BigQuery Studio editor pane, click the **Agents** tab to open the conversation pane, and then click **New chat**.

  3. In the **Chat with your data** pane, click the **Knowledge sources** tab. In the **Search for sources** field, search for and select your three Iceberg tables by using the following values. Replace `PROJECT_ID` with your project ID:

     * `PROJECT_ID.froyo_catalog.froyo_lakehouse.products`
     * `PROJECT_ID.froyo_catalog.froyo_lakehouse.feedback_insights`
     * `PROJECT_ID.froyo_catalog.froyo_lakehouse.sales_history`
**Tip:** To filter the list, enter `namespace: froyo_lakehouse` or `catalog: froyo_catalog` in the **Search for sources** field.
  4. Click **Chat**.




### Ask questions to forecast demand and evaluate the launch

Ask a sequence of natural-language questions to answer the three business questions for the Midnight Swirl launch:

  1. In the **Ask a question** field, enter the following prompt to check Midnight Swirl's product details and customer feedback, and then click send_spark **Send** :
         
         Using products and feedback_insights, what are Midnight Swirl's allergens,
         base flavor, positive sentiment share, would_buy_again count, and customer
         concerns from negative or neutral comments?
         

The agent queries both tables and reports that Midnight Swirl is based on Classic Chocolate and contains milk and soy. It also reports a 0.67 positive sentiment share, with three of six customers intending to buy it again, and highlights concerns about soy allergen labeling and dark chocolate bitterness.

  2. Enter the following prompt to forecast 12-month demand across existing flavors, and then click send_spark **Send** :
         
         Forecast monthly sales by flavor for the next 12 months, plotting only the
         trend lines without confidence intervals.
         

Conversational analytics runs a query with `AI.FORECAST`, which uses the built-in [TimesFM model](https://docs.cloud.google.com/bigquery/docs/timesfm-model) in BigQuery ML without training a separate model, and displays a chart of the 12-month forecast for each flavor.

  3. Enter the following prompt to combine the demand forecast with customer feedback and get launch recommendations, and then click send_spark **Send** :
         
         Join the total 12-month forecasted units_sold for each flavor with its
         positive sentiment share, would_buy_again count, and top complaint topics
         from feedback_insights, and recommend next steps for the Midnight Swirl
         launch.
         

  4. Optional: To inspect the generated SQL query or view the agent's reasoning steps, expand **Show thinking**.




From here, you can ask follow-up questions in the conversation (such as breaking down the forecast by region) or click **Create Agent** in the **Details** pane to save and share a reusable [data agent](https://docs.cloud.google.com/bigquery/docs/create-data-agents) with your team.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete individual resources

If you want to keep your project, delete the individual resources that you created.

  1. To delete your conversation, in the BigQuery Studio editor pane, select the **Agents** tab. In the left navigation panel, which you might need to expand, find your conversation under **Recent chats** , and then click more_vert **View actions > Delete**.

  2. In Cloud Shell, delete the four tables, the namespace, the catalog, and the Cloud Storage bucket:
         
         for TABLE in products sales_history customer_feedback feedback_insights; do
           gcloud biglake iceberg tables delete ${TABLE} \
               --project=${PROJECT_ID} \
               --catalog=${CATALOG_ID} \
               --namespace=${NAMESPACE_ID} \
               --quiet
         done
         
         gcloud biglake iceberg namespaces delete ${NAMESPACE_ID} \
             --project=${PROJECT_ID} \
             --catalog=${CATALOG_ID} \
             --quiet
         
         gcloud biglake iceberg catalogs delete ${CATALOG_ID} \
             --project=${PROJECT_ID} \
             --quiet
         
         gcloud storage rm -r gs://${BUCKET_NAME}




## What's next

To explore more ways to work with your Lakehouse data, see the following resources:

  * Learn more about querying Iceberg tables in natural language with [conversational analytics in Lakehouse](https://docs.cloud.google.com/lakehouse/docs/conversational-analytics).
  * Configure custom instructions, verified queries, and business glossaries by [creating data agents in BigQuery](https://docs.cloud.google.com/bigquery/docs/create-data-agents).
  * Generate descriptions and suggested queries for your tables with [data insights](https://docs.cloud.google.com/lakehouse/docs/dataplex-insights-support).
  * Learn how to [manage Iceberg tables in the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/manage-tables).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
