---
url: https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CalculateStatsResponse
title: Class CalculateStatsResponse (1.28.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:36:17.375907+00:00
---

# Class CalculateStatsResponse (1.28.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CalculateStatsResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class CalculateStatsResponse (1.28.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.28.0 (latest)  1.27.0  1.26.0  1.25.0  1.24.0  1.23.3  1.22.0  1.21.0  1.20.0  1.19.1  1.18.0  1.17.5  1.16.0  1.15.0  1.14.1  1.13.0  1.12.0  1.11.1  1.10.0  1.9.1  1.8.0  1.7.0  1.6.1  1.5.0  1.4.5  1.3.2  1.2.1  1.1.0  1.0.0  0.6.1  0.5.0  0.4.0  0.3.1  0.2.0  0.1.1 
    
    
    CalculateStatsResponse(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The response for calculating conversation statistics.

## Attributes  
  
---  
**Name** | **Description**  
`average_duration` |  `google.protobuf.duration_pb2.Duration`   
The average duration of all conversations. The average is calculated using only conversations that have a time duration.   
`average_turn_count` |  `int`   
The average number of turns per conversation.   
`conversation_count` |  `int`   
The total number of conversations.   
`smart_highlighter_matches` |  `MutableMapping[str, int]`   
A map associating each smart highlighter display name with its respective number of matches in the set of conversations.   
`custom_highlighter_matches` |  `MutableMapping[str, int]`   
A map associating each custom highlighter resource name with its respective number of matches in the set of conversations.   
`issue_matches` |  `MutableMapping[str, int]`   
A map associating each issue resource name with its respective number of matches in the set of conversations. Key has the format: `projects/` Deprecated, use `issue_matches_stats` field instead.   
`issue_matches_stats` |  `MutableMapping[str, [google.cloud.contact_center_insights_v1.types.IssueModelLabelStats.IssueStats](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.IssueModelLabelStats.IssueStats)]`   
A map associating each issue resource name with its respective number of matches in the set of conversations. Key has the format: `projects/`  
`conversation_count_time_series` |  `[google.cloud.contact_center_insights_v1.types.CalculateStatsResponse.TimeSeries](https://docs.cloud.google.com/python/docs/reference/contactcenterinsights/latest/google.cloud.contact_center_insights_v1.types.CalculateStatsResponse.TimeSeries)`   
A time series representing the count of conversations created over time that match that requested filter criteria.   
  
## Classes 

### CustomHighlighterMatchesEntry
    
    
    CustomHighlighterMatchesEntry(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### IssueMatchesEntry
    
    
    IssueMatchesEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### IssueMatchesStatsEntry
    
    
    IssueMatchesStatsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### SmartHighlighterMatchesEntry
    
    
    SmartHighlighterMatchesEntry(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### TimeSeries
    
    
    TimeSeries(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A time series representing conversations over time.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
