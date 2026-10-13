---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-FirewallPolicyRule/
title: Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::FirewallPolicyRule (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:21:23.711900+00:00
---

# Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::FirewallPolicyRule (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-FirewallPolicyRule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Class Google::Cloud::Compute::V1::FirewallPolicyRule (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API class Google::Cloud::Compute::V1::FirewallPolicyRule.

Represents a rule that describes one or more match conditions along with the action to be taken when traffic matches this condition (allow or deny).

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #action
    
    
    def action() -> ::String

**Returns**

  * (::String) — The Action to perform when the client connection triggers the rule. Valid actions for firewall rules are: "allow", "deny", "apply_security_profile_group" and "goto_next" ( "apply_security_profile_group" can be specified only for global network firewall policies or hierarchical firewall policies). Valid actions for packet mirroring rules are: "mirror", "do_not_mirror" and "goto_next". 



### #action=
    
    
    def action=(value) -> ::String

**Parameter**

  * **value** (::String) — The Action to perform when the client connection triggers the rule. Valid actions for firewall rules are: "allow", "deny", "apply_security_profile_group" and "goto_next" ( "apply_security_profile_group" can be specified only for global network firewall policies or hierarchical firewall policies). Valid actions for packet mirroring rules are: "mirror", "do_not_mirror" and "goto_next". 



**Returns**

  * (::String) — The Action to perform when the client connection triggers the rule. Valid actions for firewall rules are: "allow", "deny", "apply_security_profile_group" and "goto_next" ( "apply_security_profile_group" can be specified only for global network firewall policies or hierarchical firewall policies). Valid actions for packet mirroring rules are: "mirror", "do_not_mirror" and "goto_next". 



### #description
    
    
    def description() -> ::String

**Returns**

  * (::String) — An optional description for this resource. 



### #description=
    
    
    def description=(value) -> ::String

**Parameter**

  * **value** (::String) — An optional description for this resource. 



**Returns**

  * (::String) — An optional description for this resource. 



### #direction
    
    
    def direction() -> ::String

**Returns**

  * (::String) — The direction in which this rule applies. Check the Direction enum for the list of possible values. 



### #direction=
    
    
    def direction=(value) -> ::String

**Parameter**

  * **value** (::String) — The direction in which this rule applies. Check the Direction enum for the list of possible values. 



**Returns**

  * (::String) — The direction in which this rule applies. Check the Direction enum for the list of possible values. 



### #disabled
    
    
    def disabled() -> ::Boolean

**Returns**

  * (::Boolean) — Denotes whether the firewall policy rule is disabled. When set to true, the firewall policy rule is not enforced and traffic behaves as if it did not exist. If this is unspecified, the firewall policy rule will be enabled. 



### #disabled=
    
    
    def disabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Denotes whether the firewall policy rule is disabled. When set to true, the firewall policy rule is not enforced and traffic behaves as if it did not exist. If this is unspecified, the firewall policy rule will be enabled. 



**Returns**

  * (::Boolean) — Denotes whether the firewall policy rule is disabled. When set to true, the firewall policy rule is not enforced and traffic behaves as if it did not exist. If this is unspecified, the firewall policy rule will be enabled. 



### #enable_logging
    
    
    def enable_logging() -> ::Boolean

**Returns**

  * (::Boolean) — Denotes whether to enable logging for a particular rule. If logging is enabled, logs will be exported to the configured export destination in Stackdriver. Logs may be exported to BigQuery or Pub/Sub. Note: you cannot enable logging on "goto_next" rules. 



### #enable_logging=
    
    
    def enable_logging=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Denotes whether to enable logging for a particular rule. If logging is enabled, logs will be exported to the configured export destination in Stackdriver. Logs may be exported to BigQuery or Pub/Sub. Note: you cannot enable logging on "goto_next" rules. 



**Returns**

  * (::Boolean) — Denotes whether to enable logging for a particular rule. If logging is enabled, logs will be exported to the configured export destination in Stackdriver. Logs may be exported to BigQuery or Pub/Sub. Note: you cannot enable logging on "goto_next" rules. 



### #kind
    
    
    def kind() -> ::String

**Returns**

  * (::String) — Output only. [Output only] Type of the resource. Returnscompute#firewallPolicyRule for firewall rules andcompute#packetMirroringRule for packet mirroring rules. 



### #kind=
    
    
    def kind=(value) -> ::String

**Parameter**

  * **value** (::String) — Output only. [Output only] Type of the resource. Returnscompute#firewallPolicyRule for firewall rules andcompute#packetMirroringRule for packet mirroring rules. 



**Returns**

  * (::String) — Output only. [Output only] Type of the resource. Returnscompute#firewallPolicyRule for firewall rules andcompute#packetMirroringRule for packet mirroring rules. 



### #match
    
    
    def match() -> ::Google::Cloud::Compute::V1::FirewallPolicyRuleMatcher

**Returns**

  * ([::Google::Cloud::Compute::V1::FirewallPolicyRuleMatcher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-FirewallPolicyRuleMatcher)) — A match condition that incoming traffic is evaluated against. If it evaluates to true, the corresponding 'action' is enforced. 



### #match=
    
    
    def match=(value) -> ::Google::Cloud::Compute::V1::FirewallPolicyRuleMatcher

**Parameter**

  * **value** ([::Google::Cloud::Compute::V1::FirewallPolicyRuleMatcher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-FirewallPolicyRuleMatcher)) — A match condition that incoming traffic is evaluated against. If it evaluates to true, the corresponding 'action' is enforced. 



**Returns**

  * ([::Google::Cloud::Compute::V1::FirewallPolicyRuleMatcher](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-FirewallPolicyRuleMatcher)) — A match condition that incoming traffic is evaluated against. If it evaluates to true, the corresponding 'action' is enforced. 



### #priority
    
    
    def priority() -> ::Integer

**Returns**

  * (::Integer) — An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest priority. 



### #priority=
    
    
    def priority=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest priority. 



**Returns**

  * (::Integer) — An integer indicating the priority of a rule in the list. The priority must be a positive value between 0 and 2147483647. Rules are evaluated from highest to lowest priority where 0 is the highest priority and 2147483647 is the lowest priority. 



### #rule_name
    
    
    def rule_name() -> ::String

**Returns**

  * (::String) — An optional name for the rule. This field is not a unique identifier and can be updated. 



### #rule_name=
    
    
    def rule_name=(value) -> ::String

**Parameter**

  * **value** (::String) — An optional name for the rule. This field is not a unique identifier and can be updated. 



**Returns**

  * (::String) — An optional name for the rule. This field is not a unique identifier and can be updated. 



### #rule_tuple_count
    
    
    def rule_tuple_count() -> ::Integer

**Returns**

  * (::Integer) — Output only. [Output Only] Calculation of the complexity of a single firewall policy rule. 



### #rule_tuple_count=
    
    
    def rule_tuple_count=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Output only. [Output Only] Calculation of the complexity of a single firewall policy rule. 



**Returns**

  * (::Integer) — Output only. [Output Only] Calculation of the complexity of a single firewall policy rule. 



### #security_profile_group
    
    
    def security_profile_group() -> ::String

**Returns**

  * (::String) — A fully-qualified URL of a SecurityProfileGroup resource instance. Example: https://networksecurity.googleapis.com/v1/projects/{project}/locations/{location}/securityProfileGroups/my-security-profile-group Must be specified if action is one of 'apply_security_profile_group' or 'mirror'. Cannot be specified for other actions. Can be specified only for global network firewall policies or hierarchical firewall policies. 



### #security_profile_group=
    
    
    def security_profile_group=(value) -> ::String

**Parameter**

  * **value** (::String) — A fully-qualified URL of a SecurityProfileGroup resource instance. Example: https://networksecurity.googleapis.com/v1/projects/{project}/locations/{location}/securityProfileGroups/my-security-profile-group Must be specified if action is one of 'apply_security_profile_group' or 'mirror'. Cannot be specified for other actions. Can be specified only for global network firewall policies or hierarchical firewall policies. 



**Returns**

  * (::String) — A fully-qualified URL of a SecurityProfileGroup resource instance. Example: https://networksecurity.googleapis.com/v1/projects/{project}/locations/{location}/securityProfileGroups/my-security-profile-group Must be specified if action is one of 'apply_security_profile_group' or 'mirror'. Cannot be specified for other actions. Can be specified only for global network firewall policies or hierarchical firewall policies. 



### #target_forwarding_rules
    
    
    def target_forwarding_rules() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — 

A list of forwarding rules to which this rule applies. This field allows you to control which load balancers get this rule. For example, the following are valid values:
        
        - https://www.googleapis.com/compute/v1/projects/project/global/forwardingRules/forwardingRule
         - https://www.googleapis.com/compute/v1/projects/project/regions/region/forwardingRules/forwardingRule
         - projects/project/global/
         forwardingRules/forwardingRule
         - projects/project/regions/region/forwardingRules/
         forwardingRule
        




### #target_forwarding_rules=
    
    
    def target_forwarding_rules=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — 

A list of forwarding rules to which this rule applies. This field allows you to control which load balancers get this rule. For example, the following are valid values:
        
        - https://www.googleapis.com/compute/v1/projects/project/global/forwardingRules/forwardingRule
         - https://www.googleapis.com/compute/v1/projects/project/regions/region/forwardingRules/forwardingRule
         - projects/project/global/
         forwardingRules/forwardingRule
         - projects/project/regions/region/forwardingRules/
         forwardingRule
        




**Returns**

  * (::Array<::String>) — 

A list of forwarding rules to which this rule applies. This field allows you to control which load balancers get this rule. For example, the following are valid values:
        
        - https://www.googleapis.com/compute/v1/projects/project/global/forwardingRules/forwardingRule
         - https://www.googleapis.com/compute/v1/projects/project/regions/region/forwardingRules/forwardingRule
         - projects/project/global/
         forwardingRules/forwardingRule
         - projects/project/regions/region/forwardingRules/
         forwardingRule
        




### #target_resources
    
    
    def target_resources() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — A list of network resource URLs to which this rule applies. This field allows you to control which network's VMs get this rule. If this field is left blank, all VMs within the organization will receive the rule. 



### #target_resources=
    
    
    def target_resources=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — A list of network resource URLs to which this rule applies. This field allows you to control which network's VMs get this rule. If this field is left blank, all VMs within the organization will receive the rule. 



**Returns**

  * (::Array<::String>) — A list of network resource URLs to which this rule applies. This field allows you to control which network's VMs get this rule. If this field is left blank, all VMs within the organization will receive the rule. 



### #target_secure_tags
    
    
    def target_secure_tags() -> ::Array<::Google::Cloud::Compute::V1::FirewallPolicyRuleSecureTag>

**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::FirewallPolicyRuleSecureTag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-FirewallPolicyRuleSecureTag)>) — A list of secure tags that controls which instances the firewall rule applies to. If targetSecureTag are specified, then the firewall rule applies only to instances in the VPC network that have one of those EFFECTIVE secure tags, if all the target_secure_tag are in INEFFECTIVE state, then this rule will be ignored.targetSecureTag may not be set at the same time astargetServiceAccounts. If neither targetServiceAccounts nortargetSecureTag are specified, the firewall rule applies to all instances on the specified network. Maximum number of target label tags allowed is 256. 



