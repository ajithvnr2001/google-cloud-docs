---
url: https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs/patch/
title: FeatureConfigs: patch \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:51:26.258612+00:00
---

# FeatureConfigs: patch  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  FeatureConfigs: patch Stay organized with collections  Save and categorize content based on your preferences. 

Updates the specified `FeatureConfig` resource. This method supports [patch semantics](https://docs.cloud.google.com/storage/docs/json_api#patch).

## Required permissions

To use this method, the authenticated user must have the `storage.featureConfigs.update` IAM permission.

## Request

### HTTP request
    
    
    PATCH https://storage.googleapis.com/v2/projects/project/locations/global/featureConfigs/featureConfigId

### Parameters

Parameter name | Value | Description  
---|---|---  
**Path parameters**  
`project` | `string` | The project ID or number to which the feature configuration belongs.  
`featureConfigId` | `string` | The ID of the feature configuration to update.  
**Query parameters**  
`updateMask` | `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` | _Optional._ Comma-separated list of fields to update. If omitted, all populated fields in the request body are updated. Use `*` to perform a full replacement.  
`requestId` | `string` | _Optional._ A UUID for idempotent requests.  
  
### Request body

In the request body, supply a [FeatureConfig resource](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs#resource) with the fields you want to update.

## Response

If successful, this method returns a [long-running operation](https://docs.cloud.google.com/storage/docs/using-long-running-operations) in the response body which completes with an instance of [FeatureConfig](https://docs.cloud.google.com/storage/docs/json_api/v1/featureConfigs#resource).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
