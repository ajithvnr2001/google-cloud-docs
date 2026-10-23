---
url: https://docs.cloud.google.com/ull-solution/participants/firewall/create-firewall-rules/
title: Create and manage firewall policies for ULL VPC networks \u00a0|\u00a0 Ultra Low Latency Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:20.570476+00:00
---

# Create and manage firewall policies for ULL VPC networks  |  Ultra Low Latency Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ull-solution/participants/firewall/create-firewall-rules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ ULL Solution ](https://docs.cloud.google.com/ull-solution)
  * [ Exchange participants ](https://docs.cloud.google.com/ull-solution/participants)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create and manage firewall policies for ULL VPC networks

**GA with allowlist** : ULL Solution is available only to approved exchange operators and their exchange participants. If you are an approved exchange participant, contact [exchanges@google.com](mailto:exchanges@google.com) to request access.

To configure Cloud Next Generation Firewall (Cloud NGFW) for Ultra Low Latency (ULL) Virtual Private Cloud (VPC) networks, you must create a [regional network firewall policy](https://docs.cloud.google.com/firewall/docs/regional-firewall-policies) and set the policy type flag to `ULL_POLICY`. ULL VPC networks differ from regular VPC networks and don't support legacy VPC firewall rules.

This page shows you how to configure firewall policy rules that apply to ULL VPC networks.

## Before you begin

  * Make sure that you have the [Compute Security Admin role](https://docs.cloud.google.com/compute/docs/access/iam#compute.securityAdmin) (`roles/compute.securityAdmin`) to manage network firewall policies.

  * Make sure that you have a ULL VPC network.




## Create a ULL firewall policy

Once you create a ULL VPC network, you can create a firewall policy for that network. When you create the policy, set the `policy_type` field to `ULL_POLICY`. You can use only regional network firewall policies for ULL VPC networks.

###  gcloud 

  1. To create a ULL regional network firewall policy, use the [`gcloud compute network-firewall-policies create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/create):
         
         gcloud compute network-firewall-policies create FIREWALL_POLICY_NAME \
             --region=REGION \
             --policy_type=ULL_POLICY
         

Replace the following values:

     * `FIREWALL_POLICY_NAME`: the name of the network firewall policy.
     * `REGION`: the region of the ULL network firewall policy.



## Create rules in the ULL firewall policy

Add firewall rules to your ULL policy. To maintain low latency, ULL policies support a specific subset of standard Cloud NGFW features.

###  gcloud 

  1. To add a rule to the ULL network firewall policy, use the [`gcloud compute network-firewall-policies rules create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/rules/create):
         
         gcloud compute network-firewall-policies rules create PRIORITY \
             --firewall-policy-region=REGION \
             --firewall-policy=FIREWALL_POLICY_NAME \
             --action=allow \
             --direction=DIRECTION \
             --src-ip-ranges=SOURCE_IP_RANGE \
             --layer4-configs=tcp:80,udp:53
         

Replace the following values:

     * `PRIORITY`: the numeric evaluation order of the rule within the policy. Priorities must be unique for each rule.
     * `REGION`: the region of the ULL network firewall policy.
     * `FIREWALL_POLICY_NAME`: the name of the network firewall policy.
     * `DIRECTION`: the direction of the traffic the rule is applied.
     * `SOURCE_IP_RANGE`: the IP address ranges that are allowed to make inbound connections that match the firewall rule to the instances on the network. The IP address must be specified in [Classless Inter Domain Routing (CIDR)](https://en.wikipedia.org/wiki/Classless_Inter-Domain_Routing) format.



## Associate the policy with the ULL VPC network

After you create the policy and define its rules, associate it with your ULL VPC network. The association validates that the network's profile allows the `ULL_POLICY` type.

###  gcloud 

  1. To associate a ULL VPC network, use the [`gcloud compute network-firewall-policies associations create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/network-firewall-policies/associations/create):
         
         gcloud compute network-firewall-policies associations create \
             --firewall-policy-region=REGION \
             --firewall-policy=FIREWALL_POLICY_NAME \
             --network=ULL_NETWORK_NAME
         

Replace the following values:

     * `REGION`: the region of the ULL network firewall policy.
     * `FIREWALL_POLICY_NAME`: the name of the network firewall policy.
     * `ULL_NETWORK_NAME`: the name of the ULL VPC network.



## What's next

  * [Firewall for ULL VPC networks overview](https://docs.cloud.google.com/ull-solution/participants/firewall/overview)
  * [Ultra Low Latency Solution overview](https://docs.cloud.google.com/ull-solution/participants)
  * [Delete an association](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#delete-association)
  * [Update a rule](https://docs.cloud.google.com/firewall/docs/use-regional-firewall-policies#update-rule)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
