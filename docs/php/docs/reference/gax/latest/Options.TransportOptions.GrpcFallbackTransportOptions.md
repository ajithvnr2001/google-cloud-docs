---
url: https://docs.cloud.google.com/php/docs/reference/gax/latest/Options.TransportOptions.GrpcFallbackTransportOptions
title: Google API Core Client - Class GrpcFallbackTransportOptions (1.51.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:29:49.270387+00:00
---

# Google API Core Client - Class GrpcFallbackTransportOptions (1.51.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/gax/latest/Options.TransportOptions.GrpcFallbackTransportOptions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google API Core Client - Class GrpcFallbackTransportOptions (1.51.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.51.0 (latest)  1.46.0  1.43.0  1.42.5  1.40.0  1.38.2  1.36.1  1.35.1 

Reference documentation and code samples for the Google API Core Client class GrpcFallbackTransportOptions.

The GrpcFallbackTransportOptions class provides typing to the associative array of options used to configure [Google\ApiCore\Transport\GrpcFallbackTransport](https://docs.cloud.google.com/php/docs/reference/gax/latest/Transport.GrpcFallbackTransport).

## Namespace

Google \ ApiCore \ Options \ TransportOptions

## Implements

\ArrayAccess

[OptionsInterface](https://docs.cloud.google.com/php/docs/reference/gax/latest/Options.OptionsInterface)

## Methods 

### __construct

**Parameters**  
---  
**Name** | **Description**  
`options` |  `array`   
Config options used to construct the gRPC Fallback transport.  
`↳ clientCertSource` |  `callable`   
A callable which returns the client cert as a string.  
`↳ httpHandler` |  `callable`   
A handler used to deliver PSR-7 requests.  
`↳ A` |  `null|false|LoggerInterface `   
PSR-3 logger interface instance.  
  
### setHttpHandler

**Parameter**  
---  
**Name** | **Description**  
`httpHandler` |  `?callable`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### setClientCertSource

**Parameter**  
---  
**Name** | **Description**  
`clientCertSource` |  `?callable`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### setLogger

**Parameter**  
---  
**Name** | **Description**  
`logger` |  `null|false|Psr\Log\LoggerInterface`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
