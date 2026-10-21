---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/revision/
title: Rolling updates \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:37:17.857780+00:00
---

# Rolling updates  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/revision/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Rolling updates Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.13 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.13 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/revision.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/revision.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/revision.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/revision.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/revision.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/revision.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/revision.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/revision.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/revision.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/revision.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/revision.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/revision.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/revision.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/revision.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/revision.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/revision.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/revision.html)



Apigee hybrid supports two kinds of updates. The first is an _in-place update_ where you apply a configuration change and hybrid begins a Kubernetes [rolling update](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/). In Kubernetes, rolling updates allow Deployment updates to take place with zero downtime by incrementally updating Pod instances with new ones. 

Apigee hybrid also supports a canary or AB-style update. In an AB update, the new revision is deployed; however, at first a small percentage of traffic is directed to it. Over time, this percentage increases until all of the traffic goes to the revision. 

##  In-place updates 

To trigger an in-place update, simply modify the desired settings in the overrides file and apply it to the cluster. For example, suppose you want to change the current `runtime` memory from 1Gi to 5Gi: 

Here is the initial configuration: 
    
    
    ...
    runtime:
      replicaCountMin: 2
      replicaCountMax: 20
      resources:
        requests:
          cpu: 1000m
          memory: 1Gi
    ...

In the new configuration, memory is changed to 5Gi: 
    
    
    ...
    runtime:
      replicaCountMin: 2
      replicaCountMax: 20
      resources:
        requests:
          cpu: 1000m
          memory: 5Gi
    ...

When you apply the change, the updated pods start up and replace the existing pods. Because of the Kubernetes rolling update feature, clients do not experience any downtime.

##  How to perform an AB update 

To perform an AB update, use the `revision` tag in your overrides file. For example, suppose you want to change the current `runtime` memory from 1Gi to 5Gi: 

In the current configuration, `revision` is set to `blue`: 
    
    
    ...
    revision: blue
    ...
    runtime:
      replicaCountMin: 2
      replicaCountMax: 20
      resources:
        requests:
          cpu: 1000m
          memory: 1Gi
    ...

In the new configuration, if you change `revision` to `green`, you signal that you want to perform a rolling update when the change is applied. The value you set `revision` to does not matter; you can use any string you wish, as long as you change it from the previous value to something else. 
    
    
    ...
    revision: green
    ...
    runtime:
      replicaCountMin: 2
      replicaCountMax: 20
      resources:
        requests:
          cpu: 1000m
          memory: 5Gi
    ...

When you apply the change, a small percentage of traffic to the new revision. Over time, more traffic goes to the new revision until it reaches 100%. At that time, the old revision is deleted.

To trigger an AB rollout, either add the `revision` tag if it is not present, or change the value of the `revision` tag if it is already present. You are not required to make any other changes to the overrides file to trigger an AB rollout. 

The following table the schedule of an AB rollout: 

Stage | Traffic percentage | Wait time  
---|---|---  
1 | 5% | 60 seconds  
2 | 20% | 10 seconds  
3 | 100% | 10 seconds  
  
In the current release, the percentages and wait times are not configurable. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
