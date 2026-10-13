---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListBackupsRequest
title: Cloud Bigtable V2 Client - Class ListBackupsRequest (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:47.345340+00:00
---

# Cloud Bigtable V2 Client - Class ListBackupsRequest (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListBackupsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class ListBackupsRequest (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class ListBackupsRequest.

The request for [ListBackups](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Client.BigtableTableAdminClient#_Google_Cloud_Bigtable_Admin_V2_Client_BigtableTableAdminClient__listBackups__).

Generated from protobuf message `google.bigtable.admin.v2.ListBackupsRequest`

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
Required. The cluster to list backups from. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}`. Use `{cluster} = '-'` to list backups for all clusters in an instance, e.g., `projects/{project}/instances/{instance}/clusters/-`.  
`↳ filter` |  `string`   
A filter expression that filters backups listed in the response. The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be <, >, <=, >=, !=, =, or :. Colon ':' represents a HAS operator which is roughly synonymous with equality. Filter rules are case insensitive. The fields eligible for filtering are: * * `name` * * `source_table` * * `state` * * `start_time` (and values are of the format YYYY-MM-DDTHH:MM:SSZ) * * `end_time` (and values are of the format YYYY-MM-DDTHH:MM:SSZ) * * `expire_time` (and values are of the format YYYY-MM-DDTHH:MM:SSZ) * * `size_bytes` To filter on multiple expressions, provide each separate expression within parentheses. By default, each expression is an AND expression. However, you can include AND, OR, and NOT expressions explicitly. Some examples of using filters are: * * `name:"exact"` \--> The backup's name is the string "exact". * * `name:howl` \--> The backup's name contains the string "howl". * * `source_table:prod` \--> The source_table's name contains the string "prod". * * `state:CREATING` \--> The backup is pending creation. * * `state:READY` \--> The backup is fully created and ready for use. * * `(name:howl) AND (start_time < \"2018-03-28T14:50:00Z\")` \--> The backup name contains the string "howl" and start_time of the backup is before 2018-03-28T14:50:00Z. * * `size_bytes > 10000000000` \--> The backup's size is greater than 10GB  
`↳ order_by` |  `string`   
An expression for specifying the sort order of the results of the request. The string value should specify one or more fields in [Backup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup). The full syntax is described at <https://aip.dev/132#ordering>. Fields supported are: * * name * * source_table * * expire_time * * start_time * * end_time * * size_bytes * * state For example, "start_time". The default sorting order is ascending. To specify descending order for the field, a suffix " desc" should be appended to the field name. For example, "start_time desc". Redundant space characters in the syntax are insigificant. If order_by is empty, results will be sorted by `start_time` in descending order starting from the most recently created backup.  
`↳ page_size` |  `int`   
Number of backups to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.  
`↳ page_token` |  `string`   
If non-empty, `page_token` should contain a [next_page_token](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListBackupsResponse#_Google_Cloud_Bigtable_Admin_V2_ListBackupsResponse__getNextPageToken__) from a previous [ListBackupsResponse](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListBackupsResponse) to the same `parent` and with the same `filter`.  
  
### getParent

Required. The cluster to list backups from. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}`.

Use `{cluster} = '-'` to list backups for all clusters in an instance, e.g., `projects/{project}/instances/{instance}/clusters/-`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. The cluster to list backups from. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}`.

Use `{cluster} = '-'` to list backups for all clusters in an instance, e.g., `projects/{project}/instances/{instance}/clusters/-`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFilter

A filter expression that filters backups listed in the response.

The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be <, >, <=, >=, !=, =, or :. Colon ':' represents a HAS operator which is roughly synonymous with equality. Filter rules are case insensitive. The fields eligible for filtering are:

  * `name`
  * `source_table`
  * `state`
  * `start_time` (and values are of the format YYYY-MM-DDTHH:MM:SSZ)
  * `end_time` (and values are of the format YYYY-MM-DDTHH:MM:SSZ)
  * `expire_time` (and values are of the format YYYY-MM-DDTHH:MM:SSZ)
  * `size_bytes` To filter on multiple expressions, provide each separate expression within parentheses. By default, each expression is an AND expression. However, you can include AND, OR, and NOT expressions explicitly. Some examples of using filters are:
  * `name:"exact"` \--> The backup's name is the string "exact".
  * `name:howl` \--> The backup's name contains the string "howl".
  * `source_table:prod` \--> The source_table's name contains the string "prod".
  * `state:CREATING` \--> The backup is pending creation.
  * `state:READY` \--> The backup is fully created and ready for use.
  * `(name:howl) AND (start_time < \"2018-03-28T14:50:00Z\")` \--> The backup name contains the string "howl" and start_time of the backup is before 2018-03-28T14:50:00Z.
  * `size_bytes > 10000000000` \--> The backup's size is greater than 10GB



**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setFilter

A filter expression that filters backups listed in the response.

The expression must specify the field name, a comparison operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The comparison operator must be <, >, <=, >=, !=, =, or :. Colon ':' represents a HAS operator which is roughly synonymous with equality. Filter rules are case insensitive. The fields eligible for filtering are:

  * `name`
  * `source_table`
  * `state`
  * `start_time` (and values are of the format YYYY-MM-DDTHH:MM:SSZ)
  * `end_time` (and values are of the format YYYY-MM-DDTHH:MM:SSZ)
  * `expire_time` (and values are of the format YYYY-MM-DDTHH:MM:SSZ)
  * `size_bytes` To filter on multiple expressions, provide each separate expression within parentheses. By default, each expression is an AND expression. However, you can include AND, OR, and NOT expressions explicitly. Some examples of using filters are:
  * `name:"exact"` \--> The backup's name is the string "exact".
  * `name:howl` \--> The backup's name contains the string "howl".
  * `source_table:prod` \--> The source_table's name contains the string "prod".
  * `state:CREATING` \--> The backup is pending creation.
  * `state:READY` \--> The backup is fully created and ready for use.
  * `(name:howl) AND (start_time < \"2018-03-28T14:50:00Z\")` \--> The backup name contains the string "howl" and start_time of the backup is before 2018-03-28T14:50:00Z.
  * `size_bytes > 10000000000` \--> The backup's size is greater than 10GB



**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOrderBy

An expression for specifying the sort order of the results of the request.

The string value should specify one or more fields in [Backup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup). The full syntax is described at <https://aip.dev/132#ordering>. Fields supported are:

  * name
  * source_table
  * expire_time
  * start_time
  * end_time
  * size_bytes
  * state For example, "start_time". The default sorting order is ascending. To specify descending order for the field, a suffix " desc" should be appended to the field name. For example, "start_time desc". Redundant space characters in the syntax are insigificant. If order_by is empty, results will be sorted by `start_time` in descending order starting from the most recently created backup.



**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setOrderBy

An expression for specifying the sort order of the results of the request.

The string value should specify one or more fields in [Backup](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.Backup). The full syntax is described at <https://aip.dev/132#ordering>. Fields supported are:

  * name
  * source_table
  * expire_time
  * start_time
  * end_time
  * size_bytes
  * state For example, "start_time". The default sorting order is ascending. To specify descending order for the field, a suffix " desc" should be appended to the field name. For example, "start_time desc". Redundant space characters in the syntax are insigificant. If order_by is empty, results will be sorted by `start_time` in descending order starting from the most recently created backup.



**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

Number of backups to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

Number of backups to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

If non-empty, `page_token` should contain a [next_page_token](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListBackupsResponse#_Google_Cloud_Bigtable_Admin_V2_ListBackupsResponse__getNextPageToken__) from a previous [ListBackupsResponse](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListBackupsResponse) to the same `parent` and with the same `filter`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

If non-empty, `page_token` should contain a [next_page_token](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListBackupsResponse#_Google_Cloud_Bigtable_Admin_V2_ListBackupsResponse__getNextPageToken__) from a previous [ListBackupsResponse](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListBackupsResponse) to the same `parent` and with the same `filter`.

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
Required. The cluster to list backups from. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}`. Use `{cluster} = '-'` to list backups for all clusters in an instance, e.g., `projects/{project}/instances/{instance}/clusters/-`. Please see BigtableTableAdminClient::clusterName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[ListBackupsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.ListBackupsRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
