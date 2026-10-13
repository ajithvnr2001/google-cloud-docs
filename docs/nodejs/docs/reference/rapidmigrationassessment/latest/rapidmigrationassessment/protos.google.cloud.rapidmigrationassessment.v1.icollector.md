---
url: https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.icollector
title: Interface protos.google.cloud.rapidmigrationassessment.v1.ICollector (3.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:25:13.260464+00:00
---

# Interface protos.google.cloud.rapidmigrationassessment.v1.ICollector (3.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/rapidmigrationassessment/protos.google.cloud.rapidmigrationassessment.v1.icollector

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.rapidmigrationassessment.v1.ICollector (3.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

3.1.1 (latest)  2.1.0  2.0.1 

Properties of a Collector.

## Package

[@google-cloud/rapidmigrationassessment](https://docs.cloud.google.com/nodejs/docs/reference/rapidmigrationassessment/latest/overview.html)

## Properties 

### bucket
    
    
    bucket?: (string|null);

Collector bucket

### clientVersion
    
    
    clientVersion?: (string|null);

Collector clientVersion

### collectionDays
    
    
    collectionDays?: (number|null);

Collector collectionDays

### createTime
    
    
    createTime?: (google.protobuf.ITimestamp|null);

Collector createTime

### description
    
    
    description?: (string|null);

Collector description

### displayName
    
    
    displayName?: (string|null);

Collector displayName

### eulaUri
    
    
    eulaUri?: (string|null);

Collector eulaUri

### expectedAssetCount
    
    
    expectedAssetCount?: (number|Long|string|null);

Collector expectedAssetCount

### guestOsScan
    
    
    guestOsScan?: (google.cloud.rapidmigrationassessment.v1.IGuestOsScan|null);

Collector guestOsScan

### labels
    
    
    labels?: ({ [k: string]: string }|null);

Collector labels

### name
    
    
    name?: (string|null);

Collector name

### serviceAccount
    
    
    serviceAccount?: (string|null);

Collector serviceAccount

### state
    
    
    state?: (google.cloud.rapidmigrationassessment.v1.Collector.State|keyof typeof google.cloud.rapidmigrationassessment.v1.Collector.State|null);

Collector state

### updateTime
    
    
    updateTime?: (google.protobuf.ITimestamp|null);

Collector updateTime

### vsphereScan
    
    
    vsphereScan?: (google.cloud.rapidmigrationassessment.v1.IVSphereScan|null);

Collector vsphereScan

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
