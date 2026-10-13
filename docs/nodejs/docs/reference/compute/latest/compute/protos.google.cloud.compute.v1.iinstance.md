---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.iinstance
title: Interface protos.google.cloud.compute.v1.IInstance (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:52:39.054525+00:00
---

# Interface protos.google.cloud.compute.v1.IInstance (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.iinstance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.compute.v1.IInstance (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Properties of an Instance.

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Properties 

### advancedMachineFeatures
    
    
    advancedMachineFeatures?: (google.cloud.compute.v1.IAdvancedMachineFeatures|null);

Instance advancedMachineFeatures

### canIpForward
    
    
    canIpForward?: (boolean|null);

Instance canIpForward

### confidentialInstanceConfig
    
    
    confidentialInstanceConfig?: (google.cloud.compute.v1.IConfidentialInstanceConfig|null);

Instance confidentialInstanceConfig

### cpuPlatform
    
    
    cpuPlatform?: (string|null);

Instance cpuPlatform

### creationTimestamp
    
    
    creationTimestamp?: (string|null);

Instance creationTimestamp

### deletionProtection
    
    
    deletionProtection?: (boolean|null);

Instance deletionProtection

### description
    
    
    description?: (string|null);

Instance description

### disks
    
    
    disks?: (google.cloud.compute.v1.IAttachedDisk[]|null);

Instance disks

### displayDevice
    
    
    displayDevice?: (google.cloud.compute.v1.IDisplayDevice|null);

Instance displayDevice

### fingerprint
    
    
    fingerprint?: (string|null);

Instance fingerprint

### guestAccelerators
    
    
    guestAccelerators?: (google.cloud.compute.v1.IAcceleratorConfig[]|null);

Instance guestAccelerators

### hostname
    
    
    hostname?: (string|null);

Instance hostname

### id
    
    
    id?: (number|Long|string|null);

Instance id

### instanceEncryptionKey
    
    
    instanceEncryptionKey?: (google.cloud.compute.v1.ICustomerEncryptionKey|null);

Instance instanceEncryptionKey

### keyRevocationActionType
    
    
    keyRevocationActionType?: (string|null);

Instance keyRevocationActionType

### kind
    
    
    kind?: (string|null);

Instance kind

### labelFingerprint
    
    
    labelFingerprint?: (string|null);

Instance labelFingerprint

### labels
    
    
    labels?: ({ [k: string]: string }|null);

Instance labels

### lastStartTimestamp
    
    
    lastStartTimestamp?: (string|null);

Instance lastStartTimestamp

### lastStopTimestamp
    
    
    lastStopTimestamp?: (string|null);

Instance lastStopTimestamp

### lastSuspendedTimestamp
    
    
    lastSuspendedTimestamp?: (string|null);

Instance lastSuspendedTimestamp

### localSsdEncryptionMode
    
    
    localSsdEncryptionMode?: (string|null);

Instance localSsdEncryptionMode

### machineType
    
    
    machineType?: (string|null);

Instance machineType

### metadata
    
    
    metadata?: (google.cloud.compute.v1.IMetadata|null);

Instance metadata

### minCpuPlatform
    
    
    minCpuPlatform?: (string|null);

Instance minCpuPlatform

### name
    
    
    name?: (string|null);

Instance name

### networkInterfaces
    
    
    networkInterfaces?: (google.cloud.compute.v1.INetworkInterface[]|null);

Instance networkInterfaces

### networkPerformanceConfig
    
    
    networkPerformanceConfig?: (google.cloud.compute.v1.INetworkPerformanceConfig|null);

Instance networkPerformanceConfig

### params
    
    
    params?: (google.cloud.compute.v1.IInstanceParams|null);

Instance params

### privateIpv6GoogleAccess
    
    
    privateIpv6GoogleAccess?: (string|null);

Instance privateIpv6GoogleAccess

### reservationAffinity
    
    
    reservationAffinity?: (google.cloud.compute.v1.IReservationAffinity|null);

Instance reservationAffinity

### resourcePolicies
    
    
    resourcePolicies?: (string[]|null);

Instance resourcePolicies

### resourceStatus
    
    
    resourceStatus?: (google.cloud.compute.v1.IResourceStatus|null);

Instance resourceStatus

### satisfiesPzi
    
    
    satisfiesPzi?: (boolean|null);

Instance satisfiesPzi

### satisfiesPzs
    
    
    satisfiesPzs?: (boolean|null);

Instance satisfiesPzs

### scheduling
    
    
    scheduling?: (google.cloud.compute.v1.IScheduling|null);

Instance scheduling

### selfLink
    
    
    selfLink?: (string|null);

Instance selfLink

### serviceAccounts
    
    
    serviceAccounts?: (google.cloud.compute.v1.IServiceAccount[]|null);

Instance serviceAccounts

### shieldedInstanceConfig
    
    
    shieldedInstanceConfig?: (google.cloud.compute.v1.IShieldedInstanceConfig|null);

Instance shieldedInstanceConfig

### shieldedInstanceIntegrityPolicy
    
    
    shieldedInstanceIntegrityPolicy?: (google.cloud.compute.v1.IShieldedInstanceIntegrityPolicy|null);

Instance shieldedInstanceIntegrityPolicy

### sourceMachineImage
    
    
    sourceMachineImage?: (string|null);

Instance sourceMachineImage

### sourceMachineImageEncryptionKey
    
    
    sourceMachineImageEncryptionKey?: (google.cloud.compute.v1.ICustomerEncryptionKey|null);

Instance sourceMachineImageEncryptionKey

### startRestricted
    
    
    startRestricted?: (boolean|null);

Instance startRestricted

### status
    
    
    status?: (string|null);

Instance status

### statusMessage
    
    
    statusMessage?: (string|null);

Instance statusMessage

### tags
    
    
    tags?: (google.cloud.compute.v1.ITags|null);

Instance tags

### workloadIdentityConfig
    
    
    workloadIdentityConfig?: (google.cloud.compute.v1.IWorkloadIdentityConfig|null);

Instance workloadIdentityConfig

### zone
    
    
    zone?: (string|null);

Instance zone

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
