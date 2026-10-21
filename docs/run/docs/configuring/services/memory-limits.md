---
url: https://docs.cloud.google.com/run/docs/configuring/services/memory-limits/
title: Configure memory limits for services \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:54.546861+00:00
---

# Configure memory limits for services  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/services/memory-limits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure memory limits for services Stay organized with collections  Save and categorize content based on your preferences. 

You can choose the amount of memory to provide for your Cloud Run service. This page describes how to specify the amount of memory available for your service.

## Understand memory usage

Cloud Run instances that exceed their allowed memory limit are terminated.

The available memory for your instance needs to be sufficient for:

  * Running the service executable, because the executable must be loaded to memory
  * Allocating memory in your service process
  * Writing files to the file system



The size of the deployed container image does not affect memory that is available for the instance.

## Set and update memory limits

You can set memory limits on Cloud Run services. By default, the memory allocated to each instance of a revision is 512 MiB .

### Required memory when setting a CPU value

When setting a CPU value, the following memory is required:

CPUs | Memory required  
---|---  
.08 vCPU | Up to 512 MiB  
.5 vCPU | Up to 1 GiB  
1 vCPU | Up to 4 GiB  
2 vCPU | Up to 8 GiB  
4 vCPU | 2 to 16 GiB  
6 vCPU | 4 to 24 GiB  
8 vCPU | 4 to 32 GiB  
If you use less than 512 MiB of memory, you should use the [first generation execution environment](https://docs.cloud.google.com/run/docs/about-execution-environments). **Important:** If your single-threaded application's memory needs require you to select a configuration with 2 or more vCPUs, be aware that this can lead to potential "vCPU hotspots," resulting in inefficient CPU-based autoscaling. In such scenarios, carefully tuning concurrency settings becomes essential for managing load and achieving desired scaling behavior. 

### Maximum amount of memory

The maximum amount of memory you can configure is 32 gibibyte (`32 Gi`).

You can enforce a maximum memory limit by using [custom organization policies](https://docs.cloud.google.com/run/docs/securing/custom-constraints#memory-limit). 

### Minimum memory

The minimum memory setting varies depending on whether you use [first generation or second generation](https://docs.cloud.google.com/run/docs/about-execution-environments) execution environment:

  * 128 MiB for first generation
  * 512 MiB for second generation



### Cost considerations

The cost of your Cloud Run service is impacted by its memory configuration and how long your resource is active, among other factors. Overprovisioning your resources can increase your costs. To determine which memory configuration might be best for your resource:

  1. Establish an initial baseline configuration.
  2. Monitor your memory utilization metrics in Cloud Monitoring while testing the system under load.
  3. Adjust your configuration as necessary.



If memory utilization is consistently low, consider reducing the allocated memory. If latency is high and memory utilization is near 100%, consider increasing the allocated memory. If you are experiencing Out of Memory (OOM) errors, you should increase the allocated memory or modify your application to prevent memory leaks and use less memory. See the [Cloud Monitoring dashboard](https://docs.cloud.google.com/monitoring/dashboards) to better understand your memory utilization.

Review [Cloud Run pricing](https://cloud.google.com/run/pricing) or estimate costs with the [pricing calculator](https://cloud.google.com/products/calculator) for more information.

## Required roles

To get the permissions that you need to configure and deploy Cloud Run services, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run service
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



If you are deploying a [service](https://docs.cloud.google.com/run/docs/deploying-source-code#required_roles) or [function](https://docs.cloud.google.com/run/docs/deploy-functions#required-roles) from source code, you must also have additional roles granted to you on your project and Cloud Build service account.

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure memory limits

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

For Cloud Run services, you can set memory limits using the Google Cloud console, the gcloud command line, or a YAML file when you [create a new service](https://docs.cloud.google.com/run/docs/deploying#service) or [deploy a new revision](https://docs.cloud.google.com/run/docs/deploying#revision):

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu:

     1. If you are configuring a new service, click **Deploy container** and fill out the initial service settings page. Then click **Containers, Networking, Security** to expand the service configuration page.

     2. If you are configuring an existing service, click the service.

  3. Click the **Containers** tab.

  4. Select the memory size from the **Memory** list.

  5. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

You can [update the memory allocation](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) of a given service by using the following command:
    
    
    gcloud run services update SERVICE --memory SIZE

Replace SERVICE with the name of your service and SIZE with the desired memory size. The format for size is a fixed or floating point number followed by a unit: `G` or `M` corresponding to gigabyte or megabyte, respectively, or use the power-of-two equivalents: `Gi` or `Mi` corresponding to gibibyte or mebibyte respectively.

You can also set memory limits during [deployment](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) using the command:
    
    
    gcloud run deploy --image IMAGE_URL --memory SIZE

Replace the following:

  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
  * SIZE: the values described previously.

**Note:** If you are using the gcloud CLI to deploying from source, make sure to have the [required roles](https://docs.cloud.google.com/run/docs/deploying-source-code#required_roles) granted to you and to use `--source` instead of `--image`, and add `--function` if deploying a function. 

### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the `memory` attribute:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             metadata:
               name: REVISION
             spec:
               containers:
               - image: IMAGE
                 resources:
                   limits:
                     memory: SIZE

Replace the following:

     * SERVICE: the name of your Cloud Run service.
     * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
     * SIZE: the needed memory size. The format is a fixed or floating point number followed by a unit: `G` or `M` corresponding to gigabyte or megabyte, respectively, or use the power-of-two equivalents: `Gi` or `Mi` corresponding to gibibyte or mebibyte respectively.
     * `REVISION`: a new revision name or delete it (if present). If you supply a new revision name, it **must** meet the following criteria:
       * Starts with `SERVICE-`
       * Contains only lowercase letters, numbers and `-`
       * Does not end with a `-`
       * Does not exceed 63 characters
  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "cloudrun-service-memory-limits"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello"
    
    ** resources {**
    ** limits = {**
              # Memory usage limit (per container)
              memory = "512Mi"
            }
          }
        }
      }
    }

Under `template.containers.resources.limits`, replace `512Mi` with your service's needed memory limit.

### Compose

To specify CPU and memory hints in your `compose.yaml` file, add the `cpus` attribute to your service definition. Cloud Run automatically allocates the [required memory when setting a CPU value](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits#cpu-minimum).
    
    
      services:
        web:
          image: IMAGE
          cpus: CPU_VALUE

Replace the following:

  * IMAGE: the URL of your container image.
  * CPU_VALUE: the needed CPU limit—for example, `2`. This value determines the required memory.



**Deploy the services**

  1. To deploy the services, run the `gcloud run compose up` command:
         
         gcloud run compose up compose.yaml

  2. Respond `y` to any prompts to install required components or to enable APIs.

  3. Optional: [Make your service public](https://docs.cloud.google.com/run/docs/authenticating/public) if you want to allow unauthenticated access to the service.




After deployment, the Cloud Run service URL is displayed. Copy this URL and paste it into your browser to view the running container. You can disable the default authentication from the Google Cloud console.

## Optimize memory for services

For a Cloud Run service, you can determine the peak memory requirement for a service using the following: **(Standing Memory) + (Memory per Request) * (Service Concurrency)**

Accordingly,

  * If you raise the concurrency of your service, you should also increase the memory limit to account for peak usage.

  * If you lower the concurrency of your service, consider reducing the memory limit to save on memory usage costs.




For more guidance on minimizing per request memory usage read [Development Tips on Global Variables](https://docs.cloud.google.com/run/docs/tips#using_global_variables).

## View memory limit settings

To view the current memory limit settings for your Cloud Run service:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the service you are interested in to open the **Service details** page.

  3. Click the **Containers** tab to view the settings.




###  gcloud 

  1. Use the following command:
         
         gcloud run services describe SERVICE

  2. Locate the memory limit setting in the returned configuration.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
