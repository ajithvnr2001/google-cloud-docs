---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat-subnets/
title: Create external subnets for Cloud NAT \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:20:41.330403+00:00
---

# Create external subnets for Cloud NAT  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/cloud-nat-subnets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Create external subnets for Cloud NAT Stay organized with collections  Save and categorize content based on your preferences. 

### Create external subnets

To specify what egress IP addresses the gateway can use, you create external leaf subnets containing those IP addresses. The subnets to be used in a Cloud NAT gateway are required to be of the `leaf` type, as described in [Subnet hierarchy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/subnets-overview#subnet-hierarchy), and must be in the same project as the gateway. These subnets must be derived from external subnets (subnets that contain external IP addresses).

For example:
    
    
    apiVersion: ipam.gdc.goog/v1
    kind: Subnet
    metadata:
      name: external-zone1-root
      namespace: project-1
    spec:
      ipv4Request:
        cidr: 203.0.113.0/24
      type: Root
    ---
    apiVersion: ipam.gdc.goog/v1
    kind: Subnet
    metadata:
      name: subnet-1
      namespace: project-1
    spec:
      ipv4Request:
        cidr: 203.0.113.1/32
      type: Leaf
      parentReference:
        Name: external-zone1-root
        Namespace: project-1
    ---
    apiVersion: ipam.gdc.goog/v1
    kind: Subnet
    metadata:
      name: subnet-2
      namespace: project-1
    spec:
      ipv4Request:
        prefixLength: 30
      type: Leaf
      parentReference:
        Name: external-zone1-root
        Namespace: project-1
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
