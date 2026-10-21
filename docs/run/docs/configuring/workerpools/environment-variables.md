---
url: https://docs.cloud.google.com/run/docs/configuring/workerpools/environment-variables/
title: Configure environment variables for worker pools \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:52.790132+00:00
---

# Configure environment variables for worker pools  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/workerpools/environment-variables/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure environment variables for worker pools Stay organized with collections  Save and categorize content based on your preferences. 

Environment variables let you customize container runtime behavior and pass dynamic configuration settings to your Cloud Run worker pools without modifying application code. 

## Required roles

To get the permissions that you need to configure and deploy Cloud Run worker pools, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run worker pool
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run worker pool interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/workerpools/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Warning:** If your Cloud Run worker pool uses [service identity](https://docs.cloud.google.com/run/docs/securing/service-identity) to authenticate access to Google Cloud APIs, never set `GOOGLE_APPLICATION_CREDENTIALS` as an environment variable on a Cloud Run worker pool. Always configure a [user-managed service account](https://docs.cloud.google.com/run/docs/configuring/workerpool/service-identity) instead.

## Set environment variables

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

You can set environment variables for a Cloud Run worker pool using the Google Cloud console, the Google Cloud CLI, YAML, or Terraform:

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Worker pools** from the Cloud Run navigation menu:

     1. If you are configuring an existing worker pool, click the worker pool, then click **Edit and deploy new revision**.

     2. If you are configuring a new worker pool, click **Deploy container** and then fill out the initial worker pool page. Then click **Containers, Networking, Security** to expand the worker pools configuration page.

  3. Click the **Variables & Secrets** tab.

  4. Click **Add variable** to add a new environment variable.

     1. In the **Name** field, enter the name of the environment variable.
     2. In the **Value** field, enter the value of the environment variable.

For more information on how to set multiple environment variables or escape special characters, see Set multiple environment variables.

     3. Click **Done**.

  5. Click **Create** or **Deploy**.




###  gcloud 

To specify environment variables while deploying your worker pool, use the [`--set-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/deploy#--set-env-vars) flag:
    
    
    gcloud run worker-pools deploy WORKER_POOL --image IMAGE_URL --set-env-vars KEY1=VALUE1,KEY2=VALUE2
    

Replace the following:

  * WORKER_POOL: the name of your worker pool
  * KEY1=VALUE1,KEY2=VALUE2: the comma-separated list of variable names and values
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`



For more information on how to set multiple environment variables or escape special characters, see Set multiple environment variables.

### YAML

  1. If you are creating a new worker pool, skip this step. If you are updating an existing worker pool, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

  2. The following example contains the YAML configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: WorkerPool
         metadata:
           name: WORKER_POOL
         spec:
           template:
             spec:
               containers:
               - name:
                 image: IMAGE_URL
                 env:
                 - name: NAME
                   value: VALUE
                 - name: NAME2
                   value: VALUE2

Replace the following:

     * WORKER_POOL: the name of your Cloud Run worker pool.
     * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
     * NAME and VALUE: the name and values of the environment variables.
  3. Create or update the worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml

The `gcloud run worker-pools replace` command defaults to using `worker-pool.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).
    
    
    resource "google_cloud_run_v2_worker_pool" "default" {
      name     = "WORKER_POOL"
      location = "REGION"
    
      template {
        containers {
          image = "IMAGE_URL"
          env {
            name  = "KEY1"
            value = "VALUE1"
          }
          env {
            name  = "KEY2"
            value = "VALUE2"
          }
        }
      }
    }
    

Replace the following:

  * WORKER_POOL: the name of the worker pool.
  * REGION: the Google Cloud region—for example, `europe-west1`
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
  * KEY1 and VALUE1: the environment variable and value. Optionally add more variables and values as needed.



### Set default environment variables in the container

You can use the [`ENV`](https://docs.docker.com/engine/reference/builder/#env) statement in a Dockerfile to set default values for environment variables:
    
    
    ENV KEY1=VALUE1,KEY2=VALUE2

### Order of precedence: container versus worker pool variables

If you set a default environment variable in the container and also set an environment variable with the same name on the Cloud Run worker pool, the value set on the worker pool takes precedence.

## Set multiple environment variables

You can set multiple environment variables by using the `.env` file or the `--set-env-vars` flag.

### Set multiple environment variables using the `.env` file

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Worker pools** from the Cloud Run navigation menu:

     1. If you are configuring an existing worker pool, click the worker pool, then click **Edit and deploy new revision**.

     2. If you are configuring a new worker pool, click **Deploy container** and then fill out the initial worker pool page. Then click **Containers, Networking, Security** to expand the worker pools configuration page.

  3. Click the **Variables & Secrets** tab.

  4. Click **Add variable**.

  5. In the **Name** field, paste the contents of your `.env` file. Cloud Run automatically populates the **Value** field and creates new variables for each key-value pair you define in the `.env` file.

  6. Click **Done**.

  7. Click **Create** or **Deploy**.




###  gcloud 

To specify multiple environment variables from the `.env` file, run the following command:
    
    
    gcloud run worker-pools deploy WORKER_POOL --image IMAGE_URL --env-vars-file=ENV_FILE_PATH
    

Replace the following:

  * WORKER_POOL: the name of the worker pool.
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
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

You can update runtime environment variables for existing worker pools. This is a non-destructive approach that changes or adds runtime environment variables, but doesn't delete them.

You can update environment variables in Google Cloud console, the Google Cloud CLI, YAML, or Terraform:

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Select **Worker pools** from the menu, and click the worker pool you are updating, then click **Edit and deploy new revision**.

  3. Click **Containers, Networking, Security** to expand the worker pools configuration page.

  4. Click the **Variables & Secrets** tab.

  5. Locate the environment variable you want to update, then specify a different name for the variable, or a different value in the **Name** and **Value** fields.

  6. Click **Deploy**.




###  gcloud 

To update environment variables of an existing worker pool, use the [`--update-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/deploy#--update-env-vars) flag:
    
    
    gcloud run worker-pools update WORKER_POOL --update-env-vars KEY1=VALUE1,KEY2=VALUE2
    

Replace the following:

  * WORKER_POOL: the name of your worker pool
  * KEY1=VALUE1,KEY2=VALUE2: the comma-separated list of variable names and values



### YAML

  1. Download the worker pool [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

  2. Edit the name and value variables.

  3. Update the worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml




### Terraform

To update environment variables of an existing worker pool, open the `main.tf` file corresponding to the worker pool and edit the name and value variables. Then, run the command to apply the Terraform configuration.

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## Delete environment variables

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Select **Worker pools** from the menu, and click the worker pool you are updating, then click **Edit and deploy new revision**.

  3. Click **Containers, Networking, Security** to expand the worker pools configuration page.

  4. Click the **Variables & Secrets** tab.

  5. Locate the environment variable you want to delete and click the trash icon at the right of the **Value** field to delete the environment variable.

  6. Click **Deploy**.




###  gcloud 

To selectively remove environment variables from an existing worker pool, use the [`--remove-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/deploy#--remove-env-vars) flag:
    
    
    gcloud run worker-pools update WORKER_POOL --remove-env-vars KEY1,KEY2
    

Replace the following:

  * WORKER_POOL: the name of your worker pool
  * KEY1,KEY2: the comma-separated list of variable names



Alternatively, clear all previously set environment variables with the [`--clear-env-vars`](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/deploy#--clear-env-vars) flag:
    
    
    gcloud run worker-pools update WORKER_POOL --clear-env-vars
    

Replace WORKER_POOL with the name of your worker pool.

## View environment variable configuration for the worker pool

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Click **Worker pools** to display the list of deployed worker pools.

  3. Click the worker pool you want to examine to display its details pane.

  4. Click the **Containers** tab to display worker pool container configuration.




## Sample code

For a code sample that shows how to access environment variables in your code, refer to [Handling sensitive configuration with Secret Manager](https://docs.cloud.google.com/run/docs/tutorials/identity-platform#secret-manager) in the End user authentication tutorial.

## What's next

You can use environment variables to set a [buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview) configuration. For language-specific details, see the buildpacks documentation for:

  * [Node.js](https://docs.cloud.google.com/docs/buildpacks/nodejs#environment_variables)
  * [Python](https://docs.cloud.google.com/docs/buildpacks/python#environment_variables)
  * [Go](https://docs.cloud.google.com/docs/buildpacks/go#environment_variables)
  * [Ruby](https://docs.cloud.google.com/docs/buildpacks/ruby#environment_variables)
  * [PHP](https://docs.cloud.google.com/docs/buildpacks/php#customizing_nginx_configurations)
  * [Java](https://docs.cloud.google.com/docs/buildpacks/java#configure_maven)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
