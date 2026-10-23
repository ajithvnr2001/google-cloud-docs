---
url: https://docs.cloud.google.com/run/docs/configuring/jobs/environment-variables/
title: Configure environment variables for jobs \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:45:29.224888+00:00
---

# Configure environment variables for jobs  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/jobs/environment-variables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure environment variables for jobs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure environment variables for your Cloud Run job.

When you set [environment variables](https://en.wikipedia.org/wiki/Environment_variable), they are injected into the container and are accessible to your code. Environment variables are set as key/value pairs.

**Caution:** Don't use environment variables to store and consume secrets, because environment variables are visible to anyone with project Viewer permissions or greater. Instead, use Secret Manager with Cloud Run as described in the [Using secrets](https://docs.cloud.google.com/run/docs/configuring/jobs/secrets) page.

## Reserved names

The environment variables defined in the [container runtime contract](https://docs.cloud.google.com/run/docs/reference/container-contract#env-vars) are reserved and cannot be set. 

## Maximum number of environment variables

Note that you can set a maximum of 1000 environment variables per container for each Cloud Run job.

## Required roles

To get the permissions that you need to configure Cloud Run jobs, ask your administrator to grant you the following IAM roles on job: 

  * Cloud Run Developer (`roles/run.developer`) - the Cloud Run job 
  * Service Account User (`roles/iam.serviceAccountUser`) - the service identity 



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run job interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Warning:** If your Cloud Run job uses [service identity](https://docs.cloud.google.com/run/docs/securing/service-identity) to authenticate access to Google Cloud APIs, never set `GOOGLE_APPLICATION_CREDENTIALS` as an environment variable on a Cloud Run job. Always configure a [user-managed service account](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity) instead.

## Set environment variables

You can set environment variables for new and existing jobs. Note that the `--set-env-vars` flag is a destructive action that deletes previously set environment variables not included in the new list of environment variables.

You can set environment variables using the Google Cloud console, the gcloud CLI, or a YAML file:

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Jobs** from the Cloud Run navigation menu:

     1. If you are creating a new job, click **Deploy container** to fill out the initial job settings page.

     2. If you are configuring an existing job, select the job, then click **View and edit job configuration**.

  3. Click **Containers, Connections, Security** to expand the job properties page.

  4. Click the **Variables & Secrets** tab.

  5. Click **Add Variable**.

  6. Specify the name and value that you want for the variable in the **Name** and **Value** fields. For more information on how to set multiple environment variables or escape special characters, see Set multiple environment variables.

  7. Click **Create** or **Update**.




###  gcloud 

To specify environment variables when you create a job, use the [`--set-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/deploy#--set-env-vars) flag:
    
    
    gcloud run jobs create JOB_NAME --image IMAGE_URL --set-env-vars KEY1=VALUE1,KEY2=VALUE2
    

Replace the following:

  * JOB_NAME: the name of your job.
  * KEY1=VALUE1,KEY2=VALUE2: comma-separated list of variable names and their values.
  * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.



For more information on how to set multiple environment variables or escape special characters, see Set multiple environment variables.

### YAML

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2.      1. Update the `name` and `value` attributes under `env` as shown under `containers:`:
    
    apiVersion: run.googleapis.com/v1
    kind: Job
    metadata:
      name: **JOB**
    spec:
      template:
        spec:
          template:
            spec:
              containers:
              - image: **IMAGE**
                env:
                - name: KEY-1
                  value: VALUE-1
                - name: KEY-N
                  value: VALUE-N

Replace KEY-1, VALUE-1 with the environment variable and value. Optionally add more variables and values as needed.

You can also specify more configuration such as environment variables or memory limits.

  3. Update the existing job configuration:
         
         gcloud run jobs replace job.yaml




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_job`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_job) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_job" "default" {
      name     = "JOB_NAME"
      location = "REGION"
    
      template {
        template {
          containers {
            image = "us-docker.pkg.dev/cloudrun/container/job"
            env {
              name = "KEY-1"
              value = "VALUE-1"
            }
            env {
              name = "KEY-N"
              value = "VALUE-N"
            }
          }
        }
      }
    }
    

Replace the following:

  * JOB_NAME: the name of your Cloud Run job.
  * REGION: the Google Cloud region. For example, `europe-west1`.
  * KEY-1: the environment variable.
  * VALUE-1: the value associated with the key.



Optionally add more `env` blocks to set additional environment variables.

### Set default environment variables in the container

You can use the [`ENV`](https://docs.docker.com/engine/reference/builder/#env) statement in a Dockerfile to set default values for environment variables:
    
    
    ENV KEY1=VALUE1,KEY2=VALUE2

### Order of precedence: container versus job variables

If you set a default environment variable in the container and also set an environment variable with the same name on the Cloud Run job, the value set on the job takes precedence.

## Set multiple environment variables

You can set multiple environment variables by using the `.env` file or the `--set-env-vars` flag.

### Set multiple environment variables using the `.env` file

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Jobs** from the Cloud Run navigation menu:

     1. If you are creating a new job, click **Deploy container** to fill out the initial job settings page.

     2. If you are configuring an existing job, select the job, then click **View and edit job configuration**.

  3. Click **Containers, Connections, Security** to expand the job properties page.

  4. Click the **Variables & Secrets** tab.

  5. Click **Add Variable**.

  6. In the **Name** field, paste the contents of your `.env` file. Cloud Run automatically populates the **Value** field and creates new variables for each key-value pair you define in the `.env` file.

  7. Click **Create** or **Update**.




###  gcloud 

To specify multiple environment variables from the `.env` file, run the following command:
    
    
    gcloud run jobs create JOB_NAME --image=IMAGE_URL --env-vars-file=ENV_FILE_PATH
    

Replace the following:

  * JOB_NAME: the name of your Cloud Run job.
  * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
  * ENV_FILE_PATH: path to the `.env` file.



### Set multiple environment variables using the `--set-env-vars` flag

If you have multiple environment variables that cannot be listed in `KEY1=VALUE1,KEY2=VALUE2` format, you can repeat the `--set-env-vars` flag multiple times: 
    
    
       [...]
       --set-env-vars "KEY1=VALUE1" \
       --set-env-vars "KEY2=VALUE2" \
       --set-env-vars "KEY3=VALUE3"

### Escape comma characters

Because the comma character `,` is used to split environment variables, if your environment variable contains comma characters as values, you need to [escape](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping) those delimiters by specifying a different delimiter character, for example, `@`: 
    
    
    --set-env-vars "^@^KEY1=value1,value2,value3@KEY2=..."

## Update environment variables

You can update environment variables for existing jobs. This is a non-destructive approach that changes or adds environment variables, but doesn't delete previously set environment variables.

###  Console 

To update environment variables using the Google Cloud console:

  1. In the Google Cloud console, go to the Cloud Run **Jobs** page:

[Go to Cloud Run](https://console.cloud.google.com/run/jobs)

  2. Select your job from the list, and click **Edit and deploy new revision**.

  3. Click the **Container** tab.

  4. In the **Variables and secrets** tab, edit the **Name** or **Value** fields, and click **Done**.

  5. Click **Deploy**.




###  gcloud 

To update environment variables of an existing job, use the [`--update-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/update#--update-env-vars) flag:
    
    
    gcloud run jobs update JOB_NAME --update-env-vars KEY1=VALUE1,KEY2=VALUE2
    

Replace the following:

  * JOB_NAME: the name of your job.
  * KEY1=VALUE1,KEY2=VALUE2: comma-separated list of variable names and values.



## View environment variables settings

To view the current environment variables settings for your Cloud Run job, use the Google Cloud console or the Google Cloud CLI:

### Console

  1. In the Google Cloud console, go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Click the job to open the **Job details** page.

  3. Click **View and edit job configuration**.

  4. Locate the environment variables setting in the configuration details.




###  gcloud 

  1. Run the following command:
         
         gcloud run jobs describe JOB

  2. Locate the environment variables setting in the returned configuration.




## Delete environment variables

You can delete environment variables for existing jobs.

###  Console 

To delete environment variables using the Google Cloud console:

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/jobs)

  2. Select your job from the list, and click **Edit and deploy new revision**.

  3. Click the **Container** tab.

  4. In the **Variables and secrets** tab, move your cursor to the left of the **Value** field of the environment variable you are removing, to display the delete **Delete** icon, and click it.

  5. Click **Done**.

  6. Click **Deploy**.




###  gcloud 

To selectively remove environment variables of an existing job, use the [`--remove-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/update#--remove-env-vars) flag:
    
    
    gcloud run jobs update JOB_NAME --remove-env-vars KEY1,KEY2
    

Replace the following:

  * JOB_NAME: the name of your job.
  * KEY1,KEY2: comma-separated list of variable names.



Alternatively, clear all previously set environment variables with the [`--clear-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/update#--clear-env-vars) flag:
    
    
    gcloud run jobs update JOB_NAME --clear-env-vars
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 

  * ### Products and pricing

    * [ See all products ](https://cloud.google.com/products/)
    * [ Google Cloud pricing ](https://cloud.google.com/pricing/)
    * [ Google Cloud Marketplace ](https://cloud.google.com/marketplace/)
    * [ Contact sales ](https://cloud.google.com/contact/)
  * ### Support

    * [ Community forums ](https://discuss.google.dev/c/google-cloud/14/)
    * [ Support ](https://cloud.google.com/support-hub/)
    * [ Release Notes ](https://docs.cloud.google.com/release-notes)
    * [ System status ](https://status.cloud.google.com)
  * ### Resources

    * [ GitHub ](https://github.com/googlecloudPlatform/)
    * [ Getting Started with Google Cloud ](https://docs.cloud.google.com/docs/get-started/)
    * [ Code samples ](https://docs.cloud.google.com/docs/samples)
    * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture/)
    * [ Training and Certification ](https://cloud.google.com/learn/training/)
    * [ Builders Hub ](https://me.developers.google.com/)
  * ### Engage

    * [ Blog ](https://cloud.google.com/blog/)
    * [ Events ](https://cloud.google.com/events/)
    * [ X (Twitter) ](https://x.com/googlecloud)
    * [ Google Cloud on YouTube ](https://www.youtube.com/googlecloud)
    * [ Google Cloud Tech on YouTube ](https://www.youtube.com/googlecloudplatform)



[ ![Google Developers](https://www.gstatic.com/devrel-devsite/prod/v5a0f9ff8b593048661361a49e11ab98a8b1ac025e19e60e6189f2b56796f8a43/clouddocs/images/lockup-google-for-developers.svg)](https://developers.google.com/)

  * [ Android ](https://developer.android.com/)
  * [ Chrome ](https://developer.chrome.com/)
  * [ Firebase ](https://firebase.google.com/)
  * [ Google AI ](https://ai.google.com/)



  * [ About Google ](https://about.google/)
  * [ Privacy ](https://policies.google.com/privacy)
  * [ Site terms ](https://policies.google.com/terms?hl=en)
  * [ Google Cloud terms ](https://cloud.google.com/product-terms)
  * Manage cookies 
  * [ Our third decade of climate action: join us ](https://cloud.google.com/sustainability)
  * Sign up for the Google Cloud newsletter [ Subscribe ](https://cloud.google.com/newsletter/)



  * English
  * Deutsch
  * Español
  * Español – América Latina
  * Français
  * Indonesia
  * Italiano
  * Português
  * Português – Brasil
  * עברית
  * 中文 – 简体
  * 中文 – 繁體
  * 日本語
  * 한국어


