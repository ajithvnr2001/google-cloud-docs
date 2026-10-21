---
url: https://docs.cloud.google.com/iam/docs/service-accounts-actas/
title: Requiring permission to attach service accounts to resources \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T11:16:17.862333+00:00
---

# Requiring permission to attach service accounts to resources  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/service-accounts-actas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)



Send feedback 

#  Requiring permission to attach service accounts to resources Stay organized with collections  Save and categorize content based on your preferences. 

When you create certain Google Cloud resources, you have the option to attach a [service account](https://docs.cloud.google.com/iam/docs/service-accounts). The attached service account acts as the identity of any jobs running on the resource, allowing the jobs to authenticate to Google Cloud APIs.

For most Google Cloud services, users need permission to impersonate a service account in order to attach that service account to a resource. This means that the user needs the `iam.serviceAccounts.actAs` permission on the service account.

However, in the past, certain services allowed users to attach service accounts to resources even if the users didn't have permission to impersonate the service accounts. This configuration might have made it possible for users of these services to gain elevated, non-obvious permissions.

The following table lists services that had this configuration, along with each service's legacy behavior:

Service | Legacy behavior  
---|---  
App Engine | Users could deploy App Engine applications, which use the identity of the App Engine default service account, even if they didn't have permission to impersonate the App Engine default service account.  
Managed Service for Apache Airflow | Users could attach any service account in the project to a Managed Airflow environment, even if they didn't have permission to impersonate any of the project's service accounts.  
  
  * Cloud Data Fusion
  * Dataflow
  * Managed Service for Apache Spark

| Users could attach the Compute Engine default service account to resources, even if they didn't have permission to impersonate the default service account.  
Dataform | Users could attach a service account to a Dataform resource and create a workflow invocation that would execute as that service account, even if they didn't have permission to impersonate the service account.  
  
We now require that these services check that users have permission to impersonate service accounts when attaching the service accounts to resources. **However, the legacy behavior still exists for the following types of organizations:**

  * Organizations with users who have permission to deploy App Engine applications, but don't have permission to impersonate the App Engine default service account.
  * Organizations with users who have permission to deploy Managed Airflow environments, but don't have permission to impersonate any service accounts.
  * Organizations with users who have permission to deploy Cloud Data Fusion, Dataflow, or Managed Service for Apache Spark resources, but don't have permission to impersonate the Compute Engine default service account.



If your organization is still affected by the legacy behavior, you will have received communication explaining how to manually disable it. You can also refer to the sections below for detailed instructions.

## Securing App Engine

To manually disable the legacy behavior for App Engine, ensure that users have permission to impersonate the App Engine service account. Then, enable an organization policy constraint to enforce service account permission checks when deploying applications that use the identity of the App Engine default service account.

  1. Optional: Use [role recommendations](https://docs.cloud.google.com/iam/docs/recommender-overview) to safely downscope permissions for the App Engine default service account.

The App Engine default service account is automatically granted the highly permissive Editor role (`roles/editor`). However, we don't recommend using such a highly permissive role in production configurations.

**Note:** To further secure your organization, you can [disable automatic role grants](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) to service accounts
  2. Ensure that all users who deploy applications have the ability to impersonate the App Engine default service account.

To provide this ability, grant the users a role that includes the `iam.serviceAccounts.actAs` permission, like the Service Account User role (`roles/iam.serviceAccountUser`). You can grant this role on the project or on the App Engine default service account. For instructions, see [Managing service account impersonation](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts).

**Note:** If you have a large number of projects, you can use the [permission discrepancy finder](https://github.com/GoogleCloudPlatform/professional-services/tree/master/tools/permission-discrepancy-finder) to find users who have permission to deploy applications, but not to impersonate the App Engine default service account.
  3. Enable the [organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#boolean-constraint) `constraints/appengine.enforceServiceAccountActAsCheck` to enforce service account permission checks when deploying applications.

**Note:** This organization policy constraint is only visible in environments with the legacy behavior. If you don't see the constraint, then the constraint is already enforced in your environment.
  4. Optional: Use the [boolean organization policy enforcer](https://github.com/GoogleCloudPlatform/professional-services/tree/master/tools/boolean-org-policy-enforcer) to confirm that the organization policy constraint is enforced in all of your projects.




## Securing Managed Service for Apache Airflow

To manually disable the legacy behavior for Managed Airflow, ensure that users have permission to impersonate the service accounts that they attach to new environments. Then, enable an organization policy constraint to enforce service account permission checks when attaching service accounts to environments.

  1. Identify all service accounts that are bound to Managed Airflow environments:

     1. In the Google Cloud console, go to the **Composer environments** page.

[Go to the Composer environments page](https://console.cloud.google.com/composer/environments)

     2. Click the name of an environment.

     3. In the **Environment configuration** tab, find the **Service account** field and record the name of the service account.

     4. Repeat the preceding steps for all Managed Airflow environments in your project.

  2. Confirm that these service accounts follow the principle of [least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege):

     * In the Google Cloud console, go to the **IAM** page, find the service accounts, and review their roles.

[Go to the IAM page](https://console.cloud.google.com/iam-admin)

     * If necessary, [grant a less permissive role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) to the service account. You can select a role from the list of [IAM predefined roles](https://docs.cloud.google.com/iam/docs/roles-permissions), use a role suggested by a [role recommendation](https://docs.cloud.google.com/iam/docs/recommender-overview), or create a [custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#creating_a_custom_role).

  3. Ensure that all users who deploy or manage Managed Airflow environments have the ability to impersonate the service accounts that the environments use.

To provide this ability, grant the users a role that includes the `iam.serviceAccounts.actAs` permission, like the Service Account User role (`roles/iam.serviceAccountUser`). You can grant this role on the project or on an individual service account. For instructions, see [Managing service account impersonation](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts).

**Note:** If you have a large number of projects, you can use the [permission discrepancy finder](https://github.com/GoogleCloudPlatform/professional-services/tree/master/tools/permission-discrepancy-finder) to find users who have permission to deploy Managed Airflow environments, but not to impersonate service accounts.
  4. Enable the [organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#boolean-constraint) `constraints/composer.enforceServiceAccountActAsCheck` to enforce service account permission checks when attaching service accounts to environments.

**Note:** This organization policy constraint is only visible in environments with the legacy behavior. If you don't see the constraint, then the constraint is already enforced in your environment.
  5. Optional: Use the [boolean organization policy enforcer](https://github.com/GoogleCloudPlatform/professional-services/tree/master/tools/boolean-org-policy-enforcer) to confirm that the organization policy constraint is enforced in all of your projects.




## Securing Managed Service for Apache Spark, Dataflow, and Cloud Data Fusion

To manually disable the legacy behavior for Managed Service for Apache Spark, Dataflow, and Cloud Data Fusion, ensure that users have permission to impersonate the service accounts that they attach to new resources. Then, enable organization policy constraints to enforce service account permission checks when attaching service accounts to resources.

Follow the instructions for the type of service account that you want to attach to new resources:

  * If you want to stop attaching the Compute Engine default service account to new resources, follow these steps:

**Note:** In Cloud Data Fusion, using service accounts other than the Compute Engine default service account is only available for [Cloud Data Fusion Enterprise](https://docs.cloud.google.com/data-fusion/pricing#comparison_of_basic_and_enterprise_editions) customers. For more information, see [Cloud Data Fusion service accounts](https://docs.cloud.google.com/data-fusion/docs/concepts/service-accounts#service_account_table).
    1. [Create a new service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts#creating) and grant the service account the roles it needs to run jobs on the resource. Make sure to follow the [principle of least privilege](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

To learn which roles a service account needs to run jobs on Managed Service for Apache Spark, Dataflow, and Cloud Data Fusion resources, see the following:

       * [Managed Service for Apache Spark service account requirements](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts#service_account_requirements_and_limitations)
       * [Dataflow service account requirements](https://docs.cloud.google.com/dataflow/docs/concepts/security-and-permissions#specifying_a_user-managed_controller_service_account)
       * Cloud Data Fusion service accounts have the same requirements as Managed Service for Apache Spark service accounts.
    2. Allow all users who deploy these resources to impersonate the new service account.

To provide this ability, grant users a role that includes the `iam.serviceAccounts.actAs` permission, like the Service Account User role (`roles/iam.serviceAccountUser`). You can grant this role on the project or on the service account. For instructions, see [Managing service account impersonation](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts).

    3. Enable the following [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#boolean-constraint) to enforce service account permission checks when attaching service accounts to resources:

       * `constraints/dataflow.enforceComputeDefaultServiceAccountCheck`
       * `constraints/dataproc.enforceComputeDefaultServiceAccountCheck`

The organization policy constraint `constraints/dataproc.enforceComputeDefaultServiceAccountCheck` also enforces permission checks for Cloud Data Fusion.

**Note:** These organization policy constraints are only visible in environments with the legacy behavior. If you don't see the constraints, then the constraints are already enforced in your environment.
    4. Optional: Use the [boolean organization policy enforcer](https://github.com/GoogleCloudPlatform/professional-services/tree/master/tools/boolean-org-policy-enforcer) to confirm that the organization policy constraints are enforced in all of your projects.

    5. When you deploy new resources, use the new service account instead of the Compute Engine default service account.

  * If you want to continue to attach the Compute Engine default service account to new resources, follow these steps:

    1. Optional: Use [role recommendations](https://docs.cloud.google.com/iam/docs/recommender-overview) to safely downscope permissions for the Compute Engine default service account.

The Compute Engine default service account is automatically granted the highly permissive Editor role (`roles/editor`). However, we don't recommend using such a highly permissive role in production configurations.

**Note:** To further secure your organization, you can [disable automatic role grants](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) to service accounts.
    2. Ensure that all users who deploy these resources have the ability to impersonate the Compute Engine default service account.

To provide this ability, grant the users a role that includes the `iam.serviceAccounts.actAs` permission, like the Service Account User role (`roles/iam.serviceAccountUser`). You can grant this role on the project or on the Compute Engine default service account. For instructions, see [Managing service account impersonation](https://docs.cloud.google.com/iam/docs/impersonating-service-accounts).

**Note:** If you have a large number of projects, you can use the [permission discrepancy finder](https://github.com/GoogleCloudPlatform/professional-services/tree/master/tools/permission-discrepancy-finder) to find users who have permission to deploy resources, but not to impersonate the Compute Engine default service account.
    3. Enable the following [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#boolean-constraint) to enforce service account permission checks when attaching service accounts to resources:

       * `constraints/dataflow.enforceComputeDefaultServiceAccountCheck`
       * `constraints/dataproc.enforceComputeDefaultServiceAccountCheck`
    4. Optional: Use the [boolean organization policy enforcer](https://github.com/GoogleCloudPlatform/professional-services/tree/master/tools/boolean-org-policy-enforcer) to confirm that the organization policy constraints are enforced in all of your projects.




## Securing Dataform

To manually disable the legacy behavior for Dataform, ensure that users have permission to impersonate the service accounts that they attach to Dataform resources.

**Note:** [Strict act-as mode](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode) is enforced globally on all Dataform repositories.

  1. Check for permission issues to avoid interrupting your workflows. You can do this by querying Cloud Logging for Dataform-specific entries that indicate a principal (user or service account) is missing the required `iam.serviceAccounts.actAs` permission. This lets you proactively identify and resolve any access discrepancies. For more information, see [Check for permission issues in Cloud Logging](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode#check-permission-issues).

  2. For users or service accounts that need to create workflow invocations, grant them the permission to impersonate the service account associated with the Dataform repository. You can provide this permission by granting the [Service Account User role](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) (`roles/iam.serviceAccountUser`) on the specific service account. For more information, see [Resolve permission issues](https://docs.cloud.google.com/dataform/docs/strict-act-as-mode#resolve-issues).

  3. If you're using a custom service account, grant the following roles to the default Dataform service agent on the custom service account:

     * [Service Account Token Creator](https://docs.cloud.google.com/iam/docs/service-account-permissions#token-creator-role) (`roles/iam.serviceAccountTokenCreator`): required for all repository operations using a custom service account.
     * [Service Account User](https://docs.cloud.google.com/iam/docs/service-account-permissions#user-role) (`roles/iam.serviceAccountUser`): required only if you're using workflow configurations to schedule or automate executions. This role allows the default Dataform service agent to run tasks as the custom service account.
  4. Periodically audit your Dataform resources to ensure proper service account usage and permission grants. Use Cloud Asset Inventory to list all resources of the `dataform.Repository` and `dataform.WorkflowConfig` types, and then inspect the `resource.data.serviceAccount` field to check which service account is being used. If a custom service account is used, verify that the default Dataform service agent has both the Service Account User (`roles/iam.serviceAccountUser`) and Service Account Token Creator (`roles/iam.serviceAccountTokenCreator`) roles on that custom service account. For more information, see [Audit service account configurations](https://docs.cloud.google.com/dataform/docs/access-control#audit_service_account_configurations).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
