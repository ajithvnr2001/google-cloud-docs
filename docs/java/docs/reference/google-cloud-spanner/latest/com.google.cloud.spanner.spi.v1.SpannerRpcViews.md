---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.spi.v1.SpannerRpcViews
title: Class SpannerRpcViews (6.124.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:25:13.371894+00:00
---

# Class SpannerRpcViews (6.124.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.cloud.spanner.spi.v1.SpannerRpcViews

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Class SpannerRpcViews (6.124.0) Stay organized with collections  Save and categorize content based on your preferences. 

6.124.0 (latest)  6.120.0  6.119.0  6.118.0  6.116.0  6.111.1  6.108.0  6.107.0  6.103.0  6.102.1  6.101.1  6.100.0  6.99.0  6.98.1  6.97.1  6.96.1  6.95.1  6.94.0  6.93.0  6.89.0  6.88.0  6.87.0  6.86.0  6.85.0  6.83.0  6.82.0  6.80.1  6.79.0  6.77.0  6.74.1  6.72.0  6.71.0  6.69.0  6.68.0  6.66.0  6.65.1  6.62.0  6.60.0  6.58.0  6.57.0  6.56.0  6.55.0  6.54.0  6.53.0  6.52.1  6.51.0  6.50.1  6.49.0  6.25.1  6.24.0  6.23.4  6.22.0  6.21.2  6.20.0  6.19.1  6.18.0  6.17.4  6.14.1 
    
    
    public class SpannerRpcViews

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > SpannerRpcViews

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

### DATABASE_ID
    
    
    public static final TagKey DATABASE_ID

**Field Value**  
---  
**Type** | **Description**  
`io.opencensus.tags.TagKey` |   
  
### INSTANCE_ID
    
    
    public static final TagKey INSTANCE_ID

**Field Value**  
---  
**Type** | **Description**  
`io.opencensus.tags.TagKey` |   
  
### METHOD
    
    
    public static final TagKey METHOD

TagKeys

**Field Value**  
---  
**Type** | **Description**  
`io.opencensus.tags.TagKey` |   
  
### PROJECT_ID
    
    
    public static final TagKey PROJECT_ID

**Field Value**  
---  
**Type** | **Description**  
`io.opencensus.tags.TagKey` |   
  
### SPANNER_GFE_HEADER_MISSING_COUNT
    
    
    public static final Measure.MeasureLong SPANNER_GFE_HEADER_MISSING_COUNT

Number of responses without the server-timing header.

**Field Value**  
---  
**Type** | **Description**  
`io.opencensus.stats.Measure.MeasureLong` |   
  
### SPANNER_GFE_LATENCY
    
    
    public static final Measure.MeasureLong SPANNER_GFE_LATENCY

GFE t4t7 latency extracted from server-timing header.

**Field Value**  
---  
**Type** | **Description**  
`io.opencensus.stats.Measure.MeasureLong` |   
  
### viewManager
    
    
    public static ViewManager viewManager

**Field Value**  
---  
**Type** | **Description**  
`io.opencensus.stats.ViewManager` |   
  
## Static Methods 

### registerGfeHeaderMissingCountView() (deprecated)
    
    
    public static void registerGfeHeaderMissingCountView()

**Obsolete**

_The OpenCensus project is deprecated. Use OpenTelemetry to get gfe_latency and gfe_header_missing_count metrics._

This feature is stable for usage in this major version, but may be deprecated in a future release.

**Deprecated.** _The OpenCensus project is deprecated. Use OpenTelemetry to get gfe_latency and gfe_header_missing_count metrics._

Register GFE Header Missing Count view. gfe_header_missing_count is a counter of the number of RPC responses without a server-timing header.

### registerGfeLatencyAndHeaderMissingCountViews() (deprecated)
    
    
    public static void registerGfeLatencyAndHeaderMissingCountViews()

**Obsolete**

_The OpenCensus project is deprecated. Use OpenTelemetry to get gfe_latency and gfe_header_missing_count metrics._

This feature is stable for usage in this major version, but may be deprecated in a future release.

**Deprecated.** _The OpenCensus project is deprecated. Use OpenTelemetry to get gfe_latency and gfe_header_missing_count metrics._

Register views for GFE metrics, including gfe_latency and gfe_header_missing_count. gfe_latency measures the latency between Google's network receives an RPC and reads back the first byte of the response. gfe_header_missing_count is a counter of the number of RPC responses without a server-timing header.

### registerGfeLatencyView() (deprecated)
    
    
    public static void registerGfeLatencyView()

**Obsolete**

_The OpenCensus project is deprecated. Use OpenTelemetry to get gfe_latency and gfe_header_missing_count metrics._

This feature is stable for usage in this major version, but may be deprecated in a future release.

**Deprecated.** _The OpenCensus project is deprecated. Use OpenTelemetry to get gfe_latency and gfe_header_missing_count metrics._

Register GFE Latency view. gfe_latency measures the latency between Google's network receives an RPC and reads back the first byte of the response.

## Constructors 

### SpannerRpcViews()
    
    
    public SpannerRpcViews()

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
