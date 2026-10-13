---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/ml/v1/projects.models.versions/create/
title: Method: googleapis.ml.v1.projects.models.versions.create \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:20:03.144570+00:00
---

# Method: googleapis.ml.v1.projects.models.versions.create  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/ml/v1/projects.models.versions/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.ml.v1.projects.models.versions.create Stay organized with collections  Save and categorize content based on your preferences. 

Creates a new version of a model from a trained TensorFlow model. If the version created in the cloud by this call is the first deployed version of the specified model, it will be made the default version of the model. When you add a version to a model that already has one or more versions, the default version does not automatically change. If you want a new version to be the default, you must call projects.models.versions.setDefault.

## Arguments

Parameters  
---  
`parent` |  `string` Required. The name of the model.  
`body` |  `object ([GoogleCloudMlV1__Version](https://cloud.google.com/workflows/docs/reference/googleapis/ml/v1/Overview#GoogleCloudMlV1__Version))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`GoogleLongrunning__Operation`](https://cloud.google.com/workflows/docs/reference/googleapis/ml/v1/Overview#GoogleLongrunning__Operation).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.models.versions/create).

### YAML
    
    
    - create:
        call: googleapis.ml.v1.projects.models.versions.create
        args:
            parent: ...
            body:
                acceleratorConfig:
                    count: ...
                    type: ...
                autoScaling:
                    maxNodes: ...
                    metrics: ...
                    minNodes: ...
                container:
                    args: ...
                    command: ...
                    env: ...
                    image: ...
                    ports: ...
                deploymentUri: ...
                description: ...
                etag: ...
                explanationConfig:
                    integratedGradientsAttribution:
                        numIntegralSteps: ...
                    sampledShapleyAttribution:
                        numPaths: ...
                    xraiAttribution:
                        numIntegralSteps: ...
                framework: ...
                labels: ...
                machineType: ...
                manualScaling:
                    nodes: ...
                name: ...
                packageUris: ...
                predictionClass: ...
                pythonVersion: ...
                requestLoggingConfig:
                    bigqueryTableName: ...
                    samplingPercentage: ...
                routes:
                    health: ...
                    predict: ...
                runtimeVersion: ...
                serviceAccount: ...
        result: createResult

### JSON
    
    
    [
      {
        "create": {
          "call": "googleapis.ml.v1.projects.models.versions.create",
          "args": {
            "parent": "...",
            "body": {
              "acceleratorConfig": {
                "count": "...",
                "type": "..."
              },
              "autoScaling": {
                "maxNodes": "...",
                "metrics": "...",
                "minNodes": "..."
              },
              "container": {
                "args": "...",
                "command": "...",
                "env": "...",
                "image": "...",
                "ports": "..."
              },
              "deploymentUri": "...",
              "description": "...",
              "etag": "...",
              "explanationConfig": {
                "integratedGradientsAttribution": {
                  "numIntegralSteps": "..."
                },
                "sampledShapleyAttribution": {
                  "numPaths": "..."
                },
                "xraiAttribution": {
                  "numIntegralSteps": "..."
                }
              },
              "framework": "...",
              "labels": "...",
              "machineType": "...",
              "manualScaling": {
                "nodes": "..."
              },
              "name": "...",
              "packageUris": "...",
              "predictionClass": "...",
              "pythonVersion": "...",
              "requestLoggingConfig": {
                "bigqueryTableName": "...",
                "samplingPercentage": "..."
              },
              "routes": {
                "health": "...",
                "predict": "..."
              },
              "runtimeVersion": "...",
              "serviceAccount": "..."
            }
          },
          "result": "createResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
