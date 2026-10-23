---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/upgrade-kubernetes-operator-version/
title: Upgrade your AlloyDB Omni Kubernetes operator to version 1.6.3 \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:45:31.579520+00:00
---

# Upgrade your AlloyDB Omni Kubernetes operator to version 1.6.3  |  AlloyDB Omni for Kubernetes: 16.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/upgrade-kubernetes-operator-version/

This page documents AlloyDB Omni version **16.9.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/overview)



Send feedback 

#  Upgrade your AlloyDB Omni Kubernetes operator to version 1.6.3 Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.9.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/upgrade-kubernetes-operator-version)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/upgrade-kubernetes-operator-version)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/upgrade-kubernetes-operator-version)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/upgrade-kubernetes-operator-version)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/upgrade-kubernetes-operator-version)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/upgrade-kubernetes-operator-version)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/upgrade-kubernetes-operator-version)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/upgrade-kubernetes-operator-version)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/upgrade-kubernetes-operator-version)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/upgrade-kubernetes-operator-version)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/upgrade-kubernetes-operator-version)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/upgrade-kubernetes-operator-version)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/upgrade-kubernetes-operator-version)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/upgrade-kubernetes-operator-version)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/upgrade-kubernetes-operator-version)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/upgrade-kubernetes-operator-version)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/upgrade-kubernetes-operator-version)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/upgrade-kubernetes-operator-version)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/upgrade-kubernetes-operator-version)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/upgrade-kubernetes-operator-version)

This page describes how to upgrade the AlloyDB Omni operator to version 1.6.3. The steps to upgrade depend on your current version of AlloyDB Omni and the version that you upgrade to. 

## Before you begin

