---
url: https://docs.cloud.google.com/secure-source-manager/docs/configure-cicd-terraform-config-as-code/
title: Configure CI/CD to store terraform config-as-code \u00a0|\u00a0 Secure Source Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:32:34.254315+00:00
---

# Configure CI/CD to store terraform config-as-code  |  Secure Source Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-source-manager/docs/configure-cicd-terraform-config-as-code/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Secure Source Manager ](https://docs.cloud.google.com/secure-source-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-source-manager/docs/overview)



Send feedback 

#  Configure CI/CD to store terraform config-as-code Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial explains how to manage infrastructure as code with [Terraform](https://cloud.google.com/docs/terraform) and [Cloud Build](https://docs.cloud.google.com/build) using the popular GitOps methodology. The term _GitOps_ was first coined by Weaveworks, and its key concept is using a Git repository to store the environment state that you want. Terraform is a [HashiCorp](https://www.hashicorp.com/) open source tool that lets you predictably create, change, and improve your cloud infrastructure by using code. In this tutorial, you use [Cloud Build](https://docs.cloud.google.com/build), a Google Cloud continuous integration service, to automatically apply Terraform manifests to your environment.

This tutorial is for developers and operators who are looking for an elegant strategy to predictably make changes to infrastructure. The article assumes you are familiar with Google Cloud, and Linux.

