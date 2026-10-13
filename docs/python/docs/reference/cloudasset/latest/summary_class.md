---
url: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/summary_class/
title: Package Classes (4.5.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:35:14.046843+00:00
---

# Package Classes (4.5.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (4.5.0) Stay organized with collections  Save and categorize content based on your preferences. 

4.5.0 (latest)  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.30.1  3.29.2  3.28.0  3.27.1  3.26.4  3.25.1  3.24.3  3.23.0  3.22.0  3.21.0  3.20.1  3.19.1  3.18.1  3.17.1  3.16.0  3.15.0  3.14.2  3.13.1  3.12.0  3.11.0  3.10.0  3.9.1  3.8.1  3.7.1  3.6.1  3.5.0  3.4.0  3.3.0  3.2.1  3.1.0  2.2.2  2.1.0  2.0.0  1.3.2  1.2.0  1.1.0  1.0.0  0.10.0  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.1  0.3.0 

Summary of entries of Classes for cloudasset.

## Classes 

### [AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceAsyncClient)

Asset service definition.

### [AssetServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.AssetServiceClient)

Asset service definition.

### [AnalyzeOrgPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPoliciesAsyncPager)

A pager for iterating through `analyze_org_policies` requests.

This class thinly wraps an initial [AnalyzeOrgPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `org_policy_results` field.

If there are more pages, the `__aiter__` method will make additional `AnalyzeOrgPolicies` requests and continue to iterate through the `org_policy_results` field on the corresponding responses.

All the usual [AnalyzeOrgPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AnalyzeOrgPoliciesPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPoliciesPager)

A pager for iterating through `analyze_org_policies` requests.

This class thinly wraps an initial [AnalyzeOrgPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPoliciesResponse) object, and provides an `__iter__` method to iterate through its `org_policy_results` field.

If there are more pages, the `__iter__` method will make additional `AnalyzeOrgPolicies` requests and continue to iterate through the `org_policy_results` field on the corresponding responses.

All the usual [AnalyzeOrgPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AnalyzeOrgPolicyGovernedAssetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedAssetsAsyncPager)

A pager for iterating through `analyze_org_policy_governed_assets` requests.

This class thinly wraps an initial [AnalyzeOrgPolicyGovernedAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsResponse) object, and provides an `__aiter__` method to iterate through its `governed_assets` field.

If there are more pages, the `__aiter__` method will make additional `AnalyzeOrgPolicyGovernedAssets` requests and continue to iterate through the `governed_assets` field on the corresponding responses.

All the usual [AnalyzeOrgPolicyGovernedAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AnalyzeOrgPolicyGovernedAssetsPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedAssetsPager)

A pager for iterating through `analyze_org_policy_governed_assets` requests.

This class thinly wraps an initial [AnalyzeOrgPolicyGovernedAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsResponse) object, and provides an `__iter__` method to iterate through its `governed_assets` field.

If there are more pages, the `__iter__` method will make additional `AnalyzeOrgPolicyGovernedAssets` requests and continue to iterate through the `governed_assets` field on the corresponding responses.

All the usual [AnalyzeOrgPolicyGovernedAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AnalyzeOrgPolicyGovernedContainersAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedContainersAsyncPager)

A pager for iterating through `analyze_org_policy_governed_containers` requests.

This class thinly wraps an initial [AnalyzeOrgPolicyGovernedContainersResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersResponse) object, and provides an `__aiter__` method to iterate through its `governed_containers` field.

If there are more pages, the `__aiter__` method will make additional `AnalyzeOrgPolicyGovernedContainers` requests and continue to iterate through the `governed_containers` field on the corresponding responses.

All the usual [AnalyzeOrgPolicyGovernedContainersResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AnalyzeOrgPolicyGovernedContainersPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.AnalyzeOrgPolicyGovernedContainersPager)

A pager for iterating through `analyze_org_policy_governed_containers` requests.

This class thinly wraps an initial [AnalyzeOrgPolicyGovernedContainersResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersResponse) object, and provides an `__iter__` method to iterate through its `governed_containers` field.

If there are more pages, the `__iter__` method will make additional `AnalyzeOrgPolicyGovernedContainers` requests and continue to iterate through the `governed_containers` field on the corresponding responses.

All the usual [AnalyzeOrgPolicyGovernedContainersResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAssetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.ListAssetsAsyncPager)

A pager for iterating through `list_assets` requests.

This class thinly wraps an initial [ListAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListAssetsResponse) object, and provides an `__aiter__` method to iterate through its `assets` field.

If there are more pages, the `__aiter__` method will make additional `ListAssets` requests and continue to iterate through the `assets` field on the corresponding responses.

All the usual [ListAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListAssetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAssetsPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.ListAssetsPager)

A pager for iterating through `list_assets` requests.

This class thinly wraps an initial [ListAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListAssetsResponse) object, and provides an `__iter__` method to iterate through its `assets` field.

If there are more pages, the `__iter__` method will make additional `ListAssets` requests and continue to iterate through the `assets` field on the corresponding responses.

All the usual [ListAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListAssetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSavedQueriesAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.ListSavedQueriesAsyncPager)

A pager for iterating through `list_saved_queries` requests.

This class thinly wraps an initial [ListSavedQueriesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListSavedQueriesResponse) object, and provides an `__aiter__` method to iterate through its `saved_queries` field.

If there are more pages, the `__aiter__` method will make additional `ListSavedQueries` requests and continue to iterate through the `saved_queries` field on the corresponding responses.

All the usual [ListSavedQueriesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListSavedQueriesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSavedQueriesPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.ListSavedQueriesPager)

A pager for iterating through `list_saved_queries` requests.

This class thinly wraps an initial [ListSavedQueriesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListSavedQueriesResponse) object, and provides an `__iter__` method to iterate through its `saved_queries` field.

If there are more pages, the `__iter__` method will make additional `ListSavedQueries` requests and continue to iterate through the `saved_queries` field on the corresponding responses.

All the usual [ListSavedQueriesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListSavedQueriesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAllIamPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.SearchAllIamPoliciesAsyncPager)

A pager for iterating through `search_all_iam_policies` requests.

This class thinly wraps an initial [SearchAllIamPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllIamPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `results` field.

If there are more pages, the `__aiter__` method will make additional `SearchAllIamPolicies` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchAllIamPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllIamPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAllIamPoliciesPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.SearchAllIamPoliciesPager)

A pager for iterating through `search_all_iam_policies` requests.

This class thinly wraps an initial [SearchAllIamPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllIamPoliciesResponse) object, and provides an `__iter__` method to iterate through its `results` field.

If there are more pages, the `__iter__` method will make additional `SearchAllIamPolicies` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchAllIamPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllIamPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAllResourcesAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.SearchAllResourcesAsyncPager)

A pager for iterating through `search_all_resources` requests.

This class thinly wraps an initial [SearchAllResourcesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllResourcesResponse) object, and provides an `__aiter__` method to iterate through its `results` field.

If there are more pages, the `__aiter__` method will make additional `SearchAllResources` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchAllResourcesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllResourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAllResourcesPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers.SearchAllResourcesPager)

