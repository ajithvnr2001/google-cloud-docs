---
url: https://docs.cloud.google.com/tpu/docs/quickstart-create-multi-host-slice/
title: Quickstart: Create a multi-host TPU slice \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:38.617343+00:00
---

# Quickstart: Create a multi-host TPU slice  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/quickstart-create-multi-host-slice/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a multi-host TPU slice

Learn how to create a multi-host TPU slice using a managed instance group (MIG), connect to the slice, and run a calculation. This quickstart uses the on-demand consumption option. Run the commands in this quickstart in your local terminal or [Cloud Shell](https://docs.cloud.google.com/shell/docs/launching-cloud-shell).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  8. Enable the Compute Engine API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com

  9. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
  10. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  11. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  12. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  13. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  14. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  15. Enable the Compute Engine API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable compute.googleapis.com




### Required roles

To get the permissions that you need to create a MIG that forms a multi-host TPU slice, connect to each VM in the MIG using SSH, and run commands, ask your administrator to grant you the following IAM roles on your project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create an instance template

To create an instance template for TPU v6e VMs, use the [`gcloud compute instance-templates create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-templates/create):

**Note:** If you use a different machine type, ensure that you're using a supported OS image. For a list of Google-managed OS images for each supported TPU version, see [TPU OS images](https://docs.cloud.google.com/tpu/docs/tpu-os-images).
    
    
    gcloud compute instance-templates create quickstart-tpu-instance-template \
        --machine-type=ct6e-standard-4t \
        --maintenance-policy=TERMINATE \
        --image-family=ubuntu-accel-2204-amd64-tpu-v5e-v5p-v6e \
        --image-project=ubuntu-os-accelerator-images \
        --region=us-east5
    

## Create a workload policy

A workload policy defines physical properties of your compute instances. In TPU slices, the accelerator topology defines the physical arrangement of TPU chips. Specifying an accelerator topology is required for interconnected multi-host TPU slices.

To create a workload policy for a multi-host TPU slice, use the [`gcloud compute resource-policies create workload-policy` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/resource-policies/create/workload-policy) with the `--accelerator-topology` flag. The following command creates a workload policy with a 2x4 topology:
    
    
    gcloud compute resource-policies create workload-policy quickstart-tpu-workload-policy \
        --type=high-throughput \
        --accelerator-topology=2x4 \
        --region=us-east5
    

## Create a MIG

Run the following commands to create a MIG that forms a multi-host TPU slice.

**Note:** You might encounter a temporary [resource availability error](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-resource-availability#common_error_messages) while the MIG queues for capacity. If you experience extended wait times, you can try a different region. For a list of supported locations, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones). If you choose a different region, you must first create a workload policy in that region by repeating the Create a workload policy step. Make sure to update the region in all subsequent commands.

  1. To create a MIG that forms a multi-host TPU slice, use the [`gcloud compute instance-groups managed create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/create):
         
         gcloud compute instance-groups managed create quickstart-tpu-mig \
             --size=2 \
             --target-size-policy-mode=bulk \
             --template=quickstart-tpu-instance-template \
             --region=us-east5 \
             --target-distribution-shape=any-single-zone \
             --instance-redistribution-type=none \
             --default-action-on-vm-failure=do-nothing \
             --workload-policy=projects/PROJECT_ID/regions/us-east5/resourcePolicies/quickstart-tpu-workload-policy
         

Replace `PROJECT_ID` with your Google Cloud project ID.

  2. Verify that the managed instances are running by using the following commands:

     * To view the overall MIG status, use the [`gcloud compute instance-groups managed describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe):
           
           gcloud compute instance-groups managed describe quickstart-tpu-mig \
               --region=us-east5
           

     * To view the status of each instance, use the [`gcloud compute instance-groups managed list-instances` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/list-instances):
           
           gcloud compute instance-groups managed list-instances quickstart-tpu-mig \
               --region=us-east5
           

**Caution:** Ensure that all instances are in the `RUNNING` state before proceeding. Attempting to connect to instances by using SSH while they are still provisioning results in an error.



## Install JAX

Install dependencies and the JAX framework in a virtual environment on all TPU VM instances in the MIG. If your TPU VMs have a Python version earlier than 3.11 installed, you must install Python 3.11 to run the latest version of JAX.

  1. Check which Python version is running on your TPU VMs:
         
         gcloud compute instance-groups managed list-instances quickstart-tpu-mig \
             --region=us-east5 \
             --uri \
         | xargs -I {} -P 0 gcloud compute ssh {} \
             --command='python3 --version'
         

If the version is earlier than Python 3.11, install Python 3.11:
         
         gcloud compute instance-groups managed list-instances quickstart-tpu-mig \
             --region=us-east5 \
             --uri \
         | xargs -I {} -P 0 gcloud compute ssh {} \
             --command='sudo apt update && \
             sudo apt install -y software-properties-common && \
             sudo add-apt-repository -y ppa:deadsnakes/ppa && \
             sudo apt update && \
             sudo apt install -y python3.11 python3.11-dev'
         

  2. Create a virtual environment:
         
         gcloud compute instance-groups managed list-instances quickstart-tpu-mig \
             --region=us-east5 \
             --uri \
         | xargs -I {} -P 0 gcloud compute ssh {} \
             --command='sudo apt install -y python3.11-venv && \
             python3.11 -m venv ~/jax_venv'
         

  3. Install JAX in the virtual environment:
         
         gcloud compute instance-groups managed list-instances quickstart-tpu-mig \
             --region=us-east5 \
             --uri \
         | xargs -I {} -P 0 gcloud compute ssh {} \
             --command='source ~/jax_venv/bin/activate && \
             pip install --upgrade pip -q && \
             pip install jax[tpu] -f https://storage.googleapis.com/jax-releases/libtpu_releases.html -q'
         




## Run JAX code on the slice

To run JAX code on a TPU slice, you must run the code on each host in the TPU slice. The `jax.device_count()` function call stops responding until it's called on each host in the slice. The following example shows how to run a JAX calculation on a TPU slice.

### Prepare the code

Create a file called `example.py` on each instance:
    
    
    gcloud compute instance-groups managed list-instances quickstart-tpu-mig \
        --region=us-east5 \
        --uri \
    | xargs -I {} -P 0 gcloud compute ssh {} \
        --command="cat << 'EOF' > ~/example.py
    import jax
    
    # Initialize the slice
    jax.distributed.initialize()
    
    # The total number of TPU cores in the slice
    device_count = jax.device_count()
    
    # The number of TPU cores attached to this host
    local_device_count = jax.local_device_count()
    
    # The psum is performed over all mapped devices across the slice
    xs = jax.numpy.ones(jax.local_device_count())
    r = jax.pmap(lambda x: jax.lax.psum(x, 'i'), axis_name='i')(xs)
    
    # Print from a single host to avoid duplicated output
    if jax.process_index() == 0:
        print('global device count:', jax.device_count())
        print('local device count:', jax.local_device_count())
        print('pmap result:', r)
    EOF"
    

### Run the code on the slice

Run the `example.py` program on each TPU VM in the slice:
    
    
    gcloud compute instance-groups managed list-instances quickstart-tpu-mig \
        --region=us-east5 \
        --uri \
    | xargs -I {} -P 0 gcloud compute ssh {} \
        --command='source ~/jax_venv/bin/activate && python3 ~/example.py'
    

The output should be similar to the following:
    
    
    global device count: 8
    local device count: 4
    pmap result: [8. 8. 8. 8.]
    

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

Alternatively, if you want to keep your project, you can delete only the MIG and all VMs in the group by using the [`gcloud compute instance-groups managed delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/delete):
    
    
    gcloud compute instance-groups managed delete quickstart-tpu-mig --region=us-east5
    

## What's next

  * Learn about [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine)
  * [Create a multi-host TPU slice using other consumption options](https://docs.cloud.google.com/tpu/docs/create-multi-host-mig)
  * Learn about [TPU instances in MIGs](https://docs.cloud.google.com/tpu/docs/tpus-and-migs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
