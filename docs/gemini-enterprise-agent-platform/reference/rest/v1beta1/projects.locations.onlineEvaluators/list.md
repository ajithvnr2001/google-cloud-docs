---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.onlineEvaluators/list/
title: Method: onlineEvaluators.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:58:22.522696+00:00
---

# Method: onlineEvaluators.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.onlineEvaluators/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: onlineEvaluators.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.onlineEvaluators.list

Lists the OnlineEvaluators for the given project and location.

### Endpoint

get  `https://{service-endpoint}/v1beta1/{parent}/onlineEvaluators`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The parent resource of the OnlineEvaluators to list. Format: projects/{project}/locations/{location}.

### Query parameters

| `pageSize` `integer` Optional. The maximum number of OnlineEvaluators to return. The service may return fewer than this value. If unspecified, at most 100 OnlineEvaluators will be returned. The maximum value is 100; values above 100 will be coerced to 100. Based on aip.dev/158. | `pageToken` `string` Optional. A token identifying a page of results the server should return. Based on aip.dev/158. | `filter` `string` Optional. Standard list filter. Supported fields: * `createTime` * `updateTime` * `agentResource` Example: `createTime>"2026-01-01T00:00:00-04:00"` where the timestamp is in RFC 3339 format) Based on aip.dev/160. | `orderBy` `string` Optional. A comma-separated list of fields to order by. The default sorting order is ascending. Use "desc" after a field name for descending. Supported fields: * `createTime` * `updateTime`Example: `createTime desc`. Based on aip.dev/132.

### Request body

The request body must be empty.

### Response body

Response message for onlineEvaluators.list. If successful, the response body contains data with the following structure: | Fields  
  
`onlineEvaluators[]` `object (`[OnlineEvaluator](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.onlineEvaluators#OnlineEvaluator)`)` A list of OnlineEvaluators matching the request. | `nextPageToken` `string` A token to retrieve the next page. Absence of this field indicates there are no subsequent pages. | JSON representation  
---  
      
    
    {
      "onlineEvaluators": [
        {
          object ([OnlineEvaluator](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.onlineEvaluators#OnlineEvaluator))
        }
      ],
      "nextPageToken": string
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.onlineEvaluators.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
