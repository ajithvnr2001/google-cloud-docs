---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/reserved-hostports/
title: Reserved hostPorts \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:57.245918+00:00
---

# Reserved hostPorts  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/reserved-hostports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Reserved hostPorts Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes the list of reserved hostPorts within Google Kubernetes Engine (GKE).

**Note:** Always refer to the latest GKE release notes for any updates or changes to GKE's reserved hostPort ranges. When in doubt, avoid using hostPorts and rely on Kubernetes service abstractions.

## GKE System reserved hostPorts

GKE reserves specific `hostPort` ranges for its internal system processes and services. These reservations are crucial for maintaining the stability and functionality of GKE clusters. Although GKE generally discourages the use of `hostPort` for user applications due to potential conflicts and security risks, it relies on them for internal operations.

**Warning:** Attempting to use hostPorts within GKE's reserved ranges might result in Pod deployment failures or unexpected cluster behavior. GKE reserves the right to change these ranges without prior notice.

### Purpose of reserved hostPorts

  * **Control plane communication** : certain GKE components, such as the kubelet and metrics-server, might use specific hostPorts for communication with the control plane or other internal services.
  * **System daemons** : GKE system daemons and agents might require access to specific ports on the nodes for monitoring, logging, or other operational tasks.
  * **Internal services** : GKE's internal services, responsible for cluster management and health checks, might use reserved hostPorts.



### Understanding reserved ranges

Although the exact ranges can vary based on GKE version and configuration, GKE reserves a portion of the available port space. These reserved ranges are typically not documented for external user usage, as they are subject to change. It is very important to avoid using low-numbered ports, as these are commonly reserved by operating systems.

### Best practices

**Best practices** :

  * **Avoid hostPort usage** : minimize the use of hostPort in your application deployments to reduce the risk of conflicts with GKE's reserved ports.
  * **Service abstractions** : use Kubernetes service types (NodePort, LoadBalancer, Ingress) as preferred alternatives to hostPort.
  * **Security scrutiny** : if hostPort is unavoidable, carefully review and implement firewall rules to restrict access to the exposed ports.
  * **Autopilot considerations** : when you use GKE Autopilot, be aware that you are unable to specify exact hostPorts.



### List of reserved hostPorts

Component | Reserved Host Ports  
---|---  
CNI / DPv2 | 9990, 6942, 9890, 4244, 9965  
kubelet | 4194, 10248, 10250, 10255  
kube-proxy | 10249, 10256  
node-problem-detector | 20256  
fluentbit | 2020, 2021, 2022  
stackdriver-metadata-agent | 8799  
sunrpc (local NFS mounts) | 665 - 986  
Filestore | 990  
k8s-metadata-proxy / gke-metadata-server | 987, 988, 989  
node-local-dns | 53, 8080, 9253, 9353  
gcfsd | 11253  
Network policy Antrea | 10349, 10350, 10351, 10352  
network-metering-agent | 47082, 47083  
configconnector | 8888, 48797  
gke-spiffe | 9889  
workload-identity-webhook | 9910  
GKE Metrics Agent | 8200 - 8227  
node-gboc | 8228 - 8231  
GPU Device plugin | 2112  
runsc (gVisor / GKE Sandbox) | 9115  
containerd | 1338  
GKE Metrics Collector | 11123  
netd | 10231  
Cloud Storage FUSE CSI driver | 9920, 9921  
Compute Engine Persistent Disk CSI driver | 9930, 9931  
  
### List of reserved hostPorts that are specific to Autopilot

Component | Reserved HostPorts  
---|---  
Autopilot Splunk Agent | 8006, 14250, 14268, 4317, 9080, 9943, 9411  
Autopilot Datadog Monitoring Agent | 8125, 8126  
  
## What's next

  * Read an overview of [networking in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).
  * Learn about [Kubernetes Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/service).
  * Learn about [exposing applications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/exposing-apps).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
