---
url: https://docs.cloud.google.com/run/docs/configuring/workerpools/containers/
title: Configure containers for worker pools \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:20.282847+00:00
---

# Configure containers for worker pools  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/workerpools/containers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure containers for worker pools Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure the entrypoint command, and arguments for a Cloud Run worker pool.

When Cloud Run starts a container, it runs the image's default entrypoint command and default command arguments. If you want to override the image's default entrypoint and command arguments, you can use the `command` and `args` fields in the container configuration. The `command` field specifies the actual command run by the container. The `args` field specifies the arguments passed to that command.

Note that you can have a maximum of 1000 arguments per container for each worker pool.

## Required roles

To get the permissions that you need to configure and deploy Cloud Run worker pools, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run worker pool
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run worker pool interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/workerpools/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure entrypoint and arguments

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

The specified container command and arguments override the default image `ENTRYPOINT` and `CMD`.

You can set entrypoint command and arguments for a Cloud Run worker pool using the Google Cloud console, the Google Cloud CLI, YAML, or Terraform:

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Worker pools** from the Cloud Run navigation menu:

     1. If you are configuring an existing worker pool, click the worker pool, then click **Edit and deploy new revision**.

     2. If you are configuring a new worker pool, click **Deploy container** and then fill out the initial worker pool page. Then click **Containers, Networking, Security** to expand the worker pools configuration page.

  3. Specify the command you want the container to run if you don't want to use the entry point command defined in the container image. Optionally, specify the arguments to the entrypoint command.

  4. Click **Create** or **Deploy**.




###  gcloud 

To [update the start command and arguments](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/update) for an existing service:
    
    
    gcloud run worker-pools update WORKER_POOL --command COMMAND --args ARG1,ARG-N

Replace the following:

  * WORKER_POOL: the name of the worker pool.
  * COMMAND: the command that the container starts with, if you are not using the default command.
  * ARG1: the argument you are sending to the container command. Use a comma-delimited list for more than one argument.



To specify entrypoint and arguments during [deployment](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/deploy) of a new or existing worker pool:
    
    
    gcloud run worker-pools deploy --image IMAGE_URL --command COMMAND --args ARG1,ARG-N

Replace `IMAGE_URL` with a reference to the container image that contains the worker pool, such as code>us-docker.pkg.dev/cloudrun/container/worker-pool:latest.

If you want to restore the container defaults for the entrypoint commands and arguments, supply empty strings as follows:
    
    
    gcloud run worker-pools deploy --image IMAGE_URL --command "" --args ""

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
               - name: CONTAINER_NAME
                 image: IMAGE_URL
                 command:
                 - COMMAND
                 args:
                 - ARG1
                 - ARG-N

