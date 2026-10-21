---
url: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.DateUtil
title: Class DateUtil (5.0.3) \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:10:10.593568+00:00
---

# Class DateUtil (5.0.3)  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/java-gen2/reference/services/bundled/latest/com.google.appengine.api.search.DateUtil

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Reference ](https://docs.cloud.google.com/appengine/docs/standard/apis)



Send feedback 

#  Class DateUtil (5.0.3) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public final class DateUtil

A utility class that centralizes processing of dates.

## Inheritance

[java.lang.Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html) > DateUtil

## Inherited Members

[Object.clone()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#clone--)

[Object.equals(Object)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)

[Object.finalize()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#finalize--)

[Object.getClass()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#getClass--)

[Object.hashCode()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#hashCode--)

[Object.notify()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notify--)

[Object.notifyAll()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#notifyAll--)

[Object.toString()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#toString--)

[Object.wait()](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait--)

[Object.wait(long)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-)

[Object.wait(long,int)](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#wait-long-int-)

## Static Fields 

### MILLISECONDS_IN_DAY
    
    
    public static final int MILLISECONDS_IN_DAY

The milliseconds in a day.

**Field Value**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
## Static Methods 

### deserializeDate(String date)
    
    
    public static Date deserializeDate(String date)

Converts a string containing the milliseconds since the UNIX Epoch into a Date.

Two formats of date string are supported: "yyyy-MM-dd" and a long. Eventually, the "yyyy-MM-dd" format support will be removed.

**Parameter**  
---  
**Name** | **Description**  
`date` | `[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)`  
the date string to deserialize into a date  
**Returns**  
---  
**Type** | **Description**  
`[Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html)` | a date  
  
### formatDateTime(Date date)
    
    
    public static String formatDateTime(Date date)

Formats a date according ISO 8601 full date time format. Currently, this is used to print dates for error messages.

**Parameter**  
---  
**Name** | **Description**  
`date` | `[Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html)`  
the date to format as a string  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | a string representing the date in ISO 8601 format  
  
### getEpochPlusDays(int days, int milliseconds)
    
    
    public static final Date getEpochPlusDays(int days, int milliseconds)

Constructs a [Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html) set to the UNIX Epoch plus days plus milliseconds.

**Parameters**  
---  
**Name** | **Description**  
`days` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the number of days to add to the UNIX Epoch to get a Date  
`milliseconds` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
the number of milliseconds to add to the date  
**Returns**  
---  
**Type** | **Description**  
`[Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html)` | the Date with number of days plus Epoch  
  
### serializeDate(Date date)
    
    
    public static String serializeDate(Date date)

Converts date into a string containing the milliseconds since the UNIX Epoch.

**Parameter**  
---  
**Name** | **Description**  
`date` | `[Date](https://docs.oracle.com/javase/8/docs/api/java/util/Date.html)`  
the date to serialize as a string  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | a string representing the date as milliseconds since the UNIX Epoch  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-03 UTC."],[],[]] 