A pager for iterating through `search_all_resources` requests.

This class thinly wraps an initial [SearchAllResourcesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllResourcesResponse) object, and provides an `__iter__` method to iterate through its `results` field.

If there are more pages, the `__iter__` method will make additional `SearchAllResources` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchAllResourcesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllResourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AnalyzeIamPolicyLongrunningMetadata](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeIamPolicyLongrunningMetadata)

Represents the metadata of the longrunning operation for the AnalyzeIamPolicyLongrunning RPC.

### [AnalyzeIamPolicyLongrunningRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeIamPolicyLongrunningRequest)

A request message for AssetService.AnalyzeIamPolicyLongrunning.

### [AnalyzeIamPolicyLongrunningResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeIamPolicyLongrunningResponse)

A response message for AssetService.AnalyzeIamPolicyLongrunning.

### [AnalyzeIamPolicyRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeIamPolicyRequest)

A request message for AssetService.AnalyzeIamPolicy.

### [AnalyzeIamPolicyResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeIamPolicyResponse)

A response message for AssetService.AnalyzeIamPolicy.

### [IamPolicyAnalysis](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeIamPolicyResponse.IamPolicyAnalysis)

An analysis message to group the query and results.

### [AnalyzeMoveRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeMoveRequest)

The request message for performing resource move analysis.

### [AnalysisView](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeMoveRequest.AnalysisView)

View enum for supporting partial analysis responses.

### [AnalyzeMoveResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeMoveResponse)

The response message for resource move analysis.

### [AnalyzeOrgPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPoliciesRequest)

