---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Api-FieldInfo-Format/
title: Storage Control V2 API - Module Google::Api::FieldInfo::Format (v1.14.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:11:31.534854+00:00
---

# Storage Control V2 API - Module Google::Api::FieldInfo::Format (v1.14.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-storage-control-v2/latest/Google-Api-FieldInfo-Format/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Storage Control V2 API - Module Google::Api::FieldInfo::Format (v1.14.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.14.1 (latest)  1.14.0  1.13.1  1.12.0  1.11.0  1.10.1  1.9.0  1.8.1  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.1.1 

Reference documentation and code samples for the Storage Control V2 API module Google::Api::FieldInfo::Format.

The standard format of a field value. The supported formats are all backed by either an RFC defined by the IETF or a Google-defined AIP.

## Constants 

### FORMAT_UNSPECIFIED

**value:** 0  
Default, unspecified value.

### UUID4

**value:** 1  
Universally Unique Identifier, version 4, value as defined by <https://datatracker.ietf.org/doc/html/rfc4122>. The value may be normalized to entirely lowercase letters. For example, the value `F47AC10B-58CC-0372-8567-0E02B2C3D479` would be normalized to `f47ac10b-58cc-0372-8567-0e02b2c3d479`.

### IPV4

**value:** 2  
Internet Protocol v4 value as defined by [RFC 791](https://datatracker.ietf.org/doc/html/rfc791). The value may be condensed, with leading zeros in each octet stripped. For example, `001.022.233.040` would be condensed to `1.22.233.40`.

### IPV6

**value:** 3  
Internet Protocol v6 value as defined by [RFC 2460](https://datatracker.ietf.org/doc/html/rfc2460). The value may be normalized to entirely lowercase letters with zeros compressed, following [RFC 5952](https://datatracker.ietf.org/doc/html/rfc5952). For example, the value `2001:0DB8:0::0` would be normalized to `2001:db8::`.

### IPV4_OR_IPV6

**value:** 4  
An IP address in either v4 or v6 format as described by the individual values defined herein. See the comments on the IPV4 and IPV6 types for allowed normalizations of each.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
