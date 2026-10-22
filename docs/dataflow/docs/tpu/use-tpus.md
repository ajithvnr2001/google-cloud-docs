---
url: https://docs.cloud.google.com/dataflow/docs/tpu/use-tpus/
title: Run a pipeline with TPUs \u00a0|\u00a0 Cloud Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:49.143621+00:00
---

# Run a pipeline with TPUs  |  Cloud Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/tpu/use-tpus/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Run a pipeline with TPUs Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to run an Apache Beam pipeline on Dataflow with TPUs. Jobs that use TPUs incur charges as specified in the Dataflow [pricing page](https://cloud.google.com/dataflow/pricing).

For more information about using TPUs with Dataflow, see [Dataflow support for TPUs](https://docs.cloud.google.com/dataflow/docs/tpu/tpu-support).

## Optional: Make a specific reservation to use accelerators

While you can use TPUs on-demand, we strongly recommend you use Dataflow TPUs with [_specifically targeted_ Google Cloud reservations](https://docs.cloud.google.com/dataflow/docs/guides/compute-engine-reservations#reservations-accelerators). This helps to ensure you have access to available accelerators and quick worker startup times. Pipelines that consume a TPU reservation don't require additional TPU quota.

If you don't make a reservation and choose to use TPUs on-demand, provision TPU quota before you run your pipeline.

## Optional: Provision TPU quota

You can use TPUs in an on-demand capacity or using a reservation. If you want to use TPUs on-demand, you must provision TPU quota before you do. If you use a _specifically targeted_ reservation, you can skip this section.

To use TPUs on-demand without a reservation, check the limit and current usage of your Compute Engine API quota for TPUs as follows:

###  Console 

  1. Go to the **Quotas** page in the Google Cloud console:

[Go to Quotas](https://console.cloud.google.com/iam-admin/quotas)

  2. In the filter_list **Filter** box, do the following:

     1. Use the following table to select and copy the property of the quota based on the TPU version and machine type. For example, if you plan to create on-demand TPU v5e nodes whose machine type begins with `ct5lp-`, enter `Name: TPU v5 Lite PodSlice chips`.

TPU version, machine type begins with | Property and name of the quota for on-demand instances  
---|---  
TPU v5e,  
`ct5lp-` | 
            
            Name:  
            TPU v5 Lite PodSlice chips  
  
TPU v5p,  
`ct5p-` | 
            
            Name:  
            TPU v5p chips  
  
TPU v6e,  
`ct6e-` | 
            
            Dimensions (e.g. location):  
            tpu_family:CT6E  
  
     2. Select the **Dimensions (e.g. location)** property and enter `region:` followed by the name of the region in which you plan to start your pipeline. For example, enter `region:us-west4` if you plan to use the zone `us-west4-a`. TPU quota is regional, so all zones within the same region consume the same TPU quota.




## Configure a custom container image

To interact with TPUs in Dataflow pipelines, you need to provide software that can operate on XLA devices in your pipeline runtime environment. This requires installing TPU libraries based on your pipeline needs and configuring environment variables based on the TPU device you use.

To customize the container image, install Apache Beam into an [off-the-shelf base image](https://docs.cloud.google.com/dataflow/docs/guides/build-container-image#use_a_custom_base_image) that has the necessary TPU libraries. Alternatively, install the TPU software [into the images published](https://docs.cloud.google.com/dataflow/docs/guides/build-container-image#base-images) with Apache Beam SDK releases.

To provide a custom container image, use the `sdk_container_image` pipeline option. For more information, see [Use custom containers in Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/using-custom-containers).

When you use a TPU accelerator, you need to set the following environment variables in the container image.
    
    
    ENV TPU_SKIP_MDS_QUERY=1 # Don't query metadata
    ENV TPU_HOST_BOUNDS=1,1,1 # There's only one host
    ENV TPU_WORKER_HOSTNAMES=localhost
    ENV TPU_WORKER_ID=0 # Always 0 for single-host TPUs
    

Depending on the accelerator you use, the variables in the following table also need to be set.

type | topology | Required Dataflow `worker_machine_type` | additional environment variables  
---|---|---|---  
tpu-v5-lite-podslice | 1x1 | ct5lp-hightpu-1t | 
    
    
    TPU_ACCELERATOR_TYPE=v5litepod-1  
    TPU_CHIPS_PER_HOST_BOUNDS=1,1,1  
  
tpu-v5-lite-podslice | 2x2 | ct5lp-hightpu-4t | 
    
    
    TPU_ACCELERATOR_TYPE=v5litepod-4  
    TPU_CHIPS_PER_HOST_BOUNDS=2,2,1  
  
tpu-v5-lite-podslice | 2x4 | ct5lp-hightpu-8t | 
    
    
    TPU_ACCELERATOR_TYPE=v5litepod-8  
    TPU_CHIPS_PER_HOST_BOUNDS=2,4,1  
  
tpu-v6e-slice | 1x1 | ct6e-standard-1t | 
    
    
    TPU_ACCELERATOR_TYPE=v6e-1  
    TPU_CHIPS_PER_HOST_BOUNDS=1,1,1  
  
tpu-v6e-slice | 2x2 | ct6e-standard-4t | 
    
    
    TPU_ACCELERATOR_TYPE=v6e-4  
    TPU_CHIPS_PER_HOST_BOUNDS=2,2,1  
  
tpu-v6e-slice | 2x4 | ct6e-standard-8t | 
    
    
    TPU_ACCELERATOR_TYPE=v6e-8  
    TPU_CHIPS_PER_HOST_BOUNDS=2,4,1  
  
tpu-v5p-slice | 2x2x1 | ct5p-hightpu-4t | 
    
    
    TPU_ACCELERATOR_TYPE=v5p-8  
    TPU_CHIPS_PER_HOST_BOUNDS=2,2,1  
  
A sample Dockerfile for the custom container image might look like the following example:
    
    
    FROM python:3.11-slim
    
    COPY --from=apache/beam_python3.11_sdk:2.66.0 /opt/apache/beam /opt/apache/beam
    
    # Configure the environment to access TPU device
    
    ENV TPU_SKIP_MDS_QUERY=1
    ENV TPU_HOST_BOUNDS=1,1,1
    ENV TPU_WORKER_HOSTNAMES=localhost
    ENV TPU_WORKER_ID=0
    
    # Configure the environment for the chosen accelerator.
    # Adjust according to the accelerator you use.
    ENV TPU_ACCELERATOR_TYPE=v5litepod-1
    ENV TPU_CHIPS_PER_HOST_BOUNDS=1,1,1
    
    # Install TPU software stack.
    RUN pip install jax[tpu] apache-beam[gcp]==2.66.0 -f https://storage.googleapis.com/jax-releases/libtpu_releases.html
    
    ENTRYPOINT ["/opt/apache/beam/boot"]
    

## Run your job with TPUs

The considerations for running a Dataflow job with TPUs include the following:

  * Because TPU containers can be large, to avoid running out of disk space, increase the default boot disk size to 50 gigabytes or an appropriate size as required by your container image by using the `--disk_size_gb` pipeline option.
  * Limit intra-worker parallelism.



### TPUs and worker parallelism

In the default configuration, Dataflow Python pipelines launch [one Apache Beam SDK process per VM core](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-oom#dofn). TPU machine types have a large number of vCPU cores, but only one process may perform computations on a TPU device. Additionally, a TPU device might be reserved by a process for the lifetime of the process. Therefore, you must limit intra-worker parallelism when running a Dataflow TPU pipeline. To limit worker parallelism, use the following guidance:

  * If your use case involves running inferences on a model, use the Beam `RunInference` API. For more information, see [Large Language Model Inference in Beam](https://beam.apache.org/documentation/ml/large-language-modeling/).
  * If you cannot use the Beam `RunInference` API, use Beam's [multi-process shared](https://beam.apache.org/releases/pydoc/current/apache_beam.utils.multi_process_shared.html) objects to restrict certain operations to a single process.
  * If you cannot use the preceding recommendations and prefer to launch [only one Python process per worker](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-oom#one-sdk), set the `--experiments=no_use_multiple_sdk_containers` pipeline option.
  * You can further reduce the number of threads by using the `--number_of_worker_harness_threads` pipeline option if that achieves better performance.



The following table lists the total compute resources per worker for each TPU configuration.

TPU type | topology | machine type | TPU chips | vCPU | RAM (GB)  
---|---|---|---|---|---  
tpu-v5-lite-podslice | 1x1 | ct5lp-hightpu-1t | 1 | 24 | 48  
tpu-v5-lite-podslice | 2x2 | ct5lp-hightpu-4t | 4 | 112 | 192  
tpu-v5-lite-podslice | 2x4 | ct5lp-hightpu-8t | 8 | 224 | 384  
tpu-v6e-slice | 1x1 | ct6e-standard-1t | 1 | 44 | 176  
tpu-v6e-slice | 2x2 | ct6e-standard-4t | 4 | 180 | 720  
tpu-v6e-slice | 2x4 | ct6e-standard-8t | 8 | 360 | 1440  
tpu-v5p-slice | 2x2x1 | ct5p-hightpu-4t | 4 | 208 | 448  
  
### Run a pipeline with TPUs

To run a Dataflow job with TPUs, use the following command.
    
    
    python PIPELINE \
      --runner "DataflowRunner" \
      --project "PROJECT" \
      --temp_location "gs://BUCKET/tmp" \
      --region "REGION" \
      --dataflow_service_options "worker_accelerator=type:TPU_TYPE;topology:TPU_TOPOLOGY" \
      --worker_machine_type "MACHINE_TYPE" \
      --disk_size_gb "DISK_SIZE_GB" \
      --sdk_container_image "IMAGE" \
      --number_of_worker_harness_threads NUMBER_OF_THREADS
    

Replace the following:

  * PIPELINE: Your pipeline source code file.
  * PROJECT: The Google Cloud project name.
  * BUCKET: The Cloud Storage bucket.
  * REGION: A Dataflow region, for example, `us-central1`.
  * TPU_TYPE: A supported TPU type, for example, `tpu-v5-lite-podslice`. For a full list of types and topologies, see [Supported TPU accelerators](https://docs.cloud.google.com/dataflow/docs/tpu/tpu-support#supported-tpus).
  * TPU_TOPOLOGY: The TPU topology, for example, `1x1`.
  * MACHINE_TYPE: The corresponding machine type, for example, `ct5lp-hightpu-1t`.
  * DISK_SIZE_GB: The size of the boot disk for each worker VM, for example, `100`.
  * IMAGE: The Artifact Registry path for your Docker image.
  * NUMBER_OF_THREADS: Optional. The number of worker harness threads.



## Verify your Dataflow job

To confirm that the job uses worker VMs with TPUs, follow these steps:

  1. In the Google Cloud console, go to the **Dataflow** > **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/dataflow/jobs)

  2. Select a job.

  3. Click the **Job metrics** tab.

  4. In the **Autoscaling** section, confirm that there's at least one **Current workers** VM.

  5. In the side **Job info** pane, check to see that the `machine_type` starts with `ct`. For example, `ct6e-standard-1t`. This indicates TPU usage.




## Troubleshoot your Dataflow job

If you run into problems running your Dataflow job with TPUs, see [Troubleshoot your Dataflow TPU job](https://docs.cloud.google.com/dataflow/docs/tpu/troubleshoot-tpus).

## What's next

  * Try the Quickstart examples: [Running Dataflow on TPUs](https://docs.cloud.google.com/dataflow/docs/notebooks/dataflow_tpu_examples).
  * Learn more about [TPU support on Dataflow](https://docs.cloud.google.com/dataflow/docs/tpu/tpu-support).
  * Learn about [Large model inference in Beam](https://beam.apache.org/documentation/ml/large-language-modeling/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
