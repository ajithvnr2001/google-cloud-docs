---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Context.Builder
title: Class Context.Builder (3.40.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:20:57.454598+00:00
---

# Class Context.Builder (3.40.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Context.Builder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class Context.Builder (3.40.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.40.0 (latest)  3.36.0  3.35.0  3.34.0  3.32.0  3.29.0  3.28.0  3.26.0  3.24.0  3.23.10  3.22.6  3.21.4  3.20.7  3.19.0  3.18.0  3.17.2  3.16.2  3.15.17  3.14.9  3.13.7  3.12.1  3.11.10  3.10.7  3.9.0  3.8.0  3.7.6  3.6.4  3.5.3 
    
    
    public static final class Context.Builder

A builder for {@see Context} objects.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > Context.Builder

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Methods 

### build()
    
    
    public Context build()

Creates a {@see Context} object for this builder.

**Returns**  
---  
**Type** | **Description**  
`[Context](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Context)` |   
  
### loadCloudTraceContext(String cloudTrace)
    
    
    public Context.Builder loadCloudTraceContext(String cloudTrace)

Sets the trace id, span id and trace sampled flag values by parsing the string which represents xCloud Trace Context. The Cloud Trace Context is passed as ` x-cloud-trace-context` header (can be in Pascal case format). The string format is ` TRACE_ID/SPAN_ID;o=TRACE_TRUE`. See Also: [Cloud Trace header format.](https://cloud.google.com/trace/docs/trace-context#legacy-http-header)

**Parameter**  
---  
**Name** | **Description**  
`cloudTrace` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Context.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Context.Builder)` |   
  
### loadOpenTelemetryContext()
    
    
    public Context.Builder loadOpenTelemetryContext()

Sets the trace id, span id and trace sampled flag values by parsing detected OpenTelemetry span context. See Also: [OpenTelemetry SpanContext.](https://opentelemetry.io/docs/specs/otel/trace/api/#spancontext)

**Returns**  
---  
**Type** | **Description**  
`[Context.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Context.Builder)` |   
  
### loadW3CTraceParentContext(String traceParent)
    
    
    public Context.Builder loadW3CTraceParentContext(String traceParent)

Sets the trace id, span id and trace sampled flag values by parsing the string which represents the standard W3C trace context propagation header. The context propagation header is passed as `traceparent` header. The method currently supports ONLY version ` "00"`. The string format is `00-TRACE_ID-SPAN_ID-FLAGS`. field of the ` version-format` value. See Also: [traceparent header value format](https://www.w3.org/TR/trace-context/#traceparent-header-field-values)

**Parameter**  
---  
**Name** | **Description**  
`traceParent` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Context.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Context.Builder)` |   
  
### setReferer(String referer)
    
    
    public Context.Builder setReferer(String referer)

Sets the referer URL of the request, as defined in HTTP/1.1 Header Field Definitions. See Also: [HTTP/1.1 Header Field Definitions](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html)

**Parameter**  
---  
**Name** | **Description**  
`referer` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Context.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Context.Builder)` |   
  
### setRemoteIp(String remoteIp)
    
    
    public Context.Builder setRemoteIp(String remoteIp)

Sets the IP address (IPv4 or IPv6) of the client that issued the HTTP request. Examples: `192.168.1.1`, `FE80::0202:B3FF:FE1E:8329`.

**Parameter**  
---  
**Name** | **Description**  
`remoteIp` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Context.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Context.Builder)` |   
  
### setRequest(HttpRequest request)
    
    
    public Context.Builder setRequest(HttpRequest request)

Sets the HTTP request.

**Parameter**  
---  
**Name** | **Description**  
`request` | `[HttpRequest](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Context.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Context.Builder)` |   
  
### setRequestMethod(HttpRequest.RequestMethod method)
    
    
    public Context.Builder setRequestMethod(HttpRequest.RequestMethod method)

Sets the HTTP request method.

**Parameter**  
---  
**Name** | **Description**  
`method` | `[HttpRequest.RequestMethod](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.HttpRequest.RequestMethod)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Context.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Context.Builder)` |   
  
### setRequestUrl(String url)
    
    
    public Context.Builder setRequestUrl(String url)

**Parameter**  
---  
**Name** | **Description**  
`url` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Context.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Context.Builder)` |   
  
### setServerIp(String serverIp)
    
    
    public Context.Builder setServerIp(String serverIp)

Sets the IP address (IPv4 or IPv6) of the origin server that the request was sent to. Examples: `192.168.1.1`, `FE80::0202:B3FF:FE1E:8329`.

**Parameter**  
---  
**Name** | **Description**  
`serverIp` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Context.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Context.Builder)` |   
  
### setSpanId(String spanId)
    
    
    public Context.Builder setSpanId(String spanId)

Sets the string as a span id value.

**Parameter**  
---  
**Name** | **Description**  
`spanId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Context.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Context.Builder)` |   
  
### setTraceId(String traceId)
    
    
    public Context.Builder setTraceId(String traceId)

Sets the string as a trace id value.

**Parameter**  
---  
**Name** | **Description**  
`traceId` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Context.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Context.Builder)` |   
  
### setTraceSampled(boolean traceSampled)
    
    
    public Context.Builder setTraceSampled(boolean traceSampled)

Sets the boolean as trace sampled flag.

**Parameter**  
---  
**Name** | **Description**  
`traceSampled` | `[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Context.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloud-logging/latest/com.google.cloud.logging.Context.Builder)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