Replace the following:

     * WORKER_POOL: the name of your Cloud Run worker pool.
     * CONTAINER_NAME: the name of the container.
     * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`
     * COMMAND: the command that the container is to start up with if you are not using the default command.
     * ARG1: the argument you are sending to the container command. If you use multiple arguments, specify each on its own line—for example, as shown, ARG-N.
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
          command = ["COMMAND"]
          args = ["ARG1", "ARG2"]
        }
      }
    }
    

Replace the following:

  * WORKER_POOL: the name of the worker pool.
  * REGION: the Google Cloud region—for example, `europe-west1`.
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.
  * COMMAND: the command that the container starts with, if you are not using the default command.
  * ARG1, ARG2: the argument(s) you are sending to the container command.



## Set a working directory

The working directory is where the container executes its commands and arguments. You can specify a custom working directory for the container process during deployment of a new or existing worker pool. If not specified, the container image's default working directory is used. To reset this field to its default, pass an empty string or remove the field.

For example:

###  gcloud 

To [update the working directory](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/update) for an existing worker pool:
    
    
    gcloud run worker-pools update WORKER_POOL --workdir WORKING_DIR

Replace the following:

  * WORKING_DIR: Container's working directory. If not specified, the container image's default is used. To reset this field to its default, pass an empty string `""`.



To specify the working directory during [deployment](https://docs.cloud.google.com/sdk/gcloud/reference/run/worker-pools/deploy) of a new or existing worker pool:
    
    
    gcloud run worker-pools deploy --image IMAGE_URL --workdir WORKING_DIR

Replace the following:

  * `IMAGE_URL` with a reference to the container image that contains the worker pool, such as code>us-docker.pkg.dev/cloudrun/container/worker-pool:latest.
  * WORKING_DIR: Container's working directory.



### YAML

  1. If you are creating a new worker pool, skip this step. If you are updating an existing worker pool, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run worker-pools describe WORKER_POOL --format export > worker-pool.yaml

  2. Update the `workingDir:` attribute:
         
         apiVersion: run.googleapis.com/v1
         kind: WorkerPool
         metadata:
           name: WORKER_POOL
         spec:
           template:
             spec:
               containers:
               - image: IMAGE_URL
                 workingDir: WORKING_DIR

Replace the following:

     * WORKER_POOL: the name of your Cloud Run worker pool.
     * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.
     * WORKING_DIR: (Optional) Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image.
  3. Create or update the worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml

The `gcloud run worker-pools replace` command defaults to using `worker-pool.yaml` file if present.




### Terraform

Add the following to a [`google_cloud_run_v2_worker_pool`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_worker_pool) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_worker_pool" "default" {
      provider = google-beta
      name     = "WORKER_POOL"
      location = "REGION"
    
      template {
        containers {
          image = "IMAGE_URL"
          working_dir = WORKING_DIR
        }
      }
    }
    

Replace the following:

  * WORKER_POOL with the name of your Cloud Run worker pool.
  * REGION with the Google Cloud region. For example, `europe-west1`.
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.
  * WORKING_DIR: (Optional) Container's working directory. If not specified, the container runtime's default will be used, which might be configured in the container image.



## Configure container start order for sidecar deployments

To specify the container start up order in a [sidecar deployment](https://docs.cloud.google.com/run/docs/deploy-worker-pools#sidecars), use the container dependencies feature. Specify any containers that have dependencies and list the containers they depend on, so those containers are started first. The containers that don't have any dependencies are always started first and concurrently.

To use this feature successfully, you must use [startup health check probes](https://docs.cloud.google.com/run/docs/configuring/workerpools/healthchecks). The startup probe enables Cloud Run to inspect the health of a dependent container, making sure it passes successfully before it starts up the next container. If you don't use health checks, containers are started in the specified order even if containers they depend on fail to start.

Note that there is no default startup health check probe for worker pools.

Use the Google Cloud console, Google Cloud CLI, or YAML to specify the startup order:

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

     * Select **Worker pools** from the menu.
     * For an existing worker pool, click the worker pool in the list and select **Edit and deploy new revision** to display the revision deployment form.
     * For a new worker pool, click **Deploy container** to display the **Create worker pool** form.
  2. For a new worker pool, specify the worker pool name, ingress container URL, CPU allocation, ingress control, and authentication. In the **Containers, Networking, Security** tab, do the following:

     1. Configure the ingress container.
     2. To add each of the other containers you are deploying, click **Add container**.
     3. For all containers except the ingress container, [configure a startup health check](https://docs.cloud.google.com/run/docs/configuring/workerpools/healthchecks).
     4. If a container needs to be started after certain other containers, select those containers in the **Container startup order** menu.
  3. For an existing worker pool, follow these steps:

     1. For all containers except the ingress container, [configure a startup health check](https://docs.cloud.google.com/run/docs/configuring/workerpools/healthchecks).
     2. Each container is shown with its own **Container startup order** menu. If a container needs other containers to start first before it can start, use the **Container startup order** menu to select the containers that must start first.
  4. Finish any other required configurations, then click **Create** for a new worker pool or **Deploy** for an existing worker pool. Wait for the deployment to finish.




###  gcloud 

Before using the Google Cloud CLI to specify startup order, [configure a startup health check](https://docs.cloud.google.com/run/docs/configuring/workerpools/healthchecks).

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To deploy multiple containers to a service with a specified startup order, run the command:



    
    
    gcloud run worker-pools deploy WORKER_POOL \
         --container CONTAINER_1_NAME --image='WORKER_POOL_IMAGE'
         --container CONTAINER_2_NAME --image='SIDECAR_IMAGE' --depends-on=CONTAINER_1_NAME \
         --container CONTAINER_3_NAME --image='SIDECAR_IMAGE' --depends-on=CONTAINER_1_NAME,CONTAINER_2_NAME

Replace the following:

  * WORKER_POOL: the name of the worker pool.
  * `IMAGE_URL`: a reference to the container image that contains the worker pool, such as `us-docker.pkg.dev/cloudrun/container/worker-pool:latest`.
  * `SIDECAR_IMAGE`: a reference to the sidecar container image.

If you want to configure each container in the deploy command, supply each container's configuration after the `container` parameters.




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
             metadata:
               annotations:
                 run.googleapis.com/container-dependencies: '{"CONTAINER1":["CONTAINER2"], "CONTAINER3":["CONTAINER1","CONTAINER2"]}'

Replace the following:

     * WORKER_POOL: the name of your Cloud Run worker pool.
     * CONTAINER1: the name of the first container that depends on one or more container. You can set the container name in the YAML; Cloud Run automatically generates a name if one isn't specified.
     * CONTAINER2: the name of the container that must start before CONTAINER1.
     * CONTAINER3: the name of the second container that depends on one or more containers.

In the example shown in the YAML snippet, CONTAINER2 starts first, CONTAINER1 starts second, and CONTAINER3 starts last.

  3. Create or update the worker pool using the following command:
         
         gcloud run worker-pools replace worker-pool.yaml

The `gcloud run worker-pools replace` command defaults to using `worker-pool.yaml` file if present.




## View container configuration for the worker pool

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run/worker-pools)

  2. Click **Worker pools** to display the list of deployed worker pools.

  3. Click the worker pool you want to examine to display its details pane.

  4. Click the **Containers** tab to display worker pool container configuration. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
