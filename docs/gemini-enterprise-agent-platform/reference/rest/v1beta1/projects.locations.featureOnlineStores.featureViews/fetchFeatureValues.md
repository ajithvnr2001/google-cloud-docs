---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews/fetchFeatureValues/
title: Method: featureViews.fetchFeatureValues \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:56:29.826029+00:00
---

# Method: featureViews.fetchFeatureValues  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews/fetchFeatureValues/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: featureViews.fetchFeatureValues Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.featureOnlineStores.featureViews.fetchFeatureValues

Fetch feature values under a FeatureView.

### Endpoint

post  `https://{service-endpoint}/v1beta1/{featureView}:fetchFeatureValues`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`featureView` `string` Required. FeatureView resource format `projects/{project}/locations/{location}/featureOnlineStores/{featureOnlineStore}/featureViews/{featureView}`

### Request body

The request body contains data with the following structure: | Fields  
  
`dataKey` `object (`[FeatureViewDataKey](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeatureViewDataKey)`)` Optional. The request key to fetch feature values for. | `dataFormat` `enum (`[FeatureViewDataFormat](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeatureViewDataFormat)`)` Optional. Response data format. If not set, `[FeatureViewDataFormat.KEY_VALUE](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FeatureViewDataFormat#ENUM_VALUES.KEY_VALUE)` will be used. | `format  
**(deprecated)**` `enum (`[Format](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews/fetchFeatureValues#Format)`)` Specify response data format. If not set, keyvalue format will be used. Deprecated. Use `[FetchFeatureValuesRequest.data_format](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews/fetchFeatureValues#body.request_body.FIELDS.data_format)`. | `entity_id` `Union type`  
  
Entity ID to fetch feature values for. Deprecated. Use `[FetchFeatureValuesRequest.data_key](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.featureOnlineStores.featureViews/fetchFeatureValues#body.request_body.FIELDS.data_key)`. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`id  
**(deprecated)**` `string` Simple id. The whole string will be used as is to identify Entity to fetch feature values for. End of mutually exclusive fields.

### Response body

If successful, the response body contains an instance of `[FetchFeatureValuesResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/FetchFeatureValuesResponse)`.

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `featureView` resource:

  * `aiplatform.featureViews.fetchFeatureValues`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## Format

This item is deprecated!Format of the response data. | Enums  
---  
`FORMAT_UNSPECIFIED` | Not set. Will be treated as the keyvalue format.  
`KEY_VALUE` | Return response data in key-value format.  
`PROTO_STRUCT` | Return response data in proto Struct format.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