When you upgrade the AlloyDB Omni operator, the database restarts unless all of the following are true:

  * You're upgrading the AlloyDB Omni operator version 1.1.1 to a newer version.
  * You're using the AlloyDB Omni database version 15.5.5 or later.
  * AlloyDB AI is not enabled. For more information, see [Create a database cluster with AlloyDB AI](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/install-with-alloydb-ai?resource=kubernetes#enable-alloydb-ai).



If the database restarts, no data loss is expected.

Starting from the AlloyDB Omni database version 15.7.1, high availability (HA) on your Kubernetes-based AlloyDB Omni database clusters uses a new architecture to provide more hardening and improvements for HA automatic setup, failover, and healing capabilities.

If you're upgrading the AlloyDB Omni database version from 15.7.0 (or earlier) to version 15.7.1 (or later), or if you're downgrading from versions 15.7.1 (or later) to version 15.7.0 (or earlier), you must disable HA, and you must re-enable HA after the process completes.

## Determine your current versions

To check the version of AlloyDB Omni used by your database cluster, run the following command:
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -n NAMESPACE -o jsonpath='{.status.primary.currentDatabaseVersion}'

Make the following replacements:

  * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you declared when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/deploy-kubernetes#create).

  * `NAMESPACE`: the Kubernetes namespace of your database cluster.




If you run version 1.0.0 or later of the AlloyDB Omni operator, then this command prints the version of AlloyDB Omni used by your database cluster.

To check the version of the AlloyDB Omni operator installed on your Kubernetes cluster, run the following command:
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -n NAMESPACE -o jsonpath='{.status.primary.currentControlPlaneAgentsVersion}'

If you run version 1.0.0 or later of the AlloyDB Omni operator, the output is the version number of the AlloyDB Omni operator running on your Kubernetes cluster.

If you run a version of AlloyDB Omni operator earlier than 1.0.0, follow the instructions in [Upgrade from a pre-1.0.0 AlloyDB Omni operator](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/manage#older-operator). Otherwise, check your target version numbers.

## Check your target version numbers

If you run a version of AlloyDB Omni operator 1.0.0 or later, then your next steps depend on the version of AlloyDB Omni that you want to upgrade to. The AlloyDB Omni version number has the following components:

  * The major version number of its PostgreSQL compatibility
  * The minor version number of its PostgreSQL compatibility
  * The patch version number of this AlloyDB Omni release



For example, AlloyDB Omni version 16.9.0 supports PostgreSQL version 15.7 and doesn't have a AlloyDB Omni release patch.

Choose the installation option that works for your target version:

Installation scenario | Update steps  
---|---  
You want to upgrade to a version of AlloyDB Omni that supports a newer version of PostgreSQL. | Upgrade the AlloyDB Omni operator and your database cluster. Each set of AlloyDB Omni releases that supports a specific PostgreSQL minor version has its own AlloyDB Omni operator version number. Use the [AlloyDB Omni operator version compatibility table](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/choose-compatible-versions#compatibility-table) to verify your AlloyDB Omni operator version is compatible with your operator version.  
You want to upgrade only to a newer patch version of AlloyDB Omni. | [Upgrade](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/upgrade-kubernetes-alloydb-omni-version) only your database cluster.  
All other scenarios | Follow the steps in upgrade the AlloyDB Omni operator.  
  
## Upgrade the AlloyDB Omni operator

To upgrade the AlloyDB Omni operator, follow these steps:

**Note:** AlloyDB Omni operator Helm charts are no longer available in Cloud Storage. You must download them from the OCI registry. 

  1. Authenticate Docker and Helm:
         
         gcloud auth configure-docker gcr.io
         gcloud auth print-access-token | helm registry login -u oauth2accesstoken --password-stdin https://gcr.io

  2. Update the custom resource definitions (CRDs) by pulling the chart and manually applying them:
         
         helm pull oci://gcr.io/alloydb-omni/alloydbomni-operator --version 1.6.3 --untar
         kubectl apply -f ./alloydbomni-operator/crds

  3. Upgrade the AlloyDB Omni operator Helm chart:
         
         helm upgrade alloydbomni-operator oci://gcr.io/alloydb-omni/alloydbomni-operator \
           --version 1.6.3 \
           --namespace alloydb-omni-system \
           --atomic \
           --timeout 5m




## Update OpenShift database clusters from version 1.4.1 or earlier

Starting with version 1.5.0, the AlloyDB Omni operator is compatible with OpenShift's default `restricted-v2` security context constraint. For new database clusters on OpenShift running `controlPlaneAgentsVersion` 1.5.0 or later, OpenShift [injects arbitrary user IDs](https://www.redhat.com/en/blog/a-guide-to-openshift-and-uids) for the database workloads. For database clusters running an older version, the database workloads must continue to run as default user ID `999`.

To update a database cluster on OpenShift from a `controlPlaneAgentsVersion` earlier than 1.5.0, follow these steps:

  1. Grant the database cluster's service account permission to use the `anyuid` security context constraint. This enables the database workload to run as default user ID.
         
         oc adm policy add-scc-to-user anyuid system:serviceaccount:NAMESPACE:DB_CLUSTER_NAME-sa

  2. Annotate the database cluster with `openshift.io/scc=anyuid`. The AlloyDB Omni operator version 1.5.0 or later recognizes this annotation and runs the database workloads as default user ID on OpenShift instead of allowing the platform to inject an arbitrary ID.
         
         kubectl annotate dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -n NAMESPACE openshift.io/scc=anyuid

  3. Proceed with the steps to update the database cluster to the latest version.




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

Run the following example, which is part of a manifest file that specifies version 16.9.0 of `databaseVersion` and version 1.6.3 of `controlPlaneAgentsVersion`:
         
         apiVersion: alloydbomni.dbadmin.goog/v1
         kind: DBCluster
         metadata:
           name: DB_CLUSTER_NAME
           namespace: NAMESPACE
         spec:
           **databaseVersion : "16.9.0"**
           **controlPlaneAgentsVersion : "1.6.3"**
         ...
         

Replace the following variable:

     * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name that you declared when you created it. For more information, see [Install AlloyDB Omni on Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/deploy-kubernetes#create).
     * `NAMESPACE`: the Kubernetes namespace of your database cluster.
  3. Wait for the upgrade to complete successfully.

  4. If you disabled HA before the upgrade, complete the following steps.

     1. Set the `numberOfStandbys` back to the number prior to upgrade in the cluster's manifest.

     2. Re-apply the manifest to re-enable HA.




## Update `alloydb_omni_instance_postgresql_wait_time_second_total`

If you're using the `alloydb_omni_instance_postgresql_wait_time_second_total` metric, you must update it to `alloydb_omni_instance_postgresql_wait_time_us_total`. To consume both metrics, use the Prometheus `OR` operator.
    
    
    (promQL A) OR (promQL A, but replace all occurrences of alloydb_omni_instance_postgresql_wait_time_second_total to alloydb_omni_instance_postgresql_wait_time_us_total)
    

If you use `seconds` as the unit for this metric, you must convert it to `us`.

For more information, see the [release notes](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/release-notes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
