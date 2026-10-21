---
url: https://docs.cloud.google.com/run/docs/configuring/services/cpu/
title: Configure CPU limits for services \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:15:55.074251+00:00
---

# Configure CPU limits for services  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/services/cpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure CPU limits for services Stay organized with collections  Save and categorize content based on your preferences. 

This page also describes how to enable or disable startup CPU boost, a feature that temporarily increases vCPU allocation during instance startup in order to reduce startup latency.

**Note:** in addition to specifying the number of vCPUs to use, you can also specify whether vCPUs are allocated for the lifetime of the instance or only allocated during request processing. For details, refer to [Billing settings](https://docs.cloud.google.com/run/docs/configuring/billing-settings).

## Set and update vCPU limits

By default, each instance is limited to 1 vCPU. You can change this to any of the values shown in the following table.

### vCPU and memory table

The following are memory requirements for vCPUs:

CPUs | Memory required  
---|---  
.08 vCPU | Up to 512 MiB  
.5 vCPU | Up to 1 GiB  
1 vCPU | Up to 4 GiB  
2 vCPU | Up to 8 GiB  
4 vCPU | 2 to 16 GiB  
6 vCPU | 4 to 24 GiB  
8 vCPU | 4 to 32 GiB  
  
Values greater than 1 must be integer values.

**Note:** When selecting a vCPU limit greater than 1 vCPU, consider your application's threading model. If your application is single-threaded, it may only fully utilize one vCPU.

### Maximum amount of vCPU

The maximum amount of vCPU you can configure is 8 vCPU.

### Minimum amount of vCPU

The minimum vCPU setting is 0.08 vCPU.

If you want to use less than 1 vCPU, you can select any value between 0.08 and 1, in increments of 0.001.

_If you use less than 1 vCPU_ , the following requirements are enforced:

Setting | Requirement  
---|---  
Memory | A minimum of 0.5 vCPU is needed to set a [memory limit](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits) greater than 512MiB.  
A minimum of 1 vCPU is needed to set a memory limit greater than 1GiB.  
Concurrency | [Maximum concurrency](https://docs.cloud.google.com/run/docs/configuring/concurrency) must be set to `1`.  
Billing | The [billing settings](https://docs.cloud.google.com/run/docs/configuring/billing-settings) must be set to request-based billing.  
Execution environment | You must use the [first generation execution environment](https://docs.cloud.google.com/run/docs/configuring/execution-environments).  
  
### Cost considerations

The cost of your Cloud Run resource is impacted by its CPU configuration and how long your resource is active, among other factors. Overprovisioning your resources can increase your costs. To determine which CPU configuration might be best for your resource:

  1. Establish an initial baseline configuration for a CPU limit that balances CPU utilization and costs.
  2. Monitor your CPU utilization metrics in Cloud Monitoring while testing the system under load.
  3. Adjust your CPU configuration as necessary.



If CPU utilization is consistently low under peak load, consider reducing vCPU allocation. If latency is high, consider increasing vCPU allocation.

You can view summary cost data, utilization data, and cost optimization recommendations for resources on the [Cloud Hub Optimization page](https://docs.cloud.google.com/hub/docs/optimize). Review [Cloud Run pricing](https://cloud.google.com/run/pricing) or estimate costs with the [pricing calculator](https://cloud.google.com/products/calculator) for more information.

## Required roles

To get the permissions that you need to configure and deploy Cloud Run services, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run service
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



If you are deploying a [service](https://docs.cloud.google.com/run/docs/deploying-source-code#required_roles) or [function](https://docs.cloud.google.com/run/docs/deploy-functions#required-roles) from source code, you must also have additional roles granted to you on your project and Cloud Build service account.

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure CPU limits

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

You can set CPU limits using the Google Cloud console, the gcloud command line, or a YAML file when you [create a new service](https://docs.cloud.google.com/run/docs/deploying#service) or [deploy a new revision](https://docs.cloud.google.com/run/docs/deploying#revision):

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu:

     1. If you are configuring a new service, click **Deploy container** and fill out the initial service settings page. Then click **Containers, Networking, Security** to expand the service configuration page.

     2. If you are configuring an existing service, click the service.

  3. Click the **Containers** tab.

  4. Select the CPU limit from the list. Select a value of `1`, `2`, `4`, `6`, or `8` CPUs, or for less than 1 CPU, specify a value from 0.08 to less than 1.00, in increments of 0.01. (See the table under Setting and updating CPU limits for required settings.).

  5. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

You can [update the CPU limits](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) for a given service by using the following command:
    
    
    gcloud run services update SERVICE --cpu CPU

Replace the following:

  * SERVICE: the name of your service.
  * CPU: the desired CPU limit. Specify the value `1`, `2`, `4`, `6`, or `8` CPUs, or for less than 1 CPU, specify a value from 0.08 to less than 1.00, in increments of 0.01. (See the table under Setting and updating CPU limits for required settings.).



You can also set CPU during [deployment](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) using the command:
    
    
    gcloud run deploy --image IMAGE_URL --cpu CPU

Replace the following:

  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
  * CPU: the value `1`, `2`, `4`, `6`, or `8` CPUs, or for less than 1 CPU, specify a value from 0.08 to less than 1.00, in increments of 0.01. (See the table under Setting and updating CPU limits for required settings.)



### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the `cpu` attribute:
         
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
                     cpu: CPU

Replace the following:

     * SERVICE: the name of your Cloud Run service.
     * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
     * CPU: the desired CPU limit value. Specify the value `1`, `2`, `4`, `6`, or `8` CPUs, or for less than 1 CPU, specify a value from 0.08 to less than 1.00, in increments of 0.01. (See the table under Setting and updating CPU limits for required settings.)
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
      name     = "cloudrun-service-cpu"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello"
    ** resources {**
    ** limits = {**
              # CPU usage limit
              cpu = "1"
            }
          }
        }
      }
    }

The preceding `google_cloud_run_v2_service` resource specifies a CPU limit under `template.containers.resources.limits`.

Replace `1` with your desired CPU count. Tip: `1` corresponds to 1 vCPU.

## Set startup CPU boost

The _startup CPU boost_ feature for revisions provides additional CPU during [instance startup time](https://docs.cloud.google.com/run/docs/container-contract#startup) and for 10 seconds after the instance has started.

The actual CPU boost varies depending on your CPU limit settings:

CPU limit | Boosted CPU  
---|---  
0-1 | 2  
2 | 4  
4 | 8  
6 | 8  
8 | 8  
  
You are charged for the allocated boosted CPU for the duration of the container startup time. For example, if your container startup time is 15 seconds, and you allocate 2 CPU, with startup CPU boost, you'll be charged for 4 CPU during the (possibly shorter) instance startup time, including the 10 seconds after your container finished starting, and for 2 CPU during the rest of the container lifecycle.

If your Cloud Run deployment uses sidecars, and you enable startup CPU boost, all containers receive the CPU boost. Cloud Run determines the boosted CPU amount for each container by the CPU limit.

You can enable or disable startup CPU boost using Google Cloud console, Google Cloud CLI, a YAML file, or a Terraform file.

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu:

     1. If you are configuring a new service, click **Deploy container** and fill out the initial service settings page. Then click **Containers, Networking, Security** to expand the service configuration page.

     2. If you are configuring an existing service, click the service.

  3. Click the **Containers** tab.

  4. To enable startup CPU boost, select the checkbox **Startup CPU boost**. To disable this feature, deselect the checkbox.

  5. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

  1. You can [enable startup CPU boost](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) for a given service by using the following command:
         
         gcloud run services update SERVICE --cpu-boost

Replace SERVICE with the name of your service.

You can enable startup CPU boost during [deployment](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) using the command:
         
         gcloud run deploy --image IMAGE_URL --cpu-boost

Replace `IMAGE_URL` with a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .

  2. You can [disable startup CPU boost](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) for a given service by using the following command:
         
         gcloud run services update SERVICE --no-cpu-boost

Replace SERVICE with the name of your service.

You can disable startup CPU boost during [deployment](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) using the command:
         
         gcloud run deploy --image IMAGE_URL --no-cpu-boost




### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the `run.googleapis.com/startup-cpu-boost` attribute by specifying `'true'` to enable startup CPU boost or `'false'` to disable:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/startup-cpu-boost: 'true'

Replace SERVICE the name of your Cloud Run service.

  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "SERVICE"
      location = "REGION"
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello"
          resources {
            startup_cpu_boost = CPU_BOOST
          }
        }
      }
    }
    

Replace the following:

  * SERVICE: the name of your Cloud Run service.
  * REGION: the Google Cloud region—for example, `europe-west1`.
  * CPU_BOOST: `true` to enable startup CPU boost or `false` to disable it.



### Compose

To specify CPU limits in your `compose.yaml` file, add the `cpus` attribute to your service definition.
    
    
      services:
        web:
          image: IMAGE
          cpus: CPU_VALUE

Replace the following:

  * IMAGE: the URL of your container image.
  * CPU_VALUE: the needed CPU limit—for example, `2`.



**Deploy the services**

  1. To deploy the services, run the `gcloud run compose up` command:
         
         gcloud run compose up compose.yaml

  2. Respond `y` to any prompts to install required components or to enable APIs.

  3. Optional: [Make your service public](https://docs.cloud.google.com/run/docs/authenticating/public) if you want to allow unauthenticated access to the service.




After deployment, the Cloud Run service URL is displayed. Copy this URL and paste it into your browser to view the running container. You can disable the default authentication from the Google Cloud console.

## View CPU settings

To view the current CPU settings for your Cloud Run service:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the service you are interested in to open the **Service details** page.

  3. Click the **Containers** tab to view the settings.




###  gcloud 

  1. Use the following command:
         
         gcloud run services describe SERVICE

  2. Locate the CPU setting in the returned configuration.




## Application threading and CPU utilization

When selecting a CPU limit greater than 1 vCPU, consider your application's threading model. When autoscaling, Cloud Run uses the average CPU utilization across all allocated CPUs. If your application is single-threaded, it may only fully utilize one core, which leads to a low average CPU utilization even under load. This can prevent CPU-based autoscaling from occurring as expected.

To avoid this behavior for a single-threaded application, if your memory requirements allow it, we recommend starting with 1 vCPU. This results in better CPU-based autoscaling. If higher memory needs force a multi-CPU selection for a single-threaded application, consider tuning your [concurrency setting](https://docs.cloud.google.com/run/docs/configuring/concurrency).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
