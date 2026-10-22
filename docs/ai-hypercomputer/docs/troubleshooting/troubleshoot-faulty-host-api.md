---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-faulty-host-api/
title: Troubleshoot report faulty host API errors \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:04.340813+00:00
---

# Troubleshoot report faulty host API errors  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/troubleshooting/troubleshoot-faulty-host-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Troubleshoot report faulty host API errors Stay organized with collections  Save and categorize content based on your preferences. 

[ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document explains how to resolve errors that you might encounter when using the [report faulty host API](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host).

## Error messages

When you use the report faulty host API, you might encounter one of the following errors.

### Compute instance deleted during a running operation

This error occurs when you delete a compute instance while a faulty host report operation is still in progress.

**Error messages** :
    
    
    INTERNAL_ERROR
    

**Resolution** : Before you delete a compute instance, verify that the [`reportHostAsFaulty` operation has completed](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host#review-operations). Otherwise, the report faulty host operation fails.

### Compute instance not part of a reservation

This error occurs when you report a compute instance that was created without using a reservation.

**Error message** :
    
    
    INSTANCES_WITHOUT_RESERVATION_NOT_SUPPORTED
    

**Resolution** : Verify that you created the compute instance by using the [reservation-bound provisioning model](https://docs.cloud.google.com/ai-hypercomputer/docs/consumption-models). To report a faulty host for an A4X Max, A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) instance that uses the flex-start or spot provisioning model, contact your account team.

### Duplicate faulty host report operations

This error occurs when you send a request to the repair faulty host API while another request is already in progress for the same compute instance. Additionally, your compute instance may remain in the `REPAIRING` state.

**Error message** :
    
    
    FAILED_WITH_UNEXPECTED_STATUS
    

**Resolution** : Wait until the [first report faulty host operation completes](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host#review-operations) before you send another request to the API. If the compute instance is unresponsive, then restart the compute instance before you send another request to the API.

### Fault reason is missing

This error occurs when you don't specify the `faultReasons` field in a report faulty host request.

**Error message** :
    
    
    FAULT_REASONS_EMPTY_SHOULD_BE_SPECIFIED
    

**Resolution** : The `faultReasons` field is required. To resolve this issue, specify the [`faultReasons` field](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/report-faulty-host#report-a-faulty-host) in your request.

### Incorrect machine type

This error occurs when the compute instance uses an unsupported machine type.

**Error message** :
    
    
    MACHINE_TYPE_NOT_SUPPORTED
    

**Resolution** : The report faulty host API supports only A4X Max, A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) machine types.

### Rate limit exceeded

**Error message** :
    
    
    RATE_LIMIT_EXCEEDED
    

**Reason** : You exceeded the request limit for the `instances.reportHostAsFaulty` method, or Google lacks sufficient capacity to fulfill your request.

### Unsupported compute instance state

This error occurs when the compute instance is in an unsupported state.

**Error message** :
    
    
    INSTANCE_SHOULD_BE_RUNNING
    

**Resolution** : Before you send a request to the report faulty host API, verify that the compute instance is in the [`RUNNING` state](https://docs.cloud.google.com/compute/docs/instances/instance-life-cycle).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
