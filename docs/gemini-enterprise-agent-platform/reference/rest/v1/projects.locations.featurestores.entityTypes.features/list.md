---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes.features/list/
title: Method: features.list \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:20:47.996121+00:00
---

# Method: features.list  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes.features/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: features.list Stay organized with collections  Save and categorize content based on your preferences. 

**Full name** : projects.locations.featurestores.entityTypes.features.list

Lists Features in a given EntityType.

### Endpoint

get  `https://{service-endpoint}/v1/{parent}/features`   


Where `{service-endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest#rest_endpoints).

### Path parameters

`parent` `string` Required. The resource name of the Location to list Features. Format for entityType as parent: `projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entityType}` Format for featureGroup as parent: `projects/{project}/locations/{location}/featureGroups/{featureGroup}`

### Query parameters

| `filter` `string` Lists the Features that match the filter expression. The following filters are supported:

  * `valueType`: Supports = and != comparisons.
  * `createTime`: Supports =, !=, <, >, >=, and <= comparisons. Values must be in RFC 3339 format.
  * `updateTime`: Supports =, !=, <, >, >=, and <= comparisons. Values must be in RFC 3339 format.
  * `labels`: Supports key-value equality as well as key presence.

Examples:

  * `valueType = DOUBLE` \--> Features whose type is DOUBLE.
  * `createTime > \"2020-01-31T15:30:00.000000Z\" OR updateTime > \"2020-01-31T15:30:00.000000Z\"` \--> EntityTypes created or updated after 2020-01-31T15:30:00.000000Z.
  * `labels.active = yes AND labels.env = prod` \--> Features having both (active: yes) and (env: prod) labels.
  * `labels.env: *` \--> Any feature which has a label with 'env' as the key.

| `pageSize` `integer` The maximum number of Features to return. The service may return fewer than this value. If unspecified, at most 1000 Features will be returned. The maximum value is 1000; any value greater than 1000 will be coerced to 1000. | `pageToken` `string` A page token, received from a previous `[FeaturestoreService.ListFeatures](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes.features/list#google.cloud.aiplatform.v1.FeaturestoreService.ListFeatures)` call or `[FeatureRegistryService.ListFeatures](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureGroups.features/list#google.cloud.aiplatform.v1.FeatureRegistryService.ListFeatures)` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `[FeaturestoreService.ListFeatures](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featurestores.entityTypes.features/list#google.cloud.aiplatform.v1.FeaturestoreService.ListFeatures)` or `[FeatureRegistryService.ListFeatures](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureGroups.features/list#google.cloud.aiplatform.v1.FeatureRegistryService.ListFeatures)` must match the call that provided the page token. | `orderBy` `string` A comma-separated list of fields to order by, sorted in ascending order. Use "desc" after a field name for descending. Supported fields:

  * `featureId`
  * `valueType` (Not supported for FeatureRegistry feature)
  * `createTime`
  * `updateTime`

| `readMask` `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Mask specifying which fields to read.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`. | `latestStatsCount` `integer` Only applicable for Agent Platform feature Store (Legacy). If set, return the most recent `[ListFeaturesRequest.latest_stats_count](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureGroups.features/list#body.QUERY_PARAMETERS.latest_stats_count)` of stats for each feature in response. Valid value is [0, 10]. If number of stats exists < `[ListFeaturesRequest.latest_stats_count](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.featureGroups.features/list#body.QUERY_PARAMETERS.latest_stats_count)`, return all existing stats.

### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[ListFeaturesResponse](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/ListFeaturesResponse)`. Send feedback  Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates. Last updated 2026-05-04 UTC. Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-04 UTC."],[],[]] 
