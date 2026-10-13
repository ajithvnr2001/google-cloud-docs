---
url: https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1beta.MetricCompatibility
title: Google Analytics Data V1beta Client - Class MetricCompatibility (0.28.0) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:49:51.682067+00:00
---

# Google Analytics Data V1beta Client - Class MetricCompatibility (0.28.0)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1beta.MetricCompatibility

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Analytics Data V1beta Client - Class MetricCompatibility (0.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.28.0 (latest)  0.24.0  0.23.3  0.22.3  0.21.1  0.20.1  0.19.0  0.18.0  0.17.1  0.16.4  0.14.0  0.13.0  0.12.0  0.11.2  0.10.1  0.9.5 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Analytics Data V1beta Client class MetricCompatibility.

The compatibility for a single metric.

Generated from protobuf message `google.analytics.data.v1beta.MetricCompatibility`

## Namespace

Google \ Analytics \ Data \ V1beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ metric_metadata` |  `[MetricMetadata](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1beta.MetricMetadata)`   
The metric metadata contains the API name for this compatibility information. The metric metadata also contains other helpful information like the UI name and description.  
`↳ compatibility` |  `int`   
The compatibility of this metric. If the compatibility is COMPATIBLE, this metric can be successfully added to the report.  
  
### getMetricMetadata

The metric metadata contains the API name for this compatibility information. The metric metadata also contains other helpful information like the UI name and description.

**Returns**  
---  
**Type** | **Description**  
`[MetricMetadata](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1beta.MetricMetadata)|null` |   
  
### hasMetricMetadata

### clearMetricMetadata

### setMetricMetadata

The metric metadata contains the API name for this compatibility information. The metric metadata also contains other helpful information like the UI name and description.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[MetricMetadata](https://docs.cloud.google.com/php/docs/reference/analytics-data/latest/V1beta.MetricMetadata)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCompatibility

The compatibility of this metric. If the compatibility is COMPATIBLE, this metric can be successfully added to the report.

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### hasCompatibility

### clearCompatibility

### setCompatibility

The compatibility of this metric. If the compatibility is COMPATIBLE, this metric can be successfully added to the report.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `int`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
