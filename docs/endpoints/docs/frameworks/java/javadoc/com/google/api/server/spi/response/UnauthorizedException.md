---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/UnauthorizedException/
title: UnauthorizedException \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:07.548547+00:00
---

# UnauthorizedException  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/UnauthorizedException/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  UnauthorizedException Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.response

## Class UnauthorizedException

  * java.lang.Object
  *     * ServiceException
    *       * com.google.api.server.spi.response.UnauthorizedException



  * * * *

  

        
        public class UnauthorizedException
        extends ServiceException

Unauthorized exception that is mapped to a 401 response.




  *     * ### Field Summary

Fields Modifier and Type | Field and Description  
---|---  
`static java.lang.String` | `[AUTH_SCHEME_BEARER](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/UnauthorizedException.html#AUTH_SCHEME_BEARER)`  
    * ### Constructor Summary

Constructors Constructor and Description  
---  
`[UnauthorizedException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/UnauthorizedException.html#UnauthorizedException-java.lang.String-)(java.lang.String message)`  
`[UnauthorizedException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/UnauthorizedException.html#UnauthorizedException-java.lang.String-java.lang.String-)(java.lang.String statusMessage, java.lang.String reason)`  
`[UnauthorizedException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/UnauthorizedException.html#UnauthorizedException-java.lang.String-java.lang.String-java.util.Map-)(java.lang.String message, java.lang.String authScheme, java.util.Map<java.lang.String,java.lang.String> params)` Creates an UnauthorizedException.  
`[UnauthorizedException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/UnauthorizedException.html#UnauthorizedException-java.lang.String-java.lang.String-java.lang.String-)(java.lang.String statusMessage, java.lang.String reason, java.lang.String domain)`  
`[UnauthorizedException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/UnauthorizedException.html#UnauthorizedException-java.lang.String-java.lang.String-java.lang.String-java.lang.String-java.util.Map-)(java.lang.String message, java.lang.String reason, java.lang.String domain, java.lang.String authScheme, java.util.Map<java.lang.String,java.lang.String> params)`  
`[UnauthorizedException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/UnauthorizedException.html#UnauthorizedException-java.lang.String-java.lang.String-java.lang.String-java.lang.Throwable-)(java.lang.String statusMessage, java.lang.String reason, java.lang.String domain, java.lang.Throwable cause)`  
`[UnauthorizedException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/UnauthorizedException.html#UnauthorizedException-java.lang.String-java.lang.String-java.lang.Throwable-)(java.lang.String statusMessage, java.lang.String reason, java.lang.Throwable cause)`  
`[UnauthorizedException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/UnauthorizedException.html#UnauthorizedException-java.lang.String-java.lang.Throwable-)(java.lang.String message, java.lang.Throwable cause)`  
`[UnauthorizedException](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/UnauthorizedException.html#UnauthorizedException-java.lang.Throwable-)(java.lang.Throwable cause)`  
    * ### Method Summary

All Methods Instance Methods Concrete Methods Modifier and Type | Method and Description  
---|---  
`java.util.Map<java.lang.String,java.lang.String>` | `[getHeaders](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/response/UnauthorizedException.html#getHeaders--)()`  
      * ### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`



  *     * ### Field Detail

      * #### AUTH_SCHEME_BEARER
            
            public static final java.lang.String AUTH_SCHEME_BEARER

See Also:
    [Constant Field Values](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/constant-values.html#com.google.api.server.spi.response.UnauthorizedException.AUTH_SCHEME_BEARER)
    * ### Constructor Detail

      * #### UnauthorizedException
            
            public UnauthorizedException(java.lang.String message)

      * #### UnauthorizedException
            
            public UnauthorizedException(java.lang.Throwable cause)

      * #### UnauthorizedException
            
            public UnauthorizedException(java.lang.String message,
                                         java.lang.Throwable cause)

      * #### UnauthorizedException
            
            public UnauthorizedException(java.lang.String statusMessage,
                                         java.lang.String reason)

      * #### UnauthorizedException
            
            public UnauthorizedException(java.lang.String statusMessage,
                                         java.lang.String reason,
                                         java.lang.Throwable cause)

      * #### UnauthorizedException
            
            public UnauthorizedException(java.lang.String statusMessage,
                                         java.lang.String reason,
                                         java.lang.String domain)

      * #### UnauthorizedException
            
            public UnauthorizedException(java.lang.String statusMessage,
                                         java.lang.String reason,
                                         java.lang.String domain,
                                         java.lang.Throwable cause)

      * #### UnauthorizedException
            
            public UnauthorizedException(java.lang.String message,
                                         java.lang.String authScheme,
                                         java.util.Map<java.lang.String,java.lang.String> params)

Creates an UnauthorizedException.

Parameters:
    `message` \- Error message to return
    `authScheme` \- Auth scheme in the WWW-Authenticate header
    `params` \- Parameters in the WWW-Authenticate header
      * #### UnauthorizedException
            
            public UnauthorizedException(java.lang.String message,
                                         java.lang.String reason,
                                         java.lang.String domain,
                                         java.lang.String authScheme,
                                         java.util.Map<java.lang.String,java.lang.String> params)

    * ### Method Detail

      * #### getHeaders
            
            public java.util.Map<java.lang.String,java.lang.String> getHeaders()




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
