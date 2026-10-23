---
url: https://docs.cloud.google.com/knowledge-catalog/docs/manage-data-quality-rules-as-code/
title: Manage data quality rules as code with Terraform, Cloud Build, and GitHub \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:50:49.644642+00:00
---

# Manage data quality rules as code with Terraform, Cloud Build, and GitHub  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/manage-data-quality-rules-as-code/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Manage data quality rules as code with Terraform, Cloud Build, and GitHub Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial explains how to manage Knowledge Catalog (formerly Dataplex Universal Catalog) [data quality rules](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview) as code with Terraform, Cloud Build, and GitHub.

Many different options for data quality rules as code are available to define and measure the quality of your data.

If you have different versions of a dataset for multiple environments, such as `dev` and `prod` environments, Terraform provides a reliable way to assign data quality rules to environment-specific versions of datasets.

Version control also is an important [DevOps](https://cloud.google.com/devops/) best practice. Managing your data quality rules as code provides you with versions of your data quality rules that are available in your GitHub history. Terraform can also save its [state](https://www.terraform.io/docs/state/) to Cloud Storage, which can store earlier versions of the state file. Terraform uses state to map resources to your configuration, keep track of metadata, and improve performance for large infrastructures.

For more information about Terraform, Cloud Build, and auto data quality rules, see [Overview of Terraform on Google Cloud](https://docs.cloud.google.com/docs/terraform/terraform-overview), [Cloud Build](https://docs.cloud.google.com/build), and [Auto data quality overview](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview).

## Architecture

To understand how this tutorial uses Cloud Build for managing Terraform executions, consider the following architecture diagram. Note that it uses GitHub branches—`dev` and `prod`—to represent actual environments.

**Note:** For simplicity, this tutorial implements only `dev` and `prod` environments. You can extend this behavior to deploy to more environments and to create projects under your [organization hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) if needed.

![Architecture using Cloud Build to manage Terraform executions in dev and prod environments.](https://docs.cloud.google.com/static/knowledge-catalog/images/manage-data-quality-rules-as-code.svg)

The process starts when you push Terraform code to either the `dev` or `prod` branch. In this scenario, Cloud Build triggers and then applies Terraform manifests to achieve the state you want in the respective environment. On the other hand, when you push Terraform code to any other branch—for example, to a feature branch—Cloud Build runs to execute `terraform plan`, but nothing is applied to any environment.

Ideally, either developers or operators must make infrastructure proposals to [non-protected branches](https://help.github.com/en/articles/about-protected-branches) and then submit them through [pull requests](https://help.github.com/en/articles/about-pull-requests). The [Cloud Build GitHub app](https://github.com/marketplace/google-cloud-build), discussed later in this tutorial, automatically triggers the build jobs and links the `terraform plan` reports to these pull requests. This way, you can discuss and review the potential changes with collaborators and add follow-up commits before changes are merged into the base branch.

If no concerns are raised, you must first merge the changes to the `dev` branch. This merge triggers an infrastructure deployment to the `dev` environment, allowing you to test this environment. After you have tested and are confident about what was deployed, you must merge the `dev` branch into the `prod` branch to trigger the infrastructure installation to the production environment.

## Objectives

  * Set up your GitHub repository.
  * Configure Terraform to store state in a Cloud Storage bucket.
  * Grant permissions to your Cloud Build service account.
  * Connect Cloud Build to your GitHub repository.
  * Establish Knowledge Catalog data quality rules.
  * Change your environment configuration in a feature branch and test.
  * Promote changes to the development environment.
  * Promote changes to the production environment.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [BigQuery](https://cloud.google.com/bigquery/pricing)
  * [Cloud Build](https://docs.cloud.google.com/build/pricing)
  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)
  * [Compute Engine](https://docs.cloud.google.com/compute/pricing)
  * [Knowledge Catalog](https://docs.cloud.google.com/dataplex/pricing)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  7. In Cloud Shell, get the ID of the project you just selected: 
         
         gcloud config get-value project

If this command doesn't return the project ID, configure Cloud Shell to use your project. Replace `PROJECT_ID` with your project ID. 
         
         gcloud config set project PROJECT_ID

  8. Enable the required APIs: 
         
         gcloud services enable bigquery.googleapis.com cloudbuild.googleapis.com compute.googleapis.com dataplex.googleapis.com

This step might take a few minutes to finish. 
  9. If you've never used Git in Cloud Shell, configure it with your name and email address: 
         
         git config --global user.email "YOUR_EMAIL_ADDRESS"
         git config --global user.name "YOUR_NAME"
         

Git uses this information to identify you as the author of the commits that you create in Cloud Shell.



## Set up your GitHub repository

In this tutorial, you use a single Git repository to define your cloud infrastructure. You orchestrate this infrastructure by having different branches corresponding to different environments:

  * The `dev` branch contains the latest changes that are applied to the development environment.
  * The `prod` branch contains the latest changes that are applied to the production environment.



With this infrastructure, you can always reference the repository to know what configuration is expected in each environment and to propose new changes by first merging them into the `dev` environment. You then promote the changes by merging the `dev` branch into the subsequent `prod` branch.

To get started, fork the [terraform-google-dataplex-auto-data-quality](https://github.com/GoogleCloudPlatform/terraform-google-dataplex-auto-data-quality.git) repository.

  1. On GitHub, navigate to <https://github.com/GoogleCloudPlatform/terraform-google-dataplex-auto-data-quality.git>.

  2. Click **Fork**.

Now you have a copy of the `terraform-google-dataplex-auto-data-quality` repository with source files.

  3. In Cloud Shell, clone the following forked repository:
         
         cd ~
         git clone https://github.com/GITHUB_USERNAME/terraform-google-dataplex-auto-data-quality.git
         cd ~/terraform-google-dataplex-auto-data-quality
         

Replace the following:

     * GITHUB_USERNAME: your GitHub username
  4. Create `dev` and `prod` branches:
         
         git checkout -b prod
         git checkout -b dev
         




The code in this repository is structured as follows:

  * The `environments/` folder contains subfolders that represent environments, such as `dev` and `prod`, which provide logical separation between workloads at different stages of maturity, development and production, respectively.

  * The `modules/` folder contains inline Terraform modules. These modules represent logical groupings of related resources and are used to share code across different environments. The `modules/deploy/` module here represents a template for a deployment and is reused for different deployment environments.

  * Within `modules/deploy/`:

    * The `rule/` folder contains `yaml` files containing data quality rules. One file represents a set of data quality rules for one table. This file is used in `dev` and `prod` environments.

    * The `schemas/` folder contains the table schema for the BigQuery table deployed in this infrastructure.

    * The `bigquery.tf` file contains the configuration for BigQuery tables created in this deployment.

    * The `dataplex.tf` file contains a Knowledge Catalog data scan for data quality. This file is used in conjunction to `rules_file_parsing.tf` to read data quality rules from a `yaml` file into the environment.

  * The `cloudbuild.yaml` file is a build configuration file that contains instructions for Cloud Build, such as how to perform tasks based on a set of steps. This file specifies a conditional execution depending on the branch Cloud Build is fetching the code from, for example:

    * For `dev` and `prod` branches, the following steps are executed:

      1. `terraform init`
      2. `terraform plan`
      3. `terraform apply`
    * For any other branch, the following steps are executed:

      1. `terraform init` for all `environments` subfolders
      2. `terraform plan` for all `environments` subfolders



To ensure that the changes being proposed are appropriate for every environment, `terraform init` and `terraform plan` are run for all environments. Before merging the pull request, you can review the plans to make sure that access isn't being granted to an unauthorized entity, for example.

## Configure Terraform to store state in Cloud Storage buckets

By default, Terraform stores [state](https://www.terraform.io/docs/state/) locally in a file named `terraform.tfstate`. This default configuration can make Terraform usage difficult for teams, especially when many users run Terraform at the same time and each machine has its own understanding of the current infrastructure.

To help you avoid such issues, this section configures a [remote state](https://www.terraform.io/docs/state/remote.html) that points to a Cloud Storage bucket. Remote state is a feature of [backends](https://www.terraform.io/docs/backends) and, in this tutorial, is configured in the `backend.tf` file.
    
    
    # Copyright 2024 Google LLC
    #
    # Licensed under the Apache License, Version 2.0 (the "License");
    # you may not use this file except in compliance with the License.
    # You may obtain a copy of the License at
    #
    #     https://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing, software
    # distributed under the License is distributed on an "AS IS" BASIS,
    # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    # See the License for the specific language governing permissions and
    # limitations under the License.
    
    terraform {
      backend "gcs" {
        bucket = "PROJECT_ID-tfstate-dev"
      }
    }
    

A separate `backend.tf` file exists in each of the `dev` and `prod` environments. It is considered best practice to use a different Cloud Storage bucket for each environment.

In the following steps, you create two Cloud Storage buckets for `dev` and `prod` and change a few files to point to your new buckets and your Google Cloud project.

  1. In Cloud Shell, create the two Cloud Storage buckets:
         
         DEV_BUCKET=gs://PROJECT_ID-tfstate-dev
         gcloud storage buckets create ${DEV_BUCKET}
         
         PROD_BUCKET=gs://PROJECT_ID-tfstate-prod
         gcloud storage buckets create ${PROD_BUCKET}
         

  2. To keep the history of your deployments, enable [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning):
         
         gcloud storage buckets update ${DEV_BUCKET} --versioning
         gcloud storage buckets update ${PROD_BUCKET} --versioning
         

Enabling object versioning increases [storage costs](https://cloud.google.com/storage/pricing), which you can mitigate by configuring [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) to delete old state versions.

  3. In each environment, in the `main.tf` and `backend.tf` files , replace `PROJECT_ID` with the project ID:
         
         cd ~/terraform-google-dataplex-auto-data-quality
         sed -i s/PROJECT_ID/PROJECT_ID/g environments/*/main.tf
         sed -i s/PROJECT_ID/PROJECT_ID/g environments/*/backend.tf
         

On OS X or macOS, you might need to add two quotation marks (`""`) after `sed -i`, as follows:
         
         cd ~/solutions-terraform-cloudbuild-gitops
         sed -i "" s/PROJECT_ID/PROJECT_ID/g environments/*/main.tf
         sed -i "" s/PROJECT_ID/PROJECT_ID/g environments/*/backend.tf
         

  4. Check whether all files were updated:
         
         git status
         

The following is a sample output:
         
         On branch dev
         Your branch is up-to-date with 'origin/dev'.
         Changes not staged for commit:
          (use "git add <file>..." to update what will be committed)
          (use "git checkout -- <file>..." to discard changes in working directory)
                modified:   environments/dev/backend.tf
                modified:   environments/dev/main.tf
                modified:   environments/prod/backend.tf
                modified:   environments/prod/main.tf
         no changes added to commit (use "git add" and/or "git commit -a")
         

  5. Commit and push your changes:
         
         git add --all
         git commit -m "Update project IDs and buckets"
         git push origin dev
         

Depending on your GitHub configuration, you must authenticate to push the preceding changes.




## Grant permissions to your Cloud Build service account

To allow [Cloud Build service account](https://docs.cloud.google.com/build/docs/securing-builds/set-service-account-permissions) to run Terraform scripts with the goal of managing Google Cloud resources, you need to grant it appropriate access to your project. For simplicity, [project editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) access is granted in this tutorial. But when the project editor role has a wide-range permission, in production environments, you must follow your company's IT security best practices, usually providing [least-privileged access](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilege).

  1. In Cloud Shell, retrieve the email for your project's Cloud Build service account:
         
         CLOUDBUILD_SA="$(gcloud projects describe $PROJECT_ID \
             --format 'value(projectNumber)')@cloudbuild.gserviceaccount.com"
         

  2. Grant the required access to your Cloud Build service account:
         
         gcloud projects add-iam-policy-binding $PROJECT_ID \
             --member serviceAccount:$CLOUDBUILD_SA --role roles/editor
         




## Directly connect Cloud Build to your GitHub repository

This section describes you how to install the [Cloud Build GitHub app](https://github.com/marketplace/google-cloud-build). This installation lets you connect your GitHub repository with your Google Cloud project so that Cloud Build can automatically apply your Terraform manifests each time you create a new branch or push code to GitHub.

The following steps provide instructions for installing the app only for the `terraform-google-dataplex-auto-data-quality` repository, but you can choose to install the app for more or all of your repositories.

  1. In GitHub Marketplace, go to the [Cloud Build app page](https://github.com/marketplace/google-cloud-build).

     * If this is your first time configuring an app in GitHub: Click **Setup with Google Cloud Build** at the bottom of the page. Then click **Grant this app access to your GitHub account**.
     * If this is not the first time configuring an app in GitHub: Click **Configure access**. The **Applications** page of your personal account opens.
  2. Click **Configure** in the Cloud Build row.

  3. Select **Only select repositories** , then select **`terraform-google-dataplex-auto-data-quality`** to connect to the repository.

  4. Click **Save** or **Install** —the button label changes depending on your workflow. You are redirected to Google Cloud to continue the installation.

  5. Sign in with your Google Cloud account. If requested, authorize Cloud Build integration with GitHub.

  6. On the **Cloud Build** page, select your project. A wizard appears.

  7. In the **Select repository** section, select your GitHub account and the **`terraform-google-dataplex-auto-data-quality`** repository.

  8. If you agree with the terms and conditions, select the checkbox, then click **Connect**.

  9. In the **Create a trigger** section, click **Create a trigger** :

     1. Add a trigger name, such as `push-to-branch`. Note this trigger name because you will need it later.
     2. In the **Event** section, select **Push to a branch**.
     3. In the **Source** section, select `.*` in the **Branch** field.
     4. Click **Create**.



The Cloud Build GitHub app is configured, and your GitHub repository is linked to your Google Cloud project. Changes to the GitHub repository trigger Cloud Build executions, which report the results back to GitHub by using [GitHub Checks](https://developer.github.com/v3/checks/).

## Change your environment configuration in a new feature branch

You have most of your environment configured. Make necessary code changes in your local environment:

  1. On GitHub, navigate to the main page of your forked repository.
         
         https://github.com/YOUR_GITHUB_USERNAME/terraform-google-dataplex-auto-data-quality
         

  2. Make sure you are on the `dev` branch.

  3. To open the file for editing, go to the `modules/deploy/dataplex.tf` file.

  4. On line 19, change the label `the_environment` to `environment`.

  5. Add a commit message at the bottom of the page, such as "modifying label", and select **Create a new branch for this commit and start a pull request**.

  6. Click **Propose changes**.

  7. On the following page, click **Create pull request** to open a new pull request with your change to the `dev` branch.

After your pull request is open, a Cloud Build job is automatically initiated.

  8. Click **Show all checks** and wait for the check to become green. **Don't merge your pull request yet.** Merging is done in a later step of the tutorial.

  9. Click **Details** to see more information, including the output of the `terraform plan` at **View more details on Google Cloud Build** link.




Note that the Cloud Build job ran the pipeline defined in the `cloudbuild.yaml` file. This pipeline has different behaviors depending on the branch being fetched. The build checks whether the `$BRANCH_NAME` variable matches any environment folder. If so, Cloud Build executes `terraform plan` for that environment. Otherwise, Cloud Build executes `terraform plan` for all environments to make sure that the proposed change is appropriate for all of them. If any of these plans fail to execute, the build fails.
    
    
    - id: 'tf plan'
      name: 'hashicorp/terraform:1.9.8'
      entrypoint: 'sh'
      args:
      - '-c'
      - |
          if [ -d "environments/$BRANCH_NAME/" ]; then
            cd environments/$BRANCH_NAME
            terraform plan
          else
            for dir in environments/*/
            do
              cd ${dir}
              env=${dir%*/}
              env=${env#*/}
              echo ""
              echo "*************** TERRAFORM PLAN ******************"
              echo "******* At environment: ${env} ********"
              echo "*************************************************"
              terraform plan || exit 1
              cd ../../
            done
          fi

Similarly, the `terraform apply` command runs for environment branches, but it is completely ignored in any other case. In this section, you have submitted a code change to a new branch, so no infrastructure deployments were applied to your Google Cloud project.
    
    
    - id: 'tf apply'
      name: 'hashicorp/terraform:1.9.8'
      entrypoint: 'sh'
      args:
      - '-c'
      - |
          if [ -d "environments/$BRANCH_NAME/" ]; then
            cd environments/$BRANCH_NAME
            terraform apply -auto-approve
          else
            echo "***************************** SKIPPING APPLYING *******************************"
            echo "Branch '$BRANCH_NAME' does not represent an official environment."
            echo "*******************************************************************************"
          fi

## Enforce Cloud Build execution success before merging branches

To make sure merges can be applied only when respective Cloud Build executions are successful, follow these steps:

  1. On GitHub, navigate to the main page of your forked repository.
         
         https://github.com/YOUR_GITHUB_USERNAME/terraform-google-dataplex-auto-data-quality
         

  2. Under your repository name, click **Settings**.

  3. In the left menu, click **Branches**.

  4. Under **Branch protection rules** , click **Add rule**.

  5. In **Branch name pattern** , type `dev`.

  6. In the **Protect matching branches** section, select **Require status checks to pass before merging**.

  7. Search for your Cloud Build trigger name created previously.

  8. Click **Create**.

  9. Repeat steps 3–7, setting **Branch name pattern** to `prod`.




This configuration is important to [protect](https://help.github.com/en/articles/about-protected-branches) both the `dev` and `prod` branches. Meaning, commits must first be pushed to another branch, and only then they can be merged to the protected branch. In this tutorial, the protection requires that the Cloud Build execution be successful for the merge to be allowed.

## Promote changes to the development environment

You have a pull request waiting to be merged. It's time to apply the state you want to your `dev` environment.

  1. On GitHub, navigate to the main page of your forked repository.
         
         https://github.com/YOUR_GITHUB_USERNAME/terraform-google-dataplex-auto-data-quality
         

  2. Under your repository name, click **Pull requests**.

  3. Click the pull request you just created.

  4. Click **Merge pull request** , and then click **Confirm merge**.

  5. Check that a new Cloud Build has been triggered:

[Go to the Cloud Build page](https://console.cloud.google.com/cloud-build/builds)

  6. Open the build and check the logs. It will show you all of the resources that Terraform is creating and managing.




## Promote changes to the production environment

Now that you have your development environment fully tested, you can promote your code for data quality rules to production.

  1. On GitHub, navigate to the main page of your forked repository.
         
         https://github.com/YOUR_GITHUB_USERNAME/terraform-google-dataplex-auto-data-quality
         

  2. Under your repository name, click **Pull requests**.

  3. Click **New pull request**.

  4. For the **base repository** , select your just-forked repository.

  5. For **base** , select `prod` from your own base repository. For **compare** , select `dev`.

  6. Click **Create pull request**.

  7. For **title** , enter a title such as `Changing label name`, and then click **Create pull request**.

  8. Review the proposed changes, including the `terraform plan` details from Cloud Build, and then click **Merge pull request**.

  9. Click **Confirm merge**.

  10. In the Google Cloud console, open the **Build History** page to see your changes being applied to the production environment:

[Go to the Cloud Build page](https://console.cloud.google.com/cloud-build/builds)




You have successfully configured data quality rules that are managed using Terraform and Cloud Build.

## Clean up

After you've finished the tutorial, clean up the resources you created on Google Cloud so you won't be billed for them in the future.

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



### Delete the GitHub repository

To avoid blocking new pull requests on your GitHub repository, you can delete your branch protection rules:

  1. In GitHub, navigate to the main page of your forked repository.
  2. Under your repository name, click **Settings**.
  3. In the left menu, click **Branches**.
  4. Under the **Branch protection rules** section, click the **Delete** button for both `dev` and `prod` rows.



Optionally, you can completely uninstall the Cloud Build app from GitHub:

  1. In GitHub, go to the [GitHub Applications page](https://github.com/settings/installations).

  2. In the **Installed GitHub Apps** tab, click **Configure** in the **Cloud Build** row. Then, in the **Danger zone** section, click the **Uninstall** button in the **Uninstall Google Cloud Builder** row.

At the top of the page, you see a message saying "You're all set. A job has been queued to uninstall Google Cloud Build."

  3. In the **Authorized GitHub Apps** tab, click the **Revoke** button in the **Google Cloud Build** row, then **I understand, revoke access**.




If you don't want to keep your GitHub repository, delete it:

  1. In GitHub, go to the main page of your forked repository.
  2. Under your repository name, click **Settings**.
  3. Go to **Danger Zone**.
  4. Click **Delete this repository** , and follow the confirmation steps.



## What's next

  * Learn about [auto data quality](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview).
  * Learn more about [DevOps and DevOps best practices](https://cloud.google.com/devops/).
  * Explore the [Cloud Foundation Toolkit](https://cloud.google.com/foundation-toolkit/) for more Terraform templates. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
