---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/deploy-kubernetes/
title: Install AlloyDB Omni on Kubernetes \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.5.4 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:20:29.999655+00:00
---

# Install AlloyDB Omni on Kubernetes  |  AlloyDB Omni for Kubernetes: 15.5.4  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/deploy-kubernetes/

This page documents AlloyDB Omni version **15.5.4** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/overview)



Send feedback 

#  Install AlloyDB Omni on Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.4keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/deploy-kubernetes)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/deploy-kubernetes)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/deploy-kubernetes)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/deploy-kubernetes)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/deploy-kubernetes)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/deploy-kubernetes)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/deploy-kubernetes)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/deploy-kubernetes)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/deploy-kubernetes)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/deploy-kubernetes)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/deploy-kubernetes)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/deploy-kubernetes)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/deploy-kubernetes)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/deploy-kubernetes)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/deploy-kubernetes)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/deploy-kubernetes)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/deploy-kubernetes)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/deploy-kubernetes)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/deploy-kubernetes)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/deploy-kubernetes)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/deploy-kubernetes)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/deploy-kubernetes)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/deploy-kubernetes)

**Note:** Your use of AlloyDB Omni is subject to the agreement between you and Google that governs Google Cloud offerings. If you do not have a Google Cloud account, or have not otherwise entered into an agreement with Google that governs Google Cloud offerings, please do not proceed or download this software until you have done so. To create a Google Cloud account, see [ the Google Cloud homepage](https://docs.cloud.google.com/docs/get-started). 

This page provides an overview of the AlloyDB Omni Kubernetes Operator, with instructions for using it to deploy AlloyDB Omni onto a Kubernetes cluster. This page assumes basic familiarity with Kubernetes operation.

For instructions on installing AlloyDB Omni onto a standard Linux environment, see [Install AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/install).

## Overview

To deploy AlloyDB Omni onto a Kubernetes cluster, install the AlloyDB Omni Operator, an extension to the Kubernetes API provided by Google.

You configure and control a Kubernetes-based AlloyDB Omni database cluster by pairing declarative manifest files with the `kubectl` utility, just like any other Kubernetes-based deployment.

## Before you begin

You need access to the following:

  * A Kubernetes cluster, running the following software:

    * Kubernetes version 1.21 or later.
    * [The `cert-manager` service](https://cert-manager.io/docs/installation/helm/#installing-from-the-oci-registry), installed using Helm.
**Note:** For GKE Autopilot clusters, install `cert-manager` with this flag: `--set global.leaderElection.namespace=cert-manager`
  * [The `kubectl` utility](https://kubernetes.io/docs/tasks/tools/#kubectl).

  * [The `helm` package manager](https://helm.sh/docs/intro/install/).

  * The [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install).

If you do need to install the gcloud CLI, note that the step of running `gcloud init` is optional. Installing AlloyDB Omni does not require authentication with a Google Account.




Each node in the Kubernetes cluster must have the following:

  * A minimum of two x86 or AMD64 CPUs.
  * At least 8GB of RAM.
  * Linux kernel version 4.18 or later.
  * Control group v2 (cgroup v2) enabled.



## Install the AlloyDB Omni Operator

To install the AlloyDB Omni Operator, follow these steps:

  1. Define several environment variables:
         
         export GCS_BUCKET=alloydb-omni-operator
         export HELM_PATH=$(gcloud storage cat gs://$GCS_BUCKET/latest)
         export OPERATOR_VERSION="${HELM_PATH%%/*}"

  2. Download the AlloyDB Omni Operator:
         
         gcloud storage cp -r gs://$GCS_BUCKET/$HELM_PATH ./

  3. Install the AlloyDB Omni Operator:
         
         helm install alloydbomni-operator alloydbomni-operator-${OPERATOR_VERSION}.tgz \
         --create-namespace \
         --namespace alloydb-omni-system \
         $(helm install --help | grep -q -- '--rollback-on-failure' && echo '--rollback-on-failure' || echo '--atomic') \
         --timeout 5m

Successful installation displays the following output:
         
         NAME: alloydbomni-operator
         LAST DEPLOYED: CURRENT_TIMESTAMP
         NAMESPACE: alloydb-omni-system
         STATUS: deployed
         REVISION: 1
         TEST SUITE: None
         

  4. Clean up by deleting the downloaded AlloyDB Omni Operator installation file. The file is named `alloydbomni-operator-VERSION_NUMBER.tgz`, and is located in your current working directory.




## Create a database cluster

An AlloyDB Omni _database cluster_ contains all the storage and compute resources needed to run an AlloyDB Omni server, including the primary server, any replicas, and all of your data.

**Important:** Don't create a database cluster in the `alloydb-omni-system` namespace. The `alloydb-omni-system` namespace is reserved for the AlloyDB Omni Operator. 

After you install the AlloyDB Omni Operator on your Kubernetes cluster, you can create an AlloyDB Omni database cluster on the Kubernetes cluster by applying a manifest similar to the following:
    
    
    apiVersion: v1
    kind: Secret
    metadata:
      name: db-pw-DB_CLUSTER_NAME
    type: Opaque
    data:
      DB_CLUSTER_NAME: "ENCODED_PASSWORD"
    ---
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: DB_CLUSTER_NAME
    spec:
      databaseVersion: "15.5.4"
      primarySpec:
        adminUser:
          passwordRef:
            name: db-pw-DB_CLUSTER_NAME
        resources:
          cpu: CPU_COUNT
          memory: MEMORY_SIZE
          disks:
          - name: DataDisk
            size: DISK_SIZE
            storageClass: standard
    

Replace the following:

  * `DB_CLUSTER_NAME`: the name of this database cluster—for example, `my-db-cluster`.

  * `ENCODED_PASSWORD`: the database login password for the default `postgres` user role, encoded as a base64 string—for example, `Q2hhbmdlTWUxMjM=` for `ChangeMe123`.

  * `CPU_COUNT`: the number of CPUs available to each database instance in this database cluster.

  * `MEMORY_SIZE`: the amount of memory per database instance of this database cluster. We recommend setting this to 8 gigabytes per CPU. For example, if you set `cpu` to `2` earlier in this manifest, then we recommend setting `memory` to `16Gi`.

  * `DISK_SIZE`: the disk size per database instance—for example, `10Gi`.




After you apply this manifest, your Kubernetes cluster contains an AlloyDB Omni database cluster with the specified memory, CPU, and storage configuration. To establish a test connection with the new database cluster, see [Connect using the preinstalled `psql`](https://docs.cloud.google.com/alloydb/omni/15.5.4/docs/run-connect#psql-kubernetes).

For more information about Kubernetes manifests and how to apply them, see [Managing resources](https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/).

## What's next

  * [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/run-connect)
  * [Manage AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/manage)
  * [Manage high availability in Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/kubernetes-ha)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
