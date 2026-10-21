---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/vcenter-down/
title: If vCenter Server is down \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:19:59.833775+00:00
---

# If vCenter Server is down  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/vcenter-down/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  If vCenter Server is down Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how a cluster behaves if vCenter Server is down.

While vCenter Server is down:

  * The machines are in the `Available` state

  * The nodes are in the `Ready` state.

  * The Pods are in the `Running` state.

  * There are some expected errors in Pods that connect to vCenter Server; for example, the `vsphere-controller-manager` and `cluster-health-controller` Pods.

  * Stateless Pods can be created and deleted.

  * The creation of a stateful Pod will fail, because attaching a disk requires access to vCenter Server. These Pods will be in the `Pending` state.

  * The `gkectl diagnose` command will fail with an error similar to the following:
        
        Exit with error:
        failed to prepare diagnose parameters: failed to create vSphere client: Post "https://my-server": dial tcp 203.0.113.1:443: connect: connection timed out
        

  * Auto repair is not triggered. This is because the machine and node states do not change states on connection errors to vCenter Server.




After vCenter Server comes back online (versions < 7.0U2)

  * The machines go to the `Unavailable` state, and auto repair or or a manual workaround is needed to get back the correct states.

  * The cluster functions correctly even though the machines are in the `Unavailable` state.




After vCenter Server comes back online (versions >= 7.0U2)

  * No extra steps are needed, and the cluster is healthy again.



## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). 

You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for more information about support resources, including the following:

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_requirements) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_tools) to help you troubleshoot, such as logs and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#whats_supported), [versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#version-support), and [features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#supported_features) of Google Distributed Cloud for VMware (software only).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
