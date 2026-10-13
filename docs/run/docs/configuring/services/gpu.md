---
url: https://docs.cloud.google.com/run/docs/configuring/services/gpu/
title: GPU support for services \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:41.314262+00:00
---

# GPU support for services  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/services/gpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  GPU support for services Stay organized with collections  Save and categorize content based on your preferences. 

This page describes GPU configuration for your Cloud Run services. GPUs work well for AI inference workloads, such as large language models (LLMs) or other compute intensive non-AI use cases such as video transcoding and 3D rendering. Google provides NVIDIA RTX PRO 6000 Blackwell GPU with 96 GB of GPU memory (VRAM) and NVIDIA L4 GPUs with 24 GB of GPU memory (VRAM), which is separate from the [instance memory](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits).

**Important:** If you are using LLM with the Cloud Run GPU feature, make sure you _also_ consult [Best practices: Cloud Run services with GPUs](https://docs.cloud.google.com/run/docs/configuring/services/gpu-best-practices).

GPU on Cloud Run is fully managed, with no extra drivers or libraries needed. The GPU feature offers on-demand availability with no reservations needed, similar to the way on-demand [CPU](https://docs.cloud.google.com/run/docs/configuring/services/cpu) and on-demand [memory](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits) work in Cloud Run. Instances of a Cloud Run service that has been configured to use GPU can scale down to zero for cost savings when not in use.

Cloud Run instances with an attached NVIDIA RTX PRO 6000 Blackwell GPU or L4 GPU with drivers pre-installed start in approximately 5 seconds, at which point the processes running in your container can start to use the GPU.

You can configure one GPU per Cloud Run instance. If you use sidecar containers, note that the GPU can only be attached to one container.

## Supported GPU types

Cloud Run supports two types of GPUs:

  * [NVIDIA RTX PRO 6000 Blackwell GPU](https://www.nvidia.com/en-us/data-center/rtx-pro-6000-blackwell-server-edition/) with the current NVIDIA driver version: 580.x.x (13.0). For NVIDIA RTX PRO 6000 Blackwell GPU, you must use a minimum of 20 CPU and 80 GiB of memory.
  * [L4 GPU](https://www.nvidia.com/en-us/data-center/l4/) with the current NVIDIA driver version: 580.x.x (13.0). For L4 GPUs, you must use a minimum of 4 CPU and 16 GiB of memory.



## Supported regions

The following regions are supported by the NVIDIA RTX PRO 6000 Blackwell GPU:

  * `asia-southeast1` (Singapore). 
  * `asia-south2` (Delhi, India).
  * `europe-west4` (Netherlands) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-central1` (Iowa) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)



The following regions are supported by the L4 GPU:

  * `asia-southeast1` (Singapore) 
  * `asia-south1` (Mumbai) . This region is available by invitation only. Contact your Google Account team if you are interested in this region.
  * `europe-west1` (Belgium) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `europe-west4` (Netherlands) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker)
  * `us-central1` (Iowa) ![leaf icon](https://cloud.google.com/sustainability/region-carbon/gleaf.svg)[Low CO2](https://cloud.google.com/sustainability/region-carbon#region-picker) . Additional resource scaling in this region might require a quota increase request. Contact your Google Account team if you are interested in this region. 
  * `us-east4` (Northern Virginia) . Additional resource scaling in this region might require a quota increase request. Contact your Google Account team if you are interested in this region.



## Pricing impact

See [Cloud Run pricing](https://cloud.google.com/run/pricing) for GPU pricing details. Note the following requirements and considerations: 

  * There are no per request fees. You must use [instance-based billing](https://docs.cloud.google.com/run/docs/configuring/billing-settings) to use the GPU feature, minimum instances are charged at the full rate even when idle.
  * There is a difference in cost between GPU zonal redundancy and non-zonal redundancy. See [Cloud Run pricing](https://docs.cloud.google.com/run/pricing) for GPU pricing details.
  * When you deploy a Cloud Run service or function from source code with GPUs enabled, Cloud Run uses the [`e2-highcpu-8` machine type](https://docs.cloud.google.com/build/pricing), instead of the default `e2-standard-2` machine type to build your source code. The larger machine type provides higher CPU support, and higher network bandwidth which results in faster build times.
  * The CPU and memory configurations of your resource.
  * GPU is billed for the entire duration of the instance lifecycle.



## GPU zonal redundancy options

By default, Cloud Run deploys your service across multiple zones within a region. This architecture provides inherent resilience: if a zone experiences an outage, Cloud Run automatically routes traffic away from the affected zone to healthy zones within the same region.

When working with GPU resources, keep in mind GPU resources have specific capacity constraints. During a zonal outage, the standard failover mechanism for GPU workloads relies on sufficient unused GPU capacity being available in the remaining healthy zones. Due to the constrained nature of GPUs, this capacity might not always be available.

To increase the availability of your GPU-accelerated services during zonal outages, you can configure zonal redundancy specifically for GPUs:

  * **Zonal Redundancy Turned On** (default): Cloud Run reserves GPU capacity for your service across multiple zones. This significantly increases the probability that your service can successfully handle traffic rerouted from an affected zone, offering higher reliability during zonal failures with additional cost per GPU second.

  * **Zonal Redundancy Turned Off** : Cloud Run attempts failover for GPU workloads on a best-effort basis. Traffic is routed to other zones only if sufficient GPU capacity is available at that moment. This option does not guarantee reserved capacity for failover scenarios but results in a lower cost per GPU second.




## SLA

The SLA for Cloud Run GPU depends on whether the service uses the zonal redundancy or non-zonal redundancy option. Refer to the [SLA page](https://cloud.google.com/run/sla) for details.

## Request a quota increase

Quota for Cloud Run `nvidia-rtx-pro-6000` GPU is granted in milliGPUs. Projects using `nvidia-rtx-pro-6000` GPU in a region for the first time will be automatically granted 3,000 milliGPU quota (zonal redundancy off) when the first deployment is created. This is equivalent to 3 GPUs. Projects using Cloud Run `nvidia-l4` GPUs in a region for the first time are automatically granted 3 GPU quota (zonal redundancy off) when the first deployment is created.

If you need additional Cloud Run GPUs, you must request a quota increase for your Cloud Run service. Use the links provided in the following buttons to request the quota you need.

**Important:** Quota increase for GPUs with zonal redundancy turned _off_ are more likely to be granted and will be made available more quickly.Quota needed | Quota link  
---|---  
NVIDIA RTX PRO 6000 Blackwell GPU with zonal redundancy turned _off_ (lower price) | [Request GPU quota without zonal redundancy](https://console.cloud.google.com/projectselector2/iam-admin/quotas?pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22Metric_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22run.googleapis.com%252Fnvidia_rtx_pro_6000_gpu_allocation_no_zonal_redundancy_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22metricName_22%257D%255D%22\)\))  
NVIDIA RTX PRO 6000 Blackwell GPU with zonal redundancy turned _on_ (higher price) | [Request GPU quota with zonal redundancy](https://console.cloud.google.com/projectselector2/iam-admin/quotas?pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22metric_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22run.googleapis.com%252Fnvidia_rtx_pro_6000_gpu_allocation_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22metricName_22%257D%255D%22\)\))  
L4 GPU with zonal redundancy turned _off_ (lower price) | [Request GPU quota without zonal redundancy](https://console.cloud.google.com/projectselector2/iam-admin/quotas?pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22Metric_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22run.googleapis.com%252Fnvidia_l4_gpu_allocation_no_zonal_redundancy_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22metricName_22%257D%255D%22\)\))  
L4 GPU with zonal redundancy turned _on_ (higher price) | [Request GPU quota with zonal redundancy](https://console.cloud.google.com/projectselector2/iam-admin/quotas?pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22Metric_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22run.googleapis.com%252Fnvidia_l4_gpu_allocation_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22metricName_22%257D%255D%22\)\))  
  
For more information on requesting quota increases, see [How to increase quota](https://docs.cloud.google.com/run/quotas#increase).

## Before you begin

The following list describes requirements and limitations when using GPUs in Cloud Run:

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

  6. Enable the Cloud Run API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=run.googleapis.com)

  7. Request required quota.
  8. Consult [Best practices: AI inference on Cloud Run with GPUs](https://docs.cloud.google.com/run/docs/configuring/services/gpu-best-practices) for recommendations on building your container image and loading large models.
  9. Make sure your Cloud Run service has the following configurations:
     * Configure the billing settings to instance-based billing. Note that services that are set to instance-based billing can still scale to zero.
     * For NVIDIA RTX PRO 6000 Blackwell GPU, configure a minimum of [20 CPU](https://docs.cloud.google.com/run/docs/configuring/services/cpu) and a minimum of [80 GiB of memory](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits).
     * For L4 GPU, configure a minimum of [4 CPU](https://docs.cloud.google.com/run/docs/configuring/services/cpu) for your service, with 8 CPU recommended, and a minimum of [16 GiB of memory](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits), with 32 GiB recommended.
     * Determine and set an [optimal maximum concurrency for your GPU usage](https://docs.cloud.google.com/run/docs/configuring/services/gpu-best-practices#max-concurrent-requests).
     * [Maximum instances](https://docs.cloud.google.com/run/docs/configuring/max-instances) must be set to a number that is below the allowed [quota per project per region for GPU](https://docs.cloud.google.com/run/quotas#cloud_run_limits). See About GPUs and maximum instances.



### Required roles

To get the permissions that you need to configure and deploy Cloud Run services, ask your administrator to grant you the following IAM roles on services: 

  * Cloud Run Developer (`roles/run.developer`) - the Cloud Run service 
  * Service Account User (`roles/iam.serviceAccountUser`) - the service identity 



If you are deploying a [service](https://docs.cloud.google.com/run/docs/deploying-source-code#required_roles) or [function](https://docs.cloud.google.com/run/docs/deploy-functions#required-roles) from source code, you must also have additional roles granted to you on your project and Cloud Build service account.

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure a Cloud Run service with GPU

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

You can use the Google Cloud console, Google Cloud CLI or YAML to configure GPU.

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu:

     1. If you are configuring a new service, click **Deploy container** and fill out the initial service settings page. Then click **Containers, Networking, Security** to expand the service configuration page.

     2. If you are configuring an existing service, click the service.

  3. Click the **Containers** tab.

  4. Configure CPU, memory, concurrency, execution environment, and startup probe following the recommendations in Before you begin.

  5. Check the **GPU** checkbox, then select the **GPU type** and **Number of GPUs** from the respective menus.

  6. By default, zonal redundancy is turned on for new services. Selecting the **GPU** checkbox shows the **GPU redundancy** options.

     1. To turn off zonal redundancy, select **No zonal redundancy**.
     2. To turn on zonal redundancy, select **Zonal redundancy**.
  7. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

To create a service with GPU enabled, use the [`gcloud run deploy`](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) command:

  * To deploy a container:
        
        gcloud run deploy SERVICE \
              --image IMAGE_URL \
              --gpu 1

Replace the following:

    * SERVICE: the name of your Cloud Run service.
    * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
  * To deploy from source code:
        
        gcloud run deploy SERVICE \
              --source . \
              --gpu 1




To update the GPU configuration for a service, use the [`gcloud run services update`](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) command. For example, to update an existing service that specifies a container image:
    
    
      gcloud run services update SERVICE \
          --image IMAGE_URL \
          --cpu CPU \
          --memory MEMORY \
          --no-cpu-throttling \
          --gpu GPU_NUMBER \
         --gpu-type GPU_TYPE \
          --max-instances MAX_INSTANCE
          --GPU_ZONAL_REDUNDANCY
        

Replace the following:

  * SERVICE: the name of your Cloud Run service.
  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
  * CPU: the number of CPU. For NVIDIA RTX PRO 6000 Blackwell GPU, you must specify at least `20` CPU. For L4 GPU, you must specify at least `4` CPU.
  * MEMORY: the amount of memory. For NVIDIA RTX PRO 6000 Blackwell GPU, you must specify at least `80Gi` (80 GiB). For L4 GPU, you must specify at least `16Gi` (16 GiB).
  * GPU_NUMBER: the value `1` (one). If this is unspecified but a GPU_TYPE is present, the default is `1`.
  * GPU_TYPE: the GPU type. NVIDIA RTX PRO 6000 Blackwell GPU, enter `nvidia-rtx-pro-6000`. For L4 GPU, enter value `nvidia-l4` (nvidia-`L`4 lowercase L, not numeric value fourteen).
  * MAX_INSTANCE: the maximum number of instances. This number can't exceed the [GPU quota](https://docs.cloud.google.com/run/quotas#cloud_run_limits) allocated for your project.
  * GPU_ZONAL_REDUNDANCY: `no-gpu-zonal-redundancy` to turn off zonal redundancy, or `gpu-zonal-redundancy` to turn on zonal redundancy.



### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the `nvidia.com/gpu:` attribute and `nodeSelector:  
run.googleapis.com/accelerator:`:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             metadata:
               annotations:
                 autoscaling.knative.dev/maxScale: 'MAX_INSTANCE'
                 run.googleapis.com/cpu-throttling: 'false'
                 run.googleapis.com/gpu-zonal-redundancy-disabled: 'GPU_ZONAL_REDUNDANCY'
             spec:
               containers:
               - image: IMAGE_URL
                 ports:
                 - containerPort: CONTAINER_PORT
                   name: http1
                 resources:
                   limits:
                     cpu: 'CPU'
                     memory: 'MEMORY'
                     nvidia.com/gpu: '1'
                 # Optional: use a longer startup probe to allow long starting containers
                 startupProbe:
                   failureThreshold: 1800
                   periodSeconds: 1
                   tcpSocket:
                     port: CONTAINER_PORT
                   timeoutSeconds: 1
               nodeSelector:
                 run.googleapis.com/accelerator: GPU_TYPE

Replace the following:

     * SERVICE: the name of your Cloud Run service.
     * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
     * CONTAINER_PORT: the container port set for your service.
     * CPU: the number of CPU. For NVIDIA RTX PRO 6000 Blackwell GPU, you must specify at least `20` CPU. For L4 GPU, you must specify at least `4` CPU.
     * MEMORY: the amount of memory. For NVIDIA RTX PRO 6000 Blackwell GPU, you must specify at least `80Gi` (80 GiB). For L4 GPU, you must specify at least `16Gi` (16 GiB).
     * GPU_TYPE: the GPU type. NVIDIA RTX PRO 6000 Blackwell GPU, enter `nvidia-rtx-pro-6000`. For L4 GPU, enter value `nvidia-l4` (nvidia-`L`4 lowercase L, not numeric value fourteen).
     * MAX_INSTANCE: the maximum number of instances. This number can't exceed the [GPU quota](https://docs.cloud.google.com/run/quotas#cloud_run_limits) allocated for your project.
     * GPU_ZONAL_REDUNDANCY: `false` to turn on GPU zonal redundancy, or `true` to turn it off.
  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service" "default" {
      provider = google-beta
      name     = "SERVICE"
      location = "europe-west1"
    
      template {
        gpu_zonal_redundancy_disabled = "GPU_ZONAL_REDUNDANCY"
        containers {
          image = "IMAGE_URL"
          resources {
            limits = {
              "cpu" = "CPU"
              "memory" = "MEMORY"
              "nvidia.com/gpu" = "1"
            }
          }
        }
        node_selector {
          accelerator = "GPU_TYPE"
        }
      }
    }
    

Replace the following:

  * SERVICE: the name of your Cloud Run service.
  * GPU_ZONAL_REDUNDANCY: `false` to turn on GPU zonal redundancy, or `true` to turn it off.
  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
  * CPU: the number of CPU. For NVIDIA RTX PRO 6000 Blackwell GPU, you must specify at least `20` CPU. For L4 GPU, you must specify at least `4` CPU.
  * MEMORY: the amount of memory. For NVIDIA RTX PRO 6000 Blackwell GPU, you must specify at least `80Gi` (80 GiB). For L4 GPU, you must specify at least `16Gi` (16 GiB).
  * GPU_TYPE: the GPU type. For NVIDIA RTX PRO 6000 Blackwell GPU, enter `nvidia-rtx-pro-6000`. For L4 GPU, enter value `nvidia-l4` (nvidia-`L`4 lowercase L, not numeric value fourteen).



## View GPU settings

To view the current GPU settings for your Cloud Run service:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the service you are interested in to open the **Service details** page.

  3. Click the **Containers** tab to view the settings.




###  gcloud 

  1. Use the following command:
         
         gcloud run services describe SERVICE

  2. Locate the GPU setting in the returned configuration.




## Remove GPU

You can remove GPU using the Google Cloud console, the Google Cloud CLI, or YAML.

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu:

     1. If you are configuring a new service, click **Deploy container** and fill out the initial service settings page. Then click **Containers, Networking, Security** to expand the service configuration page.

     2. If you are configuring an existing service, click the service.

  3. Click the **Containers** tab.

  4. Unselect the GPU checkbox.

  5. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

To remove GPU, set the number of GPUs to `0` using the [gcloud run services update](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) command:
    
    
      gcloud run services update SERVICE --gpu 0
      

Replace SERVICE with the name of your Cloud Run service.

### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Delete the `nvidia.com/gpu:` and the `nodeSelector: run.googleapis.com/accelerator: GPU_TYPE` lines.

  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




## Driver libraries

By default, all of the NVIDIA RTX PRO 6000 Blackwell GPU and NVIDIA L4 GPU driver libraries are mounted under `/usr/local/nvidia/lib64`. Cloud Run automatically appends this path to the `LD_LIBRARY_PATH` environment variable (i.e. `${LD_LIBRARY_PATH}:/usr/local/nvidia/lib64`) of the container with the GPU. This allows the dynamic linker to find the NVIDIA driver libraries. The linker searches and resolves paths in the order you list in the `LD_LIBRARY_PATH` environment variable. Any values you specify in this variable take precedence over the default Cloud Run driver libraries path `/usr/local/nvidia/lib64`.

If you want to use a CUDA version greater than 13.0, the easiest way is to depend on a newer [NVIDIA base image](https://catalog.ngc.nvidia.com/containers) with forward compatibility packages already installed. Another option is to manually [install the NVIDIA forward compatibility packages](https://docs.nvidia.com/deploy/cuda-compatibility/#installing-the-forward-compatibility-package) and add them to `LD_LIBRARY_PATH`. Consult [NVIDIA's compatibility matrix](https://docs.nvidia.com/deeplearning/frameworks/support-matrix/index.html) to determine which CUDA versions are forward compatible with the provided NVIDIA driver version.

## About GPUs and maximum instances

The number of instances with GPUs is limited in two ways:

  * The [Maximum instances](https://docs.cloud.google.com/run/docs/configuring/max-instances) setting limits the _number of instances per service_. This can't be set higher than the GPU [quota per project per region for GPU](https://docs.cloud.google.com/run/quotas#cloud_run_limits).
  * The quota of GPUs allowed per project per region. This limits the _number of instances across services_ in the same region.



## What's next

See [Run AI inference on Cloud Run with GPUs](https://docs.cloud.google.com/run/docs/ai/inference) for tutorials.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
