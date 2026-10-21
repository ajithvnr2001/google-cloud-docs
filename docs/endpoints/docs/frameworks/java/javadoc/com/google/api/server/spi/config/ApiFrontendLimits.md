---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimits/
title: ApiFrontendLimits \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:03.831807+00:00
---

# ApiFrontendLimits  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  ApiFrontendLimits Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.config

## Annotation Type ApiFrontendLimits

  * * * *

  

        
        @Retention(value=RUNTIME)
         @Target(value=TYPE)
        public @interface ApiFrontendLimits

Annotation for configuration of API quota frontend limits. These are the limits applied to unregistered users of your API.




  *     * ### Optional Element Summary

Optional Elements Modifier and Type | Optional Element and Description  
---|---  
`[ApiFrontendLimitRule](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimitRule.html "annotation in com.google.api.server.spi.config")[]` | `[rules](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimits.html#rules--)` Sets custom rules for unregistered traffic to your API.  
`int` | `[unregisteredDaily](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimits.html#unregisteredDaily--)` Sets the maximum number of requests per day for unregistered access to your API.  
`int` | `[unregisteredQps](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimits.html#unregisteredQps--)` Sets the maximum number of queries per second across all unregistered access to your API.  
`int` | `[unregisteredUserQps](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimits.html#unregisteredUserQps--)` Sets the number of queries per second an unregistered user can make against your API.  



  *     * ### Element Detail

      * #### unregisteredUserQps
            
            public abstract int unregisteredUserQps

Sets the number of queries per second an unregistered user can make against your API. The default is unlimited. If unauthenticated, each IP address is treated as a distinct user.

Default:
    -2147483648
    *       * #### unregisteredQps
            
            public abstract int unregisteredQps

Sets the maximum number of queries per second across all unregistered access to your API. The default is unlimited.

Default:
    -2147483648
    *       * #### unregisteredDaily
            
            public abstract int unregisteredDaily

Sets the maximum number of requests per day for unregistered access to your API. The default is unlimited.

Default:
    -2147483648
    *       * #### rules
            
            public abstract [ApiFrontendLimitRule](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimitRule.html "annotation in com.google.api.server.spi.config")[] rules

Sets custom rules for unregistered traffic to your API. See [`ApiFrontendLimitRule`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiFrontendLimitRule.html "annotation in com.google.api.server.spi.config") for details.

Default:
    {}



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
