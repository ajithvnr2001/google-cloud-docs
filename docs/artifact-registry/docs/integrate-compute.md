---
url: https://docs.cloud.google.com/artifact-registry/docs/integrate-compute/
title: Deploying to Compute Engine \u00a0|\u00a0 Artifact Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:48:28.103936+00:00
---

# Deploying to Compute Engine  |  Artifact Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/artifact-registry/docs/integrate-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Artifact Registry ](https://docs.cloud.google.com/artifact-registry/docs)
  * [ Guides ](https://docs.cloud.google.com/artifact-registry/docs/overview)



Send feedback 

#  Deploying to Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine can pull containers directly from Artifact Registry repositories so you can run containerized workloads on virtual machine (VM) instances. You can configure service account roles and access scopes to control how VMs access or upload artifacts across projects.

## Required permissions

The Compute Engine service account needs access to Artifact Registry in order to pull container images.

Depending on your organization policy configuration, the default service account might automatically be granted the [Editor role](https://docs.cloud.google.com/iam/docs/roles-overview#basic) on your project. We strongly recommend that you disable the automatic role grant by [ enforcing the `iam.automaticIamGrantsForDefaultServiceAccounts` organization policy constraint](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants). If you created your organization after May 3, 2024, this constraint is enforced by default. 

If you disable the automatic role grant, you must decide which roles to grant to the default service accounts, and then [grant these roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) yourself. 

If the default service account already has the Editor role, we recommend that you replace the Editor role with less permissive roles.To safely modify the service account's roles, use [Policy Simulator](https://docs.cloud.google.com/policy-intelligence/docs/simulate-iam-policies) to see the impact of the change, and then [grant and revoke the appropriate roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

Some examples of required access scopes and required roles for different scenarios are as follows:

  * To pull container images from Artifact Registry repositories, you must grant the Compute Engine service account the Artifact Registry Reader role (`roles/artifactregistry.reader`). Additionally, ensure the `read-only` [access scope](https://docs.cloud.google.com/storage/docs/oauth-scopes) is set for Cloud Storage storage buckets.
  * You want the VM instance to upload to repositories. In this case, you must configure an [access scope](https://docs.cloud.google.com/storage/docs/oauth-scopes) with write access to storage: `read-write`, `cloud-platform`, or `full-control`.
  * The VM instance is in a different project than the repositories that you want to access. In the project with the repositories, [grant](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) the required permissions to the instance's service account.
  * The repositories are in the same project, but you don't want the default service account to have the same level of access across all repositories. In this case, you must grant the appropriate permissions at the repository level and revoke the Artifact Registry permissions at the project level.
  * The VM is associated with a custom service account. Ensure that the service account has the required permissions and access scope.
  * You are using custom roles to grant permissions and the custom role does not include the required Artifact Registry permissions. Add the required [permissions](https://docs.cloud.google.com/artifact-registry/docs/access-control#permissions) to the role.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
