---
url: https://docs.cloud.google.com/service-infrastructure/docs/polling-operations/
title: Polling Long Running Operations \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:09.742182+00:00
---

# Polling Long Running Operations  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/polling-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure/docs)
  * [ Guides ](https://docs.cloud.google.com/service-infrastructure/docs/how-to)



Send feedback 

#  Polling Long Running Operations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to programmatically poll the long-running [operation](https://docs.cloud.google.com/service-infrastructure/docs/glossary#operation) resources returned by methods in Service Infrastructure APIs that take a substantial amount of time to complete, such as [`service.rollouts.create`](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/services.rollouts/create). After an operation is done, the `done` field will be set to true.

**Note:** While you typically interact with long-running [operations](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/operations) as a result of calling methods in the Service Management API, the Service Consumer Management API also provides methods for interacting with long-running operation resources, such as [`operations.get`](https://docs.cloud.google.com/service-infrastructure/docs/service-consumer-management/reference/rest/v1/operations/get).

To poll an operation, repeatedly invoke the [`operations.get`](https://docs.cloud.google.com/service-infrastructure/docs/service-management/reference/rest/v1/operations/get) method with a recommended 10 seconds backoff until the operation is done:
    
    
    # This is an example of getting a pending `Operation` resource.
    gcurl https://servicemanagement.googleapis.com/v1/operations/rollouts.endpointsapis.appspot.com:2016-07-16r2
    {
      "name": "operations/rollouts.endpointsapis.appspot.com:2016-07-16r2",
      "metadata": {
        "@type": "type.googleapis.com/google.api.servicemanagement.v1.OperationMetadata",
        "resourceNames": [
          "services/endpointsapis.appspot.com/rollouts/2016-07-16r2"
        ],
        "steps": [
          {
            "description": "update Service Controller",
            "status": "In_PROGRESS"
          }
        ],
        "progressPercentage": 0,
        "startTime": "2016-07-16T00:56:55.737Z",
      }
      "response": {
      "@type": "type.googleapis.com/google.api.servicemanagement.v1.Rollout",
      "rolloutId": "2016-07-16r2",
      "createTime": "2016-07-16T00:56:55.724Z",
      "serviceSelectionStrategy": {
        "serviceConfigIds": [
          "2016-07-16r1"
        ]
      },
      "serviceName": "endpointsapis.appspot.com"
    }
    
    # This is an example of getting a done `Operation` resource.
    gcurl https://servicemanagement.googleapis.com/v1/operations/rollouts.endpointsapis.appspot.com:2016-07-16r2
    {
      "name": "operations/rollouts.endpointsapis.appspot.com:2016-07-16r2",
      "metadata": {
        "@type": "type.googleapis.com/google.api.servicemanagement.v1.OperationMetadata",
        "resourceNames": [
          "services/endpointsapis.appspot.com/rollouts/2016-07-16r2"
        ],
        "steps": [
          {
            "description": "update Service Controller",
            "status": "Done"
          }
        ],
        "progressPercentage": 100,
        "startTime": "2016-07-16T00:56:55.737Z",
      }
      "done": true,
      "response": {
      "@type": "type.googleapis.com/google.api.servicemanagement.v1.Rollout",
      "rolloutId": "2016-07-16r2",
      "createTime": "2016-07-16T00:56:55.724Z",
      "serviceSelectionStrategy": {
        "serviceConfigIds": [
          "2016-07-16r1"
        ]
      },
      "serviceName": "endpointsapis.appspot.com"
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
