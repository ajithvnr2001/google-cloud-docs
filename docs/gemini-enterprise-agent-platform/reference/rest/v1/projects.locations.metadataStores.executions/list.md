---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.executions/list/
title: Method: executions.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:00:12.355565+00:00
---

# Method: executions.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.executions/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: executions.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.metadataStores.executions.list

Lists Executions in the MetadataStore.

### Endpoint

get  `https://{service-endpoint}/v1/{parent}/executions`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The MetadataStore whose Executions should be listed. Format: `projects/{project}/locations/{location}/metadataStores/{metadatastore}`

### Query parameters

| `pageSize` `integer` The maximum number of Executions to return. The service may return fewer. Must be in range 1-100, inclusive. Defaults to 100. | `pageToken` `string` A page token, received from a previous `[MetadataService.ListExecutions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.executions/list#google.cloud.aiplatform.v1.MetadataService.ListExecutions)` call. Provide this to retrieve the subsequent page.When paginating, all other provided parameters must match the call that provided the page token. (Otherwise the request will fail with an INVALID_ARGUMENT error.) | `filter` `string` Filter specifying the boolean condition for the Executions to satisfy in order to be part of the result set. The syntax to define filter query is based on <https://google.aip.dev/160>. Following are the supported set of filters:

  * **attribute filtering** : For example: `display_name = "test"`. Supported fields include: `name`, `display_name`, `state`, `schema_title`, `create_time`, and `update_time`. time fields, such as `create_time` and `update_time`, require values specified in RFC-3339 format. For example: `create_time = "2020-11-19T11:30:00-04:00"`.
  * **metadata field** : To filter on metadata fields use traversal operation as follows: `metadata.<fieldName>.<typeValue>` For example: `metadata.field_1.number_value = 10.0` In case the field name contains special characters (such as colon), one can embed it inside double quote. For example: `metadata."field:1".number_value = 10.0`
  * **Context based filtering** : To filter Executions based on the contexts to which they belong use the function operator with the full resource name: `in_context(<context-name>)`. For example: `in_context("projects/<projectNumber>/locations/<location>/metadataStores/<metadatastore_name>/contexts/<context-id>")`

Each of the above supported filters can be combined together using logical operators (`AND` & `OR`). Maximum nested expression depth allowed is 5.For example: `display_name = "test" AND metadata.field1.bool_value = true`. | `orderBy` `string` How the list of messages is ordered. Specify the values to order by and an ordering operation. The default sorting order is ascending. To specify descending order for a field, users append a " desc" suffix; for example: "foo desc, bar". Subfields are specified with a `.` character, such as foo.bar. see <https://google.aip.dev/132#ordering> for more details.

### Request body

The request body must be empty.

### Response body

Response message for `[MetadataService.ListExecutions](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.executions/list#google.cloud.aiplatform.v1.MetadataService.ListExecutions)`. If successful, the response body contains data with the following structure: | Fields  
  
`executions[]` `object (`[Execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.executions#Execution)`)` The Executions retrieved from the MetadataStore. | `nextPageToken` `string` A token, which can be sent as `[ListExecutionsRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.executions/list#body.QUERY_PARAMETERS.page_token)` to retrieve the next page. If this field is not populated, there are no subsequent pages. | JSON representation  
---  
      
    
    {
      "executions": [
        {
          object ([Execution](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.metadataStores.executions#Execution))
        }
      ],
      "nextPageToken": string
    }  
  
### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `aiplatform.executions.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
