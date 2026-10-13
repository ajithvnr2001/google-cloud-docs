---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3/
title: Cloud OS Config V1alpha API - Class Google::Cloud::OsConfig::V1alpha::CVSSv3 (v0.17.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:36:51.299162+00:00
---

# Cloud OS Config V1alpha API - Class Google::Cloud::OsConfig::V1alpha::CVSSv3 (v0.17.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud OS Config V1alpha API - Class Google::Cloud::OsConfig::V1alpha::CVSSv3 (v0.17.0) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.0 (latest)  0.16.1  0.15.0  0.14.1  0.13.0  0.12.0  0.11.1  0.10.0  0.9.1  0.8.2  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.2 

Reference documentation and code samples for the Cloud OS Config V1alpha API class Google::Cloud::OsConfig::V1alpha::CVSSv3.

Common Vulnerability Scoring System version 3. For details, see <https://www.first.org/cvss/specification-document>

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #attack_complexity
    
    
    def attack_complexity() -> ::Google::Cloud::OsConfig::V1alpha::CVSSv3::AttackComplexity

**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::AttackComplexity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-AttackComplexity)) — This metric describes the conditions beyond the attacker's control that must exist in order to exploit the vulnerability. 



### #attack_complexity=
    
    
    def attack_complexity=(value) -> ::Google::Cloud::OsConfig::V1alpha::CVSSv3::AttackComplexity

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::AttackComplexity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-AttackComplexity)) — This metric describes the conditions beyond the attacker's control that must exist in order to exploit the vulnerability. 



**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::AttackComplexity](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-AttackComplexity)) — This metric describes the conditions beyond the attacker's control that must exist in order to exploit the vulnerability. 



### #attack_vector
    
    
    def attack_vector() -> ::Google::Cloud::OsConfig::V1alpha::CVSSv3::AttackVector

**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::AttackVector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-AttackVector)) — This metric reflects the context by which vulnerability exploitation is possible. 



### #attack_vector=
    
    
    def attack_vector=(value) -> ::Google::Cloud::OsConfig::V1alpha::CVSSv3::AttackVector

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::AttackVector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-AttackVector)) — This metric reflects the context by which vulnerability exploitation is possible. 



**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::AttackVector](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-AttackVector)) — This metric reflects the context by which vulnerability exploitation is possible. 



### #availability_impact
    
    
    def availability_impact() -> ::Google::Cloud::OsConfig::V1alpha::CVSSv3::Impact

**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::Impact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-Impact)) — This metric measures the impact to the availability of the impacted component resulting from a successfully exploited vulnerability. 



### #availability_impact=
    
    
    def availability_impact=(value) -> ::Google::Cloud::OsConfig::V1alpha::CVSSv3::Impact

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::Impact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-Impact)) — This metric measures the impact to the availability of the impacted component resulting from a successfully exploited vulnerability. 



**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::Impact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-Impact)) — This metric measures the impact to the availability of the impacted component resulting from a successfully exploited vulnerability. 



### #base_score
    
    
    def base_score() -> ::Float

**Returns**

  * (::Float) — The base score is a function of the base metric scores. https://www.first.org/cvss/specification-document#Base-Metrics 



### #base_score=
    
    
    def base_score=(value) -> ::Float

**Parameter**

  * **value** (::Float) — The base score is a function of the base metric scores. https://www.first.org/cvss/specification-document#Base-Metrics 



**Returns**

  * (::Float) — The base score is a function of the base metric scores. https://www.first.org/cvss/specification-document#Base-Metrics 



### #confidentiality_impact
    
    
    def confidentiality_impact() -> ::Google::Cloud::OsConfig::V1alpha::CVSSv3::Impact

**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::Impact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-Impact)) — This metric measures the impact to the confidentiality of the information resources managed by a software component due to a successfully exploited vulnerability. 



### #confidentiality_impact=
    
    
    def confidentiality_impact=(value) -> ::Google::Cloud::OsConfig::V1alpha::CVSSv3::Impact

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::Impact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-Impact)) — This metric measures the impact to the confidentiality of the information resources managed by a software component due to a successfully exploited vulnerability. 



**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::Impact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-Impact)) — This metric measures the impact to the confidentiality of the information resources managed by a software component due to a successfully exploited vulnerability. 



