---
url: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.HotTablet
title: Cloud Bigtable V2 Client - Class HotTablet (2.31.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:55:46.435028+00:00
---

# Cloud Bigtable V2 Client - Class HotTablet (2.31.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-bigtable/latest/Admin.V2.HotTablet

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Cloud Bigtable V2 Client - Class HotTablet (2.31.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.31.0 (latest)  2.30.0  2.29.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.1  2.20.2  2.19.2  2.18.0  2.17.1  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.1  2.9.1  2.8.0  2.7.0  2.6.3  2.5.0  2.4.0  2.3.0  2.2.1  2.1.0  2.0.1  1.32.1  1.31.1  1.30.0  1.29.2  1.28.3  1.27.0  1.26.2  1.25.0  1.24.1  1.23.0  1.22.2  1.21.1  1.20.3 

Reference documentation and code samples for the Cloud Bigtable V2 Client class HotTablet.

A tablet is a defined by a start and end key and is explained in <https://cloud.google.com/bigtable/docs/overview#architecture> and <https://cloud.google.com/bigtable/docs/performance#optimization>.

A Hot tablet is a tablet that exhibits high average cpu usage during the time interval from start time to end time.

Generated from protobuf message `google.bigtable.admin.v2.HotTablet`

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
`↳ name` |  `string`   
The unique name of the hot tablet. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/hotTablets/[a-zA-Z0-9_-]*`.  
`↳ table_name` |  `string`   
Name of the table that contains the tablet. Values are of the form `projects/{project}/instances/{instance}/tables/[_a-zA-Z0-9][-_.a-zA-Z0-9]*`.  
`↳ start_time` |  `Google\Protobuf\Timestamp`   
Output only. The start time of the hot tablet.  
`↳ end_time` |  `Google\Protobuf\Timestamp`   
Output only. The end time of the hot tablet.  
`↳ start_key` |  `string`   
Tablet Start Key (inclusive).  
`↳ end_key` |  `string`   
Tablet End Key (inclusive).  
`↳ node_cpu_usage_percent` |  `float`   
Output only. The average CPU usage spent by a node on this tablet over the start_time to end_time time range. The percentage is the amount of CPU used by the node to serve the tablet, from 0% (tablet was not interacted with) to 100% (the node spent all cycles serving the hot tablet).  
  
### getName

The unique name of the hot tablet. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/hotTablets/[a-zA-Z0-9_-]*`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setName

The unique name of the hot tablet. Values are of the form `projects/{project}/instances/{instance}/clusters/{cluster}/hotTablets/[a-zA-Z0-9_-]*`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getTableName

Name of the table that contains the tablet. Values are of the form `projects/{project}/instances/{instance}/tables/[_a-zA-Z0-9][-_.a-zA-Z0-9]*`.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setTableName

Name of the table that contains the tablet. Values are of the form `projects/{project}/instances/{instance}/tables/[_a-zA-Z0-9][-_.a-zA-Z0-9]*`.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStartTime

Output only. The start time of the hot tablet.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasStartTime

### clearStartTime

### setStartTime

Output only. The start time of the hot tablet.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEndTime

Output only. The end time of the hot tablet.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasEndTime

### clearEndTime

### setEndTime

Output only. The end time of the hot tablet.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getStartKey

Tablet Start Key (inclusive).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setStartKey

Tablet Start Key (inclusive).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getEndKey

Tablet End Key (inclusive).

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setEndKey

Tablet End Key (inclusive).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNodeCpuUsagePercent

Output only. The average CPU usage spent by a node on this tablet over the start_time to end_time time range. The percentage is the amount of CPU used by the node to serve the tablet, from 0% (tablet was not interacted with) to 100% (the node spent all cycles serving the hot tablet).

**Returns**  
---  
**Type** | **Description**  
`float` |   
  
### setNodeCpuUsagePercent

Output only. The average CPU usage spent by a node on this tablet over the start_time to end_time time range. The percentage is the amount of CPU used by the node to serve the tablet, from 0% (tablet was not interacted with) to 100% (the node spent all cycles serving the hot tablet).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `float`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
