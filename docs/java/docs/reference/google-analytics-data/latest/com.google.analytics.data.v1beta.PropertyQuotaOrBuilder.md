---
url: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuotaOrBuilder
title: Interface PropertyQuotaOrBuilder (0.110.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:11:35.412965+00:00
---

# Interface PropertyQuotaOrBuilder (0.110.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.PropertyQuotaOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PropertyQuotaOrBuilder (0.110.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.110.0 (latest)  0.106.0  0.105.0  0.104.0  0.102.0  0.99.0  0.98.0  0.96.0  0.94.0  0.93.0  0.92.0  0.91.0  0.89.0  0.87.0  0.86.0  0.85.0  0.84.0  0.83.0  0.81.0  0.79.0  0.78.0  0.75.0  0.74.0  0.73.0  0.71.0  0.70.0  0.69.0  0.68.0  0.67.0  0.66.0  0.65.0  0.64.0  0.63.0  0.62.0  0.60.0  0.59.0  0.58.0  0.57.0  0.56.0  0.55.0  0.54.0  0.53.0  0.52.0  0.51.0  0.50.0  0.48.0  0.47.0  0.46.0  0.45.0  0.44.0  0.43.0  0.42.0  0.41.0  0.40.0  0.39.0  0.38.0  0.35.0  0.34.0  0.33.0  0.32.0  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.0 
    
    
    public interface PropertyQuotaOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getConcurrentRequests()
    
    
    public abstract QuotaStatus getConcurrentRequests()

Standard Analytics Properties can send up to 10 concurrent requests; Analytics 360 Properties can use up to 50 concurrent requests.

`.google.analytics.data.v1beta.QuotaStatus concurrent_requests = 3;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)` | The concurrentRequests.  
  
### getConcurrentRequestsOrBuilder()
    
    
    public abstract QuotaStatusOrBuilder getConcurrentRequestsOrBuilder()

Standard Analytics Properties can send up to 10 concurrent requests; Analytics 360 Properties can use up to 50 concurrent requests.

`.google.analytics.data.v1beta.QuotaStatus concurrent_requests = 3;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatusOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatusOrBuilder)` |   
  
### getPotentiallyThresholdedRequestsPerHour()
    
    
    public abstract QuotaStatus getPotentiallyThresholdedRequestsPerHour()

Analytics Properties can send up to 120 requests with potentially thresholded dimensions per hour. In a batch request, each report request is individually counted for this quota if the request contains potentially thresholded dimensions.

`.google.analytics.data.v1beta.QuotaStatus potentially_thresholded_requests_per_hour = 5; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)` | The potentiallyThresholdedRequestsPerHour.  
  
### getPotentiallyThresholdedRequestsPerHourOrBuilder()
    
    
    public abstract QuotaStatusOrBuilder getPotentiallyThresholdedRequestsPerHourOrBuilder()

Analytics Properties can send up to 120 requests with potentially thresholded dimensions per hour. In a batch request, each report request is individually counted for this quota if the request contains potentially thresholded dimensions.

`.google.analytics.data.v1beta.QuotaStatus potentially_thresholded_requests_per_hour = 5; `

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatusOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatusOrBuilder)` |   
  
### getServerErrorsPerProjectPerHour()
    
    
    public abstract QuotaStatus getServerErrorsPerProjectPerHour()

Standard Analytics Properties and cloud project pairs can have up to 10 server errors per hour; Analytics 360 Properties and cloud project pairs can have up to 50 server errors per hour.

`.google.analytics.data.v1beta.QuotaStatus server_errors_per_project_per_hour = 4;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)` | The serverErrorsPerProjectPerHour.  
  
### getServerErrorsPerProjectPerHourOrBuilder()
    
    
    public abstract QuotaStatusOrBuilder getServerErrorsPerProjectPerHourOrBuilder()

Standard Analytics Properties and cloud project pairs can have up to 10 server errors per hour; Analytics 360 Properties and cloud project pairs can have up to 50 server errors per hour.

`.google.analytics.data.v1beta.QuotaStatus server_errors_per_project_per_hour = 4;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatusOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatusOrBuilder)` |   
  
### getTokensPerDay()
    
    
    public abstract QuotaStatus getTokensPerDay()

Standard Analytics Properties can use up to 200,000 tokens per day; Analytics 360 Properties can use 2,000,000 tokens per day. Most requests consume fewer than 10 tokens.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_day = 1;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)` | The tokensPerDay.  
  
