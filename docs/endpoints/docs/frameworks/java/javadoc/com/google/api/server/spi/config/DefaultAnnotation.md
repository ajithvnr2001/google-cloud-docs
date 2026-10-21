---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/DefaultAnnotation/
title: DefaultAnnotation \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:06.312776+00:00
---

# DefaultAnnotation  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/DefaultAnnotation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  DefaultAnnotation Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.config

## Class DefaultAnnotation

  * java.lang.Object
  *     * com.google.api.server.spi.config.DefaultAnnotation



  * * * *

  

        
        public class DefaultAnnotation
        extends java.lang.Object

Class used for creation of a default instance of an annotation.




  *     * ### Constructor Summary

Constructors Constructor and Description  
---  
`[DefaultAnnotation](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/DefaultAnnotation.html#DefaultAnnotation--)()`  
    * ### Method Summary

All Methods Static Methods Concrete Methods Modifier and Type | Method and Description  
---|---  
`static <A extends java.lang.annotation.Annotation>  
A` | `[of](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/DefaultAnnotation.html#of-java.lang.Class-)(java.lang.Class<A> annotation)` Creates an instance of an annotation with all properties set to their default values.  
      * ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`



  *     * ### Constructor Detail

      * #### DefaultAnnotation
            
            public DefaultAnnotation()

    * ### Method Detail

      * #### of
            
            public static <A extends java.lang.annotation.Annotation> A of(java.lang.Class<A> annotation)

Creates an instance of an annotation with all properties set to their default values.

Parameters:
    `annotation` \- Class of annotation to create default instance for



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
