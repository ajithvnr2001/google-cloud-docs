---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__forwarding__rules__v1_1_1ForwardingRulesConnection/
title: Class ForwardingRulesConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:14:53.201966+00:00
---

# Class ForwardingRulesConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__forwarding__rules__v1_1_1ForwardingRulesConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class ForwardingRulesConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

The [`ForwardingRulesConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__forwarding__rules__v1_1_1ForwardingRulesConnection) object for [`ForwardingRulesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__forwarding__rules__v1_1_1ForwardingRulesClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`ForwardingRulesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__forwarding__rules__v1_1_1ForwardingRulesClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`ForwardingRulesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__forwarding__rules__v1_1_1ForwardingRulesClient).

To create a concrete instance, see `MakeForwardingRulesConnection()`.

For mocking, see [`compute_forwarding_rules_v1_mocks::MockForwardingRulesConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__forwarding__rules__v1__mocks_1_1MockForwardingRulesConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual AggregatedListForwardingRules(google::cloud::cpp::compute::forwarding_rules::v1::AggregatedListForwardingRulesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::forwarding_rules::v1::AggregatedListForwardingRulesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< std::pair< std::string, google::cloud::cpp::compute::v1::ForwardingRulesScopedList > >` |   
  
### virtual DeleteForwardingRule(google::cloud::cpp::compute::forwarding_rules::v1::DeleteForwardingRuleRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::forwarding_rules::v1::DeleteForwardingRuleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual DeleteForwardingRule(NoAwaitTag, google::cloud::cpp::compute::forwarding_rules::v1::DeleteForwardingRuleRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::forwarding_rules::v1::DeleteForwardingRuleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual DeleteForwardingRule(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual GetForwardingRule(google::cloud::cpp::compute::forwarding_rules::v1::GetForwardingRuleRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::forwarding_rules::v1::GetForwardingRuleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::ForwardingRule >` |   
  
### virtual InsertForwardingRule(google::cloud::cpp::compute::forwarding_rules::v1::InsertForwardingRuleRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::forwarding_rules::v1::InsertForwardingRuleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual InsertForwardingRule(NoAwaitTag, google::cloud::cpp::compute::forwarding_rules::v1::InsertForwardingRuleRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::forwarding_rules::v1::InsertForwardingRuleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual InsertForwardingRule(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual ListForwardingRules(google::cloud::cpp::compute::forwarding_rules::v1::ListForwardingRulesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::forwarding_rules::v1::ListForwardingRulesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::ForwardingRule >` |   
  
### virtual PatchForwardingRule(google::cloud::cpp::compute::forwarding_rules::v1::PatchForwardingRuleRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::forwarding_rules::v1::PatchForwardingRuleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual PatchForwardingRule(NoAwaitTag, google::cloud::cpp::compute::forwarding_rules::v1::PatchForwardingRuleRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::forwarding_rules::v1::PatchForwardingRuleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual PatchForwardingRule(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual SetLabels(google::cloud::cpp::compute::forwarding_rules::v1::SetLabelsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::forwarding_rules::v1::SetLabelsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual SetLabels(NoAwaitTag, google::cloud::cpp::compute::forwarding_rules::v1::SetLabelsRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::forwarding_rules::v1::SetLabelsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual SetLabels(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual SetTarget(google::cloud::cpp::compute::forwarding_rules::v1::SetTargetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::forwarding_rules::v1::SetTargetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual SetTarget(NoAwaitTag, google::cloud::cpp::compute::forwarding_rules::v1::SetTargetRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::forwarding_rules::v1::SetTargetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual SetTarget(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
