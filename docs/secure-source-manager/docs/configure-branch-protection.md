---
url: https://docs.cloud.google.com/secure-source-manager/docs/configure-branch-protection/
title: Configure branch protection \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:51:07.448891+00:00
---

# Configure branch protection  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/configure-branch-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Configure branch protection Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to configure branch protection for Secure Source Manager repositories.

Branch protection lets repository administrators set rules to control who can make changes to branches, who needs to approve or review changes, and what conditions must be met before an approved change can be merged into a branch.

For more information about branch protection rules, see [Branch protection overview](https://docs.cloud.google.com/secure-source-manager/docs/branch-protection-overview).

## Before you begin

  1. [Create a Secure Source Manager instance](https://docs.cloud.google.com/secure-source-manager/docs/create-instance).
  2. [Create a Secure Source Manager repository](https://docs.cloud.google.com/secure-source-manager/docs/create-repository).



### Required roles

To get the permissions that you need to configure branch protection rules for a Secure Source Manager repository, ask your administrator to grant you the following IAM roles: 

  * [Secure Source Manager Instance Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.instanceAccessor) (`roles/securesourcemanager.instanceAccessor`) on the Secure Source Manager instance
  * [Secure Source Manager Repository Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoAdmin) (`roles/securesourcemanager.repoAdmin`) on the Secure Source Manager repository
  * To approve pull requests on protected branches in any repository in a Secure Source Manager instance: 
    * [Secure Source Manager Repository Pull Request Approver ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoPullRequestApprover) (`roles/securesourcemanager.repoPullRequestApprover`) on the Google Cloud project for the instance
    * [Secure Source Manager Repository Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`) on the Google Cloud project for the instance
  * To approve pull requests on protected branches in a single repository: 
    * [Secure Source Manager Repository Pull Request Approver ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoPullRequestApprover) (`roles/securesourcemanager.repoPullRequestApprover`) on the repository
    * [Secure Source Manager Repository Writer ](https://docs.cloud.google.com/iam/docs/roles-permissions/securesourcemanager#securesourcemanager.repoWriter) (`roles/securesourcemanager.repoWriter`) on the repository



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For information on granting Secure Source Manager roles, see [Access control with IAM](https://docs.cloud.google.com/secure-source-manager/docs/access-control) and [Grant users instance access](https://docs.cloud.google.com/secure-source-manager/docs/grant-users-instance-access).

## Create a branch protection rule

### Console

To create a new branch protection rule, do the following:

  1. In the Secure Source Manager web interface, select the repository you want to protect with a branch protection rule.
  2. From the repository page, click **Settings**.
  3. Click the **Branch rule** tab.
  4. Click **Add branch rule**.
  5. In the **Branch rule ID** field, enter a name for the branch rule.

Branch rule IDs are restricted to lower-case letters, numbers, and hyphens. The first character must be a letter, and the last character must be a letter or a number. Branch rule IDs have a 63 character maximum.

  6. In the **Branch filter** field, enter the name of the branch you want the rule to apply to, or if you want the rule to apply to all branches, enter `.*`. Full regular expression matching is not supported.

Enabled branch rule filters must be unique to their repository. Users can have multiple disabled branch rule filters. For example, you can't have two enabled branch rules in a single repository with the branch filter `main`.

When multiple rules are applicable for a branch, the branch rule with a specific branch name as the branch filter will override the wildcard rule. For example, a branch rule with branch filter `main` will override a branch rule with the branch filter `.*`. Rules are not combined.

  7. In the **Branch protection rule details** section, specify the requirements for your branch rule from the following options:

     * **Require a pull request before merging** : if enabled, direct commits to the branch will be blocked. A pull request must be opened before merging into the protected branch.

**Note:** You can't apply this rule to all branches using `.*`, because that would prevent pushing directly to all branches, even new branches.
     * **Required number of reviewers** : specify the number of reviewers required to approve in order to merge the pull request.

     * **Required number of approvers** : specify the number of approvers required to approve in order to merge the pull request.

Reviewers and approvers are users with specific IAM roles. To learn which roles are required for reviewers and approvers, see [Branch protection overview](https://docs.cloud.google.com/secure-source-manager/docs/branch-protection-overview).

     * **Block merge on stale reviews and approvals** : if enabled, a review or approval is removed if new commits are pushed to the pull request after the review or approval is granted.

     * **Require conversation resolution before merging** : if enabled, all code comments and request change reviews must be resolved before merging.

     * **Require linear history** : if enabled, pull requests that would create a non-linear Git history can't be merged.

     * **Require status checks** : if enabled, the selected build status checks must be successful before a pull request can be merged. You must configure triggers in your [triggers file](https://docs.cloud.google.com/secure-source-manager/docs/triggers-file-schema) before you can select them as status checks for branch protection.

  8. To save the branch rule, click **Submit**.




The **Branch rules** tab is displayed, with your new branch rule listed. 

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 

To create a new branch protection rule with Terraform, use the [`google_secure_source_manager_branch_rule`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/secure_source_manager_branch_rule) resource. 

The following example configuration creates a branch protection rule for the `main` branch.

Before using the sample, replace the following:

  * BRANCH_RULE_ID: the ID of the branch protection rule.
  * PROJECT_ID: the project ID.
  * LOCATION: the location of the repository.
  * REPOSITORY_ID: the ID of the repository.
  * BRANCH_NAME_PATTERN: the branch name or regex pattern, such as `main`.


    
    
    resource "google_secure_source_manager_branch_rule" "default" {
      branch_rule_id = "BRANCH_RULE_ID"
      project = "PROJECT_ID"
      location = "LOCATION"
      repository_id = "REPOSITORY_ID"
      include_pattern = "BRANCH_NAME_PATTERN"
      minimum_approvals_count   = 2
      minimum_reviews_count     = 2
      require_comments_resolved = true
      require_linear_history    = true
      require_pull_request      = true
      disabled = false
      allow_stale_reviews = false
    }
    

## Modify a branch protection rule

To modify a branch protection rule, do the following:

  1. In the Secure Source Manager web interface, select the repository with the branch protection rule you want to modify.
  2. From the repository page, click **Settings**.
  3. Click the **Branch rules** tab.
  4. Click the name of the branch rule you want to modify.
  5. Edit the branch protection rule.
  6. Click **Update**.



The branch protection rule is updated.

## Delete a branch protection rule

To delete a branch protection rule, do the following:

  1. In the Secure Source Manager web interface, select the repository that you want to remove the branch rule from.
  2. From the repository page, click **Settings.**
  3. Click the **Branch rule** tab.
  4. In the row of the rule you want to delete, click the **Delete** ![delete](https://docs.cloud.google.com/secure-source-manager/images/delete-icon.png) icon.
  5. In the **Remove branch rule** confirmation screen, click **Yes**.



The branch protection rule is deleted.

## What's next

  * Read the [Branch protection overview](https://docs.cloud.google.com/secure-source-manager/docs/branch-protection-overview).
  * Learn how to automate builds by following the steps in [Connect to Cloud Build](https://docs.cloud.google.com/secure-source-manager/docs/connect-cloud-build).
  * Learn how to [check the status of automated builds](https://docs.cloud.google.com/secure-source-manager/docs/create-triggers-file#view-build-status).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
