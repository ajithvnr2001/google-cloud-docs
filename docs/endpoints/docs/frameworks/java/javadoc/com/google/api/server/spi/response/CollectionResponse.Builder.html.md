---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html
title: CollectionResponse.Builder \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:09.533127+00:00
---

# CollectionResponse.Builder  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  CollectionResponse.Builder Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.response

## Class CollectionResponse.Builder<T>

  * java.lang.Object
  *     * com.google.api.server.spi.response.CollectionResponse.Builder<T>



  * Enclosing class:
    [CollectionResponse](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.html "class in com.google.api.server.spi.response")<[T](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.html "type parameter in CollectionResponse")>

* * *

  

        
        public static class CollectionResponse.Builder<T>
        extends java.lang.Object

Builder for [`CollectionResponse`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.html "class in com.google.api.server.spi.response").




  *     * ### Constructor Summary

Constructors Constructor and Description  
---  
`[Builder](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html#Builder--)()`  
    * ### Method Summary

All Methods Instance Methods Concrete Methods Modifier and Type | Method and Description  
---|---  
`[CollectionResponse](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.html "class in com.google.api.server.spi.response")<[T](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html "type parameter in CollectionResponse.Builder")>` | `[build](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html#build--)()`  
`[CollectionResponse.Builder](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html "class in com.google.api.server.spi.response")<[T](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html "type parameter in CollectionResponse.Builder")>` | `[setItems](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html#setItems-java.util.Collection-)(java.util.Collection<[T](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html "type parameter in CollectionResponse.Builder")> items)`  
`[CollectionResponse.Builder](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html "class in com.google.api.server.spi.response")<[T](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html "type parameter in CollectionResponse.Builder")>` | `[setNextPageToken](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html#setNextPageToken-java.lang.String-)(java.lang.String nextPageToken)`  
      * ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`



  *     * ### Constructor Detail

      * #### Builder
            
            public Builder()

    * ### Method Detail

      * #### setItems
            
            public [CollectionResponse.Builder](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html "class in com.google.api.server.spi.response")<[T](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html "type parameter in CollectionResponse.Builder")> setItems(java.util.Collection<[T](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html "type parameter in CollectionResponse.Builder")> items)

      * #### setNextPageToken
            
            public [CollectionResponse.Builder](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html "class in com.google.api.server.spi.response")<[T](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html "type parameter in CollectionResponse.Builder")> setNextPageToken(java.lang.String nextPageToken)

      * #### build
            
            public [CollectionResponse](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.html "class in com.google.api.server.spi.response")<[T](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html "type parameter in CollectionResponse.Builder")> build()




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
