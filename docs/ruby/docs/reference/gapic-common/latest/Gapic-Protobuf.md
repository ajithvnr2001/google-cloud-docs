---
url: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Protobuf/
title: gapic-common - Module Gapic::Protobuf (v1.5.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:12.143482+00:00
---

# gapic-common - Module Gapic::Protobuf (v1.5.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/gapic-common/latest/Gapic-Protobuf/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  gapic-common - Module Gapic::Protobuf (v1.5.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.5.1 (latest)  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.26.0  0.25.0  0.24.0 

Reference documentation and code samples for the gapic-common module Gapic::Protobuf.

A set of internal utilities for coercing data to protobuf messages.

## Methods 

### .coerce
    
    
    def self.coerce(hash, to:) -> Object

Creates an instance of a protobuf message from a hash that may include nested hashes. `google/protobuf` allows for the instantiation of protobuf messages using hashes but does not allow for nested hashes to instantiate nested submessages.

**Parameters**

  * **hash** (Hash, Object) — The hash to be converted into a proto message. If an instance of the proto message class is given, it is returned unchanged. 
  * **to** (Class) — The corresponding protobuf message class of the given hash. 



**Returns**

  * (Object) — An instance of the given message class. 



**Raises**

  * (ArgumentError) 



### .time_to_timestamp
    
    
    def self.time_to_timestamp(time) -> Google::Protobuf::Timestamp

Utility for converting a Ruby Time instance to a Google::Protobuf::Timestamp.

**Parameter**

  * **time** (Time) — The Time to be converted. 



**Returns**

  * (Google::Protobuf::Timestamp) — The converted Google::Protobuf::Timestamp. 



### .timestamp_to_time
    
    
    def self.timestamp_to_time(timestamp) -> Time

Utility for converting a Google::Protobuf::Timestamp instance to a Ruby time.

**Parameter**

  * **timestamp** (Google::Protobuf::Timestamp) — The timestamp to be converted. 



**Returns**

  * (Time) — The converted Time. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