A request message for AssetService.AnalyzeOrgPolicies.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnalyzeOrgPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPoliciesResponse)

The response message for AssetService.AnalyzeOrgPolicies.

### [OrgPolicyResult](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPoliciesResponse.OrgPolicyResult)

The organization policy result to the query.

### [AnalyzeOrgPolicyGovernedAssetsRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsRequest)

A request message for AssetService.AnalyzeOrgPolicyGovernedAssets.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnalyzeOrgPolicyGovernedAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsResponse)

The response message for AssetService.AnalyzeOrgPolicyGovernedAssets.

### [GovernedAsset](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedAsset)

Represents a Google Cloud asset(resource or IAM policy) governed by the organization policies of the AnalyzeOrgPolicyGovernedAssetsRequest.constraint.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GovernedIamPolicy](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedIamPolicy)

The IAM policies governed by the organization policies of the AnalyzeOrgPolicyGovernedAssetsRequest.constraint.

### [GovernedResource](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedAssetsResponse.GovernedResource)

The Google Cloud resources governed by the organization policies of the AnalyzeOrgPolicyGovernedAssetsRequest.constraint.

### [AnalyzeOrgPolicyGovernedContainersRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersRequest)

A request message for AssetService.AnalyzeOrgPolicyGovernedContainers.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AnalyzeOrgPolicyGovernedContainersResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersResponse)

The response message for AssetService.AnalyzeOrgPolicyGovernedContainers.

### [GovernedContainer](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzeOrgPolicyGovernedContainersResponse.GovernedContainer)

The organization/folder/project resource governed by organization policies of AnalyzeOrgPolicyGovernedContainersRequest.constraint.

### [AnalyzerOrgPolicy](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzerOrgPolicy)

This organization policy message is a modified version of the one defined in the Organization Policy system. This message contains several fields defined in the original organization policy with some new fields for analysis purpose.

### [Rule](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzerOrgPolicy.Rule)

This rule message is a customized version of the one defined in the Organization Policy system. In addition to the fields defined in the original organization policy, it contains additional field(s) under specific circumstances to support analysis results.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [StringValues](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzerOrgPolicy.Rule.StringValues)

The string values for the list constraints.

### [AnalyzerOrgPolicyConstraint](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzerOrgPolicyConstraint)

The organization policy constraint definition.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Constraint](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzerOrgPolicyConstraint.Constraint)

The definition of a constraint.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BooleanConstraint](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzerOrgPolicyConstraint.Constraint.BooleanConstraint)

A `Constraint` that is either enforced or not.

For example a constraint `constraints/compute.disableSerialPortAccess`. If it is enforced on a VM instance, serial port connections will not be opened to that instance.

### [ConstraintDefault](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzerOrgPolicyConstraint.Constraint.ConstraintDefault)

Specifies the default behavior in the absence of any `Policy` for the `Constraint`. This must not be `CONSTRAINT_DEFAULT_UNSPECIFIED`.

### [ListConstraint](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzerOrgPolicyConstraint.Constraint.ListConstraint)

A `Constraint` that allows or disallows a list of string values, which are configured by an organization's policy administrator with a `Policy`.

### [CustomConstraint](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzerOrgPolicyConstraint.CustomConstraint)

The definition of a custom constraint.

### [ActionType](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzerOrgPolicyConstraint.CustomConstraint.ActionType)

Allow or deny type.

### [MethodType](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AnalyzerOrgPolicyConstraint.CustomConstraint.MethodType)

The operation in which this constraint will be applied. For example: If the constraint applies only when create VMs, the method_types will be "CREATE" only. If the constraint applied when create or delete VMs, the method_types will be "CREATE" and "DELETE".

### [Asset](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.Asset)

An asset in Google Cloud. An asset can be any resource in the Google Cloud `resource hierarchy <https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy>`**, a resource outside the Google Cloud resource hierarchy (such as Google Kubernetes Engine clusters and objects), or a policy (e.g. IAM policy), or a relationship (e.g. an INSTANCE_TO_INSTANCEGROUP relationship). See`Supported asset types <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`** for more information.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AssetEnrichment](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AssetEnrichment)

The enhanced metadata information for a resource.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AttachedResource](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.AttachedResource)

Attached resource representation, which is defined by the corresponding service provider. It represents an attached resource's payload.

### [BatchGetAssetsHistoryRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.BatchGetAssetsHistoryRequest)

