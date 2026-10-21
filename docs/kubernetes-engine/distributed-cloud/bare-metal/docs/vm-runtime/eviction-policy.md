---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/eviction-policy/
title: Configure the eviction policies for VMs in Google Distributed Cloud \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:12:11.591042+00:00
---

# Configure the eviction policies for VMs in Google Distributed Cloud  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/eviction-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Configure the eviction policies for VMs in Google Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document is for platform administrators that run virtual machines (VMs) in Google Distributed Cloud. This document shows you how to configure the eviction policy that controls how VMs that use VM Runtime on GDC can automatically migrate to other hosts during maintenance events. These configuration settings let you VMs continue to run on other hosts when you upgrade a cluster or perform maintenance on a host.

## Before you begin

To complete this document, you need access to Google Distributed Cloud version 1.12.0 (`anthosBareMetalVersion: 1.12.0`) or higher cluster. You can use any cluster type capable of running workloads. If needed, [try Google Distributed Cloud on Compute Engine](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/try/gce-vms) or see the [cluster creation overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/creating-clusters/create-clusters-overview).

## Eviction policy settings

Google Distributed Cloud lets you configure node behavior when you perform cluster upgrades or place nodes into maintenance mode. VM Runtime on GDC uses an _eviction policy_ that controls how the cluster handles VMs that run during these events.

When enabled, VM Runtime on GDC uses live migration to move VM workloads to another host by default. This behavior minimizes potential disruption to the VM workloads. With live migration, migratable VMs move from one host to another without disruption to the guest OS.

**Note:** If you're upgrading to Google Distributed Cloud 1.12 from a previous version, you can't take advantage of migration-based eviction during the upgrade to version 1.12. Migration-based eviction for cluster upgrades is only supported for Google Distributed Cloud version 1.12 and higher.

The following eviction policy settings can be configured:

Property | Default | Valid values  
---|---|---  
`evictionStrategy` | `LiveMigrate` | `LiveMigrate`, `Restart`  
`maxMigrationAttemptsPerVM` | `3` | Integers in the range [`1`,`5`]  
`migrationTargetInitializationTimeout` | `30s` | Any valid duration string, such as `1m`, `2h`, or `1h30m`  
  
### `evictionStrategy`

If this value is set to `LiveMigrate`, VM Runtime on GDC attempts to migrate any migratable VM away from a node to evict it. The VM is placed on another node in the cluster and continues to run.

**Note:** The `VirtualMachineDisk` for a VM must use the `ReadWriteMany` access mode for the VM to use live migration. If the `VirtualMachineDisk` access mode is `ReadWriteOnce`, the VM can't live migrate.

If this value is set to `Restart`, VM Runtime on GDC makes no attempt to migrate VMs. Instead, VMs are stopped when the node is put into maintenance mode, and the VMs start again when the node is brought out of maintenance mode. The VM is unavailable during the host maintenance event.

When you choose the `LiveMigrate` strategy, VM Runtime on GDC falls back to the `Restart` strategy for non-migratable VMs.

### `maxMigrationAttemptsPerVM`

This setting controls the maximum number of migration attempts that can occur for a particular VM before the `Restart` strategy applies.

This setting is ignored if `evictionStrategy` is set to `Restart`.

### `migrationTargetInitializationTimeout`

This setting controls the maximum amount of time a migration can take to start before it's considered to have failed. A migration that takes too long to start counts toward the failed migration budget for a VM workload.

This setting is ignored if `evictionStrategy` is set to `Restart`.

## Enable and configure the eviction policy

To use the eviction policy in VM Runtime on GDC, the `evictionPolicy` setting must be defined in your cluster's `VMRuntime` object. This setting is enabled by default. If you upgrade from a previous version, you must enable this setting manually.

An empty object, such as `evictionPolicy: {}`, enables the eviction policy with default settings. To change the default behavior, add additional configuration options to the `evictionPolicy` object.

To enable and configure the eviction policy, complete the following steps:

  1. Edit the `VMRuntime` custom resource:
         
         kubectl edit vmruntime vmruntime
         

  2. Add or update the `evictionPolicy` section with an empty object to use the default eviction policy settings, or add your desired settings:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VMRuntime
         metadata:
           name: vmruntime
         spec:
           disableCDIUploadProxyVIP: false
           enabled: true
           evictionPolicy: {}
           useEmulation: false
         

If the `evictionPolicy` isn't populated, such as `evictionPolicy: null` or isn't included in the manifest, no special action is taken. VMs are forcefully evicted.

The following example manifests show how to enable live migration of VMs, or restart the VMs on the same host after maintenance is complete:

###  Live migrate 

The following example eviction policy enables live migration of VMs. The cluster can retry the live migration up to 3 times, with a 30-second timeout on the process each time to start:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VMRuntime
         metadata:
           name: vmruntime
         spec:
           disableCDIUploadProxyVIP: false
           enabled: true
           evictionPolicy:
             evictionStrategy: LiveMigrate
             maxMigrationAttemptsPerVM: 3
             migrationTargetInitializationTimeout: 30s
           useEmulation: false
         

###  Restart 

The following example eviction policy makes no attempt at migration for any VMs during eviction. VMs are stopped on their current host, and start again when the host finishes its maintenance event:
         
         apiVersion: vm.cluster.gke.io/v1
         kind: VMRuntime
         metadata:
           name: vmruntime
         spec:
           disableCDIUploadProxyVIP: false
           enabled: true
           evictionPolicy:
             evictionStrategy: Restart
           useEmulation: false
         

  3. Save and close the `VMRuntime` custom resource in your editor.

VM Runtime on GDC now applies the eviction policy to VMs in your cluster.




## What's next

  * [Schedule VMs that use VM Runtime on GDC](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/vm-runtime/schedule-vms)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
