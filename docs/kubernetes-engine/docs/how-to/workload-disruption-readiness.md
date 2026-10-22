---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-disruption-readiness/
title: Ensure workloads are disruption-ready \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:05.515151+00:00
---

# Ensure workloads are disruption-ready  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-disruption-readiness/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Ensure workloads are disruption-ready Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Applications running in Google Kubernetes Engine (GKE) clusters must be prepared for disruptions such as node upgrades and other maintenance events. Stateful applications, which often need time to cleanly stop I/O and unmount from storage, are especially vulnerable to disruptions. You can use Kubernetes features such as [Pod Disruption Budgets](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) (PDBs) and [Readiness Probes](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-best-practices-setting-up-health-checks-with-readiness-and-liveness-probes) to help keep applications available during upgrades.

GKE monitors your clusters and uses the [Recommender service](https://docs.cloud.google.com/recommender/docs/overview) to deliver guidance for how you can optimize your usage of the platform. GKE detects opportunities to prepare your workloads for disruption and provides guidance on how to update your PDBs or readiness probes to maximize the resiliency of your workloads to disruption. For example, if a StatefulSet is not protected by a PDB, your cluster might remove all Pods at once during a node upgrade. To avoid this, GKE delivers guidance to create a PDB so that most Pods can stay running during an upgrade.

To see the specific conditions where GKE delivers disruption-related guidance, see When GKE identifies workloads with vulnerability to disruption.

To learn more about how to manage insights and recommendations from Recommenders, see [Optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders).

## Identify workloads with vulnerability to disruption

GKE generates insights identifying your cluster's disruption-vulnerable workloads. To get these insights, follow the instructions to [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs) using the Google Cloud CLI, or the Recommender API. Use the subtypes listed in the following section to filter for specific insights. These insights are not available in the Google Cloud console.

## When GKE identifies workloads with vulnerability to disruption

See the following table for scenarios where GKE delivers an insight and recommendation, and the relevant subtype:

Insight subtype | Description | Action  
---|---|---  
`PDB_UNPROTECTED_STATEFULSET` | Alerts when a StatefulSet exists where no existing PDB labels match the StatefulSet's Pod selector labels. This means that all Pods in the StatefulSet can be taken down during an event such as a node upgrade. | [Add a PDB](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#pod-disruption-budgets) whose labels match the ones in the StatefulSet's Pod selector field. Specify in that PDB how much of a disruption can be tolerated by the StatefulSet. The recommendation associated with this insight suggests what labels a PDB should set to cover the mentioned StatefulSet.  
`PDB_UNPERMISSIVE` | Alerts when a PDB matching a Pod is impossible to adhere to for any maintenance activities, such as a node upgrade. A PDB must allow for at least one Pod to be disrupted, so GKE violates this PDB for necessary maintenance after one hour. | Adjust either the PDB's `minAvailable` setting to be less than the total Pod count, or the `maxUnavailable` setting to be greater than zero.  
`PDB_STATEFULSET_WITHOUT_PROBES` | Alerts when a StatefulSet is configured with a PDB but without readiness probes, so the PDB is not as effective in gauging application readiness. PDBs respect readiness probes when they look at which Pods can be counted as healthy. Therefore, if a Pod covered by a PDB does not have a readiness probe configured, the PDB has limited visibility into whether the Pod is healthy or is just up and running. | Add [readiness probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-readiness-probes) to Pods in StatefulSets for the PDB mentioned in the insight. We also recommend that you add [liveness probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-liveness-command).  
`DEPLOYMENT_MISSING_PDB` |  Alerts when a Deployment exists with a Pod selector that does not match an existing PDB **and** the Deployment has more than one replica **or** horizontal Pod autoscaling enabled. This means that all Pods in the Deployment can be taken down during an event such as a node upgrade.  |  [Add a PDB](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#pod-disruption-budgets) whose labels match the labels in the Deployment's Pod selector field. Specify in that PDB how much disruption can be tolerated by the Deployment. The recommendation associated with this insight suggests what labels a PDB should set to cover the mentioned Deployment.  
  
## Implement the guidance to improve disruption readiness

If you've received insights and recommendations for workloads in your cluster and you want to improve their disruption readiness, implement the instructions described in the recommendation and the action for that insight subtype, as seen in the previous section.

Recommendations are assessed once daily, so it may take up to 24 hours for them to resolve after changes have been implemented.

If you do not want to implement the recommendation, you can [dismiss it](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#dismiss-recommendation).

## What's next

  * To learn more about ensuring reliability and uptime for your GKE cluster, see [GKE Day 2 Operations Best Practices](https://cloud.google.com/blog/products/containers-kubernetes/ensuring-reliability-and-uptime-for-your-gke-cluster).
  * To learn more about possible disruptions to Pods in Kubernetes, see [Disruptions](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
