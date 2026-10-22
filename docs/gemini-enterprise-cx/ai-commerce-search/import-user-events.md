---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events/
title: Import historical user events \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:36:18.160355+00:00
---

# Import historical user events  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Import historical user events Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to import user event data from past events in bulk into AI Commerce Search. User event data is required for training models. After you've set up [real-time event recording](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events), it can take a considerable amount of time to record sufficient user event data to train your models. Importing historical data can accelerate the process.

The import procedures on this page apply to both recommendations and search. After you import data, both services are able to use those events, so you don't need to import the same data twice if you use both services.

You can import events from:

  * Cloud Storage.
  * BigQuery.
  * BigQuery for Google Analytics 360 events.
  * BigQuery for Google Analytics 4 events.
  * Events inline using the [`userEvents.import`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/import) method.



## Before you begin

To avoid import errors and verify that there is sufficient data to generate good results, review the following information before importing your user events.

  * Review the [best practices for recording user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events#bps).

  * User event formatting differs depending on the user event type. See [User event types and examples schema](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#formats) for the format to specify when creating tables for each event type.

  * Recommendations and search have differing minimum data requirements. Make sure your user events meet the requirements of the service you plan to use:

    * See [User event requirements and best practices](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#user-event-reqs) for search and recommendations requirements.

    * If you use recommendations models, also see [User event data requirements](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/models#import-reqs), which lists additional requirements depending on the recommendation model type and optimization objective you plan to use.




## Event import considerations

This section describes the methods that can be used for batch importing of your historical user events, when you might use each method, and some of their limitations.

**Note:** A search user event has a user interaction when it is followed by a `detail-page-view`, `add-to-cart`, or `purchase` event with the same visitor ID and with one of the products included in the search event.Import source | Description | When to use | Limitations  
---|---|---|---  
**Cloud Storage** |  Import JSON data from files (≤ 2 GB, max 100) using Google Cloud console or `curl`. Supports custom attributes.  | High-volume data loads in a single step. |  GA data requires an extra export to BigQuery before moving to Cloud Storage.   
**BigQuery** |  Import from a BigQuery table using the AI Commerce Search schema using Google Cloud console or `curl`.  | Preprocessing or analyzing event data before import. |  Requires manual schema mapping; higher resource cost for high event volumes.   
**BigQuery + Google Analytics 360** |  Direct import of existing Google Analytics 360 data into AI Commerce Search.  |  Existing GA360 conversion tracking; no manual schema mapping needed.  |  Limited attribute subset available; search requires GA impression tracking.   
**BigQuery + Google Analytics 4** |  Direct import of existing Google Analytics 4 data into AI Commerce Search.  |  Existing GA4 conversion tracking; no manual schema mapping needed.  |  Limited attribute subset available; search requires `search_query` event parameter keys.   
**Inline import** |  Import using direct `userEvents.import` method calls.  | High-privacy backend authentication requirements. | More complex implementation than standard web-based imports.  
  
### Size limitations

There is a total system limit of 40 billion user events. The following size limitations for data imports according to ingest platform are:

  * For bulk import from Cloud Storage, each file must be 2 GB or smaller, and you can include up to 100 files in a single bulk import request.

  * For BigQuery imports, the size limitation is 128 GB.

  * For inline imports, a recommended maximum of 10,000 user events is suggested per request.

  * For the minimum days to record live or import historical user events for model training and search optimization, do model training and tuning. Initial model training and tuning can take two to five days or, for larger datasets, longer.




### Link search events to user interactions

**Important:** For AI Commerce Search to optimize for revenue, the minimum requirement is 250,000 search user events linked with at least one user interaction. This means the data must meet [Tier 3 or Tier 4 performance requirements](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/data-quality#text-query-search).

To enable revenue-optimized ranking (Tier 3) and personalization (Tier 4), uploading general `search` events is not enough. AI Commerce Search models require a strong signal of user intent and satisfaction to learn which products are performing well for specific queries. This signal is provided by attributable user interactions. You must upload subsequent events, specifically `detail-page-view`, `add-to-cart`, and `purchase-complete`.

#### Why user interactions matter

  * **Relevance signals** : A `search` event tells the model what the user wanted. A `detail-page-view` (click) tells the model which result was relevant.
  * **Revenue signals** : `add-to-cart` and `purchase-complete` events tell the model which results drive actual business value.



#### Data quality thresholds for optimization

To activate the revenue optimization models, your data must meet specific volume and quality thresholds.

The following metrics are required:

Metric | Requirement | Context  
---|---|---  
**Attributable click volume** |  **250,000** `detail-page-view` events in last 30 days  |  These must have a valid user interaction linking them to a search result.   
**Search event volume** |  **2,000,000** events in last 90 days  |  A large baseline of historical search traffic is required to establish statistical significance.   
**Click density** |  **10** average `detail-page-view` events per product  |  Ensures the model has enough signal coverage across your catalog (in the last 30 days).   
**Conversion signal** |  **0.5** average `add-to-cart` events per product  |  Recommended to fully utilize revenue-maximizing objectives.   
**Price coverage** |  **95%** of searched products have price  |  The model cannot optimize for revenue if it doesn't know the price of the products being returned.   
  
For more information, refer to the [Data quality](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/data-quality) page.

**Important:** Monitor your progress toward these thresholds using the **Data quality** in the Google Cloud console. If your **Unjoined events** rate is high, ensure you are correctly passing the `attributionToken` from the `SearchResponse` to the subsequent user events.

## Bulk import using BigQuery or Cloud Storage

Using BigQuery or Cloud Storage as a staging area for user event data in AI Commerce Search offers distinct advantages:

  * **Enhanced resiliency** : Storing events in BigQuery or Cloud Storage provides a reliable backup mechanism, enabling purging and reingestion if necessary. This resiliency safeguards against data loss and simplifies recovery in case of errors or inconsistencies. There is also built-in resiliency in the import method where events that were not ingested are stored in [error buckets](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/ImportErrorsConfig) along with the error details.

  * **In-place custom analytics** : With events readily accessible in BigQuery, custom analytics can be performed directly on the user event data without the need for additional data export or transfer processes. This enables analysis workflows and real-time insights.

  * **Using existing events** : Bulk imports can use existing user event data collected in various formats. A straightforward extract, transform, load (ETL) process can convert this data into the AI Commerce Search format, eliminating the need for extensive frontend changes or complex integrations.




Potential downsides of bulk import are:

  * **Limited real-time personalization** : Real-time personalization capabilities are constrained by the frequency of bulk imports. The time lag between event generation and ingestion can impact the responsiveness of personalized search results.

  * **Slower KPI measurement and error reporting** : Compared to real-time streaming, bulk imports introduce delays in KPI measurement and error reporting due to the batch-oriented nature of the process. This can hinder immediate responses to emerging trends or issues.

  * **ETL pipeline infrastructure** : Compared to real-time streaming, ETL pipelines need to be built and monitored for failures. Mechanism to retry imports for failed events (after fixing) also needs to be implemented. Implementing this might need some initial development efforts.




Understanding these trade-offs can guide you in selecting the most suitable user event ingestion approach for your specific use cases and priorities within AI Commerce Search.

### Import user events from Cloud Storage

Import user events from Cloud Storage using the Google Cloud console or the [`userEvents.import`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/import) method.

###  Console 

  1. Go to the **Data** > page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Data page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/data/)
  2. Click **Import** to open the **Import Data** panel.
  3. Choose **User events**.
  4. Select **Google Cloud Storage** as the data source.
  5. Choose **Retail User Events Schema** as the schema.
  6. Enter the Cloud Storage location of your data.
  7. Click **Import**.



###  curl 

Use the [`userEvents.import`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/import) method to import your user events.

  1. Create a data file for the input parameters for the import. Use the [`GcsSource`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/GcsSource) object to point to your Cloud Storage bucket.

You can provide multiple files, or just one.

     * INPUT_FILE: A file or files in Cloud Storage containing your user event data. See [About user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events) for examples of each user event type format. Make sure each user event is on its own single line, with no line breaks.
     * ERROR_DIRECTORY: A Cloud Storage directory for error information about the import.

The input file fields must be in the format `gs://<bucket>/<path-to-file>/`. The error directory must be in the format `gs://<bucket>/<folder>/`. If the error directory does not exist, AI Commerce Search creates it. The bucket must already exist.
    
    {
    "inputConfig":{
     "gcsSource": {
       "inputUris": ["INPUT_FILE_1", "INPUT_FILE_2"],
      },
      "errorsConfig":{"gcsPrefix":"ERROR_DIRECTORY"}
    }

  2. Import your catalog information by making a `POST` request to the [`userEvents:import`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/import) REST method, providing the name of the data file.
         
         export GOOGLE_APPLICATION_CREDENTIALS=/tmp/my-key.json
         
         curl -X POST \
              -v \
              -H "Content-Type: application/json; charset=utf-8" \
              -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
              --data @./DATA_FILE.json \
           "https://retail.googleapis.com/v2/projects/PROJECT_ID/locations/global/catalogs/default_catalog/userEvents:import"
           }
         }'




### Import user events from BigQuery

Import user events from BigQuery using the Google Cloud console or the [`userEvents.import`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/import) method.

#### Set up BigQuery access

Follow the instructions in [Setting up access to your BigQuery dataset](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog#access) to give your AI Commerce Search API service account the minimum **BigQuery User** role required for the import to succeed and the additional **BigQuery Data Editor** role for your BigQuery dataset. The **BigQuery Data Owner** role is unnecessary.

#### Import your user events from BigQuery

You can import user events using the AI Commerce Search in Gemini Enterprise for Customer Experience console or the `userEvents.import` method.

###  Console 

  1. Go to the **Data** > page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Data page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/data/)
  2. Click **Import** to open the **Import Data** panel.
  3. Choose **User events**.
  4. Select **BigQuery** as the data source.
  5. Select the data schema. 

     * **Google Analytics 4** : Use for Google Analytics 4 events. 
     * **Google Analytics 360** : Use for Google Analytics 360 events, unless you are [importing events only home-page-views from Google Analytics 360](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events#bq-ga-home-page-views-import) (in that case, use **Retail User Events Schema**). 
     * **Retail User Events Schema** : Use for importing events from sources other than Google Analytics and for [importing events only home-page-views from Google Analytics 360](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events#bq-ga-home-page-views-import). 
  6. Enter the BigQuery table where your data is located.
  7. Optional: Enter the location of a Cloud Storage bucket in your project as a temporary location for your data.  
If not specified, a default location is used. If specified, the BigQuery and Cloud Storage bucket have to be in the same region.
  8. Optional: Under **Show advanced options** , enter the location of a Cloud Storage bucket in your project as a temporary location for your data.  
  
If not specified, a default location is used. If specified, the BigQuery and Cloud Storage bucket have to be in the same region.
  9. Click **Import**.



###  curl 

Import your user events by including the data for the events in your call to the `userEvents.import` method. See the [`userEvents.import`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/import) API reference.

The value you specify for `dataSchema` depends on what you're importing:

  * `user_event_ga4`: Use for Google Analytics 4 events.
  * `user_event_ga360`: Use for Google Analytics 360 events, unless you are importing only home-page-views from Google Analytics 360 (in that case, use `user_event`).
  * `user_event`: Use for importing events from sources other than Google Analytics and for importing events only home-page-views from Google Analytics 360.


    
    
    export GOOGLE_APPLICATION_CREDENTIALS=/tmp/my-key.json
    
    curl \
    -v \
    -X POST \
    -H "Content-Type: application/json; charset=utf-8" \
    -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
    "https://retail.googleapis.com/v2/projects/PROJECT_ID/locations/global/catalogs/default_catalog/userEvents:import" \
    --data '{
      "inputConfig": {
        "bigQuerySource": {
          "datasetId": "DATASET_ID",
          "tableId": "TABLE_ID",
          "dataSchema": "SCHEMA_TYPE"
      }
    }
    }'

### Import Analytics 360 user events with BigQuery

**Note:** If you use Google Analytics 4, see Importing Google Analytics 4 user events with BigQuery.

The following procedures assume you are familiar with using [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) and Analytics 360.

#### Before you begin

Before you begin the next steps, make sure:

  * You're using [Enhanced Ecommerce](https://developers.google.com/analytics/devguides/collection/analyticsjs/enhanced-ecommerce).
  * You have [BigQuery linked to Analytics 360](https://support.google.com/analytics/answer/3416092).



#### Check your data source

  1. Make sure that the user event data that you will import is correctly formatted in a BigQuery table you have access to.

Make sure that the table is named `project_id:ga360_export_dataset.ga_sessions_YYYYMMDD`.

See the [Google Analytics documentation](https://support.google.com/analytics/answer/3437719) for more about the table format and naming.

  2. In the [BigQuery Google Cloud console](https://console.cloud.google.com/bigquery), select the table from the **Explorer** panel to preview the table.

Check that:

     1. The `clientId` column has a valid value—for example, `123456789.123456789`.

Note that this value is different from the full _ga cookie value (which has a format such as `GA1.3.123456789.123456789`).

     2. The `hits.transaction.currencyCode` column has a [valid currency code](https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters#cu).

**Note:** The AI Commerce Search API `purchase-complete` event type requires a currency code. If you're importing purchase events, which [some AI Commerce Search models](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-models#import-reqs) require, [update Enhanced Ecommerce reporting](https://developers.google.com/tag-manager/enhanced-ecommerce#add) to include currency code.
     3. If you plan to import `search` events, check that either a `hits.page.searchKeyword` or `hits.customVariable.searchQuery` column is present.

While AI Commerce Search requires both `searchQuery` and `productDetails` to [return a list of search results](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#search), Analytics 360 doesn't store both search queries and product impressions in one event. For AI Commerce Search to work, you need to create a tag at the data layer or a JavaScript Pixel to be able to import both types of user events from Google Analytics sources:

        * `searchQuery`, which is read from the `search_term` parameter, or from `view_search_results` events, is derived from either `hits.page.searchKeyword`, or from `hits.customVariables.customVarValue` if `hits.customVariables.customVarName` is `searchQuery`.
        * `productDetails`, the product impression which is read from the `items` parameter of the `view_item_list` event, is taken from `hits.product` if `hits.product.isImpressions` is `TRUE`.
  3. Check the consistency of item IDs between the uploaded catalog and the Analytics 360 user event table.

Using any product ID from the `hits.product.productSKU` column in the BigQuery table preview, use the [`product.get`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/get) method to make sure the same product is in your uploaded catalog.
         
         export GOOGLE_APPLICATION_CREDENTIALS=/tmp/my-key.json
         
            curl \
              -v \
              -X GET \
              -H "Content-Type: application/json; charset=utf-8" \
              -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
              "https://retail.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/branches/default_branch/products/PRODUCT_ID"




You can import Google Analytics 360 events using the AI Commerce Search in Gemini Enterprise for Customer Experience console or the `userEvents.import` method.

### Console

  1. Go to the **Data** > page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Data page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/data/)
  2. Click **Import** to open the **Import Data** panel.
  3. Choose **User events**.
  4. Select **BigQuery** as the data source.
  5. Select the data schema. 

     * **Google Analytics 4** : Use for Google Analytics 4 events. 
     * **Google Analytics 360** : Use for Google Analytics 360 events, unless you are [importing events only home-page-views from Google Analytics 360](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events#bq-ga-home-page-views-import) (in that case, use **Retail User Events Schema**). 
     * **Retail User Events Schema** : Use for importing events from sources other than Google Analytics and for [importing events only home-page-views from Google Analytics 360](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events#bq-ga-home-page-views-import). 
  6. Enter the BigQuery table where your data is located.
  7. Optional: Enter the location of a Cloud Storage bucket in your project as a temporary location for your data.  
If not specified, a default location is used. If specified, the BigQuery and Cloud Storage bucket have to be in the same region.
  8. Optional: Under **Show advanced options** , enter the location of a Cloud Storage bucket in your project as a temporary location for your data.  
  
If not specified, a default location is used. If specified, the BigQuery and Cloud Storage bucket have to be in the same region.
  9. Click **Import**.



### REST

Import your user events by including the data for the events in your call to the [`userEvents.import`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/import) method.

For `dataSchema`, use the value `user_event_ga360`.
    
    
    export GOOGLE_APPLICATION_CREDENTIALS=/tmp/my-key.json
    curl \\
      -v \\
      -X POST \\
      -H "Content-Type: application/json; charset=utf-8" \\
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \\
      "https://retail.googleapis.com/v2/projects/PROJECT_ID/locations/global/catalogs/default_catalog/userEvents:import" \\
      --data '{
        "inputConfig": {
          "bigQuerySource": {
            "datasetId": "some_ga360_export_dataset",
            "tableId": "ga_sessions_YYYYMMDD",
            "dataSchema": "user_event_ga360"
        }
      }
    }'

### Java
    
    
    public static String importUserEventsFromBigQuerySource()
        throws IOException, InterruptedException, ExecutionException {
      UserEventServiceClient userEventsClient = getUserEventServiceClient();
    
      BigQuerySource bigQuerySource = BigQuerySource.newBuilder()
          .setProjectId(PROJECT_ID)
          .setDatasetId(DATASET_ID)
          .setTableId(TABLE_ID)
          .setDataSchema("user_event")
          .build();
    
      UserEventInputConfig inputConfig = UserEventInputConfig.newBuilder()
          .setBigQuerySource(bigQuerySource)
          .build();
    
      ImportUserEventsRequest importRequest = ImportUserEventsRequest.newBuilder()
          .setParent(DEFAULT_CATALOG_NAME)
          .setInputConfig(inputConfig)
          .build();
    
      String operationName = userEventsClient
          .importUserEventsAsync(importRequest).getName();
    
      userEventsClient.shutdownNow();
      userEventsClient.awaitTermination(2, TimeUnit.SECONDS);
    
      return operationName;
    }

You can import Analytics 360 user events if you have integrated Analytics 360 with BigQuery and use Enhanced Ecommerce.

#### Import your Analytics 360 home-page-views with BigQuery

In Analytics 360, home-page-view events are not distinguished from other page-view events. This means that home-page-view events are not imported as events with the other event types (such as detail-page-view) in Import your Analytics 360 events.

The following procedure explains how you can extract home-page-view events from your Analytics 360 data and import them into AI Commerce Search. In short, this is done by extracting users' views of the home page (identified by the home-page path) into a new BigQuery table and then importing data from that new table into AI Commerce Search.

To import home-page-view events from Analytics 360 into AI Commerce Search:

  1. Create a BigQuery dataset or make sure that you have a BigQuery dataset available that you can add a table to.

This dataset can be in your AI Commerce Search project or in the project where you have your Analytics 360 data. It is the target dataset into which you'll copy the Analytics 360 home-page-view events.

  2. Create a BigQuery table in the dataset as follows:

     1. Replace the variables in the following SQL code as follows.

        * **target_project_id** : The project where the dataset from step 1 is located.

        * **target_dataset** : The dataset name from step 1.
    
    CREATE TABLE TARGET_PROJECT_ID.TARGET_DATASET.ga_homepage (
     eventType STRING NOT NULL,
     visitorId STRING NOT NULL,
     userId STRING,
     eventTime STRING NOT NULL
    );

     2. Copy the SQL code sample.

     3. Open the BigQuery page in the Google Cloud console.

[Go to the BigQuery page](https://console.cloud.google.com/bigquery)

     4. If it's not already selected, select the target project.

     5. In the **Editor** pane, paste the SQL code sample.

     6. Click play_circle **Run** and wait for the query to finish running.

Running this code creates a table in the format `target_project_id:target_dataset.ga_homepage_YYYYMMDD`—for example, `my-project:view_events.ga_homepage_20230115`.

  3. Copy the Analytics 360 home-page-view events from your Analytics 360 data table into the table created in the preceding step 2.

     1. Replace the variables in the following SQL example code as follows:

        * **source_project_id** : The ID of the project that contains the Analytics 360 data in a BigQuery table.

        * **source_dataset** : The dataset in the source project that contains the Analytics 360 data in a BigQuery table.

        * **source_table** : The table in the source project that contains the Analytics 360 data.

        * **target_project_id** : The same target project ID as in the preceding step 2.

        * **target_dataset** : The same target dataset as in the preceding step.

        * **path** : This is the path to the home page. Usually this is `/`—for example, if the home page is `example.com/`. However, if the home page is like `examplepetstore.com/index.html`, the path is `/index.html`.
    
    INSERT INTO `TARGET_PROJECT_ID.TARGET_DATASET.ga_homepage(eventType,visitorId,userID,eventTime)`
    
    SELECT
      "home-page-view" as eventType,
      clientId as visitorId,
      userId,
      CAST(FORMAT_TIMESTAMP("%Y-%m-%dT%H:%M:%SZ",TIMESTAMP_SECONDS(visitStartTime)) as STRING) AS eventTime
    
    FROM
      `SOURCE_PROJECT_ID.SOURCE_DATASET.SOURCE_TABLE`, UNNEST(hits) as hits
    
    WHERE hits.page.pagePath = "PATH" AND visitorId is NOT NULL;

     2. Copy the SQL code sample.

     3. Open the BigQuery page in the Google Cloud console.

[Go to the BigQuery page](https://console.cloud.google.com/bigquery)

     4. If it's not already selected, select the target project.

     5. In the **Editor** pane, paste the SQL code sample.

     6. Click play_circle **Run** and wait for the query to finish running.

  4. Follow the instructions in Import user events from BigQuery to import the home-page-view events from the target table. During schema selection, if you import using console, select **Retail User Events Schema** ; if you import using `userEvents.import`, specify `user_event` for the `dataSchema` value.

  5. Delete the table and dataset that you created in steps 1 and 2.




### Import Google Analytics 4 user events with BigQuery

You can import Google Analytics 4 user events if you have integrated Google Analytics 4 with BigQuery and use Google Analytics Ecommerce.

The following procedures assume you are familiar with using [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) and Google Analytics 4.

#### Before you begin

Before you begin the next steps, make sure:

  * You're using [Google Analytics Ecommerce](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm).
  * You have [BigQuery linked to Google Analytics 4](https://support.google.com/analytics/answer/9823238).



#### Check your data source

To make sure that your user event data is prepared for importing, follow these steps.

For a table of Google Analytics 4 fields that AI Commerce Search uses and which AI Commerce Search fields they map to, see [Google Analytics 4 user event fields](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#ga4-mapping).

For all Google Analytics event parameters, see the [Google Analytics Events reference documentation](https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference/events).

  1. Make sure that the user event data that you will import is correctly formatted in a BigQuery table you have access to.

     * The dataset should be named `analytics_PROPERTY_ID`.
     * The table should be named `events_YYYYMMDD`.

For information about the table names and format, see the [Google Analytics documentation](https://support.google.com/analytics/answer/7029846).

  2. In the [BigQuery Google Cloud console](https://console.cloud.google.com/bigquery), select the dataset from the **Explorer** panel and find the table of user events that you plan to import.

Check that:

     1. The `event_params.key` column has a `currency` key and that its associated string value is a [valid currency code](https://developers.google.com/analytics/devguides/collection/protocol/v1/parameters#cu).

**Note:** The AI Commerce Search API `purchase-complete` event type requires a currency code. If you're importing purchase events, which [some AI Commerce Search models](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/create-models#import-reqs) require, [update your event reporting](https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference/events#purchase) to include currency codes.
     2. If you plan to import `search` events, check that the `event.event_params.key` column has a `search_term` key and an associated value.

While AI Commerce Search requires both `searchQuery` and `productDetails` to [return a list of search results](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events#search), Google Analytics 4 doesn't store both search queries and product impressions in one event. For AI Commerce Search to work, you need to create a tag at the data layer or from a JavaScript Pixel to be able to import both types of user events from Google Analytics sources:

        * `searchQuery`, which is read from the `search_term` parameter, or from `view_search_results` events.
        * `productDetails`, the product impression which is read from the `items` parameter of the `view_item_list` event.

For information about `search` in Google Analytics 4, see [`search`](https://developers.google.com/analytics/devguides/collection/protocol/ga4/reference/events#search) in the Google Analytics documentation.

  3. Check the consistency of item IDs between the uploaded catalog and the Google Analytics 4 user event table.

To make sure that a product in the Google Analytics 4 user table is also in your uploaded catalog, copy a product ID from the `event.items.item_id` column in the BigQuery table preview and use the [`product.get`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.branches.products/get) method to check if that product ID is in your uploaded catalog.
         
         export GOOGLE_APPLICATION_CREDENTIALS=/tmp/my-key.json
         
            curl \
              -v \
              -X GET \
              -H "Content-Type: application/json; charset=utf-8" \
              -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
              "https://retail.googleapis.com/v2/projects/PROJECT_NUMBER/locations/global/catalogs/default_catalog/branches/default_branch/products/PRODUCT_ID"




### Import your Google Analytics 4 events

You can import Google Analytics 4 events using the AI Commerce Search in Gemini Enterprise for Customer Experience console or the `userEvents.import` method.

#### Use the console

  1. Go to the **Data** > page in the AI Commerce Search in Gemini Enterprise for Customer Experience console.  
  
[Go to the Data page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/data/)
  2. Click **Import** to open the **Import Data** panel.
  3. Choose **User events**.
  4. Select **BigQuery** as the data source.
  5. Select the data schema. 

     * **Google Analytics 4** : Use for Google Analytics 4 events. 
     * **Google Analytics 360** : Use for Google Analytics 360 events, unless you are [importing events only home-page-views from Google Analytics 360](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events#bq-ga-home-page-views-import) (in that case, use **Retail User Events Schema**). 
     * **Retail User Events Schema** : Use for importing events from sources other than Google Analytics and for [importing events only home-page-views from Google Analytics 360](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/import-user-events#bq-ga-home-page-views-import). 
  6. Enter the BigQuery table where your data is located.
  7. Optional: Enter the location of a Cloud Storage bucket in your project as a temporary location for your data.  
If not specified, a default location is used. If specified, the BigQuery and Cloud Storage bucket have to be in the same region.
  8. Optional: Under **Show advanced options** , enter the location of a Cloud Storage bucket in your project as a temporary location for your data.  
  
If not specified, a default location is used. If specified, the BigQuery and Cloud Storage bucket have to be in the same region.
  9. Click **Import**.



#### Use the API

Import your user events by including the data for the events in your call to the `userEvents.import` method. See the [`userEvents.import`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/import) API reference.

For `dataSchema`, use the value `user_event_ga4`.
    
    
    export GOOGLE_APPLICATION_CREDENTIALS=/tmp/my-key.json
    curl \\
      -v \\
      -X POST \\
      -H "Content-Type: application/json; charset=utf-8" \\
      -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \\
      "https://retail.googleapis.com/v2/projects/PROJECT_ID/locations/global/catalogs/default_catalog/userEvents:import" \\
      --data '{
        "inputConfig": {
          "bigQuerySource": {
            "projectId": "PROJECT_ID",
            "datasetId": "DATASET_ID",
            "tableId": "TABLE_ID",
            "dataSchema": "user_event_ga4"
        }
      }
    }'

## Import user events inline

You can import user events inline by including the data for the events in your call to the [`userEvents.import`](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2/projects.locations.catalogs.userEvents/import) method.

The easiest way to do this is to put your user event data into a JSON file and provide the file to curl.

For the formats of the user event types, see [About user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/user-events).

### curl

  1. Create the JSON file:
         
         {
           "inputConfig": {
             "userEventInlineSource": {
               "userEvents": [
                 \{
                   "<userEvent1>"
                 \},
                 \{
                   "<userEvent2>"
                 \},
                 \....
               \]
             \}
           }
         }
         

  2. Call the POST method:
         
         curl -X POST \
              -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
              -H "Content-Type: application/json; charset=utf-8" \
              --data @./data.json \
           "https://retail.googleapis.com/v2/projects/PROJECT_ID/locations/global/catalogs/default_catalog/userEvents:import"
         




### Java
    
    
    public static String importUserEventsFromInlineSource(
        List<UserEvent> userEventsToImport)
        throws IOException, InterruptedException, ExecutionException {
      UserEventServiceClient userEventsClient = getUserEventServiceClient();
    
      UserEventInlineSource inlineSource = UserEventInlineSource.newBuilder()
          .addAllUserEvents(userEventsToImport)
          .build();
    
      UserEventInputConfig inputConfig = UserEventInputConfig.newBuilder()
          .setUserEventInlineSource(inlineSource)
          .build();
    
      ImportUserEventsRequest importRequest = ImportUserEventsRequest.newBuilder()
          .setParent(DEFAULT_CATALOG_NAME)
          .setInputConfig(inputConfig)
          .build();
    
      String operationName = userEventsClient
          .importUserEventsAsync(importRequest).getName();
    
      userEventsClient.shutdownNow();
      userEventsClient.awaitTermination(2, TimeUnit.SECONDS);
    
      return operationName;
    }

## Historical catalog data

You can also import catalog data that appears in your historical user events. This catalog data can be helpful because past product information can be used to enrich user event capturing, which can in turn improve model accuracy.

For more details, see [Import historical catalog data](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/upload-catalog#historical-catalog).

## View imported events

View event integration metrics in the **Events** tab on the AI Commerce Search in Gemini Enterprise for Customer Experience console **Data** page. This page shows all events written or imported in last year. Metrics can take up to 24 hours to appear after successful data ingestion. 

[Go to the Data page](https://console.cloud.google.com/ai/retail/catalogs/default_catalog/data/)

## A/B testing evaluation

The following parameters for A/B apply, depending on your testing objective:

  * For a click-through rate (CTR) objective, at least 21 days of user events are required, or specific event volumes. For example, more than 2 million search events and more than 500,000 search clicks.

  * For a conversion rate (CVR) or revenue objective, at least 28 days of user events are required, or specific event volumes. For example, over 4 million search events, over 1 million search clicks, over 0.5 purchase events per searchable product.




Refer to the [A/B testing](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/a-b-testing) page For more information about A/B testing and best practices.

## What's next

  * Start [recording user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/record-events).
  * [Manage your user events](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/manage-user-events).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
