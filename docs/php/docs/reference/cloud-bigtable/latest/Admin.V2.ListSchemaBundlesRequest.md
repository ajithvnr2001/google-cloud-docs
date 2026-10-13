---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListSchemaBundlesRequest
title: Cloud Bigtable V2 Client - Class ListSchemaBundlesRequest (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:50.278306+00:00
---

# Cloud Bigtable V2 Client - Class ListSchemaBundlesRequest (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListSchemaBundlesRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class ListSchemaBundlesRequest (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class ListSchemaBundlesRequest.

The request for [ListSchemaBundles](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__listSchemaBundles__).

Generated from protobuf message `google.bigtable.admin.v2.ListSchemaBundlesRequest`

## Namespace

Google \ Cloud \ Bigtable \ Admin \ V2

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. The parent, which owns this collection of schema bundles. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.  
`↳ page_size` |  `int`   
The maximum number of schema bundles to return. If the value is positive, the server may return at most this value. If unspecified, the server will return the maximum allowed page size.  
`↳ page_token` |  `string`   
A page token, received from a previous `ListSchemaBundles` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListSchemaBundles` must match the call that provided the page token.  
  
### getParent

Required. The parent, which owns this collection of schema bundles.

Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. The parent, which owns this collection of schema bundles.

Values are of the form `projects/{project}/instances/{instance}/tables/{table}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

The maximum number of schema bundles to return. If the value is positive, the server may return at most this value. If unspecified, the server will return the maximum allowed page size.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

The maximum number of schema bundles to return. If the value is positive, the server may return at most this value. If unspecified, the server will return the maximum allowed page size.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

A page token, received from a previous `ListSchemaBundles` call.

Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListSchemaBundles` must match the call that provided the page token.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

A page token, received from a previous `ListSchemaBundles` call.

Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListSchemaBundles` must match the call that provided the page token.

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
Required. The parent, which owns this collection of schema bundles. Values are of the form `projects/{project}/instances/{instance}/tables/{table}`. Please see BigtableTableAdminClient::tableName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[ListSchemaBundlesRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListSchemaBundlesRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
