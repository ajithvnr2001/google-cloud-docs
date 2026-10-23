---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/migrate-to-latest-version-kubernetes/
title: Migrate to the latest version of the AlloyDB Omni Kubernetes operator \u00a0|\u00a0 AlloyDB Omni for containers: 15.7.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:52:03.479765+00:00
---

# Migrate to the latest version of the AlloyDB Omni Kubernetes operator  |  AlloyDB Omni for containers: 15.7.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/migrate-to-latest-version-kubernetes/

This page documents AlloyDB Omni version **15.7.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/overview)



Send feedback 

#  Migrate to the latest version of the AlloyDB Omni Kubernetes operator Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.7.0keyboard_arrow_down

  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/migrate-to-latest-version-kubernetes)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/migrate-to-latest-version-kubernetes)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/migrate-to-latest-version-kubernetes)

This page describes how to upgrade the AlloyDB Omni operator. The steps to upgrade AlloyDB Omni in Kubernetes depend on your current version of AlloyDB Omni and the version that you upgrade to. 

## Determine your current versions

To check the version of AlloyDB Omni used by your database cluster, run the following command:
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -n NAMESPACE -o jsonpath='{.status.primary.currentDatabaseVersion}'

Make the following replacements:

  * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/deploy-kubernetes#create).

  * `NAMESPACE`: the Kubernetes namespace of your database cluster.




If you run version 1.0.0 or later of the AlloyDB Omni operator, then this command prints the version of AlloyDB Omni used by your database cluster.

To check the version of the AlloyDB Omni operator installed on your Kubernetes cluster, run the following command:
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -n NAMESPACE -o jsonpath='{.status.primary.currentControlPlaneAgentsVersion}'

If you run version 1.0.0 or later of the AlloyDB Omni operator, the output is the version number of the AlloyDB Omni operator running on your Kubernetes cluster.

If you run a version of AlloyDB Omni operator earlier than 1.0.0, follow the instructions in [Upgrade from a pre-1.0.0 AlloyDB Omni operator](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/manage#older-operator). Otherwise, continue with Check your target version numbers.

## Check your target version numbers

If you run a version of AlloyDB Omni operator 1.0.0 or later, then your next steps depend on the version of AlloyDB Omni that you want to upgrade to. The AlloyDB Omni version number has the following components:

  * The major version number of its PostgreSQL compatibility
  * The minor version number of its PostgreSQL compatibility
  * The patch version number of this AlloyDB Omni release



For example, AlloyDB Omni version 15.7.0 supports PostgreSQL version 15.7 and doesn't have a AlloyDB Omni release patch.

Choose the installation option that works for your target version:

Installation scenario | Update steps  
---|---  
You want to upgrade to a version of AlloyDB Omni that supports a newer version of PostgreSQL. | Upgrade the AlloyDB Omni operator and your database cluster. Each set of AlloyDB Omni releases that supports a specific PostgreSQL minor version has its own AlloyDB Omni operator version number, which you can find in [the release note](https://docs.cloud.google.com/alloydb/docs/release-notes) for the AlloyDB Omni version. Use the [AlloyDB Omni operator version compatibility table](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/choose-compatible-versions#compatibility-table) to verify your AlloyDB Omni operator version is compatible with your operator version.  
You want to upgrade only to a newer patch version of AlloyDB Omni. | [Upgrade](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/migrate-to-latest-version) only your database cluster. Check the [AlloyDB Omni operator version compatibility table](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/choose-compatible-versions#compatibility-table) and [release notes](https://docs.cloud.google.com/alloydb/docs/release-notes) before you upgrade to determine if you need to also update the AlloyDB Omni operator.  
All other scenarios | Follow the steps in [upgrade the AlloyDB Omni operator](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/migrate-to-latest-version-kubernetes#upgrade-operator).  
  
## Upgrade the AlloyDB Omni operator

To upgrade the AlloyDB Omni operator, follow these steps:

  1. Define the environment variables:
         
         export GCS_BUCKET=alloydb-omni-operator
         export OPERATOR_VERSION=OPERATOR_VERSION
         export HELM_PATH=$OPERATOR_VERSION/alloydbomni-operator-$OPERATOR_VERSION.tgz

Replace `OPERATOR_VERSION` with the version of the AlloyDB Omni operator that you're upgrading to—for example, `1.3.0`.

  2. Download the latest AlloyDB Omni operator:
         
         gcloud storage cp -r gs://$GCS_BUCKET/$HELM_PATH ./
         tar -xvzf alloydbomni-operator-${OPERATOR_VERSION}.tgz

  3. Apply the latest AlloyDB Omni operator custom resource definitions:
         
         kubectl apply -f alloydbomni-operator/crds

  4. Upgrade the AlloyDB Omni operator Helm chart:
         
         helm upgrade alloydbomni-operator alloydbomni-operator-${OPERATOR_VERSION}.tgz \
         --namespace alloydb-omni-system \
         --atomic \
         --timeout 5m

To update the `dbCluster`, you need to update the `databaseVersion` and the `controlPlaneAgentsVersion` versions in the manifest file. The following is part of a manifest file that specifies version 15.7.0 of `databaseVersion` and version 1.3.0 of `controlPlaneAgentsVersion`:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: DBCluster
         metadata:
         name: DB_CLUSTER_NAME
         spec:
         **databaseVersion: "15.7.0"**
         **controlPlaneAgentsVersion: "1.3.0"**
         ...

**Note:** When you upgrade the AlloyDB Omni operator, the database restarts unless all of the following are true: 
     * You're upgrading the AlloyDB Omni operator version 1.1.1 to a newer version. 
     * You're using the AlloyDB Omni database version 15.5.5 or later. 
     * AlloyDB AI is not [enabled](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/install-with-alloydb-ai?resource=kubernetes#enable-alloydb-ai). 
If the database restarts, no data loss is expected. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