Batch get assets history request.

### [BatchGetAssetsHistoryResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.BatchGetAssetsHistoryResponse)

Batch get assets history response.

### [BatchGetEffectiveIamPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.BatchGetEffectiveIamPoliciesRequest)

A request message for AssetService.BatchGetEffectiveIamPolicies.

### [BatchGetEffectiveIamPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.BatchGetEffectiveIamPoliciesResponse)

A response message for AssetService.BatchGetEffectiveIamPolicies.

### [EffectiveIamPolicy](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy)

The effective IAM policies on one resource.

### [PolicyInfo](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.BatchGetEffectiveIamPoliciesResponse.EffectiveIamPolicy.PolicyInfo)

The IAM policy and its attached resource.

### [BigQueryDestination](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.BigQueryDestination)

A BigQuery destination for exporting assets to.

### [ConditionEvaluation](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ConditionEvaluation)

The condition evaluation.

### [EvaluationValue](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ConditionEvaluation.EvaluationValue)

Value of this expression.

### [ContentType](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ContentType)

Asset content type.

### [CreateFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.CreateFeedRequest)

Create asset feed request.

### [CreateSavedQueryRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.CreateSavedQueryRequest)

Request to create a saved query.

### [DeleteFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.DeleteFeedRequest)

### [DeleteSavedQueryRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.DeleteSavedQueryRequest)

Request to delete a saved query.

### [EffectiveTagDetails](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.EffectiveTagDetails)

The effective tags and the ancestor resources from which they were inherited.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExportAssetsRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ExportAssetsRequest)

Export asset request.

### [ExportAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ExportAssetsResponse)

The export asset response. This message is returned by the `google.longrunning.Operations.GetOperation][google.longrunning.Operations.GetOperation]` method in the returned `google.longrunning.Operation.response][google.longrunning.Operation.response]` field.

### [Feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.Feed)

An asset feed used to export asset updates to a destinations. An asset feed filter controls what updates are exported. The asset feed must be created within a project, organization, or folder. Supported destinations are:

Pub/Sub topics.

### [FeedOutputConfig](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.FeedOutputConfig)

Output configuration for asset feed destination.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GcsDestination](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.GcsDestination)

A Cloud Storage location.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GcsOutputResult](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.GcsOutputResult)

A Cloud Storage output result.

### [GetFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.GetFeedRequest)

Get asset feed request.

### [GetSavedQueryRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.GetSavedQueryRequest)

Request to get a saved query.

### [IamPolicyAnalysisOutputConfig](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisOutputConfig)

Output configuration for export IAM policy analysis destination.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BigQueryDestination](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisOutputConfig.BigQueryDestination)

A BigQuery destination.

### [PartitionKey](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisOutputConfig.BigQueryDestination.PartitionKey)

This enum determines the partition key column for the bigquery tables. Partitioning can improve query performance and reduce query cost by filtering partitions. Refer to <https://cloud.google.com/bigquery/docs/partitioned-tables> for details.

### [GcsDestination](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisOutputConfig.GcsDestination)

A Cloud Storage location.

### [IamPolicyAnalysisQuery](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisQuery)

IAM policy analysis query message.

### [AccessSelector](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisQuery.AccessSelector)

Specifies roles and/or permissions to analyze, to determine both the identities possessing them and the resources they control. If multiple values are specified, results will include roles or permissions matching any of them. The total number of roles and permissions should be equal or less than 10.

### [ConditionContext](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisQuery.ConditionContext)

The IAM conditions context.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [IdentitySelector](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisQuery.IdentitySelector)

Specifies an identity for which to determine resource access, based on roles assigned either directly to them or to the groups they belong to, directly or indirectly.

### [Options](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisQuery.Options)

Contains query options.

### [ResourceSelector](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisQuery.ResourceSelector)

Specifies the resource to analyze for access policies, which may be set directly on the resource, or on ancestors such as organizations, folders or projects.

### [IamPolicyAnalysisResult](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisResult)

IAM Policy analysis result, consisting of one IAM policy binding and derived access control lists.

### [Access](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisResult.Access)

An IAM role or permission under analysis.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AccessControlList](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisResult.AccessControlList)

An access control list, derived from the above IAM policy binding, which contains a set of resources and accesses. May include one item from each set to compose an access control entry.

NOTICE that there could be multiple access control lists for one IAM policy binding. The access control lists are created based on resource and access combinations.

