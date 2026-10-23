---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/try-media-recommendations/
title: Get started with media recommendations \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:39.827722+00:00
---

# Get started with media recommendations  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/try-media-recommendations/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Get started with media recommendations

You can quickly build a state-of-the-art media recommendations app. Media recommendations enable your audiences to discover more personalized content, like what to watch or read next, with Google-quality results that are customized by optimization objectives.

For general information about Agent Search for media, see [Introduction to media search and recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media). 

In this getting-started tutorial, you will use the [Movielens](https://grouplens.org/datasets/movielens/) dataset to demonstrate how to upload your media content catalog and user events into Agent Search and train a personalized movie recommendation model. The Movielens dataset contains a catalog of movies (documents) and user movie ratings (user events).

In this tutorial, you train a recommendation model of type Others You May Like optimized for click-through-rate (CTR). After training, the model can recommend movies based on a user ID and on a seed movie.

To meet the minimum data requirements for the model, each positive movie rating (4 or higher) is treated as a view-item event.

Estimated time to complete this tutorial:

  * Initial steps to start training the model: ~1.5 hours.
  * Waiting for the model to train: ~24 hours. (Train the model)
  * Evaluating the model predictions and cleaning up: ~30 minutes. (Preview recommendations)



If you completed the [Get started with media search](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-media-search) tutorial and you still have the data store (suggested name `quickstart-media-data-store`), then you can use that data store instead of creating another. In this case, you should begin the tutorial at Create an app for media recommendations.

## Objectives

  * Learn how to import media documents and user events data from BigQuery into Agent Search.
  * Train and evaluate recommendation models.



Before following this tutorial, make sure you have done the steps in [Before you begin](https://docs.cloud.google.com/generative-ai-app-builder/docs/before-you-begin).

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/gen-app-builder/?tutorial=generative-ai-app-builder--genappbuilder-media-recommendations-intro)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Agent Search (Discovery Engine), Cloud Storage, BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=discoveryengine.googleapis.com,storage.googleapis.com,bigquery.googleapis.com)

  5. Make sure that you have the following role or roles on the project: Discovery Engine Admin and BigQuery Admin. 

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

  6. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Agent Search (Discovery Engine), Cloud Storage, BigQuery APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=discoveryengine.googleapis.com,storage.googleapis.com,bigquery.googleapis.com)

  9. Make sure that you have the following role or roles on the project: Discovery Engine Admin and BigQuery Admin. 

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




## Prepare the dataset

You use the Cloud Shell to import the Movielens dataset and restructure the dataset for Agent Search for media.