### getTokensPerDayOrBuilder()
    
    
    public abstract QuotaStatusOrBuilder getTokensPerDayOrBuilder()

Standard Analytics Properties can use up to 200,000 tokens per day; Analytics 360 Properties can use 2,000,000 tokens per day. Most requests consume fewer than 10 tokens.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_day = 1;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatusOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatusOrBuilder)` |   
  
### getTokensPerHour()
    
    
    public abstract QuotaStatus getTokensPerHour()

Standard Analytics Properties can use up to 40,000 tokens per hour; Analytics 360 Properties can use 400,000 tokens per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_hour = 2;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)` | The tokensPerHour.  
  
### getTokensPerHourOrBuilder()
    
    
    public abstract QuotaStatusOrBuilder getTokensPerHourOrBuilder()

Standard Analytics Properties can use up to 40,000 tokens per hour; Analytics 360 Properties can use 400,000 tokens per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_hour = 2;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatusOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatusOrBuilder)` |   
  
### getTokensPerProjectPerHour()
    
    
    public abstract QuotaStatus getTokensPerProjectPerHour()

Analytics Properties can use up to 35% of their tokens per project per hour. This amounts to standard Analytics Properties can use up to 14,000 tokens per project per hour, and Analytics 360 Properties can use 140,000 tokens per project per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_project_per_hour = 6;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatus](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatus)` | The tokensPerProjectPerHour.  
  
### getTokensPerProjectPerHourOrBuilder()
    
    
    public abstract QuotaStatusOrBuilder getTokensPerProjectPerHourOrBuilder()

Analytics Properties can use up to 35% of their tokens per project per hour. This amounts to standard Analytics Properties can use up to 14,000 tokens per project per hour, and Analytics 360 Properties can use 140,000 tokens per project per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_project_per_hour = 6;`

**Returns**  
---  
**Type** | **Description**  
`[QuotaStatusOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-analytics-data/latest/com.google.analytics.data.v1beta.QuotaStatusOrBuilder)` |   
  
### hasConcurrentRequests()
    
    
    public abstract boolean hasConcurrentRequests()

Standard Analytics Properties can send up to 10 concurrent requests; Analytics 360 Properties can use up to 50 concurrent requests.

`.google.analytics.data.v1beta.QuotaStatus concurrent_requests = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the concurrentRequests field is set.  
  
### hasPotentiallyThresholdedRequestsPerHour()
    
    
    public abstract boolean hasPotentiallyThresholdedRequestsPerHour()

Analytics Properties can send up to 120 requests with potentially thresholded dimensions per hour. In a batch request, each report request is individually counted for this quota if the request contains potentially thresholded dimensions.

`.google.analytics.data.v1beta.QuotaStatus potentially_thresholded_requests_per_hour = 5; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the potentiallyThresholdedRequestsPerHour field is set.  
  
### hasServerErrorsPerProjectPerHour()
    
    
    public abstract boolean hasServerErrorsPerProjectPerHour()

Standard Analytics Properties and cloud project pairs can have up to 10 server errors per hour; Analytics 360 Properties and cloud project pairs can have up to 50 server errors per hour.

`.google.analytics.data.v1beta.QuotaStatus server_errors_per_project_per_hour = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the serverErrorsPerProjectPerHour field is set.  
  
### hasTokensPerDay()
    
    
    public abstract boolean hasTokensPerDay()

Standard Analytics Properties can use up to 200,000 tokens per day; Analytics 360 Properties can use 2,000,000 tokens per day. Most requests consume fewer than 10 tokens.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_day = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tokensPerDay field is set.  
  
### hasTokensPerHour()
    
    
    public abstract boolean hasTokensPerHour()

Standard Analytics Properties can use up to 40,000 tokens per hour; Analytics 360 Properties can use 400,000 tokens per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_hour = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tokensPerHour field is set.  
  
### hasTokensPerProjectPerHour()
    
    
    public abstract boolean hasTokensPerProjectPerHour()

Analytics Properties can use up to 35% of their tokens per project per hour. This amounts to standard Analytics Properties can use up to 14,000 tokens per project per hour, and Analytics 360 Properties can use 140,000 tokens per project per hour. An API request consumes a single number of tokens, and that number is deducted from all of the hourly, daily, and per project hourly quotas.

`.google.analytics.data.v1beta.QuotaStatus tokens_per_project_per_hour = 6;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tokensPerProjectPerHour field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
