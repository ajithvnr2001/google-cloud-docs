---
url: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/data-protection-recommendations/
title: Protect clusters with Backup for GKE \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:40.855189+00:00
---

# Protect clusters with Backup for GKE  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/data-protection-recommendations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke)



Send feedback 

#  Protect clusters with Backup for GKE Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

You can use Google Kubernetes Engine (GKE) clusters to run mission-critical workloads, which must be resilient to many types of disruptions, including infrastructure failures, user errors, and cyber attacks.

With [Backup for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/concepts/backup-for-gke), you can:

  * Back up configurations and persistent volume data to make workloads resilient to disruption.
  * Restore workloads from backups if disruptions occur.
  * Achieve business-critical Recovery Point Objectives (RPO) and Recovery Time Objectives (RTO).
  * Streamline day-to-day operations by cloning production configuration and data for use cases such as sandbox testing, and the creation of test and development environments.



GKE monitors your clusters and uses the [Recommender service](https://docs.cloud.google.com/recommender/docs/overview) to provide guidance for how you can optimize your usage of the platform. GKE detects opportunities to make workloads more resilient to disruptions by enabling Backup for GKE.

To learn more about how to manage insights and recommendations from Recommender, see [Optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders).

## Identify clusters unprotected by Backup for GKE

GKE generates insights that identify clusters within your organization that aren't protected by backups. To get these insights, follow the instructions to [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs) using the Google Cloud console, the Google Cloud CLI, or the Recommender API with the `CLUSTER_BACKUP_PLAN_NOT_CREATED` subtype.

## How GKE identifies clusters without a backup plan

GKE uses the following criteria to determine that you should create a backup plan to protect your cluster:

  * The cluster is not ephemeral, meaning that the GKE cluster meets all of the following criteria:

    * The cluster has existed for at least seven days.
    * The cluster is in one of the following zones or regions:

      * **Zone** : `us-central1-a`, `us-central1-b`, `us-central1-c`, `us-central1-f`, `us-east1-b`, `us-east1-c`, or `us-east1-d`
      * **Region** : `us-east1`
    * The cluster is running.

    * The cluster is not an [alpha cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters).

  * The cluster has no associated Backup for GKE backup plan.




## Assess if your cluster needs data protection with Backup for GKE

Consider the following criteria to assess whether you should back up your cluster with Backup for GKE:

  * **Running stateful applications** : Stateful applications retain state, which is vulnerable to loss and corruption. Backups provide the best defense against disruptions due to zonal, regional, workload, or user-induced failures.
  * **Quick application rollback is important** : Recover both stateful and stateless applications to a known healthy state in the event of faults, failed upgrades, or corruption. A recovery from backups can often lead to quicker recovery times compared to redeploying your application. With backups, you can store multiple points in time for greater flexibility.
  * **Need protection from cyber attack** : Prepare for the impact of cyber attack threats by creating immutable and encrypted backups, and locking those backups against deletion for a minimum amount of time.



Both stateful and stateless workloads can benefit from backups. Consider configuring backups if one or more of this criteria applies to your cluster.

## Act on the recommendation

If you've determined that you should enable Backup for GKE and create a backup plan for your cluster, follow these instructions:

  1. [Enable Backup for GKE API](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/install).
  2. [Enable Backup for GKE for a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/enable-gke-cluster).
  3. [Create a backup plan](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/backup-plan#console).



## What's next

  * [Optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders)
  * [Restore a backup](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/how-to/restore)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
