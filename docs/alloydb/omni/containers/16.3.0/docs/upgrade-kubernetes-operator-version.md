---
url: https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/upgrade-kubernetes-operator-version/
title: Upgrade your AlloyDB Omni Kubernetes operator to version 1.4.0 \u00a0|\u00a0 AlloyDB Omni for containers: 16.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:37:31.631849+00:00
---

# Upgrade your AlloyDB Omni Kubernetes operator to version 1.4.0  |  AlloyDB Omni for containers: 16.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/upgrade-kubernetes-operator-version/

This page documents AlloyDB Omni version **16.3.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/overview)



Send feedback 

#  Upgrade your AlloyDB Omni Kubernetes operator to version 1.4.0 Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.3.0keyboard_arrow_down

  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/upgrade-kubernetes-operator-version)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/upgrade-kubernetes-operator-version)

This page describes how to upgrade the AlloyDB Omni operator to version 1.4.0. The steps to upgrade depend on your current version of AlloyDB Omni and the version that you upgrade to. 

## Before you begin

When you upgrade the AlloyDB Omni operator, the database restarts unless all of the following are true:

  * You're upgrading the AlloyDB Omni operator version 1.1.1 to a newer version.
  * You're using the AlloyDB Omni database version 15.5.5 or later.
  * AlloyDB AI is not enabled. For more information, see [Create a database cluster with AlloyDB AI](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/install-with-alloydb-ai?resource=kubernetes#enable-alloydb-ai).



If the database restarts, no data loss is expected.

Starting from the AlloyDB Omni database version 15.7.1, high availability (HA) on your Kubernetes-based AlloyDB Omni database clusters uses a new architecture to provide more hardening and improvements for HA automatic setup, failover, and healing capabilities.

If you're upgrading the AlloyDB Omni database version from 15.7.0 (or earlier) to version 15.7.1 (or later), or if you're downgrading versions, you must disable HA, and you must re-enable HA after the process completes.

## Determine your current versions

To check the version of AlloyDB Omni used by your database cluster, run the following command:
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -n NAMESPACE -o jsonpath='{.status.primary.currentDatabaseVersion}'

Make the following replacements:

  * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you declared when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/deploy-kubernetes#create).

  * `NAMESPACE`: the Kubernetes namespace of your database cluster.




If you run version 1.0.0 or later of the AlloyDB Omni operator, then this command prints the version of AlloyDB Omni used by your database cluster.

To check the version of the AlloyDB Omni operator installed on your Kubernetes cluster, run the following command:
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -n NAMESPACE -o jsonpath='{.status.primary.currentControlPlaneAgentsVersion}'

If you run version 1.0.0 or later of the AlloyDB Omni operator, the output is the version number of the AlloyDB Omni operator running on your Kubernetes cluster.

If you run a version of AlloyDB Omni operator earlier than 1.0.0, follow the instructions in [Upgrade from a pre-1.0.0 AlloyDB Omni operator](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/manage#older-operator). Otherwise, check your target version numbers.

## Check your target version numbers

If you run a version of AlloyDB Omni operator 1.0.0 or later, then your next steps depend on the version of AlloyDB Omni that you want to upgrade to. The AlloyDB Omni version number has the following components:

  * The major version number of its PostgreSQL compatibility
  * The minor version number of its PostgreSQL compatibility
  * The patch version number of this AlloyDB Omni release



For example, AlloyDB Omni version 16.3.0 supports PostgreSQL version 15.7 and doesn't have a AlloyDB Omni release patch.

Choose the installation option that works for your target version:

Installation scenario | Update steps  
---|---  
You want to upgrade to a version of AlloyDB Omni that supports a newer version of PostgreSQL. | Upgrade the AlloyDB Omni operator and your database cluster. Each set of AlloyDB Omni releases that supports a specific PostgreSQL minor version has its own AlloyDB Omni operator version number. Use the [AlloyDB Omni operator version compatibility table](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/choose-compatible-versions#compatibility-table) to verify your AlloyDB Omni operator version is compatible with your operator version.  
You want to upgrade only to a newer patch version of AlloyDB Omni. | [Upgrade](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/upgrade-kubernetes-alloydb-omni-version) only your database cluster.  
All other scenarios | Follow the steps in upgrade the AlloyDB Omni operator.  
  
## Upgrade the AlloyDB Omni operator

To upgrade the AlloyDB Omni operator, follow these steps:

  1. Define the environment variables:
         
         export GCS_BUCKET=alloydb-omni-operator
         export OPERATOR_VERSION=OPERATOR_VERSION
         export HELM_PATH=$OPERATOR_VERSION/alloydbomni-operator-$OPERATOR_VERSION.tgz

Replace `OPERATOR_VERSION` with the version of the AlloyDB Omni operator that you're upgrading to—for example, `1.4.0`.

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




## Update the database clusters

To update the `dbCluster`, complete the following steps:

  1. If you're upgrading an HA AlloyDB Omni database cluster from database version 15.7.0 (or earlier) to version 15.7.1 (or later), follow these steps to disable HA.

**Note:** If you're upgrading from an older version to version 15.7.0 (or earlier), or from version 15.7.1 (or later) to a newer version, skip this step.
     1. Set the `numberOfStandbys` to `0` in the cluster's manifest.
    
    spec:
      availability:
        numberOfStandbys: 0
    

     1. To disable HA, re-apply the manifest.
  2. Update the `databaseVersion` and the `controlPlaneAgentsVersion` versions in the cluster's manifest, and re-apply the manifest.

Run the following example, which is part of a manifest file that specifies version 16.3.0 of `databaseVersion` and version 1.4.0 of `controlPlaneAgentsVersion`:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: DBCluster
         metadata:
           name: DB_CLUSTER_NAME
         spec:
           **databaseVersion : "16.3.0"**
           **controlPlaneAgentsVersion : "1.4.0"**
         ...
         

Replace the following variable:

     * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you declared when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/deploy-kubernetes#create).
  3. Wait for the upgrade to complete successfully.

  4. If you disabled HA before the upgrade, complete the following steps.

     1. Set the `numberOfStandbys` back to the number prior to upgrade in the cluster's manifest.

     2. Re-apply the manifest to re-enable HA.




## Update `alloydb_omni_instance_postgresql_wait_time_second_total`

If you're using the `alloydb_omni_instance_postgresql_wait_time_second_total` metric, you must update it to `alloydb_omni_instance_postgresql_wait_time_us_total`. To consume both metrics, use the Prometheus `OR` operator.
    
    
    (promQL A) OR (promQL A, but replace all occurrences of alloydb_omni_instance_postgresql_wait_time_second_total to alloydb_omni_instance_postgresql_wait_time_us_total)
    

If you use `seconds` as the unit for this metric, you must convert it to `us`.

For more information, see the [release notes](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/release-notes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
