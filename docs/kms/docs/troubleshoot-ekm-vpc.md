---
url: https://docs.cloud.google.com/kms/docs/troubleshoot-ekm-vpc/
title: Troubleshoot EKM via VPC errors \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:53.362103+00:00
---

# Troubleshoot EKM via VPC errors  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/troubleshoot-ekm-vpc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Troubleshoot EKM via VPC errors Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with Cloud External Key Manager (Cloud EKM) over virtual private cloud (VPC).

In addition to the errors listed in the [Cloud EKM error reference](https://docs.cloud.google.com/kms/docs/reference/ekm_errors), EKMs accessed over VPC might experience additional errors.

### Input errors

The following table describes errors caused by incorrect input and suggests troubleshooting steps for these errors:

google.rpc.Status.message | violation[1].type(Error domain) | Troubleshooting  
---|---|---  
Permission denied when accessing the Service Directory. Ensure the Cloud EKM service account has access to the Service Directory resource in the VPC project. | `SD_RESOURCE_PERMISSION_DENIED` | Follow the steps in [Authorize Cloud EKM to access your VPC](https://docs.cloud.google.com/kms/docs/create-ekm-connection#authorize-ekm-vpc) to authorize Cloud EKM to access your VPC resource. Also, see the [Service Directory troubleshooting guide](https://docs.cloud.google.com/service-directory/docs/troubleshooting).  
  
### External key management system errors

The following table describes EKM system errors and troubleshooting suggestions:

google.rpc.Status.message | violation[1].type(Error domain) | Troubleshooting  
---|---|---  
Unable to use the Service Directory entry provided for the external key manager. The data was incomplete or was not found in the Service Directory service. | `SD_RESOURCE_MALFORMED` |  If you manage your own EKM:

  * Ensure the **network** field of your Service Directory endpoint is populated and that it matches the VPC network that you use to reach your EKM.
  * Ensure the **IP address** and **Port** are set correctly for your endpoint.

If your EKM is managed by a separate provider:

  * Contact your EKM provider to ensure the **network** Service Directory endpoints are correctly set.

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
