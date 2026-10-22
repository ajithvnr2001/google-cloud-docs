---
url: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/profile-based-configurations/
title: Profile-based configurations for AI/ML workloads \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:40.121811+00:00
---

# Profile-based configurations for AI/ML workloads  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/profile-based-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Profile-based configurations for AI/ML workloads Stay organized with collections  Save and categorize content based on your preferences. 

Profile-based configurations in Cloud Storage FUSE let you apply a predefined, optimized set of features for caching, threading, and buffer sizes based on your artificial intelligence or machine learning (AI/ML) workload type. Profiles help you streamline Cloud Storage FUSE configuration and achieve high performance with less effort.

To apply a profile, use the [`profile` field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#profile) or [`--profile` option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#profile) with one of the following values: `aiml-training` for training workloads, `aiml-checkpointing` for checkpointing workloads, or `aiml-serving` for serving workloads.

## Considerations

  * You can only set the `--profile` option or `profile` field during a mount operation. If you need to update the `--profile` option or `profile` field, you need to remount your Cloud Storage FUSE bucket.

  * When you use profile-based configurations, Cloud Storage FUSE sets the metadata cache capacity and time to live (TTL) to unlimited, meaning that entries are never evicted from the metadata cache. If your virtual machine doesn't have enough memory, you might experience Out of Memory (OOM) errors. Therefore, we recommend reviewing your memory capacity before you apply profile-based configurations. OOM errors are more likely to occur on machines with less than one TiB of memory.

  * When a Cloud Storage FUSE parameter is configured in multiple ways, the following order of precedence applies (from highest to lowest):

    1. Values set directly in a `gcsfuse` command or a Cloud Storage FUSE configuration file.
    2. Values set by a profile, where the profile is specified using the `--profile` option in a `gcsfuse` command or the `profile` field in a Cloud Storage FUSE configuration file.
    3. Default values automatically applied when Cloud Storage FUSE detects a high-performance machine type. For more information, see [Automated configuration values for high-performance machine types](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/automated-configurations).
  * Cloud Storage FUSE CSI volumes in Google Kubernetes Engine Pods don't support the `profile` field or `--profile` option.

  * File caching cannot be enabled using profile-based configurations because file caching requires the use of Cloud Storage FUSE configuration fields and Cloud Storage FUSE CLI options that can't be generalized. To enable file caching for serving, training, or checkpointing workloads, you must configure file caching options or fields explicitly.




## Apply profile-based configurations for training workloads

The training-specific profile optimizes performance for high throughput reads of large datasets and prevents Cloud GPUs and Cloud TPU hardware from waiting for data.

To apply the training-specific profile, specify either [`profile: aiml-training`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#profile) using a Cloud Storage FUSE configuration file or [`--profile=aiml-training`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#profile) using the Cloud Storage FUSE CLI. The following configurations are then applied:
    
    
       # Create implicit directories locally when accessed:
       - implicit-dirs
       # Disable caching for lookups of files or directories that don't exist:
       - metadata-cache:negative-ttl-secs:0
       # Keep cached metadata (file attributes, types) indefinitely time-wise:
       - metadata-cache:ttl-secs:-1
       # Allow unlimited size for the file attribute (stat) cache:
       - metadata-cache:stat-cache-max-size-mb:-1
    

## Apply profile-based configurations for checkpointing workloads

The checkpointing-specific profile optimizes performance for high throughput writes for large files by drastically reducing the time it takes to save multi-gigabyte checkpoints, minimizing training pauses.

To apply the checkpointing-specific profile, specify either [`profile: aiml-checkpointing`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#profile) using a Cloud Storage FUSE configuration file or [`--profile=aiml-checkpointing`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#profile) using the Cloud Storage FUSE CLI. The following configurations are then applied:
    
    
      # Create implicit directories locally when accessed:
      - implicit-dirs
      # Disable caching for lookups of files/dirs that don't exist:
      - metadata-cache:negative-ttl-secs:0
      # Keep cached metadata (file attributes, types) indefinitely time-wise:
      - metadata-cache:ttl-secs:-1
      # Allow unlimited size for the file attribute (stat) cache:
      - metadata-cache:stat-cache-max-size-mb:-1
      # Cache the entire file when any part is read sequentially:
      - file-cache:cache-file-for-range-read:true
      # Allow renaming directories with a lot of files in non-HNS buckets.
      - file-system:rename-dir-limit:200000
    

## Apply profile-based configurations for serving workloads

Serving optimizes performance for serving workloads by improving data access and caching mechanisms.

To apply the serving-specific profile, specify either [`profile: aiml-serving`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#profile) using a Cloud Storage FUSE configuration file or [`--profile=aiml-serving`](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#profile) using the Cloud Storage FUSE CLI. The following configurations are then applied:
    
    
      # Create implicit directories locally when accessed:
      - implicit-dirs
      # Disable caching for lookups of files/dirs that don't exist:
      - metadata-cache:negative-ttl-secs:0
      # Keep cached metadata (file attributes, types) indefinitely time-wise:
      - metadata-cache:ttl-secs:-1
      # Allow unlimited size for the file attribute (stat) cache:
      - metadata-cache:stat-cache-max-size-mb:-1
      # Cache the entire file when any part is read sequentially:
      - file-cache:cache-file-for-range-read:true
      # Enable kernel-list-cache to make listing faster as this is a readonly file system hierarchy.
      - file-system:kernel-list-cache-ttl-secs:-1
    

## What's next

  * Learn about [automated configuration values for high-performance machine types](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/automated-configurations).

  * Learn how you can [optimize performance with pre-configured GKE YAML files](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/sample-yaml-files).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
