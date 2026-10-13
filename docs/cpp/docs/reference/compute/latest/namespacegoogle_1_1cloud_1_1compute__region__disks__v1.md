---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/namespacegoogle_1_1cloud_1_1compute__region__disks__v1/
title: Namespace google::cloud::compute_region_disks_v1 (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:37:47.077384+00:00
---

# Namespace google::cloud::compute_region_disks_v1 (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/namespacegoogle_1_1cloud_1_1compute__region__disks__v1/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Namespace google::cloud::compute_region_disks_v1 (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

## Classes 

### [RegionDisksClient](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksClient)

Service for the regionDisks resource. 

### [RegionDisksConnection](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksConnection)

The [`RegionDisksConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksConnection) object for [`RegionDisksClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksClient). 

### [RegionDisksConnectionIdempotencyPolicy](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksConnectionIdempotencyPolicy)

### [RegionDisksLimitedErrorCountRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksLimitedErrorCountRetryPolicy)

A retry policy for [`RegionDisksConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksConnection) based on counting errors. 

### [RegionDisksLimitedTimeRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksLimitedTimeRetryPolicy)

A retry policy for [`RegionDisksConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksConnection) based on elapsed time. 

### [RegionDisksRetryPolicy](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksRetryPolicy)

The retry policy for [`RegionDisksConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksConnection). 

## Structs 

### [RegionDisksBackoffPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/structgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksBackoffPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure the backoff policy. 

### [RegionDisksConnectionIdempotencyPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/structgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksConnectionIdempotencyPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure which operations are retried. 

### [RegionDisksPollingPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/structgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksPollingPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure the long-running operations polling policy. 

### [RegionDisksRetryPolicyOption](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/structgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksRetryPolicyOption)

Use with [`google::cloud::Options`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/classgoogle_1_1cloud_1_1Options.html) to configure the retry policy. 

## Functions 

### MakeDefaultRegionDisksConnectionIdempotencyPolicy()

**Returns**  
---  
**Type** | **Description**  
`std::unique_ptr< RegionDisksConnectionIdempotencyPolicy >` |   
  
### MakeRegionDisksConnectionRest(Options)

A factory function to construct an object of type [`RegionDisksConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksConnection) that uses REST over HTTP as transport in lieu of gRPC. 

REST transport should only be used for services that do not support gRPC or if the existing network configuration precludes using gRPC.

The returned connection object should not be used directly; instead it should be passed as an argument to the constructor of [RegionDisksClient](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksClient).

The optional `options` argument may be used to configure aspects of the returned [`RegionDisksConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksConnection). Expected options are any of the types in the following option lists:

  * [`google::cloud::CommonOptionList`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)
  * [`google::cloud::RestOptionList`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)
  * [`google::cloud::UnifiedCredentialsOptionList`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud.html)
  * [`google::cloud::compute_region_disks_v1::RegionDisksPolicyOptionList`](about:invalid#zCSafez)

**Note:** Unexpected options will be ignored. To log unexpected options instead, set `GOOGLE_CLOUD_CPP_ENABLE_CLOG=yes` in the environment. 

**Parameter**  
---  
**Name** | **Description**  
`options` | `Options`  
(optional) Configure the [`RegionDisksConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__region__disks__v1_1_1RegionDisksConnection) created by this function.   
**Returns**  
---  
**Type** | **Description**  
`std::shared_ptr< RegionDisksConnection >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
