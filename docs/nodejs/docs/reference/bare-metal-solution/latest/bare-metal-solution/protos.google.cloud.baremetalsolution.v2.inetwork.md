---
url: https://docs.cloud.google.com/nodejs/docs/reference/bare-metal-solution/latest/bare-metal-solution/protos.google.cloud.baremetalsolution.v2.inetwork
title: Interface protos.google.cloud.baremetalsolution.v2.INetwork (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:01:14.752775+00:00
---

# Interface protos.google.cloud.baremetalsolution.v2.INetwork (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bare-metal-solution/latest/bare-metal-solution/protos.google.cloud.baremetalsolution.v2.inetwork

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.baremetalsolution.v2.INetwork (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  1.1.0  0.3.2  0.2.2 

Properties of a Network.

## Package

[@google-cloud/bare-metal-solution](https://docs.cloud.google.com/nodejs/docs/reference/bare-metal-solution/latest/overview.html)

## Properties 

### cidr
    
    
    cidr?: (string|null);

Network cidr

### gatewayIp
    
    
    gatewayIp?: (string|null);

Network gatewayIp

### id
    
    
    id?: (string|null);

Network id

### ipAddress
    
    
    ipAddress?: (string|null);

Network ipAddress

### jumboFramesEnabled
    
    
    jumboFramesEnabled?: (boolean|null);

Network jumboFramesEnabled

### labels
    
    
    labels?: ({ [k: string]: string }|null);

Network labels

### macAddress
    
    
    macAddress?: (string[]|null);

Network macAddress

### mountPoints
    
    
    mountPoints?: (google.cloud.baremetalsolution.v2.INetworkMountPoint[]|null);

Network mountPoints

### name
    
    
    name?: (string|null);

Network name

### pod
    
    
    pod?: (string|null);

Network pod

### reservations
    
    
    reservations?: (google.cloud.baremetalsolution.v2.INetworkAddressReservation[]|null);

Network reservations

### servicesCidr
    
    
    servicesCidr?: (string|null);

Network servicesCidr

### state
    
    
    state?: (google.cloud.baremetalsolution.v2.Network.State|keyof typeof google.cloud.baremetalsolution.v2.Network.State|null);

Network state

### type
    
    
    type?: (google.cloud.baremetalsolution.v2.Network.Type|keyof typeof google.cloud.baremetalsolution.v2.Network.Type|null);

Network type

### vlanId
    
    
    vlanId?: (string|null);

Network vlanId

### vrf
    
    
    vrf?: (google.cloud.baremetalsolution.v2.IVRF|null);

Network vrf

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
