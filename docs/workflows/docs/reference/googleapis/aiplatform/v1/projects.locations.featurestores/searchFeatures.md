---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.featurestores/searchFeatures/
title: Method: googleapis.aiplatform.v1.projects.locations.featurestores.searchFeatures \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:22:29.605414+00:00
---

# Method: googleapis.aiplatform.v1.projects.locations.featurestores.searchFeatures  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/projects.locations.featurestores/searchFeatures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.aiplatform.v1.projects.locations.featurestores.searchFeatures Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Searches Features matching a query in a given project.

## Arguments

Parameters  
---  
`location` |  `string` Required. The resource name of the Location to search Features. Format: `projects/{project}/locations/{location}`  
`pageSize` |  `integer ([int32](https://developers.google.com/discovery/v1/type-format?tenant=cloud) format)` The maximum number of Features to return. The service may return fewer than this value. If unspecified, at most 100 Features will be returned. The maximum value is 100; any value greater than 100 will be coerced to 100.  
`pageToken` |  `string` A page token, received from a previous FeaturestoreService.SearchFeatures call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to FeaturestoreService.SearchFeatures, except `page_size`, must match the call that provided the page token.  
`query` |  `string` Query string that is a conjunction of field-restricted queries and/or field-restricted filters. Field-restricted queries and filters can be combined using `AND` to form a conjunction. A field query is in the form FIELD:QUERY. This implicitly checks if QUERY exists as a substring within Feature's FIELD. The QUERY and the FIELD are converted to a sequence of words (i.e. tokens) for comparison. This is done by: * Removing leading/trailing whitespace and tokenizing the search value. Characters that are not one of alphanumeric `[a-zA-Z0-9]`, underscore `_`, or asterisk `*` are treated as delimiters for tokens. `*` is treated as a wildcard that matches characters within a token. * Ignoring case. * Prepending an asterisk to the first and appending an asterisk to the last token in QUERY. A QUERY must be either a singular token or a phrase. A phrase is one or multiple words enclosed in double quotation marks ("). With phrases, the order of the words is important. Words in the phrase must be matching in order and consecutively. Supported FIELDs for field-restricted queries: * `feature_id` * `description` * `entity_type_id` Examples: * `feature_id: foo` \--> Matches a Feature with ID containing the substring `foo` (eg. `foo`, `foofeature`, `barfoo`). * `feature_id: foo*feature` \--> Matches a Feature with ID containing the substring `foo*feature` (eg. `foobarfeature`). * `feature_id: foo AND description: bar` \--> Matches a Feature with ID containing the substring `foo` and description containing the substring `bar`. Besides field queries, the following exact-match filters are supported. The exact-match filters do not support wildcards. Unlike field-restricted queries, exact-match filters are case-sensitive. * `feature_id`: Supports = comparisons. * `description`: Supports = comparisons. Multi-token filters should be enclosed in quotes. * `entity_type_id`: Supports = comparisons. * `value_type`: Supports = and != comparisons. * `labels`: Supports key-value equality as well as key presence. * `featurestore_id`: Supports = comparisons. Examples: * `description = "foo bar"` \--> Any Feature with description exactly equal to `foo bar` * `value_type = DOUBLE` \--> Features whose type is DOUBLE. * `labels.active = yes AND labels.env = prod` \--> Features having both (active: yes) and (env: prod) labels. * `labels.env: *` \--> Any Feature which has a label with `env` as the key.  
`region` |  `string` Required. Region of the HTTP endpoint. For example, if region is set to `us-central1`, the endpoint https://us-central1-integrations.googleapis.com will be used. See [service endpoints](https://cloud.google.com/vertex-ai/docs/reference/rest#rest_endpoints).  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
  
## Response

If successful, the response contains an instance of [`GoogleCloudAiplatformV1SearchFeaturesResponse`](https://cloud.google.com/workflows/docs/reference/googleapis/aiplatform/v1/Overview#GoogleCloudAiplatformV1SearchFeaturesResponse).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/vertex-ai/docs/reference/rest/v1/projects.locations.featurestores/searchFeatures).

### YAML
    
    
    - searchFeatures:
        call: googleapis.aiplatform.v1.projects.locations.featurestores.searchFeatures
        args:
            location: ...
            pageSize: ...
            pageToken: ...
            query: ...
            region: ...
        result: searchFeaturesResult

### JSON
    
    
    [
      {
        "searchFeatures": {
          "call": "googleapis.aiplatform.v1.projects.locations.featurestores.searchFeatures",
          "args": {
            "location": "...",
            "pageSize": "...",
            "pageToken": "...",
            "query": "...",
            "region": "..."
          },
          "result": "searchFeaturesResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
