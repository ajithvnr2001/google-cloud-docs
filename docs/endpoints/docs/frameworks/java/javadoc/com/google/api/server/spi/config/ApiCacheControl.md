---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiCacheControl/
title: ApiCacheControl (endpoints-framework 2.0.0-beta.5 API) \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:03.725976+00:00
---

# ApiCacheControl (endpoints-framework 2.0.0-beta.5 API)  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiCacheControl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  ApiCacheControl (endpoints-framework 2.0.0-beta.5 API) Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.config

## Annotation Type ApiCacheControl

  * * * *

  

        
        @Retention(value=RUNTIME)
         @Target(value=TYPE)
        public @interface ApiCacheControl

Annotation for API cache control configuration. Note that the API frontend itself may act as a caching proxy.




  *     * ### Optional Element Summary

Optional Elements Modifier and Type | Optional Element and Description  
---|---  
`int` | `[maxAge](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiCacheControl.html#maxAge--)` The maximum age that results may be cached.  
`java.lang.String` | `[type](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiCacheControl.html#type--)` The cache control type.  



  *     * ### Element Detail

      * #### type
            
            public abstract java.lang.String type

The cache control type. Defaults to no-cache.

Default:
    ""
    *       * #### maxAge
            
            public abstract int maxAge

The maximum age that results may be cached. If unspecified, defaults to 0.

Default:
    -2147483648



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
