---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/job-timeouts/
title: Adjust job timeout values \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:12:05.474542+00:00
---

# Adjust job timeout values  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/job-timeouts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Adjust job timeout values Stay organized with collections  Save and categorize content based on your preferences. 

If jobs in Google Distributed Cloud time out and you believe the behavior isn't due to an underlying problem with your installation, you can increase the timeout interval. This document describes how to adjust the timeout intervals for machine jobs and batch jobs by using annotations in the config spec.

## Job types and errors

There are two types of Google Distributed Cloud commands and routines: machine jobs and batch jobs. Many things can affect how long it takes for a job to complete, such as hardware configuration, network configuration, and cluster configuration. Google Distributed Cloud has default timeouts that are intended to accommodate typical installations.

The following are example job timeout error messages:

  * A machine job timeout error message (wrapped for clarity) from a preflight log like `bmctl-workspace/cluster1/logs/preflight-20210501-000426/172.18.0.4`:
        
        Pod:172.18.0.4-machine-preflf3a32c8a2f7a2449545c7e8ff954c961-652st
        Result:Failed Reason:DeadlineExceeded Time:Wed Feb  3 16:59:56 2021
        

  * Output from `kubectl logs` for a failed Pod might show a similar `DeadlineExceeded` message (wrapped):
        
        cluster-cluster1
        172.18.0.4-machine-preflf3a32c8a2f7a2449545c7e8ff954c961-652st  ●  0/1
        0 DeadlineExceeded  192.168.122.180  bmctl-control-plane  7m12
        




## Adjust the machine job timeout interval

A machine job is a routine that runs on one machine only, like a preflight check that is confined to a single machine. Google Distributed Cloud machine jobs have a default timeout of 900 seconds, or 15 minutes. You can adjust the machine job timeout interval with the `baremetal.cluster.gke.io/machine-job-deadline-seconds` annotation in the cluster config file.

The following example sets the machine job timeout interval to 1,800 seconds, or 30 minutes:
    
    
       apiVersion: baremetal.cluster.gke.io/v1
       kind: Cluster
       metadata:
         name: cluster1
         namespace: cluster-cluster1
         annotations:
           baremetal.cluster.gke.io/machine-job-deadline-seconds: "1800"
       spec:
       ...
    

Your timeout interval value is applied when you create new clusters with `bmctl create cluster` or when you upgrade existing clusters with `bmctl upgrade cluster`. The new interval is used for all single machine jobs, including `bmctl check preflight`, `bmctl check -c CLUSTER_NAME`, and more.

## Adjust the batch job timeout interval

A batch job is a routine that runs across multiple machines, like a network preflight check. The default timeout interval for Google Distributed Cloud batch jobs is dependent upon the number of machines in the network. The default timeout interval is 900 seconds, plus an additional 20 seconds for each machine.

For example, if your batch job runs on 60 machines, the default timeout interval is 2,100 seconds (_900 + (20 * 60) = 2100_), or 35 minutes.

You can adjust the batch job timeout interval with the `baremetal.cluster.gke.io/batch-job-deadline-seconds` annotation in the cluster config file.

The following example sets the batch job timeout interval to 10,800 seconds, or 3 hours:
    
    
       apiVersion: baremetal.cluster.gke.io/v1
       kind: Cluster
       metadata:
         name: cluster1
         namespace: cluster-cluster1
         annotations:
           baremetal.cluster.gke.io/batch-job-deadline-seconds: "10800"
       spec:
       ...
    

Your timeout interval value is applied when you create new clusters with `bmctl create cluster` or when you upgrade existing clusters with `bmctl upgrade cluster`.

## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
