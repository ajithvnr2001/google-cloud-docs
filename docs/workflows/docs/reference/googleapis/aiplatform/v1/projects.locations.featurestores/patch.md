---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.featurestores/patch/
title: Method: googleapis.aiplatform.v1.projects.locations.featurestores.patch \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:22:28.249503+00:00
---

# Method: googleapis.aiplatform.v1.projects.locations.featurestores.patch  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.featurestores/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.aiplatform.v1.projects.locations.featurestores.patch Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Updates the parameters of a single Featurestore.

This method waits—the workflow execution is paused—until the operation is complete, fails, or times out. The default timeout value is `1800` seconds (30 minutes) and can be changed to a maximum value of `31536000` seconds (one year) for long-running operations using the `connector_params` field. See the [Connectors reference](https://docs.cloud.google.com/workflows/docs/reference/googleapis).

The connector uses polling to monitor the long-running operation, which might generate additional billable steps. For more information about retries and long-running operations, refer to [Understand connectors](https://docs.cloud.google.com/workflows/docs/connectors).

The polling policy for the long-running operation can be configured. To set the connector-specific parameters (`connector_params`), refer to [Invoke a connector call](https://docs.cloud.google.com/workflows/docs/reference/googleapis#invoke_a_connector_call).

## Arguments

Parameters  
---  
`name` |  `string` Required. Output only. Name of the Featurestore. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}`  
`updateMask` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` Field mask is used to specify the fields to be overwritten in the Featurestore resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields: * `labels` * `online_serving_config.fixed_node_count` * `online_serving_config.scaling` * `online_storage_ttl_days`  
`region` |  `string` Required. Region of the HTTP endpoint. For example, if region is set to `us-central1`, the endpoint https://us-central1-integrations.googleapis.com will be used. See [service endpoints](https://cloud.google.com/vertex-ai/docs/reference/rest#rest_endpoints).  
`body` |  `object ([GoogleCloudAiplatformV1Featurestore](https://cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/Overview#GoogleCloudAiplatformV1Featurestore))` Required.  
  
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

If successful, the response contains an instance of [`GoogleLongrunningOperation`](https://cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/Overview#GoogleLongrunningOperation).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores/patch).

### YAML
    
    
    - patch:
        call: googleapis.aiplatform.v1.projects.locations.featurestores.patch
        args:
            name: ...
            updateMask: ...
            region: ...
            body:
                encryptionSpec:
                    kmsKeyName: ...
                etag: ...
                labels: ...
                onlineServingConfig:
                    fixedNodeCount: ...
                    scaling:
                        cpuUtilizationTarget: ...
                        maxNodeCount: ...
                        minNodeCount: ...
                onlineStorageTtlDays: ...
        result: patchResult

### JSON
    
    
    [
      {
        "patch": {
          "call": "googleapis.aiplatform.v1.projects.locations.featurestores.patch",
          "args": {
            "name": "...",
            "updateMask": "...",
            "region": "...",
            "body": {
              "encryptionSpec": {
                "kmsKeyName": "..."
              },
              "etag": "...",
              "labels": "...",
              "onlineServingConfig": {
                "fixedNodeCount": "...",
                "scaling": {
                  "cpuUtilizationTarget": "...",
                  "maxNodeCount": "...",
                  "minNodeCount": "..."
                }
              },
              "onlineStorageTtlDays": "..."
            }
          },
          "result": "patchResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