### #exploitability_score
    
    
    def exploitability_score() -> ::Float

**Returns**

  * (::Float) — The Exploitability sub-score equation is derived from the Base Exploitability metrics. https://www.first.org/cvss/specification-document#2-1-Exploitability-Metrics 



### #exploitability_score=
    
    
    def exploitability_score=(value) -> ::Float

**Parameter**

  * **value** (::Float) — The Exploitability sub-score equation is derived from the Base Exploitability metrics. https://www.first.org/cvss/specification-document#2-1-Exploitability-Metrics 



**Returns**

  * (::Float) — The Exploitability sub-score equation is derived from the Base Exploitability metrics. https://www.first.org/cvss/specification-document#2-1-Exploitability-Metrics 



### #impact_score
    
    
    def impact_score() -> ::Float

**Returns**

  * (::Float) — The Impact sub-score equation is derived from the Base Impact metrics. 



### #impact_score=
    
    
    def impact_score=(value) -> ::Float

**Parameter**

  * **value** (::Float) — The Impact sub-score equation is derived from the Base Impact metrics. 



**Returns**

  * (::Float) — The Impact sub-score equation is derived from the Base Impact metrics. 



### #integrity_impact
    
    
    def integrity_impact() -> ::Google::Cloud::OsConfig::V1alpha::CVSSv3::Impact

**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::Impact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-Impact)) — This metric measures the impact to integrity of a successfully exploited vulnerability. 



### #integrity_impact=
    
    
    def integrity_impact=(value) -> ::Google::Cloud::OsConfig::V1alpha::CVSSv3::Impact

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::Impact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-Impact)) — This metric measures the impact to integrity of a successfully exploited vulnerability. 



**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::Impact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-Impact)) — This metric measures the impact to integrity of a successfully exploited vulnerability. 



### #privileges_required
    
    
    def privileges_required() -> ::Google::Cloud::OsConfig::V1alpha::CVSSv3::PrivilegesRequired

**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::PrivilegesRequired](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-PrivilegesRequired)) — This metric describes the level of privileges an attacker must possess before successfully exploiting the vulnerability. 



### #privileges_required=
    
    
    def privileges_required=(value) -> ::Google::Cloud::OsConfig::V1alpha::CVSSv3::PrivilegesRequired

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::PrivilegesRequired](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-PrivilegesRequired)) — This metric describes the level of privileges an attacker must possess before successfully exploiting the vulnerability. 



**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::PrivilegesRequired](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-PrivilegesRequired)) — This metric describes the level of privileges an attacker must possess before successfully exploiting the vulnerability. 



### #scope
    
    
    def scope() -> ::Google::Cloud::OsConfig::V1alpha::CVSSv3::Scope

**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::Scope](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-Scope)) — The Scope metric captures whether a vulnerability in one vulnerable component impacts resources in components beyond its security scope. 



### #scope=
    
    
    def scope=(value) -> ::Google::Cloud::OsConfig::V1alpha::CVSSv3::Scope

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::Scope](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-Scope)) — The Scope metric captures whether a vulnerability in one vulnerable component impacts resources in components beyond its security scope. 



**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::Scope](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-Scope)) — The Scope metric captures whether a vulnerability in one vulnerable component impacts resources in components beyond its security scope. 



### #user_interaction
    
    
    def user_interaction() -> ::Google::Cloud::OsConfig::V1alpha::CVSSv3::UserInteraction

**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::UserInteraction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-UserInteraction)) — This metric captures the requirement for a human user, other than the attacker, to participate in the successful compromise of the vulnerable component. 



### #user_interaction=
    
    
    def user_interaction=(value) -> ::Google::Cloud::OsConfig::V1alpha::CVSSv3::UserInteraction

**Parameter**

  * **value** ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::UserInteraction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-UserInteraction)) — This metric captures the requirement for a human user, other than the attacker, to participate in the successful compromise of the vulnerable component. 



**Returns**

  * ([::Google::Cloud::OsConfig::V1alpha::CVSSv3::UserInteraction](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-os_config-v1alpha/latest/Google-Cloud-OsConfig-V1alpha-CVSSv3-UserInteraction)) — This metric captures the requirement for a human user, other than the attacker, to participate in the successful compromise of the vulnerable component. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
