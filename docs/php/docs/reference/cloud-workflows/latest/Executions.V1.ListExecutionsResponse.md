---
url: https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.ListExecutionsResponse
title: Google Cloud Workflows V1 Client - Class ListExecutionsResponse (1.4.4) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:31.794261+00:00
---

# Google Cloud Workflows V1 Client - Class ListExecutionsResponse (1.4.4)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.ListExecutionsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Workflows V1 Client - Class ListExecutionsResponse (1.4.4) Stay organized with collections  Save and categorize content based on your preferences. 

1.4.4 (latest)  1.3.0  1.2.1  1.1.1  1.0.3  0.5.5  0.4.2  0.3.0  0.2.17 

Reference documentation and code samples for the Google Cloud Workflows V1 Client class ListExecutionsResponse.

Response for the [ListExecutions](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Client.ExecutionsClient#_Google_Cloud_Workflows_Executions_V1_Client_ExecutionsClient__listExecutions__) method.

Generated from protobuf message `google.cloud.workflows.executions.v1.ListExecutionsResponse`

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
`↳ executions` |  `array<[Execution](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution)>`   
The executions which match the request.  
`↳ next_page_token` |  `string`   
A token, which can be sent as `page_token` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### getExecutions

The executions which match the request.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\RepeatedField<[Execution](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution)>` |   
  
### setExecutions

The executions which match the request.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array<[Execution](https://docs.cloud.google.com/php/docs/reference/cloud-workflows/latest/Executions.V1.Execution)>`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getNextPageToken

A token, which can be sent as `page_token` to retrieve the next page.

If this field is omitted, there are no subsequent pages.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setNextPageToken

A token, which can be sent as `page_token` to retrieve the next page.

If this field is omitted, there are no subsequent pages.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
