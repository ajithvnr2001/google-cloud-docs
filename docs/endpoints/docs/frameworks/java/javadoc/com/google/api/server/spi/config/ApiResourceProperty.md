---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiResourceProperty/
title: ApiResourceProperty \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:51:21.723364+00:00
---

# ApiResourceProperty  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiResourceProperty/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  ApiResourceProperty Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.config

## Annotation Type ApiResourceProperty

  * * * *

  

        
        @Retention(value=RUNTIME)
        public @interface ApiResourceProperty

Annotation for configuring bean properties for API resources. 

This annotation can be used on all parts of the definition of a property: the field, the accessor (getter), or the mutator (setter). However, it should only be used on one of the three; behavior for multiple annotations on one property is not defined.




  *     * ### Optional Element Summary

Optional Elements Modifier and Type | Optional Element and Description  
---|---  
`[AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config")` | `[ignored](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiResourceProperty.html#ignored--)` Whether or not the property represented by the annotated getter, setter or field should be ignored for the API.  
`java.lang.String` | `[name](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/ApiResourceProperty.html#name--)` The name that the property represented by the annotated getter, setter, or field should appear as in the API.  



  *     * ### Element Detail

      * #### name
            
            public abstract java.lang.String name

The name that the property represented by the annotated getter, setter, or field should appear as in the API.

Default:
    ""
    *       * #### ignored
            
            public abstract [AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config") ignored

Whether or not the property represented by the annotated getter, setter or field should be ignored for the API.

Default:
    com.google.api.server.spi.config.AnnotationBoolean.UNSPECIFIED



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
