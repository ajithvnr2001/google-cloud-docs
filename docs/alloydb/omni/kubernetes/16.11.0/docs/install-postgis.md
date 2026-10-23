---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/install-postgis/
title: Install PostGIS for AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 16.11.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:52:25.591006+00:00
---

# Install PostGIS for AlloyDB Omni  |  AlloyDB Omni using the container orchestrator: 16.11.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/install-postgis/

This page documents AlloyDB Omni version **16.11.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/overview)



Send feedback 

#  Install PostGIS for AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.11.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/install-postgis)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/install-postgis)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/install-postgis)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/install-postgis)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/install-postgis)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/install-postgis)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/install-postgis)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/install-postgis)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/install-postgis)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/install-postgis)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/install-postgis)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/install-postgis)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/install-postgis)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/install-postgis)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/install-postgis)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/install-postgis)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/install-postgis)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/install-postgis)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/install-postgis)



Debian UBI

To store, index, and query geospatial data in AlloyDB Omni, you can manually add the [PostGIS extension](https://postgis.net/) to your installation.

You can install PostGIS by using either of the following methods:

  * Use Debian options in the Docker or Podman CLI. Docker relies on a daemon and requires root privileges for most operations, while Podman is daemonless and rootless.
  * Use Red Hat Universal Base Images (UBI). UBI container base operating system images are built from parts of Red Hat Enterprise Linux (RHEL).



## Before you begin

[Install the AlloyDB Omni Kubernetes operator](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/deploy-kubernetes#install-operator) on your Kubernetes cluster.

## Add PostGIS to your AlloyDB Omni installation

To add the PostGIS extension to your AlloyDB Omni installation, follow these steps:

  1. Set the `OMNI_VERSION` environment variable:
         
         OMNI_VERSION=VERSION
         

Replace `VERSION` with the complete AlloyDB Omni database server version—for example, `16.11.0`.

  2. Build a custom Docker image that includes the PostGIS extension:
         
         mkdir ~/alloydb-omni-postgis
         
         tee ~/alloydb-omni-postgis/Dockerfile << EOF
         ARG OMNI_VERSION
         FROM google/alloydbomni:OMNI_VERSION
         RUN apt-get update && \
               apt-get install -y --no-install-recommends \
               postgresql-16-postgis-3 && \
               apt-get purge -y --auto-remove && \
               rm -rf /var/lib/apt/lists/*
         EOF
         
         cd ~/alloydb-omni-postgis
         
         sudo docker build --build-arg OMNI_VERSION=$OMNI_VERSION --tag google/alloydbomni-with-postgis:OMNI_VERSION .
         

  3. Tag and push your custom PostGIS image to a container registry that your Kubernetes cluster can access:
         
         docker tag google/alloydbomni-with-postgis:OMNI_VERSION CUSTOM_IMAGE_URI
         docker push CUSTOM_IMAGE_URI
         

Replace `CUSTOM_IMAGE_URI` with the target image URI in your container registry—for example, `us-central1-docker.pkg.dev/my-project/my-repo/alloydbomni-with-postgis:16.11.0`.

  4. Create a manifest file named `db-cluster.yaml` that specifies your custom PostGIS image in the `databaseImage` field of the `DBCluster` resource:
         
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
           databaseVersion: "16.11.0"
           databaseImage: "CUSTOM_IMAGE_URI"
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

     * `DB_CLUSTER_NAME`: the name of your database cluster—for example, `my-db-cluster`.
     * `DB_CLUSTER_NAMESPACE`: the namespace of your database cluster—for example, `default`.
     * `ENCODED_PASSWORD`: the base64-encoded password for the `postgres` administrator user.
     * `CUSTOM_IMAGE_URI`: the URI of the custom PostGIS image that you pushed to your container registry.
     * `CPU_COUNT`: the number of vCPUs for the primary instance—for example, `2`.
     * `MEMORY_SIZE`: the memory size for the primary instance—for example, `8Gi`.
     * `DISK_SIZE`: the storage size for the primary instance data disk—for example, `10Gi`.
  5. Apply the manifest to your Kubernetes cluster:
         
         kubectl apply -f db-cluster.yaml
         

For more information about the `DBCluster` resource, see [Create a database cluster](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/deploy-kubernetes#create) and the [`DBCluster` custom resource reference](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/kubernetes-crds-1.7.0/dbcluster).

  6. Connect to your database Pod by using `psql`:
         
         export DBPOD=$(kubectl get pod -n DB_CLUSTER_NAMESPACE \
           --selector=alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME,alloydbomni.internal.dbadmin.goog/task-type=database \
           -o jsonpath='{.items[0].metadata.name}')
         
         kubectl exec -ti $DBPOD -n DB_CLUSTER_NAMESPACE -c database -- psql -h localhost -U postgres
         

  7. Enable PostGIS:
         
         CREATE EXTENSION IF NOT EXISTS POSTGIS;
         SELECT postgis_full_version();
         

The output looks similar to the following:
         
         postgres=# SELECT postgis_full_version();
         postgis_full_version
         --------------------------------------------------------------------------------------------------------------------------------
         POSTGIS="3.3.2 4975da8" [EXTENSION] PGSQL="150" GEOS="3.11.1-CAPI-1.17.1" PROJ="9.1.1" LIBXML="2.9.14" LIBJSON="0.16" LIBPROTOBUF="1.4.1" WAGYU="0.5.0 (Internal)"
         (1 row)
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
