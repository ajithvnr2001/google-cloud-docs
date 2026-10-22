---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/consent-access-determination/
title: Making access determinations \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:32.185412+00:00
---

# Making access determinations  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/consent-access-determination/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Making access determinations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to make access determinations using the Consent Management API.

Applications can request access determinations from the Consent Management API for a specific data element, for all data elements associated with a user, or for whole data stores. In each case, the Consent Management API makes an access determination by evaluating the following information against the information contained in the access request:

  * The user consent, such as the values of `REQUEST` attributes
  * The user data mappings, such as the values of `RESOURCE` attributes.



By default, access determinations only evaluate `ACTIVE` consents. `DRAFT` consents can be included in an access determination by specifying them in an access determination request.

Access determination requests always ignore consents that are expired, revoked, or rejected.

## Making consent access determinations for specific data elements

You can request an access determination for a specific data element using the [`projects.locations.datasets.consentStores.checkDataAccess`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/checkDataAccess) method. This method returns a message indicating if the specified `UserDataMapping` has valid consent for the proposed use.

To request an access determination for a specific data element, make a `POST` request and specify the following information in the request:

  * The name of the parent consent store.
  * A data resource ID, which is a description of the data element such as the REST path to a resource.
  * A set of key-value pairs that represent the requestor in terms of the relevant `REQUEST` attributes and their values. For example, `requesterIdentity == external-researcher`.
  * An optional flag indicating whether detailed access determinations should be returned. If this flag is set to `FULL`, the method returns results for every consent evaluated. If this flag is set to `BASIC`, or not defined, the method returns only whether access to the specified data is permitted by the evaluated consents. This optional feature is used when your application needs to inspect how a consent determination was made.
  * An optional list of `ACTIVE` or `DRAFT` consents for the method to consider. If no consents are specified, the method evaluates all `ACTIVE` consents. This optional feature can be used to test the behavior of new or specific consents.
  * An access token



### curl

The following sample shows a `POST` request using `curl`:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/consent+json; charset=utf-8" \
        --data "{
           'dataId' : 'DATA_ID',
           'requestAttributes': {
             'requesterIdentity': 'external-researcher'},
           'consentList':{
             'consents':[
               'projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_NAME'
             ]
           },
           'responseView': 'DETAILED_ACCESS_LEVEL'
        }" \
    "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID:checkDataAccess"

If the request is successful, the server returns a response similar to the following sample in JSON format, or an empty response body if no user data matches the specified data access. The sample response uses `FULL` as the `responseView`.
    
    
    {
      "consentDetails": {                                                                                                                         "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID": {
          "evaluationResult": "EVALUATION_RESULT"
        }
      }
    }
    

`EVALUATION_RESULT` is one of `NOT_APPLICABLE`, `NO_MATCHING_POLICY`, `NO_SATISFIED_POLICY`, or`HAS_SATISFIED_POLICY`.

### PowerShell

The following sample shows a `POST` request using Windows PowerShell:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/consent+json; charset=utf-8" `
      -Body "{
           'dataId' : 'DATA_ID',
           'requestAttributes': {
             'requesterIdentity': 'external-researcher'
           },
           'consentList': {
             'consents':[
               'projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID'
             ]
           },
           'responseView': 'DETAILED_ACCESS_LEVEL'
        }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID:checkDataAccess" | Select-Object -Expand Content

If the request is successful, the server returns a response similar to the following sample in JSON format, or an empty response body if no user data matches the specified data access. The sample response uses `FULL` as the `responseView`.
    
    
    {
      "consentDetails": {                                                                                                                         "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID": {
          "evaluationResult": "EVALUATION_RESULT"
        }
      }
    }
    

`EVALUATION_RESULT` is one of `NOT_APPLICABLE`, `NO_MATCHING_POLICY`, `NO_SATISFIED_POLICY`, or`HAS_SATISFIED_POLICY`.

## Making an access determination for all consents for a user

You can request an access determination for all data elements associated with a user by using the [`projects.locations.datasets.consentStores.evaluateUserConsents`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/evaluateUserConsents) method. This method returns all data elements associated with a specific user that have valid consent for the proposed use.

To request an access determination for all data elements associated with a user, make a `POST` request and specify the following information in the request:

  * The name of the parent consent store.
  * A user ID that defines the data elements and consents to evaluate.
  * An optional set of key-value pairs that define the `RESOURCE` attributes of the data elements to evaluate. For example, `dataIdentifiable == de-identified`. If you don't define a set of `RESOURCE` attributes, all data elements are evaluated.
  * A set of key-value pairs that define the relevant `REQUEST` attributes and their values. For example, `requesterIdentity == external-researcher`.
  * An optional flag indicating whether detailed access determinations should be returned. If this flag is set to `FULL`, the method returns results for every consent evaluated. If this flag is set to `BASIC`, or not defined, the method returns only whether access to the specified data is permitted by the evaluated consents. This optional feature is used when your application needs to inspect how a consent determination was made.
  * An optional list of `ACTIVE` or `DRAFT` consents for the method to consider. If no consents are specified, the method evaluates all `ACTIVE` consents. This optional feature can be used to test the behavior of new or specific consents.
  * An access token



### curl

The following sample shows a `POST` request using `curl`:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/consent+json; charset=utf-8" \
        --data "{
           'userId' :
             'USER_ID',
           'consentList':{
             'consents':[
               'projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID'
             ]
           },
           'resourceAttributes': {
             'dataIdentifiable': 'de-identified'
           },
           'requestAttributes': {
             'requesterIdentity': 'external-researcher'
           },
           'responseView': 'DETAILED_ACCESS_LEVEL'
        }" \
    "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID:evaluateUserConsents"

