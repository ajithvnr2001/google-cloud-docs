---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-preview/
title: Backup for GKE preview agent deprecation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:23.001528+00:00
---

# Backup for GKE preview agent deprecation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-preview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Resources ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/about-pricing)



Send feedback 

#  Backup for GKE preview agent deprecation Stay organized with collections  Save and categorize content based on your preferences. 

Standard 

**Note:** Starting on April 27th 2023, Backup for GKE will block the agent from being installed in clusters running a version of GKE earlier than 1.24. This change won't impact clusters already running the preview agent, but will block new installations.

The Backup for GKE [agent](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke#agent_overview) requires full privileges to read and write every object in the cluster.

The version of the agent that runs in GKE cluster versions prior to 1.24 is a preview version released in February 2022 that runs as a workload in the GKE user cluster. Users or workloads with root access to the underlying node on which the Backup for GKE Pod is scheduled, such as through Pod hostpath mounts or SSH, can gain these root-in-cluster privileges.

This node-to-cluster escalation vulnerability is addressed in the generally available (GA) version of the agent, which was released in November 2022. The GA agent runs on an inaccessible host in the GKE control plane and is only available in clusters running GKE version 1.24 or later. To avoid the potential for a node-to-cluster escalation, we highly recommend that you run Backup for GKE **only for GKE clusters running version 1.24 or later**.

New installations of the preview agent will be blocked starting on April 27th 2023.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
