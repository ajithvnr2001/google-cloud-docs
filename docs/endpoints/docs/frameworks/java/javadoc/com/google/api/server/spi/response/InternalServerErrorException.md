---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/InternalServerErrorException/
title: InternalServerErrorException \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:06.669194+00:00
---

# InternalServerErrorException  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/InternalServerErrorException/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  InternalServerErrorException Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.response

## Class InternalServerErrorException

  * java.lang.Object
  *     * ServiceException
    *       * com.google.api.server.spi.response.InternalServerErrorException



  * * * *

  

        
        public class InternalServerErrorException
        extends ServiceException

Internal server exception that is mapped to a 500 response.




  *     * ### Constructor Summary

Constructors Constructor and Description  
---  
`[InternalServerErrorException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/InternalServerErrorException.html#InternalServerErrorException-java.lang.String-)(java.lang.String message)`  
`[InternalServerErrorException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/InternalServerErrorException.html#InternalServerErrorException-java.lang.String-java.lang.String-)(java.lang.String statusMessage, java.lang.String reason)`  
`[InternalServerErrorException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/InternalServerErrorException.html#InternalServerErrorException-java.lang.String-java.lang.String-java.lang.String-)(java.lang.String statusMessage, java.lang.String reason, java.lang.String domain)`  
`[InternalServerErrorException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/InternalServerErrorException.html#InternalServerErrorException-java.lang.String-java.lang.String-java.lang.String-java.lang.Throwable-)(java.lang.String statusMessage, java.lang.String reason, java.lang.String domain, java.lang.Throwable cause)`  
`[InternalServerErrorException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/InternalServerErrorException.html#InternalServerErrorException-java.lang.String-java.lang.String-java.lang.Throwable-)(java.lang.String statusMessage, java.lang.String reason, java.lang.Throwable cause)`  
`[InternalServerErrorException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/InternalServerErrorException.html#InternalServerErrorException-java.lang.String-java.lang.Throwable-)(java.lang.String message, java.lang.Throwable cause)`  
`[InternalServerErrorException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/InternalServerErrorException.html#InternalServerErrorException-java.lang.Throwable-)(java.lang.Throwable cause)`  
    * ### Method Summary

      * ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`



  *     * ### Constructor Detail

      * #### InternalServerErrorException
            
            public InternalServerErrorException(java.lang.String message)

      * #### InternalServerErrorException
            
            public InternalServerErrorException(java.lang.Throwable cause)

      * #### InternalServerErrorException
            
            public InternalServerErrorException(java.lang.String message,
                                                java.lang.Throwable cause)

      * #### InternalServerErrorException
            
            public InternalServerErrorException(java.lang.String statusMessage,
                                                java.lang.String reason)

      * #### InternalServerErrorException
            
            public InternalServerErrorException(java.lang.String statusMessage,
                                                java.lang.String reason,
                                                java.lang.Throwable cause)

      * #### InternalServerErrorException
            
            public InternalServerErrorException(java.lang.String statusMessage,
                                                java.lang.String reason,
                                                java.lang.String domain)

      * #### InternalServerErrorException
            
            public InternalServerErrorException(java.lang.String statusMessage,
                                                java.lang.String reason,
                                                java.lang.String domain,
                                                java.lang.Throwable cause)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
