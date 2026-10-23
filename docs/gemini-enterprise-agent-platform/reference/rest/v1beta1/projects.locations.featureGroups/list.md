---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups/list/
title: Method: featureGroups.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:58:40.662791+00:00
---

# Method: featureGroups.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: featureGroups.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.featureGroups.list

Lists FeatureGroups in a given project and location.

### Endpoint

get  `https://{service-endpoint}/v1beta1/{parent}/featureGroups`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the Location to list FeatureGroups. Format: `projects/{project}/locations/{location}`

### Query parameters

| `filter` `string` Lists the FeatureGroups that match the filter expression. The following fields are supported:

  * `createTime`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format.
  * `updateTime`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format.
  * `labels`: Supports key-value equality and key presence.

Examples:

  * `createTime > "2020-01-01" OR updateTime > "2020-01-01"` FeatureGroups created or updated after 2020-01-01.
  * `labels.env = "prod"` FeatureGroups with label "env" set to "prod".

| `pageSize` `integer` The maximum number of FeatureGroups to return. The service may return fewer than this value. If unspecified, at most 100 FeatureGroups will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100. | `pageToken` `string` A page token, received from a previous `[FeatureRegistryService.ListFeatureGroups](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups/list#google.cloud.aiplatform.v1beta1.FeatureRegistryService.ListFeatureGroups)` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `[FeatureRegistryService.ListFeatureGroups](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups/list#google.cloud.aiplatform.v1beta1.FeatureRegistryService.ListFeatureGroups)` must match the call that provided the page token. | `orderBy` `string` A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported Fields:

  * `createTime`
  * `updateTime`



### Request body

The request body must be empty.

### Response body

Response message for `[FeatureRegistryService.ListFeatureGroups](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups/list#google.cloud.aiplatform.v1beta1.FeatureRegistryService.ListFeatureGroups)`. If successful, the response body contains data with the following structure: | Fields  
  
`featureGroups[]` `object (`[FeatureGroup](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups#FeatureGroup)`)` The FeatureGroups matching the request. | `nextPageToken` `string` A token, which can be sent as `[ListFeatureGroupsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups/list#body.QUERY_PARAMETERS.page_token)` to retrieve the next page. If this field is omitted, there are no subsequent pages. | JSON representation  
---  
      
    
    {
      "featureGroups": [
        {
          object ([FeatureGroup](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups#FeatureGroup))
        }
      ],
      "nextPageToken": string
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.featureGroups.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
