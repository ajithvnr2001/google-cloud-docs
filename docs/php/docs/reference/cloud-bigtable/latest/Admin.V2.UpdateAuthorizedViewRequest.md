---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateAuthorizedViewRequest
title: Cloud Bigtable V2 Client - Class UpdateAuthorizedViewRequest (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:02.986206+00:00
---

# Cloud Bigtable V2 Client - Class UpdateAuthorizedViewRequest (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateAuthorizedViewRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class UpdateAuthorizedViewRequest (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class UpdateAuthorizedViewRequest.

The request for [UpdateAuthorizedView](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__updateAuthorizedView__).

Generated from protobuf message `google.bigtable.admin.v2.UpdateAuthorizedViewRequest`

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
`↳ authorized_view` |  `[AuthorizedView](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AuthorizedView)`   
Required. The AuthorizedView to update. The `name` in `authorized_view` is used to identify the AuthorizedView. AuthorizedView name must in this format: `projects/{project}/instances/{instance}/tables/{table}/authorizedViews/{authorized_view}`.  
`↳ update_mask` |  `Google\Protobuf\FieldMask`   
Optional. The list of fields to update. A mask specifying which fields in the AuthorizedView resource should be updated. This mask is relative to the AuthorizedView resource, not to the request message. A field will be overwritten if it is in the mask. If empty, all fields set in the request will be overwritten. A special value `*` means to overwrite all fields (including fields not set in the request).  
`↳ ignore_warnings` |  `bool`   
Optional. If true, ignore the safety checks when updating the AuthorizedView.  
  
### getAuthorizedView

Required. The AuthorizedView to update. The `name` in `authorized_view` is used to identify the AuthorizedView. AuthorizedView name must in this format: `projects/{project}/instances/{instance}/tables/{table}/authorizedViews/{authorized_view}`.

**Returns**  
---  
**Type** | **Description**  
`[AuthorizedView](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AuthorizedView)|null` |   
  
### hasAuthorizedView

### clearAuthorizedView

### setAuthorizedView

Required. The AuthorizedView to update. The `name` in `authorized_view` is used to identify the AuthorizedView. AuthorizedView name must in this format: `projects/{project}/instances/{instance}/tables/{table}/authorizedViews/{authorized_view}`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[AuthorizedView](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AuthorizedView)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUpdateMask

Optional. The list of fields to update.

A mask specifying which fields in the AuthorizedView resource should be updated. This mask is relative to the AuthorizedView resource, not to the request message. A field will be overwritten if it is in the mask. If empty, all fields set in the request will be overwritten. A special value `*` means to overwrite all fields (including fields not set in the request).

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\FieldMask|null` |   
  
### hasUpdateMask

### clearUpdateMask

### setUpdateMask

Optional. The list of fields to update.

A mask specifying which fields in the AuthorizedView resource should be updated. This mask is relative to the AuthorizedView resource, not to the request message. A field will be overwritten if it is in the mask. If empty, all fields set in the request will be overwritten. A special value `*` means to overwrite all fields (including fields not set in the request).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\FieldMask`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getIgnoreWarnings

Optional. If true, ignore the safety checks when updating the AuthorizedView.

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### setIgnoreWarnings

Optional. If true, ignore the safety checks when updating the AuthorizedView.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### static::build

**Parameters**  
---  
**Name** | **Description**  
`authorizedView` |  `[AuthorizedView](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.AuthorizedView)`   
Required. The AuthorizedView to update. The `name` in `authorized_view` is used to identify the AuthorizedView. AuthorizedView name must in this format: `projects/{project}/instances/{instance}/tables/{table}/authorizedViews/{authorized_view}`.  
`updateMask` |  `Google\Protobuf\FieldMask`   
Optional. The list of fields to update. A mask specifying which fields in the AuthorizedView resource should be updated. This mask is relative to the AuthorizedView resource, not to the request message. A field will be overwritten if it is in the mask. If empty, all fields set in the request will be overwritten. A special value `*` means to overwrite all fields (including fields not set in the request).  
**Returns**  
---  
**Type** | **Description**  
`[UpdateAuthorizedViewRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.UpdateAuthorizedViewRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
