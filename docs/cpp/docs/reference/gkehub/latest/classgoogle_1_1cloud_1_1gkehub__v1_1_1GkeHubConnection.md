---
url: https://docs.cloud.google.com/cpp/docs/reference/gkehub/latest/classgoogle_1_1cloud_1_1gkehub__v1_1_1GkeHubConnection/
title: Class GkeHubConnection (3.13.0-rc) \u00a0|\u00a0 C++ client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:06.838221+00:00
---

# Class GkeHubConnection (3.13.0-rc)  |  C++ client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cpp/docs/reference/gkehub/latest/classgoogle_1_1cloud_1_1gkehub__v1_1_1GkeHubConnection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ C++ ](https://docs.cloud.google.com/cpp/docs)
  * [ Client libraries ](https://docs.cloud.google.com/cpp/docs/reference)



Send feedback 

#  Class GkeHubConnection (3.13.0-rc) Stay organized with collections  Save and categorize content based on your preferences. 

3.13.0-rc  3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  2.48.0-rc  2.47.1  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.0  2.40.0  2.39.0  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.0  2.27.0  2.26.0  2.25.1  2.24.0  2.23.0  2.22.1  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.1  2.14.0  2.13.0  2.12.0  2.11.0 

The [`GkeHubConnection`](https://docs.cloud.google.com/cpp/docs/reference/gkehub/latest/classgoogle_1_1cloud_1_1gkehub__v1_1_1GkeHubConnection) object for [`GkeHubClient`](https://docs.cloud.google.com/cpp/docs/reference/gkehub/latest/classgoogle_1_1cloud_1_1gkehub__v1_1_1GkeHubClient). 

This interface defines virtual methods for each of the user-facing overload sets in [`GkeHubClient`](https://docs.cloud.google.com/cpp/docs/reference/gkehub/latest/classgoogle_1_1cloud_1_1gkehub__v1_1_1GkeHubClient). This allows users to inject custom behavior (e.g., with a Google Mock object) when writing tests that use objects of type [`GkeHubClient`](https://docs.cloud.google.com/cpp/docs/reference/gkehub/latest/classgoogle_1_1cloud_1_1gkehub__v1_1_1GkeHubClient).

To create a concrete instance, see [`MakeGkeHubConnection()`](https://docs.cloud.google.com/cpp/docs/reference/gkehub/latest/namespacegoogle_1_1cloud_1_1gkehub__v1).

For mocking, see [`gkehub_v1_mocks::MockGkeHubConnection`](https://docs.cloud.google.com/cpp/docs/reference/gkehub/latest/classgoogle_1_1cloud_1_1gkehub__v1__mocks_1_1MockGkeHubConnection). 

## Functions 

### virtual options()

**Returns**  
---  
**Type** | **Description**  
`Options` |   
  
### virtual ListMemberships(google::cloud::gkehub::v1::ListMembershipsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::ListMembershipsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::gkehub::v1::Membership >` |   
  
### virtual ListBoundMemberships(google::cloud::gkehub::v1::ListBoundMembershipsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::ListBoundMembershipsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::gkehub::v1::Membership >` |   
  
### virtual ListFeatures(google::cloud::gkehub::v1::ListFeaturesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::ListFeaturesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::gkehub::v1::Feature >` |   
  
### virtual GetMembership(google::cloud::gkehub::v1::GetMembershipRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::GetMembershipRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::gkehub::v1::Membership >` |   
  
### virtual GetFeature(google::cloud::gkehub::v1::GetFeatureRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::GetFeatureRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::gkehub::v1::Feature >` |   
  
### virtual CreateMembership(google::cloud::gkehub::v1::CreateMembershipRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::CreateMembershipRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Membership > >` |   
  
### virtual CreateMembership(NoAwaitTag, google::cloud::gkehub::v1::CreateMembershipRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::CreateMembershipRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateMembership(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Membership > >` |   
  
### virtual CreateFeature(google::cloud::gkehub::v1::CreateFeatureRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::CreateFeatureRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Feature > >` |   
  
### virtual CreateFeature(NoAwaitTag, google::cloud::gkehub::v1::CreateFeatureRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::CreateFeatureRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateFeature(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Feature > >` |   
  
### virtual DeleteMembership(google::cloud::gkehub::v1::DeleteMembershipRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::DeleteMembershipRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::OperationMetadata > >` |   
  
### virtual DeleteMembership(NoAwaitTag, google::cloud::gkehub::v1::DeleteMembershipRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::DeleteMembershipRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteMembership(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::OperationMetadata > >` |   
  
### virtual DeleteFeature(google::cloud::gkehub::v1::DeleteFeatureRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::DeleteFeatureRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::OperationMetadata > >` |   
  
### virtual DeleteFeature(NoAwaitTag, google::cloud::gkehub::v1::DeleteFeatureRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::DeleteFeatureRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteFeature(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::OperationMetadata > >` |   
  
### virtual UpdateMembership(google::cloud::gkehub::v1::UpdateMembershipRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::UpdateMembershipRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Membership > >` |   
  
### virtual UpdateMembership(NoAwaitTag, google::cloud::gkehub::v1::UpdateMembershipRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::UpdateMembershipRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateMembership(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Membership > >` |   
  
### virtual UpdateFeature(google::cloud::gkehub::v1::UpdateFeatureRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::UpdateFeatureRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Feature > >` |   
  
### virtual UpdateFeature(NoAwaitTag, google::cloud::gkehub::v1::UpdateFeatureRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::UpdateFeatureRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateFeature(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Feature > >` |   
  
### virtual GenerateConnectManifest(google::cloud::gkehub::v1::GenerateConnectManifestRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::GenerateConnectManifestRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::gkehub::v1::GenerateConnectManifestResponse >` |   
  
### virtual CreateFleet(google::cloud::gkehub::v1::CreateFleetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::CreateFleetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Fleet > >` |   
  
### virtual CreateFleet(NoAwaitTag, google::cloud::gkehub::v1::CreateFleetRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::CreateFleetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateFleet(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Fleet > >` |   
  
### virtual GetFleet(google::cloud::gkehub::v1::GetFleetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::GetFleetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::gkehub::v1::Fleet >` |   
  
### virtual UpdateFleet(google::cloud::gkehub::v1::UpdateFleetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::UpdateFleetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Fleet > >` |   
  
### virtual UpdateFleet(NoAwaitTag, google::cloud::gkehub::v1::UpdateFleetRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::UpdateFleetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateFleet(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Fleet > >` |   
  
### virtual DeleteFleet(google::cloud::gkehub::v1::DeleteFleetRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::DeleteFleetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::OperationMetadata > >` |   
  
### virtual DeleteFleet(NoAwaitTag, google::cloud::gkehub::v1::DeleteFleetRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::DeleteFleetRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteFleet(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::OperationMetadata > >` |   
  
### virtual ListFleets(google::cloud::gkehub::v1::ListFleetsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::ListFleetsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::gkehub::v1::Fleet >` |   
  
### virtual GetScopeNamespace(google::cloud::gkehub::v1::GetScopeNamespaceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::GetScopeNamespaceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::gkehub::v1::Namespace >` |   
  
### virtual CreateScopeNamespace(google::cloud::gkehub::v1::CreateScopeNamespaceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::CreateScopeNamespaceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Namespace > >` |   
  
### virtual CreateScopeNamespace(NoAwaitTag, google::cloud::gkehub::v1::CreateScopeNamespaceRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::CreateScopeNamespaceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateScopeNamespace(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Namespace > >` |   
  
### virtual UpdateScopeNamespace(google::cloud::gkehub::v1::UpdateScopeNamespaceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::UpdateScopeNamespaceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Namespace > >` |   
  
### virtual UpdateScopeNamespace(NoAwaitTag, google::cloud::gkehub::v1::UpdateScopeNamespaceRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::UpdateScopeNamespaceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateScopeNamespace(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Namespace > >` |   
  
### virtual DeleteScopeNamespace(google::cloud::gkehub::v1::DeleteScopeNamespaceRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::DeleteScopeNamespaceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::OperationMetadata > >` |   
  
### virtual DeleteScopeNamespace(NoAwaitTag, google::cloud::gkehub::v1::DeleteScopeNamespaceRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::DeleteScopeNamespaceRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteScopeNamespace(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::OperationMetadata > >` |   
  
### virtual ListScopeNamespaces(google::cloud::gkehub::v1::ListScopeNamespacesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::ListScopeNamespacesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::gkehub::v1::Namespace >` |   
  
### virtual GetScopeRBACRoleBinding(google::cloud::gkehub::v1::GetScopeRBACRoleBindingRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::GetScopeRBACRoleBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::gkehub::v1::RBACRoleBinding >` |   
  
### virtual CreateScopeRBACRoleBinding(google::cloud::gkehub::v1::CreateScopeRBACRoleBindingRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::CreateScopeRBACRoleBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::RBACRoleBinding > >` |   
  
### virtual CreateScopeRBACRoleBinding(NoAwaitTag, google::cloud::gkehub::v1::CreateScopeRBACRoleBindingRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::CreateScopeRBACRoleBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateScopeRBACRoleBinding(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::RBACRoleBinding > >` |   
  
### virtual UpdateScopeRBACRoleBinding(google::cloud::gkehub::v1::UpdateScopeRBACRoleBindingRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::UpdateScopeRBACRoleBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::RBACRoleBinding > >` |   
  
### virtual UpdateScopeRBACRoleBinding(NoAwaitTag, google::cloud::gkehub::v1::UpdateScopeRBACRoleBindingRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::UpdateScopeRBACRoleBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateScopeRBACRoleBinding(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::RBACRoleBinding > >` |   
  
### virtual DeleteScopeRBACRoleBinding(google::cloud::gkehub::v1::DeleteScopeRBACRoleBindingRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::DeleteScopeRBACRoleBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::OperationMetadata > >` |   
  
### virtual DeleteScopeRBACRoleBinding(NoAwaitTag, google::cloud::gkehub::v1::DeleteScopeRBACRoleBindingRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::DeleteScopeRBACRoleBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteScopeRBACRoleBinding(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::OperationMetadata > >` |   
  
### virtual ListScopeRBACRoleBindings(google::cloud::gkehub::v1::ListScopeRBACRoleBindingsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::ListScopeRBACRoleBindingsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::gkehub::v1::RBACRoleBinding >` |   
  
### virtual GetScope(google::cloud::gkehub::v1::GetScopeRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::GetScopeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::gkehub::v1::Scope >` |   
  
### virtual CreateScope(google::cloud::gkehub::v1::CreateScopeRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::CreateScopeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Scope > >` |   
  
### virtual CreateScope(NoAwaitTag, google::cloud::gkehub::v1::CreateScopeRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::CreateScopeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateScope(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Scope > >` |   
  
### virtual UpdateScope(google::cloud::gkehub::v1::UpdateScopeRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::UpdateScopeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Scope > >` |   
  
### virtual UpdateScope(NoAwaitTag, google::cloud::gkehub::v1::UpdateScopeRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::UpdateScopeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateScope(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::Scope > >` |   
  
### virtual DeleteScope(google::cloud::gkehub::v1::DeleteScopeRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::DeleteScopeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::OperationMetadata > >` |   
  
### virtual DeleteScope(NoAwaitTag, google::cloud::gkehub::v1::DeleteScopeRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::DeleteScopeRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteScope(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::OperationMetadata > >` |   
  
### virtual ListScopes(google::cloud::gkehub::v1::ListScopesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::ListScopesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::gkehub::v1::Scope >` |   
  
### virtual ListPermittedScopes(google::cloud::gkehub::v1::ListPermittedScopesRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::ListPermittedScopesRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::gkehub::v1::Scope >` |   
  
### virtual GetMembershipBinding(google::cloud::gkehub::v1::GetMembershipBindingRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::GetMembershipBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::gkehub::v1::MembershipBinding >` |   
  
### virtual CreateMembershipBinding(google::cloud::gkehub::v1::CreateMembershipBindingRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::CreateMembershipBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::MembershipBinding > >` |   
  
### virtual CreateMembershipBinding(NoAwaitTag, google::cloud::gkehub::v1::CreateMembershipBindingRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::CreateMembershipBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateMembershipBinding(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::MembershipBinding > >` |   
  
### virtual UpdateMembershipBinding(google::cloud::gkehub::v1::UpdateMembershipBindingRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::UpdateMembershipBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::MembershipBinding > >` |   
  
### virtual UpdateMembershipBinding(NoAwaitTag, google::cloud::gkehub::v1::UpdateMembershipBindingRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::UpdateMembershipBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateMembershipBinding(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::MembershipBinding > >` |   
  
### virtual DeleteMembershipBinding(google::cloud::gkehub::v1::DeleteMembershipBindingRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::DeleteMembershipBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::OperationMetadata > >` |   
  
### virtual DeleteMembershipBinding(NoAwaitTag, google::cloud::gkehub::v1::DeleteMembershipBindingRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::DeleteMembershipBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteMembershipBinding(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::OperationMetadata > >` |   
  
### virtual ListMembershipBindings(google::cloud::gkehub::v1::ListMembershipBindingsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::ListMembershipBindingsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::gkehub::v1::MembershipBinding >` |   
  
### virtual GetMembershipRBACRoleBinding(google::cloud::gkehub::v1::GetMembershipRBACRoleBindingRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::GetMembershipRBACRoleBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::gkehub::v1::RBACRoleBinding >` |   
  
### virtual CreateMembershipRBACRoleBinding(google::cloud::gkehub::v1::CreateMembershipRBACRoleBindingRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::CreateMembershipRBACRoleBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::RBACRoleBinding > >` |   
  
### virtual CreateMembershipRBACRoleBinding(NoAwaitTag, google::cloud::gkehub::v1::CreateMembershipRBACRoleBindingRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::CreateMembershipRBACRoleBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual CreateMembershipRBACRoleBinding(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::RBACRoleBinding > >` |   
  
### virtual UpdateMembershipRBACRoleBinding(google::cloud::gkehub::v1::UpdateMembershipRBACRoleBindingRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::UpdateMembershipRBACRoleBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::RBACRoleBinding > >` |   
  
### virtual UpdateMembershipRBACRoleBinding(NoAwaitTag, google::cloud::gkehub::v1::UpdateMembershipRBACRoleBindingRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::UpdateMembershipRBACRoleBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual UpdateMembershipRBACRoleBinding(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::RBACRoleBinding > >` |   
  
### virtual DeleteMembershipRBACRoleBinding(google::cloud::gkehub::v1::DeleteMembershipRBACRoleBindingRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::DeleteMembershipRBACRoleBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::OperationMetadata > >` |   
  
### virtual DeleteMembershipRBACRoleBinding(NoAwaitTag, google::cloud::gkehub::v1::DeleteMembershipRBACRoleBindingRequest const &)

**Parameters**  
---  
**Name** | **Description**  
`` |  `NoAwaitTag`   
  
`request` |  `google::cloud::gkehub::v1::DeleteMembershipRBACRoleBindingRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::longrunning::Operation >` |   
  
### virtual DeleteMembershipRBACRoleBinding(google::longrunning::Operation const &)

**Parameter**  
---  
**Name** | **Description**  
`operation` |  `google::longrunning::Operation const &`   
  
**Returns**  
---  
**Type** | **Description**  
`future< StatusOr< google::cloud::gkehub::v1::OperationMetadata > >` |   
  
### virtual ListMembershipRBACRoleBindings(google::cloud::gkehub::v1::ListMembershipRBACRoleBindingsRequest)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::ListMembershipRBACRoleBindingsRequest`   
  
**Returns**  
---  
**Type** | **Description**  
`StreamRange< google::cloud::gkehub::v1::RBACRoleBinding >` |   
  
### virtual GenerateMembershipRBACRoleBindingYAML(google::cloud::gkehub::v1::GenerateMembershipRBACRoleBindingYAMLRequest const &)

**Parameter**  
---  
**Name** | **Description**  
`request` |  `google::cloud::gkehub::v1::GenerateMembershipRBACRoleBindingYAMLRequest const &`   
  
**Returns**  
---  
**Type** | **Description**  
`StatusOr< google::cloud::gkehub::v1::GenerateMembershipRBACRoleBindingYAMLResponse >` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
