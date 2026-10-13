---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinstancegroupmanager
title: Interface protos.google.cloud.compute.v1beta.IInstanceGroupManager (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:50:21.085252+00:00
---

# Interface protos.google.cloud.compute.v1beta.IInstanceGroupManager (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinstancegroupmanager

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.compute.v1beta.IInstanceGroupManager (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Properties of an InstanceGroupManager.

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Properties 

### allInstancesConfig
    
    
    allInstancesConfig?: (google.cloud.compute.v1beta.IInstanceGroupManagerAllInstancesConfig|null);

InstanceGroupManager allInstancesConfig

### autoHealingPolicies
    
    
    autoHealingPolicies?: (google.cloud.compute.v1beta.IInstanceGroupManagerAutoHealingPolicy[]|null);

InstanceGroupManager autoHealingPolicies

### baseInstanceName
    
    
    baseInstanceName?: (string|null);

InstanceGroupManager baseInstanceName

### creationTimestamp
    
    
    creationTimestamp?: (string|null);

InstanceGroupManager creationTimestamp

### currentActions
    
    
    currentActions?: (google.cloud.compute.v1beta.IInstanceGroupManagerActionsSummary|null);

InstanceGroupManager currentActions

### description
    
    
    description?: (string|null);

InstanceGroupManager description

### distributionPolicy
    
    
    distributionPolicy?: (google.cloud.compute.v1beta.IDistributionPolicy|null);

InstanceGroupManager distributionPolicy

### failoverAction
    
    
    failoverAction?: (string|null);

InstanceGroupManager failoverAction

### fingerprint
    
    
    fingerprint?: (string|null);

InstanceGroupManager fingerprint

### id
    
    
    id?: (number|Long|string|null);

InstanceGroupManager id

### instanceFlexibilityPolicy
    
    
    instanceFlexibilityPolicy?: (google.cloud.compute.v1beta.IInstanceGroupManagerInstanceFlexibilityPolicy|null);

InstanceGroupManager instanceFlexibilityPolicy

### instanceGroup
    
    
    instanceGroup?: (string|null);

InstanceGroupManager instanceGroup

### instanceLifecyclePolicy
    
    
    instanceLifecyclePolicy?: (google.cloud.compute.v1beta.IInstanceGroupManagerInstanceLifecyclePolicy|null);

InstanceGroupManager instanceLifecyclePolicy

### instanceTemplate
    
    
    instanceTemplate?: (string|null);

InstanceGroupManager instanceTemplate

### kind
    
    
    kind?: (string|null);

InstanceGroupManager kind

### listManagedInstancesResults
    
    
    listManagedInstancesResults?: (string|null);

InstanceGroupManager listManagedInstancesResults

### multiMig
    
    
    multiMig?: (string|null);

InstanceGroupManager multiMig

### name
    
    
    name?: (string|null);

InstanceGroupManager name

### namedPorts
    
    
    namedPorts?: (google.cloud.compute.v1beta.INamedPort[]|null);

InstanceGroupManager namedPorts

### params
    
    
    params?: (google.cloud.compute.v1beta.IInstanceGroupManagerParams|null);

InstanceGroupManager params

### region
    
    
    region?: (string|null);

InstanceGroupManager region

### resourcePolicies
    
    
    resourcePolicies?: (google.cloud.compute.v1beta.IInstanceGroupManagerResourcePolicies|null);

InstanceGroupManager resourcePolicies

### satisfiesPzi
    
    
    satisfiesPzi?: (boolean|null);

InstanceGroupManager satisfiesPzi

### satisfiesPzs
    
    
    satisfiesPzs?: (boolean|null);

InstanceGroupManager satisfiesPzs

### selfLink
    
    
    selfLink?: (string|null);

InstanceGroupManager selfLink

### serviceAccount
    
    
    serviceAccount?: (string|null);

InstanceGroupManager serviceAccount

### standbyPolicy
    
    
    standbyPolicy?: (google.cloud.compute.v1beta.IInstanceGroupManagerStandbyPolicy|null);

InstanceGroupManager standbyPolicy

### statefulPolicy
    
    
    statefulPolicy?: (google.cloud.compute.v1beta.IStatefulPolicy|null);

InstanceGroupManager statefulPolicy

### status
    
    
    status?: (google.cloud.compute.v1beta.IInstanceGroupManagerStatus|null);

InstanceGroupManager status

### targetPools
    
    
    targetPools?: (string[]|null);

InstanceGroupManager targetPools

### targetSize
    
    
    targetSize?: (number|null);

InstanceGroupManager targetSize

### targetSizePolicy
    
    
    targetSizePolicy?: (google.cloud.compute.v1beta.IInstanceGroupManagerTargetSizePolicy|null);

InstanceGroupManager targetSizePolicy

### targetStoppedSize
    
    
    targetStoppedSize?: (number|null);

InstanceGroupManager targetStoppedSize

### targetSuspendedSize
    
    
    targetSuspendedSize?: (number|null);

InstanceGroupManager targetSuspendedSize

### updatePolicy
    
    
    updatePolicy?: (google.cloud.compute.v1beta.IInstanceGroupManagerUpdatePolicy|null);

InstanceGroupManager updatePolicy

### versions
    
    
    versions?: (google.cloud.compute.v1beta.IInstanceGroupManagerVersion[]|null);

InstanceGroupManager versions

### zone
    
    
    zone?: (string|null);

InstanceGroupManager zone

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
