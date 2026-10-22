---
url: https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/deploy-kubernetes/
title: Install AlloyDB Omni on Kubernetes \u00a0|\u00a0 AlloyDB Omni for containers: 16.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:16.780161+00:00
---

# Install AlloyDB Omni on Kubernetes  |  AlloyDB Omni for containers: 16.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/deploy-kubernetes/

This page documents AlloyDB Omni version **16.3.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/overview)



Send feedback 

#  Install AlloyDB Omni on Kubernetes Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.3.0keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/deploy-kubernetes)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/deploy-kubernetes)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/deploy-kubernetes)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/deploy-kubernetes)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/deploy-kubernetes)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/deploy-kubernetes)

This page provides an overview of the AlloyDB Omni Kubernetes operator, with instructions for using it to deploy AlloyDB Omni onto a Kubernetes cluster. This page assumes basic familiarity with Kubernetes operation. 

For instructions on installing AlloyDB Omni onto a standard Linux environment, see [Install AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/deploy-kubernetes).

## Overview

To deploy AlloyDB Omni onto a Kubernetes cluster, install the AlloyDB Omni operator, an extension to the Kubernetes API provided by Google.

You configure and control a Kubernetes-based AlloyDB Omni database cluster by pairing declarative manifest files with the `kubectl` utility, just like any other Kubernetes-based deployment. You don't use the AlloyDB Omni CLI, which is intended for deployments onto individual Linux machines and not Kubernetes clusters.

### Base image

Starting with version 1.5.0, AlloyDB Omni operator Kubernetes images are built upon Red Hat's Universal Base Image (UBI) 9. This transition enhances security, consistency, and compliance for your deployments.

## AlloyDB Omni operator 1.1.0 (and later) compatibility

[The AlloyDB Omni operator version 1.1.0 is not compatible](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/choose-compatible-versions) with versions 15.5.3 and 15.5.4 of AlloyDB Omni. If you use one of these versions of AlloyDB Omni, you might receive an error similar to the following:
    
    
    Error from server (Forbidden): error when creating "[...]/dbcluster.yaml": admission webhook "vdbcluster.alloydbomni.dbadmin.goog" denied the request: unsupported database version 15.5.3
    

**Note:** To deploy AlloyDB Omni on a Kubernetes cluster with AlloyDB Omni operator 1.1.0, use AlloyDB Omni version 15.5.5 or later.

## Before you begin

Before you install AlloyDB Omni on a Kubernetes cluster with AlloyDB Omni operator, make sure that you meet the following requirements.

### Choose a download or installation option

When you manage workloads on a generic Kubernetes cluster, you can use either Helm or OLM. Helm is a universal package manager that uses Helm charts to install any workload, including operators, across all Kubernetes variants. OLM—the standard, preferred choice on OpenShift platforms— manages operator lifecycles with specialized OLM bundles.

Based on your environment and tooling, choose one of the following deployment methods:

