---
url: https://docs.cloud.google.com/firewall/docs/network-firewall-policy-examples/
title: Network firewall policy example \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:05.291089+00:00
---

# Network firewall policy example  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/network-firewall-policy-examples/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Network firewall policy example Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how network administrators can deploy network firewall policies to control traffic across Virtual Private Cloud (VPC) networks. The example helps you optimize rules for security controls.

Before you use this example, review the concepts of [global network firewall policies](https://docs.cloud.google.com/firewall/docs/network-firewall-policies) and [regional network firewall policies](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies).

The following diagram describes the scope of a global network firewall policy and a regional network firewall policy in a VPC network. A global network firewall policy applies to all subnetworks in all regions. A regional network firewall policy applies to only the subnetworks in the target region.

[ ![Figure 1. Scope of global and regional network firewall policies.](https://docs.cloud.google.com/static/firewall/images/firewall-policies/network-firewall-policy-scope.svg)](https://docs.cloud.google.com/static/firewall/images/firewall-policies/network-firewall-policy-scope.svg) **Figure 1.** Scope of global and regional network firewall policies.

## Example: Deny all external connections except to specific ports

In this use case, a global network firewall policy blocks all connections from external internet sources except for connections on destination ports `80`, `443`, and `22`. An ingress internet connection on ports other than `80`, `443`, or `22` is blocked. The rules enforcement is delegated to the regional network firewall policy for any connections on ports `80`, `443`, or `22`.

In this example, a regional network firewall policy applies to `region-a`, which allows internal traffic from source `10.2.0.0/16` and ingress traffic to ports `443` and `80` from any source. Figure 2 describes the configuration setup for this use case.

[ ![Figure 2. Deny all external connections except to specific destination ports.](https://docs.cloud.google.com/static/firewall/images/firewall-policies/network-firewall-policy-example-01.svg)](https://docs.cloud.google.com/static/firewall/images/firewall-policies/network-firewall-policy-example-01.svg) **Figure 2.** Deny all external connections except to specific destination ports.

### Effective policy applied in VMs

This section describes the effective network firewall policy applicable in this example after evaluating the rules across the hierarchy.

**Ingress connections**

  * Any ingress connections from `10.0.0.0/8` match the highest priority global network firewall policy rule `delegate-internal-traffic` and bypass the rest of the rules in the global network firewall policy. In the regional network firewall policy rule, ingress connections from `10.2.0.0/16` are allowed, and the rest of the connections are evaluated against the implied ingress `deny` rule.

  * Ingress connections with a source IP range other than `10.0.0.0/8`, and destination ports `22`, `80`, and `443`, are delegated to the regional network firewall policy rule level. In the regional network firewall policy rule, ports `80` and `443` are allowed, but port `22` is not.




**Egress connection**

  * There is no match across the global network firewall policy rules. Therefore, the implicit system rules apply, which allows egress connections.



### How to configure

  1. Create a global network firewall policy that contains the following rule:
         
         gcloud compute network-firewall-policies create \
             "example-firewall-policy-global" --global \
             --description "Global network firewall policy with rules that apply to all VMs in the VPC network"
         

  2. Associate the policy with the VPC network:
         
         gcloud compute network-firewall-policies associations create \
             --firewall-policy example-firewall-policy-global \
             --network my-example-vpc \
             --global-firewall-policy
         

  3. Add a rule to match any ingress connections from `10.0.0.0/8`:
         
         gcloud compute network-firewall-policies rules create 1000 \
             --action goto_next \
             --description "delegate-internal-traffic" \
             --layer4-configs all \
             --firewall-policy example-firewall-policy-global \
             --src-ip-ranges 10.0.0.0/8 \
             --global-firewall-policy
         

  4. Add a rule to delegate external traffic from specific ports:
         
         gcloud compute network-firewall-policies rules create 2000 \
             --action goto_next \
             --description "delegate-external-traffic-spec-ports" \
             --layer4-configs tcp:80,tcp:443,tcp:22 \
             --firewall-policy example-firewall-policy-global \
             --src-ip-ranges 0.0.0.0/0 \
             --global-firewall-policy
         

  5. Add a rule to block all remaining ingress traffic:
         
         gcloud compute network-firewall-policies rules create 3000 \
             --action deny \
             --description "block-external-traffic-spec-ports" \
             --firewall-policy example-firewall-policy-global \
             --src-ip-ranges 0.0.0.0/0 \
             --layer4-configs all \
             --global-firewall-policy
         

  6. Create a regional network firewall policy:
         
         gcloud compute network-firewall-policies create \
             example-firewall-policy-regional --region=region-a \
             --description "Regional network firewall policy with rules that apply to all VMs in region-a"
         

  7. Associate the regional network firewall policy with a VPC network to activate the policy rules for any VMs within that network within a specific region:
         
         gcloud compute network-firewall-policies associations create \
             --firewall-policy example-firewall-policy-regional \
             --network my-example-vpc \
             --firewall-policy-region=region-a  
         

  8. Add a rule to allow internal traffic for the regional network firewall policy:
         
         gcloud compute network-firewall-policies rules create 1000 \
             --action allow \
             --firewall-policy example-firewall-policy-regional \
             --description allow-internal-traffic \
             --direction INGRESS \
             --src-ip-ranges 10.2.0.0/16 \
             --layer4-configs all \
             --firewall-policy-region=region-a 
         

  9. Add a rule to allow external traffic from specific ports:
         
         gcloud compute network-firewall-policies rules create 2000 \
             --action allow \
             --firewall-policy example-firewall-policy-regional \
             --description allow-external-traffic-spec-ports \
             --direction INGRESS \
             --layer4-configs=tcp:80,tcp:443 \
             --src-ip-ranges 0.0.0.0/0 \
             --firewall-policy-region=region-a
         




## What's next

  * [Create global network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-network-firewall-policies) and [Manage global network firewall policies](https://docs.cloud.google.com/firewall/docs/manage-global-firewall-policies).

  * [Create regional network firewall policies and rules](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies) and [Manage regional network firewall policies](https://docs.cloud.google.com/firewall/docs/manage-regional-firewall-policies).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
