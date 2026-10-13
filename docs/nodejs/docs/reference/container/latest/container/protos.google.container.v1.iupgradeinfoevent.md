---
url: https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.iupgradeinfoevent
title: Interface protos.google.container.v1.IUpgradeInfoEvent (7.2.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:42:35.046491+00:00
---

# Interface protos.google.container.v1.IUpgradeInfoEvent (7.2.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/container/latest/container/protos.google.container.v1.iupgradeinfoevent

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.container.v1.IUpgradeInfoEvent (7.2.1) Stay organized with collections  Save and categorize content based on your preferences. 

7.2.1 (latest)  7.1.0  6.8.0  6.7.0  6.1.0  5.19.0  5.17.0  5.15.1  5.14.0  5.10.0  5.9.0  5.8.0  5.6.0  5.5.0  5.4.1  5.1.0  4.11.0  4.10.0  4.9.0  4.7.1  4.4.0  4.3.0  4.2.0  4.1.3  3.0.0  2.6.0  2.5.0  2.4.4  2.3.2 

Properties of an UpgradeInfoEvent.

## Package

[@google-cloud/container](https://docs.cloud.google.com/nodejs/docs/reference/container/latest/overview.html)

## Properties 

### currentEmulatedVersion
    
    
    currentEmulatedVersion?: (string|null);

UpgradeInfoEvent currentEmulatedVersion

### currentVersion
    
    
    currentVersion?: (string|null);

UpgradeInfoEvent currentVersion

### description
    
    
    description?: (string|null);

UpgradeInfoEvent description

### disruptionEvent
    
    
    disruptionEvent?: (google.container.v1.IDisruptionEvent|null);

UpgradeInfoEvent disruptionEvent

### endTime
    
    
    endTime?: (google.protobuf.ITimestamp|null);

UpgradeInfoEvent endTime

### eventType
    
    
    eventType?: (google.container.v1.UpgradeInfoEvent.EventType|keyof typeof google.container.v1.UpgradeInfoEvent.EventType|null);

UpgradeInfoEvent eventType

### extendedSupportEndTime
    
    
    extendedSupportEndTime?: (google.protobuf.ITimestamp|null);

UpgradeInfoEvent extendedSupportEndTime

### operation
    
    
    operation?: (string|null);

UpgradeInfoEvent operation

### resource
    
    
    resource?: (string|null);

UpgradeInfoEvent resource

### resourceType
    
    
    resourceType?: (google.container.v1.UpgradeResourceType|keyof typeof google.container.v1.UpgradeResourceType|null);

UpgradeInfoEvent resourceType

### standardSupportEndTime
    
    
    standardSupportEndTime?: (google.protobuf.ITimestamp|null);

UpgradeInfoEvent standardSupportEndTime

### startTime
    
    
    startTime?: (google.protobuf.ITimestamp|null);

UpgradeInfoEvent startTime

### state
    
    
    state?: (google.container.v1.UpgradeInfoEvent.State|keyof typeof google.container.v1.UpgradeInfoEvent.State|null);

UpgradeInfoEvent state

### targetEmulatedVersion
    
    
    targetEmulatedVersion?: (string|null);

UpgradeInfoEvent targetEmulatedVersion

### targetVersion
    
    
    targetVersion?: (string|null);

UpgradeInfoEvent targetVersion

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
