---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-Tablet/
title: Cloud Spanner V1 API - Class Google::Cloud::Spanner::V1::Tablet (v1.19.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:29:38.193740+00:00
---

# Cloud Spanner V1 API - Class Google::Cloud::Spanner::V1::Tablet (v1.19.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-Tablet/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Spanner V1 API - Class Google::Cloud::Spanner::V1::Tablet (v1.19.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.19.2 (latest)  1.19.1  1.18.0  1.17.1  1.16.0  1.15.0  1.14.0  1.13.0  1.12.1  1.11.1  1.10.1  1.9.1  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.2  0.27.0  0.26.0  0.25.0  0.24.0  0.23.0  0.22.2  0.21.0  0.20.1  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.1  0.13.0  0.12.0  0.11.0  0.10.0  0.9.0  0.8.1  0.7.4 

Reference documentation and code samples for the Cloud Spanner V1 API class Google::Cloud::Spanner::V1::Tablet.

A `Tablet` represents a single replica of a `Group`. A tablet is served by a single server at a time, and can move between servers due to server death or simply load balancing.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #distance
    
    
    def distance() -> ::Integer

**Returns**

  * (::Integer) — Distances help the client pick the closest tablet out of the list of tablets for a given request. Tablets with lower distances should generally be preferred. Tablets with the same distance are approximately equally close; the client can choose arbitrarily.

Distances do not correspond precisely to expected latency, geographical distance, or anything else. Distances should be compared only between tablets of the same group; they are not meaningful between different groups.

A value of zero indicates that the tablet may be in the same zone as the client, and have minimum network latency. A value less than or equal to five indicates that the tablet is thought to be in the same region as the client, and may have a few milliseconds of network latency. Values greater than five are most likely in a different region, with non-trivial network latency.

Clients should use the following algorithm:

    * If the request is using a directed read, eliminate any tablets that do not match the directed read's target zone and/or replica type.
    * (Read-write transactions only) Choose leader tablet if it has an distance <=5.
    * Group and sort tablets by distance. Choose a random tablet with the lowest distance. If the request is not a directed read, only consider replicas with distances <=5.
    * Send the request to the fallback endpoint.

The tablet picked by this algorithm may be skipped, either because it is marked as `skip` by the server or because the corresponding server is unreachable, flow controlled, etc. Skipped tablets should be added to the `skipped_tablet_uid` field in `RoutingHint`; the algorithm above should then be re-run without including the skipped tablet(s) to pick the next best tablet. 




### #distance=
    
    
    def distance=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Distances help the client pick the closest tablet out of the list of tablets for a given request. Tablets with lower distances should generally be preferred. Tablets with the same distance are approximately equally close; the client can choose arbitrarily.

Distances do not correspond precisely to expected latency, geographical distance, or anything else. Distances should be compared only between tablets of the same group; they are not meaningful between different groups.

A value of zero indicates that the tablet may be in the same zone as the client, and have minimum network latency. A value less than or equal to five indicates that the tablet is thought to be in the same region as the client, and may have a few milliseconds of network latency. Values greater than five are most likely in a different region, with non-trivial network latency.

Clients should use the following algorithm:

    * If the request is using a directed read, eliminate any tablets that do not match the directed read's target zone and/or replica type.
    * (Read-write transactions only) Choose leader tablet if it has an distance <=5.
    * Group and sort tablets by distance. Choose a random tablet with the lowest distance. If the request is not a directed read, only consider replicas with distances <=5.
    * Send the request to the fallback endpoint.

The tablet picked by this algorithm may be skipped, either because it is marked as `skip` by the server or because the corresponding server is unreachable, flow controlled, etc. Skipped tablets should be added to the `skipped_tablet_uid` field in `RoutingHint`; the algorithm above should then be re-run without including the skipped tablet(s) to pick the next best tablet. 




**Returns**

  * (::Integer) — Distances help the client pick the closest tablet out of the list of tablets for a given request. Tablets with lower distances should generally be preferred. Tablets with the same distance are approximately equally close; the client can choose arbitrarily.

Distances do not correspond precisely to expected latency, geographical distance, or anything else. Distances should be compared only between tablets of the same group; they are not meaningful between different groups.

A value of zero indicates that the tablet may be in the same zone as the client, and have minimum network latency. A value less than or equal to five indicates that the tablet is thought to be in the same region as the client, and may have a few milliseconds of network latency. Values greater than five are most likely in a different region, with non-trivial network latency.

Clients should use the following algorithm:

    * If the request is using a directed read, eliminate any tablets that do not match the directed read's target zone and/or replica type.
    * (Read-write transactions only) Choose leader tablet if it has an distance <=5.
    * Group and sort tablets by distance. Choose a random tablet with the lowest distance. If the request is not a directed read, only consider replicas with distances <=5.
    * Send the request to the fallback endpoint.

The tablet picked by this algorithm may be skipped, either because it is marked as `skip` by the server or because the corresponding server is unreachable, flow controlled, etc. Skipped tablets should be added to the `skipped_tablet_uid` field in `RoutingHint`; the algorithm above should then be re-run without including the skipped tablet(s) to pick the next best tablet. 




### #incarnation
    
    
    def incarnation() -> ::String

**Returns**

  * (::String) — `incarnation` indicates the freshness of the tablet information contained in this proto. Incarnations can be compared lexicographically; if incarnation A is greater than incarnation B, then the `Tablet` corresponding to A is newer than the `Tablet` corresponding to B, and should be used preferentially. 



### #incarnation=
    
    
    def incarnation=(value) -> ::String

**Parameter**

  * **value** (::String) — `incarnation` indicates the freshness of the tablet information contained in this proto. Incarnations can be compared lexicographically; if incarnation A is greater than incarnation B, then the `Tablet` corresponding to A is newer than the `Tablet` corresponding to B, and should be used preferentially. 



**Returns**

  * (::String) — `incarnation` indicates the freshness of the tablet information contained in this proto. Incarnations can be compared lexicographically; if incarnation A is greater than incarnation B, then the `Tablet` corresponding to A is newer than the `Tablet` corresponding to B, and should be used preferentially. 



### #location
    
    
    def location() -> ::String

**Returns**

  * (::String) — Where this tablet is located. This is the name of a Google Cloud region, such as "us-central1". 



### #location=
    
    
    def location=(value) -> ::String

**Parameter**

  * **value** (::String) — Where this tablet is located. This is the name of a Google Cloud region, such as "us-central1". 



**Returns**

  * (::String) — Where this tablet is located. This is the name of a Google Cloud region, such as "us-central1". 



### #role
    
    
    def role() -> ::Google::Cloud::Spanner::V1::Tablet::Role

**Returns**

  * ([::Google::Cloud::Spanner::V1::Tablet::Role](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-Tablet-Role)) — The role of the tablet. 



### #role=
    
    
    def role=(value) -> ::Google::Cloud::Spanner::V1::Tablet::Role

**Parameter**

  * **value** ([::Google::Cloud::Spanner::V1::Tablet::Role](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-Tablet-Role)) — The role of the tablet. 



**Returns**

  * ([::Google::Cloud::Spanner::V1::Tablet::Role](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-spanner-v1/latest/Google-Cloud-Spanner-V1-Tablet-Role)) — The role of the tablet. 



### #server_address
    
    
    def server_address() -> ::String

**Returns**

  * (::String) — The address of the server that is serving this tablet -- either an IP address or DNS hostname and a port number. 



### #server_address=
    
    
    def server_address=(value) -> ::String

**Parameter**

  * **value** (::String) — The address of the server that is serving this tablet -- either an IP address or DNS hostname and a port number. 



**Returns**

  * (::String) — The address of the server that is serving this tablet -- either an IP address or DNS hostname and a port number. 



### #skip
    
    
    def skip() -> ::Boolean

**Returns**

  * (::Boolean) — If true, the tablet should not be chosen by the client. Typically, this signals that the tablet is unhealthy in some way. Tablets with `skip` set to true should be reported back to the server in `RoutingHint.skipped_tablet_uid`; this cues the server to send updated information for this tablet should it become usable again. 



### #skip=
    
    
    def skip=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — If true, the tablet should not be chosen by the client. Typically, this signals that the tablet is unhealthy in some way. Tablets with `skip` set to true should be reported back to the server in `RoutingHint.skipped_tablet_uid`; this cues the server to send updated information for this tablet should it become usable again. 



**Returns**

  * (::Boolean) — If true, the tablet should not be chosen by the client. Typically, this signals that the tablet is unhealthy in some way. Tablets with `skip` set to true should be reported back to the server in `RoutingHint.skipped_tablet_uid`; this cues the server to send updated information for this tablet should it become usable again. 



### #tablet_uid
    
    
    def tablet_uid() -> ::Integer

**Returns**

  * (::Integer) — The UID of the tablet, unique within the database. Matches the `tablet_uids` and `leader_tablet_uid` fields in `Group`. 



### #tablet_uid=
    
    
    def tablet_uid=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — The UID of the tablet, unique within the database. Matches the `tablet_uids` and `leader_tablet_uid` fields in `Group`. 



**Returns**

  * (::Integer) — The UID of the tablet, unique within the database. Matches the `tablet_uids` and `leader_tablet_uid` fields in `Group`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
