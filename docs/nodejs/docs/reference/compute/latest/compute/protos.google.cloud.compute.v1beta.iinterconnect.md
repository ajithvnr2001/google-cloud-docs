---
url: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinterconnect
title: Interface protos.google.cloud.compute.v1beta.IInterconnect (7.6.0) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:56.486671+00:00
---

# Interface protos.google.cloud.compute.v1beta.IInterconnect (7.6.0)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/compute/protos.google.cloud.compute.v1beta.iinterconnect

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.compute.v1beta.IInterconnect (7.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

7.6.0 (latest)  7.5.1  7.2.0  6.14.0  6.13.0  6.12.0  6.11.0  6.9.0  6.7.0  6.5.0  4.11.0  4.10.0  4.9.0  4.8.0  4.6.0  4.5.0  4.3.0  4.1.0  3.9.1  3.8.1  3.6.0  3.5.1  3.1.2  3.0.0 

Properties of an Interconnect.

## Package

[@google-cloud/compute](https://docs.cloud.google.com/nodejs/docs/reference/compute/latest/overview.html)

## Properties 

### aaiEnabled
    
    
    aaiEnabled?: (boolean|null);

Interconnect aaiEnabled

### adminEnabled
    
    
    adminEnabled?: (boolean|null);

Interconnect adminEnabled

### applicationAwareInterconnect
    
    
    applicationAwareInterconnect?: (google.cloud.compute.v1beta.IInterconnectApplicationAwareInterconnect|null);

Interconnect applicationAwareInterconnect

### availableFeatures
    
    
    availableFeatures?: (string[]|null);

Interconnect availableFeatures

### circuitInfos
    
    
    circuitInfos?: (google.cloud.compute.v1beta.IInterconnectCircuitInfo[]|null);

Interconnect circuitInfos

### creationTimestamp
    
    
    creationTimestamp?: (string|null);

Interconnect creationTimestamp

### customerName
    
    
    customerName?: (string|null);

Interconnect customerName

### description
    
    
    description?: (string|null);

Interconnect description

### effectiveLocation
    
    
    effectiveLocation?: (string|null);

Interconnect effectiveLocation

### expectedOutages
    
    
    expectedOutages?: (google.cloud.compute.v1beta.IInterconnectOutageNotification[]|null);

Interconnect expectedOutages

### googleIpAddress
    
    
    googleIpAddress?: (string|null);

Interconnect googleIpAddress

### googleReferenceId
    
    
    googleReferenceId?: (string|null);

Interconnect googleReferenceId

### id
    
    
    id?: (number|Long|string|null);

Interconnect id

### interconnectAttachments
    
    
    interconnectAttachments?: (string[]|null);

Interconnect interconnectAttachments

### interconnectGroups
    
    
    interconnectGroups?: (string[]|null);

Interconnect interconnectGroups

### interconnectType
    
    
    interconnectType?: (string|null);

Interconnect interconnectType

### kind
    
    
    kind?: (string|null);

Interconnect kind

### labelFingerprint
    
    
    labelFingerprint?: (string|null);

Interconnect labelFingerprint

### labels
    
    
    labels?: ({ [k: string]: string }|null);

Interconnect labels

### linkType
    
    
    linkType?: (string|null);

Interconnect linkType

### location
    
    
    location?: (string|null);

Interconnect location

### macsec
    
    
    macsec?: (google.cloud.compute.v1beta.IInterconnectMacsec|null);

Interconnect macsec

### macsecEnabled
    
    
    macsecEnabled?: (boolean|null);

Interconnect macsecEnabled

### name
    
    
    name?: (string|null);

Interconnect name

### nocContactEmail
    
    
    nocContactEmail?: (string|null);

Interconnect nocContactEmail

### operationalStatus
    
    
    operationalStatus?: (string|null);

Interconnect operationalStatus

### params
    
    
    params?: (google.cloud.compute.v1beta.IInterconnectParams|null);

Interconnect params

### peerIpAddress
    
    
    peerIpAddress?: (string|null);

Interconnect peerIpAddress

### provisionedLinkCount
    
    
    provisionedLinkCount?: (number|null);

Interconnect provisionedLinkCount

### remoteLocation
    
    
    remoteLocation?: (string|null);

Interconnect remoteLocation

### requestedFeatures
    
    
    requestedFeatures?: (string[]|null);

Interconnect requestedFeatures

### requestedLinkCount
    
    
    requestedLinkCount?: (number|null);

Interconnect requestedLinkCount

### satisfiesPzs
    
    
    satisfiesPzs?: (boolean|null);

Interconnect satisfiesPzs

### selfLink
    
    
    selfLink?: (string|null);

Interconnect selfLink

### selfLinkWithId
    
    
    selfLinkWithId?: (string|null);

Interconnect selfLinkWithId

### state
    
    
    state?: (string|null);

Interconnect state

### subzone
    
    
    subzone?: (string|null);

Interconnect subzone

### wireGroups
    
    
    wireGroups?: (string[]|null);

Interconnect wireGroups

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
