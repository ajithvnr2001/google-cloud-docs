---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ischeduling
title: Interface protos.google.cloud.compute.v1.IScheduling (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:02:49.428464+00:00
---

# Interface protos.google.cloud.compute.v1.IScheduling (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1.ischeduling

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.compute.v1.IScheduling (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Properties of a Scheduling.

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Properties 

### automaticRestart
    
    
    automaticRestart?: (boolean|null);

Scheduling automaticRestart

### availabilityDomain
    
    
    availabilityDomain?: (number|null);

Scheduling availabilityDomain

### exposeHostTopology
    
    
    exposeHostTopology?: (boolean|null);

Scheduling exposeHostTopology

### gracefulShutdown
    
    
    gracefulShutdown?: (google.cloud.compute.v1.ISchedulingGracefulShutdown|null);

Scheduling gracefulShutdown

### hostErrorTimeoutSeconds
    
    
    hostErrorTimeoutSeconds?: (number|null);

Scheduling hostErrorTimeoutSeconds

### instanceTerminationAction
    
    
    instanceTerminationAction?: (string|null);

Scheduling instanceTerminationAction

### localSsdRecoveryTimeout
    
    
    localSsdRecoveryTimeout?: (google.cloud.compute.v1.IDuration|null);

Scheduling localSsdRecoveryTimeout

### locationHint
    
    
    locationHint?: (string|null);

Scheduling locationHint

### maxRunDuration
    
    
    maxRunDuration?: (google.cloud.compute.v1.IDuration|null);

Scheduling maxRunDuration

### minNodeCpus
    
    
    minNodeCpus?: (number|null);

Scheduling minNodeCpus

### nodeAffinities
    
    
    nodeAffinities?: (google.cloud.compute.v1.ISchedulingNodeAffinity[]|null);

Scheduling nodeAffinities

### onHostMaintenance
    
    
    onHostMaintenance?: (string|null);

Scheduling onHostMaintenance

### onInstanceStopAction
    
    
    onInstanceStopAction?: (google.cloud.compute.v1.ISchedulingOnInstanceStopAction|null);

Scheduling onInstanceStopAction

### preemptible
    
    
    preemptible?: (boolean|null);

Scheduling preemptible

### preemptionNoticeDuration
    
    
    preemptionNoticeDuration?: (google.cloud.compute.v1.IDuration|null);

Scheduling preemptionNoticeDuration

### provisioningModel
    
    
    provisioningModel?: (string|null);

Scheduling provisioningModel

### skipGuestOsShutdown
    
    
    skipGuestOsShutdown?: (boolean|null);

Scheduling skipGuestOsShutdown

### terminationTime
    
    
    terminationTime?: (string|null);

Scheduling terminationTime

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
