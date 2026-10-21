---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/try-media-search/
title: Get started with media search \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:27:59.319036+00:00
---

# Get started with media search  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/try-media-search/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Get started with media search

You can quickly build a state-of-the-art media search app. Media search enables your audiences to discover content, with Google-quality results.

For general information about Agent Search for media, see [Introduction to media search and recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media). 

In this getting-started tutorial, you will use the [Movielens](https://grouplens.org/datasets/movielens/) dataset to demonstrate how to upload your media content catalog into Agent Search. The Movielens dataset contains a catalog of movies (documents).

After uploading the movie data, you'll create a search app and test it through the preview page.

If you completed the [Get started with media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-media-recommendations) tutorial and you still have the data store (suggested name `quickstart-media-data-store`), then you can use that data store instead of creating another. In this case, you should begin the tutorial at Create an app for media search.

Estimated time to complete this tutorial: ~1 hour. 

## Objectives

  * Learn how to import media documents to create a media data store.
  * Create, configure, and test a search app.



Before following this tutorial, make sure you have done the steps in [Before you begin](https://docs.cloud.google.com/generative-ai-app-builder/docs/before-you-begin).

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/gen-app-builder/?tutorial=generative-ai-app-builder--genappbuilder-media-search-intro)

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

Note: If you completed the [Get started with media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-media-recommendations) tutorial and you still have the data store (suggested name `quickstart-media-data-store`), skip to Create an app for media search. 

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

In this step, you restructure the Movielens dataset so it follows the expected format for media data stores.

For this guide, you create fake `view-item` user events during the past 90 days from positive ratings (`>= 4`).

  1. Create a view that converts the movies table into the [`Document` schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-documents#json-schema):
         
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
         

Now the new view has the schema that the Discovery Engine API expects.

  2. Go to the **BigQuery** page in Google Cloud console.

[Go to BigQuery](https://console.cloud.google.com/bigquery)

  3. In the **Explorer** pane, expand your project name, click **Datasets** , select the **`movielens`** dataset, and click **`movies_view`** to open the schema page for this view.

Alternatively, in the **Explorer** pane, select the **Classic explorer** tab, expand your project name, expand the **`movielens`** dataset and click **`movies_view`** to open the schema page for this view.

  4. Go to the **Table explorer** tab.

  5. In the **Generated query** pane, click the **Copy to query** button. The query editor opens.

  6. Click **Run** to see movie data in the view that you created.

  7. Create fictitious [user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-user-events) from movie ratings by running the following Cloud Shell command:
         
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




## Create an app for media search

The procedures in this section guide you through creating and deploying a media search app.

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/start)

  2. Click **Create app**.

  3. On the **Create App** page, under **Media catalog search** , click **Create**.

  4. In the **Your app name** field, enter a name for your app such as `quickstart-media-search`. Your app ID appears under the engine name.

  5. Click **Continue**.

  6. If you completed the [Get started with media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-media-recommendations) tutorial and you still have the data store (suggested name `quickstart-media-data-store`), then select it, click **Create** , and skip to Preview search.

  7. If you don't have a data store that contains the movielens dataset, create a new data store and select it:

     1. On the **Data Stores** page, click **Create data store**.

     2. Enter a display name for your data store, such as `quickstart-media-data-store`, and then click **Create**.

     3. Select the data store you just created, and then click **Create** to create your app. You will be redirected to the **Select a data source** page.




## Import data

Next, import the movies and user events data that were formatted earlier.

### Import documents

  1. If you are not automatically redirected to the **Select a data source** page:

     * Open the **Documents** tab.
     * Click **Import Data**.
  2. On the **Select a data source** page, select **BigQuery**.

  3. Enter the name of the `movies` BigQuery view you created and click **Import**.
         
         PROJECT_ID.movielens.movies_view
         

  4. Wait until all documents have been imported, which should take about 15 minutes. There should be 86537 documents when complete.

You can check the **Activity** tab for the import operation status. When the import is complete, the import operation status changes to **Completed**.




### Import user events

  1. Open the **Events** tab.

  2. Click **Import Events**.

  3. Select **BigQuery**.

  4. Enter the name of the `user_events` BigQuery view you created and click **Import**.
         
         PROJECT_ID.movielens.user_events
         

  5. You can proceed to the next step before the events are imported, but the search results won't yet contain the full dataset.

You can check the **Activity** tab for the operation status. The process takes about an hour to complete because you are importing millions of rows.




## Preview and configure search

  1. In the navigation menu, click **Configurations**.

  2. In the **Search here** box, type the name of a movie, such as "The Lord of the Rings".

  3. Notice that the search results are relevant to the movie title entered.

  4. On this page, you can customize how the search widget displays the search result information. See [Configure results for the search widget](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-attributes#configure_search_structured) to learn more.

For media search apps, you can:

     * [Configure fields for search](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-search-attributes)
     * [Configure autocomplete](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-autocomplete)
     * [Configure search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/configure-widget-attributes)

After making changes click **Save and publish** to update the widget.




## Deploy the search widget

  1. In the navigation menu, click **Integration**.

  2. Make sure the **Widget** tab is selected.

  3. Select **JWT or OAuth based** as the widget authorization type.

  4. In the **Domain** field, enter the domain name for web page where you will put the widget. For example, if you are going to copy the widget to the web page `example.com/ai.html`, enter `example.com` as the domain.

  5. Click **Add** , and then click **Save**.

  6. Copy the code snippet provided in the **Copy the following code to your web application** section.

  7. In your codebase, generate an authorization token.

  8. To pass the authorization token to your widget, use the "Set authorization token" code snippet provided in the **Copy the following code to your web application** section and replace the text `<JWT or OAuth token provided by you backend>` with your authorization token.

  9. For help integrating the search app into your web app, see the code samples at [Get search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results).




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

You can reuse the data store you created for media recommendations in the [Get started with media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-media-recommendations) tutorial. Try that tutorial before doing this clean up procedure.

  1. To avoid unnecessary Google Cloud charges, use the [Google Cloud console](https://console.cloud.google.com/) to delete your project if you don't need it.
  2. If you created a new project to learn about Agent Search and you no longer need the project, [delete the project](https://console.cloud.google.com/cloud-resource-manager).
  3. If you used an existing Google Cloud project, delete the resources you created to avoid incurring charges to your account. For more information, see [Delete an app](https://docs.cloud.google.com/generative-ai-app-builder/docs/delete-engine), [Purge data from a data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/delete-datastores), and [Delete a data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/delete-a-data-store).
  4. Follow the steps in [Turn off Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/turn-off-enterprise-search).
  5. If you created a BigQuery dataset, delete it in Cloud Shell:
         
         bq rm --recursive --dataset movielens
         




## What's next

  * [Get started with media recommendations](https://docs.cloud.google.com/generative-ai-app-builder/docs/try-media-recommendations)
  * [Add the search widget to a web page](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-widget)
  * [Introduction to Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction)
  * [About apps and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
