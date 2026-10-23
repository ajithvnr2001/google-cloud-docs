---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/kube-controller-manager/
title: Troubleshoot the Kubernetes controller manager \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:07.597792+00:00
---

# Troubleshoot the Kubernetes controller manager  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/kube-controller-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Troubleshoot the Kubernetes controller manager Stay organized with collections  Save and categorize content based on your preferences. 

This pages shows you how to resolve issues with the Kubernetes controller manager (`kube-controller-manager`) for Google Distributed Cloud.

## Leader election lost

This error might be observed in a regional cluster or replicated control plane when `kube-controller-manager` (KCM) restarts unexpectedly. This restart might involve quitting itself or being restarted by `kubelet`. The KCM logs might include `leaderelection lost` messages.

This scenario can occur when the leader checks if it's still actively leading as part of the KCM health check.

If the leader is no longer leading or the lease check fails, the health check reports to be unhealthy, and the leader is restarted.

The leader election status can be retrieved by getting the `Lease` resources of the `coordination.k8s.io` group:

  1. To see all leases, run the following `kubectl` command:
         
         kubectl -n kube-system get lease
         

  2. To check status of a given lease, such as `lease/kube-controller-manager`, use the following `kubectl describe` command:
         
         kubectl -n kube-system describe lease/kube-controller-manager
         

Under the `Events` section, check for `LeaderElection` events. Review who takes the leadership and when that happens. The following example output shows that when the first node was manually shut down, the second instantaneously takes over the leadership:
         
         Events:
           Type    Reason          Age    From                     Message
           ----    ------          ----   ----                     -------
           Normal  LeaderElection  26m    kube-controller-manager  control-plane_056a86ec-84c5-48b8-b58d-86f3fde2ecdd became leader
           Normal  LeaderElection  5m20s  kube-controller-manager  control-plane2_b0475d49-7010-4f03-8a9d-34f82ed60cd4 became leader
         

You can also observe the process of losing and gaining leadership by using the `kubernetes.io/anthos/leader_election_master_status` metric grouped by `name`.




The leader election process only happens if the current leader fails. You can confirm the failure by looking at `kubernetes.io/anthos/container/uptime` and `kubernetes.io/anthos/container/restart_count` metrics filtered by a `container_name` of `kube-controller-manager`.

If you experience issues of the leader election process repeatedly running or failing, review the following remediation considerations:

  * If KCM restarts every few minutes or less, check the KCM logs for failed requests to API server. Failed requests indicate connectivity issues between the components or part of the service is overloaded.
  * If the controller manager fails to communicate with the API server for too long, the renewal fails and the KCM instance loses its leadership, even if the connection is later restored.
  * If the control plane is replicated, the new leader should smoothly take over without downtime. No action is required. The control plane of a multi-cloud or regional cluster is always replicated. Don't attempt to disable leader election for a replicated control plane. You can't re-enable leader election without downtime.



## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support) for more information about support resources, including the following: 

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#intro-support) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#support-tools) to help you troubleshoot, such as your environment configuration, logs, and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/getting-support#what-we-support).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
