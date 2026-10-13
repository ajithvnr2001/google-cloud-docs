---
url: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__organization__security__policies__v1_1_1OrganizationSecurityPoliciesConnection/
title: Class OrganizationSecurityPoliciesConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:28:13.914112+00:00
---

# Class OrganizationSecurityPoliciesConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__organization__security__policies__v1_1_1OrganizationSecurityPoliciesConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class OrganizationSecurityPoliciesConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1 

The [`OrganizationSecurityPoliciesConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__organization__security__policies__v1_1_1OrganizationSecurityPoliciesConnection) object for [`OrganizationSecurityPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__organization__security__policies__v1_1_1OrganizationSecurityPoliciesClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`OrganizationSecurityPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__organization__security__policies__v1_1_1OrganizationSecurityPoliciesClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`OrganizationSecurityPoliciesClient`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__organization__security__policies__v1_1_1OrganizationSecurityPoliciesClient).

To create a concrete instance, see `MakeOrganizationSecurityPoliciesConnection()`.

For mocking, see [`compute_organization_security_policies_v1_mocks::MockOrganizationSecurityPoliciesConnection`](https://docs.cloud.google.com/cpp/docs/reference/compute/latest/classgoogle_1_1cloud_1_1compute__organization__security__policies__v1__mocks_1_1MockOrganizationSecurityPoliciesConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual AddAssociation(google::cloud::cpp::compute::organization_security_policies::v1::AddAssociationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::AddAssociationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual AddAssociation(NoAwaitTag, google::cloud::cpp::compute::organization_security_policies::v1::AddAssociationRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::AddAssociationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual AddAssociation(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual AddRule(google::cloud::cpp::compute::organization_security_policies::v1::AddRuleRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::AddRuleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual AddRule(NoAwaitTag, google::cloud::cpp::compute::organization_security_policies::v1::AddRuleRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::AddRuleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual AddRule(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual CopyRules(google::cloud::cpp::compute::organization_security_policies::v1::CopyRulesRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::CopyRulesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual CopyRules(NoAwaitTag, google::cloud::cpp::compute::organization_security_policies::v1::CopyRulesRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::CopyRulesRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual CopyRules(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual DeleteSecurityPolicy(google::cloud::cpp::compute::organization_security_policies::v1::DeleteSecurityPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::DeleteSecurityPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual DeleteSecurityPolicy(NoAwaitTag, google::cloud::cpp::compute::organization_security_policies::v1::DeleteSecurityPolicyRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::DeleteSecurityPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual DeleteSecurityPolicy(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual GetSecurityPolicy(google::cloud::cpp::compute::organization_security_policies::v1::GetSecurityPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::GetSecurityPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::SecurityPolicy >` |   
  
### virtual GetAssociation(google::cloud::cpp::compute::organization_security_policies::v1::GetAssociationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::GetAssociationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::SecurityPolicyAssociation >` |   
  
### virtual GetRule(google::cloud::cpp::compute::organization_security_policies::v1::GetRuleRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::GetRuleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::SecurityPolicyRule >` |   
  
### virtual InsertSecurityPolicy(google::cloud::cpp::compute::organization_security_policies::v1::InsertSecurityPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::InsertSecurityPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual InsertSecurityPolicy(NoAwaitTag, google::cloud::cpp::compute::organization_security_policies::v1::InsertSecurityPolicyRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::InsertSecurityPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual InsertSecurityPolicy(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual ListOrganizationSecurityPolicies(google::cloud::cpp::compute::organization_security_policies::v1::ListOrganizationSecurityPoliciesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::ListOrganizationSecurityPoliciesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::cpp::compute::v1::SecurityPolicy >` |   
  
### virtual ListAssociations(google::cloud::cpp::compute::organization_security_policies::v1::ListAssociationsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::ListAssociationsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::OrganizationSecurityPoliciesListAssociationsResponse >` |   
  
### virtual ListPreconfiguredExpressionSets(google::cloud::cpp::compute::organization_security_policies::v1::ListPreconfiguredExpressionSetsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::ListPreconfiguredExpressionSetsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::SecurityPoliciesListPreconfiguredExpressionSetsResponse >` |   
  
### virtual Move(google::cloud::cpp::compute::organization_security_policies::v1::MoveRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::MoveRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual Move(NoAwaitTag, google::cloud::cpp::compute::organization_security_policies::v1::MoveRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::MoveRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual Move(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual PatchSecurityPolicy(google::cloud::cpp::compute::organization_security_policies::v1::PatchSecurityPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::PatchSecurityPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual PatchSecurityPolicy(NoAwaitTag, google::cloud::cpp::compute::organization_security_policies::v1::PatchSecurityPolicyRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::PatchSecurityPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual PatchSecurityPolicy(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual PatchRule(google::cloud::cpp::compute::organization_security_policies::v1::PatchRuleRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::PatchRuleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual PatchRule(NoAwaitTag, google::cloud::cpp::compute::organization_security_policies::v1::PatchRuleRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::PatchRuleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual PatchRule(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual RemoveAssociation(google::cloud::cpp::compute::organization_security_policies::v1::RemoveAssociationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::RemoveAssociationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual RemoveAssociation(NoAwaitTag, google::cloud::cpp::compute::organization_security_policies::v1::RemoveAssociationRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::RemoveAssociationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual RemoveAssociation(google::cloud::cpp::compute::v1::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::cloud::cpp::compute::v1::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual RemoveRule(google::cloud::cpp::compute::organization_security_policies::v1::RemoveRuleRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::RemoveRuleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::cpp::compute::v1::Operation > >` |   
  
### virtual RemoveRule(NoAwaitTag, google::cloud::cpp::compute::organization_security_policies::v1::RemoveRuleRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::cpp::compute::organization_security_policies::v1::RemoveRuleRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::cpp::compute::v1::Operation >` |   
  
### virtual RemoveRule(google::cloud::cpp::compute::v1::Operation const &)

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
