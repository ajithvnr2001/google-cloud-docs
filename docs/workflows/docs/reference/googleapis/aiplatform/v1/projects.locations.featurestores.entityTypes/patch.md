---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.featurestores.entityTypes/patch/
title: Method: googleapis.aiplatform.v1.projects.locations.featurestores.entityTypes.patch \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:22:37.077114+00:00
---

# Method: googleapis.aiplatform.v1.projects.locations.featurestores.entityTypes.patch  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.featurestores.entityTypes/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.aiplatform.v1.projects.locations.featurestores.entityTypes.patch Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Updates the parameters of a single EntityType.

## Arguments

Parameters  
---  
`name` |  `string` Required. Immutable. Name of the EntityType. Format: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}` The last part entity_type is assigned by the client. The entity_type can be up to 64 characters long and can consist only of ASCII Latin letters A-Z and a-z and underscore(_), and ASCII digits 0-9 starting with a letter. The value will be unique given a featurestore.  
`updateMask` |  `string ([FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask) format)` Field mask is used to specify the fields to be overwritten in the EntityType resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. If the user does not provide a mask then only the non-empty fields present in the request will be overwritten. Set the update_mask to `*` to override all fields. Updatable fields: * `description` * `labels` * `monitoring_config.snapshot_analysis.disabled` * `monitoring_config.snapshot_analysis.monitoring_interval_days` * `monitoring_config.snapshot_analysis.staleness_days` * `monitoring_config.import_features_analysis.state` * `monitoring_config.import_features_analysis.anomaly_detection_baseline` * `monitoring_config.numerical_threshold_config.value` * `monitoring_config.categorical_threshold_config.value` * `offline_storage_ttl_days`  
`region` |  `string` Required. Region of the HTTP endpoint. For example, if region is set to `us-central1`, the endpoint https://us-central1-integrations.googleapis.com will be used. See [service endpoints](https://cloud.google.com/vertex-ai/docs/reference/rest#rest_endpoints).  
`body` |  `object ([GoogleCloudAiplatformV1EntityType](https://cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/Overview#GoogleCloudAiplatformV1EntityType))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`GoogleCloudAiplatformV1EntityType`](https://cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/Overview#GoogleCloudAiplatformV1EntityType).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores.entityTypes/patch).

### YAML
    
    
    - patch:
        call: googleapis.aiplatform.v1.projects.locations.featurestores.entityTypes.patch
        args:
            name: ...
            updateMask: ...
            region: ...
            body:
                description: ...
                etag: ...
                labels: ...
                monitoringConfig:
                    categoricalThresholdConfig:
                        value: ...
                    importFeaturesAnalysis:
                        anomalyDetectionBaseline: ...
                        state: ...
                    numericalThresholdConfig: ...
                    snapshotAnalysis:
                        disabled: ...
                        monitoringIntervalDays: ...
                        stalenessDays: ...
                name: ...
                offlineStorageTtlDays: ...
        result: patchResult

### JSON
    
    
    [
      {
        "patch": {
          "call": "googleapis.aiplatform.v1.projects.locations.featurestores.entityTypes.patch",
          "args": {
            "name": "...",
            "updateMask": "...",
            "region": "...",
            "body": {
              "description": "...",
              "etag": "...",
              "labels": "...",
              "monitoringConfig": {
                "categoricalThresholdConfig": {
                  "value": "..."
                },
                "importFeaturesAnalysis": {
                  "anomalyDetectionBaseline": "...",
                  "state": "..."
                },
                "numericalThresholdConfig": "...",
                "snapshotAnalysis": {
                  "disabled": "...",
                  "monitoringIntervalDays": "...",
                  "stalenessDays": "..."
                }
              },
              "name": "...",
              "offlineStorageTtlDays": "..."
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
