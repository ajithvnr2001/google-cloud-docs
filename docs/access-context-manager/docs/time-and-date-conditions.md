---
url: https://docs.cloud.google.com/access-context-manager/docs/time-and-date-conditions/
title: Configuring time and day access conditions \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:19:04.984037+00:00
---

# Configuring time and day access conditions  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/time-and-date-conditions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Configuring time and day access conditions Stay organized with collections  Save and categorize content based on your preferences. 

The Access Context Manager date and time restriction feature gives enterprises the ability to set access controls based on the date and time.

When evaluating zero-trust access, it is often necessary to restrict user access to resources to specific days and times. For example, shift workers may only be allowed to access company resources during their shift hours, or users may be given temporary access between a particular time of the day.

To apply the time and day access level condition, use the functions listed in the following table. The format of the functions is `function(timezone)`.

You can specify `timezone` as UTC, fixed time zones which are explicit hour and minute offsets from UTC, or as long `timezone` names like `Europe/Paris`, `CET`, or `US/Central`. For a complete listing, see the [Timezone](https://github.com/google/cel-spec/blob/master/doc/langdef.md#timezones) section of the Common Express Language definition.

If you don't specify a 'timezone', the expression defaults to UTC.

Function | Description | Example  
---|---|---  
`getFullYear` | Retrieve the number that represents the current year, such as 2020.  | Is the year 2020? `request.time.getFullYear("America/Los_Angeles") == 2020`  
`getMonth` | Retrieve the month of the year. The month values range from 0 to 11, where 0 == January and 11 == December.  | Is the month January? `request.time.getMonth("America/Los_Angeles") == 0`  
`getDate` | Retrieve the date of the month. The date values range from 1 to 31, where 1 is the first of the month, and 31 is the 31st of the month.  |  Is it the first of the month? `request.time.getDate("America/Los_Angeles") == 1`  
`getDayOfMonth` | Retrieve the day of the month. The day values range from 0 to 30, where 0 is the first of the month, and 30 is the 31st of the month.  | Is it the first of the month? `request.time.getDayOfMonth("America/Los_Angeles") == 0`  
`getDayOfWeek` | Retrieve the day of the week. The day values range from 0 to 6, where 0 is Sunday, and 6 is Saturday.  | Is it Monday? `request.time.getDayOfWeek("America/Los_Angeles") == 1`  
`getDayOfYear` | Retrieve the day of the year. The day values range from 0 to 365, where 0 is the first day of the year, and 365 is the 366th day of the year. |  Is it the first day of the year? `request.time.getDayOfYear("America/Los_Angeles") == 0`  
`getHours` | Retrieve the hour of the day. The hour values range from 0 to 23, where 0 is midnight and 23 is 11 PM.  |  Is it 7 PM? `request.time.getHours("America/Los_Angeles") == 19`  
`getMinutes` | Retrieve the minute of the hour. The minute values range from 0 to 59, where 0 is the first minute and 59 is the last minute of the hour.  
| Is it 7:30 PM? `request.time.getHours("America/Los_Angeles") == 19 && request.time.getMinutes("America/Los_Angeles") == 30`  
`date` | Return the timestamp representing the date normalized to midnight UTC.  | Current time in UTC. `request.time.date()`  
`date(tz string)` |  Return the timestamp representing the date normalized to midnight relative to the TimeZone string <tz>. | Current time in Pacific time.  `request.time.date('America/Los_Angeles')` `request.time.date('08:00')`  
`timeOfDay` | Return the `google.type.TimeOfDay` associated with the timestamp in UTC. | Current time of day in UTC, such as '09:30:00' `request.time.timeOfDay()`  
`timeOfDay(tz string)` | Return the google.type.TimeOfDay associated with the timestamp and relative to the TimeZone string <tz>. |  Current time of day in pacific time, such as '09:30:00'  `request.time.timeOfDay('America/Los_Angeles')`  
`between(start, stop)`(for timestamp) | For a given timestamp, return `True` if the timestamp is between time 'start' (inclusive) and 'stop' (exclusive). 'Start' and 'stop' can be `type.Timestamp` or string, which will be converted to `type.Timestamp`. | Is the current timestamp, in PST, between Jan 10, 2020 00:00 (inclusive) and Jan 11, 2020 00:00 (exclusive)? `request.time.date('08:00') .between('2020-10-01T00:00:00+08:00', '2020-10-01T00:00:00+08:00') `  
`between(start, stop string)` (for TimeOfDay) | For a given `TimeOfDay`, return `True` if the time of date is between the 'start' (inclusive) and 'stop' (exclusive). 'Start' and 'stop' can be `type.TimeOfDay` or string, which will be converted to `type.TimeOfDay`.  | Is the current time of day, in Pacific time, between 09:30 AM (inclusive) and 05:30 PM (exclusive)? `request.time.timeOfDay('America/Los_Angeles').between('09:30:00', '17:30:00')`  
  
The following table contains examples of how to use time and date restrictions:

Example Policy | Expression  
---|---  
Allow shift workers to access resources from Monday to Friday between 9 AM to 5 PM, except for July fourth. | Option 1: `request.time.getDayOfWeek("America/Los_Angeles") >= 1 && request.time.getDayOfWeek("America/Los_Angeles") <= 5 && request.time.getHours("America/Los_Angeles") >= 9 && request.time.getHours("America/Los_Angeles") <= 17 && !(request.time.getMonth("America/Los_Angeles") == 6 && request.time.getDayOfMonth("America/Los_Angeles") == 3)` Option 2:  `request.time.getDayOfWeek("America/Los_Angeles") >= 1 && request.time.getDayOfWeek("America/Los_Angeles") <= 5 && !(request.time.getMonth("America/Los_Angeles") == 6 && request.time.getDayOfMonth("America/Los_Angeles") == 3) && request.time.timeOfDay("America/Los_Angeles").between('09:30:00', '17:00:00') `  
Allow temporary access to resources on March 1, 2020, between 10 PM to midnight. |  Option 1:  `request.time.getFullYear("America/Los_Angeles") == 2020 && request.time.getMonth("America/Los_Angeles") == 2 && request.time.getDayOfMonth("America/Los_Angeles") == 0 && request.time.getHours("America/Los_Angeles") >= 22 && request.time.getHours("America/Los_Angeles") <= 23 ` Option 2:  `request.time.between('2020-03-01T23:00:00+08:00', '2020-03-02T00:00:00+08:00')`  
  
Following are some example expressions that use some of the functions to capture specific time ranges:

**Express the range during business hours**   
The date-time format is 'HH:MM:SS' and follows the RFC 3339 standard.
    
    
    request.time.timeOfDay('America/Los_Angeles').between('09:30:00', '17:30:00')
    
    
    
    request.time.date('America/Los_Angeles')
        .between('01-10-2020T00:00:00+08:00', '01-11-2020T00:00:00-07:00')
    

**Express specific days of the month, first week**   
(Note support for alternative timezone format)
    
    
    request.time.getDayOfMonth('America/Los_Angeles') < 7
    

**Express specific date ranges, yearly**   
For example, for quarterly reporting.
    
    
    request.time.date('Asia/Hong_Kong').between(
        request.time.getFullYear('08:00') + '-12-15T00:00:00+08:00',
        request.time.getFullYear('08:00')+1 + '-01-01T00:00:00+08:00')
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
