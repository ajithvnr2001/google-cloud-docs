---
url: https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.EkmConnection
title: Google Cloud Cloud Controls Partner V1beta Client - Class EkmConnection (0.6.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:47:49.942046+00:00
---

# Google Cloud Cloud Controls Partner V1beta Client - Class EkmConnection (0.6.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.EkmConnection

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Cloud Controls Partner V1beta Client - Class EkmConnection (0.6.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.3 (latest)  0.5.3  0.4.1  0.3.0  0.2.2  0.1.4 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Cloud Controls Partner V1beta Client class EkmConnection.

Details about the EKM connection

Generated from protobuf message `google.cloud.cloudcontrolspartner.v1beta.EkmConnection`

## Namespace

Google \ Cloud \ CloudControlsPartner \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ connection_name` |  `string`   
Resource name of the EKM connection in the format: projects/{project}/locations/{location}/ekmConnections/{ekm_connection}  
`↳ connection_state` |  `int`   
Output only. The connection state  
`↳ connection_error` |  `[EkmConnection\ConnectionError](https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.EkmConnection.ConnectionError)`   
The connection error that occurred if any  
  
### getConnectionName

Resource name of the EKM connection in the format: projects/{project}/locations/{location}/ekmConnections/{ekm_connection}

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setConnectionName

Resource name of the EKM connection in the format: projects/{project}/locations/{location}/ekmConnections/{ekm_connection}

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getConnectionState

Output only. The connection state

**Returns**  
---  
**Type** | **Description**  
`int` | Enum of type [ConnectionState](https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.EkmConnection.ConnectionState).  
  
### setConnectionState

Output only. The connection state

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
Enum of type [ConnectionState](https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.EkmConnection.ConnectionState).   
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getConnectionError

The connection error that occurred if any

**Returns**  
---  
**Type** | **Description**  
`[EkmConnection\ConnectionError](https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.EkmConnection.ConnectionError)|null` |   
  
### hasConnectionError

### clearConnectionError

### setConnectionError

The connection error that occurred if any

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[EkmConnection\ConnectionError](https://docs.cloud.google.com/php/docs/reference/cloud-cloudcontrolspartner/latest/V1beta.EkmConnection.ConnectionError)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
