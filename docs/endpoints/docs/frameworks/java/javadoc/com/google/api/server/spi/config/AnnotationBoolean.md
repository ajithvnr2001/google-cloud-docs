---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean/
title: AnnotationBoolean \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:46:40.695420+00:00
---

# AnnotationBoolean  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  AnnotationBoolean Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.config

## Enum AnnotationBoolean

  * java.lang.Object
  *     * java.lang.Enum<[AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config")>
    *       * com.google.api.server.spi.config.AnnotationBoolean



  * All Implemented Interfaces:
    java.io.Serializable, java.lang.Comparable<[AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config")>

* * *

  

        
        public enum AnnotationBoolean
        extends java.lang.Enum<[AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config")>

Enum allowing a boolean flag or unspecified. For use in api annotations.




  *     * ### Enum Constant Summary

Enum Constants Enum Constant and Description  
---  
`[FALSE](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html#FALSE)`  
`[TRUE](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html#TRUE)`  
`[UNSPECIFIED](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html#UNSPECIFIED)`  
    * ### Method Summary

All Methods Static Methods Concrete Methods Modifier and Type | Method and Description  
---|---  
`static [AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config")` | `[valueOf](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html#valueOf-java.lang.String-)(java.lang.String name)` Returns the enum constant of this type with the specified name.  
`static [AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config")[]` | `[values](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html#values--)()` Returns an array containing the constants of this enum type, in the order they are declared.  
      * ### Methods inherited from class java.lang.Enum

`clone, compareTo, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`
      * ### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`



  *     * ### Enum Constant Detail

      * #### TRUE
            
            public static final [AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config") TRUE

      * #### FALSE
            
            public static final [AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config") FALSE

      * #### UNSPECIFIED
            
            public static final [AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config") UNSPECIFIED

    * ### Method Detail

      * #### values
            
            public static [AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config")[] values()

Returns an array containing the constants of this enum type, in the order they are declared. This method may be used to iterate over the constants as follows: 
            
            for (AnnotationBoolean c : AnnotationBoolean.values())
                System.out.println(c);
            

Returns:
    an array containing the constants of this enum type, in the order they are declared
      * #### valueOf
            
            public static [AnnotationBoolean](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/config/AnnotationBoolean.html "enum in com.google.api.server.spi.config") valueOf(java.lang.String name)

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
