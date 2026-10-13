---
url: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.ContextRule
title: Google API Common Protos Client - Class ContextRule (4.14.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:50:30.432988+00:00
---

# Google API Common Protos Client - Class ContextRule (4.14.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.ContextRule

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google API Common Protos Client - Class ContextRule (4.14.3) Stay organized with collections  Save and categorize content based on your preferences. 

4.14.3 (latest)  4.14.1  4.13.0  4.12.5  4.11.0  4.10.0  4.9.0  4.8.3 

Reference documentation and code samples for the Google API Common Protos Client class ContextRule.

A context rule provides information about the context for an individual API element.

Generated from protobuf message `google.api.ContextRule`

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
`↳ selector` |  `string`   
Selects the methods to which this rule applies. Refer to [selector](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.DocumentationRule#_Google_Api_DocumentationRule__getSelector__) for syntax details.  
`↳ requested` |  `string[]`   
A list of full type names of requested contexts, only the requested context will be made available to the backend.  
`↳ provided` |  `string[]`   
A list of full type names of provided contexts. It is used to support propagating HTTP headers and ETags from the response extension.  
`↳ allowed_request_extensions` |  `string[]`   
A list of full type names or extension IDs of extensions allowed in grpc side channel from client to backend.  
`↳ allowed_response_extensions` |  `string[]`   
A list of full type names or extension IDs of extensions allowed in grpc side channel from backend to client.  
  
### getSelector

Selects the methods to which this rule applies.

Refer to [selector](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.DocumentationRule#_Google_Api_DocumentationRule__getSelector__) for syntax details.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setSelector

Selects the methods to which this rule applies.

Refer to [selector](https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Api.DocumentationRule#_Google_Api_DocumentationRule__getSelector__) for syntax details.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getRequested

A list of full type names of requested contexts, only the requested context will be made available to the backend.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField.html)<string>` |   
  
### setRequested

A list of full type names of requested contexts, only the requested context will be made available to the backend.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getProvided

A list of full type names of provided contexts. It is used to support propagating HTTP headers and ETags from the response extension.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField.html)<string>` |   
  
### setProvided

A list of full type names of provided contexts. It is used to support propagating HTTP headers and ETags from the response extension.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAllowedRequestExtensions

A list of full type names or extension IDs of extensions allowed in grpc side channel from client to backend.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField.html)<string>` |   
  
### setAllowedRequestExtensions

A list of full type names or extension IDs of extensions allowed in grpc side channel from client to backend.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getAllowedResponseExtensions

A list of full type names or extension IDs of extensions allowed in grpc side channel from backend to client.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\RepeatedField](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.RepeatedField.html)<string>` |   
  
### setAllowedResponseExtensions

A list of full type names or extension IDs of extensions allowed in grpc side channel from backend to client.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string[]`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
