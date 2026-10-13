---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-UptimeCheckIp/
title: Cloud Monitoring V3 API - Class Google::Cloud::Monitoring::V3::UptimeCheckIp (v1.10.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:44:29.909634+00:00
---

# Cloud Monitoring V3 API - Class Google::Cloud::Monitoring::V3::UptimeCheckIp (v1.10.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-UptimeCheckIp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Monitoring V3 API - Class Google::Cloud::Monitoring::V3::UptimeCheckIp (v1.10.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.10.1 (latest)  1.10.0  1.9.0  1.8.0  1.7.1  1.6.1  1.5.1  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1  0.18.0  0.17.0  0.16.0  0.15.2  0.14.0  0.13.0  0.12.1  0.11.0  0.10.0  0.9.0  0.8.0  0.7.1 

Reference documentation and code samples for the Cloud Monitoring V3 API class Google::Cloud::Monitoring::V3::UptimeCheckIp.

Contains the region, location, and list of IP addresses where checkers in the location run from.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #ip_address
    
    
    def ip_address() -> ::String

**Returns**

  * (::String) — The IP address from which the Uptime check originates. This is a fully specified IP address (not an IP address range). Most IP addresses, as of this publication, are in IPv4 format; however, one should not rely on the IP addresses being in IPv4 format indefinitely, and should support interpreting this field in either IPv4 or IPv6 format. 



### #ip_address=
    
    
    def ip_address=(value) -> ::String

**Parameter**

  * **value** (::String) — The IP address from which the Uptime check originates. This is a fully specified IP address (not an IP address range). Most IP addresses, as of this publication, are in IPv4 format; however, one should not rely on the IP addresses being in IPv4 format indefinitely, and should support interpreting this field in either IPv4 or IPv6 format. 



**Returns**

  * (::String) — The IP address from which the Uptime check originates. This is a fully specified IP address (not an IP address range). Most IP addresses, as of this publication, are in IPv4 format; however, one should not rely on the IP addresses being in IPv4 format indefinitely, and should support interpreting this field in either IPv4 or IPv6 format. 



### #location
    
    
    def location() -> ::String

**Returns**

  * (::String) — A more specific location within the region that typically encodes a particular city/town/metro (and its containing state/province or country) within the broader umbrella region category. 



### #location=
    
    
    def location=(value) -> ::String

**Parameter**

  * **value** (::String) — A more specific location within the region that typically encodes a particular city/town/metro (and its containing state/province or country) within the broader umbrella region category. 



**Returns**

  * (::String) — A more specific location within the region that typically encodes a particular city/town/metro (and its containing state/province or country) within the broader umbrella region category. 



### #region
    
    
    def region() -> ::Google::Cloud::Monitoring::V3::UptimeCheckRegion

**Returns**

  * ([::Google::Cloud::Monitoring::V3::UptimeCheckRegion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-UptimeCheckRegion)) — A broad region category in which the IP address is located. 



### #region=
    
    
    def region=(value) -> ::Google::Cloud::Monitoring::V3::UptimeCheckRegion

**Parameter**

  * **value** ([::Google::Cloud::Monitoring::V3::UptimeCheckRegion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-UptimeCheckRegion)) — A broad region category in which the IP address is located. 



**Returns**

  * ([::Google::Cloud::Monitoring::V3::UptimeCheckRegion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-monitoring-v3/latest/Google-Cloud-Monitoring-V3-UptimeCheckRegion)) — A broad region category in which the IP address is located. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
