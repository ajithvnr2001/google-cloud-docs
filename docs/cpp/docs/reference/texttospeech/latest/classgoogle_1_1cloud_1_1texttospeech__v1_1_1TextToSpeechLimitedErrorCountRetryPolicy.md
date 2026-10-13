---
url: https://docs.cloud.google.com/cpp/docs/reference/texttospeech/latest/classgoogle_1_1cloud_1_1texttospeech__v1_1_1TextToSpeechLimitedErrorCountRetryPolicy/
title: Class TextToSpeechLimitedErrorCountRetryPolicy (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:15:34.535886+00:00
---

# Class TextToSpeechLimitedErrorCountRetryPolicy (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/texttospeech/latest/classgoogle_1_1cloud_1_1texttospeech__v1_1_1TextToSpeechLimitedErrorCountRetryPolicy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class TextToSpeechLimitedErrorCountRetryPolicy (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

A retry policy for [`TextToSpeechConnection`](https://docs.cloud.google.com/cpp/docs/reference/texttospeech/latest/classgoogle_1_1cloud_1_1texttospeech__v1_1_1TextToSpeechConnection) based on counting errors. 

This policy stops retrying if:

  * An RPC returns a non-transient error.
  * More than a prescribed number of transient failures is detected.



In this class the following status codes are treated as transient errors:

  * [`kUnavailable`](https://docs.cloud.google.com/cpp/docs/reference/common/latest/namespacegoogle_1_1cloud_1a90e17f75452470f0f3ee1a06ffe58847.html)



## Constructors 

### TextToSpeechLimitedErrorCountRetryPolicy(int)

Create an instance that tolerates up to `maximum_failures` transient errors. 

**Note:** Disable the retry loop by providing an instance of this policy with `maximum_failures` == 0. 

**Parameter**  
---  
**Name** | **Description**  
`maximum_failures` |  `int`   
  
  
### TextToSpeechLimitedErrorCountRetryPolicy(TextToSpeechLimitedErrorCountRetryPolicy &&)

**Parameter**  
---  
**Name** | **Description**  
`rhs` |  `TextToSpeechLimitedErrorCountRetryPolicy &&`   
  
  
### TextToSpeechLimitedErrorCountRetryPolicy(TextToSpeechLimitedErrorCountRetryPolicy const &)

**Parameter**  
---  
**Name** | **Description**  
`rhs` |  `TextToSpeechLimitedErrorCountRetryPolicy const &`   
  
  
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
`std::unique_ptr< TextToSpeechRetryPolicy >` |   
  
## Type Aliases 

### BaseType

**Alias Of** : `TextToSpeechRetryPolicy`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
