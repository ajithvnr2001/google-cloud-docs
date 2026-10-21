---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse/
title: CollectionResponse \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:14:55.646626+00:00
---

# CollectionResponse  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  CollectionResponse Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.response

## Class CollectionResponse<T>

  * java.lang.Object
  *     * com.google.api.server.spi.response.CollectionResponse<T>



  * * * *

  

        
        public class CollectionResponse<T>
        extends java.lang.Object

Collection response to be returned by an endpoint implementation method that wants to support pagination (and other metadata about returned collection in the future). Endpoint implementation method would do something like this to use it: 

` public CollectionResponse<Greeting> list(@Named("pageToken") String pageToken) { List<Greeting> greetings = new ArrayList<Greeting>(); // use pageToken to fill greetings with next page of items return CollectionResponse.<Greeting>builder() .setItems(greetings) .setNextPageToken("newPageToken") .build(); } `




  *     * ### Nested Class Summary

Nested Classes Modifier and Type | Class and Description  
---|---  
`static class ` | `[CollectionResponse.Builder](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html "class in com.google.api.server.spi.response")<[T](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html "type parameter in CollectionResponse.Builder")>` Builder for [`CollectionResponse`](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.html "class in com.google.api.server.spi.response").  
    * ### Constructor Summary

Constructors Modifier | Constructor and Description  
---|---  
`protected ` | `[CollectionResponse](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.html#CollectionResponse-java.util.Collection-java.lang.String-)(java.util.Collection<[T](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.html "type parameter in CollectionResponse")> items, java.lang.String nextPageToken)`  
    * ### Method Summary

All Methods Static Methods Instance Methods Concrete Methods Modifier and Type | Method and Description  
---|---  
`static <T> [CollectionResponse.Builder](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html "class in com.google.api.server.spi.response")<T>` | `[builder](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.html#builder--)()`  
`java.util.Collection<[T](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.html "type parameter in CollectionResponse")>` | `[getItems](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.html#getItems--)()`  
`java.lang.String` | `[getNextPageToken](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.html#getNextPageToken--)()`  
      * ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`



  *     * ### Constructor Detail

      * #### CollectionResponse
            
            protected CollectionResponse(java.util.Collection<[T](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.html "type parameter in CollectionResponse")> items,
                                         java.lang.String nextPageToken)

    * ### Method Detail

      * #### builder
            
            public static <T> [CollectionResponse.Builder](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.Builder.html "class in com.google.api.server.spi.response")<T> builder()

      * #### getNextPageToken
            
            public java.lang.String getNextPageToken()

      * #### getItems
            
            public java.util.Collection<[T](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/CollectionResponse.html "type parameter in CollectionResponse")> getItems()




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