The [State of DevOps](https://cloud.google.com/devops/) reports identified capabilities that drive software delivery performance. This tutorial will help you with the following capabilities:

  * [Version control](https://docs.cloud.google.com/solutions/devops/devops-tech-version-control)
  * [Continuous integration](https://docs.cloud.google.com/solutions/devops/devops-tech-continuous-integration)
  * [Continuous delivery](https://docs.cloud.google.com/solutions/devops/devops-tech-continuous-delivery)
  * [Continuous testing](https://docs.cloud.google.com/solutions/devops/devops-tech-test-automation)



## Architecture

This tutorial applies GitOps practices for managing Terraform executions. Note that it uses Secure Source Manager branches `dev` and `prod` to represent actual environments. These environments are defined by Virtual Private Cloud (VPC) networks `dev` and `prod`, respectively, within a Google Cloud project.

The process starts when you push Terraform code to either the `dev` or `prod` branch. In this scenario, Cloud Build triggers and then applies Terraform manifests to achieve the state you want in the respective environment. On the other hand, when you push Terraform code to any other branch—for example, to a feature branch — Cloud Build runs to execute `terraform plan`, but nothing is applied to any environment.

Ideally, either developers or operators must make infrastructure proposals to development or feature branches, and then submit them through [pull requests](https://docs.cloud.google.com/secure-source-manager/docs/work-with-issues-pull-requests#create_a_pull_request). This way, you can discuss and review the potential changes with collaborators and add follow-up commits before changes are merged into the base branch.

If no concerns are raised, you must first merge the changes to the `dev` branch. This merge triggers an infrastructure deployment to the `dev` environment, allowing you to test this environment. After you have tested and are confident about what was deployed, you must merge the `dev` branch into the `prod` branch to trigger the infrastructure installation to the production environment.

## Objectives

  * Set up your Secure Source Manager instance and repository.
  * Configure Terraform to store state in a Cloud Storage bucket.
  * Grant permissions to your Cloud Build service account.
  * Connect Cloud Build to your Secure Source Manager repository.
  * Change your environment configuration in a feature branch.
  * Promote changes to the development environment.
  * Promote changes to the production environment.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [Cloud Build](https://docs.cloud.google.com/build/pricing)
  * [Cloud Storage](https://docs.cloud.google.com/storage/pricing)
  * [Compute Engine](https://docs.cloud.google.com/compute/pricing)



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
         
         gcloud services enable cloudbuild.googleapis.com compute.googleapis.com securesourcemanager.googleapis.com

This step might take a few minutes to finish.
  9. If you've never used Git in Cloud Shell, configure it with your name and email address: 
         
         git config --global user.email "YOUR_EMAIL_ADDRESS"
         git config --global user.name "YOUR_NAME"
         

Git uses this information to identify you as the author of the commits that you create in Cloud Shell.



## Set up your Secure Source Manager repository

In this tutorial, you use a single Secure Source Manager repository to define your cloud infrastructure. You orchestrate this infrastructure by having different branches corresponding to different environments:

  * The `dev` branch contains the latest changes that are applied to the development environment.
  * The `prod` branch contains the latest changes that are applied to the production environment.
  * Feature branches similar to `feature_x` are used to make changes before pushing to the `dev` or `prod` branches.



With this infrastructure, you can always reference the repository to know what configuration is expected in each environment and to propose new changes by first merging them into the `dev` environment. You then promote the changes by merging the `dev` branch into the subsequent `prod` branch.

  1. [Create an empty Secure Source Manager repository](https://docs.cloud.google.com/secure-source-manager/docs/create-repository) \- don't initialize the repository.
  2. Add the Secure Source Manager authentication helper to your global `git config` by running the following command:
         
         git config --global credential.'https://*.*.sourcemanager.dev'.helper gcloud.sh
         

The authentication helper uses the gcloud CLI to fetch your Google Cloud credentials when using Git commands with Secure Source Manager.

  3. To re-authenticate after the initial credential setup, run the following gcloud CLI command:
         
         gcloud auth login
         

  4. Clone the [solutions-terraform-cloudbuild-gitops](https://github.com/GoogleCloudPlatform/solutions-terraform-cloudbuild-gitops.git) repository to your local shell or working environment:
         
         git clone https://github.com/GoogleCloudPlatform/solutions-terraform-cloudbuild-gitops.git
         

  5. Add your Secure Source Manager repository as an upstream.
         
         git remote add google HTTPS_REPO_URL
         

Where `HTTPS_REP_URL` is the HTTPS URL for your Secure Source Manager repository. You can find the URL at the top of your repository page in the Secure Source Manager web interface.

  6. Create and switch to your `dev` branch.
         
         git checkout dev
         

  7. Push the cloned repository to your repository with the following command:
         
         git push -u google --all
         

  8. Repeat the previous two steps for your `prod` branch.




The code in this repository is structured as follows:

  * The `environments/` folder contains subfolders that represent environments, such as `dev` and `prod`, which provide logical separation between workloads at different stages of maturity, development and production, respectively. Although it's a good practice to have these environments as similar as possible, each subfolder has its own Terraform configuration to ensure they can have unique settings as necessary.

  * The `modules/` folder contains inline Terraform modules. These modules represent logical groupings of related resources and are used to share code across different environments.

  * The `cloudbuild.yaml` file is a build configuration file that contains instructions for Cloud Build, such as how to perform tasks based on a set of steps. This file specifies a conditional execution depending on the branch Cloud Build is fetching the code from, for example:

    * For `dev` and `prod` branches, the following steps are executed:

      1. `terraform init`
      2. `terraform plan`
      3. `terraform apply`
    * For any other branch, the following steps are executed:

      1. `terraform init` for all `environments` subfolders
      2. `terraform plan` for all `environments` subfolders



To ensure that the changes being proposed are appropriate for every environment, `terraform init` and `terraform plan` are run for all `environments` subfolders. Before merging the pull request, you can review the plans to make sure that access isn't being granted to an unauthorized entity, for example.

## Modify the build configuration file

To make the sample build configuration file work with Secure Source Manager, you need to make the following edits:

  * Add a step to clone your repository.
  * Add a step to get the branch name and assign it to a variable.



Edit the build configuration file in the `dev` branch:

  1. Change to the `dev` branch:
         
         git checkout dev
         

  2. Open the `cloudbuild.yaml` file and replace the contents with the following:
         
         # Copyright 2019 Google LLC
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
         
         
         steps:
         - id: 'clone repository'
           name: 'gcr.io/cloud-builders/git'
           args:
           - clone
           - '${_REPO_URL}'
           - .
         - id: 'branch name'
           name: gcr.io/cloud-builders/git
           entrypoint: 'sh'
           args:
           - '-c'
           - |
               branch=$(basename "$_REF")
               git checkout ${branch}
               echo "***********************"
               git branch --show-current
               echo "***********************"
         
         - id: 'tf init'
           name: 'hashicorp/terraform:1.0.0'
           entrypoint: 'sh'
           args:
           - '-c'
           - |
            branch=$(basename "$_REF")
               if [ -d "environments/${branch}/" ]; then
                 cd environments/${branch}
                 terraform init
               else
                 for dir in environments/*/
                 do
                   cd ${dir}
                   env=${dir%*/}
                   env=${env#*/}
                   echo ""
                   echo "*************** TERRAFORM INIT ******************"
                   echo "******* At environment: ${env} ********"
                   echo "*************************************************"
                   terraform init || exit 1
                   cd ../../
                 done
               fi
         
         - id: 'tf plan'
           name: 'hashicorp/terraform:1.0.0'
           entrypoint: 'sh'
           args:
           - '-c'
           - |
               branch=$(basename "$_REF")
               if [ -d "environments/${branch}/" ]; then
                 cd environments/${branch}
                 terraform plan
               else
                 for dir in environments/*/
                 do
                   cd ${dir}
                   env=${dir%*/}
                   env=${env#*/}
                   echo ""
                   echo "*************** TERRAFOM PLAN ******************"
                   echo "******* At environment: ${env} ********"
                   echo "*************************************************"
                   terraform plan || exit 1
                   cd ../../
                 done
               fi
         
         - id: 'tf apply'
           name: 'hashicorp/terraform:1.0.0'
           entrypoint: 'sh'
           args:
           - '-c'
           - |
               branch=$(basename "$_REF")
               if [ -d "environments/${branch}/" ]; then
                 cd environments/${branch}
                 terraform apply -auto-approve
               else
                 echo "***************************** SKIPPING APPLYING *******************************"
                 echo "Branch '${branch}' does not represent an official environment."
                 echo "*******************************************************************************"
               fi

  3. Check that the file is modified.
         
         git status
         

  4. Commit and push your changes:
         
         git add --all
         git commit -m "Modify build config file."
         git push google dev
         

  5. Open a pull request to quickly promote your changes to the `prod` branch.

     1. In the Secure Source Manager web interface, navigate to your repository.
     2. Click the **Pull requests** tab.
     3. Click **New pull request**.
     4. In the **merge into:** field, select the `prod` branch.
     5. In the **pull from:** field, select the `dev` branch.
     6. Review the changes, then click **New pull request**.
     7. Click **Create pull request**.
     8. Click **Merge pull request**.
     9. Click **Merge pull request** again.

The changes are merged into your `prod` branch.




## Configuring Terraform to store state in a Cloud Storage bucket

By default, Terraform stores [state](https://www.terraform.io/docs/state/) locally in a file named `terraform.tfstate`. This default configuration can make Terraform usage difficult for teams, especially when many users run Terraform at the same time and each machine has its own understanding of the current infrastructure.

To help you avoid such issues, this section configures a [remote state](https://www.terraform.io/docs/state/remote.html) that points to a Cloud Storage bucket. Remote state is a feature of [backends](https://www.terraform.io/docs/backends) and, in this tutorial, is configured in the `backend.tf` files—for example:
    
    
    # Copyright 2019 Google LLC
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
        bucket = "PROJECT_ID-tfstate"
        prefix = "env/dev"
      }
    }
    

In the following steps, you create a Cloud Storage bucket and change a few files to point to your new bucket and your Google Cloud project.

  1. In Cloud Shell, create the Cloud Storage bucket:
         
         PROJECT_ID=$(gcloud config get-value project)
         gcloud storage buckets create gs://${PROJECT_ID}-tfstate
         

  2. Enable [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning) to keep the history of your deployments:
         
         gcloud storage buckets update gs://${PROJECT_ID}-tfstate --versioning
         

Enabling Object Versioning increases [storage costs](https://cloud.google.com/storage/pricing), which you can mitigate by configuring [Object Lifecycle Management](https://docs.cloud.google.com/storage/docs/lifecycle) to delete earlier state versions.

  3. Create a new `cloud-storage-bucket` branch to make your changes in:
         
         cd ~/solutions-terraform-cloudbuild-gitops
         git checkout -b cloud-storage-bucket
         

  4. Replace the `PROJECT_ID` placeholder with the project ID in both the `terraform.tfvars` and `backend.tf` files:
         
         sed -i s/PROJECT_ID/$PROJECT_ID/g environments/*/terraform.tfvars
         sed -i s/PROJECT_ID/$PROJECT_ID/g environments/*/backend.tf
         

On OS X or macOS, you might need to add two quotation marks (`""`) after `sed -i`, as follows:
         
         sed -i "" s/PROJECT_ID/$PROJECT_ID/g environments/*/terraform.tfvars
         sed -i "" s/PROJECT_ID/$PROJECT_ID/g environments/*/backend.tf
         

  5. Check whether all files were updated:
         
         git status
         

The output looks like this:
         
         On branch cloud-storage-bucket
         Changes not staged for commit:
         (use "git add ..." to update what will be committed)
         (use "git restore ..." to discard changes in working directory)
                modified:   environments/dev/backend.tf
                modified:   environments/dev/terraform.tfvars
                modified:   environments/prod/backend.tf
                modified:   environments/prod/terraform.tfvars
         no changes added to commit (use "git add" and/or "git commit -a")
         

  6. Commit and push your changes:
         
         git add --all
         git commit -m "Update project IDs and buckets"
         git push google -u cloud-storage-bucket
         

Your new `cloud-storage-bucket` branch is pushed to your repository.

  7. Merge your `cloud-storage-bucket` changes into your `dev` and `prod` branches by opening and submitting merge requests for each branch.




## Grant permissions to your Cloud Build service account

To allow [Cloud Build service account](https://docs.cloud.google.com/build/docs/securing-builds/set-service-account-permissions) to run Terraform scripts with the goal of managing Google Cloud resources, you need to grant it appropriate access to your project. For simplicity, [project editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) access is granted in this tutorial. For production environments, follow your company's IT security best practices, usually by providing [least-privileged access](https://docs.cloud.google.com/iam/docs/using-iam-securely#least_privilegey).

**Note:** The Cloud Build default service account used to run builds is being changed. As a best practice, we recommend that you [specify your own service account](https://docs.cloud.google.com/build/docs/securing-builds/configure-user-specified-service-accounts) to run your builds. For more information, see [Cloud Build service account change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates).

  1. To find the Cloud Build service account email, from the Cloud Build page, navigate to **Settings**.

[Go to Cloud Build settings](https://console.cloud.google.com/cloud-build/settings)

  2. Copy the value of the **Service account email**.

  3. Grant the required access to your Cloud Build service account:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --member serviceAccount:CLOUDBUILD_SA --role roles/editor
         

Replace the following:

     * PROJECT_ID with your project ID.
     * CLOUDBUILD_SA with the Cloud Build service account email.



## Connect to Cloud Build

To trigger Cloud Build on a push to any branch, set up a Secure Source Manager webhook. The build configuration file will check the the branch name to determine if changes need to be made to the `dev` or `prod` environments.

  1. [Enable and set up Cloud Build](https://docs.cloud.google.com/build/docs/set-up) in your project.

  2. Open the **Triggers** page in the Google Cloud console.

[Open the Triggers page](https://console.cloud.google.com/cloud-build/triggers)

  3. Select your project from the project selector drop-down menu at the top of the page.

  4. Click **Open**.

  5. Click **Create trigger**.

  6. Enter the following trigger settings:

     * **Name** : `trigger-on-push`

     * **Region** : select the [region](https://docs.cloud.google.com/build/docs/locations) for your trigger. If the build configuration file associated with your trigger specifies a [private pool](https://docs.cloud.google.com/build/docs/private-pools/private-pools-overview), the region you select for your trigger must match the region of the private pool.

**Note:** If using a private pool, you must assign external IPs to allow your private pool to access the public internet. For more details, see [Creating a new private pool](https://docs.cloud.google.com/build/docs/private-pools/create-manage-private-pools#creating_a_new_private_pool).

If you select `global` as your region, Cloud Build uses the region specified in your build configuration file to run your build. This can either be the region of the private pool, if you specify a private pool in your build configuration file, or the global default pool if you don't specify a private pool.

     * **Description** (optional): Enter a description for your trigger.

     * **Event** : Select **Webhook event** as the repository event to invoke the trigger.

If Secret Manager is not installed, you are prompted to enable the Secret Manager.

     * **Webhook URL** : select one of the following:

       * **Use a new secret** if you want to generate a new secret using Cloud Build. Click **Create secret** to create your secret.
       * **Use an existing secret or create your own** if you want to use an existing secret. Enter the secret and version in the drop down selection boxes.

If you use an existing secret, you might need to manually grant the [Secret Manager Secret Accessor](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) role to the Cloud Build service agent `service-PROJECT_NUMBER@gcp-sa-cloudbuild.iam.gserviceaccount.com`.

To learn more, see [Granting a role to the Cloud Build service agent](https://docs.cloud.google.com/build/docs/securing-builds/configure-access-for-cloud-build-service-account#service-agent-permissions).

  7. Click **Show URL preview** and record the URL. You need this URL to set up the webhook in Secure Source Manager.

     * **Configuration** : for **Type** select **Cloud Build configuration file (YAML or JSON)** and for **Location** , select **Inline**.
  8. Click the **Open Editor** button to edit your build configuration file.

  9. Copy the contents of your `cloudbuild.yaml` file into the editor.

As discussed previously, this pipeline has different behaviors depending on the branch being fetched. The build checks whether the `${branch}` variable matches any environment folder. If so, Cloud Build executes `terraform plan` for that environment. Otherwise, Cloud Build executes `terraform plan` for all environments to make sure that the proposed change is appropriate for all of them. If any of these plans fail to execute, the build fails.
         
         - id: 'tf plan'
           name: 'hashicorp/terraform:1.0.0'
           entrypoint: 'sh'
           args:
           - '-c'
           - |
               branch=$(basename "$_REF")
               if [ -d "environments/${branch}/" ]; then
                 cd environments/${branch}
                 terraform plan
               else
                 for dir in environments/*/
                 do
                   cd ${dir}
                   env=${dir%*/}
                   env=${env#*/}
                   echo ""
                   echo "*************** TERRAFOM PLAN ******************"
                   echo "******* At environment: ${env} ********"
                   echo "*************************************************"
                   terraform plan || exit 1
                   cd ../../
                 done
               fi

The `terraform apply` command runs for environment branches, but it is completely ignored in any other case.

  10. Click **\+ Add variable** and add the following two substitution variables:

     * **Variable** : `_REPO_URL`, **Value** :`$(body.repository.clone_url)`
     * **Variable** : `_REF`, **Value** :`$(body.ref)`
  11. Click **Create**.




## Set up a webhook in Secure Source Manager

Create a webhook to trigger builds on pushes to your `dev` or `prod` branches.

  1. In the Secure Source Manager web interface, navigate to the repository you want to create a webhook for.
  2. Click **Settings**.
  3. Click **Webhooks** , and then click **Add webhook**.
  4. In the **Hook ID** field, enter an ID for the webhook.

**Note:** Hook IDs must follow the [resource naming convention](https://google.aip.dev/122#resource-id-segments). They must include only lower case letters, numbers, or dashes, must begin with a letter, and cannot be changed after creating the webhook.
  5. In the **Target URL** field, enter the Webhook URL you copied when you set up a webhook trigger in Cloud Build.

To find the Webhook URL:

     1. Open the **Triggers** page in the Google Cloud console.

[Open the Triggers page](https://console.cloud.google.com/cloud-build/triggers)

     2. Click your trigger.

     3. In the **Webhook URL** section, click **Show URL preview** and copy URL.

  6. The Webhook URL contains your key and secret values entered when you created your Cloud Build trigger. To prevent leaking these values, remove them from the end of the target URL and copy to the **Sensitive Query String** field.

To locate your key and secret in your webhook URL, look for the text starting with `key=`

For example, given the following URL: `https://cloudbuild.googleapis.com/v1/projects/my-project/triggers/test-trigger:webhook?key=eitIfKhYnv0LrkdsyHqIros8fbsheKRIslfsdngf&secret=Hello%20Secret%20Manager`

Copy and remove the portion starting with the question mark `?key=...` from the **Target URL** field. Then remove the initial question mark, move the remaining portion `key=...` to the **Sensitive Query String** field.

  7. Click **Add webhook**.

  8. The webhook is displayed in the **Webhooks** page.

**Note:** When you add or edit a webhook, the length of the `Sensitive Query String` might be inconsistent with the entered one, which is expected as placeholder strings are used to ensure security.



## Change your environment configuration in a new feature branch

  1. Make sure you are in the `dev` branch:
         
         cd ~/solutions-terraform-cloudbuild-gitops
         git checkout dev
         

  2. Pull the latest changes:
         
         git pull
         

  3. Create a `bug-fix` branch to change the environment configuration.
         
         git checkout -b bug-fix
         

  4. Open `modules/firewall/main.tf` to edit.

  5. On line 30, fix the `"http-server2"` typo in `target_tags` field.

The value must be `"http-server"`.

  6. Commit and push your changes:
         
         git add --all
         git commit -m "Fix typo."
         git push google -u bug-fix
         

  7. Open the Cloud Build **History** page in the Google Cloud console:

[Open the History page](https://console.cloud.google.com/cloud-build/builds)

  8. Click the **Build** to see more information, including the output of the `terraform plan`.




Note that the Cloud Build job ran the pipeline defined in the `cloudbuild.yaml` file. As discussed previously, this pipeline has different behaviors depending on the branch being fetched. The build checks whether the `${branch}` variable matches any environment folder. If so, Cloud Build executes `terraform plan` for that environment. Otherwise, Cloud Build executes `terraform plan` for all environments to make sure that the proposed change is appropriate for all of them. If any of these plans fail to execute, the build fails.
    
    
    - id: 'tf plan'
      name: 'hashicorp/terraform:1.0.0'
      entrypoint: 'sh'
      args:
      - '-c'
      - |
          branch=$(basename "$_REF")
          if [ -d "environments/${branch}/" ]; then
            cd environments/${branch}
            terraform plan
          else
            for dir in environments/*/
            do
              cd ${dir}
              env=${dir%*/}
              env=${env#*/}
              echo ""
              echo "*************** TERRAFOM PLAN ******************"
              echo "******* At environment: ${env} ********"
              echo "*************************************************"
              terraform plan || exit 1
              cd ../../
            done
          fi

Similarly, the `terraform apply` command runs for environment branches, but it is completely ignored in any other case. In this section, you have submitted a code change to a new branch, so no infrastructure deployments were applied to your Google Cloud project.

\- id: 'tf apply' name: 'hashicorp/terraform:1.0.0' entrypoint: 'sh' args: \- '-c' \- | branch=$(basename "$_REF") if [ -d "environments/${branch}/" ]; then cd environments/${branch} terraform apply -auto-approve else echo "***************************** SKIPPING APPLYING *******************************" echo "Branch '${branch}' does not represent an official environment." echo "*******************************************************************************" fi 

## Promoting changes to the development environment

It's time to apply the state you want to your `dev` environment.

  1. In the Secure Source Manager web interface, navigate to your repository.
  2. Click the **New pull request**
  3. In the **merge into:** field, select your `dev` branch.
  4. In the **pull from:** field, select your `bug-fix` branch.
  5. Click **New pull request**.
  6. Click **Create pull request**.
  7. Click **Merge pull request** , and then click **Merge pull request** again.
  8. Check that a new Cloud Build has been triggered:

[Go to the Cloud Build page](https://console.cloud.google.com/cloud-build/builds)

  9. Open the build and check the logs.

When the build finishes, you see something like this:
         
         Step #3 - "tf apply": external_ip = EXTERNAL_IP_VALUE
         Step #3 - "tf apply": firewall_rule = dev-allow-http
         Step #3 - "tf apply": instance_name = dev-apache2-instance
         Step #3 - "tf apply": network = dev
         Step #3 - "tf apply": subnet = dev-subnet-01
         

  10. Copy `EXTERNAL_IP_VALUE` and open the address in a web browser.
         
         http://EXTERNAL_IP_VALUE
         

This provisioning might take a few seconds to boot the VM and to propagate the firewall rule. Eventually, you see **Environment: dev** in the web browser.

  11. Navigate to Cloud Storage:

[Go to the Cloud Storage page](https://console.cloud.google.com/storage/buckets)

  12. Select your project.

  13. Click your Terraform state storage bucket. The bucket name looks like the following:
         
         PROJECT_ID-tfstate
         

  14. Click **env** , and then **dev** to view your Terraform state file.




## Promoting changes to the production environment

Now that you have your development environment fully tested, you can promote your infrastructure code to production.

  1. In the Secure Source Manager web interface, navigate to your repository.
  2. Click the **Pull requests** tab.
  3. Click **New pull request**.
  4. For the **merge into:** , select your repository `prod` branch.
  5. For **pull from:** , select your repository `dev` branch.
  6. Click **New pull request**.
  7. For **title** , enter a title such as "Promoting networking changes", and then click **Create pull request**.
  8. Review the proposed changes, and then click **Merge pull request**.

The date and repository URL are added in the comment field.

  9. Click **Merge pull request** again to confirm.

  10. In the Google Cloud console, open the **Build History** page to see your changes being applied to the production environment:

[Go to the Cloud Build page](https://console.cloud.google.com/cloud-build/builds)

  11. Wait for the build to finish, and then check the logs.

At the end of the logs, you see something like this:
         
         Step #3 - "tf apply": external_ip = EXTERNAL_IP_VALUE
         Step #3 - "tf apply": firewall_rule = prod-allow-http
         Step #3 - "tf apply": instance_name = prod-apache2-instance
         Step #3 - "tf apply": network = prod
         Step #3 - "tf apply": subnet = prod-subnet-01
         

  12. Copy `EXTERNAL_IP_VALUE` and open the address in a web browser.
         
         http://EXTERNAL_IP_VALUE
         

This provisioning might take a few seconds to boot the VM and to propagate the firewall rule. Eventually, you see **Environment: prod** in the web browser.

  13. Navigate to Cloud Storage:

[Go to the Cloud Storage page](https://console.cloud.google.com/storage/buckets)

  14. Select your project.

  15. Click your Terraform state storage bucket. The bucket name looks like the following:
         
         PROJECT_ID-tfstate
         

  16. Click **env** , and then **prod** to view your Terraform state file.




You have successfully configured a serverless infrastructure-as-code pipeline on Cloud Build. In the future, you might want to try the following:

  * Add deployments for separate use cases.
  * Create additional environments to reflect your needs.
  * Use a project per environment instead of a VPC per environment.



## Clean up

After you've finished the tutorial, clean up the resources you created on Google Cloud so you won't be billed for them in the future.

### Deleting the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Consider using [Cloud Cloud Foundation Toolkit templates](https://cloud.google.com/foundation-toolkit/) to quickly build a repeatable enterprise-ready foundation in Google Cloud.
  * Watch [Repeatable Google Cloud Environments at Scale With Cloud Build Infra-As-Code Pipelines](https://www.youtube.com/watch?v=3vfXQxWJazM) from Next' 19 about the GitOps workflow described in this tutorial.
  * Check out the [GitOps-style continuous delivery with Cloud Build](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/gitops-cloud-build) tutorial.
  * Take a look at more advanced Cloud Build features: [Configuring the order of build steps](https://docs.cloud.google.com/build/docs/configuring-builds/configure-build-step-order), [Building, testing, and deploying artifacts](https://docs.cloud.google.com/build/docs/configuring-builds/build-test-deploy-artifacts), and [Creating custom build steps](https://docs.cloud.google.com/build/docs/create-custom-build-steps).
  * Check out the blog on [Ensuring scale and compliance of your Terraform Deployment with Cloud Build](https://cloud.google.com/blog/products/devops-sre/terraform-gitops-with-google-cloud-build-and-storage).
  * Read our resources about [DevOps](https://cloud.google.com/devops/).
  * Learn more about the DevOps capabilities related to this tutorial: 
    * [Version control](https://docs.cloud.google.com/solutions/devops/devops-tech-version-control)
    * [Continuous integration](https://docs.cloud.google.com/solutions/devops/devops-tech-continuous-integration)
    * [Continuous delivery](https://docs.cloud.google.com/solutions/devops/devops-tech-continuous-delivery)
    * [Continuous testing](https://docs.cloud.google.com/solutions/devops/devops-tech-test-automation)
  * Take the [DevOps quick check](https://www.devops-research.com/quickcheck.html) to understand where you stand in comparison with the rest of the industry.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
