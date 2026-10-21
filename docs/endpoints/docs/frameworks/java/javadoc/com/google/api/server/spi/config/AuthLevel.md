---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel/
title: AuthLevel \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:05.263348+00:00
---

# AuthLevel  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  AuthLevel Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.config

## Enum AuthLevel

  * java.lang.Object
  *     * java.lang.Enum<[AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config")>
    *       * com.google.api.server.spi.config.AuthLevel



  * All Implemented Interfaces:
    java.io.Serializable, java.lang.Comparable<[AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config")>

* * *

  

        
        public enum AuthLevel
        extends java.lang.Enum<[AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config")>

Enum to choose frontend authentication level for use in endpoints annotations. Frontend authentication is handled by a Google API server prior to the request reaching backends. An early return before hitting the backend can happen if the request does not fulfill the requirement specified by the AuthLevel.




  *     * ### Enum Constant Summary

Enum Constants Enum Constant and Description  
---  
`[NONE](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html#NONE)` Frontend authentication will be skipped.  
`[OPTIONAL](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html#OPTIONAL)` Authentication is optional.  
`[OPTIONAL_CONTINUE](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html#OPTIONAL_CONTINUE)` Authentication is optional and will be attempted if authentication credential are supplied.  
`[REQUIRED](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html#REQUIRED)` Valid authentication credentials are required.  
`[UNSPECIFIED](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html#UNSPECIFIED)` Unspecified; AuthLevel is system default if there is any.  
    * ### Method Summary

All Methods Static Methods Concrete Methods Modifier and Type | Method and Description  
---|---  
`static [AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config")` | `[valueOf](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html#valueOf-java.lang.String-)(java.lang.String name)` Returns the enum constant of this type with the specified name.  
`static [AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config")[]` | `[values](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html#values--)()` Returns an array containing the constants of this enum type, in the order they are declared.  
      * ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
      * ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`



  *     * ### Enum Constant Detail

      * #### REQUIRED
            
            public static final [AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config") REQUIRED

Valid authentication credentials are required.

      * #### OPTIONAL
            
            public static final [AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config") OPTIONAL

Authentication is optional. If authentication credentials are supplied they must be valid.

      * #### OPTIONAL_CONTINUE
            
            public static final [AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config") OPTIONAL_CONTINUE

Authentication is optional and will be attempted if authentication credential are supplied. The request can still reach backend if authentication failed.

      * #### NONE
            
            public static final [AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config") NONE

Frontend authentication will be skipped. Existing authentication in cloud endpoints still applies.

      * #### UNSPECIFIED
            
            public static final [AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config") UNSPECIFIED

Unspecified; AuthLevel is system default if there is any.

    * ### Method Detail

      * #### values
            
            public static [AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config")[] values()

Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows: 
            
            for (AuthLevel c : AuthLevel.values())
                System.out.println(c);
            

Returns:
    an array containing the constants of this enum type, in the order they are declared
      * #### valueOf
            
            public static [AuthLevel](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AuthLevel.html "enum in com.google.api.server.spi.config") valueOf(java.lang.String name)

Returns the enum constant of this type with the specified name. The string must match _exactly_ an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)

Parameters:
    `name` \- the name of the enum constant to be returned.
Returns:
    the enum constant with the specified name
Throws:
    `java.lang.IllegalArgumentException` \- if this enum type has no constant with the specified name
    `java.lang.NullPointerException` \- if the argument is null



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
