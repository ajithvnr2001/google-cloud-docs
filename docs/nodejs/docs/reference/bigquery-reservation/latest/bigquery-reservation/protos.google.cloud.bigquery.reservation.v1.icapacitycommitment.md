---
url: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/bigquery-reservation/protos.google.cloud.bigquery.reservation.v1.icapacitycommitment
title: Interface protos.google.cloud.bigquery.reservation.v1.ICapacityCommitment (5.3.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:43.696041+00:00
---

# Interface protos.google.cloud.bigquery.reservation.v1.ICapacityCommitment (5.3.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/bigquery-reservation/protos.google.cloud.bigquery.reservation.v1.icapacitycommitment

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.bigquery.reservation.v1.ICapacityCommitment (5.3.1) Stay organized with collections  Save and categorize content based on your preferences. 

5.3.1 (latest)  5.2.0  4.4.0  3.5.0  3.4.0  2.2.1  2.1.1  2.0.4  1.4.0  1.3.0  1.2.0  1.1.6 

Properties of a CapacityCommitment.

## Package

[@google-cloud/bigquery-reservation](https://docs.cloud.google.com/nodejs/docs/reference/bigquery-reservation/latest/overview.html)

## Properties 

### commitmentEndTime
    
    
    commitmentEndTime?: (google.protobuf.ITimestamp|null);

CapacityCommitment commitmentEndTime

### commitmentStartTime
    
    
    commitmentStartTime?: (google.protobuf.ITimestamp|null);

CapacityCommitment commitmentStartTime

### edition
    
    
    edition?: (google.cloud.bigquery.reservation.v1.Edition|keyof typeof google.cloud.bigquery.reservation.v1.Edition|null);

CapacityCommitment edition

### failureStatus
    
    
    failureStatus?: (google.rpc.IStatus|null);

CapacityCommitment failureStatus

### isFlatRate
    
    
    isFlatRate?: (boolean|null);

CapacityCommitment isFlatRate

### multiRegionAuxiliary
    
    
    multiRegionAuxiliary?: (boolean|null);

CapacityCommitment multiRegionAuxiliary

### name
    
    
    name?: (string|null);

CapacityCommitment name

### plan
    
    
    plan?: (google.cloud.bigquery.reservation.v1.CapacityCommitment.CommitmentPlan|keyof typeof google.cloud.bigquery.reservation.v1.CapacityCommitment.CommitmentPlan|null);

CapacityCommitment plan

### renewalPlan
    
    
    renewalPlan?: (google.cloud.bigquery.reservation.v1.CapacityCommitment.CommitmentPlan|keyof typeof google.cloud.bigquery.reservation.v1.CapacityCommitment.CommitmentPlan|null);

CapacityCommitment renewalPlan

### slotCount
    
    
    slotCount?: (number|Long|string|null);

CapacityCommitment slotCount

### state
    
    
    state?: (google.cloud.bigquery.reservation.v1.CapacityCommitment.State|keyof typeof google.cloud.bigquery.reservation.v1.CapacityCommitment.State|null);

CapacityCommitment state

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
