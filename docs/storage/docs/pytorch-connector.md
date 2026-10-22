---
url: https://docs.cloud.google.com/storage/docs/pytorch-connector/
title: Connector for PyTorch \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:26:32.462377+00:00
---

# Connector for PyTorch  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/pytorch-connector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Reference ](https://docs.cloud.google.com/storage/docs/apis)



Send feedback 

#  Connector for PyTorch Stay organized with collections  Save and categorize content based on your preferences. 

The Cloud Storage Connector for PyTorch is an open-source tool for direct integration between Cloud Storage and PyTorch. This connector helps you load training data and manage model checkpoints for Artificial Intelligence (AI) and Machine Learning (ML) workloads.

This page describes how to install and get started with using the Cloud Storage Connector for PyTorch.

## Overview

The Connector for PyTorch provides advantages for both data loading in training and for checkpointing and model loading:

For data loading in training, Connector for PyTorch provides the following advantages:

  * Connector for PyTorch contains optimizations to make training up to three times faster than default PyTorch in datasets consisting primarily of files smaller than 1MB.
  * Connector for PyTorch implements PyTorch's [dataset primitive](https://pytorch.org/tutorials/beginner/basics/data_tutorial) that can be used to help efficiently load training data from Cloud Storage buckets.
  * Support for [map-style datasets](https://pytorch.org/docs/stable/data.html#map-style-datasets) for random data access patterns and [iterable-style datasets](https://pytorch.org/docs/stable/data.html#iterable-style-datasets) for streaming data access patterns.
  * The ability to transform the downloaded raw bytes of data into the format of your choice, allowing the PyTorch DataLoader to flexibly work with NumPy arrays or PyTorch tensors.



For checkpointing and model loading, Connector for PyTorch provides the following advantages:

  * A checkpointing interface to conveniently and directly save model checkpoints to a Cloud Storage bucket and load model checkpoints from the bucket.
  * Connector for PyTorch supports PyTorch Lightning checkpointing by using the `DatafluxLightningCheckpoint` implementation of PyTorch Lightning's `CheckpointIO`.
  * Connector for PyTorch provides `StorageWriter` and `StorageReader` implementations for use with PyTorch distributed checkpointing. The Connector for PyTorch demo library includes example code for using this in a PyTorch Lightning FSDP workload.
  * Connector checkpointing includes support for [asynchronous checkpoint](https://github.com/GoogleCloudPlatform/dataflux-pytorch/tree/main/demo/lightning/checkpoint/singlenode) saves with both Lightning and base PyTorch.



For more information see the Connector for PyTorch [GitHub landing page](https://github.com/GoogleCloudPlatform/dataflux-pytorch).

## Frameworks

Connector for PyTorch is supported on the following framework versions:

  * Python 3.8 or greater
  * PyTorch Lightning 2.0 or greater
  * PyTorch 2.3.1 or greater



## Getting started

To use the Connector for PyTorch, you must have the following:

  * A Cloud Storage bucket that contains the data you want to work with. 
    * See composite object usage for additional recommended settings for the bucket.
  * The following [permissions](https://docs.cloud.google.com/storage/docs/access-control/iam-permissions) for working with the data stored in the bucket: 
    * `storage.objects.create`
    * `storage.objects.list`
    * `storage.objects.get`
    * `storage.objects.delete`, if you intend to use composed downloads



These permissions must be [granted](https://docs.cloud.google.com/storage/docs/access-control/using-iam-permissions) to the account that the Connector for PyTorch will use for authentication by using an IAM role such as [Storage Object User](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).

## Installation

To install the Connector for PyTorch, use the following command:
    
    
    pip install gcs-torch-dataflux
    

### Configuration

Authentication must be provided to use the Connector for PyTorch [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) through one of the following methods:

  * While running the Connector for PyTorch on a Compute Engine VM, Application Default Credentials automatically use the VM's attached service account by default. For more information, see [Choose a workload authentication method](https://docs.cloud.google.com/compute/docs/access/app-authentication-methods).
  * [Application Default Credentials](https://docs.cloud.google.com/docs/authentication/application-default-credentials) can also be configured manually. You can sign in directly using the Google Cloud CLI:


    
    
    gcloud auth application-default login
    

## Examples

A complete set of examples for working with the Connector for PyTorch can be found in the [demo directory of Connector for PyTorch GitHub repository](https://github.com/GoogleCloudPlatform/dataflux-pytorch/tree/main/demo). Examples include:

  * A [basic starter Jupyter Notebook (hosted by Google Colab)](https://github.com/GoogleCloudPlatform/dataflux-pytorch/tree/main/demo/simple-walkthrough/Getting%20Started%20with%20Dataflux%20Dataset%20for%20PyTorch%20with%20Google%20Cloud%20Storage.ipynb).
  * An [end-to-end image segmentation training workload walkthrough](https://github.com/GoogleCloudPlatform/dataflux-pytorch/tree/main/demo/image_segmentation/README.md).
  * An [end-to-end example and the notebook for PyTorch Lightning integration](https://github.com/GoogleCloudPlatform/dataflux-pytorch/tree/main/demo/lightning).



## Performance

Connector for PyTorch has specific optimizations designed for ML workloads that can provide significantly better performance than direct API calls to Cloud Storage:

  * To optimize listing performance, the Connector for PyTorch utilizes a _fast listing_ algorithm developed to balance the listing workload among parallelized object listing processes.
  * To optimize the download performance of small files, the Connector for PyTorch uses the [compose operation](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/compose) to concatenate sets of smaller objects into single, larger ones. These [composite objects](https://docs.cloud.google.com/storage/docs/composite-objects) are stored in the same bucket as the source objects and have the prefix `dataflux-composed-objects/` in their names.
  * [Multipart Upload](https://docs.cloud.google.com/storage/docs/multipart-uploads) for checkpoint write allows for up to 10x performance improvement over standard checkpoint upload.



You can find performance data on GitHub for the following:

  * Lightning Text Based Training
  * Lightning Image Training
  * Single-node checkpointing
  * Multi-node checkpointing



## Considerations

The following should be taken under consideration on a per-workload basis.

### Fast listing operations

Connector for PyTorch's _fast listing_ algorithm causes the Connector for PyTorch to use more [list operations](https://docs.cloud.google.com/storage/docs/json_api/v1/objects/list) than a regular sequential listing. List operations are charged as [Class A operations](https://docs.cloud.google.com/storage/pricing#operations-pricing).

### Composite object usage

To avoid excess storage charges and [early deletion charges](https://docs.cloud.google.com/storage/pricing#early-delete) when working with temporary composite objects, you should ensure your bucket uses the following settings:

  * Disabled [Soft delete](https://docs.cloud.google.com/storage/docs/soft-delete)
  * Disabled [Bucket Lock](https://docs.cloud.google.com/storage/docs/bucket-lock)
  * Disabled [Object Versioning](https://docs.cloud.google.com/storage/docs/object-versioning)
  * [Standard storage](https://docs.cloud.google.com/storage/docs/storage-classes) as the storage class for both the bucket and objects.



Composite objects created by the Connector for PyTorch are usually automatically removed at the end of your training loop, but in rare cases they might not be. To ensure the objects are removed from your bucket, you can run the following command:
    
    
    gcloud storage rm gs://<my-bucket>/dataflux-composed-objects/ --recursive
    

You can disable the use of composite objects by including either `disable_compose=True` or `max_composite_object_size=0` in the config portion of the dataset you're constructing. However, turning off this behavior can cause training loops to take significantly longer, especially when working with small files.

Using composite objects causes Cloud Storage to hit QPS and throughput limits at a lower scale than downloading files directly. You should disable the use of composite objects when running at high multi-node scales where you hit project QPS or throughput limits even without using composite objects.

### 429 errors and degraded performance

While working with the Connector for PyTorch, you might receive 429 errors or slower than expected execution times. There are several common reasons this occurs:

  * Many machine learning efforts opt for a highly distributed training model leveraging tools such as PyTorch Lightning and Ray. These models are compatible with the Connector for PyTorch but can often trigger the rate limits of Cloud Storage.
  * 429 errors accompanied with messages such as "This workload is drawing too much egress bandwidth from Cloud Storage" or "This workload triggered the Cloud Storage Egress Bandwidth Cap" indicate that the data [throughput rate](https://docs.cloud.google.com/storage/quotas) of your workload is exceeding the maximum capacity of your Google Cloud project. To address these issues, take the following steps: 
    * [Check that other workloads in your project are not drawing excess bandwidth.](https://docs.cloud.google.com/storage/docs/bandwidth-usage#bandwidth-monitoring)
    * [Apply for a quota increase](https://docs.cloud.google.com/storage/docs/bandwidth-usage#increase).
    * Adjust the `list_retry_config` and `download_retry_config` options in the config portion of the datasets you're constructing to tune your retry backoff and maximize performance.
  * QPS limits can trigger 429 errors with a body message indicating `TooManyRequests`, but more commonly manifest in slower than expected execution times. QPS bottlenecks are more common when operating on high volumes of small files. Bucket QPS limits [naturally scale over time](https://docs.cloud.google.com/storage/docs/request-rate#best-practices), so allowing a warmup period can often lead to faster performance. To get more details on the performance of a target bucket, look at the Observability tab when viewing your bucket from the Google Cloud console.
  * If your workload is failing with a `TooManyRequests` error that includes the keyword `dataflux-composed-objects` in the error message, disabling the use of composed objects is the best first troubleshooting step. Doing so can reduce QPS load brought on by compose operations when used at scale.



### Memory consumption

Checkpoint writes and loads, including final models for inference, are fully staged in memory in order to optimize upload and download performance. Each machine must have enough free RAM to stage its checkpoint in memory so it can take advantage of these performance improvements.

## Get support

You can get support, submit general questions, and request new features by using one of the official [Google Cloud support channels](https://docs.cloud.google.com/support-hub). You can also get support by [filing issues in GitHub](https://github.com/GoogleCloudPlatform/dataflux-pytorch/issues).

_PyTorch, the PyTorch logo, and any related marks are trademarks of The Linux Foundation._

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