For example, assume we have the following cases in one IAM policy binding:

  * Permission P1 and P2 apply to resource R1 and R2;
  * Permission P3 applies to resource R2 and R3;



This will result in the following access control lists:

  * AccessControlList 1: [R1, R2], [P1, P2]
  * AccessControlList 2: [R2, R3], [P3]



### [Edge](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisResult.Edge)

A directional edge.

### [Identity](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisResult.Identity)

An identity under analysis.

### [IdentityList](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisResult.IdentityList)

The identities and group edges.

### [Resource](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisResult.Resource)

A Google Cloud resource under analysis.

### [IamPolicyAnalysisState](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicyAnalysisState)

Represents the detailed state of an entity under analysis, such as a resource, an identity or an access.

### [IamPolicySearchResult](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicySearchResult)

A result of IAM Policy search, containing information of an IAM policy.

### [Explanation](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicySearchResult.Explanation)

Explanation about the IAM policy search result.

### [MatchedPermissionsEntry](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicySearchResult.Explanation.MatchedPermissionsEntry)

The abstract base class for a message.

### [Permissions](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.IamPolicySearchResult.Explanation.Permissions)

IAM permissions

### [ListAssetsRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListAssetsRequest)

ListAssets request.

### [ListAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListAssetsResponse)

ListAssets response.

### [ListFeedsRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListFeedsRequest)

List asset feeds request.

### [ListFeedsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListFeedsResponse)

### [ListSavedQueriesRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListSavedQueriesRequest)

Request to list saved queries.

### [ListSavedQueriesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ListSavedQueriesResponse)

Response of listing saved queries.

### [MoveAnalysis](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.MoveAnalysis)

A message to group the analysis information.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [MoveAnalysisResult](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.MoveAnalysisResult)

An analysis result including blockers and warnings.

### [MoveImpact](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.MoveImpact)

A message to group impacts of moving the target resource.

### [OutputConfig](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.OutputConfig)

Output configuration for export assets destination.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [OutputResult](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.OutputResult)

Output result of export assets.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PartitionSpec](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.PartitionSpec)

Specifications of BigQuery partitioned table as export destination.

### [PartitionKey](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.PartitionSpec.PartitionKey)

This enum is used to determine the partition key column when exporting assets to BigQuery partitioned table(s). Note that, if the partition key is a timestamp column, the actual partition is based on its date value (expressed in UTC. see details in <https://cloud.google.com/bigquery/docs/partitioned-tables#date_timestamp_partitioned_tables>).

### [PubsubDestination](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.PubsubDestination)

A Pub/Sub destination.

### [QueryAssetsOutputConfig](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.QueryAssetsOutputConfig)

Output configuration query assets.

### [BigQueryDestination](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.QueryAssetsOutputConfig.BigQueryDestination)

BigQuery destination.

### [QueryAssetsRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.QueryAssetsRequest)

QueryAssets request.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [QueryAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.QueryAssetsResponse)

QueryAssets response.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [QueryResult](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.QueryResult)

Execution results of the query.

The result is formatted as rows represented by BigQuery compatible [schema]. When pagination is necessary, it will contains the page token to retrieve the results of following pages.

### [RelatedAsset](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.RelatedAsset)

An asset identifier in Google Cloud which contains its name, type and ancestors. An asset can be any resource in the Google Cloud `resource hierarchy <https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy>`**, a resource outside the Google Cloud resource hierarchy (such as Google Kubernetes Engine clusters and objects), or a policy (e.g. IAM policy). See`Supported asset types <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`** for more information.

### [RelatedAssets](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.RelatedAssets)

DEPRECATED. This message only presents for the purpose of backward-compatibility. The server will never populate this message in responses. The detailed related assets with the `relationship_type`.

### [RelatedResource](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.RelatedResource)

The detailed related resource.

### [RelatedResources](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.RelatedResources)

The related resources of the primary resource.

### [RelationshipAttributes](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.RelationshipAttributes)

DEPRECATED. This message only presents for the purpose of backward-compatibility. The server will never populate this message in responses. The relationship attributes which include `type`, `source_resource_type`, `target_resource_type` and `action`.

### [Resource](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.Resource)

A representation of a Google Cloud resource.

### [ResourceOwners](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ResourceOwners)

The resource owners information.

### [ResourceSearchResult](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ResourceSearchResult)

A result of Resource Search, containing information of a cloud resource.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ResourceSearchResult.LabelsEntry)

