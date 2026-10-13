---
url: https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.Tablet
title: Class Tablet (3.71.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:17:30.072909+00:00
---

# Class Tablet (3.71.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.Tablet

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Tablet (3.71.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.71.0 (latest)  3.70.0  3.69.1  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.1  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.0  3.23.0  3.22.2  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.1  3.14.1  3.13.0  3.12.1  3.11.1  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.1.1  2.0.0  1.19.3  1.18.0  1.17.1  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0 
    
    
    Tablet(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A `Tablet` represents a single replica of a `Group`. A tablet is served by a single server at a time, and can move between servers due to server death or simply load balancing.

## Attributes  
  
---  
**Name** | **Description**  
`tablet_uid` |  `int`   
The UID of the tablet, unique within the database. Matches the `tablet_uids` and `leader_tablet_uid` fields in `Group`.   
`server_address` |  `str`   
The address of the server that is serving this tablet -- either an IP address or DNS hostname and a port number.   
`location` |  `str`   
Where this tablet is located. This is the name of a Google Cloud region, such as "us-central1".   
`role` |  `[google.cloud.spanner_v1.types.Tablet.Role](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.Tablet.Role)`   
The role of the tablet.   
`incarnation` |  `bytes`   
`incarnation` indicates the freshness of the tablet information contained in this proto. Incarnations can be compared lexicographically; if incarnation A is greater than incarnation B, then the `Tablet` corresponding to A is newer than the `Tablet` corresponding to B, and should be used preferentially.   
`distance` |  `int`   
Distances help the client pick the closest tablet out of the list of tablets for a given request. Tablets with lower distances should generally be preferred. Tablets with the same distance are approximately equally close; the client can choose arbitrarily. Distances do not correspond precisely to expected latency, geographical distance, or anything else. Distances should be compared only between tablets of the same group; they are not meaningful between different groups. A value of zero indicates that the tablet may be in the same zone as the client, and have minimum network latency. A value less than or equal to five indicates that the tablet is thought to be in the same region as the client, and may have a few milliseconds of network latency. Values greater than five are most likely in a different region, with non-trivial network latency. Clients should use the following algorithm: \- If the request is using a directed read, eliminate any tablets that do not match the directed read's target zone and/or replica type. \- (Read-write transactions only) Choose leader tablet if it has an distance <=5. -="" group="" and="" sort="" tablets="" by="" distance.="" choose="" a="" random="" tablet="" with="" the="" lowest="" distance.="" if="" the="" request="" is="" not="" a="" directed="" read,="" only="" consider="" replicas="" with="" distances=""><=5. -="" send="" the="" request="" to="" the="" fallback="" endpoint.="" the="" tablet="" picked="" by="" this="" algorithm="" may="" be="" skipped,="" either="" because="" it="" is="" marked="" as="">`skip` by the server or because the corresponding server is unreachable, flow controlled, etc. Skipped tablets should be added to the `skipped_tablet_uid` field in `RoutingHint`; the algorithm above should then be re-run without including the skipped tablet(s) to pick the next best tablet.   
`skip` |  `bool`   
If true, the tablet should not be chosen by the client. Typically, this signals that the tablet is unhealthy in some way. Tablets with `skip` set to true should be reported back to the server in `RoutingHint.skipped_tablet_uid`; this cues the server to send updated information for this tablet should it become usable again.   
  
## Classes 

### Role
    
    
    Role(value)

Indicates the role of the tablet.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
