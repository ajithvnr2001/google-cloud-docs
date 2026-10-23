---
url: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/arm-workloads/
title: Troubleshooting Arm workloads \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:54.396485+00:00
---

# Troubleshooting Arm workloads  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/arm-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Troubleshooting Arm workloads Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page shows you how to resolve issues with Arm workloads deployed on your Google Kubernetes Engine (GKE) Autopilot or Standard clusters.

## Pods on Arm nodes crashing

The following issue occurs when you deploy a Pod on an Arm node, but the container image isn't built for Arm architecture.

To identify the issue, do the following:

  1. Get the status of your Pods:
         
         kubectl get pods
         

  2. Get the logs for a crashing Pod:
         
         kubectl logs POD_NAME
         

Replace `POD_NAME` with the name of the crashing Pod.

The error message in your Pod logs is similar to the following:
         
         exec ./hello-app: exec format error
         




To resolve this issue, ensure that your container image supports Arm architecture. As a best practice, [build multiple architecture images](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/build-multi-arch-for-arm).

## Pod doesn't trigger scale-up

**Applies to:** Autopilot

The following issue occurs in Autopilot clusters when you attempt to deploy Arm workloads on unsupported GKE versions or unsupported Google Cloud regions.

To identify the issue, get your cluster event log:
    
    
    kubectl get events -w
    

The output is similar to the following:
    
    
    117s        Normal    NotTriggerScaleUp   pod/hello-app2-78fc858558-pg4hz   pod didn't trigger scale-up (it wouldn't fit if a new node is added): 2 node(s) didn't match Pod's node affinity/selector
    

To resolve this issue, ensure that your Autopilot cluster is running GKE version 1.24.1-gke.1400 or later, and that the Google Cloud region supports Arm nodes.

## Pods stuck in Pending state

**Applies to:** Autopilot

The following issue occurs when you attempt to deploy Autopilot Pods on Arm architecture but your Google Cloud project is out of quota.

To identify the issue, get the event log for your cluster:
    
    
    kubectl get events -w
    

The output is similar to the following:
    
    
    29m         Warning   FailedScaleUp       pod/hello-app-7b86c88cb8-8vt2k   Node scale up in zones asia-southeast1-b associated with this pod failed: GCE quota exceeded. Pod is at risk of not being scheduled.
    

This event might not appear in your log as soon as you deploy your Pods.

To help resolve this issue, [request a quota adjustment](https://docs.cloud.google.com/docs/quotas/help/request_increase).

## What's next

  * If you can't find a solution to your problem in the documentation, see [Get support](https://docs.cloud.google.com/kubernetes-engine/docs/getting-support) for further help, including advice on the following topics:

    * Opening a support case by contacting [Cloud Customer Care](https://cloud.google.com/support-hub).
    * Getting support from the community by [asking questions on StackOverflow](http://stackoverflow.com/questions/tagged/google-kubernetes-engine) and using the `google-kubernetes-engine` tag to search for similar issues. You can also join the [`#kubernetes-engine` Slack channel](https://googlecloud-community.slack.com/messages/C0B9GKTKJ/) for more community support.
    * Opening issues or feature requests by using the [public issue tracker](https://docs.cloud.google.com/support/docs/issue-trackers).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
