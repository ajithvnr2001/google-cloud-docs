---
url: https://docs.cloud.google.com/data-studio/coalesce/
title: Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:35.623790+00:00
---

# Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/coalesce/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# COALESCE

Use `COALESCE` to replace null values with a more meaningful default value.

## Sample usage
    
    
    COALESCE(Field1, Field2, Field3)
    

## Syntax
    
    
    COALESCE( field_expression [, field_expression,...])
    

### Parameters

  * `field_expression` \- a field or expression. All `field_expressions` must be of the same type.



## Example

Suppose you are tracking multiple racers across multiple heats in a competition. Racers might sit out heats for various reasons. You want to create a **First_Time** field that contains each racer's first results.

Here's the race data.

Racer  |  Heat1  |  Heat2  |  Heat3   
---|---|---|---  
Racer X  |  |  38.22  |  37.61   
Racer Y  |  41.33  |  |  38.04   
Racer Z  |  39.27  |  39.04  |  38.85   
  
Use the following formula in the **First_Time** field to get the first non-null value from the **Heat** columns:
    
    
    COALESCE(Heat1, Heat2, Heat3)
    

Results:

Racer  |  Heat1  |  Heat2  |  Heat3  |  First_Time   
---|---|---|---|---  
Racer X  |  null  |  38.22  |  37.61  |  38.22   
Racer Y  |  41.33  |  null  |  38.04  |  41.33   
Racer Z  |  39.27  |  39.04  |  38.85  |  39.27   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-14 UTC."],[],[]] 
