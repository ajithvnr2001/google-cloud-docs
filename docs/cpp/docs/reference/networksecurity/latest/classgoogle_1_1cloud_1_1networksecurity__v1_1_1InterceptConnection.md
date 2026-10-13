---
url: https://docs.cloud.google.com/cpp/docs/reference/networksecurity/latest/classgoogle_1_1cloud_1_1networksecurity__v1_1_1InterceptConnection/
title: Class InterceptConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:01:17.447101+00:00
---

# Class InterceptConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/networksecurity/latest/classgoogle_1_1cloud_1_1networksecurity__v1_1_1InterceptConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class InterceptConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0 

The [`InterceptConnection`](https://docs.cloud.google.com/cpp/docs/reference/networksecurity/latest/classgoogle_1_1cloud_1_1networksecurity__v1_1_1InterceptConnection) object for [`InterceptClient`](https://docs.cloud.google.com/cpp/docs/reference/networksecurity/latest/classgoogle_1_1cloud_1_1networksecurity__v1_1_1InterceptClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`InterceptClient`](https://docs.cloud.google.com/cpp/docs/reference/networksecurity/latest/classgoogle_1_1cloud_1_1networksecurity__v1_1_1InterceptClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`InterceptClient`](https://docs.cloud.google.com/cpp/docs/reference/networksecurity/latest/classgoogle_1_1cloud_1_1networksecurity__v1_1_1InterceptClient).

To create a concrete instance, see [`MakeInterceptConnection()`](https://docs.cloud.google.com/cpp/docs/reference/networksecurity/latest/namespacegoogle_1_1cloud_1_1networksecurity__v1).

For mocking, see [`networksecurity_v1_mocks::MockInterceptConnection`](https://docs.cloud.google.com/cpp/docs/reference/networksecurity/latest/classgoogle_1_1cloud_1_1networksecurity__v1__mocks_1_1MockInterceptConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual ListInterceptEndpointGroups(google::cloud::networksecurity::v1::ListInterceptEndpointGroupsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::ListInterceptEndpointGroupsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::networksecurity::v1::InterceptEndpointGroup >` |   
  
### virtual GetInterceptEndpointGroup(google::cloud::networksecurity::v1::GetInterceptEndpointGroupRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::GetInterceptEndpointGroupRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::networksecurity::v1::InterceptEndpointGroup >` |   
  
### virtual CreateInterceptEndpointGroup(google::cloud::networksecurity::v1::CreateInterceptEndpointGroupRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::CreateInterceptEndpointGroupRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::InterceptEndpointGroup > >` |   
  
### virtual CreateInterceptEndpointGroup(NoAwaitTag, google::cloud::networksecurity::v1::CreateInterceptEndpointGroupRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::networksecurity::v1::CreateInterceptEndpointGroupRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateInterceptEndpointGroup(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::InterceptEndpointGroup > >` |   
  
### virtual UpdateInterceptEndpointGroup(google::cloud::networksecurity::v1::UpdateInterceptEndpointGroupRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::UpdateInterceptEndpointGroupRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::InterceptEndpointGroup > >` |   
  
### virtual UpdateInterceptEndpointGroup(NoAwaitTag, google::cloud::networksecurity::v1::UpdateInterceptEndpointGroupRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::networksecurity::v1::UpdateInterceptEndpointGroupRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateInterceptEndpointGroup(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::InterceptEndpointGroup > >` |   
  
### virtual DeleteInterceptEndpointGroup(google::cloud::networksecurity::v1::DeleteInterceptEndpointGroupRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::DeleteInterceptEndpointGroupRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::OperationMetadata > >` |   
  
### virtual DeleteInterceptEndpointGroup(NoAwaitTag, google::cloud::networksecurity::v1::DeleteInterceptEndpointGroupRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::networksecurity::v1::DeleteInterceptEndpointGroupRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteInterceptEndpointGroup(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::OperationMetadata > >` |   
  
### virtual ListInterceptEndpointGroupAssociations(google::cloud::networksecurity::v1::ListInterceptEndpointGroupAssociationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::ListInterceptEndpointGroupAssociationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::networksecurity::v1::InterceptEndpointGroupAssociation >` |   
  
### virtual GetInterceptEndpointGroupAssociation(google::cloud::networksecurity::v1::GetInterceptEndpointGroupAssociationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::GetInterceptEndpointGroupAssociationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::networksecurity::v1::InterceptEndpointGroupAssociation >` |   
  
### virtual CreateInterceptEndpointGroupAssociation(google::cloud::networksecurity::v1::CreateInterceptEndpointGroupAssociationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::CreateInterceptEndpointGroupAssociationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::InterceptEndpointGroupAssociation > >` |   
  
### virtual CreateInterceptEndpointGroupAssociation(NoAwaitTag, google::cloud::networksecurity::v1::CreateInterceptEndpointGroupAssociationRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::networksecurity::v1::CreateInterceptEndpointGroupAssociationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateInterceptEndpointGroupAssociation(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::InterceptEndpointGroupAssociation > >` |   
  
### virtual UpdateInterceptEndpointGroupAssociation(google::cloud::networksecurity::v1::UpdateInterceptEndpointGroupAssociationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::UpdateInterceptEndpointGroupAssociationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::InterceptEndpointGroupAssociation > >` |   
  
### virtual UpdateInterceptEndpointGroupAssociation(NoAwaitTag, google::cloud::networksecurity::v1::UpdateInterceptEndpointGroupAssociationRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::networksecurity::v1::UpdateInterceptEndpointGroupAssociationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateInterceptEndpointGroupAssociation(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::InterceptEndpointGroupAssociation > >` |   
  
### virtual DeleteInterceptEndpointGroupAssociation(google::cloud::networksecurity::v1::DeleteInterceptEndpointGroupAssociationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::DeleteInterceptEndpointGroupAssociationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::OperationMetadata > >` |   
  
### virtual DeleteInterceptEndpointGroupAssociation(NoAwaitTag, google::cloud::networksecurity::v1::DeleteInterceptEndpointGroupAssociationRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::networksecurity::v1::DeleteInterceptEndpointGroupAssociationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteInterceptEndpointGroupAssociation(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::OperationMetadata > >` |   
  
### virtual ListInterceptDeploymentGroups(google::cloud::networksecurity::v1::ListInterceptDeploymentGroupsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::ListInterceptDeploymentGroupsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::networksecurity::v1::InterceptDeploymentGroup >` |   
  
### virtual GetInterceptDeploymentGroup(google::cloud::networksecurity::v1::GetInterceptDeploymentGroupRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::GetInterceptDeploymentGroupRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::networksecurity::v1::InterceptDeploymentGroup >` |   
  
### virtual CreateInterceptDeploymentGroup(google::cloud::networksecurity::v1::CreateInterceptDeploymentGroupRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::CreateInterceptDeploymentGroupRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::InterceptDeploymentGroup > >` |   
  
### virtual CreateInterceptDeploymentGroup(NoAwaitTag, google::cloud::networksecurity::v1::CreateInterceptDeploymentGroupRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::networksecurity::v1::CreateInterceptDeploymentGroupRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateInterceptDeploymentGroup(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::InterceptDeploymentGroup > >` |   
  
### virtual UpdateInterceptDeploymentGroup(google::cloud::networksecurity::v1::UpdateInterceptDeploymentGroupRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::UpdateInterceptDeploymentGroupRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::InterceptDeploymentGroup > >` |   
  
### virtual UpdateInterceptDeploymentGroup(NoAwaitTag, google::cloud::networksecurity::v1::UpdateInterceptDeploymentGroupRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::networksecurity::v1::UpdateInterceptDeploymentGroupRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateInterceptDeploymentGroup(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::InterceptDeploymentGroup > >` |   
  
### virtual DeleteInterceptDeploymentGroup(google::cloud::networksecurity::v1::DeleteInterceptDeploymentGroupRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::DeleteInterceptDeploymentGroupRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::OperationMetadata > >` |   
  
### virtual DeleteInterceptDeploymentGroup(NoAwaitTag, google::cloud::networksecurity::v1::DeleteInterceptDeploymentGroupRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::networksecurity::v1::DeleteInterceptDeploymentGroupRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteInterceptDeploymentGroup(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::OperationMetadata > >` |   
  
### virtual ListInterceptDeployments(google::cloud::networksecurity::v1::ListInterceptDeploymentsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::ListInterceptDeploymentsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::networksecurity::v1::InterceptDeployment >` |   
  
### virtual GetInterceptDeployment(google::cloud::networksecurity::v1::GetInterceptDeploymentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::GetInterceptDeploymentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::networksecurity::v1::InterceptDeployment >` |   
  
### virtual CreateInterceptDeployment(google::cloud::networksecurity::v1::CreateInterceptDeploymentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::CreateInterceptDeploymentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::InterceptDeployment > >` |   
  
### virtual CreateInterceptDeployment(NoAwaitTag, google::cloud::networksecurity::v1::CreateInterceptDeploymentRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::networksecurity::v1::CreateInterceptDeploymentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateInterceptDeployment(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::InterceptDeployment > >` |   
  
### virtual UpdateInterceptDeployment(google::cloud::networksecurity::v1::UpdateInterceptDeploymentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::UpdateInterceptDeploymentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::InterceptDeployment > >` |   
  
### virtual UpdateInterceptDeployment(NoAwaitTag, google::cloud::networksecurity::v1::UpdateInterceptDeploymentRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::networksecurity::v1::UpdateInterceptDeploymentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateInterceptDeployment(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::InterceptDeployment > >` |   
  
### virtual DeleteInterceptDeployment(google::cloud::networksecurity::v1::DeleteInterceptDeploymentRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::networksecurity::v1::DeleteInterceptDeploymentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::OperationMetadata > >` |   
  
### virtual DeleteInterceptDeployment(NoAwaitTag, google::cloud::networksecurity::v1::DeleteInterceptDeploymentRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::networksecurity::v1::DeleteInterceptDeploymentRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteInterceptDeployment(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::networksecurity::v1::OperationMetadata > >` |   
  
### virtual ListLocations(google::cloud::location::ListLocationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::ListLocationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::location::Location >` |   
  
### virtual GetLocation(google::cloud::location::GetLocationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::location::GetLocationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::location::Location >` |   
  
### virtual SetIamPolicy(google::iam::v1::SetIamPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::SetIamPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` |   
  
### virtual GetIamPolicy(google::iam::v1::GetIamPolicyRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::GetIamPolicyRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::Policy >` |   
  
### virtual TestIamPermissions(google::iam::v1::TestIamPermissionsRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::iam::v1::TestIamPermissionsRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::iam::v1::TestIamPermissionsResponse >` |   
  
### virtual ListOperations(google::longrunning::ListOperationsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::ListOperationsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::longrunning::Operation >` |   
  
### virtual GetOperation(google::longrunning::GetOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::GetOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteOperation(google::longrunning::DeleteOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::DeleteOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
### virtual CancelOperation(google::longrunning::CancelOperationRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::longrunning::CancelOperationRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`Status` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
