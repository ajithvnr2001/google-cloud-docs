---
url: https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates/
title: Cloud Build default service account change \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:27:41.008620+00:00
---

# Cloud Build default service account change  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Build ](https://docs.cloud.google.com/build/docs)
  * [ Guides ](https://docs.cloud.google.com/build/docs/build-push-docker-image)



Send feedback 

#  Cloud Build default service account change Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Build automatically selects the Cloud Build service account to execute builds on your behalf, unless you override this behavior. This default service account may have permissions that are unnecessarily broad for your use case, such as access to any Cloud Storage bucket in your project.

The default behavior for how Cloud Build uses service accounts in new projects was changed over several weeks in May and June 2024. These changes improve the default security posture of our customers going forward. You can opt out of these changes by configuring the organization policy constraint.

**Before this change** , Cloud Build used a Cloud Build-specific service account as the default, now referred to as the Cloud Build legacy service account.

**After this change** , Cloud Build now uses the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) as the default service account.

How your projects are impacted depends on whether you're part of an organization:

  * **Projects without an organization**. If you run the first build in your project after the change, that project will use the [Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) by default for builds submitted using the Cloud Build API or the Google Cloud CLI. These projects won't have the option to use the Cloud Build legacy service account, but can [use a user-specified service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts).

  * **Projects with an organization**. If you run the first build in your project after the change, that project will use the [Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) by default for builds submitted using the Cloud Build API or the Google Cloud CLI. You can use a [user-specified service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts) or opt out of the change by enabling the Cloud Build service account in your organization.

  * **Existing projects without an organization**. If you ran the first build in your project before the change, that project will continue with the old behavior, using the Cloud Build legacy service account by default for all your builds. You can continue to use a [user-specified service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts), by either selecting the Compute Engine service account or creating your own.

  * **Existing projects with an organization**. If you ran the first build in your project before the change, that project will continue with the old behavior, using the Cloud Build legacy service account by default. You can also continue to use a [user-specified service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts).

  * **Triggering**. You'll have to specify a service account when you create or update a trigger, unless the default service account for your project is the Cloud Build legacy service account.

  * **Cloud Build service account name** : The Cloud Build service account will be referred to as the **Cloud Build legacy service account**.




## What do you need to do?

If you are part of an organization, your organization can configure the behavior of all the projects by setting up an organization policy with the chosen constraints.

