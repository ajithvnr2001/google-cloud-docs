---
url: https://docs.cloud.google.com/managed-microsoft-ad/docs/selecting-ip-address-ranges/
title: Select IP address ranges \u00a0|\u00a0 Managed Service for Microsoft Active Directory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:00.038566+00:00
---

# Select IP address ranges  |  Managed Service for Microsoft Active Directory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-microsoft-ad/docs/selecting-ip-address-ranges/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Managed Microsoft AD ](https://docs.cloud.google.com/managed-microsoft-ad/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-microsoft-ad/docs/overview)



Send feedback 

#  Select IP address ranges Stay organized with collections  Save and categorize content based on your preferences. 

This page identifies important considerations and helps you select the appropriate IP address ranges for your domains. CIDR ranges for Managed Service for Microsoft Active Directory domain controllers cannot be changed after they are set. To avoid conflicts and time-consuming mistakes, you should carefully consider your current and future infrastructure needs when selecting these ranges.

## Using a /24 range size

Managed Microsoft AD requires a minimum of /24 private [RFC 1918](https://tools.ietf.org/html/rfc1918) CIDR range, such as `192.168.255.0/24`. Although you can select a broader private [RFC 1918](https://tools.ietf.org/html/rfc1918) CIDR range, we recommend using /24 because this range is exclusively reserved for domain controllers. No other resources can use the additional IP addresses in the range.

If you want to use a different IP address range that is recommended by another Google Cloud product with Managed Microsoft AD, contact [ Google Cloud Support](https://cloud.google.com/support-hub).

## Avoiding overlapping ranges

You should avoid setting ranges that might overlap with current and future infrastructure.

### Asking your network specialist

Check if there is a network specialist in your organization who can help you identify or reserve safe IP address ranges.

### Listing IP address ranges in use

To avoid conflicts with existing infrastructure, you can list which IP address ranges are in use, and then use one that is not in the list.

###  Console 

To view the IP address ranges in use on your VPC network, follow these steps:

  1. In the Google Cloud console, go to the [**VPC**](https://console.cloud.google.com/networking/networks) page.   
[Go to VPC](https://console.cloud.google.com/networking/networks)

  2. Select the name of your VPC network.

  3. On the **VPC Network details** page, in the **IP address ranges** column, you can see which ranges are already in use.




Use an IP address range that is not shown in the list.

###  gcloud 

To list all subnetworks in a project, run the following gcloud CLI command:
    
    
    gcloud compute networks subnets list --sort-by=NETWORK
    

Use an IP address range that is not shown in the list.

Learn more about the [`compute networks subnets list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/subnets/list).

### Considering future needs

To avoid future conflicts, consider your infrastructure plans, including the potential addition of authorized networks. For example, if you plan to configure a VPN or Interconnect from the authorized networks to your on-premises networks, you must select an IP address range that is not used on any of those networks.

## Separating test and production environments

To prevent development and testing work from impacting production workloads or hampering the security of your deployment, consider deploying separate domains for each environment.

For a simple isolated test domain, any private CIDR /24 range that isn't already a subnet on your authorized VPC network or one of its peered networks is sufficient.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
