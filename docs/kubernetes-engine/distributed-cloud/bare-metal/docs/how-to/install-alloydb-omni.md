---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/install-alloydb-omni/
title: Install AlloyDB Omni \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:54.240204+00:00
---

# Install AlloyDB Omni  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/install-alloydb-omni/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Install AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Install and run AlloyDB Omni on Google Distributed Cloud (software only) for bare metal clusters.

## Overview

Google Distributed Cloud for bare metal completed [partner qualification](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/anthos-ready-partners) for AlloyDB Omni (starting with AlloyDB Omni Operator version 1.7.0).

AlloyDB Omni is a downloadable database software package that:

  * Lets you deploy a streamlined version of [AlloyDB for PostgreSQL](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes).
  * Offers full PostgreSQL compatibility.
  * Provides high throughput on transactional workload.
  * Offers columnar engine acceleration for analytical workloads.
  * Offers built-in support for generative AI and vector search workloads with AlloyDB AI.



Deploy and manage AlloyDB Omni on your bare metal clusters using the AlloyDB Omni Kubernetes Operator.

## Before you begin

Before you install AlloyDB Omni, you must have the following:

  * A Google Distributed Cloud bare metal cluster running Kubernetes version 1.21 or later.
  * The `kubectl` command-line tool configured to communicate with your cluster.
  * [The `helm` package manager](https://helm.sh/docs/intro/install/) (version 3 or later) installed on your admin workstation.
  * A default StorageClass configured on your bare metal cluster for dynamic volume provisioning. For more information, see [Storage overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/storage).
  * Nodes in your cluster that meet the minimum resource requirements for AlloyDB Omni: 
    * At least 2 CPUs per database instance.
    * At least 8 GB of RAM per CPU (for example, 16 GB for 2 CPUs).
    * Linux kernel 4.18 or later with control group (cgroup) v2 enabled.



## Install cert-manager

The AlloyDB Omni Operator requires `cert-manager` to manage TLS certificates for its admission webhooks.

  1. If `cert-manager` isn't already installed on your cluster, install it using Helm: `sh helm repo add jetstack https://charts.jetstack.io helm repo update helm install cert-manager jetstack/cert-manager \ --namespace cert-manager \ --create-namespace \ --version v1.16.0 \ --set crds.enabled=true \ --kubeconfig KUBECONFIG`

  2. Replace `KUBECONFIG` with the path of your cluster kubeconfig file.

  3. Verify that the `cert-manager` Pods are running: `sh kubectl get pods -n cert-manager --kubeconfig KUBECONFIG`

## Install the AlloyDB Omni Operator




To install the AlloyDB Omni Kubernetes Operator from the OCI registry using [Helm](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/deploy-kubernetes#helm), do the following:

  1. Install the operator Helm chart:
         
         helm install alloydbomni-operator oci://gcr.io/alloydb-omni/alloydbomni-operator \
             --version OPERATOR_VERSION \
             --create-namespace \
             --namespace alloydb-omni-system \
             $(helm install --help | grep -q -- '--rollback-on-failure' && echo '--rollback-on-failure' || echo '--atomic') \
             --timeout 5m \
             --kubeconfig KUBECONFIG
         

Replace the following:

     * `OPERATOR_VERSION`: the version of the AlloyDB Omni Operator to install (for example, `1.8.0` or later).
     * `KUBECONFIG`: the path of your cluster kubeconfig file.
  2. Verify that the operator Pod is running:
         
         kubectl get pods -n alloydb-omni-system --kubeconfig KUBECONFIG
         

The output is similar to the following:
         
         NAME                                        READY   STATUS    RESTARTS   AGE
         fleet-controller-manager-796c698cd7-x2vsr   1/1     Running   0          22h
         local-controller-manager-76f6c98446-rzpsc   1/1     Running   0          22h
         




## Create an AlloyDB Omni cluster

After the operator runs, create an AlloyDB Omni database cluster by creating a password Secret and applying a `DBCluster` custom resource.

**Important:** Don't create database clusters in the `alloydb-omni-system` namespace. Use a separate application namespace for your database resources. 

  1. Create a namespace for your database workloads:
         
         kubectl create namespace my-db-ns --kubeconfig KUBECONFIG
         

  2. Create a Kubernetes Secret containing the database administrator login password for the default `postgres` user:
         
         kubectl create secret generic db-pw-my-db-cluster \
             --namespace my-db-ns \
             --from-literal=my-db-cluster=PASSWORD \
             --kubeconfig KUBECONFIG
         

Replace `PASSWORD` with a secure password.

  3. Create a manifest named `db-cluster.yaml`:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: DBCluster
         metadata:
           name: my-db-cluster
           namespace: my-db-ns
         spec:
           databaseVersion: "18.3.0"
           primarySpec:
             adminUser:
               passwordRef:
                 name: db-pw-my-db-cluster
             resources:
               cpu: 2
               memory: 16Gi
               disks:
               - name: DataDisk
                 size: 20Gi
         

  4. Apply the manifest:
         
         kubectl apply -f db-cluster.yaml --kubeconfig KUBECONFIG
         

  5. Verify that the database cluster reaches the `Ready` state:
         
         kubectl get dbclusters -n my-db-ns --kubeconfig KUBECONFIG
         

The output is similar to the following:
         
         NAME            PRIMARY             PRIMARYSTATUS   STANDBY   STANDBYSTATUS   STATUS
         my-db-cluster   my-db-cluster-0     Ready                                     Ready
         




## What's next

  * Learn more about [AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/deploy-kubernetes).
  * Learn how to [run and connect](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/run-connect) to AlloyDB Omni.
  * Learn how to configure [High availability for Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/kubernetes-ha).
  * Learn how to [Serve third-party LLMs on bare metal](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/serve-3p-llms) and integrate with vector databases.
  * Learn how to [Run AlloyDB Omni in production](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/run-alloydb-omni-production)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