The abstract base class for a message.

### [RelationshipsEntry](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ResourceSearchResult.RelationshipsEntry)

The abstract base class for a message.

### [SccSecurityMarksEntry](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.ResourceSearchResult.SccSecurityMarksEntry)

The abstract base class for a message.

### [SavedQuery](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SavedQuery)

A saved query which can be shared with others or used later.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SavedQuery.LabelsEntry)

The abstract base class for a message.

### [QueryContent](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SavedQuery.QueryContent)

The query content.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [SearchAllIamPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllIamPoliciesRequest)

Search all IAM policies request.

### [SearchAllIamPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllIamPoliciesResponse)

Search all IAM policies response.

### [SearchAllResourcesRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllResourcesRequest)

Search all resources request.

### [SearchAllResourcesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.SearchAllResourcesResponse)

Search all resources response.

### [TableFieldSchema](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.TableFieldSchema)

A field in TableSchema.

### [TableSchema](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.TableSchema)

BigQuery Compatible table schema.

### [Tag](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.Tag)

The key and value for a `tag <https://cloud.google.com/resource-manager/docs/tags/tags-overview>`__.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [TemporalAsset](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.TemporalAsset)

An asset in Google Cloud and its temporal metadata, including the time window when it was observed and its status during that window.

### [PriorAssetState](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.TemporalAsset.PriorAssetState)

State of prior asset.

### [TimeWindow](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.TimeWindow)

A time window specified by its `start_time` and `end_time`.

### [UpdateFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.UpdateFeedRequest)

Update asset feed request.

### [UpdateSavedQueryRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.UpdateSavedQueryRequest)

Request to update a saved query.

### [VersionedResource](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.types.VersionedResource)

Resource representation as defined by the corresponding service providing the resource for a given API version.

### [AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceAsyncClient)

Asset service definition.

### [AssetServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.AssetServiceClient)

Asset service definition.

### [SearchAllIamPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllIamPoliciesAsyncPager)

A pager for iterating through `search_all_iam_policies` requests.

This class thinly wraps an initial [SearchAllIamPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.SearchAllIamPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `results` field.

If there are more pages, the `__aiter__` method will make additional `SearchAllIamPolicies` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchAllIamPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.SearchAllIamPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAllIamPoliciesPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllIamPoliciesPager)

A pager for iterating through `search_all_iam_policies` requests.

This class thinly wraps an initial [SearchAllIamPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.SearchAllIamPoliciesResponse) object, and provides an `__iter__` method to iterate through its `results` field.

If there are more pages, the `__iter__` method will make additional `SearchAllIamPolicies` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchAllIamPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.SearchAllIamPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAllResourcesAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllResourcesAsyncPager)

A pager for iterating through `search_all_resources` requests.

This class thinly wraps an initial [SearchAllResourcesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.SearchAllResourcesResponse) object, and provides an `__aiter__` method to iterate through its `results` field.

If there are more pages, the `__aiter__` method will make additional `SearchAllResources` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchAllResourcesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.SearchAllResourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAllResourcesPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.pagers.SearchAllResourcesPager)

A pager for iterating through `search_all_resources` requests.

This class thinly wraps an initial [SearchAllResourcesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.SearchAllResourcesResponse) object, and provides an `__iter__` method to iterate through its `results` field.

If there are more pages, the `__iter__` method will make additional `SearchAllResources` requests and continue to iterate through the `results` field on the corresponding responses.

All the usual [SearchAllResourcesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.SearchAllResourcesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [IamPolicySearchResult](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.IamPolicySearchResult)

The result for an IAM policy search.

### [Explanation](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.IamPolicySearchResult.Explanation)

Explanation about the IAM policy search result.

### [MatchedPermissionsEntry](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.IamPolicySearchResult.Explanation.MatchedPermissionsEntry)

The abstract base class for a message.

### [Permissions](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.Permissions)

IAM permissions.

### [SearchAllIamPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.SearchAllIamPoliciesRequest)

Search all IAM policies request.

### [SearchAllIamPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.SearchAllIamPoliciesResponse)

Search all IAM policies response.

### [SearchAllResourcesRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.SearchAllResourcesRequest)

Search all resources request.

### [SearchAllResourcesResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.SearchAllResourcesResponse)

Search all resources response.

### [StandardResourceMetadata](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.StandardResourceMetadata)

The standard metadata of a cloud resource.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.types.StandardResourceMetadata.LabelsEntry)

