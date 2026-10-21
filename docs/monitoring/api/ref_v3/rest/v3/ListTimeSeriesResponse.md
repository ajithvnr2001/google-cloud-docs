---
url: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/ListTimeSeriesResponse/
title: ListTimeSeriesResponse \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:11:17.794945+00:00
---

# ListTimeSeriesResponse  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/ListTimeSeriesResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)
  * [ Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Reference ](https://docs.cloud.google.com/monitoring/docs/apis)



Send feedback 

#  ListTimeSeriesResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The `timeSeries.list` response.

JSON representation  
---  
      
    
    {
      "timeSeries": [
        {
          object ([TimeSeries](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries))
        }
      ],
      "nextPageToken": string,
      "executionErrors": [
        {
          object ([Status](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/Status))
        }
      ],
      "unit": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`timeSeries[]` |  `object (`[TimeSeries](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/TimeSeries)`)` One or more time series that match the filter included in the request.  
`nextPageToken` |  `string` If there are more results than have been returned, then this field is set to a non-empty value. To see the additional results, use that value as `pageToken` in the next call to this method.  
`executionErrors[]` |  `object (`[Status](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/Shared.Types/Status)`)` Query execution errors that may have caused the time series data returned to be incomplete.  
`unit` |  `string` The unit in which all `timeSeries` point values are reported. `unit` follows the UCUM format for units as seen in <https://unitsofmeasure.org/ucum.html>. If different `timeSeries` have different units (for example, because they come from different metric types, or a unit is absent), then `unit` will be "{not_a_unit}".  
`unreachable[]` |  `string` Cloud regions that were unreachable which may have caused incomplete data to be returned.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-23 UTC."],[],[]] 
