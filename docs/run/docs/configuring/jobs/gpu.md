---
url: https://docs.cloud.google.com/run/docs/configuring/jobs/gpu/
title: Configure GPUs for Cloud Run jobs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:45:04.262840+00:00
---

# Configure GPUs for Cloud Run jobs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/jobs/gpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Configure GPUs for Cloud Run jobs Stay organized with collections  Save and categorize content based on your preferences. 

This page describes GPU configuration for your Cloud Run jobs. GPUs work well for AI workloads such as, training large language models (LLMs) using your preferred frameworks, performing batch or offline inference on LLMs, and handling other compute-intensive tasks like video processing and graphics rendering as background jobs. Google provides NVIDIA RTX PRO 6000 Blackwell GPU with 96 GB of GPU memory (VRAM) and NVIDIA L4 GPUs with 24 GB of GPU memory (VRAM), which is separate from the [instance memory](https://docs.cloud.google.com/run/docs/configuring/jobs/memory-limits).

**Important:** If you are using LLM with the Cloud Run GPU feature, make sure you _also_ consult [Best practices: Cloud Run jobs with GPUs](https://docs.cloud.google.com/run/docs/configuring/jobs/gpu-best-practices).

GPU on Cloud Run is fully managed, with no extra drivers or libraries needed. The GPU feature offers on-demand availability with no reservations needed, similar to the way on-demand [CPU](https://docs.cloud.google.com/run/docs/configuring/jobs/cpu) and on-demand [memory](https://docs.cloud.google.com/run/docs/configuring/jobs/memory-limits) work in Cloud Run. 

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

  * GPU for jobs follow [No zonal redundancy pricing](https://cloud.google.com/run/pricing).
  * The CPU and memory configurations of your resource.
  * GPU is billed for the entire duration of the instance lifecycle.



## GPU non-zonal redundancy

The Cloud Run jobs feature provides non-zonal redundancy support only for GPU-enabled instances. With non-zonal redundancy enabled, Cloud Run attempts failover for GPU-enabled jobs on a best-effort basis. Cloud Run routes job executions to other zones only if sufficient GPU capacity is available at that moment. This option does not guarantee reserved capacity for failover scenarios but results in a lower cost per GPU second.

See configure a Cloud Run job with GPU for details on enabling non-zonal redundancy.

## Request a quota increase

Quota for Cloud Run `nvidia-rtx-pro-6000` GPUs is granted in milliGPUs. Projects using `nvidia-rtx-pro-6000` GPUs in a region for the first time will be automatically granted 3,000 milliGPU quota (zonal redundancy off) when the first deployment is created. This is equivalent to 3 GPUs. Projects using Cloud Run `nvidia-l4` GPUs in a region for the first time are automatically granted 3 GPU quota (zonal redundancy off) when the first deployment is created.

Note that this automatic quota grant is subject to availability depending on your CPU and memory capacity. This limits the count of GPUs that might be active across all of the project's services, jobs, and worker pools at any given time.

If you need additional Cloud Run GPUs for jobs, [request a quota increase](https://console.cloud.google.com/projectselector2/iam-admin/quotas?pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22Metric_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22run.googleapis.com%252Fnvidia_l4_gpu_allocation_no_zonal_redundancy_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22metricName_22%257D%255D%22\)\)).

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

  7. Consult [Best practices: Cloud Run jobs with GPUs](https://docs.cloud.google.com/run/docs/configuring/jobs/gpu-best-practices) for optimizing performance when using Cloud Run jobs with GPU.



### Required roles

To get the permissions that you need to configure Cloud Run jobs, ask your administrator to grant you the following IAM roles on jobs: 

  * Cloud Run Developer (`roles/run.developer`) - the Cloud Run job 
  * Service Account User (`roles/iam.serviceAccountUser`) - the service identity 



For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run job interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/jobs/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Configure a Cloud Run job to use GPUs

You can configure a Cloud Run job to use GPUs using the Google Cloud console, the gcloud CLI, or YAML:

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Jobs** from the Cloud Run navigation menu:

     1. If you are creating a new job, click **Deploy container** to fill out the initial job settings page.

     2. If you are configuring an existing job, select the job, then click **View and edit job configuration**.

  3. Click **Containers, Connections, Security** to expand the job properties page.

  4. In the **Containers** tab, configure memory and CPU following the requirements in Supported GPU types.

  5. Select the **GPU** checkbox.

  6. Select the GPU type from the **GPU type** menu, and the number of GPUs from the **Number of GPUs** menu.

  7. Click **Create** or **Update**.




###  gcloud 

To enable non-zonal redundancy, you must specify `--no-gpu-zonal-redundancy`. This is required for using GPU with jobs.

  * To [create a job](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/create) with GPUs enabled, run the following command:
        
        gcloud run jobs create JOB \
          --image=IMAGE_URL \
          --gpu=1 \
          --no-gpu-zonal-redundancy

Replace the following:

    * `JOB`: the name of your Cloud Run job.
    * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
  * To [update the GPU configuration](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/update) for an existing job, run the following command:
        
        gcloud run jobs update JOB \
          --image IMAGE_URL \
          --cpu CPU \
          --memory MEMORY \
          --gpu GPU_NUMBER \
          --gpu-type GPU_TYPE \
          --parallelism PARALLELISM \
          --no-gpu-zonal-redundancy

Replace the following:

    * `JOB`: the name of your Cloud Run job.
    * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
    * `CPU`: the number of CPUs. For NVIDIA RTX PRO 6000 Blackwell GPU, you must specify at least `20` CPU. For L4 GPU, you must specify at least `4` CPU.
    * `MEMORY`: the amount of memory. For NVIDIA RTX PRO 6000 Blackwell GPU, you must specify at least `80Gi` (80 GiB). For L4 GPU, you must specify at least `16Gi` (16 GiB).
    * `GPU_NUMBER`: the value `1` (one). If this is unspecified but a GPU_TYPE is present, the default is `1`.
    * `GPU_TYPE`: the GPU type. For NVIDIA RTX PRO 6000 Blackwell GPU, enter `nvidia-rtx-pro-6000`. For L4 GPU, enter `nvidia-l4` (nvidia-`L`4 lowercase L, not numeric value fourteen).
    * `PARALLELISM`: an integer value less than the lowest value of the applicable quota limits you allocated for your project.



### YAML

You must set the annotation `run.googleapis.com/gpu-zonal-redundancy-disabled:` to `true`. This enables non-zonal redundancy, which is required for GPUs for jobs.

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2. Update the `nvidia.com/gpu` attribute, `annotations: run.googleapis.com/launch-stage` for launch stage, and `nodeSelector:  
run.googleapis.com/accelerator`:
         
         apiVersion: run.googleapis.com/v1
         kind: Job
         metadata:
           name: JOB
           labels:
             cloud.googleapis.com/location: REGION
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/gpu-zonal-redundancy-disabled: 'true'
             spec:
               template:
                 spec:
                   containers:
                   - image: IMAGE_URL
                     limits:
                       cpu: 'CPU'
                       memory: 'MEMORY'
                       nvidia.com/gpu: 'GPU_NUMBER'
                   nodeSelector:
                     run.googleapis.com/accelerator: GPU_TYPE

Replace the following:

     * `JOB`: the name of your Cloud Run job.
     * `REGION`: the Google Cloud region. For example, `europe-west1`.
     * `IMAGE_URL`: a reference to the [container image](https://docs.cloud.google.com/run/docs/building/containers)—for example, `us-docker.pkg.dev/cloudrun/container/job:latest`.
     * `CPU`: the number of CPU. For NVIDIA RTX PRO 6000 Blackwell GPU, you must specify at least `20` CPU. For L4 GPU, you must specify at least `4` CPU.
     * `MEMORY`: the amount of memory. For NVIDIA RTX PRO 6000 Blackwell GPU, you must specify at least `80Gi` (80 GiB). For L4 GPU, you must specify at least `16Gi` (16 GiB).
     * `GPU_NUMBER`: the value `1` (one) because we only support attaching one GPU per Cloud Run instance.
     * `GPU_TYPE`: the GPU type. For NVIDIA RTX PRO 6000 Blackwell GPU, enter `nvidia-rtx-pro-6000`. For L4 GPU, enter value `nvidia-l4` (nvidia-`L`4 lowercase L, not numeric value fourteen).
  3. Create or update the job using the following command:
         
         gcloud run jobs replace job.yaml

The `gcloud run jobs replace` command defaults to using `job.yaml` file if present.




## View GPU settings

To view the current GPU settings for your Cloud Run job, use the Google Cloud console or the Google Cloud CLI:

### Console

  1. In the Google Cloud console, go to the Cloud Run jobs page:

[Go to Cloud Run jobs](https://console.cloud.google.com/run/jobs)

  2. Click the job to open the **Job details** page.

  3. Click **View and edit job configuration**.

  4. Locate the GPU setting in the configuration details.




###  gcloud 

  1. Run the following command:
         
         gcloud run jobs describe JOB

  2. Locate the GPU setting in the returned configuration.




## Detach GPU resources from a job

You can detach GPU resources from a job using the Google Cloud console, the gcloud CLI, or YAML:

### Console

  1. In the Google Cloud console, go to the Cloud Run page:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Jobs** from the Cloud Run navigation menu:

     1. If you are creating a new job, click **Deploy container** to fill out the initial job settings page.

     2. If you are configuring an existing job, select the job, then click **View and edit job configuration**.

  3. Click **Containers, Connections, Security** to expand the job properties page.

  4. In the **Containers** tab, clear the **GPU** checkbox.

  5. Click **Update**.




###  gcloud 

To detach GPU resources from your Cloud Run job, set the number of GPUs to `0` using the [`gcloud run jobs update`](https://docs.cloud.google.com/sdk/gcloud/reference/run/jobs/update) command:
    
    
    gcloud run jobs update JOB --gpu 0

Replace `JOB` with the name of your Cloud Run job.

### YAML

  1. If you are creating a new job, skip this step. If you are updating an existing job, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job):
         
         gcloud run jobs describe JOB --format export > job.yaml

  2. Delete the `nvidia.com/gpu:`, the `run.googleapis.com/gpu-zonal-redundancy-disabled: 'true'`, and the `nodeSelector:  
run.googleapis.com/accelerator: GPU_TYPE` lines.

  3. Create or update the job using the following command:
         
         gcloud run jobs replace job.yaml

The `gcloud run jobs replace` command defaults to using `job.yaml` file if present.




## Driver libraries

By default, all of the NVIDIA RTX PRO 6000 Blackwell GPU and NVIDIA L4 GPU driver libraries are mounted under `/usr/local/nvidia/lib64`. Cloud Run automatically appends this path to the `LD_LIBRARY_PATH` environment variable (i.e. `${LD_LIBRARY_PATH}:/usr/local/nvidia/lib64`) of the container with the GPU. This allows the dynamic linker to find the NVIDIA driver libraries. The linker searches and resolves paths in the order you list in the `LD_LIBRARY_PATH` environment variable. Any values you specify in this variable take precedence over the default Cloud Run driver libraries path `/usr/local/nvidia/lib64`.

If you want to use a CUDA version greater than 13.0, the easiest way is to depend on a newer [NVIDIA base image](https://catalog.ngc.nvidia.com/containers) with forward compatibility packages already installed. Another option is to manually [install the NVIDIA forward compatibility packages](https://docs.nvidia.com/deploy/cuda-compatibility/#installing-the-forward-compatibility-package) and add them to `LD_LIBRARY_PATH`. Consult [NVIDIA's compatibility matrix](https://docs.nvidia.com/deeplearning/frameworks/support-matrix/index.html) to determine which CUDA versions are forward compatible with the provided NVIDIA driver version.

## About GPUs and parallelism

If you are running parallel tasks in a job execution, determine and set [parallelism](https://docs.cloud.google.com/run/docs/configuring/parallelism) value to less than the [GPU quota without zonal redundancy](https://console.cloud.google.com/projectselector2/iam-admin/quotas?pageState=\(%22allQuotasTable%22:\(%22f%22:%22%255B%257B_22k_22_3A_22Metric_22_2C_22t_22_3A10_2C_22v_22_3A_22_5C_22run.googleapis.com%252Fnvidia_l4_gpu_allocation_no_zonal_redundancy_5C_22_22_2C_22s_22_3Atrue_2C_22i_22_3A_22metricName_22%257D%255D%22\)\)) allocated for your project. To request for a quota increase, see [How to increase quota](https://docs.cloud.google.com/run/quotas#increase). GPU tasks start as quickly as possible and go up to a maximum that varies depending on how much GPU quota you allocated for the project and the region selected. Cloud Run deployments fail if you set parallelism to more than the GPU quota limit.

To calculate the GPU quota your job uses per execution, multiply the number of GPUs per job task with the parallelism value. For example, if you have a GPU quota of 10, and deploy your Cloud Run job with `--gpu=1`, `--parallelism=10`, then your job consumes all 10 GPU quota. Alternatively, if you deploy with `--gpu=1`, `--parallelism=20`, then deployments fail.

For more information, see [Best practices: Cloud Run jobs with GPUs](https://docs.cloud.google.com/run/docs/configuring/jobs/gpu-best-practices).

## What's next

See [Run AI inference on Cloud Run with GPUs](https://docs.cloud.google.com/run/docs/ai/inference) for tutorials.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
