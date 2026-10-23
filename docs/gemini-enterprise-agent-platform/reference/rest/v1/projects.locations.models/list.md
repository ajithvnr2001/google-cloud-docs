---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/list/
title: Method: models.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:06.808278+00:00
---

# Method: models.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: models.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.models.list

Lists Models in a Location.

### Endpoint

get  `https://{service-endpoint}/v1/{parent}/models`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the Location to list the Models from. Format: `projects/{project}/locations/{location}`

### Query parameters

| `filter` `string` An expression for filtering the results of the request. For field names both snake_case and camelCase are supported.

  * `model` supports = and !=. `model` represents the Model id, i.e. the last segment of the Model's `[resource name](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models#Model.FIELDS.name)`.
  * `displayName` supports = and !=
  * `labels` supports general map functions that is: 
    * `labels.key=value` \- key:value equality
    * `labels.key:* or labels:key - key existence
    * A key including a space must be quoted. `labels."a key"`.
  * `base_model_name` only supports =

Some examples:

  * `model=1234`
  * `displayName="myDisplayName"`
  * `labels.myKey="myValue"`
  * `baseModelName="text-bison"`

| `pageSize` `integer` The standard list page size. | `pageToken` `string` The standard list page token. Typically obtained via `[ListModelsResponse.next_page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/list#body.ListModelsResponse.FIELDS.next_page_token)` of the previous `[ModelService.ListModels](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/list#google.cloud.aiplatform.v1.ModelService.ListModels)` call. | `readMask` `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Mask specifying which fields to read.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`. | `orderBy` `string` A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields:

  * `displayName`
  * `createTime`
  * `updateTime`

Example: `displayName, createTime desc`.

### Request body

The request body must be empty.

### Response body

Response message for `[ModelService.ListModels](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/list#google.cloud.aiplatform.v1.ModelService.ListModels)` If successful, the response body contains data with the following structure: | Fields  
  
`models[]` `object (`[Model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models#Model)`)` List of Models in the requested page. | `nextPageToken` `string` A token to retrieve next page of results. Pass to `[ListModelsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models/list#body.QUERY_PARAMETERS.page_token)` to obtain that page. | JSON representation  
---  
      
    
    {
      "models": [
        {
          object ([Model](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.models#Model))
        }
      ],
      "nextPageToken": string
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.models.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
