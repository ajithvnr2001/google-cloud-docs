---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.ScheduledCronTaskOrBuilder
title: Interface ScheduledCronTaskOrBuilder (0.7.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:51:36.328613+00:00
---

# Interface ScheduledCronTaskOrBuilder (0.7.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-backstory/latest/com.google.backstory.ScheduledCronTaskOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ScheduledCronTaskOrBuilder (0.7.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.7.0 (latest)  0.3.0  0.2.0  0.1.0 
    
    
    public interface ScheduledCronTaskOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getAuthor()
    
    
    public abstract String getAuthor()

The author or creator of the task.

`string author = 7;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The author.  
  
### getAuthorBytes()
    
    
    public abstract ByteString getAuthorBytes()

The author or creator of the task.

`string author = 7;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for author.  
  
### getComment()
    
    
    public abstract String getComment()

A comment or description for the task.

`string comment = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The comment.  
  
### getCommentBytes()
    
    
    public abstract ByteString getCommentBytes()

A comment or description for the task.

`string comment = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for comment.  
  
### getEvent()
    
    
    public abstract String getEvent()

Crontab special string or event (e.g., "@reboot", "@daily").

`string event = 8;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The event.  
  
### getEventBytes()
    
    
    public abstract ByteString getEventBytes()

Crontab special string or event (e.g., "@reboot", "@daily").

`string event = 8;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for event.  
  
### getHour()
    
    
    public abstract String getHour()

Crontab hour field. Value is an integer between 0 and 23, a range or list of values (e.g., "0-6", "_/2", "1,2"), or an asterisk (_) to indicate first-last hours.

`string hour = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The hour.  
  
### getHourBytes()
    
    
    public abstract ByteString getHourBytes()

Crontab hour field. Value is an integer between 0 and 23, a range or list of values (e.g., "0-6", "_/2", "1,2"), or an asterisk (_) to indicate first-last hours.

`string hour = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for hour.  
  
### getMinute()
    
    
    public abstract String getMinute()

Crontab minute field. Value is an integer between 0 and 59 and can also be a range or list of values (e.g., "0-59", "0-59/5", "0,15,30,45") and it // can also be an asterisk (*) to indicate first-last minutes. More on crontab format can be found here: <https://www.linux.org/docs/man5/crontab.html>

`string minute = 1;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The minute.  
  
### getMinuteBytes()
    
    
    public abstract ByteString getMinuteBytes()

Crontab minute field. Value is an integer between 0 and 59 and can also be a range or list of values (e.g., "0-59", "0-59/5", "0,15,30,45") and it // can also be an asterisk (*) to indicate first-last minutes. More on crontab format can be found here: <https://www.linux.org/docs/man5/crontab.html>

`string minute = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for minute.  
  
### getMonth()
    
    
    public abstract String getMonth()

Crontab month field. Value is an integer between 1 and 12 or a 3-letter name (e.g., "Jan"), a range or list of values (e.g., "1-3", "_/2", "1,6"), or an asterisk (_) to indicate first-last months.

`string month = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The month.  
  
### getMonthBytes()
    
    
    public abstract ByteString getMonthBytes()

Crontab month field. Value is an integer between 1 and 12 or a 3-letter name (e.g., "Jan"), a range or list of values (e.g., "1-3", "_/2", "1,6"), or an asterisk (_) to indicate first-last months.

`string month = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for month.  
  
### getMonthDay()
    
    
    public abstract String getMonthDay()

Crontab day of month field. Value is an integer between 1 and 31, a range or list of values (e.g., "1-7", "1-31/7", "1,15"), or an asterisk (*) to indicate first-last days of month.

`string month_day = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The monthDay.  
  
### getMonthDayBytes()
    
    
    public abstract ByteString getMonthDayBytes()

Crontab day of month field. Value is an integer between 1 and 31, a range or list of values (e.g., "1-7", "1-31/7", "1,15"), or an asterisk (*) to indicate first-last days of month.

`string month_day = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for monthDay.  
  
### getPath()
    
    
    public abstract String getPath()

The PATH environment variable defined in the crontab file.

`string path = 9;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The path.  
  
### getPathBytes()
    
    
    public abstract ByteString getPathBytes()

The PATH environment variable defined in the crontab file.

`string path = 9;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for path.  
  
### getWeekDay()
    
    
    public abstract String getWeekDay()

Crontab day of week field. Value is an integer between 0 and 7 (0 or 7 is Sunday) or a 3-letter name (e.g., "Fri"), a range or list of values (e.g., "1-5", "0,6"), or an asterisk (*) to indicate first-last days of week.

`string week_day = 5;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The weekDay.  
  
### getWeekDayBytes()
    
    
    public abstract ByteString getWeekDayBytes()

Crontab day of week field. Value is an integer between 0 and 7 (0 or 7 is Sunday) or a 3-letter name (e.g., "Fri"), a range or list of values (e.g., "1-5", "0,6"), or an asterisk (*) to indicate first-last days of week.

`string week_day = 5;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for weekDay.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