If the request is successful, the server returns a response similar to the following sample in JSON format, or an empty response body if no user data matches the specified data access. The sample response uses `FULL` as the `responseView`.
    
    
    {
      "results": [
        {
          "dataId": "DATA_ID",
          "consentDetails": {
           "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID": {
           "evaluationResult": "EVALUATION_RESULT"
            }
          }
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
           'userId' : 'USER_ID',
           'consentList':{
             'consents':[
               'projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_NAME'
             ]
           },
           'resourceAttributes': { 'dataIdentifiable': 'de-identified'},
           'requestAttributes': { 'requesterIdentity': 'external-researcher'},
           'responseView': 'DETAILED_ACCESS_LEVEL'
        }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID:evaluateUserConsents" | Select-Object -Expand Content

If the request is successful, the server returns a response similar to the following sample in JSON format, or an empty response body if no user data matches the specified data access. The sample response uses `FULL` as the `responseView`.
    
    
    {
      "results": [
        {
          "dataId": "DATA_ID",
          "consentDetails": {
           "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID/consents/CONSENT_ID": {
           "evaluationResult": "EVALUATION_RESULT"
            }
          }
        }
      ]
    }
    

## Making access determinations for consent stores

You can request an access determination for an entire consent store using the [`projects.locations.datasets.consentStores.queryAccessibleData`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/queryAccessibleData) method. This method returns all data elements within a consent store that have valid consent.

**Important:** This method returns a [long-running operation (LRO)](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations) and is best used in batch operations.

To request an access determination across an entire consent store, make a `POST` request and specify the following information in the request:

  * The name of the parent consent store
  * A set of key-value pairs that define the relevant `REQUEST` attributes and their values. For example, `requesterIdentity == external-researcher`.
  * An optional set of key-value pairs that define the `RESOURCE` attributes of the data elements to evaluate. For example, `dataIdentifiable == de-identified`. If you do not define a set of `RESOURCE` attributes, all data elements are evaluated
  * A Cloud Storage destination where the list of results is saved. The Cloud Healthcare API service account must have the `roles/storage.objectAdmin` IAM role on this destination. For more information, see [Consent store Cloud Storage permissions](https://docs.cloud.google.com/healthcare-api/docs/how-tos/permissions-healthcare-api-gcp-products#consent_store_gcs_permissions).
  * An access token



### curl

The following sample shows a `POST` request using `curl`:
    
    
    curl -X POST \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/consent+json; charset=utf-8" \
        --data "{
           'gcsDestination': {
             'uriPrefix': 'gs://BUCKET/DIRECTORY'
           },
           'resourceAttributes': {
             'dataIdentifiable': 'de-identified'
           },
           'requestAttributes': {
             'requesterIdentity': 'external-researcher'
           }
        }" \
    "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID:queryAccessibleData"

If the request is successful, the server returns a response similar to the following sample in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. To track the status of the operation, you can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get):
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"

If the request is successful, the server returns a response with the status of the operation in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1beta1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1beta1.consent.consentService.queryAccessibleData",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME"
        "logsUrl": "LOGS_URL",
        "counter": {
          "success": "SUCCESS_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.protobuf.Empty"
      }
    }
    

After the long-running operation completes, the results appear in a text file in the folder you specified. For information about long-running operations, see [Managing long-running operations](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations).

### PowerShell

The following sample shows a `POST` request using Windows PowerShell:
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/consent+json; charset=utf-8" `
      -Body "{
           'gcsDestination': {
             'uriPrefix': 'gs://BUCKET/DIRECTORY'
           },
           'resourceAttributes': {
             'dataIdentifiable': 'de-identified'
           },
           'requestAttributes': {
             'requesterIdentity': 'external-researcher'
           }
        }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/consentStores/CONSENT_STORE_ID:queryAccessibleData" | Select-Object -Expand Content

If the request is successful, the server returns a response similar to the following sample in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID"
    }
    

The response contains an operation name. To track the status of the operation, you can use the [Operation `get` method](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.operations/get):
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID" | Select-Object -Expand Content

If the request is successful, the server returns a response with the status of the operation in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.healthcare.v1beta1.OperationMetadata",
        "apiMethodName": "google.cloud.healthcare.v1beta1.consent.consentService.queryAccessibleData",
        "createTime": "CREATE_TIME",
        "endTime": "END_TIME"
        "logsUrl": "LOGS_URL",
        "counter": {
          "success": "SUCCESS_COUNT"
        }
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.protobuf.Empty"
      }
    }
    

After the long-running operation completes, the results appear in a text file in the folder you specified. For information about long-running operations, see [Managing long-running operations](https://docs.cloud.google.com/healthcare-api/docs/how-tos/long-running-operations).

## Logging access determination requests and responses

When [Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access) are enabled, the Consent Management API logs requests made using the [`checkDataAccess`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/checkDataAccess), [`evaluateUserConsents`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/evaluateUserConsents), and [`queryAccessibleData`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.consentStores/queryAccessibleData) methods. These logs record the information contained within the request, such as the target `UserDataMapping` or the specified `RESOURCE` or `REQUEST` attributes. Logs will also contain the API response, which includes the result of the Consent Management API access determination. Each log includes the identity of the Google Cloud tool making the request.

For more information on enabling Data Access audit logs, see [Configuring Data Access audit logs](https://docs.cloud.google.com/logging/docs/audit/configure-data-access). For more information on audit logging in the Cloud Healthcare API, see [Viewing Cloud Audit Logs](https://docs.cloud.google.com/healthcare-api/docs/how-tos/audit-logging).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
