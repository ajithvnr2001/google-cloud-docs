---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.featureMonitors/list/
title: Method: featureMonitors.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:31:07.007531+00:00
---

# Method: featureMonitors.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.featureMonitors/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: featureMonitors.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.featureGroups.featureMonitors.list

Lists FeatureGroups in a given project and location.

### Endpoint

get  `https://{service-endpoint}/v1beta1/{parent}/featureMonitors`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the FeatureGroup to list FeatureMonitors. Format: `projects/{project}/locations/{location}/featureGroups/{featureGroup}`

### Query parameters

| `filter` `string` Optional. Lists the FeatureMonitors that match the filter expression. The following fields are supported:

  * `createTime`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format.
  * `updateTime`: Supports `=`, `!=`, `<`, `>`, `<=`, and `>=` comparisons. Values must be in RFC 3339 format.
  * `labels`: Supports key-value equality and key presence.

Examples:

  * `createTime > "2020-01-01" OR updateTime > "2020-01-01"` FeatureMonitors created or updated after 2020-01-01.
  * `labels.env = "prod"` FeatureGroups with label "env" set to "prod".

| `pageSize` `integer` Optional. The maximum number of FeatureGroups to return. The service may return fewer than this value. If unspecified, at most 100 FeatureMonitors will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100. | `pageToken` `string` Optional. A page token, received from a previous `[FeatureRegistryService.ListFeatureMonitors](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.featureMonitors/list#google.cloud.aiplatform.v1beta1.FeatureRegistryService.ListFeatureMonitors)` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `[FeatureRegistryService.ListFeatureMonitors](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.featureMonitors/list#google.cloud.aiplatform.v1beta1.FeatureRegistryService.ListFeatureMonitors)` must match the call that provided the page token. | `orderBy` `string` Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported Fields:

  * `createTime`
  * `updateTime`



### Request body

The request body must be empty.

### Response body

Response message for `[FeatureRegistryService.ListFeatureMonitors](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.featureMonitors/list#google.cloud.aiplatform.v1beta1.FeatureRegistryService.ListFeatureMonitors)`. If successful, the response body contains data with the following structure: | Fields  
  
`featureMonitors[]` `object (`[FeatureMonitor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.featureMonitors#FeatureMonitor)`)` The FeatureMonitors matching the request. | `nextPageToken` `string` A token, which can be sent as `[ListFeatureMonitorsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.featureMonitors/list#body.QUERY_PARAMETERS.page_token)` to retrieve the next page. If this field is omitted, there are no subsequent pages. | JSON representation  
---  
      
    
    {
      "featureMonitors": [
        {
          object ([FeatureMonitor](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureGroups.featureMonitors#FeatureMonitor))
        }
      ],
      "nextPageToken": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
