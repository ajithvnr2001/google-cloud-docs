---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimitRule/
title: ApiFrontendLimitRule \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:55:32.768089+00:00
---

# ApiFrontendLimitRule  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimitRule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  ApiFrontendLimitRule Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.config

## Annotation Type ApiFrontendLimitRule

  * * * *

  

        
        @Retention(value=RUNTIME)
         @Target(value=TYPE)
        public @interface ApiFrontendLimitRule

Annotation for configuration of API quota frontend limit rules.




  *     * ### Optional Element Summary

Optional Elements Modifier and Type | Optional Element and Description  
---|---  
`java.lang.String` | `[analyticsId](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimitRule.html#analyticsId--)` Logs traffic for this rule under a specific analytics project id.  
`int` | `[daily](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimitRule.html#daily--)` The total queries per day to allow for this rule.  
`java.lang.String` | `[match](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimitRule.html#match--)` The matching rule that defines this segment.  
`int` | `[qps](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimitRule.html#qps--)` The total queries per second to allow for this rule.  
`int` | `[userQps](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimitRule.html#userQps--)` The per-user queries per second to allow for this rule.  



  *     * ### Element Detail

      * #### match
            
            public abstract java.lang.String match

The matching rule that defines this segment. You can define the match in terms of headers or query parameters. For example "Referer=.*\\.example\\.com" will define a match for traffic from the example.com site. The first matching rule will be used to define the limits for a particular request.

Default:
    ""
    *       * #### qps
            
            public abstract int qps

The total queries per second to allow for this rule. The default is unlimited.

Default:
    -1
    *       * #### userQps
            
            public abstract int userQps

The per-user queries per second to allow for this rule. The default is unlimited.

Default:
    -1
    *       * #### daily
            
            public abstract int daily

The total queries per day to allow for this rule. The default is unlimited.

Default:
    -1
    *       * #### analyticsId
            
            public abstract java.lang.String analyticsId

Logs traffic for this rule under a specific analytics project id.

Default:
    ""



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
