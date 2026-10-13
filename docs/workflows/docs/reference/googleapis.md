---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/
title: Connectors reference \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:21:35.870618+00:00
---

# Connectors reference  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Connectors reference Stay organized with collections  Save and categorize content based on your preferences. 

Workflows publishes connectors that make it easier to access other Google Cloud products within a workflow. This document details the correct Workflows syntax for the available connectors.

For workflow samples that demonstrate how to use a connector, see each connector's overview page.

To learn more about authentication, and behavior during retries and long-running operations, see [Understand connectors](https://docs.cloud.google.com/workflows/docs/connectors).

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



## List of supported connectors

Google Cloud product | Connector | Long-running operation type  
---|---|---  
[AI Platform Training](https://docs.cloud.google.com/ai-platform/training/docs) | [ml](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/ml/Overview) | [Job](https://docs.cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.jobs#Job)  
[Application Integration](https://docs.cloud.google.com/application-integration/docs) | [integrations](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/integrations/Overview) | None  
[Batch](https://docs.cloud.google.com/batch/docs) | [batch](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/batch/Overview)   
| [Job](https://docs.cloud.google.com/batch/docs/reference/rest/v1/projects.locations.jobs#Job)   
[Operation](https://docs.cloud.google.com/batch/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)  
[BigQuery](https://docs.cloud.google.com/bigquery/docs) | [bigquery](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/bigquery/Overview) | [Job](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/Job)  
[BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction) | [bigquerydatatransfer](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/bigquerydatatransfer/Overview) | [TransferRun](https://docs.cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs.runs)  
[Cloud Build](https://docs.cloud.google.com/build/docs) | [cloudbuild](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/cloudbuild/Overview) | [Operation](https://docs.cloud.google.com/build/docs/api/reference/rest/v1/operations#Operation)  
[Cloud Run functions](https://docs.cloud.google.com/functions/docs) | [cloudfunctions](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/cloudfunctions/Overview) | [Operation](https://docs.cloud.google.com/functions/docs/reference/rest/v1/operations#Operation)  
[Cloud Natural Language API](https://docs.cloud.google.com/natural-language/docs) | [language](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/language/Overview) | None  
[Cloud Run](https://docs.cloud.google.com/run/docs) | [run](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/run/Overview) | None  
[Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs) | [cloudscheduler](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/cloudscheduler/Overview) | None  
[Cloud SQL](https://docs.cloud.google.com/sql/docs) | [sqladmin](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/sqladmin/Overview) | [Operation](https://docs.cloud.google.com/sql/docs/mysql/admin-api/rest/v1beta4/operations#Operation)  
[Cloud Storage](https://docs.cloud.google.com/storage/docs) | [storage](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/storage/Overview) | None  
[Cloud Tasks](https://docs.cloud.google.com/tasks/docs) | [cloudtasks](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/cloudtasks/Overview) | None  
[Cloud Translation](https://docs.cloud.google.com/translate/docs) | [translate](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/translate/Overview) | [Operation](https://docs.cloud.google.com/translate/docs/reference/rest/v3/projects.locations.operations)  
[Compute Engine](https://docs.cloud.google.com/compute/docs) | [compute](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/compute/Overview) | [Operation](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalOperations#resource:-operation)  
[Dataflow](https://docs.cloud.google.com/dataflow/docs) | [dataflow](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/dataflow/Overview) | [Job](https://docs.cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.locations.jobs#resource:-job)  
[Document AI](https://docs.cloud.google.com/document-ai/docs) | [documentai](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/documentai/Overview)   
| [Operation](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.operations#Operation)   
[Processor](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors#Processor)  
[Firestore](https://docs.cloud.google.com/firestore/docs) | [firestore](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/firestore/Overview) | [Operation](https://docs.cloud.google.com/firestore/docs/reference/rest/Shared.Types/Operation)  
[Google Forms](https://developers.google.com/forms/api/guides) | [forms](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/forms/Overview) | None  
[Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs) | [container](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/container/Overview) | [Operation](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.operations#resource:-operation)  
[Google Sheets](https://developers.google.com/sheets/api/guides/concepts) | [sheets](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/sheets/Overview) | None  
[Kubernetes API (control plane)](https://docs.cloud.google.com/workflows/docs/access-kubernetes-api) | [gke](https://docs.cloud.google.com/workflows/docs/reference/connectors/gke/Overview) | None  
[Pub/Sub](https://docs.cloud.google.com/pubsub/docs) | [pubsub](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/pubsub/Overview) | None  
[Resource Manager](https://docs.cloud.google.com/resource-manager/docs) | [cloudresourcemanager](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/cloudresourcemanager/Overview) | None  
[Secret Manager](https://docs.cloud.google.com/secret-manager/docs) | [secretmanager](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/secretmanager/Overview) | None  
[Spanner](https://docs.cloud.google.com/spanner/docs) | [spanner](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/spanner/Overview) | [Operation](https://docs.cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.backups.operations#Operation)  
[Storage Transfer Service](https://docs.cloud.google.com/storage-transfer/docs) | [storagetransfer](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/storagetransfer/Overview) | [Operation](https://docs.cloud.google.com/storage-transfer/docs/reference/rest/v1/Operation)  
[Transcoder API](https://docs.cloud.google.com/transcoder/docs) | [transcoder](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/transcoder/Overview) | [Job](https://docs.cloud.google.com/transcoder/docs/reference/rest/v1/projects.locations.jobs#Job)  
[Vertex AI](https://docs.cloud.google.com/vertex-ai/docs) | [aiplatform (Vertex AI)](https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/Overview)   
| [Artifact](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.metadataStores.artifacts#Artifact)   
[Execution](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.metadataStores.executions#Execution)   
[Job](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.batchPredictionJobs#BatchPredictionJob)   
[Operation](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)   
[Pipeline](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.pipelineJobs#PipelineJob)   
[Schedule](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.schedules#Schedule)   
[Study](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.studies#Study)   
[Trial](https://docs.cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.studies.trials#Trial)  
[Workflows](https://docs.cloud.google.com/workflows/docs) | [workflows](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/workflows/Overview)   
[workflowexecutions](https://docs.cloud.google.com/workflows/docs/reference/stdlib/googleapis/workflowexecutions/Overview) | [Operation](https://docs.cloud.google.com/workflows/docs/reference/rest/v1/projects.locations.operations)   
[Execution](https://docs.cloud.google.com/workflows/docs/reference/executions/rest/v1/projects.locations.workflows.executions)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
