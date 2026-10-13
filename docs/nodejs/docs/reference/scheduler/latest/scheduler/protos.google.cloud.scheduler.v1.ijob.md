---
url: https://docs.cloud.google.com/nodejs/docs/reference/scheduler/latest/scheduler/protos.google.cloud.scheduler.v1.ijob
title: Interface protos.google.cloud.scheduler.v1.IJob (6.1.1) \u00a0|\u00a0 Node.js client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:47:28.931682+00:00
---

# Interface protos.google.cloud.scheduler.v1.IJob (6.1.1)  |  Node.js client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/nodejs/docs/reference/scheduler/latest/scheduler/protos.google.cloud.scheduler.v1.ijob

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Node.js ](https://docs.cloud.google.com/nodejs/docs)
  * [ Client libraries ](https://docs.cloud.google.com/nodejs/docs/reference)



Send feedback 

#  Interface protos.google.cloud.scheduler.v1.IJob (6.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

6.1.1 (latest)  5.4.0  5.2.0  3.3.1  3.2.1  3.0.5  2.3.0  2.2.6  2.1.1 

Properties of a Job.

## Package

[@google-cloud/scheduler](https://docs.cloud.google.com/nodejs/docs/reference/scheduler/latest/overview.html)

## Properties 

### appEngineHttpTarget
    
    
    appEngineHttpTarget?: (google.cloud.scheduler.v1.IAppEngineHttpTarget|null);

Job appEngineHttpTarget

### attemptDeadline
    
    
    attemptDeadline?: (google.protobuf.IDuration|null);

Job attemptDeadline

### description
    
    
    description?: (string|null);

Job description

### httpTarget
    
    
    httpTarget?: (google.cloud.scheduler.v1.IHttpTarget|null);

Job httpTarget

### lastAttemptTime
    
    
    lastAttemptTime?: (google.protobuf.ITimestamp|null);

Job lastAttemptTime

### name
    
    
    name?: (string|null);

Job name

### pubsubTarget
    
    
    pubsubTarget?: (google.cloud.scheduler.v1.IPubsubTarget|null);

Job pubsubTarget

### retryConfig
    
    
    retryConfig?: (google.cloud.scheduler.v1.IRetryConfig|null);

Job retryConfig

### schedule
    
    
    schedule?: (string|null);

Job schedule

### scheduleTime
    
    
    scheduleTime?: (google.protobuf.ITimestamp|null);

Job scheduleTime

### state
    
    
    state?: (google.cloud.scheduler.v1.Job.State|keyof typeof google.cloud.scheduler.v1.Job.State|null);

Job state

### status
    
    
    status?: (google.rpc.IStatus|null);

Job status

### timeZone
    
    
    timeZone?: (string|null);

Job timeZone

### userUpdateTime
    
    
    userUpdateTime?: (google.protobuf.ITimestamp|null);

Job userUpdateTime

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
