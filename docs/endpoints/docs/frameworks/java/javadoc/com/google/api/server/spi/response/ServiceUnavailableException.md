---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/ServiceUnavailableException/
title: ServiceUnavailableException \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:07.326143+00:00
---

# ServiceUnavailableException  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/ServiceUnavailableException/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  ServiceUnavailableException Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.response

## Class ServiceUnavailableException

  * java.lang.Object
  *     * ServiceException
    *       * com.google.api.server.spi.response.ServiceUnavailableException



  * * * *

  

        
        public class ServiceUnavailableException
        extends ServiceException

Service Unavailable response for the API, mapped to a HTTP 503 response.




  *     * ### Constructor Summary

Constructors Constructor and Description  
---  
`[ServiceUnavailableException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/ServiceUnavailableException.html#ServiceUnavailableException-java.lang.String-)(java.lang.String message)`  
`[ServiceUnavailableException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/ServiceUnavailableException.html#ServiceUnavailableException-java.lang.String-java.lang.String-)(java.lang.String statusMessage, java.lang.String reason)`  
`[ServiceUnavailableException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/ServiceUnavailableException.html#ServiceUnavailableException-java.lang.String-java.lang.String-java.lang.String-)(java.lang.String statusMessage, java.lang.String reason, java.lang.String domain)`  
`[ServiceUnavailableException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/ServiceUnavailableException.html#ServiceUnavailableException-java.lang.String-java.lang.String-java.lang.String-java.lang.Throwable-)(java.lang.String statusMessage, java.lang.String reason, java.lang.String domain, java.lang.Throwable cause)`  
`[ServiceUnavailableException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/ServiceUnavailableException.html#ServiceUnavailableException-java.lang.String-java.lang.String-java.lang.Throwable-)(java.lang.String statusMessage, java.lang.String reason, java.lang.Throwable cause)`  
`[ServiceUnavailableException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/ServiceUnavailableException.html#ServiceUnavailableException-java.lang.String-java.lang.Throwable-)(java.lang.String message, java.lang.Throwable cause)`  
`[ServiceUnavailableException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/ServiceUnavailableException.html#ServiceUnavailableException-java.lang.Throwable-)(java.lang.Throwable cause)`  
    * ### Method Summary

      * ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`



  *     * ### Constructor Detail

      * #### ServiceUnavailableException
            
            public ServiceUnavailableException(java.lang.String message)

      * #### ServiceUnavailableException
            
            public ServiceUnavailableException(java.lang.Throwable cause)

      * #### ServiceUnavailableException
            
            public ServiceUnavailableException(java.lang.String message,
                                               java.lang.Throwable cause)

      * #### ServiceUnavailableException
            
            public ServiceUnavailableException(java.lang.String statusMessage,
                                               java.lang.String reason)

      * #### ServiceUnavailableException
            
            public ServiceUnavailableException(java.lang.String statusMessage,
                                               java.lang.String reason,
                                               java.lang.Throwable cause)

      * #### ServiceUnavailableException
            
            public ServiceUnavailableException(java.lang.String statusMessage,
                                               java.lang.String reason,
                                               java.lang.String domain)

      * #### ServiceUnavailableException
            
            public ServiceUnavailableException(java.lang.String statusMessage,
                                               java.lang.String reason,
                                               java.lang.String domain,
                                               java.lang.Throwable cause)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