**Media** | **Download locations and installation guides** | **Deployment to**  
---|---|---  
**AlloyDB Omni operator with Helm Chart** | [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/deploy-kubernetes#install) | Bring-your-own Kubernetes container environment—for example, on-premises, public clouds, GKE, Amazon EKS, and Azure AKS.  
  
**Tip:** If your CD (continuous delivery) tooling is integrated with Helm, use this option.  
**AlloyDB Omni operator with OLM bundle** | [OperatorHub.io](https://operatorhub.io/operator/alloydb-omni-operator) | Bring-your-own Kubernetes container environment—for example, on-premises, public clouds, Google Kubernetes Engine, Amazon EKS, and Azure AKS.  
  
To use an OLM bundle, install OLM on the Kubernetes cluster before you install the operator. For more information, see [olm.operatorframework.io](https://olm.operatorframework.io/).  
  
**Tip:** If your CD (continuous delivery) tooling already uses OLM, choose this option.  
**OpenShift Operator with OLM Bundle** | [Openshift Container Platform Web Console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/web_console/web-console) | OpenShift environment  
  
OpenShift, a variant of Kubernetes, uses OLM as its standard, built-in method for packaging and deploying operators.  
  
### Verify access

Verify that you have access to the following:

  * A Kubernetes cluster, running the following software:

    * Kubernetes version 1.21 or later.
    * [The `cert-manager` service](https://cert-manager.io/docs/installation/helm/#installing-from-the-oci-registry), installed using Helm.
**Note:** For GKE Autopilot clusters, install `cert-manager` with this flag: `--set global.leaderElection.namespace=cert-manager`
  * [The `kubectl` utility](https://kubernetes.io/docs/tasks/tools/#kubectl).

  * [The `helm` package manager](https://helm.sh/docs/intro/install/) or [the Operator Lifecycle Manager](https://olm.operatorframework.io/docs/getting-started/).




### Fulfill hardware and software requirements

Each node in the Kubernetes cluster must have the following:

  * A minimum of two x86 or AMD64 CPUs.
  * At least 8GB of RAM.
  * Linux kernel version 4.18 or later.
  * Control group (cgroup) v2 enabled.



## Install the AlloyDB Omni operator

**Note:** If you want to deploy AlloyDB Omni in your production environment, see [Run AlloyDB Omni in production](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/run-alloydb-omni-production).

You can install the AlloyDB Omni operator using different methods, including Helm and the Operator Lifecycle Manager (OLM).

### Helm

To install the AlloyDB Omni operator, follow these steps:

  1. Define the following environment variables: 
         
         export HELM_PATH=$(curl https://storage.googleapis.com/alloydb-omni-operator/latest)
         export OPERATOR_VERSION="${HELM_PATH%%/*}"
         

  2. Download the AlloyDB Omni operator: 
         
         curl -X GET -o "./alloydbomni-operator-${OPERATOR_VERSION}.tgz" "https://storage.googleapis.com/storage/v1/b/alloydb-omni-operator/o/$(echo ${HELM_PATH} | sed 's/\//%2F/g')?alt=media"
         

  3. Install the AlloyDB Omni operator: 
         
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
         

  4. To clean up, delete the downloaded AlloyDB Omni operator installation file. The file is named `alloydbomni-operator-VERSION_NUMBER.tgz`, and is located in your current working directory.



### OLM

To install the AlloyDB Omni operator using the Operator Lifecycle Manager, follow these steps:

  1. Go to the [**AlloyDB Omni Operator**](https://operatorhub.io/operator/alloydb-omni-operator) page.

  2. Click **Install**. If you haven't done so already, follow the instructions to install only the OLM operator and OperatorHub.io catalog.

  3. Create the `alloydb-omni-system` namespace if it does not already exist.
         
         kubectl create ns alloydb-omni-system
         

  4. Set up the OLM `OperatorGroup` to make sure that the operator is cluster-scoped.
         
         kubectl apply -f - <<EOF
         apiVersion: operators.coreos.com/v1
         kind: OperatorGroup
         metadata:
           name: operator-sdk-og
           namespace: alloydb-omni-system
         spec:
           upgradeStrategy: Default
         EOF
         

  5. Install the operator using an OLM Subscription resource.
         
         kubectl apply -f - <<EOF
         apiVersion: operators.coreos.com/v1alpha1
         kind: Subscription
         metadata:
           name: my-alloydb-omni-operator
           namespace: alloydb-omni-system
         spec:
           channel: stable
           name: alloydb-omni-operator
           source: operatorhubio-catalog
           sourceNamespace: olm
         EOF
         

  6. Install the default certificate `ClusterIssuer`. This step is optional if you use [custom certificate issuers](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/manage-certificates-kubernetes-operator).
         
         kubectl apply -f - <<EOF
         apiVersion: cert-manager.io/v1
         kind: ClusterIssuer
         metadata:
           name: alloydbomni-selfsigned-cluster-issuer
         spec:
           selfSigned: {}
         EOF
         




### OLM

**Note:** You must enable the `community-operators` CatalogSource because the AlloyDB Omni operator is available solely as a community operator. Red Hat documentation indicates that you can [disable the community catalog](https://access.redhat.com/solutions/5611481) if needed. 

To install the AlloyDB Omni operator on your Red Hat OpenShift environment using the OLM, [sign in to your Red Hat OpenShift web console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/web_console/web-console).

  1. Select **Operators** > **OperatorHub**.

  2. Find AlloyDB Omni operator using the search field.

  3. In the AlloyDB Omni operator pane, click **Install**.

  4. Install the default certificate `ClusterIssuer`. This step is optional if you use [custom certificate issuers](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/manage-certificates-kubernetes-operator).
         
         kubectl apply -f - <<EOF
         apiVersion: cert-manager.io/v1
         kind: ClusterIssuer
         metadata:
           name: alloydbomni-selfsigned-cluster-issuer
         spec:
           selfSigned: {}
         EOF
         




## Configure GDC connected storage

To install the AlloyDB Omni operator on [GDC connected](https://docs.cloud.google.com/distributed-cloud/edge/latest/docs/overview), you need to follow additional steps to configure storage because GDC connected clusters don't set a default storage class. You must set a default storage class before you create an AlloyDB Omni database cluster.

To learn how to set Symcloud Storage as the default storage class, see [Set Symcloud Storage as the default storage class](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/storage#set_symcloud_storage_as_the_default_storage_class).

For more information about changing the default for all other storage classes, see [Change the default StorageClass](https://kubernetes.io/docs/tasks/administer-cluster/change-default-storage-class/).

## Create a database cluster

**Important:** Don't create a database cluster in the `alloydb-omni-system` namespace. The `alloydb-omni-system` namespace is reserved for the AlloyDB Omni operator. 

An AlloyDB Omni _database cluster_ contains all the storage and compute resources needed to run an AlloyDB Omni server, including the primary server, any replicas, and all of your data.

To create an AlloyDB Omni database cluster, follow these steps:

  1. Create a dedicated namespace for your database cluster. This improves isolation and security.
         
         kubectl create namespace DB_CLUSTER_NAMESPACE
         

Replace `DB_CLUSTER_NAMESPACE` with the namespace where you want to create the database cluster—for example, `my-db-cluster-namespace`.

  2. Create a manifest file named `db-cluster.yaml` with the following content. This manifest defines both the secret for the database password and the DBCluster resource itself.
         
         apiVersion: v1
         kind: Secret
         metadata:
           name: db-pw-DB_CLUSTER_NAME
           namespace: DB_CLUSTER_NAMESPACE
         type: Opaque
         data:
           DB_CLUSTER_NAME: "ENCODED_PASSWORD"
         ---
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: DBCluster
         metadata:
           name: DB_CLUSTER_NAME
           namespace: DB_CLUSTER_NAMESPACE
         spec:
           databaseVersion: "16.3.0"
           # Optional: Specify the base OS type for the database image.
           # Valid values are "Debian" and "UBI9".
           # If not specified, the operator defaults to "Debian" for databaseVersion < 16.9.0
           # and "UBI9" for databaseVersion 16.9.0 or later.
           # databaseImageOSType: "OS_TYPE"
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
         

Replace the following:

     * `DB_CLUSTER_NAME`: the name of this database cluster—for example, `my-db-cluster`.

     * `OS_TYPE`: Optional. The base operating system type for the database image. Valid values are `Debian` and `UBI9`. If you don't specify this, the operator automatically sets it to `Debian` if `databaseVersion` is less than `16.9.0`, and to `UBI9` if `databaseVersion` is `16.9.0` or later.

     * `ENCODED_PASSWORD`: the database login password for the default `postgres` user role, encoded as a base64 string—for example, `Q2hhbmdlTWUxMjM=` for `ChangeMe123`.

     * `CPU_COUNT`: the number of CPUs available to each database instance in this database cluster.

     * `MEMORY_SIZE`: the amount of memory per database instance of this database cluster. We recommend setting this to 8 gigabytes per CPU. For example, if you set `cpu` to `2` earlier in this manifest, then we recommend setting `memory` to `16Gi`.

     * `DISK_SIZE`: the disk size per database instance—for example, `10Gi`.

  3. Apply the manifest to your Kubernetes cluster:
         
         kubectl apply -f db-cluster.yaml
         




After you apply this manifest, your Kubernetes cluster contains an AlloyDB Omni database cluster with the specified memory, CPU, and storage configuration. To establish a test connection with the new database cluster, see [Connect using the preinstalled `psql`](https://docs.cloud.google.com/alloydb/omni/15.12.0/docs/run-connect#psql-kubernetes).

**Note:** Starting with version 1.1.0 of AlloyDB Omni operator, the admin password secret is no longer deleted after you set it. You must keep the newly set secret for the lifespan of your AlloyDB Omni database cluster.

For more information about Kubernetes manifests and how to apply them, see [Managing resources](https://kubernetes.io/docs/concepts/cluster-administration/manage-deployment/).

## What's next

  * [Run and connect to AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/run-connect)
  * [Manage AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/manage)
  * [Manage high availability in Kubernetes](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/kubernetes-ha)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
