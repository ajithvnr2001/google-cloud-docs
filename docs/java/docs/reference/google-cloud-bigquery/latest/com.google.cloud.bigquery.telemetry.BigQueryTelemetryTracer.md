---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.telemetry.BigQueryTelemetryTracer
title: Class BigQueryTelemetryTracer (2.73.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:05:29.349746+00:00
---

# Class BigQueryTelemetryTracer (2.73.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquery/latest/com.google.cloud.bigquery.telemetry.BigQueryTelemetryTracer

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class BigQueryTelemetryTracer (2.73.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.73.0 (latest)  2.69.0  2.68.0  2.67.0  2.65.0  2.62.0  2.61.0  2.60.0  2.59.0  2.58.0  2.57.2  2.56.0  2.55.3  2.54.2  2.53.0  2.52.0  2.51.0  2.50.1  2.49.0  2.48.1  2.47.0  2.46.0  2.45.0  2.44.0  2.43.3  2.42.3  2.41.0  2.40.3  2.39.1  2.38.2  2.37.2  2.36.0  2.35.0  2.34.2  2.33.2 
    
    
    public final class BigQueryTelemetryTracer

BigQuery Telemetry class that stores generic telemetry attributes and values

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > BigQueryTelemetryTracer

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

## Static Fields 

### BQ_GCP_CLIENT_ARTIFACT
    
    
    public static final String BQ_GCP_CLIENT_ARTIFACT

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### BQ_GCP_CLIENT_REPO
    
    
    public static final String BQ_GCP_CLIENT_REPO

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### BQ_GCP_CLIENT_SERVICE
    
    
    public static final String BQ_GCP_CLIENT_SERVICE

**Field Value**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` |   
  
### ERROR_TYPE
    
    
    public static final AttributeKey<String> ERROR_TYPE

**Field Value**  
---  
**Type** | **Description**  
`io.opentelemetry.api.common.AttributeKey<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### EXCEPTION_TYPE
    
    
    public static final AttributeKey<String> EXCEPTION_TYPE

**Field Value**  
---  
**Type** | **Description**  
`io.opentelemetry.api.common.AttributeKey<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### GCP_CLIENT_ARTIFACT
    
    
    public static final AttributeKey<String> GCP_CLIENT_ARTIFACT

**Field Value**  
---  
**Type** | **Description**  
`io.opentelemetry.api.common.AttributeKey<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### GCP_CLIENT_REPO
    
    
    public static final AttributeKey<String> GCP_CLIENT_REPO

**Field Value**  
---  
**Type** | **Description**  
`io.opentelemetry.api.common.AttributeKey<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### GCP_CLIENT_SERVICE
    
    
    public static final AttributeKey<String> GCP_CLIENT_SERVICE

**Field Value**  
---  
**Type** | **Description**  
`io.opentelemetry.api.common.AttributeKey<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### GCP_CLIENT_VERSION
    
    
    public static final AttributeKey<String> GCP_CLIENT_VERSION

**Field Value**  
---  
**Type** | **Description**  
`io.opentelemetry.api.common.AttributeKey<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### GCP_RESOURCE_DESTINATION_ID
    
    
    public static final AttributeKey<String> GCP_RESOURCE_DESTINATION_ID

**Field Value**  
---  
**Type** | **Description**  
`io.opentelemetry.api.common.AttributeKey<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### RPC_SYSTEM_NAME
    
    
    public static final AttributeKey<String> RPC_SYSTEM_NAME

**Field Value**  
---  
**Type** | **Description**  
`io.opentelemetry.api.common.AttributeKey<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### STATUS_MESSAGE
    
    
    public static final AttributeKey<String> STATUS_MESSAGE

**Field Value**  
---  
**Type** | **Description**  
`io.opentelemetry.api.common.AttributeKey<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### URL_DOMAIN
    
    
    public static final AttributeKey<String> URL_DOMAIN

**Field Value**  
---  
**Type** | **Description**  
`io.opentelemetry.api.common.AttributeKey<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
### URL_TEMPLATE
    
    
    public static final AttributeKey<String> URL_TEMPLATE

**Field Value**  
---  
**Type** | **Description**  
`io.opentelemetry.api.common.AttributeKey<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` |   
  
## Static Methods 

### addCommonAttributeToSpan(Span span)
    
    
    public static void addCommonAttributeToSpan(Span span)

**Parameter**  
---  
**Name** | **Description**  
`span` | `io.opentelemetry.api.trace.Span`  
  
  
### addExceptionToSpan(Exception e, Span span)
    
    
    public static void addExceptionToSpan(Exception e, Span span)

Adds the following error attributes to trace span: STATUS_MESSAGE: the name of the exception + message if available EXCEPTION_TYPE: full name of exception ex: java.net.UnknownHostException ERROR_TYPE: mapped string based on ErrorTypeUtil#getClientErrorType(Exception)

**Parameters**  
---  
**Name** | **Description**  
`e` | `[Exception](https://docs.oracle.com/javase/8/docs/api/java/lang/Exception.html)`  
  
`span` | `io.opentelemetry.api.trace.Span`  
  
  
### addServerErrorResponseToSpan(GoogleJsonResponseException errorResponse, Span span)
    
    
    public static void addServerErrorResponseToSpan(GoogleJsonResponseException errorResponse, Span span)

Adds the following error attributes to trace span from GoogleJsonResponseException: STATUS_MESSAGE: user readable error message ERROR_TYPE: reason if available otherwise the status code

**Parameters**  
---  
**Name** | **Description**  
`errorResponse` | `com.google.api.client.googleapis.json.GoogleJsonResponseException`  
  
`span` | `io.opentelemetry.api.trace.Span`  
  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
