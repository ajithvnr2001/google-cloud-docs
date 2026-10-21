---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethodCacheControl/
title: ApiMethodCacheControl \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:09:25.193835+00:00
---

# ApiMethodCacheControl  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethodCacheControl/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  ApiMethodCacheControl Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.config

## Annotation Type ApiMethodCacheControl

  * * * *

Deprecated.

ApiMethodCacheControl is deprecated and will be removed in a future version of Cloud Endpoints.

  

        
        @Retention(value=RUNTIME)
         @Target(value=METHOD)
         @Deprecated
        public @interface ApiMethodCacheControl

Annotation for configuration of API method cache control.




  *     * ### Optional Element Summary

Optional Elements Modifier and Type | Optional Element and Description  
---|---  
`int` | `[maxAge](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethodCacheControl.html#maxAge--)` Deprecated. Overrides the maximum age to cache responses from this method.  
`boolean` | `[noCache](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiMethodCacheControl.html#noCache--)` Deprecated. Disables caching of this method.  



  *     * ### Element Detail

      * #### noCache
            
            public abstract boolean noCache

Deprecated.

Disables caching of this method. The default value is true, so merely adding this annotation to your method config will disable caching for that method, unless you set this field to `false`.

Default:
    true
    *       * #### maxAge
            
            public abstract int maxAge

Deprecated.

Overrides the maximum age to cache responses from this method.

Default:
    0



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
