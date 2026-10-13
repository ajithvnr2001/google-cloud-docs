---
url: https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/organizations.locations.recommenders.recommendations/markDismissed/
title: Method: organizations.locations.recommenders.recommendations.markDismissed \u00a0|\u00a0 Recommender \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:48:36.447501+00:00
---

# Method: organizations.locations.recommenders.recommendations.markDismissed  |  Recommender  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/organizations.locations.recommenders.recommendations/markDismissed/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Recommender ](https://docs.cloud.google.com/recommender/docs)
  * [ Reference ](https://docs.cloud.google.com/recommender/docs/apis)



Send feedback 

#  Method: organizations.locations.recommenders.recommendations.markDismissed Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions



Mark the Recommendation State as Dismissed. Users can use this method to indicate to the Recommender API that an ACTIVE recommendation has to be marked back as DISMISSED.

recommendations.markDismissed can be applied to recommendations in ACTIVE state.

Requires the recommender.*.update IAM permission for the specified recommender.

### HTTP request

`POST https://recommender.googleapis.com/v1beta1/{name=organizations/*/locations/*/recommenders/*/recommendations/*}:markDismissed`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Name of the recommendation.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "etag": string
    }  
  
Fields  
---  
`etag` |  `string` Fingerprint of the Recommendation. Provides optimistic locking.  
  
### Response body

If successful, the response body contains an instance of `[Recommendation](https://docs.cloud.google.com/recommender/docs/reference/rest/v1beta1/billingAccounts.locations.recommenders.recommendations#Recommendation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires **one of** the following [IAM](https://cloud.google.com/iam/docs) permissions on the `name` resource, depending on the resource type:

  * `recommender.usageCommitmentRecommendations.update`
  * `recommender.computeAddressIdleResourceRecommendations.update`
  * `recommender.computeDiskIdleResourceRecommendations.update`
  * `recommender.computeImageIdleResourceRecommendations.update`
  * `recommender.computeInstanceGroupManagerMachineTypeRecommendations.update`
  * `recommender.computeInstanceIdleResourceRecommendations.update`
  * `recommender.computeInstanceMachineTypeRecommendations.update`
  * `recommender.iamPolicyRecommendations.update`
  * `recommender.resourcemanagerProjectUtilizationRecommendations.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-14 UTC."],[],[]] 
