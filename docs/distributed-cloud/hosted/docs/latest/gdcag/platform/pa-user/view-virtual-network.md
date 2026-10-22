---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/view-virtual-network/
title: View the virtual network \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:02:05.534727+00:00
---

# View the virtual network  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/view-virtual-network/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  View the virtual network Stay organized with collections  Save and categorize content based on your preferences. 

Each organization in Google Distributed Cloud (GDC) air-gapped has its own isolated virtual network. An organization has two different IP ranges: an internal range and an external range.

**Note:** The GDC console does not support viewing IP ranges. To view the IP ranges and subnets allocated for an organization's virtual network, use the `kubectl` CLI.

## View IP ranges using the CLI

To view the subnets and CIDR IP ranges for your organization's virtual network:

  1. Obtain the kubeconfig for the organization admin cluster or root admin cluster, and set the environment variable:
         
         export KUBECONFIG=CLUSTER_KUBECONFIG
         

  2. List all subnets in the `platform` namespace:
         
         kubectl --kubeconfig=${KUBECONFIG} get subnet -n platform
         

The output displays the subnets and their configured IPv4 and IPv6 CIDR ranges:
         
         NAME                                READY   IPV4 CIDR       IPV6 CIDR
         default-vpc-default-node-subnet     True    10.210.2.0/23
         default-vpc-root-cidr               True    10.210.0.0/16
         

  3. To view details for a specific subnet, run:
         
         kubectl --kubeconfig=${KUBECONFIG} get subnet SUBNET_NAME -n platform -o yaml
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
