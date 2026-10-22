---
url: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/configure-vpc/
title: (Optional) Configure your reporting to use Virtual Private Cloud (VPC) \u00a0|\u00a0 Google Cloud Marketplace Partners \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:45.438066+00:00
---

# (Optional) Configure your reporting to use Virtual Private Cloud (VPC)  |  Google Cloud Marketplace Partners  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/configure-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Partners ](https://docs.cloud.google.com/marketplace/docs/partners)
  * [ Develop ](https://docs.cloud.google.com/marketplace/docs/partners/develop)



Send feedback 

#  (Optional) Configure your reporting to use Virtual Private Cloud (VPC) Stay organized with collections  Save and categorize content based on your preferences. 

Optionally, if you want to use [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc) in the environment in which your product's service runs, you must complete the following steps to integrate Google Cloud Marketplace reporting with VPC. By default, the Compute Engine virtual machines (VMs) in your VPC can only communicate internally. You must configure one of the VMs to communicate externally, so that the rest of the VMs in your VPC can use it for reporting.

## Before you begin

  * Set up your preferred implementation of VPC in your service environment. For steps to set up VPC, visit [ Create and modify Virtual Private Cloud (VPC) networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).
  * Ensure that you have the [ Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute) Identity and Access Management (IAM) role for your Google Cloud project.



## Set up Private Google Access

To enable your product's Compute Engine virtual machines (VMs) to communicate externally for reporting purposes, you must set up [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access). For more information about configuring Private Google Access, refer to [Configuring Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

  1. [Enable Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#enabling-pga) for your service environment.

  2. [Configure DNS](https://docs.cloud.google.com/vpc/docs/configure-private-google-access#config-domain) to resolve requests to `private.googleapis.com`.

  3. [Create a custom route](https://docs.cloud.google.com/vpc/docs/using-routes#addingroute) for Google APIs:

     * For **Name** , specify `route-google-apis-services`.
     * For **Network** , select your VPC.
     * For **Destination IP range** , specify `199.36.153.8/30`.
     * For **Priority** , specify `0`.
     * For **Instance tags** , specify `google-apis-services`.
     * For **Next hop** , select **Default internet gateway**.
  4. [Create a VPC firewall rule](https://docs.cloud.google.com/vpc/docs/using-firewalls#creating_firewall_rules) to enable your product to communicate with Google APIs:

     * For the **Name** , specify `google-apis-services`.
     * For the **Description** , specify `Allow egress traffic to Google APIs and services`.
     * Enable [firewall rules logging](https://docs.cloud.google.com/vpc/docs/using-firewall-rules-logging).
     * For **Network** , select your VPC.
     * For **Direction of traffic** , select **Egress**.
     * For the **Action on match** , select **Allow**.
     * For **Targets** , select `Specified target tags`, and then for **Target tags** , specify `google-apis-services`.
     * For the **Destination filter** , select `IPv4 ranges`, and for the **Destination IPv4 ranges** , specify `199.36.153.8/30`.
     * For **Protocols and ports** , select `Allow all`.
  5. In Google Cloud console, select the VM you want to use to report your product's usage. Under **Network tags** , add `google-apis-services`, and click **SAVE**.

  6. Under **Network interfaces** , locate your VPC's network interface.

  7. In the **Subnetwork** column, click the subnet link. From the **Subnet details** page, click **Edit** , and set **Private Google Access** to **On**.

  8. Click **Save**.




[ Previous arrow_back  Best practices for usage labeling  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/best-practices-labeling)

[ Next Configure your reporting to use VPC Service Controls  arrow_forward  ](https://docs.cloud.google.com/marketplace/docs/partners/integrated-saas/configure-vpc-service-controls)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
