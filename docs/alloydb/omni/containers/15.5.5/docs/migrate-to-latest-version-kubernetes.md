---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/migrate-to-latest-version-kubernetes/
title: Migrate to the latest version of the AlloyDB Omni Kubernetes Operator \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:23:32.430984+00:00
---

# Migrate to the latest version of the AlloyDB Omni Kubernetes Operator  |  AlloyDB Omni for containers: 15.5.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/migrate-to-latest-version-kubernetes/

This page documents AlloyDB Omni version **15.5.5** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/overview)



Send feedback 

#  Migrate to the latest version of the AlloyDB Omni Kubernetes Operator Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.5keyboard_arrow_down

  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/migrate-to-latest-version-kubernetes)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/migrate-to-latest-version-kubernetes)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/migrate-to-latest-version-kubernetes)

This page covers instructions for upgrading from version 1.0.0 to version 1.1.0 of the AlloyDB Omni Operator. 

The steps that you take to upgrade AlloyDB Omni in Kubernetes depend upon the version of AlloyDB Omni that you run, and the version that you upgrade to.

## Determine your current version numbers

###  Kubernetes 

To check the version of AlloyDB Omni used by your database cluster, run this command:
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -n NAMESPACE -o jsonpath='{.status.primary.currentDatabaseVersion}'

Replace the following:

  * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/15.5.2/docs/deploy-kubernetes#create).

  * `NAMESPACE`: the Kubernetes namespace of your database cluster.




If you run version 1.0.0 or later of the AlloyDB Omni Operator, then this command prints the version of AlloyDB Omni used by your database cluster.

To check the version of the AlloyDB Omni Operator installed on your Kubernetes cluster, run this command:
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -n NAMESPACE -o jsonpath='{.status.primary.currentControlPlaneAgentsVersion}'

If you run version 1.0.0 or later of the AlloyDB Omni Operator, then this command prints the version number of the AlloyDB Omni Operator running on your Kubernetes cluster.

If you run a version of AlloyDB Omni Operator earlier than 1.0.0, follow the instructions in [Upgrade from a pre-1.0.0 AlloyDB Omni Operator](https://docs.cloud.google.com/alloydb/omni/15.5.2/docs/manage#older-operator).

Otherwise, continue to the Check your target version numbers section.

## Check your target version numbers

###  Kubernetes 

If you run a version of AlloyDB Omni Operator 1.0.0 or later, then your next steps depend upon the version of AlloyDB Omni that you want to upgrade to. This, in turn, requires understanding of the AlloyDB Omni version number.

The AlloyDB Omni version number has the following components:

  * The major version number of its PostgreSQL compatibility
  * The minor version number of its PostgreSQL compatibility
  * The patch version number of this AlloyDB Omni release



For example, AlloyDB Omni version 15.5.5 is patch version 5 of the AlloyDB Omni that supports PostgreSQL version 15.5.

If you want to upgrade to a version of AlloyDB Omni that supports a newer version of PostgreSQL, then you must upgrade the AlloyDB Omni Operator itself, alongside your database cluster. Each set of AlloyDB Omni releases that support a particular PostgreSQL minor version has its own AlloyDB Omni Operator version number, which you can find in [the release note](https://docs.cloud.google.com/alloydb/docs/release-notes) for the AlloyDB Omni version.

If you want to upgrade only to a newer patch version of AlloyDB Omni, then you can [upgrade](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/migrate-to-latest-version) only your database cluster, with no need to upgrade the AlloyDB Omni Operator itself.

Otherwise, continue to the Upgrade the AlloyDB Omni Operator section.

## Upgrade the AlloyDB Omni Operator

###  Kubernetes 

To upgrade the AlloyDB Omni Operator, follow these steps:

  1. Define the environment variables:
         
         export GCS_BUCKET=alloydb-omni-operator
         export OPERATOR_VERSION=OPERATOR_VERSION
         export HELM_PATH=$OPERATOR_VERSION/alloydbomni-operator-$OPERATOR_VERSION.tgz

Replace `OPERATOR_VERSION` with the version of the AlloyDB Omni Operator that you are upgrading to—for example, `1.1.0`.

  2. Download the latest AlloyDB Omni Operator:
         
         gcloud storage cp -r gs://$GCS_BUCKET/$HELM_PATH ./
         tar -xvzf alloydbomni-operator-${OPERATOR_VERSION}.tgz

  3. Apply the latest AlloyDB Omni Operator custom resource definitions:
         
         kubectl apply -f alloydbomni-operator/crds

  4. Upgrade the AlloyDB Omni Operator Helm chart:
         
         helm upgrade alloydbomni-operator alloydbomni-operator-${OPERATOR_VERSION}.tgz \
         --namespace alloydb-omni-system \
         --atomic \
         --timeout 5m




After completing the upgrade of your AlloyDB Omni Operator, follow the instructions in [Perform an in-place upgrade](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/migrate-to-latest-version#perform-in-place-upgrade) to create a new database cluster.

If your AlloyDB Omni cluster was created with AlloyDB Omni Operator 1.0.0, then add the `controlPlaneAgentsVersion` field to the manifest and set it to `1.1.0` before upgrading the cluster to version 15.5.5. Otherwise, the following error displays:
    
    
    admission webhook "vdbcluster.alloydbomni.dbadmin.goog" denied the request: unsupported database version 15.5.5 and/or control plane agents version 1.0.0
    

A sample manifest with the `controlPlaneAgentsVersion` field looks as follows:
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1
    kind: DBCluster
    metadata:
      name: DB_CLUSTER_NAME
    spec:
      databaseVersion: "15.5.5"
      **controlPlaneAgentsVersion: "1.1.0"**
    ...

**Note:** Upgrading to version 1.1.0 of the AlloyDB Omni Operator results in a brief interruption to all database clusters. No data loss is expected.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
