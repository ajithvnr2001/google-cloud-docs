---
url: https://docs.cloud.google.com/organization-policy/restrict-service-accounts/
title: Restrict IAM service account usage \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:10:04.195125+00:00
---

# Restrict IAM service account usage  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/restrict-service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Guides ](https://docs.cloud.google.com/organization-policy/overview)



Send feedback 

#  Restrict IAM service account usage Stay organized with collections  Save and categorize content based on your preferences. 

The Organization Policy Service provides constraints that can be used in [organization policies](https://docs.cloud.google.com/organization-policy/overview) to limit the usage of Identity and Access Management (IAM) [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts).

Many of these constraints determine whether service accounts and other resources can be created or configured in specific ways. These constraints are not retroactive; they do not affect previously created and configured service accounts.

## Before you begin

You must have permission to modify [organization policies](https://docs.cloud.google.com/resource-manager/reference/rest/v1/Policy) to set constraints. For example, the [`orgpolicy.policyAdmin`](https://docs.cloud.google.com/resource-manager/docs/access-control-org) role has permission to set organization policy constraints. Read the [Create organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies#delegate-admin) page to learn more about managing policies at the organization level.

## Managed constraints

The following constraints are types of [managed constraint](https://docs.cloud.google.com/organization-policy/overview#managed-constraints), which are set to true or false. Managed constraints are built on the [custom organization policy](https://docs.cloud.google.com/organization-policy/overview#custom-constraints) platform.

To learn how to create organization policies that enforce managed constraints, see [Create organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies#managed-constraints).

### Prevent the Owner and Editor role from being granted to default service accounts

Some Google Cloud services automatically create [default service accounts](https://docs.cloud.google.com/iam/docs/service-account-types#default). When a default service account is created, it is automatically granted the Editor role (`roles/editor`) on your project. Someone might also choose to grant a highly privileged role, like the Editor role or Owner role (`roles/owner`), to a default service account at a later time.

The Editor and Owner roles are highly privileged [basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic). You shouldn't grant them to any principal in production, including default service accounts.

To prevent default service accounts from being granted the Editor or Owner roles, use the `iam.managed.preventPrivilegedBasicRolesForDefaultServiceAccounts` managed constraint. This constraint prevents default service accounts from ever being granted the Editor or Owner roles, either automatically or manually.

### Disable service account creation

You can use the `iam.managed.disableServiceAccountCreation` managed constraint to disable the creation of new service accounts. This lets you centralize management of service accounts while not restricting the other permissions your developers have on projects.

If you enforce this constraint in a project, then some Google Cloud services cannot automatically create [default service accounts](https://docs.cloud.google.com/iam/docs/service-account-types#default). As a result, if the project runs workloads that need to [impersonate a service account](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts), the project might not contain a service account that the workload can use. To address this issue, you can [enable service account impersonation across projects](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project). When you enable this feature, you can create service accounts in a centralized project, then attach the service accounts to resources in other projects.

For more information about organizing service accounts, see [Where to create service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview#locations). 

### Limit creation of authorization keys to specific services

You can use the `iam.managed.disableServiceAccountApiKeyCreation` managed constraint to limit [authorization key](https://docs.cloud.google.com/docs/authentication/api-keys#api-keys-bound-sa) creation to specific services. When users create an authorization key, they must add an API restriction that matches a service allowed by the constraint.

This constraint is enforced and allows the [Gemini API](https://ai.google.dev/api) (`generativelanguage.googleapis.com`) by default.

### Disable service account key creation

You can use the `iam.managed.disableServiceAccountKeyCreation` managed constraint to disable the creation of new external service account keys and [Cloud Storage HMAC keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys). This lets you control the use of unmanaged long-term credentials for service accounts. When this constraint is set, user-managed credentials cannot be created for service accounts in projects affected by the constraint.

### Disable service account key upload

You can use the `iam.managed.disableServiceAccountKeyUpload` managed constraint to disable the upload of external public keys to service accounts. When this constraint is set, users cannot upload public keys to service accounts in projects affected by the constraint.

## Managed constraints (legacy) with boolean rules

The following constraints are types of legacy managed constraint with [boolean rules](https://docs.cloud.google.com/organization-policy/create-organization-policies#boolean-constraint), which are set to true or false.

### Disable automatic role grants to default service accounts

**Note:** This constraint prevents default service accounts from being automatically granted the Editor role (`roles/editor`). However, it doesn't prevent default service accounts from being granted the Editor or Owner roles later. To disable the automatic Editor role grant _and_ prevent the Editor and Owner roles from being granted to default service accounts in the future, use the `iam.managed.preventPrivilegedBasicRolesForDefaultServiceAccounts` managed constraint.

Some Google Cloud services automatically create [default service accounts](https://docs.cloud.google.com/iam/docs/service-account-types#default). When a default service account is created, it is automatically granted the Editor role (`roles/editor`) on your project.

To improve security, we strongly recommend that you disable the automatic role grant. Use the `iam.automaticIamGrantsForDefaultServiceAccounts` legacy managed constraint to disable the automatic role grant.

**Note** : If your organization was created on or after May 3, 2024, this constraint is enforced by default. 

### Disable service account creation

**Note:** To make your organization policies more flexible and to get greater insight from Policy Intelligence tools, we recommend using the equivalent managed constraint: `iam.managed.disableServiceAccountCreation`.

You can use the `iam.disableServiceAccountCreation` legacy managed constraint to disable the creation of new service accounts. This lets you centralize management of service accounts while not restricting the other permissions your developers have on projects.

If you enforce this constraint in a project, then some Google Cloud services cannot automatically create [default service accounts](https://docs.cloud.google.com/iam/docs/service-account-types#default). As a result, if the project runs workloads that need to [impersonate a service account](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts), the project might not contain a service account that the workload can use. To address this issue, you can [enable service account impersonation across projects](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project). When you enable this feature, you can create service accounts in a centralized project, then attach the service accounts to resources in other projects.

For more information about organizing service accounts, see [Where to create service accounts](https://docs.cloud.google.com/iam/docs/service-account-overview#locations).

### Disable service account key creation

You can use the `iam.disableServiceAccountKeyCreation` legacy managed constraint to disable the creation of new external service account keys and [Cloud Storage HMAC keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys). This lets you control the use of unmanaged long-term credentials for service accounts. When this constraint is set, user-managed credentials cannot be created for service accounts in projects affected by the constraint.

**Note** : If your organization was created on or after May 3, 2024, this constraint is enforced by default. 

### Disable service account key upload

**Note:** To make your organization policies more flexible and to get greater insight from Policy Intelligence tools, we recommend using the equivalent managed constraint: `iam.managed.disableServiceAccountKeyUpload`.

You can use the `iam.disableServiceAccountKeyUpload` legacy managed constraint to disable the upload of external public keys to service accounts. When this constraint is set, users cannot upload public keys to service accounts in projects affected by the constraint.

**Note** : If your organization was created on or after May 3, 2024, this constraint is enforced by default. 

### Disable attachment of service accounts to resources in other projects

Each service account is located in a project. You can use the `iam.disableCrossProjectServiceAccountUsage` legacy managed constraint to prevent service accounts in a project from being attached to resources in other projects.

If you want to allow service accounts to be used across projects, see [Enabling service account impersonation across projects](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project).

### Restrict removal of project liens when service accounts are used across projects

When you allow a project's service accounts to be attached to resources in other projects, IAM adds a [project lien](https://docs.cloud.google.com/resource-manager/docs/project-liens) that prevents you from deleting the project. By default, anyone who has the `resourcemanager.projects.updateLiens` permission on the project can delete the lien.

If you enforce the `iam.restrictCrossProjectServiceAccountLienRemoval` legacy managed constraint, then principals can delete the lien only if they have the `resourcemanager.projects.updateLiens` permission on the organization.

We recommend enforcing this constraint if any of your projects allow [service account impersonation across projects](https://docs.cloud.google.com/iam/docs/attach-service-accounts#enabling-cross-project).

### Disable workload identity cluster creation

You can use the `iam.disableWorkloadIdentityClusterCreation` legacy managed constraint to require that any new Google Kubernetes Engine clusters have the [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) feature disabled at the time of their creation. If you want to tightly control service account access in your organization, you may want to disable Workload Identity in addition to service account creation and service account key creation.

Existing GKE clusters with Workload Identity Federation for GKE enabled will not be affected, and will continue to work as normal.

## Setting a managed constraint (legacy) with boolean rules

### Console

To set an organization policy that enforces a constraint to restrict service account usage:

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the organization for which you want to restrict service account usage.

  3. Click one of the service account usage constraints listed on this page.

  4. Click **Manage policy**.

  5. Under **Applies to** , select **Override parent's policy**.

  6. Click **Add a rule**.

  7. Under **Enforcement** , select **On**.

  8. To enforce the policy, click **Set policy**.




### gcloud

Policies can be set through the Google Cloud CLI.

To restrict service account usage, run the following command:
    
    
    gcloud resource-manager org-policies enable-enforce \
        --organization 'ORGANIZATION_ID' \
        CONSTRAINT_NAME
    

Where CONSTRAINT_NAME is the constraint you want to enforce.

To disable enforcement, the same command can be issued with the 
    
    
    disable-enforce

command.

To learn about using constraints in organization policies, see [Create organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies#boolean-constraint).

### Example managed constraint (legacy) with boolean rules

The following code snippet shows an organization policy that enforces the `iam.disableServiceAccountCreation` legacy managed constraint, which prevents service accounts from being created:
    
    
    name: organizations/012345678901/policies/iam.disableServiceAccountCreation
    spec:
      rules:
      - enforce: true
    

## Managed constraints (legacy) with list rules

The following constraints are types of legacy managed constraint with [list rules](https://docs.cloud.google.com/organization-policy/create-organization-policies#list-constraint), which are set to a list of values.

### Extend lifetime of OAuth 2.0 access tokens

You can [create an OAuth 2.0 access token](https://docs.cloud.google.com/iam/docs/creating-short-lived-service-account-credentials#sa-credentials-oauth) that provides short-lived credentials for a service account. By default, the maximum lifetime of an access token is 1 hour (3,600 seconds). However, you can extend the maximum lifetime to 12 hours (43,200 seconds).

To do so, identify the service accounts that need an extended lifetime for tokens, then [add these service accounts to an organization policy](https://docs.cloud.google.com/organization-policy/apply-policies#list_constraints) that includes the `constraints/iam.allowServiceAccountCredentialLifetimeExtension` constraint. You can then specify a lifetime up to 43,200 seconds (12 hours) when you create a token using the REST API for these service accounts. The Google Cloud CLI doesn't support setting a lifetime for the token.

### Limit lifetime of service account keys

A [service account key](https://docs.cloud.google.com/iam/docs/service-account-overview) lets you authenticate a request as a service account. By default, service account keys never expire. You can change this default by setting an expiry time for all newly created keys in your project, folder, or organization.

**Caution:** In some scenarios, if you set an expiry time for service account keys, you might cause a production outage or disable business-critical workloads. Before you set an expiry time, review [Expiry times for user-managed keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys#key-expiry) and confirm that setting an expiry time is appropriate for your use case.

To set an expiry time, use the `constraints/iam.serviceAccountKeyExpiryHours` legacy managed constraint to specify the number of hours for which a newly created key is valid. After this amount of time, the service account key expires, and you can no longer use it.

This legacy managed constraint accepts the following `ALLOW` values; it does not accept `DENY` values. As a best practice, use the shortest expiry time that meets your needs:

  * `1h`: 1 hour
  * `8h`: 8 hours
  * `24h`: 24 hours (1 day)
  * `168h`: 168 hours (7 days)
  * `336h`: 336 hours (14 days)
  * `720h`: 720 hours (30 days)
  * `1440h`: 1,440 hours (60 days)
  * `2160h`: 2,160 hours (90 days)



The `constraints/iam.serviceAccountKeyExpiryHours` constraint can't be merged with a parent policy. To enforce this constraint, you must either replace or inherit the parent policy.

### Specify allowed external identity providers

If you use [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation), which lets external identities access Google Cloud resources, you can specify which external identity providers are allowed. By default, all providers are allowed. To set a limit, use the `constraints/iam.workloadIdentityPoolProviders` legacy managed constraint to specify URIs for the allowed providers, using the following formats:

  * Amazon Web Services (AWS): `https://sts.amazonaws.com`

To limit which AWS accounts are allowed, use the `constraints/iam.workloadIdentityPoolAwsAccounts` legacy managed constraint as described on this page.

  * Microsoft Azure: `https://sts.windows.net/azure-tenant-id`

  * Other identity providers that support OpenID Connect (OIDC): Use the issuer URI from your identity provider.




### Specify allowed AWS accounts

If you use [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation), which lets external identities access Google Cloud resources, you can specify which AWS accounts are allowed to access your resources. By default, workloads from any AWS account are allowed to access your Google Cloud resources. To limit which AWS accounts are allowed, use the `constraints/iam.workloadIdentityPoolAwsAccounts` legacy managed constraint to specify a list of allowed account IDs.

### Automatically disable exposed service account keys

Google Cloud occasionally detects that a particular service account key has been exposed—for example, it might detect a key in a public repository. To specify what Google Cloud does with these keys, use the `iam.serviceAccountKeyExposureResponse` legacy managed constraint. Keys that are monitored include long-lived service account keys and API keys that are bound to a service account.

**Important:** Google Cloud doesn't guarantee that it will detect exposed keys. To minimize key exposure and the effect of exposed keys, follow the [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

This legacy managed constraint accepts the following `ALLOW` values; it doesn't accept `DENY` values.

  * `DISABLE_KEY`: If Google Cloud detects an exposed key, it will automatically disable the key. It also creates a Cloud Audit Logs event and sends a notification about the exposed key to project owners and [security contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).

**Note:** Starting on June 16, 2024, if you don't set a value for this constraint, Google Cloud will default to the behavior described for `DISABLE_KEY`.
  * `WAIT_FOR_ABUSE`: Google Cloud won't proactively disable exposed keys. However, Google Cloud might still disable exposed keys if they're used in ways that adversely affect the platform. Regardless of whether the exposed key is disabled, Google Cloud creates a Cloud Audit Logs event and sends a notification about the exposed key to project owners and [security contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).




When Google Cloud detects a exposed key or disables an exposed key, it also does the following:

  * Generates Cloud Audit Logs events.

    * When Google Cloud detects that a key has been exposed, an abuse event is created in the [Abuse Event logs](https://docs.cloud.google.com/logging/docs/api/platform-logs#abuse_event).

    * When Google Cloud disables a key, the audit logs contain the disable action by principal `gcp-compromised-key-response@system.gserviceaccount.com`.

  * Sets the [`extendedStatus.value`](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts.keys#extendedstatus) field of the exposed or disabled key. The extended status field includes the location where the leak was detected.


**Note:** Audit logs for keys that were exposed between January 16, 2024 and June 16, 2024 were generated retroactively. To see when these keys were exposed, check the URL in the `extendedStatus.value` field of the key. This URL has the string `#HISTORIC_EXPOSED_KEY_EXPOSURE_DATE`, where `EXPOSURE_DATE` is the date that the key was exposed. Because these keys were exposed before this organizational policy was introduced, none of them were disabled automatically. We strongly advise that you rotate the exposed keys as soon as possible.

We strongly recommend that you set this constraint to `DISABLE_KEY`. Setting this constraint to `WAIT_FOR_ABUSE` increases the risk that exposed keys will be misused.

If you do decide to set the constraint to `WAIT_FOR_ABUSE`, we recommend that you subscribe to Cloud Audit Logs events, review your security contact information in [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts), and ensure that your security contacts respond to notifications in a timely manner.

The `iam.serviceAccountKeyExposureResponse` constraint can't be merged with a parent policy. To enforce this constraint, you must replace the parent policy.

## Setting a managed constraint (legacy) with list rules

### Console

To set an organization policy that contains a legacy managed constraint:

  1. In the Google Cloud console, go to the **Organization policies** page.

[Go to Organization policies](https://console.cloud.google.com/iam-admin/orgpolicies)

  2. From the project picker, select the resource for which you want to set the organization policy.

  3. On the **Organization policies** page, select a constraint from the list. The **Policy details** page for that constraint appears.

  4. To update the organization policy for this resource, click **Manage policy**.

  5. Under **Policy enforcement** , select an enforcement option:

     * To merge and evaluate your organization policies together, select **Merge with parent**. For more information about inheritance and the resource hierarchy, see [Hierarchy evaluation](https://docs.cloud.google.com/organization-policy/hierarchy-evaluation).
     * To override policies inherited from a parent resource, select **Replace**.
  6. Click **Add a rule**.

  7. Under **Policy values** , select **Custom**.

  8. Under **Policy type** , select **Allow**.

  9. Under **Custom values** , enter the first value for the legacy managed constraint.

     1. If you want to add more values, click **Add value** to create more rows, and add one value to each row.
  10. When you have finished adding values, click **Done**.

  11. To enforce the policy, click **Set policy**.




### gcloud

Policies can be set through the Google Cloud CLI:
    
    
    gcloud resource-manager org-policies allow \
        CONSTRAINT_NAME \
        VALUE_1 [VALUE_N ...] \
        --organization=ORGANIZATION_ID \

Replace the following values:

  * `CONSTRAINT_NAME`: The name of the legacy managed constraint. For example, `constraints/iam.allowServiceAccountCredentialLifetimeExtension`.
  * `VALUE_1`, `VALUE_N...`: Values for the legacy managed constraint.



To learn about using constraints in organization policies, see [Create organization policies](https://docs.cloud.google.com/organization-policy/create-organization-policies#list-constraint).

### Example managed constraint (legacy) with list rules

The following code snippet shows an organization policy that enforces the `iam.allowServiceAccountCredentialLifetimeExtension` legacy managed constraint, which extends the maximum lifetime of OAuth 2.0 access tokens for listed service accounts:
    
    
    name: organizations/012345678901/policies/iam.allowServiceAccountCredentialLifetimeExtension
    spec:
      rules:
      - values:
          allowedValues:
          - SERVICE_ACCOUNT_ADDRESS
    

## Enforcing constraints conditionally using tags

[Tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) can be used to include or exclude tagged resources from organization policy enforcement. After [creating a tag and attaching it to a service account](https://docs.cloud.google.com/iam/docs/service-accounts-tags), you can add a condition to the policy to conditionally include or excluded tagged service accounts from enforcement.

For more details on using tags with organization policies, see [Scope organization policies with tags](https://docs.cloud.google.com/organization-policy/scope-policies).

**Note:** Tags cannot be used with service accounts to conditionally enforce iam.disableCrossProjectServiceAccountUsage. This constraint is enforced at the project level, so service account tags won't be evaluated.

## Error messages

### Disable service account creation

If `iam.disableServiceAccountCreation` is enforced, creating a service account will fail with the error:
    
    
    FAILED_PRECONDITION: Service account creation is not allowed on this project.

### Disable creation of API keys bound to service accounts

If `iam.managed.disableServiceAccountApiKeyCreation` is enforced, creating an API key that is bound to a service account will fail with the error:
    
    
    FAILED_PRECONDITION: Operation denied by org policy:
    ["constraints/iam.managed.disableServiceAccountApiKeyCreation":
    "When enforced, disables creation of API Keys bound to service accounts."]
    

### Disable service account key creation

If `iam.disableServiceAccountKeyCreation` is enforced, creating a service account will fail with the error:
    
    
    FAILED_PRECONDITION: Key creation is not allowed on this service account.

### Disable workload identity cluster creation

If `iam.disableWorkloadIdentityClusterCreation` is enforced, creating a GKE cluster with Workload Identity enabled will fail with the error:
    
    
    FAILED_PRECONDITION: Workload Identity is disabled by the organization
    policy constraints/iam.disableWorkloadIdentityClusterCreation. Contact your
    administrator to enable this feature.

## Troubleshooting known issues

### Default service accounts

Applying the `iam.disableServiceAccountCreation` constraint will prevent the creation of service accounts in that project. This limitation also affects Google Cloud services that, when enabled, automatically create default service accounts in the project, such as:

  * Compute Engine
  * GKE
  * App Engine
  * Dataflow



If the `iam.disableServiceAccountCreation` constraint is applied, attempting to enable these services will fail because their default service accounts cannot be created.

To resolve this issue:

  1. Temporarily remove the `iam.disableServiceAccountCreation` constraint.
  2. Enable the desired services.
  3. Create any other desired service accounts.
  4. Finally, re-apply the constraint.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
