---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiReference/
title: ApiReference \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:05.361737+00:00
---

# ApiReference  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiReference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  ApiReference Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.config

## Annotation Type ApiReference

  * * * *

  

        
        @Retention(value=RUNTIME)
         @Target(value=TYPE)
        public @interface ApiReference

Annotation to specify that the annotated class should use the same [`Api`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html "annotation in com.google.api.server.spi.config") configuration information as the referenced class. This referenced configuration is used instead of any configuration inherited from [`Api`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html "annotation in com.google.api.server.spi.config") annotations or other `ApiReference` annotations on super classes. If a single class is annotated with both [`Api`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html "annotation in com.google.api.server.spi.config") and [`ApiReference`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiReference.html "annotation in com.google.api.server.spi.config") annotations, configuration is first retrieved using the [`ApiReference`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiReference.html "annotation in com.google.api.server.spi.config") annotation and is then overridden with configuration from the [`Api`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html "annotation in com.google.api.server.spi.config") annotation.




  *     * ### Required Element Summary

Required Elements Modifier and Type | Required Element and Description  
---|---  
`java.lang.Class<?>` | `[value](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiReference.html#value--)` The class to which this ApiReference annotation will act as a reference.  



  *     * ### Element Detail

      * #### value
            
            public abstract java.lang.Class<?> value

The class to which this ApiReference annotation will act as a reference. The referenced class or an inherited superclass of the referenced class must have API configuration provided from an [`Api`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/Api.html "annotation in com.google.api.server.spi.config") annotation or another [`ApiReference`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiReference.html "annotation in com.google.api.server.spi.config") annotation.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