### #target_secure_tags=
    
    
    def target_secure_tags=(value) -> ::Array<::Google::Cloud::Compute::V1::FirewallPolicyRuleSecureTag>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Compute::V1::FirewallPolicyRuleSecureTag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-FirewallPolicyRuleSecureTag)>) — A list of secure tags that controls which instances the firewall rule applies to. If targetSecureTag are specified, then the firewall rule applies only to instances in the VPC network that have one of those EFFECTIVE secure tags, if all the target_secure_tag are in INEFFECTIVE state, then this rule will be ignored.targetSecureTag may not be set at the same time astargetServiceAccounts. If neither targetServiceAccounts nortargetSecureTag are specified, the firewall rule applies to all instances on the specified network. Maximum number of target label tags allowed is 256. 



**Returns**

  * (::Array<[::Google::Cloud::Compute::V1::FirewallPolicyRuleSecureTag](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-FirewallPolicyRuleSecureTag)>) — A list of secure tags that controls which instances the firewall rule applies to. If targetSecureTag are specified, then the firewall rule applies only to instances in the VPC network that have one of those EFFECTIVE secure tags, if all the target_secure_tag are in INEFFECTIVE state, then this rule will be ignored.targetSecureTag may not be set at the same time astargetServiceAccounts. If neither targetServiceAccounts nortargetSecureTag are specified, the firewall rule applies to all instances on the specified network. Maximum number of target label tags allowed is 256. 



