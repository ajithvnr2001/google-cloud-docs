---
url: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/automated-configurations/
title: Automated configuration values for high-performance machine types \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:00:57.570135+00:00
---

# Automated configuration values for high-performance machine types  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/automated-configurations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Automated configuration values for high-performance machine types Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage FUSE automatically applies optimized default configuration values when it runs on high-performance Compute Engine machine types, such as the A3, A4, and TPU v6e series. These defaults help you get high throughput for demanding workloads without manual tuning. Any values that you set manually at mount time take precedence.

## Machine types

Configuration values are automated for the following high-performance Compute Engine machine types:

Series type | Machine type  
---|---  
[A2 machine series](https://docs.cloud.google.com/compute/docs/gpus#a100-gpus) |  `a2-megagpu-16g` `a2-ultragpu-8g`  
[A3 machine series](https://docs.cloud.google.com/compute/docs/gpus#a3-series) |  `a3-edgegpu-8g` `a3-highgpu-8g` `a3-megagpu-8g` `a3-ultragpu-8g`  
[A4 machine series](https://docs.cloud.google.com/compute/docs/gpus#b200-gpus) |  `a4-highgpu-8g-lowmem`  
[A4X machine series](https://docs.cloud.google.com/compute/docs/gpus#gb200-gpus) |   
| `a4x-highgpu-4g`  
[TPU v5e](https://docs.cloud.google.com/tpu/docs/v5e) |  `ct5l-hightpu-8t` `ct5lp-hightpu-8t`  
[TPU v5p](https://docs.cloud.google.com/tpu/docs/v5p) |  `ct5p-hightpu-4t` `ct5p-hightpu-4t-tpu`  
[TPU v6e (Trillium)](https://docs.cloud.google.com/tpu/docs/v6e) |  `ct6e-standard-4t` `ct6e-standard-4t-tpu` `ct6e-standard-8t` `ct6e-standard-8t-tpu`  
[TPU 7x (Ironwood)](https://docs.cloud.google.com/tpu/docs/tpu7x) |   
| `tpu7x-standard-4t`  
  
## Automated configuration values

When a supported machine type is detected, Cloud Storage FUSE automatically applies the following configuration values:

Cloud Storage FUSE configuration file field | Cloud Storage FUSE CLI option | Automated configuration value  
---|---|---  
`[metadata-cache:negative-ttl-secs](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#negative-ttl-secs)` | `[--metadata-cache-negative-ttl-secs](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#metadata-cache-negative-ttl-secs)` | `0`  
`[metadata-cache:ttl-secs](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#ttl-secs)`1 | `[--metadata-cache-ttl-secs](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#metadata-cache-ttl-secs)`1 | `-1`  
`[metadata-cache:stat-cache-max-size-mb](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#stat-cache-max-size-mb)` | `[--stat-cache-max-size-mb](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#stat-cache-max-size-mb)` | `1024`  
`[implicit-dirs](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#implicit-dirs)` | `[--implicit-dirs](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#implicit-dirs)` | `true`  
`[file-system:rename-dir-limit](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#rename-dir-limit)` | `[--rename-dir-limit](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#rename-dir-limit)` | `200000`  
`[write:global-max-blocks](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#write:global-max-blocks)` | `[--write-global-max-blocks](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#write-global-max-blocks)` | `1600`  
  
1Setting this configuration to `-1` significantly boosts performance by always serving files from the cache. Be aware that this configuration bypasses consistency checks, which can lead to serving outdated data. For details on managing data consistency, refer to [Overview of caching in Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/caching).

## Further performance tuning

When you use a high-performance Google Cloud machine type, the configuration values detailed on this page are automatically applied. However, you can further fine-tune your machine for optimal performance using the following methods:

  * Use the [Performance tuning best practices guide](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance) to improve Cloud Storage FUSE using key Cloud Storage FUSE features and configurations to achieve maximum throughput and optimal performance.

  * If you're running training, serving, or checkpointing and Just in Time (JIT) cache workloads on Google Kubernetes Engine clusters that use Cloud GPUs or Cloud TPU to access large datasets in Cloud Storage, you can streamline your setup by utilizing pre-configured YAML files to mount your Cloud Storage buckets directly into your pods more efficiently. For more information and instructions on how to use pre-configured GKE YAML files, see [Use pre-configured GKE YAML files to optimize Cloud Storage FUSE performance](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance).

  * If you're running training, serving, or checkpointing workloads using Cloud Storage FUSE, you can use the [`profile` field](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/config-file#profile) or [`--profile` command option](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/cli-options#profile) to automatically adjust specific Cloud Storage FUSE configurations for optimal performance based on the specific workload type. For more information, see [Profile-based configurations for AI/ML workloads](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/profile-based-configurations).




## What's next

  * Learn how to [tune Cloud Storage FUSE for optimal performance](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/performance).

  * Use a [pre-configured GKE YAML file](https://docs.cloud.google.com/storage/docs/cloud-storage-fuse/sample-yaml-files) to configure tuning best practices.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
