---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/ml/v1/projects.jobs/create/
title: Method: googleapis.ml.v1.projects.jobs.create \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:09:10.954094+00:00
---

# Method: googleapis.ml.v1.projects.jobs.create  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/ml/v1/projects.jobs/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.ml.v1.projects.jobs.create Stay organized with collections  Save and categorize content based on your preferences. 

Creates a training or a batch prediction job.

This method waits—the workflow execution is paused—until the operation is complete, fails, or times out. The default timeout value is `1800` seconds (30 minutes) and can be changed to a maximum value of `31536000` seconds (one year) for long-running operations using the `connector_params` field. See the [Connectors reference](https://docs.cloud.google.com/workflows/docs/reference/googleapis).

The connector uses polling to monitor the long-running operation, which might generate additional billable steps. For more information about retries and long-running operations, refer to [Understand connectors](https://docs.cloud.google.com/workflows/docs/connectors).

The polling policy for the long-running operation can be configured. To set the connector-specific parameters (`connector_params`), refer to [Invoke a connector call](https://docs.cloud.google.com/workflows/docs/reference/googleapis#invoke_a_connector_call).

## Arguments

Parameters  
---  
`parent` |  `string` Required. The project name.  
`body` |  `object ([GoogleCloudMlV1__Job](https://cloud.google.com/workflows/docs/reference/googleapis/ml/v1/Overview#GoogleCloudMlV1__Job))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
`OperationError` | If the long-running operation finished unsuccessfully.  
`ResponseTypeError` | If the long-running operation returned a response of the wrong type.  
  
## Response

If successful, the response contains an instance of [`GoogleCloudMlV1__Job`](https://cloud.google.com/workflows/docs/reference/googleapis/ml/v1/Overview#GoogleCloudMlV1__Job).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/ai-platform/training/docs/reference/rest/v1/projects.jobs/create).

### YAML
    
    
    - create:
        call: googleapis.ml.v1.projects.jobs.create
        args:
            parent: ...
            body:
                etag: ...
                jobId: ...
                labels: ...
                predictionInput:
                    batchSize: ...
                    dataFormat: ...
                    inputPaths: ...
                    maxWorkerCount: ...
                    modelName: ...
                    outputDataFormat: ...
                    outputPath: ...
                    region: ...
                    runtimeVersion: ...
                    signatureName: ...
                    uri: ...
                    versionName: ...
                predictionOutput:
                    errorCount: ...
                    nodeHours: ...
                    outputPath: ...
                    predictionCount: ...
                trainingInput:
                    args: ...
                    enableWebAccess: ...
                    encryptionConfig:
                        kmsKeyName: ...
                    evaluatorConfig:
                        acceleratorConfig:
                            count: ...
                            type: ...
                        containerArgs: ...
                        containerCommand: ...
                        diskConfig:
                            bootDiskSizeGb: ...
                            bootDiskType: ...
                        imageUri: ...
                        tpuTfVersion: ...
                    evaluatorCount: ...
                    evaluatorType: ...
                    hyperparameters:
                        algorithm: ...
                        enableTrialEarlyStopping: ...
                        goal: ...
                        hyperparameterMetricTag: ...
                        maxFailedTrials: ...
                        maxParallelTrials: ...
                        maxTrials: ...
                        params: ...
                        resumePreviousJobId: ...
                    jobDir: ...
                    masterConfig: ...
                    masterType: ...
                    network: ...
                    packageUris: ...
                    parameterServerConfig: ...
                    parameterServerCount: ...
                    parameterServerType: ...
                    pythonModule: ...
                    pythonVersion: ...
                    region: ...
                    runtimeVersion: ...
                    scaleTier: ...
                    scheduling:
                        maxRunningTime: ...
                        maxWaitTime: ...
                        priority: ...
                    serviceAccount: ...
                    useChiefInTfConfig: ...
                    workerConfig: ...
                    workerCount: ...
                    workerType: ...
                trainingOutput:
                    builtInAlgorithmOutput:
                        framework: ...
                        modelPath: ...
                        pythonVersion: ...
                        runtimeVersion: ...
                    completedTrialCount: ...
                    consumedMLUnits: ...
                    hyperparameterMetricTag: ...
                    isBuiltInAlgorithmJob: ...
                    isHyperparameterTuningJob: ...
                    trials: ...
        result: createResult

### JSON
    
    
    [
      {
        "create": {
          "call": "googleapis.ml.v1.projects.jobs.create",
          "args": {
            "parent": "...",
            "body": {
              "etag": "...",
              "jobId": "...",
              "labels": "...",
              "predictionInput": {
                "batchSize": "...",
                "dataFormat": "...",
                "inputPaths": "...",
                "maxWorkerCount": "...",
                "modelName": "...",
                "outputDataFormat": "...",
                "outputPath": "...",
                "region": "...",
                "runtimeVersion": "...",
                "signatureName": "...",
                "uri": "...",
                "versionName": "..."
              },
              "predictionOutput": {
                "errorCount": "...",
                "nodeHours": "...",
                "outputPath": "...",
                "predictionCount": "..."
              },
              "trainingInput": {
                "args": "...",
                "enableWebAccess": "...",
                "encryptionConfig": {
                  "kmsKeyName": "..."
                },
                "evaluatorConfig": {
                  "acceleratorConfig": {
                    "count": "...",
                    "type": "..."
                  },
                  "containerArgs": "...",
                  "containerCommand": "...",
                  "diskConfig": {
                    "bootDiskSizeGb": "...",
                    "bootDiskType": "..."
                  },
                  "imageUri": "...",
                  "tpuTfVersion": "..."
                },
                "evaluatorCount": "...",
                "evaluatorType": "...",
                "hyperparameters": {
                  "algorithm": "...",
                  "enableTrialEarlyStopping": "...",
                  "goal": "...",
                  "hyperparameterMetricTag": "...",
                  "maxFailedTrials": "...",
                  "maxParallelTrials": "...",
                  "maxTrials": "...",
                  "params": "...",
                  "resumePreviousJobId": "..."
                },
                "jobDir": "...",
                "masterConfig": "...",
                "masterType": "...",
                "network": "...",
                "packageUris": "...",
                "parameterServerConfig": "...",
                "parameterServerCount": "...",
                "parameterServerType": "...",
                "pythonModule": "...",
                "pythonVersion": "...",
                "region": "...",
                "runtimeVersion": "...",
                "scaleTier": "...",
                "scheduling": {
                  "maxRunningTime": "...",
                  "maxWaitTime": "...",
                  "priority": "..."
                },
                "serviceAccount": "...",
                "useChiefInTfConfig": "...",
                "workerConfig": "...",
                "workerCount": "...",
                "workerType": "..."
              },
              "trainingOutput": {
                "builtInAlgorithmOutput": {
                  "framework": "...",
                  "modelPath": "...",
                  "pythonVersion": "...",
                  "runtimeVersion": "..."
                },
                "completedTrialCount": "...",
                "consumedMLUnits": "...",
                "hyperparameterMetricTag": "...",
                "isBuiltInAlgorithmJob": "...",
                "isHyperparameterTuningJob": "...",
                "trials": "..."
              }
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
