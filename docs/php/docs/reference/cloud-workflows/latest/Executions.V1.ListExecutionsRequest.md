---
url: https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.ListExecutionsRequest
title: Google Cloud Workflows V1 Client - Class ListExecutionsRequest (1.4.4) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:31.623511+00:00
---

# Google Cloud Workflows V1 Client - Class ListExecutionsRequest (1.4.4)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.ListExecutionsRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Workflows V1 Client - Class ListExecutionsRequest (1.4.4) Stay organized with collections  Save and categorize content based on your preferences. 

1.4.4 (latest)  1.3.0  1.2.1  1.1.1  1.0.3  0.5.5  0.4.2  0.3.0  0.2.17 

Reference documentation and code samples for the Google Cloud Workflows V1 Client class ListExecutionsRequest.

Request for the ListExecutions method.

Generated from protobuf message `google.cloud.workflows.executions.v1.ListExecutionsRequest`

## Namespace

Google \ Cloud \ Workflows \ Executions \ V1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ parent` |  `string`   
Required. Name of the workflow for which the executions should be listed. Format: projects/{project}/locations/{location}/workflows/{workflow}  
`↳ page_size` |  `int`   
Maximum number of executions to return per call. Max supported value depends on the selected Execution view: it's 1000 for BASIC and 100 for FULL. The default value used if the field is not specified is 100, regardless of the selected view. Values greater than the max value will be coerced down to it.  
`↳ page_token` |  `string`   
A page token, received from a previous `ListExecutions` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListExecutions` must match the call that provided the page token. Note that pagination is applied to dynamic data. The list of executions returned can change between page requests.  
`↳ view` |  `int`   
Optional. A view defining which fields should be filled in the returned executions. The API will default to the BASIC view.  
`↳ filter` |  `string`   
Optional. Filters applied to the [Executions.ListExecutions] results. The following fields are supported for filtering: executionID, state, startTime, endTime, duration, workflowRevisionID, stepName, and label.  
`↳ order_by` |  `string`   
Optional. The ordering applied to the [Executions.ListExecutions] results. By default the ordering is based on descending start time. The following fields are supported for order by: executionID, startTime, endTime, duration, state, and workflowRevisionID.  
  
### getParent

Required. Name of the workflow for which the executions should be listed.

Format: projects/{project}/locations/{location}/workflows/{workflow}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setParent

Required. Name of the workflow for which the executions should be listed.

Format: projects/{project}/locations/{location}/workflows/{workflow}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageSize

Maximum number of executions to return per call.

Max supported value depends on the selected Execution view: it's 1000 for BASIC and 100 for FULL. The default value used if the field is not specified is 100, regardless of the selected view. Values greater than the max value will be coerced down to it.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### setPageSize

Maximum number of executions to return per call.

Max supported value depends on the selected Execution view: it's 1000 for BASIC and 100 for FULL. The default value used if the field is not specified is 100, regardless of the selected view. Values greater than the max value will be coerced down to it.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPageToken

A page token, received from a previous `ListExecutions` call.

Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListExecutions` must match the call that provided the page token. Note that pagination is applied to dynamic data. The list of executions returned can change between page requests.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setPageToken

A page token, received from a previous `ListExecutions` call.

Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `ListExecutions` must match the call that provided the page token. Note that pagination is applied to dynamic data. The list of executions returned can change between page requests.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getView

Optional. A view defining which fields should be filled in the returned executions. The API will default to the BASIC view.

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [ExecutionView](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.ExecutionView).  
  
### setView

Optional. A view defining which fields should be filled in the returned executions. The API will default to the BASIC view.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [ExecutionView](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.ExecutionView).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFilter

Optional. Filters applied to the [Executions.ListExecutions] results.

The following fields are supported for filtering: executionID, state, startTime, endTime, duration, workflowRevisionID, stepName, and label.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setFilter

Optional. Filters applied to the [Executions.ListExecutions] results.

The following fields are supported for filtering: executionID, state, startTime, endTime, duration, workflowRevisionID, stepName, and label.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getOrderBy

Optional. The ordering applied to the [Executions.ListExecutions] results.

By default the ordering is based on descending start time. The following fields are supported for order by: executionID, startTime, endTime, duration, state, and workflowRevisionID.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setOrderBy

Optional. The ordering applied to the [Executions.ListExecutions] results.

By default the ordering is based on descending start time. The following fields are supported for order by: executionID, startTime, endTime, duration, state, and workflowRevisionID.

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
Required. Name of the workflow for which the executions should be listed. Format: projects/{project}/locations/{location}/workflows/{workflow} Please see ExecutionsClient::workflowName() for help formatting this field.  
**Returns**  
---  
**Type** | **Description**  
`[ListExecutionsRequest](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.ListExecutionsRequest)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
