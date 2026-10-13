---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/history/
title: Version history \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:56:27.085322+00:00
---

# Version history  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Redis.Cluster.V1/latest/history/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Version history Stay organized with collections  Save and categorize content based on your preferences. 

1.9.0 (latest)  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 

## Version 1.9.0, released 2026-10-09

### New features

  * [Memorystore for Redis Cluster] Add support for ACL policies



## Version 1.8.0, released 2026-07-20

### New features

  * [Memorystore for Redis Cluster] add Cluster.AsyncClusterEndpointsDeletionEnabled



## Version 1.7.0, released 2026-05-04

### New features

  * [Memorystore for Redis Cluster] Updating new node types added



## Version 1.6.0, released 2026-04-06

### New features

  * [Memorystore for Redis Cluster] Add support for Flexible CA feature



## Version 1.5.0, released 2025-11-06

### New features

  * Update dependencies



## Version 1.4.0, released 2025-01-27

### Bug fixes

  * Changed field behavior for an existing field `psc_connection_id` in message `.google.cloud.redis.cluster.v1beta1.PscConnection` ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))
  * Changed field behavior for an existing field `address` in message `.google.cloud.redis.cluster.v1beta1.PscConnection` ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))
  * Changed field behavior for an existing field `forwarding_rule` in message `.google.cloud.redis.cluster.v1beta1.PscConnection` ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))
  * Changed field behavior for an existing field `network` in message `.google.cloud.redis.cluster.v1beta1.PscConnection` ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))



### New features

  * [Memorystore for Redis Cluster] Added support for maintenance window and rescheduling maintenance ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))
  * [Memorystore for Redis Cluster] Added support for Backups and Backup Collections ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))
  * [Memorystore for Redis Cluster] Added support for Multiple VPCs ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))
  * [Memorystore for Redis Cluster] Added support for Cross Cluster Replication ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))
  * [Memorystore for Redis Cluster] Added support for CMEK ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))
  * New REQUIRED field `service_attachment` in message `.google.cloud.redis.cluster.v1beta1.PscConnection` ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))



### Documentation improvements

  * A comment for enum value `NODE_TYPE_UNSPECIFIED` in enum `NodeType` is changed ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))
  * A comment for field `name` in message `.google.cloud.redis.cluster.v1beta1.Cluster` is changed ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))
  * A comment for field `shard_count` in message `.google.cloud.redis.cluster.v1beta1.Cluster` is changed ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))
  * A comment for field `psc_configs` in message `.google.cloud.redis.cluster.v1beta1.Cluster` is changed ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))
  * A comment for field `psc_connections` in message `.google.cloud.redis.cluster.v1beta1.Cluster` is changed ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))
  * A comment for field `psc_connection_id` in message `.google.cloud.redis.cluster.v1beta1.PscConnection` is changed ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))
  * A comment for field `address` in message `.google.cloud.redis.cluster.v1beta1.PscConnection` is changed ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))
  * A comment for field `forwarding_rule` in message `.google.cloud.redis.cluster.v1beta1.PscConnection` is changed ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))
  * A comment for field `project_id` in message `.google.cloud.redis.cluster.v1beta1.PscConnection` is changed ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))
  * A comment for field `network` in message `.google.cloud.redis.cluster.v1beta1.PscConnection` is changed ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))
  * A comment for enum value `ALWAYS` in enum `AppendFsync` is changed ([commit 2a8e11c](https://github.com/googleapis/google-cloud-dotnet/commit/2a8e11cd93533b6f8c34072cc44ac1cfc68c8936))



## Version 1.3.0, released 2024-06-10

### New features

  * [Memorystore for Redis Cluster] Add support for different node types ([commit 536acb5](https://github.com/googleapis/google-cloud-dotnet/commit/536acb56ba7e3f849aedba247d604707fcf841db))
  * [Memorystore for Redis Cluster] Add persistence support ([commit 536acb5](https://github.com/googleapis/google-cloud-dotnet/commit/536acb56ba7e3f849aedba247d604707fcf841db))
  * [Memorystore for Redis Cluster] Get details of certificate authority from redis cluster ([commit 536acb5](https://github.com/googleapis/google-cloud-dotnet/commit/536acb56ba7e3f849aedba247d604707fcf841db))



### Documentation improvements

  * [Memorystore for Redis Cluster] size_gb field shows the size of the cluster rounded up to the next integer, precise_size_gb field will show the exact size of the cluster ([commit 536acb5](https://github.com/googleapis/google-cloud-dotnet/commit/536acb56ba7e3f849aedba247d604707fcf841db))



## Version 1.2.0, released 2024-05-14

### New features

  * Add IServiceCollection extension methods for client registration where an IServiceProvider is required. ([commit 022fab2](https://github.com/googleapis/google-cloud-dotnet/commit/022fab203f28fb9c608972af7f8b83f571ae5694))



## Version 1.1.0, released 2024-03-26

### New features

  * Change netstandard2.1 target to netstandard2.0 ([commit 82bea85](https://github.com/googleapis/google-cloud-dotnet/commit/82bea850661975b9750ac30753528cc9d2e05240))



## Version 1.0.0, released 2024-03-12

No API surface changes; just promotion to GA.

## Version 1.0.0-beta02, released 2024-02-29

No API surface changes; just dependency updates.

## Version 1.0.0-beta01, released 2023-10-31

Initial release.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
