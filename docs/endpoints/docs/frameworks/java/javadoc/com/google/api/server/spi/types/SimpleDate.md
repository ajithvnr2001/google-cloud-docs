---
url: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/types/SimpleDate/
title: SimpleDate \u00a0|\u00a0 Cloud Endpoints Frameworks for App Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:45:07.461195+00:00
---

# SimpleDate  |  Cloud Endpoints Frameworks for App Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/types/SimpleDate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ Endpoints Frameworks ](https://docs.cloud.google.com/endpoints/docs/frameworks/about-cloud-endpoints-frameworks)
  * [ Reference ](https://docs.cloud.google.com/endpoints/docs/frameworks/ref-endpoints-logs)



Send feedback 

#  SimpleDate Stay organized with collections  Save and categorize content based on your preferences. 

com.google.api.server.spi.types

## Class SimpleDate

  * java.lang.Object
  *     * com.google.api.server.spi.types.SimpleDate



  * * * *

  

        
        public class SimpleDate
        extends java.lang.Object

A class for storing simple date values without a time component.




  *     * ### Constructor Summary

Constructors Constructor and Description  
---  
`[SimpleDate](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/types/SimpleDate.html#SimpleDate-int-int-int-)(int year, int month, int day)` Constructs a new simple date.  
    * ### Method Summary

All Methods Instance Methods Concrete Methods Modifier and Type | Method and Description  
---|---  
`boolean` | `[equals](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/types/SimpleDate.html#equals-java.lang.Object-)(java.lang.Object obj)`  
`int` | `[getDay](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/types/SimpleDate.html#getDay--)()` Gets the calendar day; this should be between 1 and 31.  
`int` | `[getMonth](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/types/SimpleDate.html#getMonth--)()` Gets the calendar month number.  
`int` | `[getYear](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/types/SimpleDate.html#getYear--)()` Gets the calendar year.  
`int` | `[hashCode](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/types/SimpleDate.html#hashCode--)()`  
`java.lang.String` | `[toString](https://docs.cloud.google.com/endpoints/docs/frameworks/java/javadoc/com/google/api/server/spi/types/SimpleDate.html#toString--)()`  
      * ### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`



  *     * ### Constructor Detail

      * #### SimpleDate
            
            public SimpleDate(int year,
                              int month,
                              int day)

Constructs a new simple date.

Parameters:
    `year` \- the full year number
    `month` \- a month number between 1-12
    `day` \- a day number between 1-31
Throws:
    `java.lang.IllegalArgumentException` \- throws if the date is invalid, or the year is outside the RFC3339 supported range
    * ### Method Detail

      * #### getYear
            
            public int getYear()

Gets the calendar year.

Returns:
    the full year number
      * #### getMonth
            
            public int getMonth()

Gets the calendar month number. This would return 1 for January, and 12 for December.

Returns:
    the month number
      * #### getDay
            
            public int getDay()

Gets the calendar day; this should be between 1 and 31.

Returns:
    the day number
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