### Open the Cloud Shell

  1. Open [Google Cloud console](https://console.cloud.google.com/).
  2. Select your Google Cloud project.
  3. Take note of the project ID in the **Project info** card on the dashboard page. You will need the project ID for the following procedures. 
  4. Click the **Activate Cloud Shell** button at the top of the console. A Cloud Shell session opens inside a new frame at the bottom of the Google Cloud console and displays a command-line prompt. For other ways to launch the Cloud Shell, see [Launch Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell).

![Cloud Shell](https://docs.cloud.google.com/static/generative-ai-app-builder/images/tutorial-cloud-shell.png)




### Import the dataset

The Movielens dataset is available in a public Cloud Storage bucket to make it easier to import.

  1. Run the following using your project ID to set the default project for the command-line.
         
         gcloud config set project PROJECT_ID
         

  2. Create a BigQuery dataset:
         
         bq mk movielens
         

  3. Load `movies.csv` into a new `movies` BigQuery table:
         
         bq load --skip_leading_rows=1 movielens.movies \
           gs://cloud-samples-data/gen-app-builder/media-recommendations/movies.csv \
           movieId:integer,title,genres
         

  4. Load `ratings.csv` into a new `ratings` BigQuery table:
         
         bq load --skip_leading_rows=1 movielens.ratings \
           gs://cloud-samples-data/gen-app-builder/media-recommendations/ratings.csv \
           userId:integer,movieId:integer,rating:float,time:timestamp
         




### Create BigQuery views

In this step, you restructure the Movielens dataset so it follows the expected format for media recommendations.

Media recommendations require user events data in order to create a model. For this guide, you create fake `view-item` events during the past 90 days from positive ratings (`>= 4`).

  1. Create a view that converts the movies table into the Google-defined [`Document` schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-documents#json-schema):
         
         bq mk --project_id=PROJECT_ID \
          --use_legacy_sql=false \
          --view '
           WITH t AS (
             SELECT
               CAST(movieId AS string) AS id,
               SUBSTR(title, 0, 128) AS title,
               SPLIT(genres, "|") AS categories
               FROM `PROJECT_ID.movielens.movies`)
             SELECT
               id, "default_schema" as schemaId, null as parentDocumentId,
               TO_JSON_STRING(STRUCT(title as title, categories as categories,
               CONCAT("http://mytestdomain.movie/content/", id) as uri,
               "2023-01-01T00:00:00Z" as available_time,
               "2033-01-01T00:00:00Z" as expire_time,
               "movie" as media_type)) as jsonData
             FROM t;' \
         movielens.movies_view
         

Now, the new view has the schema that the Discovery Engine API expects.

  2. Go to the **BigQuery** page in Google Cloud console.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  3. In the **Explorer** pane, expand your project name, expand the **`movielens`** dataset and click **`movies_view`** to open the query page for this view.

  4. Go to the **Table explorer** tab.

  5. In the **Generated query** pane, click the **Copy to query** button. The query editor opens.

  6. Click **Run** to see movie data in the view that you created.




### Create user events

  1. Create fictitious [user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-user-events) from movie ratings by running the following Cloud Shell command:
         
         bq mk --project_id=PROJECT_ID \
          --use_legacy_sql=false \
          --view '
          WITH t AS (
           SELECT
             MIN(UNIX_SECONDS(time)) AS old_start,
             MAX(UNIX_SECONDS(time)) AS old_end,
             UNIX_SECONDS(TIMESTAMP_SUB(
             CURRENT_TIMESTAMP(), INTERVAL 90 DAY)) AS new_start,
             UNIX_SECONDS(CURRENT_TIMESTAMP()) AS new_end
           FROM `PROJECT_ID.movielens.ratings`)
           SELECT
             CAST(userId AS STRING) AS userPseudoId,
             "view-item" AS eventType,
             FORMAT_TIMESTAMP("%Y-%m-%dT%X%Ez",
             TIMESTAMP_SECONDS(CAST(
               (t.new_start + (UNIX_SECONDS(time) - t.old_start) *
               (t.new_end - t.new_start) / (t.old_end - t.old_start))
             AS int64))) AS eventTime,
             [STRUCT(movieId AS id, null AS name)] AS documents,
           FROM `PROJECT_ID.movielens.ratings`, t
           WHERE rating >= 4;' \
           movielens.user_events
         




## Activate Agent Search

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Optional: Click **Allow Google to selectively sample model input and responses**.

  3. Click **Continue and activate the API**.




## Create an app for media recommendations

The procedures in this section guide you through creating and deploying a media recommendations app.

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Click **Create app**.

  3. On the **Create app** page, under **Media recommendations** , click **Create**.

  4. In the **App name** field, enter a name for your app, such as `quickstart-media-recommendations`. Your app ID appears under the app name.

  5. Under **Recommendations type** , make sure **Others you may like** is selected.

  6. Under **Business Objective** , make sure **Click-through rate (CTR)** is selected.

  7. Click **Continue**.

  8. Create a data store.

**Note:** If you completed the [Get started with media search](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-media-search) tutorial and you still have the data store (suggested name `quickstart-media-data-store`), then select it, click **Create** , and skip to Train the recommendation model.
     1. On the **Data Stores** page, click **Create data store**.

     2. Enter a display name for your data store, such as `quickstart-media-data-store`, and then click **Create**.

  9. Select the data store you just created, and then click **Create** to create your app.




## Import data

Next, import the movies and user events data that were formatted earlier.

### Import documents

Import the `movies_view` document created in the Create BigQuery views section to your `quickstart-media-data-store` data store.

  1. Under **Native sources** on the **Import documents** page, select **BigQuery**.

  2. Enter the name of the `movies` BigQuery view that you created and click **Import**.
         
         PROJECT_ID.movielens.movies_view
         

  3. Wait until all documents have been imported, which should take about 15 minutes. There should be 86537 documents when complete.

You can check the **Activity** tab for the import operation status. When the import is complete, the import operation status changes to **Completed**.




### Import user events

**Note:** User events are required to train your app and to generate recommendations.

Import the `user_events` records created in the Create BigQuery views section to your data store.

  1. On the **Events** tab, click **Import Events**.

  2. Under **Native sources** on the Import documents page, select **BigQuery**.

  3. Enter the name of the `user_events` BigQuery view that you created and click **Import**.
         
         PROJECT_ID.movielens.user_events
         

  4. Wait until at least a million events have been imported before proceeding to the next step, in order to meet the data requirements for training a new model.

You can check the **Activity** tab for the operation status. The process takes about an hour to complete because you are importing millions of rows.

  5. To see if the requirements have been met, go to the **Data quality** > **Requirements** tab. Even after the user events have been imported, it can take some time for the **Requirements** tab to update its status to **Data requirements met**.




## Train the recommendation model

  1. Go to the **Configurations** page.

  2. Click the **Control** tab. A serving config has already been created.

If you want to adjust the [**Recommendation demotion**](https://docs.cloud.google.com/generative-ai-app-builder/docs/demote-recommendations) or [**Result diversification**](https://docs.cloud.google.com/generative-ai-app-builder/docs/diversify-recommendations) settings, you can do so on this page.

  3. Click the **Training** tab.

After the data requirements have been met, the model begins training automatically. You can view the training and tuning status on this page.

It might take a couple of days for the model to train and become ready to query. The **Ready to query** field indicates **Yes** when the process is complete. You need to refresh the page to see the change **No** to **Yes**.




## Preview recommendations

After the model is ready to query:

  1. In the navigation menu, click **Preview**.

  2. Click the **Document ID** field. A list of document IDs appears.

  3. Enter a seed document (movie) ID, such as `4993` for "The Lord of the Rings: The Fellowship of the Ring (2001)".

![Enter ID](https://docs.cloud.google.com/static/generative-ai-app-builder/images/tutorial-evaluate.png)

  4. Select the **Serving config** name from the drop-down menu.

  5. Click **Get recommendations**. A list of recommended documents appears.




## Deploy your app for structured data

There is no recommendations widget for deploying your app. To test your app before deployment:

  1. Go to the **Data** page, **Documents** tab, and copy a document **ID**.

  2. Go to the **Integration** page. This page includes a sample command for the [`servingConfigs.recommend`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1beta/projects.locations.dataStores.servingConfigs/recommend) method in the REST API.

  3. Paste the document ID you copied earlier into the **Document ID** field.

  4. Leave the **User Pseudo ID** field as is.

  5. Copy the example request and run it in Cloud Shell.




For help integrating the recommendations app into your web app, see the code samples at [Get media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-recommendations#get-media-recommendations).

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

You can reuse the data store you created for media search in the [Get started with media search](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-media-search) tutorial. Try that tutorial before doing this clean up procedure.

  1. To avoid unnecessary Google Cloud charges, use the [Google Cloud console](https://console.cloud.google.com/) to delete your project if you don't need it.
  2. If you created a new project to learn about Agent Search and you no longer need the project, [delete the project](https://console.cloud.google.com/cloud-resource-manager).
  3. If you used an existing Google Cloud project, delete the resources you created to avoid incurring charges to your account. For more information, see [Delete an app](https://docs.cloud.google.com/generative-ai-app-builder/docs/delete-engine).
  4. Follow the steps in [Turn off Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/turn-off-enterprise-search).
  5. If you created a BigQuery dataset, delete it in Cloud Shell:
         
         bq rm --recursive --dataset movielens
         




## What's next

  * [Introduction to Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction)
  * [About apps and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
