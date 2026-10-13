---
url: https://docs.cloud.google.com/php/docs/reference/cloud-trace/latest/Trace/
title: Stackdriver Trace Client - Class Trace (1.9.5) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:54:22.253469+00:00
---

# Stackdriver Trace Client - Class Trace (1.9.5)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-trace/latest/Trace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Stackdriver Trace Client - Class Trace (1.9.5) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.5 (latest)  2.0.0  1.9.5  1.8.10  1.7.0  1.6.5  1.5.3  1.4.11 

Reference documentation and code samples for the Stackdriver Trace Client class Trace.

This plain PHP class represents a Trace resource. The model currently has no backing API model and is identified by its traceId.

Example:
    
    
    use Google\Cloud\Trace\TraceClient;
    
    $traceClient = new TraceClient();
    
    $trace = $traceClient->trace();
    

## Namespace

Google \ Cloud \ Trace

## Methods 

### __construct

Instantiate a new Trace instance.

**Parameters**  
---  
**Name** | **Description**  
`projectId` |  `string`   
The id of the project this trace belongs to.  
`traceId` |  `string`   
[optional] The id of the trace. If not provided, one will be generated automatically for you.  
`spans` |  `array`   
[optional] Array of Span constructor arguments. See [Span::__construct()](https://docs.cloud.google.com/php/docs/reference/cloud-trace/latest/Span#_Google_Cloud_Trace_Span____construct__) for configuration details.  
  
### traceId

Retrieves the trace's id.

Example:
    
    
    echo $trace->traceId();
    

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### info

Returns a serializable array representing this trace.

**Returns**  
---  
**Type** | **Description**  
`array` |   
  
### spans

Retrieves the spans for this trace.

Example:
    
    
    $spans = $trace->spans();
    

**Returns**  
---  
**Type** | **Description**  
`array<[Span](https://docs.cloud.google.com/php/docs/reference/cloud-trace/latest/Span)>` |   
  
### span

Create an instance of [Span](https://docs.cloud.google.com/php/docs/reference/cloud-trace/latest/Span)

Example:
    
    
    $span = $trace->span(['name' => 'newSpan']);
    

**Parameter**  
---  
**Name** | **Description**  
`options` |  `array`   
[optional] See [Span::__construct()](https://docs.cloud.google.com/php/docs/reference/cloud-trace/latest/Span#_Google_Cloud_Trace_Span____construct__) for configuration details.  
**Returns**  
---  
**Type** | **Description**  
`[Span](https://docs.cloud.google.com/php/docs/reference/cloud-trace/latest/Span)` |   
  
### setSpans

Set the spans for this trace.

Example:
    
    
    $trace->setSpans([$span1, $span2]);
    

**Parameter**  
---  
**Name** | **Description**  
`spans` |  `array<[Span](https://docs.cloud.google.com/php/docs/reference/cloud-trace/latest/Span)>`   
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
