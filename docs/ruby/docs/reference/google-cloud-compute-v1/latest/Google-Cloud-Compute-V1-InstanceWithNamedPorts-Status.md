---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceWithNamedPorts-Status/
title: Google Cloud Compute V1 API - Module Google::Cloud::Compute::V1::InstanceWithNamedPorts::Status (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:27:37.225007+00:00
---

# Google Cloud Compute V1 API - Module Google::Cloud::Compute::V1::InstanceWithNamedPorts::Status (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-InstanceWithNamedPorts-Status/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Module Google::Cloud::Compute::V1::InstanceWithNamedPorts::Status (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API module Google::Cloud::Compute::V1::InstanceWithNamedPorts::Status.

Output only. [Output Only] The status of the instance.

## Constants 

### UNDEFINED_STATUS

**value:** 0  
A value indicating that the enum field is not set.

### DEPROVISIONING

**value:** 428_935_662  
The instance is halted and we are performing tear down tasks like network deprogramming, releasing quota, IP, tearing down disks etc.

### PENDING

**value:** 35_394_935  
For Flex Start provisioning instance is waiting for available capacity from Dynamic Workload Scheduler (DWS).

### PENDING_STOP

**value:** 362_509_770  
The instance is gracefully shutting down.

### PROVISIONING

**value:** 290_896_621  
Resources are being allocated for the instance.

### REPAIRING

**value:** 413_483_285  
The instance is in repair.

### RUNNING

**value:** 121_282_975  
The instance is running.

### STAGING

**value:** 431_072_283  
All required resources have been allocated and the instance is being started.

### STOPPED

**value:** 444_276_141  
The instance has stopped successfully.

### STOPPING

**value:** 350_791_796  
The instance is currently stopping (either being deleted or killed).

### SUSPENDED

**value:** 51_223_995  
The instance has suspended.

### SUSPENDING

**value:** 514_206_246  
The instance is suspending.

### TERMINATED

**value:** 250_018_339  
The instance has stopped (either by explicit action or underlying failure).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
