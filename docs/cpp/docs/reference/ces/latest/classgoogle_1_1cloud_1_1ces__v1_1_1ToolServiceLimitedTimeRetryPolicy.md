---
url: https://docs.cloud.google.com/cpp/docs/reference/ces/latest/classgoogle_1_1cloud_1_1ces__v1_1_1ToolServiceLimitedTimeRetryPolicy/
title: Class ToolServiceLimitedTimeRetryPolicy (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:47.908045+00:00
---

# Class ToolServiceLimitedTimeRetryPolicy (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/ces/latest/classgoogle_1_1cloud_1_1ces__v1_1_1ToolServiceLimitedTimeRetryPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class ToolServiceLimitedTimeRetryPolicy (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0 

A retry policy for [`ToolServiceConnection`](https://docs.cloud.google.com/cpp/docs/reference/ces/latest/classgoogle_1_1cloud_1_1ces__v1_1_1ToolServiceConnection) based on elapsed time. 

This policy stops retrying if:

  * An RPC returns a non-transient error.
  * The elapsed time in the retry loop exceeds a prescribed duration.



In this class the following status codes are treated as transient errors:

  * [`kUnavailable`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud_1a90e17f75452470f0f3ee1a06ffe58847.html)



## Constructors 

### ToolServiceLimitedTimeRetryPolicy(std::chrono::duration< DurationRep, DurationPeriod >)

Constructor given a `std::chrono::duration<>` object. 

###### See Also

<https://en.cppreference.com/w/cpp/chrono/duration> for more information about `std::chrono::duration`. 

**Parameters**  
---  
**Name** | **Description**  
`maximum_duration` |  `std::chrono::duration< DurationRep, DurationPeriod >`   
the maximum time allowed before the policy expires. While the application can express this time in any units they desire, the class truncates to milliseconds.  
`typename DurationRep` |  ``   
a placeholder to match the `Rep` tparam for `duration's` type. The semantics of this template parameter are documented in `std::chrono::duration<>`. In brief, the underlying arithmetic type used to store the number of ticks. For our purposes it is simply a formal parameter.   
`typename DurationPeriod` |  ``   
a placeholder to match the `Period` tparam for `duration's` type. The semantics of this template parameter are documented in `std::chrono::duration<>`. In brief, the length of the tick in seconds, expressed as a `std::ratio<>`. For our purposes it is simply a formal parameter.   
  
### ToolServiceLimitedTimeRetryPolicy(ToolServiceLimitedTimeRetryPolicy &&)

**Parameter**  
---  
**Name** | **Description**  
`rhs` |  `ToolServiceLimitedTimeRetryPolicy &&`   
  
  
### ToolServiceLimitedTimeRetryPolicy(ToolServiceLimitedTimeRetryPolicy const &)

**Parameter**  
---  
**Name** | **Description**  
`rhs` |  `ToolServiceLimitedTimeRetryPolicy const &`   
  
  
## Functions 

### maximum_duration() const

**Returns**  
---  
**Type** | **Description**  
`std::chrono::milliseconds` |   
  
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
`std::unique_ptr< ToolServiceRetryPolicy >` |   
  
## Type Aliases 

### BaseType

**Alias Of** : `ToolServiceRetryPolicy`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
