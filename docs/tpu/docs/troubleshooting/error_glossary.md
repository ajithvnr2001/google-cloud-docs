---
url: https://docs.cloud.google.com/tpu/docs/troubleshooting/error_glossary/
title: Cloud TPU Error Glossary \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:19.702730+00:00
---

# Cloud TPU Error Glossary  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/troubleshooting/error_glossary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cloud TPU Error Glossary

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

This document provides a glossary of common errors with solutions from the Cloud TPU service.

* * *

## Invalid Accelerator Type

### **Error Message**
    
    
    generic::invalid_argument: Accelerator type v2-512 as preemptible (false) and
    reserved (false) is not available in zone us-central1-a, please contact support.
    

### **Solution**

An invalid parameter has been provided to the create command. The availability of an accelerator in a zone depends on the following parameters: the type, the `preemptible` flag, the `spot` flag, and the `reserved` flag. The `preemptible`, `spot`, and `reserved` flags can be changed by including or excluding them in the create command.

A TPU created with the `reserved` flag will use reserved capacity. Including the `spot` or `preemptible` flags will allow the TPU to be preempted by higher priority TPUs. If none of these flags are provided, the TPU will be on-demand. It is not a valid configuration to enable more than one of these flags. See the [create command documentation](https://docs.cloud.google.com/tpu/docs/create-tpu-vm) for more information.

The accelerator types available in each zone can be found in the [TPU regions and zones documentation](https://docs.cloud.google.com/tpu/docs/regions-zones) or they can be queried using the [accelerator-types list command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/tpus/accelerator-types/list). Change the create command to use one of these accelerator types and try again or contact support if the problem persists.

## Network Not Found

### **Error Message**
    
    
      Cloud TPU received a bad request. The field "Network" cannot be "NETWORK_NAME":
      requested resource not found
    

### **Solution**

The Network NETWORK_NAME was not found. Ensure that the Network was created and set up properly. See [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks) for more information.

## Service Account Permission Denied

### **Error Message**
    
    
      generic::permission_denied: Cloud TPU got permissions denied when trying to
      access the customer project. Make sure that the IAM account
      'service-[project number]@cloud-tpu.iam.gserviceaccount.com' has the 'Cloud
      TPU API Service Agent' role by following https://cloud.google.com/iam/docs/manage-access-service-accounts
    

### **Solution**

This error occurs when a user attempts to create or list nodes in a project without IAM authorization. A likely cause of this issue is that the Cloud TPU API service account does not have the required role for the project. The [Manage access accounts documentation](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts) gives an overview of how to manage access. Follow the [Grant or revoke a single role](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts#single-role) steps and give the account 'service-`PROJECT_NUMBER`@cloud-tpu.iam.gserviceaccount.com'the role of 'Cloud TPU API Service Agent' (be sure to replace `PROJECT_NUMBER` with your project number, which can be found in the project settings in the Google Cloud console). For more information on service agents, see the [Service agents documentation](https://docs.cloud.google.com/iam/docs/service-agents).

## Quota Exceeded

### **Error Message**
    
    
    You have reached XXXX limit. Please request an increase for the 'YYYY' quota for
    Compute Engine API by following https://cloud.google.com/docs/quotas/view-manage#requesting_higher_quota.
    

### **Solution**

Your project has reached a quota limit. To learn more about working with quotas, see the [Cloud Quotas documentation](https://docs.cloud.google.com/docs/quotas/overview). This shouldn't be confused with the [TPU quota](https://docs.cloud.google.com/tpu/docs/quota), which governs the usage of TPU pods.

You may request an increase to the appropriate limit by following the steps listed at [Request a quota adjustment](https://docs.cloud.google.com/docs/quotas/view-manage#requesting_higher_quota). On the quotas page, you may search for the quota specified by the 'YYYY' part of this message. Some quotas are split across different regions or services. The error message will indicate which one needs to be increased.

The 'XXXX' and 'YYYY' parts of the message may be one of the following:

  * HEALTH_CHECKS - 'Health checks' quota
  * FIREWALLS - 'Firewall rules' quota
  * NETWORK_ENDPOINT_GROUPS - 'Network endpoint groups' quota for this region
  * READ_REQUESTS - 'Read requests per minute' quota for the Compute Engine API service
  * OPERATION_READ_REQUESTS - 'Operation read requests per minute' quota



This request is typically processed within 2-3 business days. If the request is urgent, reach out to a customer engineer or technical account manager.

## Fatal Error

### **Error Message**
    
    
    !!!! FATAL ERROR !!!! observed errors are: [ERROR_TYPE]. Now taking a TPU core dump...
    

### **Solution**

This error indicates a critical issue with the TPU node. The error type (`[ERROR_TYPE]`) in the message specifies the nature of the error. The recommended action depends on the observed error:

#### `HARDWARE`

  * **Cause:** A hardware problem with the TPU, its memory (HBM), or the host machine. Examples include uncorrectable memory errors (ECC HBM) or internal link quality problems. Common examples of hardware problems are: v6e ECC HBM error, v6e runtime Intra Link Quality error, and v5e ECC HBM error.
  * **Solution:** While Google Cloud often automatically detects and resolves these issues, hardware errors are typically not transient. If you encounter this error more than once on the same TPU node, contact [Google Cloud Support](https://docs.cloud.google.com/tpu/docs/getting-support). If you have an [All Capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-overview) reservation, consider [reporting and replacing](https://docs.cloud.google.com/tpu/docs/all-capacity-report-faulty-hosts) the node.



#### `USER`

  * **Cause:** An issue within your code or configuration, possibly related to memory management, incorrect API usage, or other aspects of the ML workload.
  * **Solution:** Review your machine learning code and job configuration for potential bugs or resource issues. Retry the workload. If this error persists on the same node, contact [Google Cloud Support](https://docs.cloud.google.com/tpu/docs/getting-support). If you have an [All Capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-overview) reservation, consider [reporting and replacing](https://docs.cloud.google.com/tpu/docs/all-capacity-report-faulty-hosts) the node.



#### `POWER`

  * **Cause:** A power-related issue with the TPU hardware or its firmware.
  * **Solution:** Google Cloud automatically handles this issue without any action required from you. Retry the workload and contact [Google Cloud Support](https://docs.cloud.google.com/tpu/docs/getting-support) if the issue persists.



#### `NETWORK`

  * **Cause:** A network-related issue within the TPU system. This could range from transient glitches to more persistent problems with the Inter-Chip Interconnect (ICI) links.
  * **Solution:** Google Cloud automatically attempts to resolve hardware-related network issues. Retry your workload, as some network-related issues are transient. If the problem continues to occur across different nodes or after you recreate your nodes, contact [Google Cloud Support](https://docs.cloud.google.com/tpu/docs/getting-support). If you have an [All Capacity mode](https://docs.cloud.google.com/tpu/docs/all-capacity-overview) reservation, consider [reporting and replacing](https://docs.cloud.google.com/tpu/docs/all-capacity-report-faulty-hosts) the node.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
