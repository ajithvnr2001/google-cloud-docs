---
url: https://docs.cloud.google.com/cpp/docs/reference/agentidentity/latest/classgoogle_1_1cloud_1_1agentidentity__v1_1_1AuthProviderServiceLimitedErrorCountRetryPolicy/
title: Class AuthProviderServiceLimitedErrorCountRetryPolicy (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:55.004732+00:00
---

# Class AuthProviderServiceLimitedErrorCountRetryPolicy (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/agentidentity/latest/classgoogle_1_1cloud_1_1agentidentity__v1_1_1AuthProviderServiceLimitedErrorCountRetryPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class AuthProviderServiceLimitedErrorCountRetryPolicy (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0 

A retry policy for [`AuthProviderServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/agentidentity/latest/classgoogle_1_1cloud_1_1agentidentity__v1_1_1AuthProviderServiceConnection) based on counting errors. 

This policy stops retrying if:

  * An RPC returns a non-transient error.
  * More than a prescribed number of transient failures is detected.



In this class the following status codes are treated as transient errors:

  * [`kUnavailable`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud_1a90e17f75452470f0f3ee1a06ffe58847.html)



## Constructors 

### AuthProviderServiceLimitedErrorCountRetryPolicy(int)

Create an instance that tolerates up to `maximum_failures` transient errors. 

**Note:** Disable the retry loop by providing an instance of this policy with `maximum_failures` == 0. 

**Parameter**  
---  
**Name** | **Description**  
`maximum_failures` |  `int`   
  
  
### AuthProviderServiceLimitedErrorCountRetryPolicy(AuthProviderServiceLimitedErrorCountRetryPolicy &&)

**Parameter**  
---  
**Name** | **Description**  
`rhs` |  `AuthProviderServiceLimitedErrorCountRetryPolicy &&`   
  
  
### AuthProviderServiceLimitedErrorCountRetryPolicy(AuthProviderServiceLimitedErrorCountRetryPolicy const &)

**Parameter**  
---  
**Name** | **Description**  
`rhs` |  `AuthProviderServiceLimitedErrorCountRetryPolicy const &`   
  
  
## Functions 

### maximum_failures() const

**Returns**  
---  
**Type** | **Description**  
`int` |   
  
### virtual OnFailure(Status const &)

**Parameter**  
---  
**Name** | **Description**  
`status` |  `Status const &`   
  
**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### virtual IsExhausted() const

**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### virtual IsPermanentFailure(Status const &) const

**Parameter**  
---  
**Name** | **Description**  
`status` |  `Status const &`   
  
**Returns**  
---  
**Type** | **Description**  
`bool` |   
  
### virtual clone() const

Creates a new instance of the policy, reset to the initial state. 

**Returns**  
---  
**Type** | **Description**  
`std::unique_ptr< AuthProviderServiceRetryPolicy >` |   
  
## Type Aliases 

### BaseType

**Alias Of** : `AuthProviderServiceRetryPolicy`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
