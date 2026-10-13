---
url: https://docs.cloud.google.com/firestore/docs/reference/rest/v1/Cursor/
title: Cursor \u00a0|\u00a0 Firestore \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:17.580578+00:00
---

# Cursor  |  Firestore  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firestore/docs/reference/rest/v1/Cursor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore ](https://docs.cloud.google.com/firestore/docs)
  * [ Reference ](https://docs.cloud.google.com/firestore/native/docs/apis)



Send feedback 

#  Cursor Stay organized with collections  Save and categorize content based on your preferences. 

A position in a query result set.

JSON representation  
---  
      
    
    {
      "values": [
        {
          object ([Value](https://docs.cloud.google.com/firestore/docs/reference/rest/Shared.Types/ArrayValue#Value))
        }
      ],
      "before": boolean
    }  
  
Fields  
---  
`values[]` |  `object (`[Value](https://docs.cloud.google.com/firestore/docs/reference/rest/Shared.Types/ArrayValue#Value)`)` The values that represent a position, in the order they appear in the order by clause of a query.Can contain fewer values than specified in the order by clause.  
`before` |  `boolean` If the position is just before or just after the given values, relative to the sort order defined by the query.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-19 UTC."],[],[]] 