Your organization can opt out of these changes by setting the following organization policy [boolean constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#boolean_constraint):

  * Not enforced: `constraints/cloudbuild.disableCreateDefaultServiceAccount`
  * Not enforced: `constraints/cloudbuild.useComputeServiceAccount`
  * Enforced: `constraints/cloudbuild.useBuildServiceAccount`



If you can't or don't want to adjust the organization policy, and you enable the Cloud Build API after the change, validate that the either the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) or [your user-created service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts) has enough permissions for your build. In particular, the user submitting the build must have the [`iam.serviceAccounts.actAs`](https://docs.cloud.google.com/iam/docs/permissions-reference) permission on the service account.

## New organization policy constraints

Cloud Build has introduced new organization policy [boolean constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#boolean_constraint) to configure:

  * The ability to use the Cloud Build legacy service account.
  * The default service account for all the projects in an organization.



To modify organization policies, you can use Google Cloud console or the Google Cloud CLI:

  * Google Cloud console: Select the constraint you want to change and [set the **Enforcement** option to **On** or **Off** in the Google Cloud console](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#boolean_constraints).

  * Google Cloud CLI: [Configure the constraints enforcement in the Google Cloud CLI](https://docs.cloud.google.com/resource-manager/docs/organization-policy/using-constraints#boolean-constraint).




To learn more about organization policies see the [Introduction to the Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).

### Configure availability of the Cloud Build legacy service account

To configure the availability of the Cloud Build legacy service account when you enable the Cloud Build API, Cloud Build will introduce the following boolean policy constraint:

  * Not enforced: `constraints/cloudbuild.disableCreateDefaultServiceAccount`. Allows the use of the Cloud Build legacy service account in new projects.

**Note:** Setting this to not enforced allows all projects within your organization to use the Cloud Build legacy service account, regardless of when the Cloud Build API was enabled for those projects. But you can avoid this by setting the constraint at the project level.
  * Enforced: `constraints/cloudbuild.disableCreateDefaultServiceAccount`. Disables the use of the Cloud Build legacy service account in new projects. This is the default value of the constraint.




This constraint only affects projects that run their first build after the change rolled out. If you decide to not enforce the policy constraint, the change is permanent for all the projects that run their first build when that configuration is active. You can't toggle off the availability of the Cloud Build legacy service account on a project where the service account was previously available. However, even if the service account is available, you can prevent users in your organization from using it, as described in the following section.

As with all org policies and constraints, you can set these policies at the organization level, or at the project level.

### Configure the default service account for an organization

To configure which default service account is used in an organization, Cloud Build is introducing two new policy [boolean constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#boolean_constraint):

  * `constraints/cloudbuild.useBuildServiceAccount`: Configure the use of the Cloud Build legacy service account.
  * `constraints/cloudbuild.useComputeServiceAccount`: Configure the use of the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account).



You can configure these policies independently from each other, but are most useful when the enforcement rules are combined in the following scenarios:

  * **Most secure option** : Use a [user-specified service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts) for both manually submitted builds and triggered builds. To do so, set the following constraints in your organization policy:

    * Not enforced: `constraints/cloudbuild.useBuildServiceAccount`
    * Not enforced: `constraints/cloudbuild.useComputeServiceAccount`
  * **Compute Engine default service account** : To use the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) for both manually submitted builds and triggered builds, set the following constraints in your organization policy:

    * Not enforced: `constraints/cloudbuild.useBuildServiceAccount`
    * Enforced: `constraints/cloudbuild.useComputeServiceAccount`
  * **Cloud Build legacy service account** : If you understand the security trade-offs involved, set the following constraints in your organization policy:

    * Not Enforced: `constraints/cloudbuild.disableCreateDefaultServiceAccount`
    * Not enforced: `constraints/cloudbuild.useComputeServiceAccount`
    * Enforced: `constraints/cloudbuild.useBuildServiceAccount`
  * **Legacy and Compute Engine default service accounts** : Continue using the Cloud Build legacy service account for projects that have enabled the Cloud Build API before the change, and start using the [Compute Engine default service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account) for new projects. If you understand the security trade-offs involved, set the following constraints in your organization policy:

    * Enforced: `constraints/cloudbuild.disableCreateDefaultServiceAccount`
    * Enforced: `constraints/cloudbuild.useComputeServiceAccount`
    * Enforced: `constraints/cloudbuild.useBuildServiceAccount`

**Warning:** Don't delete the Compute Engine default service account. If you don't want to use it as your default service account, disallow it using organization policies. Deleting this service account is irreversible and can have unintended consequences either on Cloud Build or other services. If you accidentally delete the Compute Engine service account, you can try to [undelete it](https://docs.cloud.google.com/iam/docs/service-accounts-delete-undelete#undeleting) within 30 days.

### Guidelines for IAM roles

The `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy prevents certain default service accounts from being granted the [Editor role](https://docs.cloud.google.com/iam/docs/roles-overview) (`roles/editor`) on creation. This policy is enabled in organizations as of May 3, 2024, and applies to Compute Engine and App Engine default service accounts created on or after May 3, 2024. We recommend that you leave this policy enabled as the Editor role is very broad and grants more permissions than are needed for most use cases.

This organization policy doesn't apply to the Cloud Build legacy service account as that service account doesn't have the Editor role granted by default. However, the Cloud Build legacy service account does have the [Cloud Build Service Account role](https://docs.cloud.google.com/build/docs/securing-builds/service-accounts#service-account-roles) (`roles/cloudbuild.builds.builder`) granted by default, which also has a broad range of permissions. If you use the Cloud Build legacy service account, we recommend that you verify whether the Cloud Build Service Account role is necessary for your use case, or whether you could replace it with a role that has fewer permissions.

For more information, see [Restricting IAM service account usage](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#boolean_constraints) and [Use IAM securely](https://docs.cloud.google.com/iam/docs/using-iam-securely).

## Get the current default service account for a project

To determine which service account Cloud Build is using as default for a project, you can use Google Cloud CLI or the Cloud Build API:

###  gcloud CLI 

Run the following command to get the default service account for the current project:
    
    
    gcloud builds get-default-service-account

###  Cloud Build API 

Use [cURL](http://curl.haxx.se/) to call the Cloud Build API:
    
    
    curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         https://cloudbuild.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/defaultServiceAccount

Replace the placeholder values with the following:

  * `PROJECT_ID`: the ID of the project.
  * `REGION`: one of the [supported regions](https://docs.cloud.google.com/build/docs/locations).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
