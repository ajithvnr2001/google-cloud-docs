---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.specialistPools/list/
title: Method: specialistPools.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:57:45.275288+00:00
---

# Method: specialistPools.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.specialistPools/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: specialistPools.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.specialistPools.list

Lists SpecialistPools in a Location.

### Endpoint

get  `https://{service-endpoint}/v1/{parent}/specialistPools`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The name of the SpecialistPool's parent resource. Format: `projects/{project}/locations/{location}`

### Query parameters

| `pageSize` `integer` The standard list page size. | `pageToken` `string` The standard list page token. Typically obtained by `[ListSpecialistPoolsResponse.next_page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.specialistPools/list#body.ListSpecialistPoolsResponse.FIELDS.next_page_token)` of the previous `[SpecialistPoolService.ListSpecialistPools](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.specialistPools/list#google.cloud.aiplatform.v1.SpecialistPoolService.ListSpecialistPools)` call. Return first page if empty. | `readMask` `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Mask specifying which fields to read. FieldMask represents a set ofThis is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.

### Request body

The request body must be empty.

### Response body

Response message for `[SpecialistPoolService.ListSpecialistPools](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.specialistPools/list#google.cloud.aiplatform.v1.SpecialistPoolService.ListSpecialistPools)`. If successful, the response body contains data with the following structure: | Fields  
  
`specialistPools[]` `object (`[SpecialistPool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.specialistPools#SpecialistPool)`)` A list of SpecialistPools that matches the specified filter in the request. | `nextPageToken` `string` The standard List next-page token. | JSON representation  
---  
      
    
    {
      "specialistPools": [
        {
          object ([SpecialistPool](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.specialistPools#SpecialistPool))
        }
      ],
      "nextPageToken": string
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.specialistPools.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
