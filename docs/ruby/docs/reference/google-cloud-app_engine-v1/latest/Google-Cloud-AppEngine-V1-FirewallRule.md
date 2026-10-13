---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::FirewallRule (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:24.847823+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::FirewallRule (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::FirewallRule (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::FirewallRule.

A single firewall rule that is evaluated against incoming traffic and provides an action to take on matched requests.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #action
    
    
    def action() -> ::Google::Cloud::AppEngine::V1::FirewallRule::Action

**Returns**

  * ([::Google::Cloud::AppEngine::V1::FirewallRule::Action](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule-Action)) — The action to take on matched requests. 



### #action=
    
    
    def action=(value) -> ::Google::Cloud::AppEngine::V1::FirewallRule::Action

**Parameter**

  * **value** ([::Google::Cloud::AppEngine::V1::FirewallRule::Action](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule-Action)) — The action to take on matched requests. 



**Returns**

  * ([::Google::Cloud::AppEngine::V1::FirewallRule::Action](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule-Action)) — The action to take on matched requests. 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — An optional string description of this rule. This field has a maximum length of 100 characters. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — An optional string description of this rule. This field has a maximum length of 100 characters. 



**Returns**

  * (::String) — An optional string description of this rule. This field has a maximum length of 100 characters. 



### #priority
    
    
    def priority() -> ::Integer

**Returns**

  * (::Integer) — A positive integer between [1, Int32.MaxValue-1] that defines the order of rule evaluation. Rules with the lowest priority are evaluated first.

A default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic when no previous rule matches. Only the action of this rule can be modified by the user. 




### #priority=
    
    
    def priority=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — A positive integer between [1, Int32.MaxValue-1] that defines the order of rule evaluation. Rules with the lowest priority are evaluated first.

A default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic when no previous rule matches. Only the action of this rule can be modified by the user. 




**Returns**

  * (::Integer) — A positive integer between [1, Int32.MaxValue-1] that defines the order of rule evaluation. Rules with the lowest priority are evaluated first.

A default rule at priority Int32.MaxValue matches all IPv4 and IPv6 traffic when no previous rule matches. Only the action of this rule can be modified by the user. 




### #source_range
    
    
    def source_range() -> ::String

**Returns**

  * (::String) — IP address or range, defined using CIDR notation, of requests that this rule applies to. You can use the wildcard character "*" to match all IPs equivalent to "0/0" and "::/0" together. Examples: `192.168.1.1` or `192.168.0.0/16` or `2001:db8::/32` or `2001:0db8:0000:0042:0000:8a2e:0370:7334`.

Truncation will be silently performed on addresses which are not properly truncated. For example, `1.2.3.4/24` is accepted as the same address as `1.2.3.0/24`. Similarly, for IPv6, `2001:db8::1/32` is accepted as the same address as `2001:db8::/32`. 




### #source_range=
    
    
    def source_range=(value) -> ::String

**Parameter**

  * **value** (::String) — IP address or range, defined using CIDR notation, of requests that this rule applies to. You can use the wildcard character "*" to match all IPs equivalent to "0/0" and "::/0" together. Examples: `192.168.1.1` or `192.168.0.0/16` or `2001:db8::/32` or `2001:0db8:0000:0042:0000:8a2e:0370:7334`.

Truncation will be silently performed on addresses which are not properly truncated. For example, `1.2.3.4/24` is accepted as the same address as `1.2.3.0/24`. Similarly, for IPv6, `2001:db8::1/32` is accepted as the same address as `2001:db8::/32`. 




**Returns**

  * (::String) — IP address or range, defined using CIDR notation, of requests that this rule applies to. You can use the wildcard character "*" to match all IPs equivalent to "0/0" and "::/0" together. Examples: `192.168.1.1` or `192.168.0.0/16` or `2001:db8::/32` or `2001:0db8:0000:0042:0000:8a2e:0370:7334`.

Truncation will be silently performed on addresses which are not properly truncated. For example, `1.2.3.4/24` is accepted as the same address as `1.2.3.0/24`. Similarly, for IPv6, `2001:db8::1/32` is accepted as the same address as `2001:db8::/32`. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
