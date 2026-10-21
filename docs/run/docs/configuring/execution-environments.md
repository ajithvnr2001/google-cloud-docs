---
url: https://docs.cloud.google.com/run/docs/configuring/execution-environments/
title: Select an execution environment for services \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:10:43.353235+00:00
---

# Select an execution environment for services  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/execution-environments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Select an execution environment for services Stay organized with collections  Save and categorize content based on your preferences. 

All Cloud Run instances are sandboxed. The sandboxing technology and available features differs depending on the selected _execution environment_.

The first generation execution environment is based on [gVisor](https://gvisor.dev/) and features fast [cold start](https://docs.cloud.google.com/run/docs/tips/general#using_minimum_instances_to_reduce_cold_starts) times and emulation of most, but not all operating system calls.

The second generation execution environment is a microVM and provides full Linux compatibility rather than system call emulation. This execution environment provides:

  * Faster CPU performance
  * Faster network performance, especially in the presence of packet loss
  * Full Linux compatibility, including support for all system calls, namespaces, and cgroups
  * Network file system support



Although the second generation execution environment generally performs faster under sustained load, it has longer [cold start times](https://docs.cloud.google.com/run/docs/tips/general#starting_services_quickly) than first generation for some services.

Both execution environments have the same pricing. See the [Cloud Run pricing page](https://cloud.google.com/run/pricing) for details.

## Selecting an execution environment for a Cloud Run service

Cloud Run services by default don't have an execution environment specified, which means Cloud Run selects the execution environment based on the features used. If you don't specify an execution environment for your service, Cloud Run can select either the first generation or the second generation environment.

Cloud Run jobs and worker pools only use the second generation execution environment, and this cannot be changed.

### How to choose an execution environment

You should use first generation if any of the following apply:

  * Your Cloud Run service has bursty traffic, and needs to scale out fast to many instances, or your service is sensitive to cold start times.
  * Your Cloud Run service has infrequent traffic that causes frequent scale out from zero.
  * You want to use less than 512 MiB of memory. The second generation execution environment requires at least 512 MiB of memory.



You should use second generation if any of the following apply to your Cloud Run service:

  * Your service needs to use NFS, which is only supported by second generation.
  * Your service has fairly steady traffic and is tolerant of somewhat slower cold starts.
  * Your service has CPU-intensive workloads.
  * Your service could benefit from faster network performance.
  * Your service uses [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) to send traffic to a VPC network and requires the best possible network performance.
  * Your service needs to use software that has issues running in first generation due to [unimplemented system calls](https://docs.cloud.google.com/run/docs/troubleshooting#openblas-warning).
  * Your service needs Linux cgroup functionality.
  * Your service makes use of third-party infrastructure for securing containers.



### Required roles

To get the permissions that you need to configure and deploy Cloud Run services, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run service
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



If you are deploying a [service](https://docs.cloud.google.com/run/docs/deploying-source-code#required_roles) or [function](https://docs.cloud.google.com/run/docs/deploy-functions#required-roles) from source code, you must also have additional roles granted to you on your project and Cloud Build service account.

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

### Set and update execution environment

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

The default for Cloud Run services is _unspecified_ , which means that Cloud Run selects a suitable execution environment. Alternatively, you can specify an execution environment. To use second generation, you must [specify at least 512 MiB of memory](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits).

You can set the execution environment using the Google Cloud console, the gcloud command line, or a YAML file when you [create a new service](https://docs.cloud.google.com/run/docs/deploying#service) or [deploy a new revision](https://docs.cloud.google.com/run/docs/deploying#revision):

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu:

     1. If you are configuring a new service, click **Deploy container** and fill out the initial service settings page. Then click **Containers, Networking, Security** to expand the service configuration page.

     2. If you are configuring an existing service, click the service.

  3. Click the **Containers** tab.

  4. Select the execution environment using the option buttons. Keep **Default** to let Cloud Run select a suitable execution environment.

  5. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

You can [update the execution environment](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) for a given service by using the following command:
    
    
    gcloud run services update SERVICE --execution-environment ENVIRONMENT

Replace SERVICE with the name of your service and ENVIRONMENT with the desired execution environment. Specify the value `gen1` for first generation or `gen2` for second generation.

You can also set the execution environment during [deployment](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) using the command:
    
    
    gcloud run deploy --image IMAGE_URL --execution-environment ENVIRONMENT

Replace the following:

  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
  * `ENVIRONMENT`: the desired execution environment. Specify the value `gen1` for first generation or `gen2` for second generation.



### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. set the `run.googleapis.com/execution-environment` annotation:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/execution-environment: ENVIRONMENT

Replace the following:

     * SERVICE: the name of your Cloud Run service.
     * ENVIRONMENT: the selected execution environment. Specify the value `gen1` for first generation or `gen2` for second generation.

Remove the `run.googleapis.com/execution-environment` annotation for the default behavior.

  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "cloudrun-service-execution-environment"
      location = "REGION"
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
        execution_environment = "ENVIRONMENT"
      }
    }
    

Replace the following:

  * REGION: the Google Cloud region. For example, `europe-west1`.
  * ENVIRONMENT: `EXECUTION_ENVIRONMENT_GEN1` for first generation, or `EXECUTION_ENVIRONMENT_GEN2` for second generation.



## View execution environment settings

To view the current execution environment settings for your Cloud Run service:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the service you are interested in to open the **Service details** page.

  3. Click the **Containers** tab to view the settings.




###  gcloud 

  1. Use the following command:
         
         gcloud run services describe SERVICE

  2. Locate the execution environment setting in the returned configuration.




## Graceful shutdowns

When a Cloud Run instance is shutting down, it receives a [`SIGTERM` signal](https://docs.cloud.google.com/run/docs/container-contract#instance-shutdown) to enable a 10 second graceful shutdown.

### Handling SIGTERM signal

We recommend that your container install a [SIGTERM handler](https://docs.cloud.google.com/run/docs/container-contract#instance-shutdown), especially if you are using [request-based billing](https://docs.cloud.google.com/run/docs/configuring/billing-settings).

Handling SIGTERM gives your container a chance to perform any necessary cleanup tasks such as flushing logs before exiting. If your container does not catch SIGTERM, it will still be given 10 seconds to perform these tasks; those 10 seconds are billed.

#### How to check whether your container handles SIGTERM

To determine whether your container has a SIGTERM handler installed:

  1. Start Cloud Shell. You can find ![Activate Cloud Run button](https://docs.cloud.google.com/static/shell/docs/images/activate-cloud-shell-button.svg)**Activate Cloud Shell** in the header of the documentation page you're on. You may need to authorize it and wait for it to provision. Alternatively, [start a standalone session](https://docs.cloud.google.com/shell/docs/launching-cloud-shell#launch_a_standalone_session).

  2. Run the container locally in Cloud Shell:
         
         docker run IMAGE_URL

Replace `IMAGE_URL` with a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .

  3. Open another tab in Cloud Shell and get a list of the containers running in the current Cloud Shell session:
         
         docker container ls

You need to locate the container ID returned from the command.

  4. Using the container ID, send your container a SIGTERM signal
         
         docker kill -s SIGTERM CONTAINER_ID

  5. Return to the tab where you invoked `docker run` to see whether the container has exited (stopped). If the SIGTERM signal caused your container to exit, your container is handling SIGTERM.




### How to handle SIGTERM

If your container does not handle SIGTERM, the simplest way to add a SIGTERM handler is to wrap your service with `tini`. Doing this makes your service run as a subprocess of `tini`, which takes on the role of the container init process. Refer to the [Docker instructions](https://github.com/docker-library/official-images#init) for instructions.

Alternatively, you can change your application to directly handle SIGTERM.

## What's next

  * To use Filestore with Cloud Run, refer to [Using Filestore with Cloud Run](https://docs.cloud.google.com/run/docs/tutorials/network-filesystems-filestore).
  * To use Cloud Storage FUSE with Cloud Run, refer to [Using Cloud Storage FUSE with Cloud Run](https://docs.cloud.google.com/run/docs/tutorials/network-filesystems-fuse).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
