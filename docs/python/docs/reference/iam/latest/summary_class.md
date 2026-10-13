---
url: https://docs.cloud.google.com/python/docs/reference/iam/latest/summary_class/
title: Package Classes (2.26.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:45:24.914536+00:00
---

# Package Classes (2.26.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/iam/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (2.26.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.26.0 (latest)  2.25.0  2.24.1  2.23.0  2.22.0  2.21.0  2.20.0  2.19.1  2.18.3  2.17.0  2.16.1  2.15.2  2.14.3  2.13.0  2.12.1  2.11.2  2.10.0  2.9.0  2.8.2  2.7.0  2.6.2  2.5.1  2.4.0  2.3.2  2.2.0  2.1.0  2.0.0  1.0.3  0.3.2  0.2.0 

Summary of entries of Classes for iam.

## Classes 

### [IAMAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMAsyncClient)

Creates and manages Identity and Access Management (IAM) resources.

You can use this service to work with all of the following resources:

  * **Service accounts** , which identify an application or a virtual machine (VM) instance rather than a person
  * **Service account keys** , which service accounts use to authenticate with Google APIs
  * **IAM policies for service accounts** , which specify the roles that a principal has for the service account
  * **IAM custom roles** , which help you limit the number of permissions that you grant to principals



In addition, you can use this service to complete the following tasks, among others:

  * Test whether a service account can use specific permissions
  * Check which roles you can grant for a specific resource
  * Lint, or validate, condition expressions in an IAM policy



When you read data from the IAM API, each read is eventually consistent. In other words, if you write data with the IAM API, then immediately read that data, the read operation might return an older version of the data. To deal with this behavior, your application can retry the request with truncated exponential backoff.

In contrast, writing data to the IAM API is sequentially consistent. In other words, write operations are always processed in the order in which they were received.

### [IAMClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient)

Creates and manages Identity and Access Management (IAM) resources.

You can use this service to work with all of the following resources:

  * **Service accounts** , which identify an application or a virtual machine (VM) instance rather than a person
  * **Service account keys** , which service accounts use to authenticate with Google APIs
  * **IAM policies for service accounts** , which specify the roles that a principal has for the service account
  * **IAM custom roles** , which help you limit the number of permissions that you grant to principals



In addition, you can use this service to complete the following tasks, among others:

  * Test whether a service account can use specific permissions
  * Check which roles you can grant for a specific resource
  * Lint, or validate, condition expressions in an IAM policy



When you read data from the IAM API, each read is eventually consistent. In other words, if you write data with the IAM API, then immediately read that data, the read operation might return an older version of the data. To deal with this behavior, your application can retry the request with truncated exponential backoff.

In contrast, writing data to the IAM API is sequentially consistent. In other words, write operations are always processed in the order in which they were received.

### [ListRolesAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.ListRolesAsyncPager)

A pager for iterating through `list_roles` requests.

This class thinly wraps an initial [ListRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListRolesResponse) object, and provides an `__aiter__` method to iterate through its `roles` field.

If there are more pages, the `__aiter__` method will make additional `ListRoles` requests and continue to iterate through the `roles` field on the corresponding responses.

All the usual [ListRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListRolesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListRolesPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.ListRolesPager)

A pager for iterating through `list_roles` requests.

This class thinly wraps an initial [ListRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListRolesResponse) object, and provides an `__iter__` method to iterate through its `roles` field.

If there are more pages, the `__iter__` method will make additional `ListRoles` requests and continue to iterate through the `roles` field on the corresponding responses.

All the usual [ListRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListRolesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListServiceAccountsAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.ListServiceAccountsAsyncPager)

A pager for iterating through `list_service_accounts` requests.

This class thinly wraps an initial [ListServiceAccountsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountsResponse) object, and provides an `__aiter__` method to iterate through its `accounts` field.

If there are more pages, the `__aiter__` method will make additional `ListServiceAccounts` requests and continue to iterate through the `accounts` field on the corresponding responses.

All the usual [ListServiceAccountsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListServiceAccountsPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.ListServiceAccountsPager)

A pager for iterating through `list_service_accounts` requests.

This class thinly wraps an initial [ListServiceAccountsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountsResponse) object, and provides an `__iter__` method to iterate through its `accounts` field.

If there are more pages, the `__iter__` method will make additional `ListServiceAccounts` requests and continue to iterate through the `accounts` field on the corresponding responses.

All the usual [ListServiceAccountsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [QueryGrantableRolesAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.QueryGrantableRolesAsyncPager)

A pager for iterating through `query_grantable_roles` requests.

This class thinly wraps an initial [QueryGrantableRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryGrantableRolesResponse) object, and provides an `__aiter__` method to iterate through its `roles` field.

If there are more pages, the `__aiter__` method will make additional `QueryGrantableRoles` requests and continue to iterate through the `roles` field on the corresponding responses.

All the usual [QueryGrantableRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryGrantableRolesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [QueryGrantableRolesPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.QueryGrantableRolesPager)

A pager for iterating through `query_grantable_roles` requests.

This class thinly wraps an initial [QueryGrantableRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryGrantableRolesResponse) object, and provides an `__iter__` method to iterate through its `roles` field.

If there are more pages, the `__iter__` method will make additional `QueryGrantableRoles` requests and continue to iterate through the `roles` field on the corresponding responses.

All the usual [QueryGrantableRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryGrantableRolesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [QueryTestablePermissionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.QueryTestablePermissionsAsyncPager)

A pager for iterating through `query_testable_permissions` requests.

This class thinly wraps an initial [QueryTestablePermissionsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryTestablePermissionsResponse) object, and provides an `__aiter__` method to iterate through its `permissions` field.

If there are more pages, the `__aiter__` method will make additional `QueryTestablePermissions` requests and continue to iterate through the `permissions` field on the corresponding responses.

All the usual [QueryTestablePermissionsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryTestablePermissionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [QueryTestablePermissionsPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers.QueryTestablePermissionsPager)

A pager for iterating through `query_testable_permissions` requests.

This class thinly wraps an initial [QueryTestablePermissionsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryTestablePermissionsResponse) object, and provides an `__iter__` method to iterate through its `permissions` field.

If there are more pages, the `__iter__` method will make additional `QueryTestablePermissions` requests and continue to iterate through the `permissions` field on the corresponding responses.

All the usual [QueryTestablePermissionsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryTestablePermissionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AuditData](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.AuditData)

Audit log information specific to Cloud IAM admin APIs. This message is serialized as an `Any` type in the `ServiceData` message of an `AuditLog` message.

### [PermissionDelta](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.AuditData.PermissionDelta)

A PermissionDelta message to record the added_permissions and removed_permissions inside a role.

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

### [Level](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.LintResult.Level)

Possible Level values of a validation unit corresponding to its domain of discourse.

### [Severity](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.LintResult.Severity)

Possible Severity values of an issued result.
    
    
        - Unsatisfiable condition: Expired timestamp in date/time
          condition.
        - Ineffective condition: Condition on a <principal, role>
          pair which is granted unconditionally in another binding
          of the same policy.
    NOTICE (3):
        Reserved for the issues that are not severe as
        `ERROR`/`WARNING`, but need special handling. For
        instance, messages about skipped validation units are issued
        as `NOTICE`.
    INFO (4):
        Any informative statement which is not severe enough to
        raise `ERROR`/`WARNING`/`NOTICE`, like auto-correction
        recommendations on the input content. Note that current
        version of the linter does not utilize `INFO`.
    DEPRECATED (5):
        Deprecated severity level.
    

### [ListRolesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListRolesRequest)

The request to get all roles defined under a resource.

### [ListRolesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListRolesResponse)

The response containing the roles defined under a resource.

### [ListServiceAccountKeysRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountKeysRequest)

The service account keys list request.

### [KeyType](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.ListServiceAccountKeysRequest.KeyType)

`KeyType` filters to selectively retrieve certain varieties of keys.

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

### [CustomRolesSupportLevel](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Permission.CustomRolesSupportLevel)

The state of the permission with regards to custom roles.

### [PermissionLaunchStage](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Permission.PermissionLaunchStage)

A stage representing a permission's lifecycle phase.

### [QueryAuditableServicesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryAuditableServicesRequest)

A request to get the list of auditable services for a resource.

### [QueryAuditableServicesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryAuditableServicesResponse)

A response containing a list of auditable services for a resource.

### [AuditableService](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.QueryAuditableServicesResponse.AuditableService)

Contains information about an auditable service.

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

### [RoleLaunchStage](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.types.Role.RoleLaunchStage)

A stage representing a role's lifecycle phase.

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

### [IAMCredentialsAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsAsyncClient)

A service account is a special type of Google account that belongs to your application or a virtual machine (VM), instead of to an individual end user. Your application assumes the identity of the service account to call Google APIs, so that the users aren't directly involved.

Service account credentials are used to temporarily assume the identity of the service account. Supported credential types include OAuth 2.0 access tokens, OpenID Connect ID tokens, self-signed JSON Web Tokens (JWTs), and more.

### [IAMCredentialsClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.services.iam_credentials.IAMCredentialsClient)

A service account is a special type of Google account that belongs to your application or a virtual machine (VM), instead of to an individual end user. Your application assumes the identity of the service account to call Google APIs, so that the users aren't directly involved.

Service account credentials are used to temporarily assume the identity of the service account. Supported credential types include OAuth 2.0 access tokens, OpenID Connect ID tokens, self-signed JSON Web Tokens (JWTs), and more.

### [GenerateAccessTokenRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.types.GenerateAccessTokenRequest)

### [GenerateAccessTokenResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.types.GenerateAccessTokenResponse)

### [GenerateIdTokenRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.types.GenerateIdTokenRequest)

### [GenerateIdTokenResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.types.GenerateIdTokenResponse)

### [SignBlobRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.types.SignBlobRequest)

### [SignBlobResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.types.SignBlobResponse)

### [SignJwtRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.types.SignJwtRequest)

### [SignJwtResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_credentials_v1.types.SignJwtResponse)

### [PoliciesAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesAsyncClient)

An interface for managing Identity and Access Management (IAM) policies.

### [PoliciesClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.PoliciesClient)

An interface for managing Identity and Access Management (IAM) policies.

### [ListPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.pagers.ListPoliciesAsyncPager)

A pager for iterating through `list_policies` requests.

This class thinly wraps an initial [ListPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.ListPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `policies` field.

If there are more pages, the `__aiter__` method will make additional `ListPolicies` requests and continue to iterate through the `policies` field on the corresponding responses.

All the usual [ListPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.ListPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPoliciesPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.pagers.ListPoliciesPager)

A pager for iterating through `list_policies` requests.

This class thinly wraps an initial [ListPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.ListPoliciesResponse) object, and provides an `__iter__` method to iterate through its `policies` field.

If there are more pages, the `__iter__` method will make additional `ListPolicies` requests and continue to iterate through the `policies` field on the corresponding responses.

All the usual [ListPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.ListPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [CreatePolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.CreatePolicyRequest)

Request message for `CreatePolicy`.

### [DeletePolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.DeletePolicyRequest)

Request message for `DeletePolicy`.

### [DenyRule](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.DenyRule)

A deny rule in an IAM deny policy.

### [GetPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.GetPolicyRequest)

Request message for `GetPolicy`.

### [ListPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.ListPoliciesRequest)

Request message for `ListPolicies`.

### [ListPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.ListPoliciesResponse)

Response message for `ListPolicies`.

### [Policy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.Policy)

Data for an IAM policy.

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.Policy.AnnotationsEntry)

The abstract base class for a message.

### [PolicyOperationMetadata](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.PolicyOperationMetadata)

Metadata for long-running `Policy` operations.

### [PolicyRule](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.PolicyRule)

A single rule in a `Policy`.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [UpdatePolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.types.UpdatePolicyRequest)

Request message for `UpdatePolicy`.

### [PoliciesAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesAsyncClient)

An interface for managing Identity and Access Management (IAM) policies.

### [PoliciesClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.PoliciesClient)

An interface for managing Identity and Access Management (IAM) policies.

### [ListPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.pagers.ListPoliciesAsyncPager)

A pager for iterating through `list_policies` requests.

This class thinly wraps an initial [ListPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.ListPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `policies` field.

If there are more pages, the `__aiter__` method will make additional `ListPolicies` requests and continue to iterate through the `policies` field on the corresponding responses.

All the usual [ListPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.ListPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPoliciesPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.pagers.ListPoliciesPager)

A pager for iterating through `list_policies` requests.

This class thinly wraps an initial [ListPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.ListPoliciesResponse) object, and provides an `__iter__` method to iterate through its `policies` field.

If there are more pages, the `__iter__` method will make additional `ListPolicies` requests and continue to iterate through the `policies` field on the corresponding responses.

All the usual [ListPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.ListPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [CreatePolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.CreatePolicyRequest)

Request message for `CreatePolicy`.

### [DeletePolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.DeletePolicyRequest)

Request message for `DeletePolicy`.

### [DenyRule](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.DenyRule)

A deny rule in an IAM deny policy.

### [GetPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.GetPolicyRequest)

Request message for `GetPolicy`.

### [ListPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.ListPoliciesRequest)

Request message for `ListPolicies`.

### [ListPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.ListPoliciesResponse)

Response message for `ListPolicies`.

### [Policy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.Policy)

Data for an IAM policy.

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.Policy.AnnotationsEntry)

The abstract base class for a message.

### [PolicyOperationMetadata](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.PolicyOperationMetadata)

Metadata for long-running `Policy` operations.

### [PolicyRule](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.PolicyRule)

A single rule in a `Policy`.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [UpdatePolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.types.UpdatePolicyRequest)

Request message for `UpdatePolicy`.

### [AccessPoliciesAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesAsyncClient)

Manages Identity and Access Management (IAM) access policies.

### [AccessPoliciesClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.AccessPoliciesClient)

Manages Identity and Access Management (IAM) access policies.

### [ListAccessPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.pagers.ListAccessPoliciesAsyncPager)

A pager for iterating through `list_access_policies` requests.

This class thinly wraps an initial [ListAccessPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.ListAccessPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `access_policies` field.

If there are more pages, the `__aiter__` method will make additional `ListAccessPolicies` requests and continue to iterate through the `access_policies` field on the corresponding responses.

All the usual [ListAccessPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.ListAccessPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAccessPoliciesPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.pagers.ListAccessPoliciesPager)

A pager for iterating through `list_access_policies` requests.

This class thinly wraps an initial [ListAccessPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.ListAccessPoliciesResponse) object, and provides an `__iter__` method to iterate through its `access_policies` field.

If there are more pages, the `__iter__` method will make additional `ListAccessPolicies` requests and continue to iterate through the `access_policies` field on the corresponding responses.

All the usual [ListAccessPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.ListAccessPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAccessPolicyBindingsAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.pagers.SearchAccessPolicyBindingsAsyncPager)

A pager for iterating through `search_access_policy_bindings` requests.

This class thinly wraps an initial [SearchAccessPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.SearchAccessPolicyBindingsResponse) object, and provides an `__aiter__` method to iterate through its `policy_bindings` field.

If there are more pages, the `__aiter__` method will make additional `SearchAccessPolicyBindings` requests and continue to iterate through the `policy_bindings` field on the corresponding responses.

All the usual [SearchAccessPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.SearchAccessPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAccessPolicyBindingsPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.pagers.SearchAccessPolicyBindingsPager)

A pager for iterating through `search_access_policy_bindings` requests.

This class thinly wraps an initial [SearchAccessPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.SearchAccessPolicyBindingsResponse) object, and provides an `__iter__` method to iterate through its `policy_bindings` field.

If there are more pages, the `__iter__` method will make additional `SearchAccessPolicyBindings` requests and continue to iterate through the `policy_bindings` field on the corresponding responses.

All the usual [SearchAccessPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.SearchAccessPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [PolicyBindingsAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsAsyncClient)

An interface for managing Identity and Access Management (IAM) policy bindings.

### [PolicyBindingsClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.PolicyBindingsClient)

An interface for managing Identity and Access Management (IAM) policy bindings.

### [ListPolicyBindingsAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.pagers.ListPolicyBindingsAsyncPager)

A pager for iterating through `list_policy_bindings` requests.

This class thinly wraps an initial [ListPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.ListPolicyBindingsResponse) object, and provides an `__aiter__` method to iterate through its `policy_bindings` field.

If there are more pages, the `__aiter__` method will make additional `ListPolicyBindings` requests and continue to iterate through the `policy_bindings` field on the corresponding responses.

All the usual [ListPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.ListPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPolicyBindingsPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.pagers.ListPolicyBindingsPager)

A pager for iterating through `list_policy_bindings` requests.

This class thinly wraps an initial [ListPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.ListPolicyBindingsResponse) object, and provides an `__iter__` method to iterate through its `policy_bindings` field.

If there are more pages, the `__iter__` method will make additional `ListPolicyBindings` requests and continue to iterate through the `policy_bindings` field on the corresponding responses.

All the usual [ListPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.ListPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchTargetPolicyBindingsAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.pagers.SearchTargetPolicyBindingsAsyncPager)

A pager for iterating through `search_target_policy_bindings` requests.

This class thinly wraps an initial [SearchTargetPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.SearchTargetPolicyBindingsResponse) object, and provides an `__aiter__` method to iterate through its `policy_bindings` field.

If there are more pages, the `__aiter__` method will make additional `SearchTargetPolicyBindings` requests and continue to iterate through the `policy_bindings` field on the corresponding responses.

All the usual [SearchTargetPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.SearchTargetPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchTargetPolicyBindingsPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.pagers.SearchTargetPolicyBindingsPager)

A pager for iterating through `search_target_policy_bindings` requests.

This class thinly wraps an initial [SearchTargetPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.SearchTargetPolicyBindingsResponse) object, and provides an `__iter__` method to iterate through its `policy_bindings` field.

If there are more pages, the `__iter__` method will make additional `SearchTargetPolicyBindings` requests and continue to iterate through the `policy_bindings` field on the corresponding responses.

All the usual [SearchTargetPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.SearchTargetPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [PrincipalAccessBoundaryPoliciesAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient)

Manages Identity and Access Management (IAM) principal access boundary policies.

### [PrincipalAccessBoundaryPoliciesClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient)

Manages Identity and Access Management (IAM) principal access boundary policies.

### [ListPrincipalAccessBoundaryPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesAsyncPager)

A pager for iterating through `list_principal_access_boundary_policies` requests.

This class thinly wraps an initial [ListPrincipalAccessBoundaryPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.ListPrincipalAccessBoundaryPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `principal_access_boundary_policies` field.

If there are more pages, the `__aiter__` method will make additional `ListPrincipalAccessBoundaryPolicies` requests and continue to iterate through the `principal_access_boundary_policies` field on the corresponding responses.

All the usual [ListPrincipalAccessBoundaryPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.ListPrincipalAccessBoundaryPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPrincipalAccessBoundaryPoliciesPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesPager)

A pager for iterating through `list_principal_access_boundary_policies` requests.

This class thinly wraps an initial [ListPrincipalAccessBoundaryPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.ListPrincipalAccessBoundaryPoliciesResponse) object, and provides an `__iter__` method to iterate through its `principal_access_boundary_policies` field.

If there are more pages, the `__iter__` method will make additional `ListPrincipalAccessBoundaryPolicies` requests and continue to iterate through the `principal_access_boundary_policies` field on the corresponding responses.

All the usual [ListPrincipalAccessBoundaryPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.ListPrincipalAccessBoundaryPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager)

A pager for iterating through `search_principal_access_boundary_policy_bindings` requests.

This class thinly wraps an initial [SearchPrincipalAccessBoundaryPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.SearchPrincipalAccessBoundaryPolicyBindingsResponse) object, and provides an `__aiter__` method to iterate through its `policy_bindings` field.

If there are more pages, the `__aiter__` method will make additional `SearchPrincipalAccessBoundaryPolicyBindings` requests and continue to iterate through the `policy_bindings` field on the corresponding responses.

All the usual [SearchPrincipalAccessBoundaryPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.SearchPrincipalAccessBoundaryPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchPrincipalAccessBoundaryPolicyBindingsPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsPager)

A pager for iterating through `search_principal_access_boundary_policy_bindings` requests.

This class thinly wraps an initial [SearchPrincipalAccessBoundaryPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.SearchPrincipalAccessBoundaryPolicyBindingsResponse) object, and provides an `__iter__` method to iterate through its `policy_bindings` field.

If there are more pages, the `__iter__` method will make additional `SearchPrincipalAccessBoundaryPolicyBindings` requests and continue to iterate through the `policy_bindings` field on the corresponding responses.

All the usual [SearchPrincipalAccessBoundaryPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.SearchPrincipalAccessBoundaryPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AccessPolicy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.AccessPolicy)

An IAM access policy resource.

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.AccessPolicy.AnnotationsEntry)

The abstract base class for a message.

### [AccessPolicyDetails](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.AccessPolicyDetails)

Access policy details.

### [AccessPolicyRule](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.AccessPolicyRule)

Access Policy Rule that determines the behavior of the policy.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConditionsEntry](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.AccessPolicyRule.ConditionsEntry)

The abstract base class for a message.

### [Effect](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.AccessPolicyRule.Effect)

An effect to describe the access relationship.

### [Operation](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.AccessPolicyRule.Operation)

Attributes that are used to determine whether this rule applies to a request.

### [CreateAccessPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.CreateAccessPolicyRequest)

Request message for CreateAccessPolicy method.

### [CreatePolicyBindingRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.CreatePolicyBindingRequest)

Request message for CreatePolicyBinding method.

### [CreatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.CreatePrincipalAccessBoundaryPolicyRequest)

Request message for CreatePrincipalAccessBoundaryPolicyRequest method.

### [DeleteAccessPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.DeleteAccessPolicyRequest)

Request message for DeleteAccessPolicy method.

### [DeletePolicyBindingRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.DeletePolicyBindingRequest)

Request message for DeletePolicyBinding method.

### [DeletePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.DeletePrincipalAccessBoundaryPolicyRequest)

Request message for DeletePrincipalAccessBoundaryPolicy method.

### [GetAccessPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.GetAccessPolicyRequest)

Request message for GetAccessPolicy method.

### [GetPolicyBindingRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.GetPolicyBindingRequest)

Request message for GetPolicyBinding method.

### [GetPrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.GetPrincipalAccessBoundaryPolicyRequest)

Request message for GetPrincipalAccessBoundaryPolicy method.

### [ListAccessPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.ListAccessPoliciesRequest)

Request message for ListAccessPolicies method.

### [ListAccessPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.ListAccessPoliciesResponse)

Response message for ListAccessPolicies method.

### [ListPolicyBindingsRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.ListPolicyBindingsRequest)

Request message for ListPolicyBindings method.

### [ListPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.ListPolicyBindingsResponse)

Response message for ListPolicyBindings method.

### [ListPrincipalAccessBoundaryPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.ListPrincipalAccessBoundaryPoliciesRequest)

Request message for ListPrincipalAccessBoundaryPolicies method.

### [ListPrincipalAccessBoundaryPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.ListPrincipalAccessBoundaryPoliciesResponse)

Response message for ListPrincipalAccessBoundaryPolicies method.

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.OperationMetadata)

Represents the metadata of the long-running operation.

### [PolicyBinding](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.PolicyBinding)

IAM policy binding resource.

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.PolicyBinding.AnnotationsEntry)

The abstract base class for a message.

### [PolicyKind](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.PolicyBinding.PolicyKind)

The different policy kinds supported in this binding.

### [Target](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.PolicyBinding.Target)

The full resource name of the resource to which the policy will be bound. Immutable once set.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.PrincipalAccessBoundaryPolicy)

An IAM principal access boundary policy resource.

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.PrincipalAccessBoundaryPolicy.AnnotationsEntry)

The abstract base class for a message.

### [PrincipalAccessBoundaryPolicyDetails](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.PrincipalAccessBoundaryPolicyDetails)

Principal access boundary policy details

### [PrincipalAccessBoundaryPolicyRule](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.PrincipalAccessBoundaryPolicyRule)

Principal access boundary policy rule that defines the resource boundary.

### [Effect](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.PrincipalAccessBoundaryPolicyRule.Effect)

An effect to describe the access relationship.

### [SearchAccessPolicyBindingsRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.SearchAccessPolicyBindingsRequest)

Request message for SearchAccessPolicyBindings rpc.

### [SearchAccessPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.SearchAccessPolicyBindingsResponse)

Response message for SearchAccessPolicyBindings rpc.

### [SearchPrincipalAccessBoundaryPolicyBindingsRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.SearchPrincipalAccessBoundaryPolicyBindingsRequest)

Request message for SearchPrincipalAccessBoundaryPolicyBindings rpc.

### [SearchPrincipalAccessBoundaryPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.SearchPrincipalAccessBoundaryPolicyBindingsResponse)

Response message for SearchPrincipalAccessBoundaryPolicyBindings rpc.

### [SearchTargetPolicyBindingsRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.SearchTargetPolicyBindingsRequest)

Request message for SearchTargetPolicyBindings method.

### [SearchTargetPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.SearchTargetPolicyBindingsResponse)

Response message for SearchTargetPolicyBindings method.

### [UpdateAccessPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.UpdateAccessPolicyRequest)

Request message for UpdateAccessPolicy method.

### [UpdatePolicyBindingRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.UpdatePolicyBindingRequest)

Request message for UpdatePolicyBinding method.

### [UpdatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.types.UpdatePrincipalAccessBoundaryPolicyRequest)

Request message for UpdatePrincipalAccessBoundaryPolicy method.

### [AccessPoliciesAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesAsyncClient)

Manages Identity and Access Management (IAM) access policies.

### [AccessPoliciesClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.AccessPoliciesClient)

Manages Identity and Access Management (IAM) access policies.

### [ListAccessPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.pagers.ListAccessPoliciesAsyncPager)

A pager for iterating through `list_access_policies` requests.

This class thinly wraps an initial [ListAccessPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListAccessPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `access_policies` field.

If there are more pages, the `__aiter__` method will make additional `ListAccessPolicies` requests and continue to iterate through the `access_policies` field on the corresponding responses.

All the usual [ListAccessPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListAccessPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListAccessPoliciesPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.pagers.ListAccessPoliciesPager)

A pager for iterating through `list_access_policies` requests.

This class thinly wraps an initial [ListAccessPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListAccessPoliciesResponse) object, and provides an `__iter__` method to iterate through its `access_policies` field.

If there are more pages, the `__iter__` method will make additional `ListAccessPolicies` requests and continue to iterate through the `access_policies` field on the corresponding responses.

All the usual [ListAccessPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListAccessPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAccessPolicyBindingsAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.pagers.SearchAccessPolicyBindingsAsyncPager)

A pager for iterating through `search_access_policy_bindings` requests.

This class thinly wraps an initial [SearchAccessPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchAccessPolicyBindingsResponse) object, and provides an `__aiter__` method to iterate through its `policy_bindings` field.

If there are more pages, the `__aiter__` method will make additional `SearchAccessPolicyBindings` requests and continue to iterate through the `policy_bindings` field on the corresponding responses.

All the usual [SearchAccessPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchAccessPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchAccessPolicyBindingsPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.pagers.SearchAccessPolicyBindingsPager)

A pager for iterating through `search_access_policy_bindings` requests.

This class thinly wraps an initial [SearchAccessPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchAccessPolicyBindingsResponse) object, and provides an `__iter__` method to iterate through its `policy_bindings` field.

If there are more pages, the `__iter__` method will make additional `SearchAccessPolicyBindings` requests and continue to iterate through the `policy_bindings` field on the corresponding responses.

All the usual [SearchAccessPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchAccessPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [PolicyBindingsAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsAsyncClient)

An interface for managing Identity and Access Management (IAM) policy bindings.

### [PolicyBindingsClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.PolicyBindingsClient)

An interface for managing Identity and Access Management (IAM) policy bindings.

### [ListPolicyBindingsAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.pagers.ListPolicyBindingsAsyncPager)

A pager for iterating through `list_policy_bindings` requests.

This class thinly wraps an initial [ListPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListPolicyBindingsResponse) object, and provides an `__aiter__` method to iterate through its `policy_bindings` field.

If there are more pages, the `__aiter__` method will make additional `ListPolicyBindings` requests and continue to iterate through the `policy_bindings` field on the corresponding responses.

All the usual [ListPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPolicyBindingsPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.pagers.ListPolicyBindingsPager)

A pager for iterating through `list_policy_bindings` requests.

This class thinly wraps an initial [ListPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListPolicyBindingsResponse) object, and provides an `__iter__` method to iterate through its `policy_bindings` field.

If there are more pages, the `__iter__` method will make additional `ListPolicyBindings` requests and continue to iterate through the `policy_bindings` field on the corresponding responses.

All the usual [ListPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchTargetPolicyBindingsAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.pagers.SearchTargetPolicyBindingsAsyncPager)

A pager for iterating through `search_target_policy_bindings` requests.

This class thinly wraps an initial [SearchTargetPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchTargetPolicyBindingsResponse) object, and provides an `__aiter__` method to iterate through its `policy_bindings` field.

If there are more pages, the `__aiter__` method will make additional `SearchTargetPolicyBindings` requests and continue to iterate through the `policy_bindings` field on the corresponding responses.

All the usual [SearchTargetPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchTargetPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchTargetPolicyBindingsPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.pagers.SearchTargetPolicyBindingsPager)

A pager for iterating through `search_target_policy_bindings` requests.

This class thinly wraps an initial [SearchTargetPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchTargetPolicyBindingsResponse) object, and provides an `__iter__` method to iterate through its `policy_bindings` field.

If there are more pages, the `__iter__` method will make additional `SearchTargetPolicyBindings` requests and continue to iterate through the `policy_bindings` field on the corresponding responses.

All the usual [SearchTargetPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchTargetPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [PrincipalAccessBoundaryPoliciesAsyncClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesAsyncClient)

Manages Identity and Access Management (IAM) principal access boundary policies.

### [PrincipalAccessBoundaryPoliciesClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.PrincipalAccessBoundaryPoliciesClient)

Manages Identity and Access Management (IAM) principal access boundary policies.

### [ListPrincipalAccessBoundaryPoliciesAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesAsyncPager)

A pager for iterating through `list_principal_access_boundary_policies` requests.

This class thinly wraps an initial [ListPrincipalAccessBoundaryPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListPrincipalAccessBoundaryPoliciesResponse) object, and provides an `__aiter__` method to iterate through its `principal_access_boundary_policies` field.

If there are more pages, the `__aiter__` method will make additional `ListPrincipalAccessBoundaryPolicies` requests and continue to iterate through the `principal_access_boundary_policies` field on the corresponding responses.

All the usual [ListPrincipalAccessBoundaryPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListPrincipalAccessBoundaryPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListPrincipalAccessBoundaryPoliciesPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.ListPrincipalAccessBoundaryPoliciesPager)

A pager for iterating through `list_principal_access_boundary_policies` requests.

This class thinly wraps an initial [ListPrincipalAccessBoundaryPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListPrincipalAccessBoundaryPoliciesResponse) object, and provides an `__iter__` method to iterate through its `principal_access_boundary_policies` field.

If there are more pages, the `__iter__` method will make additional `ListPrincipalAccessBoundaryPolicies` requests and continue to iterate through the `principal_access_boundary_policies` field on the corresponding responses.

All the usual [ListPrincipalAccessBoundaryPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListPrincipalAccessBoundaryPoliciesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsAsyncPager)

A pager for iterating through `search_principal_access_boundary_policy_bindings` requests.

This class thinly wraps an initial [SearchPrincipalAccessBoundaryPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchPrincipalAccessBoundaryPolicyBindingsResponse) object, and provides an `__aiter__` method to iterate through its `policy_bindings` field.

If there are more pages, the `__aiter__` method will make additional `SearchPrincipalAccessBoundaryPolicyBindings` requests and continue to iterate through the `policy_bindings` field on the corresponding responses.

All the usual [SearchPrincipalAccessBoundaryPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchPrincipalAccessBoundaryPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [SearchPrincipalAccessBoundaryPolicyBindingsPager](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers.SearchPrincipalAccessBoundaryPolicyBindingsPager)

A pager for iterating through `search_principal_access_boundary_policy_bindings` requests.

This class thinly wraps an initial [SearchPrincipalAccessBoundaryPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchPrincipalAccessBoundaryPolicyBindingsResponse) object, and provides an `__iter__` method to iterate through its `policy_bindings` field.

If there are more pages, the `__iter__` method will make additional `SearchPrincipalAccessBoundaryPolicyBindings` requests and continue to iterate through the `policy_bindings` field on the corresponding responses.

All the usual [SearchPrincipalAccessBoundaryPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchPrincipalAccessBoundaryPolicyBindingsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AccessPolicy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.AccessPolicy)

An IAM access policy resource.

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.AccessPolicy.AnnotationsEntry)

The abstract base class for a message.

### [AccessPolicyDetails](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.AccessPolicyDetails)

Access policy details.

### [AccessPolicyRule](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.AccessPolicyRule)

Access Policy Rule that determines the behavior of the policy.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ConditionsEntry](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.AccessPolicyRule.ConditionsEntry)

The abstract base class for a message.

### [Effect](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.AccessPolicyRule.Effect)

An effect to describe the access relationship.

### [Operation](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.AccessPolicyRule.Operation)

Attributes that are used to determine whether this rule applies to a request.

### [CreateAccessPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.CreateAccessPolicyRequest)

Request message for CreateAccessPolicy method.

### [CreatePolicyBindingRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.CreatePolicyBindingRequest)

Request message for CreatePolicyBinding method.

### [CreatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.CreatePrincipalAccessBoundaryPolicyRequest)

Request message for CreatePrincipalAccessBoundaryPolicyRequest method.

### [DeleteAccessPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.DeleteAccessPolicyRequest)

Request message for DeleteAccessPolicy method.

### [DeletePolicyBindingRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.DeletePolicyBindingRequest)

Request message for DeletePolicyBinding method.

### [DeletePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.DeletePrincipalAccessBoundaryPolicyRequest)

Request message for DeletePrincipalAccessBoundaryPolicy method.

### [GetAccessPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.GetAccessPolicyRequest)

Request message for GetAccessPolicy method.

### [GetPolicyBindingRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.GetPolicyBindingRequest)

Request message for GetPolicyBinding method.

### [GetPrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.GetPrincipalAccessBoundaryPolicyRequest)

Request message for GetPrincipalAccessBoundaryPolicy method.

### [ListAccessPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListAccessPoliciesRequest)

Request message for ListAccessPolicies method.

### [ListAccessPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListAccessPoliciesResponse)

Response message for ListAccessPolicies method.

### [ListPolicyBindingsRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListPolicyBindingsRequest)

Request message for ListPolicyBindings method.

### [ListPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListPolicyBindingsResponse)

Response message for ListPolicyBindings method.

### [ListPrincipalAccessBoundaryPoliciesRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListPrincipalAccessBoundaryPoliciesRequest)

Request message for ListPrincipalAccessBoundaryPolicies method.

### [ListPrincipalAccessBoundaryPoliciesResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.ListPrincipalAccessBoundaryPoliciesResponse)

Response message for ListPrincipalAccessBoundaryPolicies method.

### [OperationMetadata](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.OperationMetadata)

Represents the metadata of the long-running operation.

### [PolicyBinding](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.PolicyBinding)

IAM policy binding resource.

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.PolicyBinding.AnnotationsEntry)

The abstract base class for a message.

### [PolicyKind](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.PolicyBinding.PolicyKind)

The different policy kinds supported in this binding.

### [Target](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.PolicyBinding.Target)

The full resource name of the resource to which the policy will be bound. Immutable once set.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.PrincipalAccessBoundaryPolicy)

An IAM principal access boundary policy resource.

### [AnnotationsEntry](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.PrincipalAccessBoundaryPolicy.AnnotationsEntry)

The abstract base class for a message.

### [PrincipalAccessBoundaryPolicyDetails](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.PrincipalAccessBoundaryPolicyDetails)

Principal access boundary policy details

### [PrincipalAccessBoundaryPolicyRule](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.PrincipalAccessBoundaryPolicyRule)

Principal access boundary policy rule that defines the resource boundary.

### [Effect](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.PrincipalAccessBoundaryPolicyRule.Effect)

An effect to describe the access relationship.

### [SearchAccessPolicyBindingsRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchAccessPolicyBindingsRequest)

Request message for SearchAccessPolicyBindings rpc.

### [SearchAccessPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchAccessPolicyBindingsResponse)

Response message for SearchAccessPolicyBindings rpc.

### [SearchPrincipalAccessBoundaryPolicyBindingsRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchPrincipalAccessBoundaryPolicyBindingsRequest)

Request message for SearchPrincipalAccessBoundaryPolicyBindings rpc.

### [SearchPrincipalAccessBoundaryPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchPrincipalAccessBoundaryPolicyBindingsResponse)

Response message for SearchPrincipalAccessBoundaryPolicyBindings rpc.

### [SearchTargetPolicyBindingsRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchTargetPolicyBindingsRequest)

Request message for SearchTargetPolicyBindings method.

### [SearchTargetPolicyBindingsResponse](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.SearchTargetPolicyBindingsResponse)

Response message for SearchTargetPolicyBindings method.

### [UpdateAccessPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.UpdateAccessPolicyRequest)

Request message for UpdateAccessPolicy method.

### [UpdatePolicyBindingRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.UpdatePolicyBindingRequest)

Request message for UpdatePolicyBinding method.

### [UpdatePrincipalAccessBoundaryPolicyRequest](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.types.UpdatePrincipalAccessBoundaryPolicyRequest)

Request message for UpdatePrincipalAccessBoundaryPolicy method.

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.pagers)

API documentation for `iam_admin_v1.services.iam.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2.services.policies.pagers)

API documentation for `iam_v2.services.policies.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v2beta.services.policies.pagers)

API documentation for `iam_v2beta.services.policies.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.access_policies.pagers)

API documentation for `iam_v3.services.access_policies.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.policy_bindings.pagers)

API documentation for `iam_v3.services.policy_bindings.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3.services.principal_access_boundary_policies.pagers)

API documentation for `iam_v3.services.principal_access_boundary_policies.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.access_policies.pagers)

API documentation for `iam_v3beta.services.access_policies.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.policy_bindings.pagers)

API documentation for `iam_v3beta.services.policy_bindings.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_v3beta.services.principal_access_boundary_policies.pagers)

API documentation for `iam_v3beta.services.principal_access_boundary_policies.pagers` module.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
