---
url: https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-process-dataflow-fuse/
title: Process ML data using Dataflow and Cloud Storage FUSE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:25:16.660509+00:00
---

# Process ML data using Dataflow and Cloud Storage FUSE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/machine-learning/ml-process-dataflow-fuse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Dataflow ML ](https://docs.cloud.google.com/dataflow/docs/machine-learning)



Send feedback 

#  Process ML data using Dataflow and Cloud Storage FUSE Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/overview) with Dataflow to process datasets for machine learning (ML) tasks.

When working with ML tasks, Dataflow can be used for processing large datasets. However, some common software libraries used for ML, like OpenCV, have input file requirements. They frequently require files to be accessed as if they are stored on a local computer's hard drive, rather than from cloud-based storage. This requirement creates difficulties and delays. As a solution, pipelines can either use special I/O connectors for input or download files onto the Dataflow virtual machines (VMs) before processing. These solutions are frequently inefficient.

Cloud Storage FUSE provides a way to avoid these inefficient solutions. Cloud Storage FUSE lets you mount your Cloud Storage buckets onto the Dataflow VMs. This makes the files in Cloud Storage appear as if they are local files. As a result, the ML software can access them directly without needing to download them beforehand.

## Benefits

Using Cloud Storage FUSE for ML tasks offers the following benefits:

  * Input files hosted on Cloud Storage can be accessed in the Dataflow VM using local file system semantics.
  * Because the data is accessed on-demand, the input files don't have to be downloaded beforehand.



## Support and limitations

  * To use Cloud Storage FUSE with Dataflow, you must configure worker VMs with [external IP addresses](https://docs.cloud.google.com/dataflow/docs/guides/routes-firewall#internet_access_for) so that they meet the internet access requirements.



## Specify buckets to use with Cloud Storage FUSE

To specify a Cloud Storage bucket to mount to a VM, use the [`--experiments`](https://docs.cloud.google.com/dataflow/docs/reference/pipeline-options) flag. To specify multiple buckets, use a semicolon delimiter (`;`) between bucket names.

The format is as follows:
    
    
    --experiments="gcsfuse_buckets=CONFIG"
    

Replace the following:

  * `CONFIG`: a semicolon-delimited list of Cloud Storage entries, where each entry is one of the following:

    1. `BUCKET_NAME`: A Cloud Storage bucket name. For example, `dataflow-samples`. If you omit the bucket mode, the bucket is treated as read-only.

    2. `BUCKET_NAME:MODE`: A Cloud Storage bucket name and its associated mode, where `MODE` is either `ro` (read-only) or `rw` (read-write).

For example:
           
           --experiments="gcsfuse_buckets=read-bucket1;read-bucket2**:ro** ;write-bucket1**:rw** "
           

In this example, specifying the mode assures the following:

       * `gs://read-bucket1` is mounted in read-only mode.
       * `gs://read-bucket2` is mounted in read-only mode.
       * `gs://write-bucket1` is mounted in read-write mode.

Beam pipeline code can access these buckets at `/var/opt/google/gcs/BUCKET_NAME`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
