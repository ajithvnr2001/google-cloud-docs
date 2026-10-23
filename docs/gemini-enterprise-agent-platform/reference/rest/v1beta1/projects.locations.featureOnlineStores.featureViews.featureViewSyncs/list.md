---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews.featureViewSyncs/list/
title: Method: featureViewSyncs.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:58:40.316260+00:00
---

# Method: featureViewSyncs.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews.featureViewSyncs/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: featureViewSyncs.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.featureOnlineStores.featureViews.featureViewSyncs.list

Lists FeatureViewSyncs in a given FeatureView.

### Endpoint

get  `https://{service-endpoint}/v1beta1/{parent}/featureViewSyncs`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the FeatureView to list FeatureViewSyncs. Format: `projects/{project}/locations/{location}/featureOnlineStores/{featureOnlineStore}/featureViews/{featureView}`

### Query parameters

| `filter` `string` Lists the FeatureViewSyncs that match the filter expression. The following filters are supported:

  * `createTime`: Supports `=`, `!=`, `<`, `>`, `>=`, and `<=` comparisons. Values must be in RFC 3339 format.

Examples:

  * `createTime > \"2020-01-31T15:30:00.000000Z\"` \--> FeatureViewSyncs created after 2020-01-31T15:30:00.000000Z.

| `pageSize` `integer` The maximum number of FeatureViewSyncs to return. The service may return fewer than this value. If unspecified, at most 1000 FeatureViewSyncs will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000. | `pageToken` `string` A page token, received from a previous `[FeatureOnlineStoreAdminService.ListFeatureViewSyncs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews.featureViewSyncs/list#google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService.ListFeatureViewSyncs)` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `[FeatureOnlineStoreAdminService.ListFeatureViewSyncs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews.featureViewSyncs/list#google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService.ListFeatureViewSyncs)` must match the call that provided the page token. | `orderBy` `string` A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending.Supported fields:

  * `createTime`



### Request body

The request body must be empty.

### Response body

Response message for `[FeatureOnlineStoreAdminService.ListFeatureViewSyncs](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews.featureViewSyncs/list#google.cloud.aiplatform.v1beta1.FeatureOnlineStoreAdminService.ListFeatureViewSyncs)`. If successful, the response body contains data with the following structure: | Fields  
  
`featureViewSyncs[]` `object (`[FeatureViewSync](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews.featureViewSyncs#FeatureViewSync)`)` The FeatureViewSyncs matching the request. | `nextPageToken` `string` A token, which can be sent as `[ListFeatureViewSyncsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews.featureViewSyncs/list#body.QUERY_PARAMETERS.page_token)` to retrieve the next page. If this field is omitted, there are no subsequent pages. | JSON representation  
---  
      
    
    {
      "featureViewSyncs": [
        {
          object ([FeatureViewSync](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews.featureViewSyncs#FeatureViewSync))
        }
      ],
      "nextPageToken": string
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.featureViewSyncs.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
