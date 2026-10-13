---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Cloud-PolicyTroubleshooter-Iam-V3-ConditionContext/
title: Policy Troubleshooter V3 API - Class Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext (v0.12.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:04.001003+00:00
---

# Policy Troubleshooter V3 API - Class Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext (v0.12.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Cloud-PolicyTroubleshooter-Iam-V3-ConditionContext/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Policy Troubleshooter V3 API - Class Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext (v0.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.12.0 (latest)  0.11.1  0.10.0  0.9.1  0.8.0  0.7.0  0.6.1  0.5.0  0.4.1  0.3.2  0.2.0  0.1.0 

Reference documentation and code samples for the Policy Troubleshooter V3 API class Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext.

Additional context for troubleshooting conditional role bindings and deny rules.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #destination
    
    
    def destination() -> ::Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Peer

**Returns**

  * ([::Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Peer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Cloud-PolicyTroubleshooter-Iam-V3-ConditionContext-Peer)) — The destination of a network activity, such as accepting a TCP connection. In a multi-hop network activity, the destination represents the receiver of the last hop. 



### #destination=
    
    
    def destination=(value) -> ::Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Peer

**Parameter**

  * **value** ([::Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Peer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Cloud-PolicyTroubleshooter-Iam-V3-ConditionContext-Peer)) — The destination of a network activity, such as accepting a TCP connection. In a multi-hop network activity, the destination represents the receiver of the last hop. 



**Returns**

  * ([::Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Peer](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Cloud-PolicyTroubleshooter-Iam-V3-ConditionContext-Peer)) — The destination of a network activity, such as accepting a TCP connection. In a multi-hop network activity, the destination represents the receiver of the last hop. 



### #effective_tags
    
    
    def effective_tags() -> ::Array<::Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::EffectiveTag>

**Returns**

  * (::Array<[::Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::EffectiveTag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Cloud-PolicyTroubleshooter-Iam-V3-ConditionContext-EffectiveTag)>) — Output only. The effective tags on the resource. The effective tags are fetched during troubleshooting. 



### #request
    
    
    def request() -> ::Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Request

**Returns**

  * ([::Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Request](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Cloud-PolicyTroubleshooter-Iam-V3-ConditionContext-Request)) — Represents a network request, such as an HTTP request. 



### #request=
    
    
    def request=(value) -> ::Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Request

**Parameter**

  * **value** ([::Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Request](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Cloud-PolicyTroubleshooter-Iam-V3-ConditionContext-Request)) — Represents a network request, such as an HTTP request. 



**Returns**

  * ([::Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Request](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Cloud-PolicyTroubleshooter-Iam-V3-ConditionContext-Request)) — Represents a network request, such as an HTTP request. 



### #resource
    
    
    def resource() -> ::Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Resource

**Returns**

  * ([::Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Cloud-PolicyTroubleshooter-Iam-V3-ConditionContext-Resource)) — Represents a target resource that is involved with a network activity. If multiple resources are involved with an activity, this must be the primary one. 



### #resource=
    
    
    def resource=(value) -> ::Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Resource

**Parameter**

  * **value** ([::Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Cloud-PolicyTroubleshooter-Iam-V3-ConditionContext-Resource)) — Represents a target resource that is involved with a network activity. If multiple resources are involved with an activity, this must be the primary one. 



**Returns**

  * ([::Google::Cloud::PolicyTroubleshooter::Iam::V3::ConditionContext::Resource](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-policy_troubleshooter-iam-v3/latest/Google-Cloud-PolicyTroubleshooter-Iam-V3-ConditionContext-Resource)) — Represents a target resource that is involved with a network activity. If multiple resources are involved with an activity, this must be the primary one. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
