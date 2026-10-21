---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models/list/
title: Method: models.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:10:32.915880+00:00
---

# Method: models.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: models.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : publishers.models.list

Lists publisher models in Model Garden.

### Endpoint

get  `https://{service-endpoint}/v1beta1/{parent}/models`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The name of the Publisher from which to list the PublisherModels. Format: `publishers/{publisher}`

### Query parameters

| `filter` `string` Optional. The standard list filter. | `pageSize` `integer` Optional. The standard list page size. | `pageToken` `string` Optional. The standard list page token. Typically obtained via `[ListPublisherModelsResponse.next_page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models/list#body.ListPublisherModelsResponse.FIELDS.next_page_token)` of the previous `[ModelGardenService.ListPublisherModels](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models/list#google.cloud.aiplatform.v1beta1.ModelGardenService.ListPublisherModels)` call. | `view` `enum (`[PublisherModelView](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/PublisherModelView)`)` Optional. PublisherModel view specifying which fields to read. | `orderBy` `string` Optional. A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. | `languageCode` `string` Optional. The IETF BCP-47 language code representing the language in which the publisher models' text information should be written in. If not set, by default English (en). | `listAllVersions` `boolean` Optional. List all publisher model versions if the flag is set to true.

### Request body

The request body must be empty.

### Response body

Response message for `[ModelGardenService.ListPublisherModels](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models/list#google.cloud.aiplatform.v1beta1.ModelGardenService.ListPublisherModels)`. If successful, the response body contains data with the following structure: | Fields  
  
`publisherModels[]` `object (`[PublisherModel](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#PublisherModel)`)` List of PublisherModels in the requested page. | `nextPageToken` `string` A token to retrieve next page of results. Pass to [models.list.page_token][] to obtain that page. | JSON representation  
---  
      
    
    {
      "publisherModels": [
        {
          object ([PublisherModel](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/publishers.models#PublisherModel))
        }
      ],
      "nextPageToken": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