The abstract base class for a message.

### [AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceAsyncClient)

Asset service definition.

### [AssetServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.services.asset_service.AssetServiceClient)

Asset service definition.

### [Asset](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.Asset)

An asset in Google Cloud. An asset can be any resource in the Google Cloud `resource hierarchy <https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy>`**, a resource outside the Google Cloud resource hierarchy (such as Google Kubernetes Engine clusters and objects), or a policy (e.g. IAM policy). See`Supported asset types <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`** for more information.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BatchGetAssetsHistoryResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.BatchGetAssetsHistoryResponse)

Batch get assets history response.

### [ContentType](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.ContentType)

Asset content type.

### [CreateFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.CreateFeedRequest)

Create asset feed request.

### [DeleteFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.DeleteFeedRequest)

### [ExportAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.ExportAssetsResponse)

The export asset response. This message is returned by the `google.longrunning.Operations.GetOperation][google.longrunning.Operations.GetOperation]` method in the returned `google.longrunning.Operation.response][google.longrunning.Operation.response]` field.

### [Feed](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.Feed)

An asset feed used to export asset updates to a destinations. An asset feed filter controls what updates are exported. The asset feed must be created within a project, organization, or folder. Supported destinations are:

Cloud Pub/Sub topics.

### [FeedOutputConfig](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.FeedOutputConfig)

Output configuration for asset feed destination.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GcsDestination](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.GcsDestination)

A Cloud Storage location.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [GetFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.GetFeedRequest)

Get asset feed request.

### [ListFeedsRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.ListFeedsRequest)

List asset feeds request.

### [ListFeedsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.ListFeedsResponse)

### [OutputConfig](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.OutputConfig)

Output configuration for export assets destination.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PubsubDestination](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.PubsubDestination)

A Pub/Sub destination.

### [Resource](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.Resource)

A representation of a Google Cloud resource.

### [TemporalAsset](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.TemporalAsset)

An asset in Google Cloud and its temporal metadata, including the time window when it was observed and its status during that window.

### [TimeWindow](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.TimeWindow)

A time window specified by its `start_time` and `end_time`.

### [UpdateFeedRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p2beta1.types.UpdateFeedRequest)

Update asset feed request.

### [AssetServiceAsyncClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceAsyncClient)

Asset service definition.

### [AssetServiceClient](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.AssetServiceClient)

Asset service definition.

### [ListAssetsAsyncPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.pagers.ListAssetsAsyncPager)

A pager for iterating through `list_assets` requests.

This class thinly wraps an initial [ListAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.types.ListAssetsResponse) object, and provides an `__aiter__` method to iterate through its `assets` field.

If there are more pages, the `__aiter__` method will make additional `ListAssets` requests and continue to iterate through the `assets` field on the corresponding responses.

All the usual [ListAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.types.ListAssetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAssetsPager](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.pagers.ListAssetsPager)

A pager for iterating through `list_assets` requests.

This class thinly wraps an initial [ListAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.types.ListAssetsResponse) object, and provides an `__iter__` method to iterate through its `assets` field.

If there are more pages, the `__iter__` method will make additional `ListAssets` requests and continue to iterate through the `assets` field on the corresponding responses.

All the usual [ListAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.types.ListAssetsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [Asset](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.types.Asset)

An asset in Google Cloud. An asset can be any resource in the Google Cloud `resource hierarchy <https://cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy>`**, a resource outside the Google Cloud resource hierarchy (such as Google Kubernetes Engine clusters and objects), or a policy (e.g. IAM policy). See`Supported asset types <https://cloud.google.com/asset-inventory/docs/supported-asset-types>`** for more information.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ContentType](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.types.ContentType)

Asset content type.

### [ListAssetsRequest](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.types.ListAssetsRequest)

ListAssets request.

### [ListAssetsResponse](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.types.ListAssetsResponse)

ListAssets response.

### [Resource](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.types.Resource)

A representation of a Google Cloud resource.

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1.services.asset_service.pagers)

API documentation for `asset_v1.services.asset_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p1beta1.services.asset_service.pagers)

API documentation for `asset_v1p1beta1.services.asset_service.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/cloudasset/latest/google.cloud.asset_v1p5beta1.services.asset_service.pagers)

API documentation for `asset_v1p5beta1.services.asset_service.pagers` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
