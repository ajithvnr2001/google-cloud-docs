---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores/searchFeatures/
title: Method: featurestores.searchFeatures \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:20:39.179864+00:00
---

# Method: featurestores.searchFeatures  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores/searchFeatures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: featurestores.searchFeatures Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.featurestores.searchFeatures

Searches Features matching a query in a given project.

### Endpoint

get  `https://{service-endpoint}/v1/{location}/featurestores:searchFeatures`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`location` `string` Required. The resource name of the Location to search Features. Format: `projects/{project}/locations/{location}`

### Query parameters

| `query` `string` Query string that is a conjunction of field-restricted queries and/or field-restricted filters. Field-restricted queries and filters can be combined using `AND` to form a conjunction.A field query is in the form FIELD:QUERY. This implicitly checks if QUERY exists as a substring within feature's FIELD. The QUERY and the FIELD are converted to a sequence of words (i.e. tokens) for comparison. This is done by:

  * Removing leading/trailing whitespace and tokenizing the search value. Characters that are not one of alphanumeric `[a-zA-Z0-9]`, underscore `_`, or asterisk `*` are treated as delimiters for tokens. `*` is treated as a wildcard that matches characters within a token.
  * Ignoring case.
  * Prepending an asterisk to the first and appending an asterisk to the last token in QUERY.

A QUERY must be either a singular token or a phrase. A phrase is one or multiple words enclosed in double quotation marks ("). With phrases, the order of the words is important. Words in the phrase must be matching in order and consecutively.Supported FIELDs for field-restricted queries:

  * `featureId`
  * `description`
  * `entityTypeId`

Examples:

  * `featureId: foo` \--> Matches a feature with id containing the substring `foo` (eg. `foo`, `foofeature`, `barfoo`).
  * `featureId: foo*feature` \--> Matches a feature with id containing the substring `foo*feature` (eg. `foobarfeature`).
  * `featureId: foo AND description: bar` \--> Matches a feature with id containing the substring `foo` and description containing the substring `bar`.

Besides field queries, the following exact-match filters are supported. The exact-match filters do not support wildcards. Unlike field-restricted queries, exact-match filters are case-sensitive.

  * `featureId`: Supports = comparisons.
  * `description`: Supports = comparisons. Multi-token filters should be enclosed in quotes.
  * `entityTypeId`: Supports = comparisons.
  * `valueType`: Supports = and != comparisons.
  * `labels`: Supports key-value equality as well as key presence.
  * `featurestoreId`: Supports = comparisons.

Examples:

  * `description = "foo bar"` \--> Any feature with description exactly equal to `foo bar`
  * `valueType = DOUBLE` \--> Features whose type is DOUBLE.
  * `labels.active = yes AND labels.env = prod` \--> Features having both (active: yes) and (env: prod) labels.
  * `labels.env: *` \--> Any feature which has a label with `env` as the key.

| `pageSize` `integer` The maximum number of Features to return. The service may return fewer than this value. If unspecified, at most 100 Features will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100. | `pageToken` `string` A page token, received from a previous `[FeaturestoreService.SearchFeatures](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores/searchFeatures#google.cloud.aiplatform.v1.FeaturestoreService.SearchFeatures)` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `[FeaturestoreService.SearchFeatures](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores/searchFeatures#google.cloud.aiplatform.v1.FeaturestoreService.SearchFeatures)`, except `pageSize`, must match the call that provided the page token.

### Request body

The request body must be empty.

### Response body

Response message for `[FeaturestoreService.SearchFeatures](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores/searchFeatures#google.cloud.aiplatform.v1.FeaturestoreService.SearchFeatures)`. If successful, the response body contains data with the following structure: | Fields  
  
`features[]` `object (`[Feature](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureGroups.features#Feature)`)` The Features matching the request.Fields returned:

  * `name`
  * `description`
  * `labels`
  * `createTime`
  * `updateTime`

| `nextPageToken` `string` A token, which can be sent as `[SearchFeaturesRequest.page_token](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores/searchFeatures#body.QUERY_PARAMETERS.page_token)` to retrieve the next page. If this field is omitted, there are no subsequent pages. | JSON representation  
---  
      
    
    {
      "features": [
        {
          object ([Feature](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureGroups.features#Feature))
        }
      ],
      "nextPageToken": string
    }  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
