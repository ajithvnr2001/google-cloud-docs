---
url: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types
title: Package types (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:30.855575+00:00
---

# Package types (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package types (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.1  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.3  2.17.0  2.16.1  2.15.2  2.14.3  2.13.0  2.12.1  2.11.2  2.10.0  2.9.0  2.8.2  2.7.0  2.6.2  2.5.1  2.4.0  2.3.2  2.2.0  2.1.0  2.0.0  1.0.3  0.3.2  0.2.0 

API documentation for `iam_admin_v1.types` package.

## Classes 

### [AuditData](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.AuditData)

Audit log information specific to Cloud IAM admin APIs. This message is serialized as an `Any` type in the `ServiceData` message of an `AuditLog` message.

### [CreateRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.CreateRoleRequest)

The request to create a new role.

### [CreateServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.CreateServiceAccountKeyRequest)

The service account key create request.

### [CreateServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.CreateServiceAccountRequest)

The service account create request.

### [DeleteRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DeleteRoleRequest)

The request to delete an existing role.

### [DeleteServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DeleteServiceAccountKeyRequest)

The service account key delete request.

### [DeleteServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DeleteServiceAccountRequest)

The service account delete request.

### [DisableServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DisableServiceAccountKeyRequest)

The service account key disable request.

### [DisableServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.DisableServiceAccountRequest)

The service account disable request.

### [EnableServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.EnableServiceAccountKeyRequest)

The service account key enable request.

### [EnableServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.EnableServiceAccountRequest)

The service account enable request.

### [GetRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.GetRoleRequest)

The request to get the definition of an existing role.

### [GetServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.GetServiceAccountKeyRequest)

The service account key get by id request.

### [GetServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.GetServiceAccountRequest)

The service account get request.

### [LintPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.LintPolicyRequest)

The request to lint a Cloud IAM policy object.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [LintPolicyResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.LintPolicyResponse)

The response of a lint operation. An empty response indicates the operation was able to fully execute and no lint issue was found.

### [LintResult](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.LintResult)

Structured response of a single validation unit.

### [ListRolesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListRolesRequest)

The request to get all roles defined under a resource.

### [ListRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListRolesResponse)

The response containing the roles defined under a resource.

### [ListServiceAccountKeysRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountKeysRequest)

The service account keys list request.

### [ListServiceAccountKeysResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountKeysResponse)

The service account keys list response.

### [ListServiceAccountsRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountsRequest)

The service account list request.

### [ListServiceAccountsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountsResponse)

The service account list response.

### [PatchServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.PatchServiceAccountRequest)

The service account patch request.

You can patch only the `display_name` and `description` fields. You must use the `update_mask` field to specify which of these fields you want to patch.

Only the fields specified in the request are guaranteed to be returned in the response. Other fields may be empty in the response.

### [Permission](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Permission)

A permission which can be included by a role.

### [QueryAuditableServicesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryAuditableServicesRequest)

A request to get the list of auditable services for a resource.

### [QueryAuditableServicesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryAuditableServicesResponse)

A response containing a list of auditable services for a resource.

### [QueryGrantableRolesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryGrantableRolesRequest)

The grantable role query request.

### [QueryGrantableRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryGrantableRolesResponse)

The grantable role query response.

### [QueryTestablePermissionsRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryTestablePermissionsRequest)

A request to get permissions which can be tested on a resource.

### [QueryTestablePermissionsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryTestablePermissionsResponse)

The response containing permissions which can be tested on a resource.

### [Role](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role)

A role in the Identity and Access Management API.

### [RoleView](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.RoleView)

A view for Role objects.

### [ServiceAccount](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccount)

An IAM service account.

A service account is an account for an application or a virtual machine (VM) instance, not a person. You can use a service account to call Google APIs. To learn more, read the `overview of service accounts <https://cloud.google.com/iam/help/service-accounts/overview>`__.

When you create a service account, you specify the project ID that owns the service account, as well as a name that must be unique within the project. IAM uses these values to create an email address that identifies the service account.

### [ServiceAccountKey](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccountKey)

Represents a service account key.

A service account has two sets of key-pairs: user-managed, and system-managed.

User-managed key-pairs can be created and deleted by users. Users are responsible for rotating these keys periodically to ensure security of their service accounts. Users retain the private key of these key-pairs, and Google retains ONLY the public key.

System-managed keys are automatically rotated by Google, and are used for signing for a maximum of two weeks. The rotation process is probabilistic, and usage of the new key will gradually ramp up and down over the key's lifetime.

If you cache the public key set for a service account, we recommend that you update the cache every 15 minutes. User-managed keys can be added and removed at any time, so it is important to update the cache frequently. For Google-managed keys, Google will publish a key at least 6 hours before it is first used for signing and will keep publishing it for at least 6 hours after it was last used for signing.

Public keys for all service accounts are also published at the OAuth2 Service Account API.

### [ServiceAccountKeyAlgorithm](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccountKeyAlgorithm)

Supported key algorithms.

### [ServiceAccountKeyOrigin](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccountKeyOrigin)

Service Account Key Origin.

### [ServiceAccountPrivateKeyType](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccountPrivateKeyType)

Supported private key output formats.

### [ServiceAccountPublicKeyType](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ServiceAccountPublicKeyType)

Supported public key output formats.

### [SignBlobRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.SignBlobRequest)

Deprecated. `Migrate to Service Account Credentials API <https://cloud.google.com/iam/help/credentials/migrate-api>`__.

The service account sign blob request.

### [SignBlobResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.SignBlobResponse)

Deprecated. `Migrate to Service Account Credentials API <https://cloud.google.com/iam/help/credentials/migrate-api>`__.

The service account sign blob response.

### [SignJwtRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.SignJwtRequest)

Deprecated. `Migrate to Service Account Credentials API <https://cloud.google.com/iam/help/credentials/migrate-api>`__.

The service account sign JWT request.

### [SignJwtResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.SignJwtResponse)

Deprecated. `Migrate to Service Account Credentials API <https://cloud.google.com/iam/help/credentials/migrate-api>`__.

The service account sign JWT response.

### [UndeleteRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UndeleteRoleRequest)

The request to undelete an existing role.

### [UndeleteServiceAccountRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UndeleteServiceAccountRequest)

The service account undelete request.

### [UndeleteServiceAccountResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UndeleteServiceAccountResponse)

### [UpdateRoleRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UpdateRoleRequest)

The request to update a role.

### [UploadServiceAccountKeyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.UploadServiceAccountKeyRequest)

The service account key upload request.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
