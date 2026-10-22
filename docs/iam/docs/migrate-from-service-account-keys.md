---
url: https://docs.cloud.google.com/iam/docs/migrate-from-service-account-keys/
title: Migrate from service account keys \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:29.506390+00:00
---

# Migrate from service account keys  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/migrate-from-service-account-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Migrate from service account keys Stay organized with collections  Save and categorize content based on your preferences. 

[Service account keys](https://docs.cloud.google.com/iam/docs/service-account-creds#key-types) are commonly used to authenticate to Google Cloud services. However, they can also become a security risk if they're not managed properly, increasing your vulnerability to threats like credential leakage, privilege escalation, information disclosure, and non-repudiation.

In many cases, you can authenticate with [more secure alternatives](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) to service account keys. This guide helps you to migrate from using service account keys as your primary authentication mechanism to using more secure alternatives, with occasional exceptions where service account keys are truly necessary.

This document is intended for security administrators who want to improve their security posture by reducing the usage of service account keys in favor of more secure authentication mechanisms. These security administrators might be responsible for the security of existing production workloads, developer workflows, and internal processes that use service account keys.

## Overview

Removing service account keys from existing workloads requires careful planning to prevent accidental disruption. The following migration plan is designed to allow you to enforce centralized controls while minimizing disruption to developers.

This migration plan includes three phases:

  * **Assess:** In this phase, you assess your existing environment to understand where service account keys exist and whether the keys are in use.
  * **Plan:** In this phase, you decide which controls you will eventually deploy and communicate the migration plan to stakeholders.
  * **Deploy:** In this phase, you begin refactoring workloads to authenticate with more secure alternatives to service account keys. You also build additional capabilities to continuously monitor your environment and mitigate future risk.



## Assess service account key use

In this phase, you assess your existing environment to understand where service account keys exist and whether the keys are in use.

The following sections describe the data you can collect to better understand how service account keys are used in your organization.

### Gather data on key usage

First, identify where service account keys exist and how they're used.

Google Cloud provides [tools to understand service account usage](https://docs.cloud.google.com/policy-intelligence/docs/service-account-usage-tools). These tools help you determine which service accounts and keys were recently used to authenticate, which service accounts haven't been used in the past 90 days, and which service accounts have overly privileged roles.

You can combine information from all of these tools to get a better picture of how service accounts and keys are used across your organization. For an example of how to combine information from these various sources across your entire organization, see the [deployable reference architecture](https://github.com/GoogleCloudPlatform/migrate-from-service-account-keys) on GitHub. This reference architecture aggregates data from various tools and regularly exports it to a BigQuery table for analysis.

![](https://docs.cloud.google.com/static/iam/img/migrate-sa-keys-architecture.svg)

![](https://docs.cloud.google.com/static/iam/img/migrate-sa-keys-architecture.svg)

The reference architecture deploys a data pipeline that queries Cloud Asset Inventory to identify service account keys in your organization. Then, the data pipeline combines that data with data about key usage and permission usage for the associated account. The resulting table, `sa_key_usage`, helps you answer questions like the following:

  * **How many persistent keys have been created?** This number can be useful as a high-level metric to track progress as you migrate away from keys.
  * **Which projects and service accounts use keys?** This information helps you identify the owners of workloads that use service account keys.
  * **Which keys are inactive?** You can likely delete these keys without further assessment from workload owners. 
  * **Which keys are associated with service accounts that have recommendations about excess permissions?** If a service account key is associated with an overly privileged service account, especially one with an Owner, Editor, or Viewer role, the key might be particularly high-risk. Looking for service accounts that have [role recommendations](https://docs.cloud.google.com/policy-intelligence/docs/role-recommendations-overview) can help you identify which service accounts are overly privileged. After you identify these service accounts, you might decide to prioritize these workloads for migration. You can also choose to apply the role recommendations to proactively reduce excess permissions. 



This data pipeline runs daily and writes to a date-partitioned BigQuery table. You can use this table to investigate specific service accounts or keys, or to track remediation progress using a dashboard tool like [Data Studio](https://support.google.com/looker-studio/answer/6283323).

### Enrich key usage data with additional context

After you gather data about key usage, you can optionally enrich your data with additional data sources. We recommend adding data sources that you already use for tracking governance and provenance of resources. Depending on your existing governance, you might add additional data such as the following:

  * Ownership information from a configuration management database (CMDB) or similar system.
  * Governance information configured in [project labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels#common-uses), like the team or cost center responsible for a project.
  * Environment information about keys used for workloads in environments external to Google Cloud.



## Create a plan for reducing service account key usage

Before you can deploy any changes to reduce service account key usage, you need to determine which workloads and environments will be affected and how you will enforce those changes. You also need to communicate this plan across your business and make sure that workload owners support the plan.

The following sections introduce key topics your plan should address. Your specific plan will vary based on the size of your organization and the specific requirements of your workloads.

### Decide the responsibility of current workload owners

Although a central security team can assess which keys exist, a successful migration requires effort from workload owners. For keys in scope for migration, workload owners must determine which of the available authentication methods will work for their use case, then execute that migration.

Consider how to balance improvements to your existing security posture against the effort required from workload owners. The following sections describe two sample approaches: one that heavily prioritizes improvements to your security posture, and one that heavily prioritizes minimizing effort from workload owners. Your actual approach might vary—for example, you might decide to individually select which workloads are in scope.

#### Example: All current workloads are evaluated for migration

One possible approach is to enforce service account key controls for all existing and future workloads. This involves steps like the following:

  * Collaborating with workload owners to evaluate their key usage for existing workloads.
  * Requiring that workload owners migrate all existing workloads with key usage, unless they have been granted an exception.
  * Preventing all future workloads from using service account keys, unless they have been granted an exception.



This approach prioritizes improvements to your existing security posture but requires more effort from developers and workload owners in the short term. To successfully execute a plan like this, you must have commitment from workload owners to participate in workload review and refactoring.

#### Example: No current workloads are evaluated for migration

Another approach is to allow existing workloads an automatic exception to continue using service account keys and only apply new controls on future workloads.

This approach improves the security posture of future workloads and minimizes the responsibility of current workload owners. However, it doesn't improve the security posture of existing workloads.

### Identify quick wins

In your assessment, you might identify keys that can be safely deleted without further remediation work from workload owners. For example, if a key has no activity for 90 days, or is related to resources that are no longer active, you might be able to remove it safely without needing to migrate to a different authentication mechanism.

Make a list of keys that meet this criteria. You will use this list during the deployment phase to delete unnecessary keys. Before you add a key to the list, confirm whether there are use cases that require the service account key infrequently, such as emergency production access relying on service account keys.

### Plan where to enforce organization policy changes

To successfully migrate away from using service account keys, you need to prevent new keys from being created. During the deployment phase, you enforce the [`iam.disableServiceAccountKeyCreation`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_key_creation) organization policy constraint to prevent the creation of new service account keys.

**Note** : If your organization was created on or after May 3, 2024, this constraint is enforced by default. 

Although this constraint doesn't prevent the usage of existing keys, it might disrupt existing workloads that regularly rotate their keys. Before you start the deployment phase, decide where you will enforce it in your resource hierarchy to minimize disruption.

You might prefer to initially enforce the constraint at the project or folder level instead of the organization level. For example, you might enforce the constraint on the folder used for your development environment before deploying it to production folders. Or, in a large organization with many teams, you might enforce the constraint on a folder for a single team first, and then enforce the constraint for additional folders as you migrate them.

You can use [organization policies with tags](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy) to conditionally enforce organization policies at the project or folder level.

### Design an exceptions process

Although the goal of this migration is to reduce or eliminate service account key usage, there are some legitimate use cases that require service account keys. Even if no existing workloads require service account keys, it's possible that future workloads will. Therefore, you must define an operational process to evaluate and approve exceptions for use cases that require service account keys.

Define a process for workload owners to request an exception that allows their workload to use service account keys. Ensure that the decision makers responsible for granting an exception have the technical knowledge to validate the use case, consult with the workload owners on which of the more secure alternatives to service account keys might be more appropriate, and advise workload owners about [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

### Communicate upcoming changes to workload owners

After you've designed a plan, you need to clearly communicate that plan across your organization and make sure that stakeholders, particularly senior leaders, are willing to commit to the migration.

While the specific migration details will vary for your organization, consider including the following topics in your communication plan:

  * The negative impact that insecure service account keys can have on the organization, and the motivations that drive your migration away from service account keys.
  * The new security controls to prevent service account key creation and how this can impact existing processes.
  * Guidance for developers to identify more secure alternatives to service account keys.
  * The process for teams to request an exception to allow service account keys, including how frequently this exception is re-evaluated.
  * The timeline to enforce your proposed changes.



Work with workload owners to refine your plan and ensure that it works across your organization.

## Deploy controls and refactor workloads

After you create a plan and communicate it to workload owners, you can begin migrating away from service account keys.

In this phase, you begin refactoring workloads to authenticate with more secure alternatives to service account keys. You also build additional capabilities to continuously monitor your environment and mitigate future risk.

The following sections describe the steps you can take to refactor workloads and delete keys with minimal disruption. You can choose to do these steps in any order, based on the priority and effort required for your organization.

### Enforce controls to stop the creation of new service account keys

To stop the creation of new service account keys, you enforce the [`iam.disableServiceAccountKeyCreation`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_key_creation) organization policy constraint.

However, before enforcing this constraint, you need to add [tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) to any projects or folders that will be exempt from the policy. You might allow exceptions for existing workloads that are unable to migrate from service account keys, or for new workloads that have a legitimate reason to authenticate only with service account keys.

After you add tags to exempt projects and folders, you can set an [organization policy with tags](https://docs.cloud.google.com/resource-manager/docs/organization-policy/tags-organization-policy) to enforce the `iam.disableServiceAccountKeyCreation` constraint for non-exempt projects and folders.

To prevent the creation of service account keys in all non-exempt projects and folders, do the following:

  1. Ensure that you have the Tag Administrator role (`roles/resourcemanager.tagAdmin`) and the Organization Policy Administrator role (`roles/orgpolicy.policyAdmin`) at the organization level. To learn how to grant roles at the organization level, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  2. At the organization level, create a tag key and tag value that you will use to define whether a resource should be exempt from the organization policy. We recommend creating a tag with the key `disableServiceAccountKeyCreation` and the values `enforced` and `not_enforced`. 

To learn how to create tag keys and tag values, see [Creating and defining a new tag](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating). 

  3. Attach the `disableServiceAccountKeyCreation` tag to the organization and set its value to `enforced`. All resources in the organization inherit this tag value, unless it's overwritten with a different tag value. 

To learn how to attach tags to resources, see [Attaching tags to resources](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#attaching). 

  4. For each project or folder that you want to exempt from the organization policy, attach the `disableServiceAccountKeyCreation` tag and set its value to `not_enforced`. Setting a tag value for a project or folder in this way overrides the tag value inherited from the organization. 
  5. [Create an organization policy](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies) that prevents the creation of service account keys for all resources except the exempt resources. This policy should have the following rules: 

     * Configure the `iam.disableServiceAccountKeyCreation` constraint to not be enforced on any resources with the `disableServiceAccountKeyCreation: not_enforced` tag. The condition in this rule should look like the following: 
           
           "resource.matchTag('ORGANIZATION_ID/disableServiceAccountKeyCreation', 'not_enforced')"
           

     * Configure the `iam.disableServiceAccountKeyCreation` constraint to be enforced on all other resources. 



### Remediate existing workloads

For each workload that uses service account keys, collaborate with the workload owners to choose and implement an alternative authentication method.

When you access Google Cloud services by using the Google Cloud CLI, Cloud Client Libraries, tools that support [ Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) like Terraform, or REST requests, use the following diagram to help you choose an authentication method: 

![Decision tree for choosing authentication method based on use case](https://docs.cloud.google.com/static/docs/authentication/images/authn-tree.svg)

This diagram guides you through the following questions: 

  1. Are you running code in a single-user development environment, such as your own workstation, Cloud Shell, or a virtual desktop interface? 
     1. If yes, proceed to question 4.
     2. If no, proceed to question 2.
  2. Are you running code in Google Cloud? 
     1. If yes, proceed to question 3.
     2. If no, proceed to question 5.
  3. Are you running containers in Google Kubernetes Engine? 
     1. If yes, use [ Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity#authenticating_to) to attach service accounts to Kubernetes pods. 
     2. If no, [attach a service account](https://docs.cloud.google.com/iam/docs/attach-service-accounts#attaching-to-resources) to the resource. 
  4. Does your use case require a service account?

For example, you want to configure authentication and authorization consistently for your application across all environments. 

     1. If no, [authenticate with user credentials](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment#local-user-cred). 
     2. If yes, [ impersonate a service account with user credentials](https://docs.cloud.google.com/docs/authentication/use-service-account-impersonation). 
  5. Does your workload authenticate with an external identity provider that supports [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation#providers)? 
     1. If yes, [ configure Workload Identity Federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds) to let applications running on-premises or on other cloud providers use a service account. 
     2. If no, [create a service account key](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment#local-key). 



In some cases, you might not be able to use any authentication method other than service account keys. Examples of where a service account key might be your only feasible option include the following:

  * You're using commercial off-the-shelf products (COTS) or software-as-a-service (SaaS) applications that ask you to input a Google Cloud service account key directly into its user interface.
  * Your workload is running outside of Google Cloud and isn't authenticated with an identity provider that can support [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation).



In cases where you must keep using service account keys, ensure that you're following the [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).

You might also decide not to remediate certain workloads because you assess that the risk of continuing to use service account keys doesn't justify the cost of switching to a different authentication method.

### Delete unnecessary keys

If you are certain that a service account key isn't needed, you should delete the key. Unnecessary keys include the following:

  * Keys with no recent usage or keys that are related to unused resources, which you identified in the Identify quick wins section of this page.

  * Keys for workloads that have migrated to other authentication methods.

After you delete all of the service account keys in a project, ensure that the `iam.disableServiceAccountKeyCreation` constraint is enforced for that project. If the project was previously exempt from this constraint, remove the tag that allowed for the exemption.




To delete keys safely, we recommend that you [disable the key](https://docs.cloud.google.com/iam/docs/keys-disable-enable#disabling) before deleting it. Deleting is irreversible, but disabling it lets you quickly re-enable the key if you identify unexpected issues. After you disable the key, wait until you're sure that removing the key permanently won't cause issues, then [delete the key](https://docs.cloud.google.com/iam/docs/keys-create-delete#deleting). If, after disabling the key, you identify unexpected issues, re-enable the key, resolve the issues, and then repeat the process until you can safely delete the key.

### Use built-in controls to help respond to leaked keys

Google Cloud offers tools and services to help you detect and respond to leaked service account keys. Consider using the following mechanisms to help you respond to leaked service account keys:

  * The [Service Account Key Exposure Response constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable-exposed-keys) lets you automatically disable exposed keys that Google Cloud detects. 

To learn about other best practices for managing compromised credentials, see [Handling compromised Google Cloud credentials](https://docs.cloud.google.com/docs/security/compromised-credentials). 

### Ongoing improvements to service account management

Wherever possible, implement [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). Improving your key management processes can help mitigate the risk of any remaining service account keys in your organization.

## What's next

  * [Best practices for using service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts)
  * [Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys)
  * [Build a collaborative incident management process](https://docs.cloud.google.com/architecture/framework/operational-excellence/manage-incidents-and-problems)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
