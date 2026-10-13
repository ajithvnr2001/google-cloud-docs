---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-CreateIngressRuleRequest/
title: App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::CreateIngressRuleRequest (v1.8.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:48:18.233316+00:00
---

# App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::CreateIngressRuleRequest (v1.8.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-CreateIngressRuleRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  App Engine Admin V1 API - Class Google::Cloud::AppEngine::V1::CreateIngressRuleRequest (v1.8.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.2 (latest)  1.8.1  1.7.0  1.6.0  1.5.1  1.4.0  1.3.0  1.2.1  1.1.0  1.0.1  0.10.0  0.9.2  0.8.0  0.7.0  0.6.1  0.5.0  0.4.0  0.3.6 

Reference documentation and code samples for the App Engine Admin V1 API class Google::Cloud::AppEngine::V1::CreateIngressRuleRequest.

Request message for `Firewall.CreateIngressRule`.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Name of the parent Firewall collection in which to create a new rule. Example: `apps/myapp/firewall/ingressRules`. 



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Name of the parent Firewall collection in which to create a new rule. Example: `apps/myapp/firewall/ingressRules`. 



**Returns**

  * (::String) — Name of the parent Firewall collection in which to create a new rule. Example: `apps/myapp/firewall/ingressRules`. 



### #rule
    
    
    def rule() -> ::Google::Cloud::AppEngine::V1::FirewallRule

**Returns**

  * ([::Google::Cloud::AppEngine::V1::FirewallRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule)) — A FirewallRule containing the new resource.

The user may optionally provide a position at which the new rule will be placed. The positions define a sequential list starting at 1. If a rule already exists at the given position, rules greater than the provided position will be moved forward by one.

If no position is provided, the server will place the rule as the second to last rule in the sequence before the required default allow-all or deny-all rule. 




### #rule=
    
    
    def rule=(value) -> ::Google::Cloud::AppEngine::V1::FirewallRule

**Parameter**

  * **value** ([::Google::Cloud::AppEngine::V1::FirewallRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule)) — A FirewallRule containing the new resource.

The user may optionally provide a position at which the new rule will be placed. The positions define a sequential list starting at 1. If a rule already exists at the given position, rules greater than the provided position will be moved forward by one.

If no position is provided, the server will place the rule as the second to last rule in the sequence before the required default allow-all or deny-all rule. 




**Returns**

  * ([::Google::Cloud::AppEngine::V1::FirewallRule](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-app_engine-v1/latest/Google-Cloud-AppEngine-V1-FirewallRule)) — A FirewallRule containing the new resource.

The user may optionally provide a position at which the new rule will be placed. The positions define a sequential list starting at 1. If a rule already exists at the given position, rules greater than the provided position will be moved forward by one.

If no position is provided, the server will place the rule as the second to last rule in the sequence before the required default allow-all or deny-all rule. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
