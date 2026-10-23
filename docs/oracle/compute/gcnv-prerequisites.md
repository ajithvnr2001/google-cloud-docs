---
url: https://docs.cloud.google.com/oracle/compute/gcnv-prerequisites/
title: Prerequisites for Oracle Database deployment using NetApp Volumes \u00a0|\u00a0 Oracle on Google Cloud Compute \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:52.813416+00:00
---

# Prerequisites for Oracle Database deployment using NetApp Volumes  |  Oracle on Google Cloud Compute  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/oracle/compute/gcnv-prerequisites/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Oracle on Google Cloud Compute ](https://docs.cloud.google.com/oracle/compute)
  * [ Guides ](https://docs.cloud.google.com/oracle/compute/overview)



Send feedback 

#  Prerequisites for Oracle Database deployment using NetApp Volumes Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the prerequisites for deploying Oracle Database using Google Cloud NetApp Volumes.

Make sure that the following prerequisites are complete before creating a deployment:

  * Oracle Linux 10 running on all three Compute Engine instances.
  * Enable the NetApp Volumes API. Run the following Google Cloud CLI command:
        
        gcloud services enable netapp.googleapis.com
        

  * Synchronize the time on all three VMs. Run the following commands:
        
        chronyc tracking
        
        timedatectl

  * [Configure networking for NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/networking). Create a VPC network and a subnet with private services access.

  * Grant the required Identity and Access Management (IAM) roles and permissions.

Task | Required access  
---|---  
Create Compute Engine VMs | Compute Instance Admin `roles/compute.instanceAdmin`  
Virtual Private Cloud (VPC) and firewall policies | Network administrator or policy administrator  
Create NetApp Volumes storage pools and volumes | NetApp Volumes Admin `roles/netapp.admin`  
Configure private services access | Network administrator in host project  
SSH using Identity-Aware Proxy (IAP) | IAP-secured tunnel user and OS login (if used)  



## What's next

  * [Provision Compute Engine instances](https://docs.cloud.google.com/oracle/compute/gcnv-provision-compute-instances).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
