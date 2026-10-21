---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/kubernetes-dr-backup-overview/
title: Clone a database cluster from a Kubernetes backup overview \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.13.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:57:00.448849+00:00
---

# Clone a database cluster from a Kubernetes backup overview  |  AlloyDB Omni for Kubernetes: 15.13.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/kubernetes-dr-backup-overview/

This page documents AlloyDB Omni version **15.13.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/overview)



Send feedback 

#  Clone a database cluster from a Kubernetes backup overview Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.13.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/kubernetes-dr-backup-overview)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/kubernetes-dr-backup-overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/kubernetes-dr-backup-overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/kubernetes-dr-backup-overview)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/kubernetes-dr-backup-overview)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/kubernetes-dr-backup-overview)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/kubernetes-dr-backup-overview)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/kubernetes-dr-backup-overview)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/kubernetes-dr-backup-overview)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/kubernetes-dr-backup-overview)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/kubernetes-dr-backup-overview)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/kubernetes-dr-backup-overview)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/kubernetes-dr-backup-overview)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/kubernetes-dr-backup-overview)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/kubernetes-dr-backup-overview)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/kubernetes-dr-backup-overview)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/kubernetes-dr-backup-overview)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/kubernetes-dr-backup-overview)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/kubernetes-dr-backup-overview)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/kubernetes-dr-backup-overview)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/kubernetes-dr-backup-overview)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/kubernetes-dr-backup-overview)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/kubernetes-dr-backup-overview)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/kubernetes-dr-backup-overview)

To support disaster recovery, you can manually clone the backup of your AlloyDB Omni database cluster in a standalone server environment or in a Kubernetes environment. 

When you manually clone your database cluster, only the data from the primary instance of the source database cluster is cloned to the primary instance of the target database cluster or server.

A _source database cluster_ is an AlloyDB Omni database cluster where the backup exists. This backup is cloned on other database clusters in a standalone server environment or in a Kubernetes environment. A _target database cluster_ is a database cluster in the Kubernetes environment where the backup of the source database cluster is cloned. A _target server_ is a database cluster in the standalone server environment where the backup of the source database cluster is cloned.

To take a backup of your AlloyDB Omni database cluster, you configure the backup location in the [`BackupPlan`](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/backup-kubernetes) resource manifest file. When you want to clone the backup, you can only clone it to a database cluster that is in the same Kubernetes cluster and uses the same namespace as the source database cluster. For more information about creating a backup, see [Back up and restore in Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/backup-kubernetes).

If you want to clone the backup to another database cluster in a standalone server environment or in a different Kubernetes environment especially for disaster recovery, then you must use the `pgBackRest` configurations and commands. The backup and restore method for both environments uses `pgBackRest` as the underlying backup and restore solution.

The following terms are used throughout the subsequent sections that explain how to clone a database cluster:

Source database cluster
    An AlloyDB Omni database cluster where the backup exists. This backup is cloned on other database clusters in a standalone server environment or a Kubernetes environment.
Target database cluster
    A database cluster in the Kubernetes environment where the backup of the source database cluster is cloned.
Target server
    A database cluster in the standalone server environment where the backup of the source database cluster is cloned.

## Supported backup and restore combinations

Because the backup of your AlloyDB Omni database cluster can be stored either locally or in a Cloud Storage bucket, the following backup and restore combinations are supported:

  * [Clone a database cluster in Kubernetes using a Cloud Storage backup](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/kubernetes-dr-backup-k8-gcs)
  * [Clone a database cluster in Kubernetes using a local backup](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/kubernetes-dr-backup-k8-local)
  * [Clone a database cluster in a single server using a Cloud Storage backup](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/kubernetes-dr-backup-singleserver-gcs)
  * [Clone a database cluster in a single server using a local backup](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/kubernetes-dr-backup-singleserver-local)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
