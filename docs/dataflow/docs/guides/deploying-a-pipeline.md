---
url: https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline/
title: Deploy Dataflow pipelines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:45:46.281614+00:00
---

# Deploy Dataflow pipelines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/deploying-a-pipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Deploy Dataflow pipelines Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of pipeline deployment and highlights some of the operations you can perform on a deployed pipeline.

## Run your pipeline

After you [create](https://beam.apache.org/documentation/pipelines/create-your-pipeline/) and [test](https://beam.apache.org/documentation/pipelines/test-your-pipeline/) your Apache Beam pipeline, run your pipeline. You can run your pipeline locally, which lets you test and debug your Apache Beam pipeline, or on Dataflow, a data processing system available for running Apache Beam pipelines.

### Run locally

Run your pipeline locally.

### Java

The following example code, taken from the quickstart, shows how to run the WordCount pipeline locally. To learn more, see how to [run your Java pipeline locally](https://docs.cloud.google.com/dataflow/docs/quickstarts/create-pipeline-java#run-the-pipeline-locally). 

In your terminal, run the following command:
    
    
      mvn compile exec:java \
          -Dexec.mainClass=org.apache.beam.examples.WordCount \
          -Dexec.args="--output=counts"
      

### Python

The following example code, taken from the quickstart, shows how to run the WordCount pipeline locally. To learn more, see how to [run your Python pipeline locally](https://docs.cloud.google.com/dataflow/docs/quickstarts/create-pipeline-python#run-the-pipeline-locally). 

In your terminal, run the following command:
    
    
    python -m apache_beam.examples.wordcount \ --output outputs

**Note:** This example demonstrates how to run the pipeline using a module file. For different Python implementations, including how to run Python code contained in a script, see [Command line and environment](https://docs.python.org/3/using/cmdline.html) in the Python documentation. 

### Go

The following example code, taken from the quickstart, shows how to run the WordCount pipeline locally. To learn more, see how to [run your Go pipeline locally](https://docs.cloud.google.com/dataflow/docs/quickstarts/create-pipeline-go#run_the_unmodified_pipeline). 

In your terminal, run the following command:
    
    
        go run wordcount.go --input gs://dataflow-samples/shakespeare/kinglear.txt \ --output outputs
      

Learn how to run your pipeline locally, on your machine, [using the direct runner](https://beam.apache.org/documentation/runners/direct/).

### Run on Dataflow

Run your pipeline on Dataflow.

Dataflow jobs use Cloud Storage to store temporary files during pipeline execution. To avoid being billed for unnecessary storage costs, turn off the soft delete feature on buckets that your Dataflow jobs use for temporary storage. For more information, see [Disable soft delete](https://docs.cloud.google.com/storage/docs/disable-soft-delete).

### Java

The following example code, taken from the quickstart, shows how to run the WordCount pipeline on Dataflow. To learn more, see how to [run your Java pipeline on Dataflow](https://docs.cloud.google.com/dataflow/docs/quickstarts/create-pipeline-java#run-the-pipeline-on-the-dataflow-service).

In your terminal, run the following command (from your `word-count-beam` directory):
    
    
      mvn -Pdataflow-runner compile exec:java \
        -Dexec.mainClass=org.apache.beam.examples.WordCount \
        -Dexec.args="--project=PROJECT_ID \
        --gcpTempLocation=gs://BUCKET_NAME/temp/ \
        --output=gs://BUCKET_NAME/output \
        --runner=DataflowRunner \
        --region=REGION"
        

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID
  * `BUCKET_NAME`: the name of your Cloud Storage bucket
  * `REGION`: a [Dataflow region](https://docs.cloud.google.com/dataflow/docs/resources/locations), like `us-central1`



### Python

The following example code, taken from the quickstart, shows how to run the WordCount pipeline on Dataflow. To learn more, see how to [run your Python pipeline on Dataflow](https://docs.cloud.google.com/dataflow/docs/quickstarts/create-pipeline-python#run-the-pipeline-on-the-dataflow-service).

In your terminal, run the following command:
    
    
    python -m apache_beam.examples.wordcount \
        --region DATAFLOW_REGION \
        --input gs://dataflow-samples/shakespeare/kinglear.txt \
        --output gs://STORAGE_BUCKET/results/outputs \
        --runner DataflowRunner \
        --project PROJECT_ID \
        --temp_location gs://STORAGE_BUCKET/tmp/

Replace the following:

  * `DATAFLOW_REGION`: the [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy the Dataflow job—for example, `europe-west1`

The `--region` flag overrides the default region that is set in the metadata server, your local client, or environment variables.

  * `STORAGE_BUCKET`: the Cloud Storage name that you copied earlier
  * `PROJECT_ID`: the Google Cloud project ID that you copied earlier



### Go

The following example code, taken from the quickstart, shows how to run the WordCount pipeline on Dataflow. To learn more, see how to [run your Go pipeline on Dataflow](https://docs.cloud.google.com/dataflow/docs/quickstarts/create-pipeline-go#run_the_pipeline_on_the_service).

In your terminal, run the following command:
    
    
      go run wordcount.go --input gs://dataflow-samples/shakespeare/kinglear.txt \
        --output gs://STORAGE_BUCKET/results/outputs \
        --runner dataflow \
        --project PROJECT_ID \
        --region DATAFLOW_REGION \
        --staging_location gs://STORAGE_BUCKET/binaries/
      

Replace the following:

  * `STORAGE_BUCKET`: The Cloud Storage bucket name.
  * `PROJECT_ID`: the Google Cloud project ID.
  * `DATAFLOW_REGION`: The [region](https://docs.cloud.google.com/dataflow/docs/resources/locations) where you want to deploy the Dataflow job. For example, `europe-west1`. For a list of available locations, see [Dataflow locations](https://docs.cloud.google.com/dataflow/docs/resources/locations). Note that the `--region` flag overrides the default region that is set in the metadata server, your local client, or environment variables.



Learn how to run your pipeline on the Dataflow service, [using the Dataflow runner](https://beam.apache.org/documentation/runners/dataflow/).

When you run your pipeline on Dataflow, Dataflow turns your Apache Beam pipeline code into a Dataflow job. Dataflow fully manages Google Cloud services for you, such as [Compute Engine](https://docs.cloud.google.com/compute) and [Cloud Storage](https://docs.cloud.google.com/storage) to run your Dataflow job, and automatically spins up and tears down necessary resources. You can learn more about how Dataflow turns your Apache Beam code into a Dataflow job in [Pipeline lifecycle](https://docs.cloud.google.com/dataflow/docs/pipeline-lifecycle).

## Pipeline validation

When you run your pipeline on Dataflow, before the job launches, Dataflow performs validation tests on the pipeline. When a validation test finds problems with the pipeline, Dataflow fails the job submission early. In the [job logs](https://docs.cloud.google.com/dataflow/docs/guides/logging#MonitoringLogs), Dataflow includes messages with the following text. Each message also includes details about the validation findings and instructions for resolving the issue.
    
    
    The preflight pipeline validation failed for job JOB_ID.
    

Which validation tests run depends on the resources and services that your Dataflow job uses.

  * If the [Service Usage API](https://docs.cloud.google.com/service-usage/docs/reference/rest) is enabled for your project, the pipeline validation tests check whether the services needed to run your Dataflow job are enabled.
  * If the [Cloud Resource Manager API](https://docs.cloud.google.com/resource-manager/reference/rest) is enabled for your project, the pipeline validation tests check whether you have the project-level configurations needed to run your Dataflow job.



For more information about enabling services, see [Enabling and disabling services](https://docs.cloud.google.com/service-usage/docs/enable-disable).

For information about how to resolve permission issues caught during pipeline validation, see [Pipeline validation failed](https://docs.cloud.google.com/dataflow/docs/guides/troubleshoot-permissions#validation-failed).

If you want to override the pipeline validation and launch your job with validation errors, use the following pipeline [service option](https://docs.cloud.google.com/dataflow/docs/reference/service-options):

### Java
    
    
    --dataflowServiceOptions=enable_preflight_validation=false

### Python
    
    
    --dataflow_service_options=enable_preflight_validation=false

### Go
    
    
    --dataflow_service_options=enable_preflight_validation=false

## Set pipeline options

You can control some aspects of how Dataflow runs your job by setting [pipeline options](https://docs.cloud.google.com/dataflow/docs/guides/setting-pipeline-options) in your Apache Beam pipeline code. For example, you can use pipeline options to set whether your pipeline runs on worker virtual machines, on the Dataflow service backend, or locally.

## Manage pipeline dependencies

Many Apache Beam pipelines can run using the default Dataflow runtime environments. However, some data processing use cases benefit from using additional libraries or classes. In these cases, you might need to manage your pipeline dependencies. For more information about managing dependencies, see [Manage pipeline dependencies in Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/manage-dependencies).

## Monitor your job

Dataflow provides visibility into your jobs through tools like the [Dataflow monitoring interface](https://docs.cloud.google.com/dataflow/pipelines/dataflow-monitoring-intf) and the [Dataflow command-line interface](https://docs.cloud.google.com/dataflow/pipelines/dataflow-command-line-intf).

## Access worker VMs

You can view the VM instances for a given pipeline by using the Google Cloud console. From there, you can use SSH to access each instance. However, after your job either completes or fails, the Dataflow service automatically shuts down and cleans up the VM instances.

## Job optimizations

In addition to managing Google Cloud resources, Dataflow automatically performs and optimizes many aspects of distributed parallel processing for you.

### Parallelization and distribution

Dataflow automatically partitions your data and distributes your worker code to Compute Engine instances for parallel processing. For more information, see [parallelization and distribution](https://docs.cloud.google.com/dataflow/docs/pipeline-lifecycle#parallelization_and_distribution).

### Fusion and combine optimizations

Dataflow uses your pipeline code to create an execution graph that represents your pipeline's `PCollection`s and transforms, and optimizes the graph for the most efficient performance and resource usage. Dataflow also automatically optimizes potentially costly operations, such as data aggregations. For more information, see [Fusion optimization](https://docs.cloud.google.com/dataflow/docs/pipeline-lifecycle#fusion_optimization) and [Combine optimization](https://docs.cloud.google.com/dataflow/docs/pipeline-lifecycle#combine_optimization).

### Automatic tuning features

The Dataflow service includes several features that provide on-the-fly adjustment of resource allocation and data partitioning. These features help Dataflow execute your job as quickly and efficiently as possible. These features include the following:

  * [Horizontal Autoscaling](https://docs.cloud.google.com/dataflow/docs/horizontal-autoscaling)
  * [Vertical Autoscaling](https://docs.cloud.google.com/dataflow/docs/vertical-autoscaling)
  * [Dynamic work rebalancing](https://docs.cloud.google.com/dataflow/docs/dynamic-work-rebalancing)

**Note:** With the introduction of Vertical Autoscaling, the feature that was previously called Autoscaling has been renamed to Horizontal Autoscaling.

### Streaming Engine

By default, the Dataflow pipeline runner executes the steps of your streaming pipeline entirely on worker virtual machines, consuming worker CPU, memory, and Persistent Disk storage. Dataflow's Streaming Engine moves pipeline execution out of the worker VMs and into the Dataflow service backend. For more information, see [Streaming Engine](https://docs.cloud.google.com/dataflow/docs/streaming-engine).

### Dataflow Flexible Resource Scheduling

Dataflow FlexRS reduces batch processing costs by using [advanced scheduling techniques](https://docs.cloud.google.com/dataflow/docs/guides/flexrs#delayed_scheduling), the [Dataflow Shuffle](https://docs.cloud.google.com/dataflow/docs/shuffle-for-batch) service, and a combination of [preemptible virtual machine (VM) instances](https://docs.cloud.google.com/compute/docs/instances/preemptible) and regular VMs. By running preemptible VMs and regular VMs in parallel, Dataflow improves the user experience if Compute Engine stops preemptible VM instances during a system event. FlexRS helps to ensure that the pipeline continues to make progress and that you do not lose previous work when [Compute Engine preempts](https://docs.cloud.google.com/compute/docs/instances/preemptible#what_is_a_preemptible_instance) your preemptible VMs. For more information about FlexRS, see [Using Flexible Resource Scheduling in Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/flexrs).

### Dataflow Shielded VM

Starting on June 1, 2022, the Dataflow service uses [Shielded VM](https://docs.cloud.google.com/security/shielded-cloud/shielded-vm) for all workers. To learn more about Shielded VM capabilities, see [Shielded VM](https://docs.cloud.google.com/security/shielded-cloud/shielded-vm).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
