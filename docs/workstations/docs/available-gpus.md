---
url: https://docs.cloud.google.com/workstations/docs/available-gpus/
title: Available GPUs \u00a0|\u00a0 Cloud Workstations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:42.263550+00:00
---

# Available GPUs  |  Cloud Workstations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workstations/docs/available-gpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Workstations ](https://docs.cloud.google.com/workstations/docs)
  * [ Guides ](https://docs.cloud.google.com/workstations/docs/overview)



Send feedback 

#  Available GPUs Stay organized with collections  Save and categorize content based on your preferences. 

GPUs are used to accelerate workloads, and Cloud Workstations supports attaching GPUs to workstations. Cloud Workstations supports many of the various [GPU models](https://docs.cloud.google.com/compute/docs/gpus) that are available to attach to Compute Engine VMs. The model and quantity of GPUs to attach to each workstation are specified on the workstation configuration. Cloud Workstations handles attaching the GPUs and installing their device drivers.

Attaching GPUs to workstations will affect costs as described in the [Cloud Workstations pricing](https://cloud.google.com/workstations/pricing#pricing-overview) overview.

## Limitations

A workstation configuration may specify GPUs, subject to the following limitations:

  * Cloud Workstations only supports GPUs for configurations that specify machine types in the [N1 machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines), the [A2 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-vms), or the [A3 machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms). Refer to [supported GPU models](https://docs.cloud.google.com/workstations/docs/available-gpus#supported_gpu_models) for details.
  * The configuration must specify [replica zones](https://docs.cloud.google.com/workstations/docs/reference/rest/v1/projects.locations.workstationClusters.workstationConfigs#WorkstationConfig.FIELDS.replica_zones) where the chosen GPU model is available.
  * It is not possible to configure workstations to have more than one model of GPU attached at a time.
  * Configurations that specify A2 Ultra machine types must not specify persistent storage. Consider using an NFS-based solution such as [Filestore](https://docs.cloud.google.com/workstations/docs/mount-filestore-nfs-instances) or [Cloud Storage FUSE](https://cloud.google.com/storage/docs/cloud-storage-fuse/overview) if persistent file storage is required. Note that A2 Standard machine types do support persistent storage. To create configurations without persistent storage, use the following Google Cloud CLI command:
        
        gcloud workstations configs create CONFIG_NAME \
            --project=PROJECT_ID \
            --cluster=CLUSTER_NAME \
            --region=LOCATION \
            --machine-type=A2_MACHINE_TYPE \
            --no-persistent-storage
        

Replace the following:

    * `PROJECT_ID`: the ID of the project that contains the workstation configuration.
    * `LOCATION`: the region of the workstation cluster.
    * `CLUSTER_NAME`: the name workstation cluster that contains the workstation configuration.
    * `CONFIG_NAME`: the name of the workstation configuration.
    * `A2_MACHINE_TYPE`: the type of the A2 machine.
  * Configurations that specify A3 machine types only support Hyperdisk persistent volumes.

  * Using Google Cloud Hyperdisk disk types is only supported on these following machine series:

    * A3
    * C3
    * C4
    * G4
    * M3
    * N4
    * N4D
    * Z3



## Supported GPU models

Cloud Workstations supports many of the GPU models that Compute Engine makes available. The models that are supported depend on the machine series chosen for the workstation configuration, as summarized in the following table.

### N1 machine series

The [N1 general-purpose machine series](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1_machines) supports several GPU models, and workstation configurations that specify any of the N1 machine types can also specify one of the following GPU models. For the chosen GPU model, the configuration may specify a count of how many GPU cards to attach to each workstation. 

**Caution:** NVIDIA P100 GPUs reach end of support on September 15, 2026. For more information, see [NVIDIA P100 end of support](https://docs.cloud.google.com/compute/docs/eol/p100-eos). 

GPU model | GPU counts  
---|---  
[NVIDIA T4](https://www.nvidia.com/en-us/data-center/tesla-t4/) (`nvidia-tesla-t4`) | 1, 2, or 4 GPUs  
[NVIDIA P4](https://www.nvidia.com/en-us/deep-learning-ai/inference-platform/hpc/) (`nvidia-tesla-p4`) | 1, 2, or 4 GPUs  
[NVIDIA V100](https://www.nvidia.com/en-us/data-center/v100/) (`nvidia-tesla-v100`) | 1, 2, 4, or 8 GPUs  
[NVIDIA P100](http://www.nvidia.com/object/tesla-p100.html) (`nvidia-tesla-p100`) | 1, 2, or 4 GPUs  
  
### A2 machine series

The [A2 Standard](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-standard-vms) and [A2 Ultra accelerator-optimized machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a2-ultra-vms) have a fixed number of NVIDIA A100 GPUs attached, based solely on the chosen machine type. 

The following table shows the mapping from machine type to the number of cards that will be attached.

GPU model | [Machine type](https://docs.cloud.google.com/compute/docs/gpus/about-gpus#gpu-machine-types) | GPU count  
---|---|---  
[NVIDIA A100 40GB](https://www.nvidia.com/en-us/data-center/a100/) (`nvidia-tesla-a100`) | `a2-highgpu-1g` | 1 GPU  
`a2-highgpu-2g` | 2 GPUs  
`a2-highgpu-4g` | 4 GPUs  
`a2-highgpu-8g` | 8 GPUs  
`a2-megagpu-16g` | 16 GPUs  
[NVIDIA A100 80GB](https://www.nvidia.com/en-us/data-center/a100/) (`nvidia-a100-80gb`) | `a2-ultragpu-1g` | 1 GPU  
`a2-ultragpu-2g` | 2 GPUs  
`a2-ultragpu-4g` | 4 GPUs  
`a2-ultragpu-8g` | 8 GPUs  
  
### A3 machine series

The [A3 Mega and A3 High accelerator-optimized machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) has a fixed number of NVIDIA H100 GPUs attached, based solely on the chosen machine type. 

The following table shows the mapping from machine type to the number of cards that will be attached.

GPU model | [Machine type](https://docs.cloud.google.com/compute/docs/gpus/about-gpus#gpu-machine-types) | GPU count  
---|---|---  
[NVIDIA H100 80GB](https://www.nvidia.com/en-us/data-center/a100/) (`nvidia-tesla-h100`) | `a3-highgpu-8g` | 8 GPUs  
`a3-megagpu-8g` | 8 GPUs  
  
### Google Cloud Hyperdisk Support

Some GPU workloads require very high disk throughput. To satisfy this use case, Cloud Workstations allows the use of [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) Balanced High Availability disks as persistent directories for the machine types enumerated earlier.

Hyperdisk storage can be configured through both the Console and with the `gcloud` CLI. **It is not possible to change the disk type after creating a Workstation configuration**.

**Warning:** It is not possible to switch to Hyperdisk after the Workstation configuration is created. To switch a workstation's backing home disk, you must create a new configuration using Hyperdisk and then manually [clone the workstation](https://docs.cloud.google.com/workstations/docs/clone-workstation) to the new configuration. 

Attaching a Hyperdisk to a Workstation will affect costs as described in [Google Cloud Hyperdisk pricing](https://cloud.google.com/compute/disks-image-pricing).

## Add GPUs to an Existing Workstation Configuration

To add GPUs to a workstation configuration, complete the steps in one of the following tabs.

### Before you begin

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
    
    
    gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the `gcloud` CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

Review the [Cloud Workstations pricing](https://cloud.google.com/workstations/pricing#pricing-overview) overview to understand how your costs will be affected by configuring GPUs. Note that GPUs are attached to the pre-started virtual machines (VMs) specified by a configuration's **Quick start pool size**.

### Updating your existing configuration

###  Console 

Configure GPUs on an existing workstation configuration from the Google Cloud console, by doing the following:

  1. In the Google Cloud console, go to the **Workstation configurations** page.

[Go to Workstation configurations](https://console.cloud.google.com/workstations/configurations)

  2. In the **Workstation configurations** list, click the **Name** of the configuration to add GPUs to.

  3. On the **Workstation configuration details** page, click edit **Edit**.

  4. On the **Edit workstation configuration** page, click **Machine settings** in the navigation menu.

  5. Click the toggle to select **GPUs** instead of the **General purpose** machine family.

In the **GPU type** field, select the GPU Model that you want to use.

In the **Number of GPUs** field, select the number of GPU cards you want to attach to each workstation.

In the **Machine type** field, select the machine type you want to use.

**Note:** the options for each field vary depending on the replica zones chosen for the configuration and the GPU and [machine type](https://docs.cloud.google.com/compute/docs/regions-zones#available) availability in those zones. If you cannot find suitable GPUs in the replica zones for this configuration, you may decide to create a new configuration with GPUs instead.
  6. Click **Save** to update the configuration.




###  gcloud 

Configure GPUs on an existing workstation configuration by running the [`gcloud workstations configs update` command](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update).

First though, collect some information to see which GPU models are available and to choose one for your configuration:

  1. Check which replica zones the configuration specifies by running the following `gcloud` CLI command:
         
         gcloud workstations configs describe \
           --format="table(name.scope(workstationConfigs),replicaZones.list())" \
           --project=PROJECT_ID \
           --region=LOCATION \
           --cluster=CLUSTER_NAME \
           CONFIG_NAME
         

Replace the following:

     * `PROJECT_ID`: the ID of the project that contains the workstation configuration.
     * `LOCATION`: the location of the workstation cluster.
     * `CLUSTER_NAME`: the name workstation cluster that contains the workstation configuration.
     * `CONFIG_NAME`: the name of the workstation configuration.
  2. Choose a supported GPU model that is available in _both_ of the configuration's replica zones by running the [`gcloud compute accelerator-types list` command](https://cloud.google.com/sdk/gcloud/reference/compute/accelerator-types/list):
         
         gcloud compute accelerator-types list \
           --format="table(name:sort=1,zone,description,maximumCardsPerInstance)" \
           --filter='zone.basename()=(ZONES) AND name~"nvidia-tesla-(a100|p100|p4|t4|v100)$"' \
           --project=PROJECT_ID
         

Replace `ZONES` with a comma-separated list of the replica zones determined in the previous step (for example, `us-central1-a,us-central1-c`).

Choose a GPU model that is listed twice in the table, indicating it is available in both replica zones.

Take note of the maximum cards you can attach for the chosen GPU model.

**Note:** If there isn't suitable GPU Availability in the replica zones for this configuration, you may decide to create a new configuration with GPUs instead.
  3. Determine which of the supported machine types are available in _both_ of the configuration's replica zones using the [`gcloud compute machine-types list` command](https://cloud.google.com/sdk/gcloud/reference/compute/machine-types/list).

     1. If you chose the NVIDIA A100 40GB GPU model in the previous step, your configuration must use the A2 machine series:
            
            gcloud compute machine-types list \
              --format="table(name,zone,guestCpus:sort=1)" \
              --filter="name:a2-highgpu- OR name:a2-megagpu-" \
              --zones=ZONES \
              --project=PROJECT_ID
            

     2. If you chose any other GPU model in the previous step, your configuration must use the N1 machine series:
            
            gcloud compute machine-types list \
              --format="table(name,zone,guestCpus:sort=1)" \
              --filter="name:n1-standard-" \
              --zones=ZONES \
              --project=PROJECT_ID
            

Choose a machine type that is _listed twice_ in the table, indicating it is available in _both replica zones_.

  4. Now that you have selected a GPU model and compatible machine type, update the configuration:

     1. For NVIDIA A100 40GB GPUs, run this command to update your configuration:
            
            gcloud beta workstations configs update \
              --project=PROJECT_ID \
              --region=LOCATION \
              --cluster=CLUSTER_NAME \
              CONFIG_NAME \
              --machine-type=A2_MACHINE_TYPE
            

Replace `A2_MACHINE_TYPE` with the chosen A2 machine type determined in the previous step (for example, `a2-highgpu-1g`).

**Note:** for the A2 machine series the model and quantity of GPUs is fixed based on the machine type, so you may omit the `--accelerator-type` and `--accelerator-count` flags.
     2. For all other GPU models, run this command:
            
            gcloud beta workstations configs update \
              --project=PROJECT_ID \
              --region=LOCATION \
              --cluster=CLUSTER_NAME \
              CONFIG_NAME \
              --machine-type=N1_MACHINE_TYPE \
              --accelerator-type=ACCELERATOR_TYPE \
              --accelerator-count=ACCELERATOR_COUNT
            

Replace the following:

        * `N1_MACHINE_TYPE`: the chosen machine type from the N1 series (for example, `n1-standard-2`).
        * `ACCELERATOR_TYPE`: the chosen GPU model's name (for example, `nvidia-tesla-t4`).
        * `ACCELERATOR_COUNT`: the number of GPUs to attach to each workstation (for example, `1`, `2`, `4`). Must be a power of two less than the maximum for the GPU model.



## Create a new Workstation Configuration with GPUs

To create a new workstation configuration that attaches GPUs to workstations that are based on it, complete the steps in one of the following tabs.

### Before you begin

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
    
    
    gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the `gcloud` CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the `gcloud` CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the `gcloud` CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 




For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

Choose a GPU model and consult the GPU availability table to select a region where the chosen GPU model is available in at _least two_ zones.

If you don't already have a cluster in the chosen region where you can create a new configuration, follow the steps to [Create a workstation cluster](https://docs.cloud.google.com/workstations/docs/create-cluster) in the region.

Review the [Cloud Workstations pricing](https://cloud.google.com/workstations/pricing#pricing-overview) overview to understand how your costs will be affected by configuring GPUs. Note that GPUs are attached to the pre-started virtual machines (VMs) specified by a configuration's **Quick start pool size**.

### Creating a new configuration

###  Console 

Create a new workstation configuration with GPUs from the Google Cloud console, by doing the following:

  1. In the Google Cloud console, go to the **Workstation configurations** page.

[Go to Workstation configurations](https://console.cloud.google.com/workstations/configurations)

  2. On the **Workstation configurations** page, click add_box **Create**.

  3. On the **Basic information** step of the **Create workstation configuration** page, specify a name for your configuration in the **Name** field.

In the **Workstation cluster** field, select a cluster in the chosen region.

**Tip:** GPUs are also attached to **Quick start workstations**. You can keep costs down by selecting **Disabled**.

Click **Continue** to advance to the **Machine settings** step.

  4. On the **Machine settings** step of the **Create workstation configuration** page, begin by clicking the toggle to select **GPUs** instead of the **General purpose** machine family.

     1. Then, in the **Zones** field, select the checkboxes next to two zones where the GPU model you chose is available (see the GPU availability table).

     2. In the **GPU type** field, select the GPU Model that you want to use.

     3. In the **Number of GPUs** field, select the number of GPU cards you want to attach to each workstation.

     4. In the **Machine type** field, select a compatible machine type.

  5. **Optional:** This feature is not yet supported in the UI. See the `gcloud` instructions to use the CLI to configure this feature.

  6. Click **Continue** to configure the Environment settings and Identity and Access Management (IAM) policy before clicking **Create** to provision the new workstation configuration.




###  gcloud 

Create a new workstation configuration with GPUs using the `gcloud` CLI, by running the [`gcloud workstations configs create` command](https://cloud.google.com/sdk/gcloud/reference/workstations/configs/update).

  * For NVIDIA A100 40GB GPUs run this command to create your configuration:
        
        gcloud beta workstations configs create \
          --project=PROJECT_ID \
          --region=LOCATION \
          --cluster=CLUSTER_NAME \
          CONFIG_NAME \
          --replica-zones=REPLICA_ZONES \
          --machine-type=A2_MACHINE_TYPE
        

Replace the following:

    * `PROJECT_ID`: the ID of the project that will contain the new workstation configuration.
    * `LOCATION`: the location of the workstation cluster where the configuration will be contained.
    * `CLUSTER_NAME`: the name workstation cluster that will contain the new workstation configuration.
    * `CONFIG_NAME`: the name of the new workstation configuration.
    * `REPLICA_ZONES`: exactly two zones in the cluster's region where the chosen GPU model is available (for example, `us-central1-a,us-central1-c`).
    * `A2_MACHINE_TYPE`: the chosen A2 series machine type (for example, `a2-highgpu-1g`).
**Note:** for the A2 machine series the model and quantity of GPUs is fixed based on the machine type, so you may omit the `--accelerator-type` and `--accelerator-count` flags.
  * For all other GPU models, run this command to create your configuration:
        
        gcloud beta workstations configs create \
          --project=PROJECT_ID \
          --region=LOCATION \
          --cluster=CLUSTER_NAME \
          CONFIG_NAME \
          --replica-zones=REPLICA_ZONES \
          --machine-type=N1_MACHINE_TYPE \
          --accelerator-type=ACCELERATOR_TYPE \
          --accelerator-count=ACCELERATOR_COUNT
        

Replace the following:

    * `PROJECT_ID`: the ID of the project that will contain the new workstation configuration.
    * `LOCATION`: the location of the workstation cluster where the configuration will be contained.
    * `CLUSTER_NAME`: the name workstation cluster that will contain the new workstation configuration.
    * `CONFIG_NAME`: the name of the new workstation configuration.
    * `REPLICA_ZONES`: exactly two zones in the cluster's region where the chosen GPU model is available (for example, `us-central1-a,us-central1-c`).
    * `N1_MACHINE_TYPE`: the chosen N1 series machine type (for example, `n1-standard-2`).
    * `ACCELERATOR_TYPE`: the chosen GPU model's name (for example, `nvidia-tesla-t4`).
    * `ACCELERATOR_COUNT`: the number of GPUs to attach to each workstation (for example, `1`, `2`, `4`).
  * **Optional:** To use a Hyperdisk, add flag `--disk-type=hyperdisk-balanced-ha`. For example:
        
        gcloud beta workstations configs create \
          ... \
          --disk-type=hyperdisk-balanced-ha \
          --disk-size=200
        

This command will create a Hyperdisk with size 200 GB. The disk type cannot be changed after creating the Workstation configuration.




## NVIDIA GPU device drivers

Cloud Workstations installs the NVIDIA device drivers on workstations' host VMs during VM startup.

To determine which version device driver has been installed on a workstation, run the following command:
    
    
    nvidia-smi --query-gpu=name,driver_version --format=csv
    

## GPU availability by region and zone

You can search either by location or GPU model, or a combination of both.

A100 40GBA100 80GBH100P100P4RTX 6000T4V100

Clear all

Zones | Location | [GPU platforms](https://docs.cloud.google.com/compute/docs/gpus)  
---|---|---  
`asia-east1-a` | Taiwan | P100, RTX 6000, T4  
`asia-east1-b` | Taiwan | RTX 6000  
`asia-east1-c` | Taiwan | H100, P100, T4, V100  
`asia-east2-a` | Hong Kong | T4  
`asia-east2-b` | Hong Kong |   
`asia-east2-c` | Hong Kong | T4  
`asia-northeast1-a` | Tokyo | A100 40GB, T4  
`asia-northeast1-b` | Tokyo | H100  
`asia-northeast1-c` | Tokyo | A100 40GB, T4  
`asia-northeast3-a` | Seoul | A100 40GB, H100  
`asia-northeast3-b` | Seoul | A100 40GB, T4  
`asia-northeast3-c` | Seoul | H100, T4  
`asia-south1-a`  
`asia-south1-b` | Mumbai | T4  
`asia-south1-c` | Mumbai | H100, RTX 6000  
`asia-southeast1-a` | Singapore | A100 40GB, P4, RTX 6000, T4  
`asia-southeast1-b` | Singapore | A100 40GB, H100, P4, RTX 6000, T4  
`asia-southeast1-c` | Singapore | A100 40GB, A100 80GB, H100, P4, RTX 6000, T4  
`australia-southeast1-a` | Sydney | P4, T4  
`australia-southeast1-b` | Sydney | P100, P4  
`australia-southeast1-c` | Sydney | H100, T4  
`australia-southeast2-a`  
`australia-southeast2-b`  
`australia-southeast2-c` | Melbourne |   
`europe-central2-a` | Warsaw |   
`europe-central2-b`  
`europe-central2-c` | Warsaw | T4  
`europe-north1-a`  
`europe-north1-b` | Finland | RTX 6000  
`europe-north1-c` | Finland | H100, RTX 6000  
`europe-southwest1-a`  
`europe-southwest1-b`  
`europe-southwest1-c` | Madrid |   
`europe-west1-b` | Belgium | H100, P100, T4  
`europe-west1-c` | Belgium | H100, RTX 6000, T4  
`europe-west1-d` | Belgium | P100, T4  
`europe-west12-a`  
`europe-west12-b` | Turin |   
`europe-west2-a` | London | T4  
`europe-west2-b` | London | H100, RTX 6000, T4  
`europe-west2-c` | London | RTX 6000  
`europe-west3-a` | Frankfurt | H100  
`europe-west3-b` | Frankfurt | T4  
`europe-west3-c` | Frankfurt | H100  
`europe-west4-a` | Netherlands | A100 40GB, A100 80GB, P100, RTX 6000, T4, V100  
`europe-west4-b` | Netherlands | A100 40GB, H100, P4, RTX 6000, T4, V100  
`europe-west4-c` | Netherlands | H100, P4, T4, V100  
`europe-west6-a`  
`europe-west6-b`  
`europe-west6-c` | Zurich |   
`europe-west8-a` | Milan |   
`europe-west8-b` | Milan | RTX 6000  
`europe-west8-c` | Milan | H100  
`europe-west9-a`  
`europe-west9-b` | Paris |   
`europe-west9-c` | Paris | H100  
`me-central2-a`  
`me-central2-b`  
`me-central2-c` | Dammam |   
`me-west1-a` | Tel Aviv | A100 40GB  
`me-west1-b` | Tel Aviv | T4  
`me-west1-c` | Tel Aviv | A100 40GB, T4  
`northamerica-northeast1-a`  
`northamerica-northeast1-b` | Montréal | P4  
`northamerica-northeast1-c` | Montréal | P4, T4  
`southamerica-east1-a`  
`southamerica-east1-b`  
`southamerica-east1-c` | São Paulo | T4  
`southamerica-west1-a`  
`southamerica-west1-b`  
`southamerica-west1-c` | Santiago |   
`us-central1-a` | Iowa | A100 40GB, A100 80GB, H100, P4, T4, V100  
`us-central1-b` | Iowa | A100 40GB, H100, RTX 6000, T4, V100  
`us-central1-c` | Iowa | A100 40GB, A100 80GB, H100, P100, P4, T4, V100  
`us-central1-f` | Iowa | A100 40GB, P100, RTX 6000, T4, V100  
`us-east1-b` | South Carolina | A100 40GB, P100, RTX 6000, T4, V100  
`us-east1-c` | South Carolina | P100, T4, V100  
`us-east1-d` | South Carolina | RTX 6000, T4  
`us-east4-a` | Northern Virginia | H100, P4, T4  
`us-east4-b` | Northern Virginia | H100, P4, RTX 6000, T4  
`us-east4-c` | Northern Virginia | A100 80GB, H100, P4, RTX 6000, T4  
`us-east5-a` | Columbus | A100 80GB, H100, RTX 6000  
`us-east5-b` | Columbus | A100 80GB, RTX 6000  
`us-east5-c` | Columbus | RTX 6000  
`us-west1-a` | Oregon | H100, P100, RTX 6000, T4, V100  
`us-west1-b` | Oregon | A100 40GB, H100, P100, RTX 6000, T4, V100  
`us-west1-c` | Oregon | RTX 6000  
`us-west4-a` | Las Vegas | H100, RTX 6000, T4  
`us-west4-b` | Las Vegas | A100 40GB, T4  
`us-west4-c` | Las Vegas | RTX 6000  
  
## What's next

  * Specify GPUs using the [Cloud Workstations API](https://docs.cloud.google.com/workstations/docs/reference/rest/v1beta/projects.locations.workstationClusters.workstationConfigs#WorkstationConfig).

  * Learn about [Running Compute Engine instances with GPU accelerators](https://docs.cloud.google.com/container-optimized-os/docs/how-to/run-gpus).

  * See the complete list of [Compute Engine machine types](https://docs.cloud.google.com/compute/docs/machine-types).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
