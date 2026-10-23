---
url: https://docs.cloud.google.com/vpc/docs/configure-security-private-service-connect-interfaces/
title: Configure security for Private Service Connect interfaces \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:31.032657+00:00
---

# Configure security for Private Service Connect interfaces  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/configure-security-private-service-connect-interfaces/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure security for Private Service Connect interfaces 

This page describes how producer network administrators can manage security in VPC networks that use Private Service Connect interfaces.

Because a Private Service Connect interface exists in a consumer Private Service Connect network, a producer organization does not control firewall rules that apply directly to the interface. If a producer organization wants to ensure that consumer workloads cannot initiate traffic to VMs in the producer network, or that only selected consumer workloads can initiate traffic, they must define security policies in the guest OS of their interface's VM.

## Block consumer-to-producer ingress

You can use `iptables` to configure a Private Service Connect interface to block ingress traffic from a consumer network, but still allow egress traffic from the producer network. This configuration is illustrated by figure 1.

[ ![](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/block-consumer-to-producer-ingress.svg)](https://docs.cloud.google.com/static/vpc/images/psc-interfaces/block-consumer-to-producer-ingress.svg) Consumer traffic is blocked from ingress through a Private Service Connect interface, but producer egress traffic is allowed (click to enlarge). 

To configure a Private Service Connect interface to block ingress traffic from the consumer network but allow egress traffic from the producer network, do the following:

  1. Ensure that firewall rules are configured to [allow ingress SSH connections](https://docs.cloud.google.com/firewall/docs/using-firewalls#common-use-cases-allow-ssh) to your Private Service Connect interface's VM.

  2. [Connect](https://docs.cloud.google.com/compute/docs/connect/standard-ssh#connect_to_vms) to the VM. 

  3. If the `iptables` command isn't available, install it.

  4. Allow consumer reply traffic to ingress into the Private Service Connect interface:
         
         sudo iptables -A INPUT -m state --state RELATED,ESTABLISHED -j ACCEPT -i OS_INTERFACE_NAME
         

Replace `OS_INTERFACE_NAME` with the [guest OS name for your Private Service Connect interface](https://docs.cloud.google.com/vpc/docs/configure-routing-private-service-connect-interfaces#find-os-interface-name).

  5. Block consumer-initiated traffic from ingressing through the Private Service Connect interface:
         
         sudo iptables -A INPUT -j DROP -i OS_INTERFACE_NAME
         




## Block Private Service Connect interface creation

To create Private Service Connect interfaces, users must have the `compute.instances.pscInterfaceCreate` Identity and Access Management (IAM) permission. This permission is included in the following roles:

  * [Compute Admin](https://docs.cloud.google.com/compute/docs/access/iam#compute.admin) (`roles/compute.admin`)
  * [Compute Instance Admin (v1)](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)



If you want a user to have the permissions that are associated with these roles, while preventing that user from creating Private Service Connect interfaces, you can [Create a custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating) and grant it to the user. Add the necessary permissions to the role. Omit the `compute.instances.pscInterfaceCreate` permission.

## What's next?

  * [Manage destination overlap](https://docs.cloud.google.com/vpc/docs/manage-destination-overlap) in a network that has a Private Service Connect interface connection.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
