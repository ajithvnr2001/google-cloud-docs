---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/CalculateStatsResponse/
title: CalculateStatsResponse \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:35:34.110241+00:00
---

# CalculateStatsResponse  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/CalculateStatsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  CalculateStatsResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * TimeSeries
    * JSON representation
  * Interval
    * JSON representation



The response for calculating conversation statistics.

JSON representation  
---  
      
    
    {
      "averageDuration": string,
      "averageTurnCount": integer,
      "conversationCount": integer,
      "smartHighlighterMatches": {
        string: integer,
        ...
      },
      "customHighlighterMatches": {
        string: integer,
        ...
      },
      "issueMatches": {
        string: integer,
        ...
      },
      "issueMatchesStats": {
        string: {
          object ([IssueStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels#IssueStats))
        },
        ...
      },
      "conversationCountTimeSeries": {
        object ([TimeSeries](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/CalculateStatsResponse#TimeSeries))
      }
    }  
  
Fields  
---  
`averageDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The average duration of all conversations. The average is calculated using only conversations that have a time duration.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`averageTurnCount` |  `integer` The average number of turns per conversation.  
`conversationCount` |  `integer` The total number of conversations.  
`smartHighlighterMatches` |  `map (key: string, value: integer)` A map associating each smart highlighter display name with its respective number of matches in the set of conversations.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`customHighlighterMatches` |  `map (key: string, value: integer)` A map associating each custom highlighter resource name with its respective number of matches in the set of conversations.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`issueMatches  
**(deprecated)**` |  `map (key: string, value: integer)` This item is deprecated!A map associating each issue resource name with its respective number of matches in the set of conversations. Key has the format: `projects/<Project-ID>/locations/<Location-ID>/issueModels/<Issue-Model-ID>/issues/<Issue-ID>` Deprecated, use `issueMatchesStats` field instead.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`issueMatchesStats` |  `map (key: string, value: object (`[IssueStats](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/projects.locations.issueModels#IssueStats)`))` A map associating each issue resource name with its respective number of matches in the set of conversations. Key has the format: `projects/<Project-ID>/locations/<Location-ID>/issueModels/<Issue-Model-ID>/issues/<Issue-ID>`An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`conversationCountTimeSeries` |  `object (`[TimeSeries](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/CalculateStatsResponse#TimeSeries)`)` A time series representing the count of conversations created over time that match that requested filter criteria.  
  
## TimeSeries

A time series representing conversations over time.

JSON representation  
---  
      
    
    {
      "intervalDuration": string,
      "points": [
        {
          object ([Interval](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/CalculateStatsResponse#Interval))
        }
      ]
    }  
  
Fields  
---  
`intervalDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The duration of each interval.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`points[]` |  `object (`[Interval](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1alpha1/CalculateStatsResponse#Interval)`)` An ordered list of intervals from earliest to latest, where each interval represents the number of conversations that transpired during the time window.  
  
## Interval

A single interval in a time series.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "conversationCount": integer
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The start time of this interval.Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`conversationCount` |  `integer` The number of conversations created in this interval.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
