---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/list/
title: Method: endpoints.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:58:03.792965+00:00
---

# Method: endpoints.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: endpoints.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.endpoints.list

Lists endpoints in a Location.

### Endpoint

get  `https://{service-endpoint}/v1/{parent}/endpoints`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the Location from which to list the endpoints. Format: `projects/{project}/locations/{location}`

### Query parameters

| `filter` `string` Optional. An expression for filtering the results of the request. For field names both snake_case and camelCase are supported.

  * `endpoint` supports `=` and `!=`. `endpoint` represents the Endpoint id, i.e. the last segment of the Endpoint's `[resource name](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints#Endpoint.FIELDS.name)`.
  * `displayName` supports `=` and `!=`.
  * `labels` supports general map functions that is: 
    * `labels.key=value` \- key:value equality
    * `labels.key:*` or `labels:key` \- key existence
    * A key including a space must be quoted. `labels."a key"`.
  * `base_model_name` only supports `=`.

Some examples:

  * `endpoint=1`
  * `displayName="myDisplayName"`
  * `labels.myKey="myValue"`
  * `baseModelName="text-bison"`

| `pageSize` `integer` Optional. The standard list page size. | `pageToken` `string` Optional. The standard list page token. Typically obtained via `[ListEndpointsResponse.next_page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/list#body.ListEndpointsResponse.FIELDS.next_page_token)` of the previous `[EndpointService.ListEndpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/list#google.cloud.aiplatform.v1.EndpointService.ListEndpoints)` call. | `readMask` `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. Mask specifying which fields to read.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`. | `orderBy` `string` A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields:

  * `displayName`
  * `createTime`
  * `updateTime`

Example: `displayName, createTime desc`. | `gdcZone` `string` Optional. Configures the Google Distributed Cloud (GDC) environment for online prediction. Only set this field when the Endpoint is to be deployed in a GDC environment.

### Request body

The request body must be empty.

### Response body

Response message for `[EndpointService.ListEndpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/list#google.cloud.aiplatform.v1.EndpointService.ListEndpoints)`. If successful, the response body contains data with the following structure: | Fields  
  
`endpoints[]` `object (`[Endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints#Endpoint)`)` List of endpoints in the requested page. | `nextPageToken` `string` A token to retrieve the next page of results. Pass to `[ListEndpointsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/list#body.QUERY_PARAMETERS.page_token)` to obtain that page. | JSON representation  
---  
      
    
    {
      "endpoints": [
        {
          object ([Endpoint](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints#Endpoint))
        }
      ],
      "nextPageToken": string
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.endpoints.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
