---
url: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/job-timeouts/
title: Adjust job timeout values \u00a0|\u00a0 Google Distributed Cloud Virtual for Bare Metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T20:46:52.837132+00:00
---

# Adjust job timeout values  |  Google Distributed Cloud Virtual for Bare Metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/job-timeouts/

**Version 1.16**. This version is no longer supported. For information about how to upgrade to version 1.28, see [ Upgrade clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/upgrade) in the latest documentation. For more information about supported and unsupported versions, see the [Versioning](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/version-history) page in the latest documentation.

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for Bare Metal 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/concepts/about-bare-metal)



Send feedback 

#  Adjust job timeout values Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.16 keyboard_arrow_down

  * [ Latest ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/latest/troubleshooting/job-timeouts)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/troubleshooting/job-timeouts)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/bare-metal/1.16/getting-support#version-support)



If jobs are timing out and you believe the timeout is not due to an underlying problem with your installation, you can increase the timeout interval. This document describes how to adjust the timeout intervals for machine jobs and batch jobs with annotations to the config spec.

Distributed Cloud commands and routines fall into two categories, machine jobs and batch jobs. Many things can affect how long it takes for a job to complete, such as hardware configuration, network configuration, and cluster configuration. Google Distributed Cloud has default timeouts that are intended to accommodate typical installations.

Here are a couple of examples of where you can find job timeout error messages:

  * Machine job timeout error message (wrapped for clarity) from a preflight log, for example, `bmctl-workspace/cluster1/logs/preflight-20210501-000426/172.18.0.4`
        
        Pod:172.18.0.4-machine-preflf3a32c8a2f7a2449545c7e8ff954c961-652st
        Result:Failed Reason:DeadlineExceeded Time:Wed Feb  3 16:59:56 2021
        

  * Output from `kubectl logs` for a failed pod may show a similar `DeadlineExceeded` message (wrapped):
        
        cluster-cluster1
        172.18.0.4-machine-preflf3a32c8a2f7a2449545c7e8ff954c961-652st  ●  0/1
        0 DeadlineExceeded  192.168.122.180  bmctl-control-plane  7m12
        




## Adjusting the machine job timeout interval

A machine job is a routine that runs on one machine only, like a preflight check that is confined to a single machine. Google Distributed Cloud machine jobs have a default timeout of 900 seconds or 15 minutes. The machine job timeout interval is adjusted with the `baremetal.cluster.gke.io/machine-job-deadline-seconds` annotation in the cluster config file.

The following example sets the machine job timeout interval to 1800 seconds or 30 minutes:
    
    
       apiVersion: baremetal.cluster.gke.io/v1
       kind: Cluster
       metadata:
         name: cluster1
         namespace: cluster-cluster1
         annotations:
           baremetal.cluster.gke.io/machine-job-deadline-seconds: "1800"
       spec:
       ...
    

Your timeout interval value will be applied when you create new clusters with `bmctl create cluster` or when you upgrade existing clusters with `bmctl upgrade cluster`. The new interval will be used for all single machine jobs, including `bmctl check preflight`, `bmctl check -c <cluster-name>`, and more.

## Adjusting the batch job timeout interval

A batch job is a routine that runs across multiple machines, like a network preflight check. The default timeout interval for Google Distributed Cloud batch jobs is dependent upon the number of machines in the network. The default timeout interval is 900 seconds plus an additional 20 seconds for each machine. So, if your batch job runs on 60 machines, the default timeout interval is 2100 seconds (900 + 20 * 60 = 2100) or 35 minutes. The batch job timeout interval is adjusted with the `baremetal.cluster.gke.io/batch-job-deadline-seconds` annotation in the cluster config file.

The following example sets the batch job timeout interval to 10800 seconds or 3 hours:
    
    
       apiVersion: baremetal.cluster.gke.io/v1
       kind: Cluster
       metadata:
         name: cluster1
         namespace: cluster-cluster1
         annotations:
           baremetal.cluster.gke.io/batch-job-deadline-seconds: "10800"
       spec:
       ...
    

Your timeout interval value will be applied when you create new clusters with `bmctl create cluster` or when you upgrade existing clusters with `bmctl upgrade cluster`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
