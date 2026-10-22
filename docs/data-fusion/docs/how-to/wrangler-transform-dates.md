---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-transform-dates/
title: Transform dates \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:37.904953+00:00
---

# Transform dates  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/wrangler-transform-dates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Transform dates Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to perform date transformations when you prepare data in the Wrangler workspace of the Cloud Data Fusion Studio.

The Wrangler workspace supports the date transformations described in the following sections.

## Parse dates

To parse column values from a string to a date data type, follow these steps:

  1. [Go to Wrangler workspace in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#navigate-to-wrangler).
  2. On the **Data** tab, go to a column name and click the arrow_drop_down expander arrow.
  3. Select **Parse > Simple date**.
  4. Specify the following custom format: `MM/dd/yy HH:mm`. The format must match the date formatting in the column. If you select a date format that doesn't match the dates in the column, you will get incorrect results.

The data type of the column changes from string to `Timestamp_micros`.




## Get components

The following examples show directives retrieving date components, such as the month, day, year, minute, second, or hour:
    
    
    set-column :month Transaction_date.getMonth()
    
    set-column :year Transaction_date.getYear()
    
    set-column :day_of_week Transaction_date.getDayOfWeek()
    
    set-column :day_of_month Transaction_date.getDayOfMonth()
    
    set-column :day_of_year Transaction_date.getDayOfYear()
    
    set-column :minute Transaction_date.getMinute()
    
    set-column :hour Transaction_date.getHour()
    
    set-column :second Transaction_date.getSecond()
    
    set-column :zone Transaction_date.getZone()
    

## Add time

The following examples show directives that add units of time to the date:
    
    
    set-column :add_days Transaction_date.plusDays(1)
    
    set-column :add_hours Transaction_date.plusHours(200)
    
    set-column :add_minutes Transaction_date.plusMinutes(3600)
    
    set-column :add_months Transaction_date.plusMonths(3)
    
    set-column :add_weeks Transaction_date.plusWeeks(2)
    
    set-column :add_years Transaction_date.plusYears(2)
    
    set-column :add_seconds Transaction_date.plusSeconds(36000)
    
    set-column :add_nonoseconds Transaction_date.plusNanos(3600000)
    

## Subtract time

The following examples show directives that subtract units of time from the date:
    
    
    set-column :subtract_days Transaction_date.minusDays(1)
    
    set-column :subtract_hours Transaction_date.minusHours(200)
    
    set-column :subtract_minutes Transaction_date.minusMinutes(3600)
    
    set-column :subtract_months Transaction_date.minusMonths(3)
    
    set-column :subtract_weeks Transaction_date.minusWeeks(2)
    
    set-column :subtract_years Transaction_date.minusYears(2)
    
    set-column :subtract_seconds Transaction_date.minusSeconds(36000)
    
    set-column :subtract_nonoseconds Transaction_date.minusNanos(3600000)
    

## What's next

  * Learn more about [Wrangler directives](https://docs.cloud.google.com/data-fusion/docs/concepts/wrangler-overview#apply_directives).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
