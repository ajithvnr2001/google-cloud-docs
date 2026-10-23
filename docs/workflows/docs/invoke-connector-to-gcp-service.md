---
url: https://docs.cloud.google.com/workflows/docs/invoke-connector-to-gcp-service/
title: Invoke a Google Cloud service using a connector \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:05.135729+00:00
---

# Invoke a Google Cloud service using a connector  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/invoke-connector-to-gcp-service/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Guides ](https://docs.cloud.google.com/workflows/docs/create-workflow-console)



Send feedback 

#  Invoke a Google Cloud service using a connector Stay organized with collections  Save and categorize content based on your preferences. 

Workflows publishes connectors to make it easier to access other Google Cloud APIs within a workflow, and to integrate your workflows with those Google Cloud products. For example, you can use connectors to publish Pub/Sub messages, read or write data to a Firestore database, or retrieve authentication keys from Secret Manager. For a detailed reference of available connectors, see the [Connectors reference](https://docs.cloud.google.com/workflows/docs/reference/googleapis#list_of_supported_connectors).

Connectors simplify calling services because they handle the formatting of requests for you, providing methods and arguments so that you don't need to know the details of a Google Cloud API. To learn more about authentication, and behavior during retries and long-running operations, see [Understand connectors](https://docs.cloud.google.com/workflows/docs/connectors).

**Note:** API operations that are facilitated by Workflows connectors should not be confused with calling or invoking a Google Cloud service—such as Cloud Run functions or Cloud Run—which is done through an [HTTP request](https://docs.cloud.google.com/workflows/docs/http-requests).

## Invoke a connector call

Similar to [invoking an HTTP endpoint](https://docs.cloud.google.com/workflows/docs/http-requests), a connector call requires `call` and `args` fields. You can specify a timeout value and polling policy using the `connector_params` block:
    
    
    - STEP_NAME:
        call: CONNECTOR
        args:
            ARG: ARG_VALUE
            [...]
            body:
                KEY:KEY_VALUE
                [...]
            connector_params:
                timeout: TIMEOUT_IN_SECONDS
                polling_policy:
                    initial_delay: INITIAL_DELAY_IN_SECONDS
                    multiplier: MULTIPLIER_VALUE
                    max_delay: MAX_DELAY_IN_SECONDS
                skip_polling: SKIP_POLLING_SWITCH 
                scopes:  OAUTH2_SCOPE 
        result: RESPONSE_VALUE

Replace the following:

  * `STEP_NAME`: the name of the step.
  * `CONNECTOR` (required): the connector method in the form `googleapis.gcp_service.version.resource.operation`. For example, `googleapis.bigquery.v2.tables.get`.
  * `ARG` and `ARG_VALUE` (required): each connector call requires different arguments.
  * `KEY` and `KEY_VALUE` (optional): fields to supply input to the API.
  * Connector-specific parameters (optional): 
    * `TIMEOUT_IN_SECONDS`: time in seconds. The end-to-end duration the connector call is allowed to run for before throwing a timeout exception. The default value is `1800` and this should be the maximum for connector methods that are not long-running operations. Otherwise, for long-running operations, the maximum timeout for a connector call is `31536000` seconds (one year).
    * `INITIAL_DELAY_IN_SECONDS`: polling policy parameter with a default value of `1.0`. Only applies to long-running operation calls.
    * `MULTIPLIER_VALUE`: polling policy parameter with a default value of `1.25`. Only applies to long-running operation calls.
    * `MAX_DELAY_IN_SECONDS`: polling policy parameter with a default value of `60.0`. Only applies to long-running operation calls.
    * `SKIP_POLLING_SWITCH`: if set to `True`, the connector invocation call is non-blocking if the initial request to manage or update the resource succeeds (usually `HTTP POST`, `HTTP UPDATE`, or `HTTP DELETE`). If the initial request is not successful, retries might occur. Polling of status (`HTTP GET` requests that follow the initial request) is skipped for the long-running operation after the initial request completes. The default value is `False`.
    * `OAUTH2_SCOPE`: OAuth2 scopes to pass to the Google API. Can be a string, list of strings, space-separated string, or comma-separated string.
  * `RESPONSE_VALUE` (optional): variable name where the result of a connector call invocation step is stored.



### Example

The following workflow demonstrates using both the [Cloud Storage API connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/storage/Overview) and the [Cloud Translation API connector](https://docs.cloud.google.com/workflows/docs/reference/googleapis/translate/Overview) to translate two files to French and Spanish, saving the results in a Cloud Storage bucket.
    
    
    main:
      steps:
      - init:
          assign:
          - projectId: ${sys.get_env("GOOGLE_CLOUD_PROJECT_ID")}
          - location: ${sys.get_env("GOOGLE_CLOUD_LOCATION")}
          - inputBucketName: ${projectId + "-input-files"}
          - outputBucketName: ${projectId + "-output-files-" + string(int(sys.now()))}
      - createOutputBucket:
            call: googleapis.storage.v1.buckets.insert
            args:
              project: ${projectId}
              body:
                name: ${outputBucketName}
      - batchTranslateText:
          call: googleapis.translate.v3beta1.projects.locations.batchTranslateText
          args:
              parent: ${"projects/" + projectId + "/locations/" + location}
              body:
                  inputConfigs:
                    gcsSource:
                      inputUri: ${"gs://" + inputBucketName + "/*"}
                  outputConfig:
                      gcsDestination:
                        outputUriPrefix: ${"gs://" + outputBucketName + "/"}
                  sourceLanguageCode: "en"
                  targetLanguageCodes: ["es", "fr"]
          result: batchTranslateTextResult

## What's next

  * [Tutorial: Run a batch translation using the Cloud Translation connector](https://docs.cloud.google.com/workflows/docs/tutorials/translation-connector)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
