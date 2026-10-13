---
url: https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.Event
title: Google Cloud Life Sciences V2beta Client - Class Event (0.10.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:37.515788+00:00
---

# Google Cloud Life Sciences V2beta Client - Class Event (0.10.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.Event

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Google Cloud Life Sciences V2beta Client - Class Event (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.9.0  0.8.1  0.7.3  0.6.8  0.5.4  0.4.0  0.3.5 

**Beta**

This library is covered by the [Pre-GA Offerings Terms](https://docs.cloud.google.com/terms/service-terms#1) of the Terms of Service. Pre-GA libraries might have limited support, and changes to pre-GA libraries might not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://docs.cloud.google.com/products#product-launch-stages). 

Reference documentation and code samples for the Google Cloud Life Sciences V2beta Client class Event.

Carries information about events that occur during pipeline execution.

Generated from protobuf message `google.cloud.lifesciences.v2beta.Event`

## Namespace

Google \ Cloud \ LifeSciences \ V2beta

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ timestamp` |  `Google\Protobuf\Timestamp`   
The time at which the event occurred.  
`↳ description` |  `string`   
A human-readable description of the event. Note that these strings can change at any time without notice. Any application logic must use the information in the `details` field.  
`↳ delayed` |  `[DelayedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.DelayedEvent)`   
See [google.cloud.lifesciences.v2beta.DelayedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.DelayedEvent).  
`↳ worker_assigned` |  `[WorkerAssignedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.WorkerAssignedEvent)`   
See [google.cloud.lifesciences.v2beta.WorkerAssignedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.WorkerAssignedEvent).  
`↳ worker_released` |  `[WorkerReleasedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.WorkerReleasedEvent)`   
See [google.cloud.lifesciences.v2beta.WorkerReleasedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.WorkerReleasedEvent).  
`↳ pull_started` |  `[PullStartedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.PullStartedEvent)`   
See [google.cloud.lifesciences.v2beta.PullStartedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.PullStartedEvent).  
`↳ pull_stopped` |  `[PullStoppedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.PullStoppedEvent)`   
See [google.cloud.lifesciences.v2beta.PullStoppedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.PullStoppedEvent).  
`↳ container_started` |  `[ContainerStartedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ContainerStartedEvent)`   
See [google.cloud.lifesciences.v2beta.ContainerStartedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ContainerStartedEvent).  
`↳ container_stopped` |  `[ContainerStoppedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ContainerStoppedEvent)`   
See [google.cloud.lifesciences.v2beta.ContainerStoppedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ContainerStoppedEvent).  
`↳ container_killed` |  `[ContainerKilledEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ContainerKilledEvent)`   
See [google.cloud.lifesciences.v2beta.ContainerKilledEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ContainerKilledEvent).  
`↳ unexpected_exit_status` |  `[UnexpectedExitStatusEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.UnexpectedExitStatusEvent)`   
See [google.cloud.lifesciences.v2beta.UnexpectedExitStatusEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.UnexpectedExitStatusEvent).  
`↳ failed` |  `[FailedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.FailedEvent)`   
See [google.cloud.lifesciences.v2beta.FailedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.FailedEvent).  
  
### getTimestamp

The time at which the event occurred.

**Returns**  
---  
**Type** | **Description**  
`Google\Protobuf\Timestamp|null` |   
  
### hasTimestamp

### clearTimestamp

### setTimestamp

The time at which the event occurred.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `Google\Protobuf\Timestamp`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDescription

A human-readable description of the event. Note that these strings can change at any time without notice. Any application logic must use the information in the `details` field.

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
### setDescription

A human-readable description of the event. Note that these strings can change at any time without notice. Any application logic must use the information in the `details` field.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `string`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDelayed

See [google.cloud.lifesciences.v2beta.DelayedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.DelayedEvent).

**Returns**  
---  
**Type** | **Description**  
`[DelayedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.DelayedEvent)|null` |   
  
### hasDelayed

### setDelayed

See [google.cloud.lifesciences.v2beta.DelayedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.DelayedEvent).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[DelayedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.DelayedEvent)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getWorkerAssigned

See [google.cloud.lifesciences.v2beta.WorkerAssignedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.WorkerAssignedEvent).

**Returns**  
---  
**Type** | **Description**  
`[WorkerAssignedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.WorkerAssignedEvent)|null` |   
  
### hasWorkerAssigned

### setWorkerAssigned

See [google.cloud.lifesciences.v2beta.WorkerAssignedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.WorkerAssignedEvent).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[WorkerAssignedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.WorkerAssignedEvent)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getWorkerReleased

See [google.cloud.lifesciences.v2beta.WorkerReleasedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.WorkerReleasedEvent).

**Returns**  
---  
**Type** | **Description**  
`[WorkerReleasedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.WorkerReleasedEvent)|null` |   
  
### hasWorkerReleased

### setWorkerReleased

See [google.cloud.lifesciences.v2beta.WorkerReleasedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.WorkerReleasedEvent).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[WorkerReleasedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.WorkerReleasedEvent)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPullStarted

See [google.cloud.lifesciences.v2beta.PullStartedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.PullStartedEvent).

**Returns**  
---  
**Type** | **Description**  
`[PullStartedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.PullStartedEvent)|null` |   
  
### hasPullStarted

### setPullStarted

See [google.cloud.lifesciences.v2beta.PullStartedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.PullStartedEvent).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[PullStartedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.PullStartedEvent)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getPullStopped

See [google.cloud.lifesciences.v2beta.PullStoppedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.PullStoppedEvent).

**Returns**  
---  
**Type** | **Description**  
`[PullStoppedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.PullStoppedEvent)|null` |   
  
### hasPullStopped

### setPullStopped

See [google.cloud.lifesciences.v2beta.PullStoppedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.PullStoppedEvent).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[PullStoppedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.PullStoppedEvent)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getContainerStarted

See [google.cloud.lifesciences.v2beta.ContainerStartedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ContainerStartedEvent).

**Returns**  
---  
**Type** | **Description**  
`[ContainerStartedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ContainerStartedEvent)|null` |   
  
### hasContainerStarted

### setContainerStarted

See [google.cloud.lifesciences.v2beta.ContainerStartedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ContainerStartedEvent).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[ContainerStartedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ContainerStartedEvent)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getContainerStopped

See [google.cloud.lifesciences.v2beta.ContainerStoppedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ContainerStoppedEvent).

**Returns**  
---  
**Type** | **Description**  
`[ContainerStoppedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ContainerStoppedEvent)|null` |   
  
### hasContainerStopped

### setContainerStopped

See [google.cloud.lifesciences.v2beta.ContainerStoppedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ContainerStoppedEvent).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[ContainerStoppedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ContainerStoppedEvent)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getContainerKilled

See [google.cloud.lifesciences.v2beta.ContainerKilledEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ContainerKilledEvent).

**Returns**  
---  
**Type** | **Description**  
`[ContainerKilledEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ContainerKilledEvent)|null` |   
  
### hasContainerKilled

### setContainerKilled

See [google.cloud.lifesciences.v2beta.ContainerKilledEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ContainerKilledEvent).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[ContainerKilledEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.ContainerKilledEvent)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getUnexpectedExitStatus

See [google.cloud.lifesciences.v2beta.UnexpectedExitStatusEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.UnexpectedExitStatusEvent).

**Returns**  
---  
**Type** | **Description**  
`[UnexpectedExitStatusEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.UnexpectedExitStatusEvent)|null` |   
  
### hasUnexpectedExitStatus

### setUnexpectedExitStatus

See [google.cloud.lifesciences.v2beta.UnexpectedExitStatusEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.UnexpectedExitStatusEvent).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[UnexpectedExitStatusEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.UnexpectedExitStatusEvent)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getFailed

See [google.cloud.lifesciences.v2beta.FailedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.FailedEvent).

**Returns**  
---  
**Type** | **Description**  
`[FailedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.FailedEvent)|null` |   
  
### hasFailed

### setFailed

See [google.cloud.lifesciences.v2beta.FailedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.FailedEvent).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[FailedEvent](https://docs.cloud.google.com/php/docs/reference/cloud-life-sciences/latest/V2beta.FailedEvent)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getDetails

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
