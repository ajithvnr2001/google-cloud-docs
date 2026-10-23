---
url: https://docs.cloud.google.com/run/docs/configuring/workerpools/sandboxes/
title: Configure sandboxes for worker pools \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:03:21.967373+00:00
---

# Configure sandboxes for worker pools  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/workerpools/sandboxes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure sandboxes for worker pools Stay organized with collections  Save and categorize content based on your preferences. 

**Preview — Cloud Run sandboxes**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Cloud Run sandboxes provide a fast, secure, and isolated environment to run agent workflows within your worker pool, execute untrusted payloads, and handle events in isolation. Sandboxes are highly optimized for latency and run within the same instance as your container, sharing its allocated CPU and memory.

This page describes how to configure sandboxes on your container. For details about writing code to interact with the sandbox using the CLI, see [Code execution in Cloud Run](https://docs.cloud.google.com/run/docs/code-execution).

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

  6. [Install and initialize](https://docs.cloud.google.com/sdk/docs) the gcloud CLI. 
  7. Deploy a Cloud Run [worker pool](https://docs.cloud.google.com/run/docs/deploy-worker-pools). 



## Required roles

To get the permissions that you need to configure and deploy Cloud Run worker pools, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run worker pool
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run worker pool interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/workerpools/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Enable sandboxes

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

To enable sandboxes in Cloud Run worker pools, use the Google Cloud CLI or a YAML configuration:

###  gcloud 

To deploy or update the worker pool, specify the `--sandbox-launcher` flag:

  * To deploy a new worker pool, run the following command:
        
        gcloud beta run worker-pools deploy WORKER_POOL --image IMAGE_URL --sandbox-launcher

Replace the following:

    * WORKER_POOL: the name of your Cloud Run worker pool.
    * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
  * To update an existing worker pool, run the following command:
        
        gcloud beta run worker-pools update WORKER_POOL --sandbox-launcher




###  YAML 

  1. If you are creating a new worker pool, skip this step. If you are updating an existing worker pool, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

  2. Update your YAML file to include the `sandboxLauncher` attribute set to `true` inside your container configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: WorkerPool
         metadata:
           name: WORKER_POOL
           annotations:
             run.googleapis.com/launch-stage: BETA
         spec:
           template:
             spec:
               containers:
               - name: CONTAINER
                 image: IMAGE_URL
                 sandboxLauncher: true
         

Replace the following:

     * WORKER_POOL: the name of your Cloud Run worker pool.
     * CONTAINER: the name of your container.
     * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
  3. Create or update the worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml

The `gcloud run worker-pools replace` command defaults to using `worker-pool.yaml` file if present.




Sandboxes share the CPU and memory allocated to the host container. Make sure your main container's CPU and memory limits can accommodate both your application and any active sandboxes that you run at the same time.

## Disable sandboxes

To disable the ability to launch a sandbox in your worker pool, use the Google Cloud CLI or a YAML configuration:

###  gcloud 

Update the worker pool using the `--no-sandbox-launcher` flag by running the following command:
    
    
    gcloud beta run worker-pools update WORKER_POOL --no-sandbox-launcher

Replace WORKER_POOL with the name of your worker pool.

###  YAML 

  1. If you are creating a new worker pool, skip this step. If you are updating an existing worker pool, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

  2. Update your YAML file to remove the `sandboxLauncher` attribute inside your container configuration:
         
         apiVersion: run.googleapis.com/v1
         kind: WorkerPool
         metadata:
           name: WORKER_POOL
         spec:
           template:
             spec:
               containers:
               - name: CONTAINER
                 image: IMAGE_URL
         

Replace the following:

     * WORKER_POOL: the name of your Cloud Run worker pool.
     * CONTAINER: the name of your container.
     * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
  3. Create or update the worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml

The `gcloud run worker-pools replace` command defaults to using `worker-pool.yaml` file if present.




## View sandbox settings

To view the current sandbox settings for your Cloud Run worker pool:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Worker pools** page:

[Go to Cloud Run worker pools](https://console.cloud.google.com/run/worker-pools)

  2. Click the worker pool to open its **Worker pools details** page.

  3. Click the **Revisions** tab.

  4. In the **Containers** tab, locate the **Sandbox launcher** setting to view whether sandboxed containers are enabled or disabled.




###  gcloud 

  1. Use the following command:
         
         gcloud run worker-pools describe WORKER_POOL

Replace WORKER_POOL with the name of your worker pool.

  2. To verify that sandboxed containers are enabled, locate the `sandboxLauncher: true` attribute in the returned configuration.




To run untrusted code in a sandbox from your worker pool, see [Code execution in Cloud Run](https://docs.cloud.google.com/run/docs/code-execution).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
