---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-hc/
title: Create a healthcare search app \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:14.662262+00:00
---

# Create a healthcare search app  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/create-app-hc/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Create a healthcare search app Stay organized with collections  Save and categorize content based on your preferences. 

**Deprecated:** Agent Search for healthcare is deprecated and won't be available after May 15, 2027. 

**Caution:**

  * Restrictions for healthcare: As a customer, you will not, and will not allow End Users to, use the Generative AI Services for clinical purposes (for clarity, non-clinical research, scheduling, or other administrative tasks is not restricted), as a substitute for professional medical advice, or in any manner that is overseen by or requires clearance or approval from any applicable regulatory authority. For more information, see [Service Specific Terms](https://cloud.google.com/terms/service-terms). 

For clarity, with respect to the use of Agent Search to retrieve and summarize existing medical information, the restriction on the use for clinical purposes means the restriction on the use for direct diagnosis or treatment purposes without review by a licensed professional in compliance with applicable laws and regulations. 

  * The generated output may not always be completely reliable. Due to the nature of LLMs and Generative AI, outputs may have incorrect or biased (for example, stereotypes or other harmful content) information and should be reviewed. All summaries or answers should be considered draft and not final.
  * This product's intended usage is not to provide information pertaining to the prevention, diagnosis or treatment of illness or disease. Questions regarding diagnosis or treatment recommendations are not intended to be addressed by the product. This product's intended use is to retrieve and summarize existing medical information provided by users.
  * Due to limited test data, this product may or may not be applicable to age group 0-18 and to age group 85 and above. Therefore, when reviewing the generated output, customers must consider the representativeness of subpopulations within their source data.



To search clinical data in Agent Search, you can follow one of these workflows:

  * Create a healthcare data store, import FHIR R4 data into the data store, connect it to a healthcare search app, and query the clinical data. For more information, see [Create a healthcare data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-hc).
  * Create a healthcare search app, create a healthcare data store and import FHIR R4 data into the data store during the app creation process, and query the clinical data.



This page describes the second method.

## About data import frequency

You can import FHIR R4 data into a data store in the following ways:

  * [Batch import](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-hc#batch): a one-time import. Data is imported into a data store in batches. For further incremental imports, see [Refresh healthcare data](https://docs.cloud.google.com/generative-ai-app-builder/docs/refresh-hc-data).

  * [Streaming import](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-hc#stream): a near real-time streaming data import. Any incremental changes in the source FHIR store are synchronized in the Agent Search data store. Streaming requires a _data connector_ , which is a type of a data store. To create a data connector, you must set up a collection. A data connector contains an _entity_ , which is also a data store instance.

You can also pause and resume streaming and perform manual synchronization whenever necessary. For more information, see [Manage a healthcare search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/manage-data-store-hc).

The data streaming rate for a given Google Cloud project is dependent on the following quotas. If you exceed the quota you might experience streaming delays.

    * The number of pending FHIR or BigQuery streaming writes per minute. For more information, see [Quotas and limits](https://docs.cloud.google.com/generative-ai-app-builder/quotas).
    * The number of FHIR read operations per minute per region. For more information, see [Cloud Healthcare API FHIR quotas](https://docs.cloud.google.com/healthcare-api/quotas#fhir_read_ops).



You can select the data import frequency at the time of data store creation and you can't change this configuration later.

## Before you begin

Before you create the healthcare search app, understand the following:

  * The relationship between apps and data stores for healthcare search. For more information, see [About apps and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest).

  * The [preparation of your FHIR data for ingestion](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#hc-fhir-data).

  * Agent Search for healthcare provides search services only in the US multi-region (`us`). Therefore, your healthcare search app and data stores must reside in the `us` multi-region.

  * If you're importing healthcare data from a Cloud Healthcare API FHIR store in one Google Cloud project to an Agent Search data store in a different Google Cloud project and you're using VPC Service Controls, the two projects must be in the same [perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/overview#isolate).




## Create an app

You can create a healthcare search app either in the Google Cloud console or using the API. To create a healthcare search app, follow these steps:

#### Permissions required for this task

Grant the following Identity and Access Management (IAM) roles to the `service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com` service account in the project that contains the Agent Search data store:

Purpose | Roles  
---|---  
To perform a one-time batch import of FHIR data from FHIR stores in Cloud Healthcare API. | 

  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [BigQuery data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor)
  * [Healthcare FHIR Store Administrator (`roles/healthcare.fhirStoreAdmin`)](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.fhirStoreAdmin)

  
To perform a streaming import of FHIR data from FHIR stores in Cloud Healthcare API in the same Google Cloud project. | 

  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [BigQuery data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor)
  * [Healthcare FHIR Store Administrator (`roles/healthcare.fhirStoreAdmin`)](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.fhirStoreAdmin)
  * [Healthcare FHIR Resource Reader (`roles/healthcare.fhirResourceReader`)](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.fhirResourceReader)

  
To perform a streaming import of FHIR data from FHIR stores in Cloud Healthcare API in a different Google Cloud project. | 

  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [BigQuery data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor)
  * [Healthcare FHIR Store Administrator (`roles/healthcare.fhirStoreAdmin`)](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.fhirStoreAdmin)
  * [Healthcare FHIR Resource Reader (`roles/healthcare.fhirResourceReader`)](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.fhirResourceReader)

  
To import FHIR data that references files in Cloud Storage. These are granted by default if the referenced files are in the same Google Cloud project as the Agent Search app. |  [Storage Object Admin (`roles/storage.objectAdmin`)](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)  
To customize the schema when creating a data store to configure the indexability, searchability, and retrievability of FHIR resources and elements. |  [Storage Object Admin (`roles/storage.objectAdmin`)](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)  
  
Grant the following Identity and Access Management roles to the `service-PROJECT_NUMBER@gcp-sa-discoveryengine.iam.gserviceaccount.com` service account in the project that contains the Cloud Healthcare API FHIR R4 data store:

Purpose | Roles  
---|---  
To perform a streaming import of FHIR data from FHIR stores in Cloud Healthcare API in a different Google Cloud project. | 

  * [Healthcare FHIR Store Administrator (`roles/healthcare.fhirStoreAdmin`)](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.fhirStoreAdmin)
  * [Healthcare FHIR Resource Reader (`roles/healthcare.fhirResourceReader`)](https://docs.cloud.google.com/healthcare-api/docs/access-control#healthcare.fhirResourceReader)

  
  
Grant the following Identity and Access Management roles to the `service-SOURCE_PROJECT_NUMBER@gcp-sa-healthcare.iam.gserviceaccount.com` service account in the project that contains the Cloud Healthcare API FHIR R4 data store:

Purpose | Roles  
---|---  
To perform a streaming import of FHIR data from FHIR stores in Cloud Healthcare API in the same Google Cloud project. | 

  * [BigQuery Job User (`roles/bigquery.jobUser`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.jobUser)
  * [BigQuery data Editor (`roles/bigquery.dataEditor`)](https://docs.cloud.google.com/bigquery/docs/access-control#bigquery.dataEditor)

  
To customize the schema when creating a data store to configure the indexability, searchability, and retrievability of FHIR resources and elements. |  [Storage Object Admin (`roles/storage.objectAdmin`)](https://docs.cloud.google.com/storage/docs/access-control/iam-roles)  
  
### Console

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. On the **Apps** page, click _add_box_ **New app**.

  3. On the **Create App** page, under **Healthcare search** , click **Create**.

  4. In the **Search app configuration** pane, select **Healthcare**.

  5. To turn on generative responses that use [advanced LLM features](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#generative-response-features) for this app, click the **Generative responses** toggle to on position.

When you activate generative responses, it can take up to five minutes for the supported features to become available.

  6. In the **Your app name** field, enter a name for your app.

  7. In the **External name of your company or organization** field, enter the common name for your company or organization. You don't need to include suffixes such as Inc or LLC. This field is useful for the LLM to identify the company that the app represents.

  8. In the **Access Transparency** section, select **Disable search metrics for this app** to turn off logging metrics for the current app. This can't be changed after the app is created.

  9. Click **Continue**.

  10. To connect to a data store, on the **Data Stores** page, do one of the following:

     * Select an existing healthcare data store for batch import or an existing data connector for streaming import. To create a data store or a data connector before creating an app, see [Create a healthcare data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-hc#create-data-store-healthcare-console).
     * Create a data store (for one-time batch import) or a data connector, which is an instance of a data store (for streaming import): 
       1. Click _add_box_ **Create data store**.
       2. In the **Select a data source** pane, select **Healthcare API (FHIR)** as your data source.
       3. To import data from your FHIR store, do one of the following: 
          * Select the FHIR store from the list of available FHIR stores: 
            1. Expand the **FHIR store** field.
            2. In this list, select a dataset that resides in a [permitted location](https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data#hc-fhir-data) and then select a FHIR store that uses FHIR version R4.
          * Enter the FHIR store manually: 
            1. Expand the **FHIR store** field.
            2. Click **Enter FHIR store manually**.
            3. In the **FHIR store name** dialog, enter the full name of the FHIR store in the following format: 

` project/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID `

            4. Click **Save**.
       4. In the **Synchronization** section, select one of the following options. This selection cannot be changed after the data store is created. 
          * **One time** : to perform a one-time batch data import. For further incremental imports, see [Refresh healthcare data](https://docs.cloud.google.com/generative-ai-app-builder/docs/refresh-hc-data). 
          * **Streaming** : to perform a near real-time streaming data import. To stream data, you must create a data connector, which is a type of a data store. To set up a streaming data store using the REST API, contact your customer engineer. 
       5. In the **What is the schema for this data?** section, select one of these options: 
          * **Google predefined schema** : to retain the Google-defined schema configurations, such as indexability, searchability, and retrievability, for the supported FHIR resources and elements. After you select this option, you cannot update the schema after you create the data store. If you want to be able to change the schema after the data store creation, select the **Custom schema** option. 
            1. Click **Continue**.
            2. In the **Your data store name** field, enter a name for your data store.
            3. Click **Create**.

The data store you created is listed on the **Data Stores** page.

          * **Custom schema** : to define your own schema configurations, such as indexability, searchability, and retrievability, for the supported FHIR resources and elements. To set up a configurable schema, contact your customer engineer. 
            1. Click **Continue**.
            2. Review the schema, expand each field, and edit the field settings.
            3. Click **Add new fields** to add new fields on the supported FHIR resources. You cannot remove the fields provided in the Google-defined schema.
            4. Click **Continue**.
            5. In the **Your data connector name** field, enter a name for your data connector.
            6. Click **Create**.

The data connector you created is listed on the **Data Stores** page. The source FHIR store is added as an entity within the data connector.

       6. Click **Continue**.
       7. Select the created data store or data connector.
  11. Optional: To see a list of unavailable data stores, click **Learn why**.

A table is displayed with a list of data stores and the reason why they are unavailable. Here are some of the reasons why a data store might be unavailable:

     * Your data store type allows connection to only one app and the data store is already connected.
     * Your data store and your app are of different types. For example, you you can't connect a website search data store to a healthcare search app.
  12. Click **Create**.

If the app and its data store are created successfully, the data store details page displays the details of the imported FHIR data.




### REST

  1. [Create a healthcare data store and import healthcare data into it](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-hc#create-data-store-healthcare-rest).
  2. Create a healthcare search app and connect it to a data store. A healthcare search app can only connect to one data store, whereas a given data store can be connected to several apps.

**Key Term:** In Agent Search, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs.
         
         curl -X POST\
          -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json"\
          -H "X-Goog-User-Project: PROJECT_ID" \
         "https://us-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/us/collections/default_collection/engines?engineId=APP_ID" \
          -d '{
             "displayName": "APP_DISPLAY_NAME",
             "dataStoreIds":"DATA_STORE_ID",
             "industryVertical": "HEALTHCARE_FHIR",
             "solutionType": "SOLUTION_TYPE_SEARCH",
             "searchEngineConfig": {
               "searchTier": "SEARCH_TIER_STANDARD",
               "searchAddOns": ["SEARCH_ADD_ON"]
             }
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app that you want to create.
     * `APP_DISPLAY_NAME`: the display name of the Agent Search app that you want to create.
     * `DATA_STORE_ID`: the ID of an existing Agent Search data store that you want to add to the Agent Search app.
     * `SEARCH_ADD_ON`: an optional field to specify whether you want the advanced LLM features, such as [searching with generative AI answers](https://docs.cloud.google.com/generative-ai-app-builder/docs/search-hc-data#nl-search-genAI), for this app. To activate advanced LLM features, enter the value `SEARCH_ADD_ON_LLM`. If you don't want Advanced LLM features, then either specify `SEARCH_ADD_ON_UNSPECIFIED` or remove the `searchAddOns` field. For more information, see [Advanced LLM features](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#advanced-llm-features).

#### Response

You should receive a JSON response similar to the following. If the value for the `done` field is `true`, it indicates that the operation to create the app was completed. If it is `false`, the app creation operation was unsuccessful. 
    
    {
      "name": "projects/PROJECT_ID/locations/us/collections/default_collection/operations/APP_CREATION_OPERATION_ID",
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.discoveryengine.v1.Engine",
        "name": "projects/PROJECT_ID/locations/us/collections/default_collection/engines/APP_ID",
        "displayName": "APP_DISPLAY_NAME",
        "dataStoreIds": [
          "DATA_STORE_ID"
        ],
        "solutionType": "SOLUTION_TYPE_SEARCH",
        "searchEngineConfig": {
          "searchTier": "SEARCH_TIER_STANDARD",
          "searchAddOns": [
            "SEARCH_ADD_ON_LLM"
          ]
        },
        "industryVertical": "HEALTHCARE_FHIR"
      }
    }
    




## Verify app creation

This task shows you how to verify whether a healthcare search app was created successfully and whether FHIR data was imported into the data store successfully.

  * In the Google Cloud console: Select the app and verify its details.
  * Through the REST API, use the [`engines.get`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/get) method to get the healthcare data store details.



To verify data store creation and data import, complete the following steps.

### Console

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/)

  2. On the **Apps** page, verify whether the app that you created is in the apps list.

  3. Verify that the data store that you connected to the app is listed in the **Connected data stores** table.

  4. Select the data store and [verify the data store details](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-hc#verify-data-store-console).




### REST

  1. Verify the app creation.
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
          -H "Content-Type: application/json"\
          -H "X-Goog-User-Project: PROJECT_ID" \
          "https://us-discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/us/collections/default_collection/engines/APP_ID"
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app.

#### Response

You should receive a JSON response similar to the following. The response contains details of the created app.
    
    {
      "name": "projects/PROJECT_ID/locations/us/collections/default_collection/engines/APP_ID",
      "displayName": "APP_DISPLAY_NAME",
      "createTime": "APP_CREATION_TIMESTAMP",
      "dataStoreIds": [
        "DATA_STORE_ID"
      ],
      "solutionType": "SOLUTION_TYPE_SEARCH",
      "searchEngineConfig": {
        "searchTier": "SEARCH_TIER_STANDARD",
        "searchAddOns": [
          "SEARCH_ADD_ON_LLM"
        ]
      },
      "industryVertical": "HEALTHCARE_FHIR",
      "dataStores": [
        "projects/PROJECT_ID/locations/us/collections/default_collection/dataStores/APP_ID"
      ]
    }
    

  2. [Verify data store creation and FHIR data import](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-hc#verify-data-store-rest). 




## What's next

  * [Search for healthcare data](https://docs.cloud.google.com/generative-ai-app-builder/docs/search-hc-data) in your healthcare search app.
  * [Refresh healthcare data](https://docs.cloud.google.com/generative-ai-app-builder/docs/refresh-hc-data).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
