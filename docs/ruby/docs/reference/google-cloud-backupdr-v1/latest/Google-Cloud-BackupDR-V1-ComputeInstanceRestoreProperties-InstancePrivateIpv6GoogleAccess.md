---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ComputeInstanceRestoreProperties-InstancePrivateIpv6GoogleAccess/
title: Backup and DR Service V1 API - Module Google::Cloud::BackupDR::V1::ComputeInstanceRestoreProperties::InstancePrivateIpv6GoogleAccess (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:41.678170+00:00
---

# Backup and DR Service V1 API - Module Google::Cloud::BackupDR::V1::ComputeInstanceRestoreProperties::InstancePrivateIpv6GoogleAccess (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-ComputeInstanceRestoreProperties-InstancePrivateIpv6GoogleAccess/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Module Google::Cloud::BackupDR::V1::ComputeInstanceRestoreProperties::InstancePrivateIpv6GoogleAccess (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API module Google::Cloud::BackupDR::V1::ComputeInstanceRestoreProperties::InstancePrivateIpv6GoogleAccess.

The private IPv6 google access type for the VMs.

## Constants 

### INSTANCE_PRIVATE_IPV6_GOOGLE_ACCESS_UNSPECIFIED

**value:** 0  
Default value. This value is unused.

### INHERIT_FROM_SUBNETWORK

**value:** 1  
Each network interface inherits PrivateIpv6GoogleAccess from its subnetwork.

### ENABLE_OUTBOUND_VM_ACCESS_TO_GOOGLE

**value:** 2  
Outbound private IPv6 access from VMs in this subnet to Google services. If specified, the subnetwork who is attached to the instance's default network interface will be assigned an internal IPv6 prefix if it doesn't have before.

### ENABLE_BIDIRECTIONAL_ACCESS_TO_GOOGLE

**value:** 3  
Bidirectional private IPv6 access to/from Google services. If specified, the subnetwork who is attached to the instance's default network interface will be assigned an internal IPv6 prefix if it doesn't have before.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
