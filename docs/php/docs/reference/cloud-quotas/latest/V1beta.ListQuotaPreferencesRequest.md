---
url: https://docs.cloud.google.com/php/docs/reference/cloud-quotas/latest/V1beta.ListQuotaPreferencesRequest
title: Google Cloud Quotas V1beta Client - Class ListQuotaPreferencesRequest (1.7.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:35.170405+00:00
---

# Google Cloud Quotas V1beta Client - Class ListQuotaPreferencesRequest (1.7.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-quotas/latest/V1beta.ListQuotaPreferencesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Quotas V1beta Client - Class ListQuotaPreferencesRequest (1.7.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.7.3 (latest)  1.5.5  1.4.1  1.3.1  1.2.1  1.1.1  1.0.1  0.2.3  0.1.0 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Quotas V1beta Client class ListQuotaPreferencesRequest.

Message for requesting list of QuotaPreferences

Generated from protobuf message `google.api.cloudquotas.v1beta.ListQuotaPreferencesRequest`

## Namespace

Google \ Cloud \ CloudQuotas \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. Parent value of QuotaPreference resources. Listing across different resource containers (such as 'projects/-') is not allowed. When the value starts with 'folders' or 'organizations', it lists the QuotaPreferences for org quotas in the container. It does not list the QuotaPreferences in the descendant projects of the container. Example parents: `projects/123/locations/global`  
`↳ page_size` |  `int`   
Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`↳ page_token` |  `string`   
Optional. A token identifying a page of results the server should return.  
`↳ filter` |  `string`   
Optional. Filter result QuotaPreferences by their state, type, create/update time range. Example filters: `reconciling=true AND request_type=CLOUD_CONSOLE`, `reconciling=true OR creation_time>2022-12-03T10:30:00`  
`↳ order_by` |  `string`   
Optional. How to order of the results. By default, the results are ordered by create time. Example orders: `quota_id`, `service, create_time`  
  
### getParent

Required. Parent value of QuotaPreference resources.

Listing across different resource containers (such as 'projects/-') is not allowed. When the value starts with 'folders' or 'organizations', it lists the QuotaPreferences for org quotas in the container. It does not list the QuotaPreferences in the descendant projects of the container. Example parents: `projects/123/locations/global`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. Parent value of QuotaPreference resources.

Listing across different resource containers (such as 'projects/-') is not allowed. When the value starts with 'folders' or 'organizations', it lists the QuotaPreferences for org quotas in the container. It does not list the QuotaPreferences in the descendant projects of the container. Example parents: `projects/123/locations/global`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

Optional. A token identifying a page of results the server should return.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

Optional. A token identifying a page of results the server should return.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFilter

Optional. Filter result QuotaPreferences by their state, type, create/update time range.

Example filters: `reconciling=true AND request_type=CLOUD_CONSOLE`, `reconciling=true OR creation_time>2022-12-03T10:30:00`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setFilter

Optional. Filter result QuotaPreferences by their state, type, create/update time range.

Example filters: `reconciling=true AND request_type=CLOUD_CONSOLE`, `reconciling=true OR creation_time>2022-12-03T10:30:00`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOrderBy

Optional. How to order of the results. By default, the results are ordered by create time.

Example orders: `quota_id`, `service, create_time`

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setOrderBy

Optional. How to order of the results. By default, the results are ordered by create time.

Example orders: `quota_id`, `service, create_time`

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameter**  
---  
**Name** | **Description**  
`parent` |  `string`   
Required. Parent value of QuotaPreference resources. Listing across different resource containers (such as 'projects/-') is not allowed. When the value starts with 'folders' or 'organizations', it lists the QuotaPreferences for org quotas in the container. It does not list the QuotaPreferences in the descendant projects of the container. Example parents: `projects/123/locations/global` Please see CloudQuotasClient::locationName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[ListQuotaPreferencesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-quotas/latest/V1beta.ListQuotaPreferencesRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
