---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMetricCost/
title: ApiMetricCost \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:04.713854+00:00
---

# ApiMetricCost  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMetricCost/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  ApiMetricCost Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.config

## Annotation Type ApiMetricCost

  * * * *

  

        
        public @interface ApiMetricCost

Metric cost definition for a method.




  *     * ### Required Element Summary

Required Elements Modifier and Type | Required Element and Description  
---|---  
`int` | `[cost](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMetricCost.html#cost--)` The cost charged to the metric.  
`java.lang.String` | `[name](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMetricCost.html#name--)` The metric name, which must be defined using [`ApiLimitMetric`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiLimitMetric.html "annotation in com.google.api.server.spi.config").  



  *     * ### Element Detail

      * #### name
            
            public abstract java.lang.String name

The metric name, which must be defined using [`ApiLimitMetric`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiLimitMetric.html "annotation in com.google.api.server.spi.config").

    *       * #### cost
            
            public abstract int cost

The cost charged to the metric.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
