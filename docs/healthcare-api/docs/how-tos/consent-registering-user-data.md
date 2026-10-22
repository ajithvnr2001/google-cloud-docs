---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/consent-registering-user-data/
title: Registering user data \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:54.370244+00:00
---

# Registering user data  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/consent-registering-user-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Registering user data Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to register user data with the Consent Management API.

Data elements are registered with the Consent Management API and connected to consents using user data mappings. User data is never stored in the Consent Management API.

The user data mappings, represented as [`UserDataMappings`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.userDataMappings) resources, include the following elements:

  * A user ID that identifies the user. This ID matches the ID the application provided the Consent Management API when registering the consent.
  * A data ID that identifies user data stored elsewhere, such as on Google Cloud or on-premises. The data ID can be an opaque ID, a URL, or any other identifier.
  * Resource attributes, which describe the characteristics of the user data using resource attribute values configured for the consent store using attribute definitions. For example, the data could include the `attribute_definition_id` `data_identifiable` with the value of `de-identified`.



The following diagram shows the data flow for creating user data mappings:

![user data mappings](https://docs.cloud.google.com/static/healthcare-api/images/user_data_mapping.png)

## Registering user data mappings

To create a user data mapping, use the [`projects.locations.datasets.consentStores.userDataMappings.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores.userDataMappings/create) method. Make a `POST` request and specify the following information in the request:

  * The name of the parent consent store
  * A unique and opaque `userID` that represents the user with whom the data element is associated
  * An identifier for the user data resource, such as the REST path to a unique resource
  * A set of `RESOURCE` attributes that describe the data element
  * An access token



### curl

The following sample shows a `POST` request using `curl`:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/consent+json; charset=utf-8" \
        --data "{
           'user_id': 'USER_ID',
           'data_id' : 'DATA_ID',
           'resource_attributes': [{
               'attribute_definition_id': 'data_identifiable',
               'values': ['de-identified']
          }]
        }" \
    "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/userDataMappings"

If the request is successful, the server returns a response similar to the following sample in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/userDataMappings/USER_DATA_MAPPING_ID",
      "dataId": "DATA_ID",
      "userId": "USER_ID",
      "resourceAttributes": [
        {
          "attributeDefinitionId": "data_identifiable",
          "values": [
            "de-identified"
          ]
        }
      ]
    }
    

### PowerShell

The following sample shows a `POST` request using Windows PowerShell:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/consent+json; charset=utf-8" `
      -Body "{
           'user_id': 'USER_ID',
           'data_id' : 'DATA_ID',
           'resource_attributes': [{
               'attribute_definition_id': 'data_identifiable',
               'values': ['de-identified']
          }]
        }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/userDataMappings" | Select-Object -Expand Content

If the request is successful, the server returns a response similar to the following sample in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/userDataMappings/USER_DATA_MAPPING_ID",
      "dataId": "DATA_ID",
      "userId": "USER_ID",
      "resourceAttributes": [
        {
          "attributeDefinitionId": "data_identifiable",
          "values": [
            "de-identified"
          ]
        }
      ]
    }
    

## Configuring data IDs

The `data_id` field of the user data mapping resource contains a customer-specified string that describes the data that the user data mapping resource refers to. Any string is permitted, such as an opaque ID or URI.

Data IDs can be as granular as is required by your application. If the data you are registering can be described at the table or bucket level, define `data_id` as the REST path to that resource. If the data you are registering requires more granularity, then you may want to specify specific rows or cells. If your application uses conceptual resources, such as permitted actions or classes of data, you should define `data_id` with a convention that supports those use-cases.

Examples of a `data_id` that describes data stored in different services and at various levels of granularity include, but are not limited to, the following:

Google Cloud Storage object
    
    
      'data_id' : 'gs://BUCKET_NAME/OBJECT_NAME'
      

Amazon S3 object
    
    
      'data_id' : 'https://BUCKET_NAME.s3.REGION.amazonaws.com/OBJECT_NAME'
      

BigQuery table
    
    
      'data_id' : 'bigquery/v2/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID'
      

BigQuery row (there is no REST path for a BigQuery row, so your own identifier is necessary - one possible approach is below)
    
    
      'data_id' : 'bigquery/v2/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID/myRows/ROW_ID'
      

BigQuery cell (there is no REST path for a BigQuery cell, so your own identifier is necessary - one possible approach is below)
    
    
      'data_id' : 'bigquery/v2/projects/PROJECT_ID/datasets/DATASET_ID/tables/TABLE_ID/myRows/ROW_ID/myColumns/COLUMN_ID'
      

FHIR resource
    
    
      'data_id' : 'https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID/fhir/Patient/PATIENT_ID'
      

Conceptual representation
    
    
      'data_id' : 'wearables/fitness/step_count/daily_sum'
      

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
