---
url: https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.corpora.searchConfigs/patch/
title: Method: projects.locations.corpora.searchConfigs.patch \u00a0|\u00a0 Agent Platform Vision \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:51.668017+00:00
---

# Method: projects.locations.corpora.searchConfigs.patch  |  Agent Platform Vision  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.corpora.searchConfigs/patch/

Vertex AI Vision is deprecated as of June 15, 2026 and reaches End of Life on September 30, 2026. To migrate, see the [Cloud Vision API](https://docs.cloud.google.com/vision/docs), [Agent Platform serverless training](https://docs.cloud.google.com/gemini-enterprise-agent-platform/machine-learning/training/overview), or [Agent Platform models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Platform Vision ](https://docs.cloud.google.com/vision-ai/docs)
  * [ Reference ](https://docs.cloud.google.com/vision-ai/docs/reference/rest)



Send feedback 

#  Method: projects.locations.corpora.searchConfigs.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions



Updates a search configuration inside a corpus.

Please follow the rules below to create a valid UpdateSearchConfigRequest. --- General Rules --- 1. Request.search_configuration.name must already exist. 2. Request must contain at least one non-empty searchCriteriaProperty or facetProperty. 3. mappedFields must not be empty, and must map to existing UGA keys. 4. All mappedFields must be of the same type. 5. All mappedFields must share the same granularity. 6. All mappedFields must share the same semantic SearchConfig match options. For property-specific rules, please reference the comments for FacetProperty and SearchCriteriaProperty.

### HTTP request

`PATCH https://visionai.googleapis.com/v1alpha1/{searchConfig.name=projects/*/locations/*/corpora/*/searchConfigs/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`searchConfig.name` |  `string` Resource name of the search configuration. For CustomSearchCriteria, searchConfig would be the search operator name. For Facets, searchConfig would be the facet dimension name. Format: `projects/{project_number}/locations/{location}/corpora/{corpus}/searchConfigs/{searchConfig}`  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.FieldMask)` format)` The list of fields to be updated. If left unset, all field paths will be updated/overwritten.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[SearchConfig](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.corpora.searchConfigs#SearchConfig)`.

### Response body

If successful, the response body contains an instance of `[SearchConfig](https://docs.cloud.google.com/vision-ai/docs/reference/rest/v1alpha1/projects.locations.corpora.searchConfigs#SearchConfig)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://cloud.google.com/docs/authentication/).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `visionai.searchConfigs.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
