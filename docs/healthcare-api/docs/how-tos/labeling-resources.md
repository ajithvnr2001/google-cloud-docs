---
url: https://docs.cloud.google.com/healthcare-api/docs/how-tos/labeling-resources/
title: Using resource labels \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:29:28.827897+00:00
---

# Using resource labels  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/how-tos/labeling-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  Using resource labels Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to add, view, edit, and remove labels on Cloud Healthcare API resources. Labels are key-value pairs you can use to organize resources. You can attach a label to individual resources, then filter the resources based on their labels. Information about labels is forwarded to the billing system, so you can [break down your billing charges](https://docs.cloud.google.com/billing/docs/how-to/bq-examples) by label.

You can use labels with the following Cloud Healthcare API resources:

  * FHIR stores
  * DICOM stores
  * Consent stores
  * HL7v2 stores
  * HL7v2 messages



Labels are available using the REST or RPC APIs. Labels are not available in the Google Cloud CLI or Google Cloud console.

## Label requirements

The labels applied to a resource must meet the following requirements:

  * Each resource can have multiple labels, up to a maximum of 64.
  * Each label must be a key-value pair.
  * Keys have a minimum length of 1 character and a maximum length of 63 characters, and cannot be empty. Values can be empty and have a maximum length of 63 characters.
  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes. All characters must use UTF-8 encoding and international characters are allowed.
  * The key of a label must be unique in a single resource, but you can use the same key with multiple resources.
  * Keys must start with a lowercase letter or international character.



## Adding a label

The following sample shows how to add a label to an existing FHIR store.

For example, you could use the label to signify that the FHIR store is being used as a test environment. The key for the label would be `environment` and the value would be `test`.

### curl

To add a label to an existing FHIR store, make a `PATCH` request and specify the following information:

  * The name of the parent dataset
  * The name of the FHIR store
  * The label data to update
  * An update mask set to `labels`
  * An access token



The following sample shows a `PATCH` request using `curl`.
    
    
    curl -X PATCH \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'labels': {
            'KEY' : 'VALUE'
          }
         }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID?updateMask=labels"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
      "labels": {
        "KEY": "VALUE"
      }
    }
    

### PowerShell

To add a label to an existing FHIR store, make a `PATCH` request and specify the following information:

  * The name of the parent dataset
  * The name of the FHIR store
  * The label data to update
  * An update mask set to `labels`
  * An access token



The following sample shows a `PATCH` request using Windows PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Patch `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
          'labels': {
            'KEY': 'VALUE'
          }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID?updateMask=labels" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
      "labels": {
        "KEY": "VALUE"
      }
    }
    

### Adding multiple labels

The following sample shows how to add multiple labels to an existing FHIR store. To add multiple labels, separate each label by a comma.

For example, you could use the labels to signify that the FHIR store is being used as a test environment and that it's used for a research team.

The key for the first label would be `environment` and the value would be `test`. The key for the second label would be `team` and the value would be `research`.

### curl

To add multiple labels to an existing FHIR store, make a `PATCH` request and specify the following information:

  * The name of the parent dataset
  * The name of the FHIR store
  * The label data to update as a comma-delimited list of key-value pairs
  * An update mask set to `labels`
  * An access token



The following sample shows a `PATCH` request using `curl`.
    
    
    curl -X PATCH \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'labels': {
            'KEY_1' : 'VALUE_1',
            'KEY_2' : 'VALUE_2'
          }
         }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID?updateMask=labels"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
      "labels": {
        "KEY_1": "VALUE_1",
        "KEY_2": "VALUE_2"
      }
    }
    

### PowerShell

To add a label to an existing FHIR store, make a `PATCH` request and specify the following information:

  * The name of the parent dataset
  * The name of the FHIR store
  * The label data to update as a comma-delimited list of key-value pairs
  * An update mask set to `labels`
  * An access token



The following sample shows a `PATCH` request using Windows PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Patch `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
          'labels': {
            'KEY_1': 'VALUE_1',
            'KEY_2': 'VALUE_2'
          }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID?updateMask=labels" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
      "labels": {
        "KEY_1": "VALUE_1",
        "KEY_2": "VALUE_2"
      }
    }
    

## Listing and filtering by labels

After you add a label to a Cloud Healthcare API resource, you can list resources and filter them by their labels. For example, after adding a label to a FHIR store in the previous samples, you can list the FHIR stores in your dataset and filter by the labels you added.

HL7v2 messages have additional filtering options that you can view in [`projects.locations.datasets.hl7V2Stores.messages.list`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/list#body.QUERY_PARAMETERS.filter).

### curl

To view the FHIR stores in a dataset and filter them by a label, make a `GET` request and provide the following information:

  * The name of the parent dataset
  * The name of the FHIR store
  * A query string containing the information to filter by
  * An access token



The following sample shows a `GET` request using `curl`.
    
    
    curl -X GET \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores?filter=labels.KEY=VALUE"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "fhirStores": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
          "labels": {
            "KEY": "VALUE"
          }
        },
        {
          ...
        }
      ]
    }
    

### PowerShell

To view the FHIR stores in a dataset and filter them by a label, make a `GET` request and provide the following information:

  * The name of the parent dataset
  * The name of the FHIR store
  * A query string containing the information to filter by
  * An access token



The following sample shows a `GET` request using Windows PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Get `
      -Headers $headers `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores?filter=labels.KEY=VALUE" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "fhirStores": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
          "labels": {
            "KEY": "VALUE"
          }
        },
        {
          ...
        }
      ]
    }
    

## Removing a label

You can remove a label in one of two ways:

  * To remove the label entirely, meaning that both the key and the value are removed, use the read-modify-write pattern by completing the following steps:

    1. Read the current labels by calling the resource's `get()` method.
    2. Edit the returned labels, either by using a text editor or programmatically, to add or remove any applicable keys and their values.
    3. Write the updated labels by calling the resource's `patch()` method.
  * To keep the key and remove the value, set the value to `null`.




### curl

The following sample shows how to remove a label by setting the value of the label to `null`.

To remove a label from an existing FHIR store, make a `PATCH` request and specify the following information:

  * The name of the parent dataset
  * The name of the FHIR store
  * The label data to update
  * An update mask set to `labels`
  * An access token



The following sample shows a `PATCH` request using `curl`.
    
    
    curl -X PATCH \
        -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -H "Content-Type: application/json; charset=utf-8" \
        --data "{
          'labels': {
            'KEY' : null
          }
         }" "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID?updateMask=labels"

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
      "labels": {
        "KEY":
      }
    }
    

### PowerShell

The following sample shows how to remove a label by setting the value of the label to `null`.

To remove a label from an existing FHIR store, make a `PATCH` request and specify the following information:

  * The name of the parent dataset
  * The name of the FHIR store
  * The label data to update
  * An update mask set to `labels`
  * An access token



The following sample shows a `PATCH` request using Windows PowerShell.
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ Authorization = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method Post `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body "{
          'labels': {
            'KEY': nullresource_manager_api
          }
      }" `
      -Uri "https://healthcare.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID?updateMask=labels" | Select-Object -Expand Content

If the request is successful, the server returns the response in JSON format:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/fhirStores/FHIR_STORE_ID",
      "labels": {
        "KEY":
      }
    }
    

## What's next

[Read about other uses for labels with the Cloud Resource Manager API](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
