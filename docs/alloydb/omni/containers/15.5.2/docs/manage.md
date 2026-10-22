---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/manage/
title: Manage and monitor AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.2 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:50:50.843518+00:00
---

# Manage and monitor AlloyDB Omni  |  AlloyDB Omni for containers: 15.5.2  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/manage/

This page documents AlloyDB Omni version **15.5.2** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/overview)



Send feedback 

#  Manage and monitor AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.2keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/manage)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/manage)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/manage)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/manage)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/manage)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/manage)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/manage)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/manage)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/manage)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/manage)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/manage)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/manage)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/manage)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/manage)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/manage)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/manage)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/manage)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/manage)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/manage)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/manage)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/manage)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/manage)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/manage)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/manage)

This page describes how to manage AlloyDB Omni user roles, monitor the activity of your AlloyDB Omni server, and update or remove your AlloyDB Omni installation. 

## Manage user roles

AlloyDB Omni uses the same [set of predefined PostgreSQL user roles that AlloyDB includes](https://docs.cloud.google.com/alloydb/docs/database-users/about#psql-roles-users), with the following differences:

  * AlloyDB Omni does not have an `alloydbiamuser` role.

  * AlloyDB Omni includes a superuser role named `alloydbadmin`.




As with AlloyDB, it's a best practice to follow these steps when setting up a database:

  1. Define or import your databases using the `postgres` user role. In a new installation, this role has database-creation and role-creation privileges, and no password.

  2. Create new user roles that have the correct level of access to your application's tables, again using the `postgres` user role.

  3. Configure your application to connect to the database using these new, limited-access roles.




You can create and define as many new user roles as you need. Don't modify or delete any of the user roles with which AlloyDB Omni ships.

For more information, see [Manage AlloyDB user roles](https://docs.cloud.google.com/alloydb/docs/database-users/about).

## Monitor AlloyDB Omni

Monitoring your AlloyDB Omni installation means reading and analyzing its log files.

AlloyDB Omni running on Kubernetes also has a set of basic metrics available as Prometheus endpoints. For a list of available metrics, see [AlloyDB Omni metrics](https://docs.cloud.google.com/alloydb/docs/reference/omni-metrics).

###  Single-server 

AlloyDB Omni logs its activity in two locations:

  * AlloyDB Omni logs database activity at `data/log/postgres`, relative to the directory that you defined in your `dataplane.conf` configuration file.

You can customize the name and format of this log file through the various `log_*` directives defined in `/var/alloydb/config/postgresql.conf`. For more information, see [Error Reporting and Logging](https://www.postgresql.org/docs/15/runtime-config-logging.html).

  * AlloyDB Omni logs its installation, startup, and shutdown activity at `/var/alloydb/logs/alloydb.log`.




To check the immediate running status of your server, see [Check the status of AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/run-connect#status).

###  Kubernetes 

### Find your database cluster log files

You can find `postgresql.audit` and `postgresql.log` files on the file system of the database pod. To access these files, follow these steps:

  1. Define an environment variable containing the name of the database pod.
         
         export DB_POD=`kubectl get pod -l alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME,alloydbomni.internal.dbadmin.goog/task-type=database -o jsonpath='{.items[0].metadata.name}'`

Replace `DB_CLUSTER_NAME` with the name of your database cluster. It's the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/deploy-kubernetes#create).

  2. Run a shell on the database pod as root.
         
         kubectl exec ${DB_POD} -it -- /bin/bash

  3. Find the log files in the `/obs/diagnostic/` directory:

     * `/obs/diagnostic/postgresql.audit`
     * `/obs/diagnostic/postgresql.log`



### List monitoring services

### v1.0

When you create a database cluster, AlloyDB Omni creates the following monitoring service for each instance CR of the database cluster in the same namespace:

`al-INSTANCE_NAME-monitoring-system`

To list the monitoring services, run the following command.
    
    
    kubectl get svc -n NAMESPACE | grep monitoring
    

Replace `NAMESPACE` with a namespace where your cluster belongs.

The following example response shows the `al-1060-dbc-monitoring-system`, `al-3de6-dbc-monitoring-system`, and `al-4bc0-dbc-monitoring-system` services. Each service corresponds to one instance.
    
    
    al-1060-dbc-monitoring-system   ClusterIP   10.0.15.227   <none>        9187/TCP   7d20h
    al-3de6-dbc-monitoring-system   ClusterIP   10.0.5.205    <none>        9187/TCP   7d19h
    al-4bc0-dbc-monitoring-system   ClusterIP   10.0.15.92    <none>        9187/TCP   7d19h
    

### Version < 1.0 

When you create a database cluster, AlloyDB Omni creates the following monitoring services in the same namespace as the database cluster:

  * `DB_CLUSTER-monitoring-db`

  * `DB_CLUSTER-monitoring-system`




To list the monitoring services, run the following command.
    
    
    kubectl get svc -n NAMESPACE | grep monitoring
    

Replace `NAMESPACE` with a namespace where your cluster belongs.

The following example response shows the `al-2953-dbcluster-foo7-monitoring-system` and the `al-2953-dbcluster-foo7-monitoring-db` service.
    
    
    al-2953-dbcluster-foo7-monitoring-db           ClusterIP   10.36.3.243    <none>        9187/TCP   44m
    al-2953-dbcluster-foo7-monitoring-system       ClusterIP   10.36.7.72     <none>        9187/TCP   44m
    

### View Prometheus metrics from the command line

The port `9187` is named as `metricsalloydbomni` for all monitoring services.

  1. Set up port forwarding from your local environment to the monitoring service.
         
         kubectl port-forward service/MONITORING_SERVICE -n NAMESPACE MONITORING_METRICS_PORT:metricsalloydbomni
         

Replace the following:

     * `MONITORING_SERVICE`: The name of the monitoring service that you want to forward—for example, `al-1060-dbc-monitoring-system`.

     * `NAMESPACE`: The namespace where your cluster belongs.

     * `MONITORING_METRICS_PORT`: A local available TCP port.

The following response shows that the services are being forwarded.
    
    Forwarding from 127.0.0.1:9187 -> 9187
    Forwarding from [::1]:9187 -> 9187
    

  2. While the previous command runs, you can access monitoring metrics through HTTP on the port that you specified. For example, you can use `curl` to see all of the metrics as plain text:
         
         curl http://localhost:MONITORING_METRICS_PORT/metrics
         




### View metrics using the Prometheus API

The `alloydbomni.internal.dbadmin.goog/task-type` label key and the `metricsalloydbomni` port is available as a default for all monitoring services in AlloyDB Omni. You can use them together with a single [`ServiceMonitor`](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/api-reference/api.md#monitoring.coreos.com/v1.ServiceMonitor) custom resource to select all the services for all namespaces in your database cluster.

For more information about using the Prometheus API, see the [Prometheus Operator documentation](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/getting-started/introduction.md).

The following is an example `spec` field of the `ServiceMonitor` custom resource that includes the `alloydbomni.internal.dbadmin.gdc.goog/task-type` label key and `metricsalloydbomni` port. The `ServiceMonitor` custom resource monitors and collects all the kubernetes services in all namespaces 

For more information about the complete `ServiceMonitor` definition, see the [`ServiceMonitor` custom resource definition ](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/api-reference/api.md#monitoring.coreos.com/v1.ServiceMonitor).

### v1.0
    
    
        spec:
          selector:
            matchLabels:
              alloydbomni.internal.dbadmin.goog/task-type: monitoring
          namespaceSelector:
            any: true
          endpoints:
            - port: metricsalloydbomni
    

### Version < 1.0 
    
    
        spec:
          selector:
            matchExpressions:
            - key: alloydbomni.internal.dbadmin.gdc.goog/task-type
              operator: Exists
              values: []
          namespaceSelector:
            any: true
          endpoints:
          - port: metricsalloydbomni
    

## Upgrade AlloyDB Omni

**Caution:** As with any database upgrade, be sure to back up your data before proceeding. You can use [the `pg_dumpall` command](https://www.postgresql.org/docs/current/app-pg-dumpall.html) to make a one-time local export of your data.

###  Single-server 

These instructions apply only to AlloyDB Omni version 15.2.0 and later.

### Before you begin

Your machine must have version 1.2 or later of [the AlloyDB Omni CLI](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/omni-cli) installed.

### Perform the upgrade

To upgrade your AlloyDB Omni installation, run the following command:
    
    
    sudo alloydb database-server upgrade

###  Kubernetes 

The steps that you take to upgrade AlloyDB Omni in Kubernetes depend upon the version of AlloyDB Omni that you are running, and the version that you are upgrading to.

### Determine your current version numbers

To check the version of AlloyDB Omni used by your database cluster, run this command:
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -n NAMESPACE -o jsonpath='{.status.primary.currentDatabaseVersion}'

Replace the following:

  * `DB_CLUSTER_NAME`: the name of your database cluster. It's the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/deploy-kubernetes#create).

  * `NAMESPACE`: the Kubernetes namespace of your database cluster.




If you are running version 1.0.0 or later of the AlloyDB Omni Operator, then this command prints the version of AlloyDB Omni in use by your database cluster.

To check the version of the AlloyDB Omni Operator installed on your Kubernetes cluster, run this command:
    
    
    kubectl get dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -n NAMESPACE -o jsonpath='{.status.primary.currentControlPlaneAgentsVersion}'

If you are running version 1.0.0 or later of the AlloyDB Omni Operator, then this command prints the version number of the AlloyDB Omni Operator running on your Kubernetes cluster.

If you are running a version of AlloyDB Omni Operator earlier than 1.0.0, then you can't perform an in-place upgrade of your database cluster or of the AlloyDB Omni Operator. Instead, you must follow the instructions in Upgrade from a pre-1.0.0 AlloyDB Omni Operator.

Otherwise, continue to the next section.

### Determine your target version numbers

If you are running a version of AlloyDB Omni Operator 1.0.0 or later, then your next steps depend upon the version of AlloyDB Omni that you want to upgrade to. This, in turn, requires understanding of the AlloyDB Omni version number.

The AlloyDB Omni version number has three parts:

  * The major version number of its PostgreSQL compatibility
  * The minor version number of its PostgreSQL compatibility
  * The patch version number of this AlloyDB Omni release



For example, AlloyDB Omni version 15.5.2 is patch version 2 of the AlloyDB Omni that supports PostgreSQL version 15.5.

If you want to upgrade to a version of AlloyDB Omni that supports a newer version of PostgreSQL, then you must upgrade the AlloyDB Omni Operator itself, alongside your database cluster. Each set of AlloyDB Omni releases that support a particular PostgreSQL minor version has its own associated AlloyDB Omni Operator version number, which you can find in [the release note](https://docs.cloud.google.com/alloydb/docs/release-notes) for the AlloyDB Omni version.

If you want to upgrade only to a newer patch version of AlloyDB Omni, then you can upgrade only your database cluster, with no need to upgrade the AlloyDB Omni Operator itself. You can skip to the instructions in Upgrade your database cluster.

Otherwise, continue to the next section.

### Upgrade the AlloyDB Omni Operator

To upgrade the AlloyDB Omni Operator, do the following:

  1. Define necessary environment variables:
         
         export GCS_BUCKET=alloydb-omni-operator
         export OPERATOR_VERSION=OPERATOR_VERSION
         export HELM_PATH=$OPERATOR_VERSION/alloydbomni-operator-$OPERATOR_VERSION.tgz

Replace `OPERATOR_VERSION` with the version of the AlloyDB Omni Operator that you are upgrading to—for example, `1.1.0`.

  2. Download the newer AlloyDB Omni Operator:
         
         gcloud storage cp gs://$GCS_BUCKET/$HELM_PATH ./ --recursive
         tar -xvzf alloydbomni-operator-${OPERATOR_VERSION}.tgz

  3. Apply the newer AlloyDB Omni Operator custom resource definitions:
         
         kubectl apply -f alloydbomni-operator/crds

  4. Upgrade the AlloyDB Omni Operator Helm chart:
         
         helm upgrade alloydbomni-operator alloydbomni-operator-${OPERATOR_VERSION}.tgz \
         --namespace alloydb-omni-system \
         --atomic \
         --timeout 5m




To follow up on your AlloyDB Omni Operator upgrade by upgrading both your Kubernetes manifest and your database cluster, follow the instructions in the next section immediately after completing the previous steps.

### Upgrade your database cluster

To upgrade your database cluster, update the following fields in the `spec` section of the manifest that defines it:

  * Set `databaseVersion` to the full version number of AlloyDB Omni that you want to upgrade this database cluster to.

  * If you have also upgraded AlloyDB Omni Operator, then set `controlPlaneAgentsVersion` to the full version number of the AlloyDB Omni Operator that you have upgraded.




If you are upgrading only the patch version of AlloyDB Omni—for example, updating `databaseVersion` from `15.5.1` to `15.5.2`—then this step is all that you need to accomplish.

If you are upgrading the minor version of PostgreSQL compatibility—for example, updating `databaseVersion` from `15.4.1` to `15.5.2`‐then you must also update `controlPlaneAgentsVersion`. In that case, make sure that you have followed the extra steps listed in Upgrade the AlloyDB Omni Operator.

As an example, the following manifest excerpt defines a database cluster running AlloyDB Omni Operator version `15.5.2`, with AlloyDB Omni Operator version `1.0.0`:
    
    
    apiVersion: alloydbomni.dbadmin.goog/v1 
    kind: DBCluster
    metadata:
      name: dbcluster-sample
    spec:
      databaseVersion: 15.5.2
      controlPlaneAgentsVersion: 1.0.0
    

In this example, to upgrade the database cluster to run AlloyDB Omni version `15.5.3`, change `databaseVersion: 15.5.2` to `databaseVersion: 15.5.3`.

### Upgrade from a pre-1.0.0 AlloyDB Omni Operator

If you are running a version of AlloyDB Omni Operator earlier than 1.0.0, then upgrading a Kubernetes-based AlloyDB Omni installation involves uninstalling and then re-installing the AlloyDB Omni Operator after backing up your data. Follow these steps:

  1. List all of your database clusters:
         
         kubectl get dbclusters.alloydbomni.dbadmin.goog --all-namespaces

  2. For each database cluster, use [the `pg_dumpall` command](https://www.postgresql.org/docs/current/app-pg-dumpall.html) to export all of its data.

**Warning:** Don't skip this step. If you don't export your data, then the next step irretrievably erases your data.
  3. [Uninstall the AlloyDB Omni Operator.](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/manage#uninstall) This includes deleting all of your database clusters.

  4. [Reinstall the AlloyDB Omni Operator.](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/deploy-kubernetes#install) You can use the same commands that you used to install the previous version of the AlloyDB Omni Operator, with no need to specify a new version number.

  5. [Recreate your database clusters.](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/deploy-kubernetes#create) You can adapt the same manifest files that you used when previously creating your database clusters. You might need to update the files to reflect API changes that version 1.0.0 of the AlloyDB Omni Operator introduced, such as the `databaseVersion` attribute replacing the older `version` attribute.

  6. Use [`pg_restore`](https://www.postgresql.org/docs/15/app-pgrestore.html) or [the `\i` command in `psql`](https://www.postgresql.org/docs/current/app-psql.html#APP-PSQL-META-COMMAND-INCLUDE) to import your previously exported data into the recreated clusters.




## Roll back an upgrade

These instructions apply only to AlloyDB Omni version 15.2.1 to 15.5.2. They don't apply to Kubernetes-based deployments of AlloyDB Omni.

To roll back AlloyDB Omni to its previously installed version, run this command:
    
    
    sudo alloydb database-server rollback
    

**Caution:** If you have installed the parameterized secure views technology preview on AlloyDB Omni version 15.5.0 or later, then you must [take some additional steps before rolling back](https://docs.cloud.google.com/alloydb/docs/ai/use-psvs#rollback).

## Uninstall AlloyDB Omni

###  Single-server 

To uninstall AlloyDB Omni, run the following command:
    
    
    sudo alloydb database-server uninstall

Your data directory remains on your file system after you uninstall AlloyDB Omni. You can move, archive, or delete this directory, depending on whether and how you want to preserve your data after uninstalling AlloyDB Omni.

###  Kubernetes 

### Delete your database cluster

To delete your database cluster, set `isDeleted` to `true` in its manifest. You can accomplish this with the following command.

**Caution:** Running the following command permanently erases all of the data stored in the named database cluster.
    
    
    kubectl patch dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -p '{"spec":{"isDeleted":true}}' --type=merge

Replace `DB_CLUSTER_NAME` with the name of your database cluster. It's the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/deploy-kubernetes#create).

### Uninstall the AlloyDB Omni Operator

**Caution:** Following these steps permanently deletes all AlloyDB Omni databases from your Kubernetes cluster.

To uninstall the AlloyDB Omni Kubernetes Operator from your Kubernetes cluster, take the following steps:

  1. Delete all of your database clusters:
         
         for ns in $(kubectl get dbclusters.alloydbomni.dbadmin.goog --all-namespaces -o=jsonpath='{range .items[*]}{.metadata.namespace}{"\n"}{end}'); do
         for cr in $(kubectl get dbclusters.alloydbomni.dbadmin.goog -n $ns -o=jsonpath='{range .items[*]}{.metadata.name}{"\n"}{end}'); do
         kubectl patch dbclusters.alloydbomni.dbadmin.goog $cr -n $ns --type=merge -p '{"spec":{"isDeleted":true}}'
         done
         done

  2. Wait for the AlloyDB Omni Kubernetes Operator to delete all of your database clusters. Use the following command to check whether any database resources remain:
         
         kubectl get dbclusters.alloydbomni.dbadmin.goog --all-namespaces

  3. Delete other resources that the AlloyDB Omni Kubernetes Operator created:
         
         kubectl delete failovers.alloydbomni.dbadmin.goog --all --all-namespaces
         kubectl delete restores.alloydbomni.dbadmin.goog --all --all-namespaces
         kubectl delete switchovers.alloydbomni.dbadmin.goog --all --all-namespaces

  4. Uninstall the AlloyDB Omni Kubernetes Operator:
         
         helm uninstall alloydbomni-operator --namespace alloydb-omni-system

  5. Clean up secrets, custom resource descriptions, and namespaces related to the AlloyDB Omni Kubernetes Operator:
         
         kubectl delete certificate -n alloydb-omni-system --all
         kubectl get secrets --all-namespaces -o custom-columns=NAMESPACE:.metadata.namespace,NAME:.metadata.name,ANNOTATION:.metadata.annotations.cert-manager\.io/issuer-name | grep -E 'alloydbomni|dbs-al' | awk '{print $1 " " $2}' | xargs -n 2 kubectl delete secret -n
         kubectl delete crd -l alloydb-omni=true
         kubectl delete ns alloydb-omni-system




## Resize your Kubernetes-based database cluster

To resize the CPU, memory, or storage of your Kubernetes-based database cluster, update the `resources` field of the manifests that define its pod. The AlloyDB Omni Operator applies the new specifications to your database pod immediately.

For more information about the AlloyDB Omni Operator manifest syntax, see [Create a database cluster](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/deploy-kubernetes#create).

The following restrictions apply to modifying a running database cluster's resources:

  * You can increase a disk's size only if the specified `storageClass` supports volume expansion.
  * You can't decrease a disk's size.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
