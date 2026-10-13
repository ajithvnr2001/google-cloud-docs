---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Metric/
title: Metric \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:06.742953+00:00
---

# Metric  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Metric/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback 

#  Metric Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * Measure
    * JSON representation



Stores precomputed aggregated analytic data for an entity.

JSON representation  
---  
      
    
    {
      "firstSeen": string,
      "lastSeen": string,
      "sumMeasure": {
        object ([Measure](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Metric#Measure))
      },
      "totalEvents": string,
      "metricName": enum ([MetricName](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MetricName)),
      "dimensions": [
        enum ([Dimension](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Dimension))
      ],
      "exportWindow": string
    }  
  
Fields  
---  
`firstSeen` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Timestamp of the first time the entity was seen in the environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastSeen` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time stamp of the last time last time the entity was seen in the environment.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`sumMeasure` |  `object (`[Measure](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Metric#Measure)`)` Sum of all precomputed measures for the given metric.  
`totalEvents` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total number of events used to calculate the given precomputed metric.  
`metricName` |  `enum (`[MetricName](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/MetricName)`)` Name of the analytic.  
`dimensions[]` |  `enum (`[Dimension](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Dimension)`)` All group by clauses used to calculate the metric.  
`exportWindow` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Export window for which the metric was exported.  
  
## Measure

Describes the precomputed measure.

JSON representation  
---  
      
    
    {
      "value": number,
      "aggregateFunction": enum ([AggregateFunction](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/AggregateFunction))
    }  
  
Fields  
---  
`value` |  `number` Value of the aggregated measure.  
`aggregateFunction` |  `enum (`[AggregateFunction](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/AggregateFunction)`)` Function used to calculate the aggregated measure.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-19 UTC."],[],[]] 