### #target_service_accounts
    
    
    def target_service_accounts() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — A list of service accounts indicating the sets of instances that are applied with this rule. 



### #target_service_accounts=
    
    
    def target_service_accounts=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — A list of service accounts indicating the sets of instances that are applied with this rule. 



**Returns**

  * (::Array<::String>) — A list of service accounts indicating the sets of instances that are applied with this rule. 



### #target_type
    
    
    def target_type() -> ::String

**Returns**

  * (::String) — Target types of the firewall policy rule. Default value is INSTANCES. Check the TargetType enum for the list of possible values. 



### #target_type=
    
    
    def target_type=(value) -> ::String

**Parameter**

  * **value** (::String) — Target types of the firewall policy rule. Default value is INSTANCES. Check the TargetType enum for the list of possible values. 



**Returns**

  * (::String) — Target types of the firewall policy rule. Default value is INSTANCES. Check the TargetType enum for the list of possible values. 



### #tls_inspect
    
    
    def tls_inspect() -> ::Boolean

**Returns**

  * (::Boolean) — Boolean flag indicating if the traffic should be TLS decrypted. Can be set only if action = 'apply_security_profile_group' and cannot be set for other actions. 



### #tls_inspect=
    
    
    def tls_inspect=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Boolean flag indicating if the traffic should be TLS decrypted. Can be set only if action = 'apply_security_profile_group' and cannot be set for other actions. 



**Returns**

  * (::Boolean) — Boolean flag indicating if the traffic should be TLS decrypted. Can be set only if action = 'apply_security_profile_group' and cannot be set for other actions. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
