---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/v2/routines/update/
title: Method: googleapis.bigquery.v2.routines.update \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:20.934440+00:00
---

# Method: googleapis.bigquery.v2.routines.update  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/bigquery/v2/routines/update/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.bigquery.v2.routines.update Stay organized with collections  Save and categorize content based on your preferences. 

Updates information in an existing routine. The update method replaces the entire Routine resource. # IAM Permissions Requires the `bigquery.routines.update` permission on the routine.

## Arguments

Parameters  
---  
`datasetId` |  `string` Required. Dataset ID of the routine to update  
`projectId` |  `string` Required. Project ID of the routine to update  
`routineId` |  `string` Required. Routine ID of the routine to update  
`body` |  `object ([Routine](https://cloud.google.com/workflows/docs/reference/googleapis/bigquery/v2/Overview#Routine))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`Routine`](https://cloud.google.com/workflows/docs/reference/googleapis/bigquery/v2/Overview#Routine).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/routines/update).

### YAML
    
    
    - update:
        call: googleapis.bigquery.v2.routines.update
        args:
            datasetId: ...
            projectId: ...
            routineId: ...
            body:
                arguments: ...
                dataGovernanceType: ...
                definitionBody: ...
                description: ...
                determinismLevel: ...
                externalRuntimeOptions:
                    containerCpu: ...
                    containerMemory: ...
                    containerRequestConcurrency: ...
                    maxBatchingRows: ...
                    runtimeConnection: ...
                    runtimeVersion: ...
                    volumeMounts: ...
                importedLibraries: ...
                language: ...
                pythonOptions:
                    entryPoint: ...
                    packages: ...
                remoteFunctionOptions:
                    connection: ...
                    endpoint: ...
                    maxBatchingRows: ...
                    userDefinedContext: ...
                returnTableType:
                    columns: ...
                returnType:
                    arrayElementType: ...
                    rangeElementType: ...
                    structType:
                        fields: ...
                    typeKind: ...
                routineReference:
                    datasetId: ...
                    projectId: ...
                    routineId: ...
                routineType: ...
                securityMode: ...
                sparkOptions:
                    archiveUris: ...
                    connection: ...
                    containerImage: ...
                    fileUris: ...
                    jarUris: ...
                    mainClass: ...
                    mainFileUri: ...
                    properties: ...
                    pyFileUris: ...
                    runtimeVersion: ...
                strictMode: ...
        result: updateResult

### JSON
    
    
    [
      {
        "update": {
          "call": "googleapis.bigquery.v2.routines.update",
          "args": {
            "datasetId": "...",
            "projectId": "...",
            "routineId": "...",
            "body": {
              "arguments": "...",
              "dataGovernanceType": "...",
              "definitionBody": "...",
              "description": "...",
              "determinismLevel": "...",
              "externalRuntimeOptions": {
                "containerCpu": "...",
                "containerMemory": "...",
                "containerRequestConcurrency": "...",
                "maxBatchingRows": "...",
                "runtimeConnection": "...",
                "runtimeVersion": "...",
                "volumeMounts": "..."
              },
              "importedLibraries": "...",
              "language": "...",
              "pythonOptions": {
                "entryPoint": "...",
                "packages": "..."
              },
              "remoteFunctionOptions": {
                "connection": "...",
                "endpoint": "...",
                "maxBatchingRows": "...",
                "userDefinedContext": "..."
              },
              "returnTableType": {
                "columns": "..."
              },
              "returnType": {
                "arrayElementType": "...",
                "rangeElementType": "...",
                "structType": {
                  "fields": "..."
                },
                "typeKind": "..."
              },
              "routineReference": {
                "datasetId": "...",
                "projectId": "...",
                "routineId": "..."
              },
              "routineType": "...",
              "securityMode": "...",
              "sparkOptions": {
                "archiveUris": "...",
                "connection": "...",
                "containerImage": "...",
                "fileUris": "...",
                "jarUris": "...",
                "mainClass": "...",
                "mainFileUri": "...",
                "properties": "...",
                "pyFileUris": "...",
                "runtimeVersion": "..."
              },
              "strictMode": "..."
            }
          },
          "result": "updateResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
