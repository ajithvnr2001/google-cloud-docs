---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-QuotaStatusWarning-Code/
title: Google Cloud Compute V1 API - Module Google::Cloud::Compute::V1::QuotaStatusWarning::Code (v4.0.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:39.998636+00:00
---

# Google Cloud Compute V1 API - Module Google::Cloud::Compute::V1::QuotaStatusWarning::Code (v4.0.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-compute-v1/latest/Google-Cloud-Compute-V1-QuotaStatusWarning-Code/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Google Cloud Compute V1 API - Module Google::Cloud::Compute::V1::QuotaStatusWarning::Code (v4.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.0.0 (latest)  3.12.0  3.10.0  3.9.1  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.22.0  2.21.1  2.20.0  2.19.1  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.2  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.10.0  1.9.0  1.8.0  1.7.1  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0  0.5.0 

Reference documentation and code samples for the Google Cloud Compute V1 API module Google::Cloud::Compute::V1::QuotaStatusWarning::Code.

[Output Only] A warning code, if applicable. For example, Compute Engine returns NO_RESULTS_ON_PAGE if there are no results in the response.

## Constants 

### UNDEFINED_CODE

**value:** 0  
A value indicating that the enum field is not set.

### CLEANUP_FAILED

**value:** 150_308_440  
Warning about failed cleanup of transient changes made by a failed operation.

### DEPRECATED_RESOURCE_USED

**value:** 391_835_586  
A link to a deprecated resource was created.

### DEPRECATED_TYPE_USED

**value:** 346_526_230  
When deploying and at least one of the resources has a type marked as deprecated

### DISK_SIZE_LARGER_THAN_IMAGE_SIZE

**value:** 369_442_967  
The user created a boot disk that is larger than image size.

### EXPERIMENTAL_TYPE_USED

**value:** 451_954_443  
When deploying and at least one of the resources has a type marked as experimental

### EXTERNAL_API_WARNING

**value:** 175_546_307  
Warning that is present in an external api call

### FIELD_VALUE_OVERRIDEN

**value:** 329_669_423  
Warning that value of a field has been overridden. Deprecated unused field.

### INJECTED_KERNELS_DEPRECATED

**value:** 417_377_419  
The operation involved use of an injected kernel, which is deprecated.

### INVALID_HEALTH_CHECK_FOR_DYNAMIC_WIEGHTED_LB

**value:** 401_542_606  
A WEIGHTED_MAGLEV backend service is associated with a health check that is not of type HTTP/HTTPS/HTTP2.

### LARGE_DEPLOYMENT_WARNING

**value:** 481_440_678  
When deploying a deployment with a exceedingly large number of resources

### LIST_OVERHEAD_QUOTA_EXCEED

**value:** 47_618_117  
Resource can't be retrieved due to list overhead quota exceed which captures the amount of resources filtered out by user-defined list filter.

### MISSING_TYPE_DEPENDENCY

**value:** 344_505_463  
A resource depends on a missing type

### NEXT_HOP_ADDRESS_NOT_ASSIGNED

**value:** 324_964_999  
The route's nextHopIp address is not assigned to an instance on the network.

### NEXT_HOP_CANNOT_IP_FORWARD

**value:** 383_382_887  
The route's next hop instance cannot ip forward.

### NEXT_HOP_INSTANCE_HAS_NO_IPV6_INTERFACE

**value:** 146_748_434  
The route's nextHopInstance URL refers to an instance that does not have an ipv6 interface on the same network as the route.

### NEXT_HOP_INSTANCE_NOT_FOUND

**value:** 464_250_446  
The route's nextHopInstance URL refers to an instance that does not exist.

### NEXT_HOP_INSTANCE_NOT_ON_NETWORK

**value:** 243_758_146  
The route's nextHopInstance URL refers to an instance that is not on the same network as the route.

### NEXT_HOP_NOT_RUNNING

**value:** 417_081_265  
The route's next hop instance does not have a status of RUNNING.

### NOT_CRITICAL_ERROR

**value:** 105_763_924  
Error which is not critical. We decided to continue the process despite the mentioned error.

### NO_RESULTS_ON_PAGE

**value:** 30_036_744  
No results are present on a particular list page.

### PARTIAL_SUCCESS

**value:** 39_966_469  
Success is reported, but some results may be missing due to errors

### QUOTA_INFO_UNAVAILABLE

**value:** 304_294_182  
Quota information is not available to client requests (e.g: regions.list).

### REQUIRED_TOS_AGREEMENT

**value:** 3_745_539  
The user attempted to use a resource that requires a TOS they have not accepted.

### RESOURCE_IN_USE_BY_OTHER_RESOURCE_WARNING

**value:** 496_728_641  
Warning that a resource is in use.

### RESOURCE_NOT_DELETED

**value:** 168_598_460  
One or more of the resources set to auto-delete could not be deleted because they were in use.

### SCHEMA_VALIDATION_IGNORED

**value:** 275_245_642  
When a resource schema validation is ignored.

### SINGLE_INSTANCE_PROPERTY_TEMPLATE

**value:** 268_305_617  
Instance template used in instance group manager is valid as such, but its application does not make a lot of sense, because it allows only single instance in instance group.

### UNDECLARED_PROPERTIES

**value:** 390_513_439  
When undeclared properties in the schema are present

### UNREACHABLE

**value:** 13_328_052  
A given scope cannot be reached.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
