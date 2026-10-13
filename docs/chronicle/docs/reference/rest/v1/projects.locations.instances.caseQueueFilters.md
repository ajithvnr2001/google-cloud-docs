---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters
title: REST Resource: projects.locations.instances.caseQueueFilters \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:42.853097+00:00
---

# REST Resource: projects.locations.instances.caseQueueFilters  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.caseQueueFilters Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CaseQueueFilter
    * JSON representation
  * FilterOperator
  * CaseQueueCriteria
    * JSON representation
  * CaseQueueFilterType
  * CompareOperator
  * SearchTimeRangeType
  * Methods



## Resource: CaseQueueFilter

This service is available for customers who migrated SOAR to a customer managed project and have the Chronicle API enabled. Case Queue Filters enable users to narrow your case search in the queue to precisely target the cases you want to analyze, by saving and editing filters that are significantly useful for them.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "filterOperator": enum ([FilterOperator](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters#FilterOperator)),
      "criteria": [
        {
          object ([CaseQueueCriteria](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters#CaseQueueCriteria))
        }
      ],
      "timeRangeFilter": enum ([SearchTimeRangeType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters#SearchTimeRangeType)),
      "startTime": string,
      "endTime": string,
      "author": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique name(ID) of the CaseQueueFilter. Format: projects/{project}/locations/{location}/instances/{instance}/caseQueueFilters/{caseQueueFilter}  
`displayName` |  `string` Required. This is the name of the case queue filter that will be applied to the case filter.  
`filterOperator` |  `enum (`[FilterOperator](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters#FilterOperator)`)` Required. Specifies the logical operator for combining multiple filtering criteria. Required if Criteria is available.  
`criteria[]` |  `object (`[CaseQueueCriteria](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters#CaseQueueCriteria)`)` Optional. List of filters to apply, optional.  
`timeRangeFilter` |  `enum (`[SearchTimeRangeType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters#SearchTimeRangeType)`)` Optional. Specifies the time range filter type to apply.  
`startTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Specifies the start time for filtering cases based on timestamp.  
`endTime` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Specifies the end time for filtering cases based on timestamp.  
`author` |  `string` Output only. Specifies the author of the case queue filter.  
  
## FilterOperator

Enum defining logical operators for combining multiple filters.

Enums  
---  
`FILTER_OPERATOR_UNSPECIFIED` | Default value. This value is unused.  
`OR` | The value is equal to any of the values.  
`AND` | The value is equal to all of the values.  
  
## CaseQueueCriteria

The filtering criteria that each case queue filter can have.

JSON representation  
---  
      
    
    {
      "type": enum ([CaseQueueFilterType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters#CaseQueueFilterType)),
      "operator": enum ([CompareOperator](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters#CompareOperator)),
      "values": [
        string
      ],
      "includeUsers": boolean,
      "customFieldId": string
    }  
  
Fields  
---  
`type` |  `enum (`[CaseQueueFilterType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters#CaseQueueFilterType)`)` Required. The type of the filter.  
`operator` |  `enum (`[CompareOperator](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters#CompareOperator)`)` Required. The comparison operator used for the filter.  
`values[]` |  `string` Required. The values of the filter.  
`includeUsers` |  `boolean` Optional. If the filter is of type Analysts (Roles / users) , and this is set to True, then the BE will also search for cases assigned to users that are a part of the roles in the search. "Include users associated with selected roles" in the UI. Otherwise the related to the selected roles users will not be included in the result.  
`customFieldId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. The ID of the custom field, if type is CUSTOM_FIELD.  
  
## CaseQueueFilterType

Enum representing different filter types that can be used for case queue filtering.

Enums  
---  
`CASE_QUEUE_FILTER_TYPE_UNSPECIFIED` | Default value. This value is unused.  
`ENVIRONMENTS` | The value is Environments.  
`PRIORITIES` | The value is Priorities.  
`STAGES` | The value is Stages.  
`TAGS` | The value is Tags.  
`ALERTS_NAME` | The value is Alerts name.  
`PRODUCTS` | The value is Products.  
`PLATFORMS` | The value is Platforms.  
`ANALYSTS` | The value is Analysts.  
`ALERTS_VENDOR` | The value is Alerts vendor.  
`TYPE` | The value is Type.  
`ENVIRONMENT_DYNAMIC_PARAMETERS` | The value is Environments dynamic parameters.  
`CASE_SLA` | The value is Case SLA.  
`WORKFLOW_STATUS` | The value is Workflow status.  
`DATA_ACCESS_SCOPES` | The value is Data Access Scopes.  
`CUSTOM_FIELD` | Represents a filter based on custom fields.  
  
## CompareOperator

Enum defining comparison operators used in filtering criteria.

Enums  
---  
`COMPARE_OPERATOR_UNSPECIFIED` | Default value. This value is unused.  
`IS` | The value is equal to any of the selected values.  
`IS_NOT` | The value is not equal to any of the selected values.  
  
## SearchTimeRangeType

Enum representing predefined time range filters. The SEARCH_TIME_RANGE_TYPE_UNSPECIFIED (Custom value in the UI) provides a fixed interval search - e.g. to find cases only for [March 10 - March 30]. The rest of enum values provide dynamic time range search - e.g. if LAST_WEEK is selected it always queries cases for the last week.

Enums  
---  
`SEARCH_TIME_RANGE_TYPE_UNSPECIFIED` | Default value.  
`CUSTOM` | Custom time Range.  
`LAST_DAY` | Search for cases for the last day.  
`LAST_2_DAYS` | Search for cases for the last 2 days.  
`LAST_3_DAYS` | Search for cases for the last 3 days.  
`LAST_WEEK` | Search for cases for the last 7 days.  
`LAST_YEAR` | Search for cases for the last year.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters/create)`

|  Creates a new CaseQueueFilter.  
  
### `[delete](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters/delete)`

|  Deletes a CaseQueueFilter.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters/get)`

|  Gets a single CaseQueueFilter by its resource name.  
  
### `[getShareConfig](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters/getShareConfig)`

|  Gets the ShareConfig for a specific CaseQueueFilter.  
  
### `[list](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters/list)`

|  Lists CaseQueueFilters available to the user.  
  
### `[patch](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters/patch)`

|  Updates an existing CaseQueueFilter.  
  
### `[updateShareConfig](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.caseQueueFilters/updateShareConfig)`

|  Updates the ShareConfig for a specific CaseQueueFilter.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-13 UTC."],[],[]] 
