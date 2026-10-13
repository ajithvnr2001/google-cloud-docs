---
url: https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/organizations.locations.insightTypes.insights/markAccepted/
title: Method: organizations.locations.insightTypes.insights.markAccepted \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:10:15.588000+00:00
---

# Method: organizations.locations.insightTypes.insights.markAccepted  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/organizations.locations.insightTypes.insights/markAccepted/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Reference ](https://docs.cloud.google.com/recommender/docs/apis)



Send feedback 

#  Method: organizations.locations.insightTypes.insights.markAccepted Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Marks the Insight State as Accepted. Users can use this method to indicate to the Recommender API that they have applied some action based on the insight. This stops the insight content from being updated.

insights.markAccepted can be applied to insights in ACTIVE state. Requires the recommender.*.update IAM permission for the specified insight.

### HTTP request

`POST https://recommender.googleapis.com/v1beta1/{name=organizations/*/locations/*/insightTypes/*/insights/*}:markAccepted`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the insight.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "stateMetadata": {
        string: string,
        ...
      },
      "etag": string
    }  
  
Fields  
---  
`stateMetadata` |  `map (key: string, value: string)` Optional. State properties user wish to include with this state. Full replace of the current stateMetadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`etag` |  `string` Required. Fingerprint of the Insight. Provides optimistic locking.  
  
### Response body

If successful, the response body contains an instance of `[Insight](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/billingAccounts.locations.insightTypes.insights#Insight)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires **one of** the following [IAM](https://cloud.google.com/iam/docs) permissions on the `name` resource, depending on the resource type:

  * `recommender.commitmentUtilizationInsights.update`
  * `recommender.computeAddressIdleResourceInsights.update`
  * `recommender.computeDiskIdleResourceInsights.update`
  * `recommender.computeFirewallInsights.update`
  * `recommender.computeImageIdleResourceInsights.update`
  * `recommender.iamPolicyInsights.update`
  * `recommender.iamServiceAccountInsights.update`
  * `recommender.resourcemanagerProjectUtilizationInsights.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
