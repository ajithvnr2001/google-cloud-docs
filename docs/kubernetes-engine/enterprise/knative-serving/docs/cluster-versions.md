---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/cluster-versions/
title: Available GKE cluster versions \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:08:49.313449+00:00
---

# Available GKE cluster versions  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/cluster-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/apis)



Send feedback 

#  Available GKE cluster versions Stay organized with collections  Save and categorize content based on your preferences. 

The [minor version](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades#versioning) of your GKE cluster control plane (master) determines the version of Knative serving installed on your cluster.

You can monitor the [release notes](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/release-notes) for announcements about Knative serving and cluster version support.

The following table lists the Knative serving version that each GKE minor version supports.

## Determining the version of an existing cluster

To get the Knative serving version of an existing cluster, enter the following command:
    
    
    kubectl get namespace knative-serving -o 'go-template={{index .metadata.labels "serving.knative.dev/release"}}'
    

The output is similar to:
    
    
    v0.0.24-gke.0
    

Where `0.24`, is the [pinned Knative version](https://github.com/knative/serving/releases) for this Knative serving build.

## Knative serving versions

### 0.23

  * References the Knative [0.23](https://github.com/knative/serving/releases/tag/v0.23.0) release.



### 0.22

  * References the Knative [0.22](https://github.com/knative/serving/releases/tag/v0.22.0) release.



## Knative serving version release process

Each Knative serving release references a [Knative release](https://github.com/knative/serving/releases). A Knative serving release is available in the Rapid [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#channels) one to three weeks after a version of Knative is released.

The following table describes the available Google Kubernetes Engine release channels and the Knative serving strategies for releasing to those channels.

Channel  | Knative serving Release Cadence | Properties   
---|---|---  
Rapid  | Weekly  | Get the latest Knative serving release as early as possible. Gain access to new Knative serving features as soon as they go GA. Your cluster is frequently updated to use the latest technology.  
Regular (default)  | 1-2 weeks after releasing in Rapid  | Recommended for most users. Access Knative serving features reasonably soon after they debut, but on a more steady and predictable release cadence. Offers a good balance of feature availability and update stability. Your cluster is upgraded 2‑3 times a month.  
Stable  | 1-2 months after releasing in Regular.  | Prioritizes stability over new functionality. Changes and new versions in this channel are rolled out last, after being released on the Rapid and Regular channels. This channel allows more time for validation. Your cluster is upgraded 2‑3 times a quarter.  
  
### Knative serving cluster upgrade process

Your GKE clusters are automatically upgraded two to three days after a new version of GKE becomes available in your cluster's release channel, unless you have configured a [maintenance window or exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions). Subscribe to the [Knative serving release notes](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/release-notes) and [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) for announcements.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
