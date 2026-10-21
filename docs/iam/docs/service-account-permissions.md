---
url: https://docs.cloud.google.com/iam/docs/service-account-permissions/
title: Roles for service account authentication \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:01.267028+00:00
---

# Roles for service account authentication  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/service-account-permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Roles for service account authentication Stay organized with collections  Save and categorize content based on your preferences. 

Principals can use service accounts to authenticate in a few different ways. Each type of authentication requires the principal to have specific Identity and Access Management (IAM) permissions on the service account.

This page describes the roles that you can grant to principals to let them impersonate service accounts or attach service accounts to resources. It also describes the permissions that you need in common scenarios.

To learn about different ways to authenticate with a service account, see [Service account credentials](https://docs.cloud.google.com/iam/docs/service-account-overview#credentials) and [Service account impersonation](https://docs.cloud.google.com/iam/docs/service-account-impersonation).

## Service account roles

This section describes the roles that let principals authenticate with service accounts. To learn how to grant and revoke these roles, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).

### Service Account User role

The Service Account User role (`roles/iam.serviceAccountUser`) lets a principal [attach a service account to a resource](https://docs.cloud.google.com/iam/docs/attach-service-accounts). When the code running on that resource needs to authenticate, it can get credentials for the attached service account.

This role does _not_ allow principals to [create short-lived credentials](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct) for service accounts, or to use the [`--impersonate-service-account` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account) for the Google Cloud CLI. To complete these tasks, you need the Service Account Token Creator role on the service account.

### Service Account Token Creator role

The Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`) lets principals [create short-lived credentials](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct) for a service account.

The Service Account Token Creator role lets you create the following types of short-lived credentials:

  * OAuth 2.0 access tokens, which you can use to authenticate with Google APIs
  * OpenID Connect (OIDC) ID tokens
  * Signed JSON Web Tokens (JWTs) and binary blobs

**Note:** If you only need to create OIDC ID tokens, use the Service Account OpenID Connect Identity Token Creator role instead. This role includes only the permission for creating OIDC ID tokens.

The Service Account Token Creator role also lets principals use the [`--impersonate-service-account` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account) for the gcloud CLI. When you use this flag, the gcloud CLI automatically creates short-lived credentials for the service account.

The role's permissions include the following:

  * `iam.serviceAccounts.getAccessToken`: lets you create OAuth 2.0 access tokens
  * `iam.serviceAccounts.getOpenIdToken`: lets you create OpenID Connect (OIDC) ID tokens
  * `iam.serviceAccounts.implicitDelegation`: lets service accounts get tokens in a [delegation chain](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-delegated)
  * `iam.serviceAccounts.signBlob`: lets you sign binary blobs
  * `iam.serviceAccounts.signJwt`: lets you sign JWTs



### Service Account OpenID Connect Identity Token Creator

The Service Account OpenID Connect Identity Token Creator role (`roles/iam.serviceAccountOpenIdTokenCreator`) lets principals [create short-lived OIDC ID tokens](https://docs.cloud.google.com/iam/docs/create-short-lived-credentials-direct#sa-credentials-oidc). If you only need to create OIDC ID tokens, use this role. If you need to create other types of tokens, use the Service Account Token Creator role instead.

The role includes the `iam.serviceAccounts.getOpenIdToken` permission, which lets you create an OIDC ID token.

### Workload Identity User role

The Workload Identity User role (`roles/iam.workloadIdentityUser`) lets principals impersonate service accounts from GKE workloads.

The role's permissions include the following:

  * `iam.serviceAccounts.getAccessToken`: lets you create OAuth 2.0 access tokens
  * `iam.serviceAccounts.getOpenIdToken`: lets you create OpenID Connect (OIDC) ID tokens



## Service account permissions for common scenarios

Service accounts can be used in many different scenarios, and each of them requires certain permissions. This section describes common scenarios and what permissions are required.

### Attaching service accounts to resources

If you want to start a long-running job that authenticates as a service account, you need to attach a service account to the resource that will run the job.

**Permissions:**

  * Permissions to create the resource
  * `iam.serviceAccounts.actAs`



To find roles that include these permissions, search the [roles list](https://docs.cloud.google.com/iam/docs/understanding-roles) for the permissions.

There are several different Google Cloud resources that can run long-running jobs as service accounts. Some examples of these resources include:

  * Compute Engine VMs 
  * App Engine apps 
  * Cloud Run functions



When you create these resources, you have the option to attach a service account. This service account acts as the resource's identity.

To create a resource and attach a service account, you need permissions to create that resource and permission to attach the service account to resources. Permission to attach service accounts to resources is provided by any role that includes the `iam.serviceAccounts.actAs` permission—for example, the Service Account User role (roles/iam.serviceAccountUser).

**Note:** In the past, some Google Cloud services did not always require users to have the `iam.serviceAccounts.actAs` permission to attach a service account to a resource. This legacy behavior still exists for some organizations. For more information, see [Requiring permission to attach service accounts to resources](https://docs.cloud.google.com/iam/docs/service-accounts-actas).

After you create the resource and attach a service account to it, you can start a long-running job on the resource. The job runs as the service account that is attached to the resource, and uses that service account to authorize requests to Google Cloud APIs.

To learn more about attaching service accounts to resources, see [Attaching a service account to a resource](https://docs.cloud.google.com/iam/docs/attach-service-accounts).

### Impersonating a service account

**Permissions:**

  * `iam.serviceAccounts.getAccessToken`
  * `iam.serviceAccounts.signBlob`
  * `iam.serviceAccounts.signJwt`
  * `iam.serviceAccounts.implicitDelegation`



**Roles:**

  * `roles/iam.serviceAccountTokenCreator` (Service Account Token Creator)



Once granted the required permissions, a user (or another service account) can impersonate the service account in a few common scenarios.

First, the user can authenticate as the service account. For example, they can get short-lived credentials for the service account using the `iam.serviceAccounts.getAccessToken` permission and by calling the [`generateAccessToken()`](https://docs.cloud.google.com/iam/credentials/reference/rest/v1/projects.serviceAccounts/generateAccessToken) method. Or, they can use the [`--impersonate-service-account` flag](https://docs.cloud.google.com/sdk/gcloud/reference#--impersonate-service-account) for gcloud CLI to impersonate the service account. When a user authenticates as a service account, they can issue commands to Google Cloud and can access all resources to which the service account has access.

Second, the user can get artifacts signed by the Google-managed private key of the service account using the `iam.serviceAccounts.signBlob` permission and by calling either the [`signBlob()`](https://docs.cloud.google.com/iam/credentials/reference/rest/v1/projects.serviceAccounts/signBlob) or [`signJwt()`](https://docs.cloud.google.com/iam/credentials/reference/rest/v1/projects.serviceAccounts/signJwt) method. The Google-managed private key is always held in escrow and is never directly exposed. `signBlob()` allows signing of arbitrary payloads (such as Cloud Storage-signed URLs), while `signJwt()` only allows signing well-formed JWTs.

Finally, the user can impersonate the service account without ever retrieving a credential for the service account. This is an advanced use case, and is only supported for programmatic access using the [`generateAccessToken()`](https://docs.cloud.google.com/iam/credentials/reference/rest/v1/projects.serviceAccounts/generateAccessToken) method. In scenarios with at least 3 service accounts, namely _A_ , _B_ , and _C_ : service account _A_ can get an access token for service account _C_ if service account _A_ is granted the `iam.serviceAccounts.implicitDelegation` permission on _B_ , and _B_ is granted the `iam.serviceAccounts.getAccessToken` permission on _C_.

### Generating OpenID Connect (OIDC) ID tokens

**Permissions:**

  * `iam.serviceAccounts.getOpenIdToken`



**Roles:**

  * `roles/iam.serviceAccountOpenIdTokenCreator` (Service Account OpenID Connect Identity Token Creator)



A user (or service) can generate an OpenID Connect (OIDC)-compatible JWT token signed by the Google OIDC Provider (accounts.google.com) that represents the identity of the service account using the `iam.serviceAccounts.getOpenIdToken` permission.

These tokens are not directly accepted by most Google APIs without your organization deploying additional identity federation to grant access to Google.

### Generating external private keys

**Permissions:**

  * `iam.serviceAccountKeys.create`



**Roles:**

  * `roles/editor` (Editor)
  * `roles/iam.serviceAccountKeyAdmin` (Service Account Key Admin)



A user or service can generate external private key material (RSA) that can be used to authenticate directly to Google as the service account. This key material can then be used with Application Default Credentials (ADC) libraries, or with the [`gcloud auth activate-service-account`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/activate-service-account) command. Any person who gains access to the key material will then have full access to all resources to which the service account has access. Such private key material should be treated with the highest concern, and should be considered less secure the longer the material exists. Therefore, rotating private key material is critical to maintaining strong security.

## Service account permissions that enable other capabilities

Some permissions for service account credentials enable multiple capabilities. For example, `iam.serviceAccounts.signBlob` and `iam.serviceAccounts.signJwt` also let principals generate access tokens and ID tokens for a service account. Additionally, because `iam.serviceAccounts.signBlob` allows principals to sign any kind of data, it also lets principals sign JWTs.

Before adding any of these permissions to custom roles, ensure that you understand what actions each permission enables.

The following table shows the operations enabled by these permissions:

Permission | Enabled operations  
---|---  
`iam.serviceAccounts.getAccessToken` | Get an access token for the service account  
`iam.serviceAccounts.getOpenIdToken` | Get an ID token for the service account  
`iam.serviceAccounts.signJwt` | 

  * Sign a JWT
  * Get an access token or ID token for the service account by using a [ JWT bearer token](https://developers.google.com/identity/protocols/oauth2/service-account#authorizingrequests). 

  
`iam.serviceAccounts.signBlob` | 

  * Sign any type of blob, including JWTs
  * Get an access token or ID token for the service account by using a [ JWT bearer token](https://developers.google.com/identity/protocols/oauth2/service-account#authorizingrequests). 

  
  
## Best practices for granting roles on service accounts

In scenarios where a service account has been granted permissions to perform highly-privileged operations, be cautious when granting the Service Account User role or its included permissions to a user on that service account.

Service accounts represent your service-level security. The security of the service is determined by the people who have IAM roles to manage and use the service accounts, and people who hold [service account keys](https://docs.cloud.google.com/iam/docs/service-account-creds#user-managed-keys) for those service accounts. Best practices to ensure security include the following:

  * Use the IAM API to audit the service accounts, the keys, and the allow policies on those service accounts.
  * If your service accounts don't need service account keys, disable or delete them.
  * If users don't need permission to manage or use service accounts, then remove them from the applicable allow policy.
  * Understand how granting certain permissions for service accounts can effectively enable other capabilities.
  * Make sure that service accounts have the fewest permissions possible. Use [default service accounts](https://docs.cloud.google.com/iam/docs/service-account-types#default) with caution, because they are automatically granted the Editor (`roles/editor`) role on the project.



To learn more about best practices, see [Best practices for working with service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).

##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
