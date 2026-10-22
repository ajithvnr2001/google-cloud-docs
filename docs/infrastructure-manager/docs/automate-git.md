---
url: https://docs.cloud.google.com/infrastructure-manager/docs/automate-git/
title: Automate the deployment of Google Cloud resources \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:46.085997+00:00
---

# Automate the deployment of Google Cloud resources  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/automate-git/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Automate the deployment of Google Cloud resources Stay organized with collections  Save and categorize content based on your preferences. 

Connecting [Cloud Build triggers](https://docs.cloud.google.com/build/docs/triggers) with Infrastructure Manager lets you automate infrastructure deployments directly from your Git repositories. In this workflow, pull requests generate a [deployment preview](https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment), and merged commits automatically [create](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources) or [update the deployment](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment).

## Before you begin

  1. Ensure [Infra Manager is enabled](https://docs.cloud.google.com/infrastructure-manager/docs/enable-service).
  2. Ensure that you have the IAM permissions needed to create deployments: 
     * `roles/config.admin`
  3. Ensure you have a service account with the needed permissions. For details, see [Configure the service account](https://docs.cloud.google.com/infrastructure-manager/docs/configure-service-account).
  4. Identify the existing Git repository that has the Terraform configuration. When you set up the automation described on this page, this is the Terraform configuration that Infra Manager uses to update resources.
  5. Recommended: Set up [branch protection](https://docs.cloud.google.com/docs/terraform/resource-management/managing-infrastructure-as-code#enforcing_cloud_build_execution_success_before_merging_branches) for your Git repository.



## Automate the deployment of Google Cloud resources

**Caution:** Infra Manager does not perform data migration or ensure service continuity. For example, if a revision deletes or replaces a database, it is your responsibility to manage data migration. Creating a revision can cause unrecoverable data loss. Re-applying the previous revision will not restore the data.

The following steps describe the setup required to automate the preview and deployment of a Terraform configuration stored in a Git repository. A deployment of a Terraform configuration can be a revision to an existing deployment. Revisions might delete or replace provisioned Google Cloud resources.

When the setup is complete, a pull request in the Git repository causes Infra Manager to create a preview of the deployment. When a pull request is merged, then Infra Manager automatically deploys the Terraform configuration.

The `im_cloudbuild_workspace` module creates several resources, including:

  * A Cloud Build repository connection.
  * A Cloud Build trigger that is invoked when a pull request is created. This trigger causes Infra Manager to create a preview deployment using the Terraform configuration in the repository.
  * A Cloud Build trigger that is invoked when a pull request is merged with the Git repository. This trigger causes Infra Manager to create or update the deployment using the Terraform configuration in the repository.

**Note:** For more information about how you can modify the `im_cloudbuild_workspace` module's behavior, see the [`README`](https://github.com/terraform-google-modules/terraform-google-bootstrap/tree/master/modules/im_cloudbuild_workspace).

To automate Terraform configuration deployments when the repository is updated:

  1. Install the [Cloud Build GitHub App](https://github.com/apps/google-cloud-build) on your GitHub account or in an organization you own.
  2. [Create a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token).

Make sure to set your token to have no expiration date and select the following permissions when prompted in GitHub: `repo` and `read:user`. If your app is installed in an organization, make sure to also select the `read:org` permission.

After you generate your personal access token, save your generated token in a secure place. You use the generated token in the following steps.

**Note:** If you have an authentication token stored in a secret from a previously created connection, you can use that same secret for the new connection.
  3. Copy the `im_cloudbuild_workspace` module into the `main.tf` file within your Git repository:
         
         module "im-workspace" {
          source = "terraform-google-modules/bootstrap/google//modules/im_cloudbuild_workspace"
          version = "~> 7.0"
         
          project_id = "PROJECT_ID"
          deployment_id = "DEPLOYMENT_ID"
          im_deployment_repo_uri = "GIT_REPO"
          im_deployment_ref = "REF"
         
          github_app_installation_id = "GIT_APP_ID"
          github_personal_access_token = "TOKEN"
         }
         

Replace:

     * PROJECT_ID: the project ID where Infrastructure Manager runs.
     * DEPLOYMENT_ID: the deployment identifier that you specify. See [Deployment name](https://docs.cloud.google.com/infrastructure-manager/docs/deployments-revisions#deployment_name) for details about constraints on the deployment identifier.
     * GIT_REPO: the URI of the Git repository.
     * REF: the Git reference of the configuration. The reference is optional. If you don't specify the reference, the Git repository's default configured branch is used. 
     * GIT_APP_ID: Installation ID of the Cloud Build GitHub app used for pull and push request triggers.
     * TOKEN: Personal access token for a GitHub repository. If provided, creates a secret within Secret Manager.
  4. Create a deployment (or update your existing deployment) with the `im_cloudbuild_workspace` module:
         
         gcloud infra-manager deployments apply projects/PROJECT_ID/locations/LOCATION/deployments/DEPLOYMENT_ID \ 
            --service-account projects/SERVICE_ACCOUNT_PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT \
            --git-source-repo=GIT_REPO \
            --git-source-directory=DIRECTORY \
            --git-source-ref=REF
         

Replace: 

     * PROJECT_ID: the project ID where Infrastructure Manager runs.
     * LOCATION: the location where Infra Manager runs. See [Infrastructure Manager locations](https://docs.cloud.google.com/infrastructure-manager/docs/locations) for the list of locations.
     * DEPLOYMENT_ID: the deployment identifier that you specify. See [Deployment name](https://docs.cloud.google.com/infrastructure-manager/docs/deployments-revisions#deployment_name) for details about constraints on the deployment identifier.
     * SERVICE_ACCOUNT: the name of the service account you use to call Infra Manager.
     * SERVICE_ACCOUNT_PROJECT_ID is the project ID of the service account. It's common for this to be the same project where Infrastructure Manager runs.
     * GIT_REPO: the public Git repository.
     * DIRECTORY: the directory that has the Terraform configuration.
     * REF: the Git reference of the configuration. The reference is optional. If you don't specify the reference, the Git repository's default configured branch is used. 
  5. To confirm that your Git repository is connected correctly with Infra Manager, [create a pull request on your repository](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request).

To see the results of the validation of the forked Terraform configuration, [view the pull request in GitHub](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/reviewing-changes-in-pull-requests/commenting-on-a-pull-request#discovering-and-navigating-conversations).

**Note:** For more information about how you can modify the `im_cloudbuild_workspace` module's behavior, see the [`README`](https://github.com/terraform-google-modules/terraform-google-bootstrap/tree/master/modules/im_cloudbuild_workspace).



Now that this automation is set up, the Cloud Build triggers cause the following:

  * When a pull request is made to the repository, Infra Manager creates a preview deployment using the forked Terraform configuration stored in the Git repository.
  * When a pull request is merged into the repository, Infra Manager updates the deployment using the forked Terraform configuration stored in the Git repository.



## What's next

  * Use Cloud Build to [view build results for your build triggers](https://docs.cloud.google.com/build/docs/view-build-results-triggers).
  * [View resources deployed](https://docs.cloud.google.com/infrastructure-manager/docs/view-resources) with Infra Manager.
  * Monitor your Google Cloud resources with [Infrastructure Manager audit logging](https://docs.cloud.google.com/infrastructure-manager/docs/audit-logging).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
