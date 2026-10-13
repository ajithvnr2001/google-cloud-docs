---
url: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.MonitoredResourceMetadata
title: Google API Common Protos Client - Class MonitoredResourceMetadata (4.14.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:37:04.850285+00:00
---

# Google API Common Protos Client - Class MonitoredResourceMetadata (4.14.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.MonitoredResourceMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google API Common Protos Client - Class MonitoredResourceMetadata (4.14.3) Stay organized with collections  Save and categorize content based on your preferences. 

4.14.3 (latest)  4.14.1  4.13.0  4.12.5  4.11.0  4.10.0  4.9.0  4.8.3 

Reference documentation and code samples for the Google API Common Protos Client class MonitoredResourceMetadata.

Auxiliary metadata for a [MonitoredResource](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.MonitoredResource) object. [MonitoredResource](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.MonitoredResource) objects contain the minimum set of information to uniquely identify a monitored resource instance. There is some other useful auxiliary metadata. Monitoring and Logging use an ingestion pipeline to extract metadata for cloud resources of all types, and store the metadata in this message.

Generated from protobuf message `google.api.MonitoredResourceMetadata`

## Namespace

Google \ Api

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ system_labels` |  `[Google\Protobuf\Struct](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Struct.html)`   
Output only. Values for predefined system metadata labels. System labels are a kind of metadata extracted by Google, including "machine_image", "vpc", "subnet_id", "security_group", "name", etc. System label values can be only strings, Boolean values, or a list of strings. For example: { "name": "my-test-instance", "security_group": ["a", "b", "c"], "spot_instance": false }  
`↳ user_labels` |  `array|[Google\Protobuf\Internal\MapField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.MapField.html)`   
Output only. A map of user-defined metadata labels.  
  
### getSystemLabels

Output only. Values for predefined system metadata labels.

System labels are a kind of metadata extracted by Google, including "machine_image", "vpc", "subnet_id", "security_group", "name", etc. System label values can be only strings, Boolean values, or a list of strings. For example: { "name": "my-test-instance", "security_group": ["a", "b", "c"], "spot_instance": false }

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\Struct](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Struct.html)|null` |   
  
### hasSystemLabels

### clearSystemLabels

### setSystemLabels

Output only. Values for predefined system metadata labels.

System labels are a kind of metadata extracted by Google, including "machine_image", "vpc", "subnet_id", "security_group", "name", etc. System label values can be only strings, Boolean values, or a list of strings. For example: { "name": "my-test-instance", "security_group": ["a", "b", "c"], "spot_instance": false }

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Protobuf\Struct](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Struct.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUserLabels

Output only. A map of user-defined metadata labels.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\Internal\MapField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.MapField.html)` |   
  
### setUserLabels

Output only. A map of user-defined metadata labels.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `array|[Google\Protobuf\Internal\MapField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Internal.MapField.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
