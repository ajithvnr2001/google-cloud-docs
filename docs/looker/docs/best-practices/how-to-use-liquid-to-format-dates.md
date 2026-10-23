---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-liquid-to-format-dates/
title: How to use Liquid to format dates \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:44:22.456452+00:00
---

# How to use Liquid to format dates  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-use-liquid-to-format-dates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  How to use Liquid to format dates Stay organized with collections  Save and categorize content based on your preferences. 

In some situations, you may want to change the way Looker formats dates. 

For example, if you're building Explores and dashboards for users in Europe, any dates that are in an all-numeric format should appear in the order Day-Month-Year. For example, June 7th, 2019 should be formatted as `07/06/2019` or `Jun 07, 2019`. Looker's default format renders the date as `2019-06-07`. While you can use SQL functions like `DATE_FORMAT()` to change a date format, you may not want to write everything in plain SQL. 

##  Using Liquid in the `html` parameter 

**Note:** When [downloading content](https://docs.cloud.google.com/looker/docs/downloading), Liquid formatting applied in the [`html`](https://docs.cloud.google.com/looker/docs/reference/param-field-html) parameter is not applied to text-based download formats, such as TXT, CSV, Excel, or JSON.

You can use [Liquid formatting](https://shopify.github.io/liquid/filters/date/) in the [`html`](https://docs.cloud.google.com/looker/docs/reference/param-field-html) parameter of a dimension to change the format of any field that uses a valid date format. Since Liquid expects a valid date, it is best to use the timeframes from an existing dimension group. You can't change the week or month _numbers_ , because those are returned as integers. 

**Caution:** Liquid formatting is not supported for the [`month`](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#time_type) timeframe. 

For example, you can format `${created_date}` to render as `Aug 23 22` instead of the Looker default `2022-08-23`: 
    
    
    
      dimension: date_formatted {
        sql: ${created_date} ;;
        html:{{ rendered_value | date: "%b %d, %y" }};;
      }
    
    
    

The format for the string syntax `"%b %d, %y"` is the same as [`strftime`](http://strftime.net). 

Because the `html` parameter uses Liquid formatting, the original value of the timeframe is not changed — only the way that the value is rendered to the user. This ensures that the order in which dates appear in a query won't change. 

Following are some other examples you can use. The larger reference of available formats is at the bottom of this page. 

**Preset** |  **Example**  
---|---  
` %m/%d/%Y ` |  06/05/2013   
` %A, %B %e, %Y ` |  Wednesday, June 5, 2013   
` %b %e %a ` |  Jun 5 Wed   
  
##  Example 

The following example of an Explore query shows **Order Items Date** and **Orders Items Week** formatted differently and organized under a **Created date** group label to simulate a date dimension group in the Explore field picker. 

The custom formatting shows users which date and which week number of the year correspond to the largest **Count of Items** values in descending order. 

See the [`group_label` documentation page](https://docs.cloud.google.com/looker/docs/reference/param-field-group-label) to learn more about using the `group_label` parameter. 

![An Explore query displays custom date formatting results for Order Items Date, Order Items Week, sorted by Order Items Count of Items descending.](https://docs.cloud.google.com/static/looker/docs/images/best-practices-liquid-date-formatting-result-explore.png)

###  The LookML 

The Explore example uses the following LookML: 
    
    
    
    
    # The original dimension group - hidden so that users can only choose from the formatted dates date and week timeframes
      dimension_group: created {
        hidden: yes
        type: time
        timeframes: [
          raw,
          time,
          date,
          hour,
          hour_of_day,
          time_of_day,
          week,
          month,
          quarter,
          year
        ]
        sql: ${TABLE}.created_at ;;
      }
    
    # The customized timeframes, organized in the Explore field picker under the group label Created date
      dimension: date_formatted {
        group_label: "Created date"
        label: "Date"
        type: date_raw
        sql: ${created_date} ;;
        html: {{ rendered_value | date: "%b %d, %y" }};;
      }
    
      dimension: week_formatted {
        group_label: "Created date"
        label: "Week"
        type: date_raw
        sql: ${created_week} ;;
        html: {{ rendered_value | date: "Week %U (%b %d)" }};;
      }
    
    
    

##  `strftime Reference`

The following table lists various `strftime` formats. Note that not all formats may render as expected in Looker. 

**specifier** |  **Replaced by** |  **Example**  
---|---|---  
%a  |  Abbreviated weekday name *  |  Thu   
%A  |  Full weekday name *  |  Thursday   
%b  |  Abbreviated month name *  |  Aug   
%B  |  Full month name *  |  August   
%c  |  Date and time representation *  |  Thu Aug 23 14:55:02 2001   
%C  |  Year divided by 100 and truncated to integer (00-99)  |  20   
%d  |  Day of the month, zero-padded (01-31)  |  23   
%D  |  Short MM/DD/YY date, equivalent to %m/%d/%y  |  08/23/01   
%e  |  Day of the month, space-padded ( 1-31)  |  23   
%F  |  Short YYYY-MM-DD date, equivalent to %Y-%m-%d  |  2001-08-23   
%g  |  Week-based year, last two digits (00-99)  |  1   
%G  |  Week-based year  |  2001   
%h  |  Abbreviated month name * (same as %b)  |  Aug   
%H  |  Hour in 24h format (00-23)  |  14   
%I  |  Hour in 12h format (01-12)  |  02   
%j  |  Day of the year (001-366)  |  235   
%k  |  Hour in 24h format, single digits are proceeded by a blank space (0-23)  |  14   
%l  |  Hour in 12h format, single digits are proceeded by a blank space (0-12)  |  2   
%m  |  Month as a decimal number (01-12)  |  8   
%M  |  Minute (00-59)  |  55   
%n  |  New-line character ('\n')  |   
%P  |  am or pm designation in lowercase  |  pm   
%r  |  12-hour clock time *  |  2:55:02 PM   
%R  |  24-hour HH:MM time, equivalent to %H:%M  |  14:55   
%s  |  Number of seconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC)  |  1566236649   
%S  |  Second (00-61)  |  2   
%t  |  Horizontal-tab character ('\t')  |   
%T  |  ISO 8601 time format (HH:MM:SS), equivalent to %H:%M:%S  |  14:55:02   
%u  |  ISO 8601 weekday as number with Monday as 1 (1-7)  |  4   
%U  |  Week number with the first Sunday as the first day of week one (00-53)  |  33   
%V  |  ISO 8601 week number (01-53)  |  34   
%w  |  Weekday as a decimal number with Sunday as 0 (0-6)  |  4   
%W  |  Week number with the first Monday as the first day of week one (00-53)  |  34   
%x  |  Date representation *  |  08/23/01   
%X  |  Time representation *  |  14:55:02   
%y  |  Year, last two digits (00-99)  |  1   
%Y  |  Year  |  2001   
%z  |  ISO 8601 offset from UTC in timezone (1 minute=1, 1 hour=100)If timezone cannot be determined, no characters  |  100   
%Z  |  Timezone name or abbreviation *If timezone cannot be determined, no characters  |  CDT   
%%  |  A % sign  |  %   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
