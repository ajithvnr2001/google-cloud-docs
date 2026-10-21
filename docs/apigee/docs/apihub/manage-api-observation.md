---
url: https://docs.cloud.google.com/apigee/docs/apihub/manage-api-observation/
title: Manage API observations in API hub \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:51:01.828588+00:00
---

# Manage API observations in API hub  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/apihub/manage-api-observation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Manage API observations in API hub Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to view, analyze, and stop collecting API observations and API operations data in API hub 

## Before you begin

To manage API observations in API hub, make sure that you have the required IAM roles and permissions. For more information, see [IAM roles and permissions](https://docs.cloud.google.com/apigee/docs/apihub/api-observation-overview#iam-roles-permissions). 

## View discovered API observations in API hub

You can view or list all the [discovered API observations](https://docs.cloud.google.com/apigee/docs/apihub/api-observation-overview#discovered-api-observations) using the Google Cloud console or the APIM API.

### Console

To view discovered API observations, do the following:

  1. In the Google Cloud console, go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  2. Click ![](https://docs.cloud.google.com/static/cloud/console/web/common/icons/common/18px/radar.svg)**API observations** from the left navigation menu to open the **API observations** page.

The **API observations** page displays all the discovered API observations in your API ecosystem.




### REST

To list all the discovered API observations using the `DiscoveredApiObservations` API, use the following API call: 
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    "https://apihub.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/discoveredApiObservations"
    

Replace the following:

  * PROJECT_ID: The name of your API hub host project. The host project was selected when API hub was provisioned.
  * LOCATION: The location of the host project. The location was chosen when API hub was provisioned.



## Analyze discovered API observations in API hub

You can analyze a specific discovered API observation to examine the individual API operations and associated metadata of the observation. 

### Console

To analyze a specific discovered API observation, do the following:

  1. In the Google Cloud console, go to the **API hub** page. 

[Go to API hub](https://console.cloud.google.com/apigee/api-hub)

  2. Click ![](https://docs.cloud.google.com/static/cloud/console/web/common/icons/common/18px/radar.svg)**API observations** from the left navigation menu to open the **API observations** page.
  3. Click the **Host name** of the discovered API observation that you want to analyze. 

The observation details page appears displaying the associated API metadata and API operations collected by API hub. 




### API operation details

The API operation details section displays the following information: 

  * **Path** : the HTTP request path for the API operation.
  * **Method** : the HTTP request method string.
  * **Count** : the total number of times API observations in API hub observed this operation.
  * **Observation** : indicates if the API is **Known** or **Unknown**. You can click the observation to view its complete resource definition in API hub. **Known API:** APIs that are [registered](https://docs.cloud.google.com/apigee/docs/apihub/quickstart-api) with API hub. 

**Unknown API:** APIs that are detected by API observations but are not registered with API hub. 

  * **Transaction Request** : lists the key value pairs of the request headers and their count.
  * **Transaction Response Headers** : lists the key value pairs of response headers and their count.
  * **Transaction Response Codes** : lists the key value pairs of response codes and their count.
  * **First Seen** : the timestamp when the API operation was first observed.
  * **Last Seen** : The timestamp when this API operation was last .



### REST

To analyze a specific discovered API observation, do the following:

  * To retrieve detailed information for a specific discovered API observation, use the following API call: 
        
        curl -X GET \
              -H "Authorization: Bearer $(gcloud auth print-access-token)" \
            "https://apihub.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/discoveredApiObservations/OBSERVATION_ID
            

Replace the following:

    * PROJECT_ID: The name of your API hub host project. The host project was selected when API hub was provisioned.
    * LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
    * OBSERVATION_ID: The ID of the discovered API observation.
  * To retrieve a list of all the API operations in a specific discovered API observation, use the following API call: 
        
        curl -X GET \
                -H "Authorization: Bearer $(gcloud auth print-access-token)" \
              "https://apihub.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/discoveredApiObservations/OBSERVATION_ID/discoveredApiOperations"
              

Replace the following:

    * PROJECT_ID: The name of your API hub host project. The host project was selected when API hub was provisioned.
    * LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
    * OBSERVATION_ID: The ID of the discovered API observation.
  * To retrieve detailed information for a specific API operation, use the following API call: 
        
        curl -X GET \
                -H "Authorization: Bearer $(gcloud auth print-access-token)" \
              "https://apihub.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/discoveredApiObservations/OBSERVATION_ID/discoveredApiOperations/OPERATION_ID"
              

Replace the following:

    * PROJECT_ID: The name of your API hub host project. The host project was selected when API hub was provisioned.
    * LOCATION: The location of the host project. The location was chosen when API hub was provisioned.
    * OBSERVATION_ID: The ID of the discovered API observation.
    * OPERATION_ID: The ID of the API operation.



## Stop collecting API observations in API hub

Stopping the collection of API observations in API hub temporarily stops the ingestion of new data. This operation doesn't delete the existing data that is already ingested in API hub. You can stop collecting API observations data in API hub using any of the following methods: 

  * [Detach runtime project](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#detach-a-runtime-project) from API hub.
  * [Edit project association settings](https://docs.cloud.google.com/apigee/docs/apihub/auto-register-apigee-proxies#edit-project-association-settings) to deselect the **Apigee API Observation** import configuration. **Important:** Deselecting the **Apigee API Observation** import configuration doesn't automatically disable or delete any Apigee API observation jobs from the Apigee runtime projects. This also means that the underlying Shadow API Discovery job will continue to run and incur charges in Apigee. You must disable any Apigee API observation jobs manually in Apigee runtime projects to avoid this. Disabling a job preserves its results, while deleting it removes both the job and its associated observation results. 
  * [Delete the associated plugin instance](https://docs.cloud.google.com/apigee/docs/apihub/manage-plugin-instances#delete-plugin-instance) from API hub.



## Considerations

The following considerations apply when managing API observation data in API hub: 

  * When you stop collecting API observations in API hub, the data that has already been collected is not deleted. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
