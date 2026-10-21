---
url: https://docs.cloud.google.com/tpu/docs/jax-pods/
title: Run JAX code on TPU slices \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:24.029370+00:00
---

# Run JAX code on TPU slices  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/jax-pods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Run JAX code on TPU slices

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

Before running the commands in this document, make sure you have followed the instructions in [Set up an account and Cloud TPU project](https://docs.cloud.google.com/tpu/docs/setup-gcp-account).

After you have your JAX code running on a single TPU board, you can scale up your code by running it on a [TPU slice](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#slices). TPU slices are multiple TPU boards connected to each other over dedicated high-speed network connections. This document is an introduction to running JAX code on TPU slices; for more in-depth information, see [Using JAX in multi-host and multi-process environments](https://jax.readthedocs.io/en/latest/multi_process.html).

## Required roles

To get the permissions that you need to create a TPU and connect to it using SSH, ask your administrator to grant you the following IAM roles on your project: 

  * [TPU Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/tpu#tpu.admin) (`roles/tpu.admin`)
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`)
  * [Compute Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.viewer) (`roles/compute.viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create a Cloud TPU slice

  1. Create some environment variables:
         
         export PROJECT_ID=your-project-id
         export TPU_NAME=your-tpu-name
         export ZONE=europe-west4-b
         export ACCELERATOR_TYPE=v5litepod-32
         export RUNTIME_VERSION=v2-alpha-tpuv5-lite

#### Environment variable descriptions

     * `PROJECT_ID`: Your Google Cloud project ID. Use an existing project or [create a new one.](https://docs.cloud.google.com/tpu/docs/setup-gcp-account#set-up-project)
     * `TPU_NAME`: The name of the TPU.
     * `ZONE`: The zone in which to create the TPU VM. For more information about supported zones, see [TPU regions and zones](https://docs.cloud.google.com/tpu/docs/regions-zones). 
     * `ACCELERATOR_TYPE`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions). 
     * `RUNTIME_VERSION`: The Cloud TPU [software version](https://docs.cloud.google.com/tpu/docs/runtimes).
  2. Create a TPU slice using the `gcloud` command. For example, to create a v5litepod-32 slice use the following command:
         
         $ gcloud compute tpus tpu-vm create ${TPU_NAME}  \
             --zone=${ZONE} \
             --project=${PROJECT_ID} \
             --accelerator-type=${ACCELERATOR_TYPE}  \
             --version=${RUNTIME_VERSION} 




## Install JAX on your slice

After creating the TPU slice, you must install JAX on all hosts in the TPU slice. You can do this using the `gcloud compute tpus tpu-vm ssh` command using the `--worker=all` and `--commamnd` parameters.
    
    
    gcloud compute tpus tpu-vm ssh ${TPU_NAME} \
      --zone=${ZONE} \
      --project=${PROJECT_ID} \
      --worker=all \
      --command='pip install -U "jax[tpu]" -f https://storage.googleapis.com/jax-releases/libtpu_releases.html'

## Run JAX code on the slice

To run JAX code on a TPU slice, you must run the code **on each host in the TPU slice**. The `jax.device_count()` call stops responding until it is called on each host in the slice. The following example illustrates how to run a JAX calculation on a TPU slice.

### Prepare the code

You need `gcloud` version >= 344.0.0 (for the `[scp](https://docs.cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/scp)` command). Use `gcloud --version` to check your `gcloud` version, and run `gcloud components upgrade`, if needed.

Create a file called `example.py` with the following code:
    
    
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
    

### Copy `example.py` to all TPU worker VMs in the slice
    
    
    $ gcloud compute tpus tpu-vm scp ./example.py ${TPU_NAME}: \
      --worker=all \
      --zone=${ZONE} \
      --project=${PROJECT_ID}

If you have not previously used the `scp` command, you might see an error similar to the following:
    
    
    ERROR: (gcloud.alpha.compute.tpus.tpu-vm.scp) SSH Key is not present in the SSH
    agent. Please run `ssh-add /.../.ssh/google_compute_engine` to add it, and try
    again.
    

To resolve the error, run the `ssh-add` command as displayed in the error message and rerun the command.

### Run the code on the slice

Launch the `example.py` program on every VM:
    
    
    $ gcloud compute tpus tpu-vm ssh ${TPU_NAME} \
      --zone=${ZONE} \
      --project=${PROJECT_ID} \
      --worker=all \
      --command="python3 ./example.py"

### Output (produced with a v5litepod-32 slice):
    
    
    global device count: 32
    local device count: 4
    pmap result: [32. 32. 32. 32.]
    

## Clean up

When you are done with your TPU VM follow these steps to clean up your resources.

  1. Delete your Cloud TPU and Compute Engine resources.
         
         $ gcloud compute tpus tpu-vm delete ${TPU_NAME} \
           --zone=${ZONE} \
           --project=${PROJECT_ID}

  2. Verify the resources have been deleted by running `gcloud compute tpus execution-groups list`. The deletion might take several minutes. The output from the following command shouldn't include any of the resources created in this tutorial:
         
         $ gcloud compute tpus tpu-vm list --zone=${ZONE} \
         --project=${PROJECT_ID}




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
