---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1beta/latest/Google-Type-Interval/
title: Cloud Controls Partner V1BETA API - Class Google::Type::Interval (v0.9.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:52:12.257741+00:00
---

# Cloud Controls Partner V1BETA API - Class Google::Type::Interval (v0.9.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1beta/latest/Google-Type-Interval/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Controls Partner V1BETA API - Class Google::Type::Interval (v0.9.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.9.1 (latest)  0.9.0  0.8.0  0.7.1  0.6.0  0.5.1  0.4.0  0.3.0  0.2.0  0.1.2 

Reference documentation and code samples for the Cloud Controls Partner V1BETA API class Google::Type::Interval.

Represents a time interval, encoded as a Timestamp start (inclusive) and a Timestamp end (exclusive).

The start must be less than or equal to the end. When the start equals the end, the interval is empty (matches no time). When both start and end are unspecified, the interval matches any time.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #end_time
    
    
    def end_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1beta/latest/Google-Protobuf-Timestamp)) — Optional. Exclusive end of the interval.

If specified, a Timestamp matching this interval will have to be before the end. 




### #end_time=
    
    
    def end_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1beta/latest/Google-Protobuf-Timestamp)) — Optional. Exclusive end of the interval.

If specified, a Timestamp matching this interval will have to be before the end. 




**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1beta/latest/Google-Protobuf-Timestamp)) — Optional. Exclusive end of the interval.

If specified, a Timestamp matching this interval will have to be before the end. 




### #start_time
    
    
    def start_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1beta/latest/Google-Protobuf-Timestamp)) — Optional. Inclusive start of the interval.

If specified, a Timestamp matching this interval will have to be the same or after the start. 




### #start_time=
    
    
    def start_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1beta/latest/Google-Protobuf-Timestamp)) — Optional. Inclusive start of the interval.

If specified, a Timestamp matching this interval will have to be the same or after the start. 




**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-cloud_controls_partner-v1beta/latest/Google-Protobuf-Timestamp)) — Optional. Inclusive start of the interval.

If specified, a Timestamp matching this interval will have to be the same or after the start. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
