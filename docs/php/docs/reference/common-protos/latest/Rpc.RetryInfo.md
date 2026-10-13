---
url: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Rpc.RetryInfo
title: Google API Common Protos Client - Class RetryInfo (4.14.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:26:22.631610+00:00
---

# Google API Common Protos Client - Class RetryInfo (4.14.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/common-protos/latest/Rpc.RetryInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google API Common Protos Client - Class RetryInfo (4.14.3) Stay organized with collections  Save and categorize content based on your preferences. 

4.14.3 (latest)  4.14.1  4.13.0  4.12.5  4.11.0  4.10.0  4.9.0  4.8.3 

Reference documentation and code samples for the Google API Common Protos Client class RetryInfo.

Describes when the clients can retry a failed request. Clients could ignore the recommendation here or retry when this information is missing from error responses.

It's always recommended that clients should use exponential backoff when retrying. Clients should wait until `retry_delay` amount of time has passed since receiving the error response before retrying. If retrying requests also fail, clients should use an exponential backoff scheme to gradually increase the delay between retries based on `retry_delay`, until either a maximum number of retries have been reached or a maximum retry delay cap has been reached.

Generated from protobuf message `google.rpc.RetryInfo`

## Namespace

Google \ Rpc

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ retry_delay` |  `[Google\Protobuf\Duration](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Duration.html)`   
Clients should wait at least this long between retrying the same request.  
  
### getRetryDelay

Clients should wait at least this long between retrying the same request.

**Returns**  
---  
**Type** | **Description**  
`[Google\Protobuf\Duration](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Duration.html)|null` |   
  
### hasRetryDelay

### clearRetryDelay

### setRetryDelay

Clients should wait at least this long between retrying the same request.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[Google\Protobuf\Duration](https://docs.cloud.google.com/php/docs/reference/protobuf/latest/Google.Protobuf.Duration.html)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-07 UTC."],[],[]] 
