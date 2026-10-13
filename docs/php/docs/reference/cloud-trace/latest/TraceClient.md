---
url: https://docs.cloud.google.com/php/docs/reference/cloud-trace/latest/TraceClient/
title: Stackdriver Trace Client - Class TraceClient (1.9.5) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:02.959982+00:00
---

# Stackdriver Trace Client - Class TraceClient (1.9.5)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-trace/latest/TraceClient/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Stackdriver Trace Client - Class TraceClient (1.9.5) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.5 (latest)  2.0.0  1.9.5  1.8.10  1.7.0  1.6.5  1.5.3  1.4.11 

Reference documentation and code samples for the Stackdriver Trace Client class TraceClient.

Google Stackdriver Trace allows you to collect latency data from your applications and display it in the Google Cloud Platform Console.

Find more information at [Stackdriver Trace API docs](https://cloud.google.com/trace/docs/).

Example:
    
    
    use Google\Cloud\Trace\TraceClient;
    
    $trace = new TraceClient();
    

## Namespace

Google \ Cloud \ Trace

## Methods 

### __construct

Create a Trace client.

**Parameters**  
---  
**Name** | **Description**  
`config` |  `array`   
Configuration options.  
`↳ apiEndpoint` |  `string`   
A hostname with optional port to use in place of the service's default endpoint.  
`↳ projectId` |  `string`   
The project ID from the Google Developer's Console.  
`↳ authCache` |  `CacheItemPoolInterface`   
A cache used storing access tokens. **Defaults to** a simple in memory implementation.  
`↳ authCacheOptions` |  `array`   
Cache configuration options.  
`↳ authHttpHandler` |  `callable`   
A handler used to deliver Psr7 requests specifically for authentication.  
`↳ credentialsFetcher` |  `FetchAuthTokenInterface`   
A credentials fetcher instance.  
`↳ keyFile` |  `array`   
[DEPRECATED] This option is being deprecated because of a potential security risk. This option does not validate the credential configuration. The security risk occurs when a credential configuration is accepted from a source that is not under your control and used without validation on your side. If you know that you will be loading credential configurations of a specific type, it is recommended to create the credentials directly and configure them using the `credentialsFetcher` option instead. `use Google\Auth\Credentials\ServiceAccountCredentials; $credentialsFetcher = new ServiceAccountCredentials($scopes, $json); $creds = new TraceClient(['credentialsFetcher' => $creds]);` This will ensure that an unexpected credential type with potential for malicious intent is not loaded unintentionally. You might still have to do validation for certain credential types. If you are loading your credential configuration from an untrusted source and have not mitigated the risks (e.g. by validating the configuration yourself), make these changes as soon as possible to prevent security risks to your environment. Regardless of the method used, it is always your responsibility to validate configurations received from external sources. @see <https://cloud.google.com/docs/authentication/external/externally-sourced-credentials>  
`↳ keyFilePath` |  `string`   
[DEPRECATED] This option is being deprecated because of a potential security risk. This option does not validate the credential configuration. The security risk occurs when a credential configuration is accepted from a source that is not under your control and used without validation on your side. If you know that you will be loading credential configurations of a specific type, it is recommended to create the credentials directly and configure them using the `credentialsFetcher` option instead. `use Google\Auth\Credentials\ServiceAccountCredentials; $credentialsFetcher = new ServiceAccountCredentials($scopes, $json); $creds = new TraceClient(['credentialsFetcher' => $creds]);` This will ensure that an unexpected credential type with potential for malicious intent is not loaded unintentionally. You might still have to do validation for certain credential types. If you are loading your credential configuration from an untrusted source and have not mitigated the risks (e.g. by validating the configuration yourself), make these changes as soon as possible to prevent security risks to your environment. Regardless of the method used, it is always your responsibility to validate configurations received from external sources. @see <https://cloud.google.com/docs/authentication/external/externally-sourced-credentials>  
`↳ requestTimeout` |  `float`   
Seconds to wait before timing out the request. **Defaults to** `0` with REST and `60` with gRPC.  
`↳ retries` |  `int`   
Number of retries for a failed request. **Defaults to** `3`.  
`↳ scopes` |  `array`   
Scopes to be used for the request.  
`↳ quotaProject` |  `string`   
Specifies a user project to bill for access charges associated with the request.  
  
### insert

See also:

  * [Project patchTraces API documentation.](https://cloud.google.com/trace/docs/reference/v1/rest/v1/projects/patchTraces)



**Parameters**  
---  
**Name** | **Description**  
`trace` |  `[Trace](https://docs.cloud.google.com/php/docs/reference/cloud-trace/latest/Trace)`   
The trace log to send.  
`options` |  `array`   
[optional] Configuration Options  
**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### insertBatch

See also:

  * [Project patchTraces API documentation.](https://cloud.google.com/trace/docs/reference/v1/rest/v1/projects/patchTraces)



**Parameters**  
---  
**Name** | **Description**  
`traces` |  `array<[Trace](https://docs.cloud.google.com/php/docs/reference/cloud-trace/latest/Trace)>`   
The trace logs to send.  
`options` |  `array`   
[optional] Configuration Options  
**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### trace

Lazily find or instantiates a trace. There are no network requests made at this point. To see the operations that can be performed on a trace please see [Trace](https://docs.cloud.google.com/php/docs/reference/cloud-trace/latest/Trace). If no traceId is provided, one will be generated for you.

Example:
    
    
    // Create a trace with a generated traceId
    $trace = $traceClient->trace();
    
    
    
    // Create a trace with a specific traceId
    $trace = $traceClient->trace('1234abcd');
    

**Parameter**  
---  
**Name** | **Description**  
`traceId` |  `string`   
[optional] The trace id of the trace to reference.  
**Returns**  
---  
**Type** | **Description**  
`[Trace](https://docs.cloud.google.com/php/docs/reference/cloud-trace/latest/Trace)` |   
  
## Constants 

### VERSION
    
    
    Value: '1.9.5'

### FULL_CONTROL_SCOPE
    
    
    Value: 'https://www.googleapis.com/auth/cloud-platform'

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
