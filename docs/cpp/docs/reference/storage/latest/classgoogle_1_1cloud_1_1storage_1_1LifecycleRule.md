---
url: https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1LifecycleRule/
title: Class LifecycleRule (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:19:05.715754+00:00
---

# Class LifecycleRule (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1LifecycleRule/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class LifecycleRule (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

Defines objects to read, create, and modify Object Lifecycle Rules. 

Object Lifecycle Rules allow to configure a Bucket to automatically delete or change the storage class of objects as they go through lifecycle events.

###### See Also

<https://cloud.google.com/storage/docs/lifecycle> for general information on Object Lifecycle Management in Google Cloud Storage. 

## Constructors 

### LifecycleRule(LifecycleRuleCondition, LifecycleRuleAction)

**Parameters**  
---  
**Name** | **Description**  
`condition` |  `LifecycleRuleCondition`   
  
`action` |  `LifecycleRuleAction`   
  
  
## Functions 

### static Delete()

Creates different types of LifecycleRule actions.

**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleAction` |   
  
### static AbortIncompleteMultipartUpload()

Creates different types of LifecycleRule actions.

**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleAction` |   
  
### static SetStorageClassStandard()

Creates different types of LifecycleRule actions.

**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleAction` |   
  
### static SetStorageClassMultiRegional()

Creates different types of LifecycleRule actions.

**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleAction` |   
  
### static SetStorageClassRegional()

Creates different types of LifecycleRule actions.

**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleAction` |   
  
### static SetStorageClassNearline()

Creates different types of LifecycleRule actions.

**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleAction` |   
  
### static SetStorageClassColdline()

Creates different types of LifecycleRule actions.

**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleAction` |   
  
### static SetStorageClassDurableReducedAvailability()

Creates different types of LifecycleRule actions.

**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleAction` |   
  
### static SetStorageClassArchive()

Creates different types of LifecycleRule actions.

**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleAction` |   
  
### static SetStorageClass(std::string)

Creates different types of LifecycleRule actions.

**Parameter**  
---  
**Name** | **Description**  
`storage_class` |  `std::string`   
  
**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleAction` |   
  
### static MaxAge(std::int32_t)

Creates different types of LifecycleRule rules.

**Parameter**  
---  
**Name** | **Description**  
`days` |  `std::int32_t`   
  
**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static CreatedBefore(absl::CivilDay)

Creates different types of LifecycleRule rules.

**Parameter**  
---  
**Name** | **Description**  
`date` |  `absl::CivilDay`   
  
**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static IsLive(bool)

Creates different types of LifecycleRule rules.

**Parameter**  
---  
**Name** | **Description**  
`value` |  `bool`   
  
**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static MatchesStorageClass(std::string)

Creates different types of LifecycleRule rules.

**Parameter**  
---  
**Name** | **Description**  
`storage_class` |  `std::string`   
  
**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static MatchesStorageClasses(std::initializer_list< std::string >)

Creates different types of LifecycleRule rules.

**Parameter**  
---  
**Name** | **Description**  
`list` |  `std::initializer_list< std::string >`   
  
**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static MatchesStorageClasses(Iterator, Iterator)

Creates different types of LifecycleRule rules.

**Parameters**  
---  
**Name** | **Description**  
`begin` |  `Iterator`   
  
`end` |  `Iterator`   
  
`typename Iterator` |  ``   
  
**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static MatchesStorageClassStandard()

Creates different types of LifecycleRule rules.

**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static MatchesStorageClassMultiRegional()

Creates different types of LifecycleRule rules.

**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static MatchesStorageClassRegional()

Creates different types of LifecycleRule rules.

**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static MatchesStorageClassNearline()

Creates different types of LifecycleRule rules.

**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static MatchesStorageClassColdline()

Creates different types of LifecycleRule rules.

**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static MatchesStorageClassDurableReducedAvailability()

Creates different types of LifecycleRule rules.

**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static MatchesStorageClassArchive()

Creates different types of LifecycleRule rules.

**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static NumNewerVersions(std::int32_t)

Creates different types of LifecycleRule rules.

**Parameter**  
---  
**Name** | **Description**  
`days` |  `std::int32_t`   
  
**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static DaysSinceNoncurrentTime(std::int32_t)

Creates different types of LifecycleRule rules.

**Parameter**  
---  
**Name** | **Description**  
`days` |  `std::int32_t`   
  
**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static NoncurrentTimeBefore(absl::CivilDay)

Creates different types of LifecycleRule rules.

**Parameter**  
---  
**Name** | **Description**  
`date` |  `absl::CivilDay`   
  
**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static DaysSinceCustomTime(std::int32_t)

Creates different types of LifecycleRule rules.

**Parameter**  
---  
**Name** | **Description**  
`days` |  `std::int32_t`   
  
**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static CustomTimeBefore(absl::CivilDay)

Creates different types of LifecycleRule rules.

**Parameter**  
---  
**Name** | **Description**  
`date` |  `absl::CivilDay`   
  
**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static MatchesPrefix(std::string)

Creates different types of LifecycleRule rules.

**Parameter**  
---  
**Name** | **Description**  
`prefix` |  `std::string`   
  
**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static MatchesPrefixes(std::initializer_list< std::string >)

Creates different types of LifecycleRule rules.

**Parameter**  
---  
**Name** | **Description**  
`list` |  `std::initializer_list< std::string >`   
  
**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static MatchesSuffix(std::string)

Creates different types of LifecycleRule rules.

**Parameter**  
---  
**Name** | **Description**  
`suffix` |  `std::string`   
  
**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### static MatchesSuffixes(std::initializer_list< std::string >)

Creates different types of LifecycleRule rules.

**Parameter**  
---  
**Name** | **Description**  
`list` |  `std::initializer_list< std::string >`   
  
**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` |   
  
### action() const

**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleAction const &` |   
  
### condition() const

**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition const &` |   
  
### static ConditionConjunction(Condition &&...)

Combines multiple [LifecycleRule](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/classgoogle_1_1cloud_1_1storage_1_1LifecycleRule) conditions using conjunction. 

Create a condition that require all the `condition` parameters to be met to take effect.

###### Example
    
    
    // Affect objects that are in the STANDARD storage class, have at
    // least 2 new versions, are at least 7 days old, and are alive.
    LifecycleRuleCondition condition = LifecycleRule::ConditionConjunction(
        LifecycleRule::NumNewerVersions(2),
        LifecycleRule::MatchesStorageClassStandard(),
        LifecycleRule::MaxAge(7), LifecycleRule::IsLive(true));
    

**Parameters**  
---  
**Name** | **Description**  
`condition` |  `Condition &&...`   
  
`typename...` |  ``   
  
**Exceptions**  
---  
**Type** | **Description**  
`std::invalid_argument` | if the list of parameters is contradictory, for example, `IsLive(true)` and `IsLive(false)` are in the `condition` list.   
**Returns**  
---  
**Type** | **Description**  
`LifecycleRuleCondition` | a [LifecycleRuleCondition](https://docs.cloud.google.com/cpp/docs/reference/storage/latest/structgoogle_1_1cloud_1_1storage_1_1LifecycleRuleCondition) that is satisfied when all the `condition` conditions are satisfied.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
