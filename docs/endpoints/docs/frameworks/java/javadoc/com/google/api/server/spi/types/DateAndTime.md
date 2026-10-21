---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/types/DateAndTime/
title: DateAndTime \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:06.174047+00:00
---

# DateAndTime  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/types/DateAndTime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  DateAndTime Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.types

## Class DateAndTime

  * java.lang.Object
  *     * com.google.api.server.spi.types.DateAndTime



  * * * *

  

        
        public final class DateAndTime
        extends java.lang.Object

A class for storing date-time values. Unlike `java.util.Date`, this preserves time zone information.




  *     * ### Method Summary

All Methods Static Methods Instance Methods Concrete Methods Modifier and Type | Method and Description  
---|---  
`boolean` | `[equals](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/types/DateAndTime.html#equals-java.lang.Object-)(java.lang.Object obj)`  
`int` | `[hashCode](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/types/DateAndTime.html#hashCode--)()`  
`static [DateAndTime](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/types/DateAndTime.html "class in com.google.api.server.spi.types")` | `[parseRfc3339String](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/types/DateAndTime.html#parseRfc3339String-java.lang.String-)(java.lang.String rfc3339String)` Constructs a new date-time from an RFC 3339 formatted string.  
`java.lang.String` | `[toRfc3339String](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/types/DateAndTime.html#toRfc3339String--)()` Returns the RFC 3339 representation of the date-time.  
`java.lang.String` | `[toString](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/types/DateAndTime.html#toString--)()`  
      * ### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`



  *     * ### Method Detail

      * #### toRfc3339String
            
            public java.lang.String toRfc3339String()

Returns the RFC 3339 representation of the date-time.

Returns:
    an RFC 3339 string
      * #### parseRfc3339String
            
            public static [DateAndTime](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/types/DateAndTime.html "class in com.google.api.server.spi.types") parseRfc3339String(java.lang.String rfc3339String)

Constructs a new date-time from an RFC 3339 formatted string.

Parameters:
    `rfc3339String` \- An RFC 3339 string to parse.
Returns:
    the parsed datetime
      * #### equals
            
            public boolean equals(java.lang.Object obj)

Overrides:
    `equals` in class `java.lang.Object`
      * #### hashCode
            
            public int hashCode()

Overrides:
    `hashCode` in class `java.lang.Object`
      * #### toString
            
            public java.lang.String toString()

Overrides:
    `toString` in class `java.lang.Object`



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
