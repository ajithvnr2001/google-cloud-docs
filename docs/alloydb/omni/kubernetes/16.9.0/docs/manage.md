---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/manage/
title: Manage and monitor AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:37:38.922678+00:00
---

# Manage and monitor AlloyDB Omni  |  AlloyDB Omni for Kubernetes: 16.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/manage/

This page documents AlloyDB Omni version **16.9.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/overview)



Send feedback 

#  Manage and monitor AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.9.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/manage)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/manage)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/manage)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/manage)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/manage)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/manage)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/manage)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/manage)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/manage)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/manage)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/manage)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/manage)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/manage)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/manage)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/manage)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/manage)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/manage)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/manage)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/manage)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/manage)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/manage)
  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/manage)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/manage)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/manage)

This page describes how to manage AlloyDB Omni user roles, monitor the activity of your AlloyDB Omni server, and update or remove your AlloyDB Omni installation. 

## Manage user roles

AlloyDB Omni uses the same [set of predefined PostgreSQL user roles that AlloyDB for PostgreSQL includes](https://docs.cloud.google.com/alloydb/docs/database-users/about#psql-roles-users), with the following differences:

  * AlloyDB Omni includes a superuser role named `alloydbadmin`, and a non-superuser role named `alloydbmetadata`.

  * The default `postgres` user has a superuser role.

  * All other predefined user roles have no privileges. They are reserved for potential uses in the future.




### Set up an AlloyDB Omni database

As with AlloyDB for PostgreSQL, it's a best practice to follow these steps when setting up a database:

  1. Define or import your databases using the `postgres` user role. In a new installation, this role has superuser privileges, and requires no password.

  2. Create new user roles that have the correct level of access to your application's tables, again using the `postgres` user role.

  3. Configure your application to connect to the database using these new, limited-access roles.




You can create and define as many new user roles as you need. Don't modify or delete any of the user roles with which AlloyDB Omni ships.

For more information, see [Manage AlloyDB Omni users and roles](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/database-users/manage-users).

## Monitor AlloyDB Omni

Monitoring your AlloyDB Omni installation includes reading and analyzing AlloyDB Omni log files.

For a list of available metrics, see [AlloyDB Omni metrics](https://docs.cloud.google.com/alloydb/docs/reference/omni-metrics).

AlloyDB Omni running on [Kubernetes](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/deploy-kubernetes) provides a set of basic metrics available as Prometheus endpoints. For a list of available metrics, see [AlloyDB Omni metrics](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/omni-metrics).

Additionally, AlloyDB Omni running on Kubernetes exposes metrics from custom resources leveraging [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics?tab=readme-ov-file#overview) (KSM). To enable custom resource metrics, see [Monitor AlloyDB Omni Kubernetes operator custom resources](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/monitor-kubernetes-operator-custom-resources).

###  Kubernetes 

### Find your database cluster log files

`postgresql.audit` and `postgresql.log` files are located on the file system of the database pod. `postgresql.audit` is only present if you [enabled pgaudit](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/configure-log-rotation#enable_audit_logs).

To access these files, follow these steps:

  1. Define an environment variable containing the name of the database pod.
         
         export DB_POD=`kubectl get pod -l alloydbomni.internal.dbadmin.goog/dbcluster=DB_CLUSTER_NAME,alloydbomni.internal.dbadmin.goog/task-type=database -o jsonpath='{.items[0].metadata.name}'`

Replace `DB_CLUSTER_NAME` with the name of your database cluster. It's the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/deploy-kubernetes#create).

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

The `alloydbomni.internal.dbadmin.goog/task-type` label key and the `metricsalloydbomni` port is available as a default for all monitoring services in AlloyDB Omni. You can use them together with a single [`serviceMonitor`](https://github.com/prometheus-operator/prometheus-operator/blob/main/Documentation/api-reference/api.md#monitoring.coreos.com/v1.ServiceMonitor) custom resource to select all the services for all namespaces in your database cluster.

For more information about using the Prometheus API, see the [Prometheus Operator documentation](https://prometheus-operator.dev/docs/api-reference/api/).

The following is an example `spec` field of the `serviceMonitor` custom resource that includes the `alloydbomni.internal.dbadmin.gdc.goog/task-type` label key and `metricsalloydbomni` port. The `serviceMonitor` custom resource monitors and collects all the kubernetes services in all namespaces

For more information about the complete `ServiceMonitor` definition, see the [`ServiceMonitor` custom resource definition ](https://prometheus-operator.dev/docs/api-reference/api/#monitoring.coreos.com/v1.ServiceMonitor).

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
    

### View metrics using Grafana

For a visual representation of metrics in AlloyDB Omni on Kubernetes, use the monitoring dashboard. The monitoring dashboard relies on a basic observability stack that consists of Prometheus and Grafana. To configure the monitoring dashboard to collect metrics from AlloyDB Omni, follow these steps:

  1. To download the Grafana dashboard, use the `wget` command:
         
         wget https://raw.githubusercontent.com/GoogleCloudPlatform/alloydb-omni-samples/refs/heads/main/monitoring-dashboards/grafana/alloydbomni_dashboard.yaml
         

  2. You must download and install the grafana-operator before deploying Grafana in Kubernetes. For detailed instructions, see [Installation](https://grafana.github.io/grafana-operator/docs/installation/).

  3. Add the `monitoring.dashboard/product=alloydb-omni` label to the Grafana instance where you install the dashboard:
         
         kubectl label grafana/GRAFANA_INSTANCE_NAME monitoring.dashboard/product=alloydb-omni -n NAMESPACE
         

Replace the following:

     * `GRAFANA_INSTANCE_NAME`: the name of the Grafana instance where you put the dashboard.
     * `NAMESPACE`: the namespace where you deployed the Grafana operator.
  4. To apply the Grafana dashboard configuration to your AlloyDB Omni cluster on Kubernetes, use the following command:
         
         kubectl apply -f alloydbomni_dashboard.yaml -n NAMESPACE
         

See [Grafana operator documentation](https://grafana.github.io/grafana-operator/docs/) for information about using the Grafana operator.

  5. To configure Grafana to use Prometheus as a data source, see [Datasources](https://grafana.github.io/grafana-operator/docs/examples/datasource/).

  6. To verify Grafana is configured correctly, do one of the following:

     * View the collection of Grafana panels on the **AlloyDB Omni dashboard**.
     * Retrieve information about the Grafana dashboard in a Kubernetes cluster:
           
           kubectl get grafanadashboard alloydb-omni-dashboard -n NAMESPACE -o jsonpath='{.status.conditions[?(@.type=="DashboardSynchronized")].status}'
           

If the command returns `True`, the `alloydb-omni-dashboard` is successfully deployed to the Grafana instance.




## Upgrade AlloyDB Omni

To upgrade from AlloyDB Omni 15.5.2 or earlier to 15.5.4, follow instructions in [Migrate from earlier version of AlloyDB Omni to latest version](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/migrate-to-latest-version-kubernetes). 

To upgrade from 15.5.4 and later:

  1. Restart AlloyDB Omni using a new image version.

  2. Make sure to specify your data directory to match the same path as used in earlier versions of AlloyDB Omni.




## Uninstall AlloyDB Omni

###  Kubernetes 

### Delete your database cluster

To delete your database cluster, set `isDeleted` to `true` in its manifest. You can accomplish this with the following command.

**Caution:** Running the following command permanently erases all of the data stored in the named database cluster.
    
    
    kubectl patch dbclusters.alloydbomni.dbadmin.goog DB_CLUSTER_NAME -p '{"spec":{"isDeleted":true}}' --type=merge

Replace `DB_CLUSTER_NAME` with the name of your database cluster. It's the same database cluster name you declared when [you created it](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/deploy-kubernetes#create).

### Uninstall the AlloyDB Omni operator

**Caution:** Following these steps permanently deletes all AlloyDB Omni databases from your Kubernetes cluster.

To uninstall the AlloyDB Omni Kubernetes operator from your Kubernetes cluster, take the following steps:

  1. Delete all of your database clusters:
         
         for ns in $(kubectl get dbclusters.alloydbomni.dbadmin.goog --all-namespaces -o=jsonpath='{range .items[*]}{.metadata.namespace}{"\n"}{end}'); do
         for cr in $(kubectl get dbclusters.alloydbomni.dbadmin.goog -n $ns -o=jsonpath='{range .items[*]}{.metadata.name}{"\n"}{end}'); do
         kubectl patch dbclusters.alloydbomni.dbadmin.goog $cr -n $ns --type=merge -p '{"spec":{"isDeleted":true}}'
         done
         done

  2. Wait for the AlloyDB Omni Kubernetes operator to delete all of your database clusters. Use the following command to check whether any database resources remain:
         
         kubectl get dbclusters.alloydbomni.dbadmin.goog --all-namespaces

  3. Delete other resources that the AlloyDB Omni Kubernetes operator created:
         
         kubectl delete failovers.alloydbomni.dbadmin.goog --all --all-namespaces
         kubectl delete restores.alloydbomni.dbadmin.goog --all --all-namespaces
         kubectl delete switchovers.alloydbomni.dbadmin.goog --all --all-namespaces

  4. Uninstall the AlloyDB Omni Kubernetes operator:
         
         helm uninstall alloydbomni-operator --namespace alloydb-omni-system

  5. Clean up secrets, custom resource descriptions, and namespaces related to the AlloyDB Omni Kubernetes operator:
         
         kubectl delete certificate -n alloydb-omni-system --all
         kubectl get secrets --all-namespaces -o custom-columns=NAMESPACE:.metadata.namespace,NAME:.metadata.name,ANNOTATION:.metadata.annotations.cert-manager\.io/issuer-name | grep -E 'alloydbomni|dbs-al' | awk '{print $1 " " $2}' | xargs -n 2 kubectl delete secret -n
         kubectl delete crd -l alloydb-omni=true
         kubectl delete ns alloydb-omni-system




## Resize your Kubernetes-based database cluster

To resize the CPU, memory, or storage of your Kubernetes-based database cluster, update the `resources` field of the manifests that define its pod. The AlloyDB Omni operator applies the new specifications to your database pod immediately.

For more information about the AlloyDB Omni operator manifest syntax, see [Create a database cluster](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/deploy-kubernetes#create).

The following restrictions apply to modifying a running database cluster's resources:

  * You can increase a disk's size only if the specified `storageClass` supports volume expansion.
  * You can't decrease a disk's size.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
