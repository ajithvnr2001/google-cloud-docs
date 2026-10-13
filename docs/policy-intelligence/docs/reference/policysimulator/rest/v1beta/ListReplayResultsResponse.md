---
url: https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/ListReplayResultsResponse/
title: ListReplayResultsResponse \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:41.985482+00:00
---

# ListReplayResultsResponse  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/ListReplayResultsResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Reference ](https://docs.cloud.google.com/policy-intelligence/docs/apis)



Send feedback 

#  ListReplayResultsResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



Response message for `[Simulator.ListReplayResults](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/projects.locations.replays.results/list#google.cloud.policysimulator.v1beta.Simulator.ListReplayResults)`.

JSON representation  
---  
      
    
    {
      "replayResults": [
        {
          object ([ReplayResult](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/folders.locations.replays.results#ReplayResult))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`replayResults[]` |  `object (`[ReplayResult](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/folders.locations.replays.results#ReplayResult)`)` The results of running a `[Replay](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/folders.locations.replays#Replay)`.  
`nextPageToken` |  `string` A token that you can use to retrieve the next page of `[ReplayResult](https://docs.cloud.google.com/policy-intelligence/docs/reference/policysimulator/rest/v1beta/folders.locations.replays.results#ReplayResult)` objects. If this field is omitted, there are no subsequent pages.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-16 UTC."],[],[]] 
