---
url: https://docs.cloud.google.com/memorystore/docs/memcached/supported-versions/
title: Supported versions \u00a0|\u00a0 Memorystore for Memcached \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:27:50.161388+00:00
---

# Supported versions  |  Memorystore for Memcached  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/memcached/supported-versions/

Memorystore for Memcached is being deprecated and will be shut down on January 31, 2029. After February 1, 2027, you can't create Memorystore for Memcached instances in new projects unless these instances already exist in these projects. We recommend that you migrate your workloads to [Memorystore for Valkey](https://docs.cloud.google.com/memorystore/docs/valkey), which offers superior performance and features.

[Learn more about the deprecation](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation) | [Read the migration guide](https://docs.cloud.google.com/memorystore/docs/memcached/deprecation/migrate-to-valkey)

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Memcached ](https://docs.cloud.google.com/memorystore/docs/memcached)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/memcached/memcached-overview)



Send feedback 

#  Supported versions Stay organized with collections  Save and categorize content based on your preferences. 

Memorystore for Memcached is backed by open source Memcached software. Memorystore currently supports Memcached versions 1.5.16 and 1.6.15. The default version is Memcached 1.5.16.

For instructions on how to upgrade the Memcached version of an instance, see [Upgrade the Memcached version of an instance](https://docs.cloud.google.com/memorystore/docs/memcached/upgrade-memcached-version).

For information about how upgrading the Memcached version affects the instance, see [About upgrading the Memcached version of an instance](https://docs.cloud.google.com/memorystore/docs/memcached/about-upgrading-version).

## Version support policy

Memorystore for Memcached supports one patch version for every major OSS Memcached version listed in the [Current versions](https://docs.cloud.google.com/memorystore/docs/memcached/supported-versions#current_versions) section of this page. The patch is kept up to date on a regular basis during maintenance periods. Memorystore for Memcached monitors for any critical patches that need to be applied to your instance. Critical security patches are rolled out outside of the regular maintenance period. See [About maintenance](https://docs.cloud.google.com/memorystore/docs/memcached/about-maintenance) for more details.

## Current versions

This table lists the supported Memcached versions and when each version was last updated:

Memcached version | Last update  
---|---  
1.5.16 | March 26, 2020  
[1.6.15](https://docs.cloud.google.com/memorystore/docs/memcached/supported-versions#version_1_6_15) | September 19, 2023  
  
### Memcached version 1.6.15

The table below outlines Memorystore support of some major features introduced by Memcached version 1.6.15.

Feature | Description | Supported in Memorystore for Memcached  
---|---|---  
Meta protocol | The [new meta protocol](https://github.com/memcached/memcached/wiki/MetaCommands) now has more features than the binary protocol. Anything you can do with the text/binary protocol can be done with the new meta commands. These commands can bring huge benefits to performance and correctness of cache systems. | Yes  
Batching of response syscalls | The network code has been refactored to allow automatic batching of response syscalls. As a result of this feature, if you submit multiple get commands in the same TCP packet, Memcached tends to send the responses with a single syscall. | Yes  
Disable watch commands | A configuration to disable watch commands. For more details, see [Supported Memcached configurations](https://docs.cloud.google.com/memorystore/docs/memcached/supported-memcached-configurations). | Yes  
XXH3 hash algorithm | XXH3 hash algorithm has been added to the list of hash table algorithms. For more details, see [Supported Memcached configurations](https://docs.cloud.google.com/memorystore/docs/memcached/supported-memcached-configurations). | Yes  
Watch connevents | Watch connevents command shows real-time entries about connection/disconnection events | Yes  
Warm Cache Restart | Memcached can now recover its cache in between restarts. | No  
Extstore | [Extstore](https://memcached.org/extstore) is an addition to memcached which leaves the hash table and keys in memory, but moves values to external storage (usually flash). | No  
TLS | Memcached versions 1.5.13 and later support authentication and encryption by using [Transport Layer Security (TLS)](https://docs.memcached.org/features/tls/). TLS lets clients communicate with servers by using a secure channel. | No  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
