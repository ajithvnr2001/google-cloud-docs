---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.Feed
title: Class Feed (0.6.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:08.254722+00:00
---

# Class Feed (0.6.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.Feed

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Feed (0.6.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.6.4 (latest)  0.6.3  0.5.0  0.4.0  0.3.0  0.2.0  0.1.0 
    
    
    Feed(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Feed is a resource that contains feed information needed to create a feed.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
The resource name of the feed. Format: projects/{project}/locations/{location}/instances/{instance}/feeds/{feed}   
`uid` |  `str`   
Output only. Unique identifier for the feed.   
`display_name` |  `str`   
Customer-provided feed name.   
`details` |  `[google.cloud.chronicle_v1.types.FeedDetails](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.FeedDetails)`   
Additional details of the feed, these details are dynamic and will be different for each of the feeds.   
`state` |  `[google.cloud.chronicle_v1.types.Feed.State](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.Feed.State)`   
Output only. State of the feed.   
`failure_msg` |  `str`   
Output only. Details about the most recent failure when feed state is FAILED.   
`read_only` |  `bool`   
Output only. Whether this feed can be updated or deleted.   
`last_feed_initiation_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Latest timestamp when the transfer was successful for the feed.   
`failure_details` |  `[google.cloud.chronicle_v1.types.FeedFailureDetails](https://docs.cloud.google.com/python/docs/reference/google-cloud-chronicle/latest/google.cloud.chronicle_v1.types.FeedFailureDetails)`   
Output only. Failure details for the feed. If the feed is in the failure state, this field will contain the details of the error cause and actions.   
`reference_id` |  `str`   
Output only. Reference ID, this field will contain the legacy id of the feed.   
  
## Classes 

### State
    
    
    State(value)

List of states a feed can have.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
