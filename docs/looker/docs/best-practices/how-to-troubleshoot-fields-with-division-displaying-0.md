---
url: https://docs.cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-fields-with-division-displaying-0/
title: Why are my fields with division showing up as 0? \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:42.224006+00:00
---

# Why are my fields with division showing up as 0?  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-fields-with-division-displaying-0/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Why are my fields with division showing up as 0? Stay organized with collections  Save and categorize content based on your preferences. 

In certain dialects, including Postgres and Redshift, performing a calculation between integers (like dividing counts) will return an integer even if the result would be a decimal in normal math. For example, you might make measures like the following: 
    
    
    measure: sold_ratio {
        type: number
        sql: ${sold_count} / ${total_count} ;;
        value_format: "0.00" # Number with exactly 2 decimals (1.23)
    }
    
    
    measure: sold_percent {
        type: number
        sql: 100 * ${sold_count} / ${count} ;;
        value_format: "0.00"
    }
    

However, when you run the measures in an Explore, the **Sold Ratio** column returns zero, and the **Sold Percent** column does not have its decimal places populated. This is not correct: 

Inventory Items Sold Percent | Inventory Items Sold Ratio | Inventory Items Count | Inventory Items Sold Count  
---|---|---|---  
48.00 | 0 | 1,165,224 | 560,223  
  
##  The solution: Cast your field as a floating-point number 

If the calculation is multiplied by a non-integer, the values will cast as floats, and decimals will be returned as expected. You can multiply the numerator by a decimal number (like 1.0 or 100.0) to force SQL to return a decimal result: 
    
    
    measure: sold_ratio {
        type: number
        sql: 1.0 * ${sold_count} / ${total_count};;
        value_format: "0.00"
    }
    
    
    measure: sold_percent {
        type: Number
        sql: 100.0 * ${sold_count} / ${count};;
        value_format: "0.00"
    }
    

The resulting Explore **Data** table now displays the expected results: 

Inventory Items Sold Percent | Inventory Items Sold Ratio | Inventory Items Count | Inventory Items Sold Count  
---|---|---|---  
48.08 | 0.48 | 1,165,224 | 560,223  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
