---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-troubleshooting/observability/
title: Observability troubleshooting \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:59:43.531370+00:00
---

# Observability troubleshooting  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-troubleshooting/observability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Observability troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to identify deployment failures and operational incidents you might encounter in Google Distributed Cloud (GDC) air-gapped appliance and contains descriptions of all the alerts displayed in the system to help you solve common issues with logging and monitoring components.

## Identify Observability components

The Observability platform deploys its components to the `obs-system` namespace in the org infrastructure cluster.

The Grafana instance of the Infrastructure Operator (IO) provides access to organization-level metrics to monitor infrastructure components such as CPU utilization and storage consumption. It also provides access to operational and audit logs. Additionally, it gives access to alerts, logs, and metrics from the GDC operable components.

The GDC monitoring and logging stacks use open source solutions as part of the Observability platform. These components collect logs and metrics from Kubernetes pods, bare metal machines, network switches, storage, and managed services.

The following table contains a description of all the components that integrate the Observability platform:

Component | Description  
---|---  
`Prometheus` |  [Prometheus](https://prometheus.io/docs/introduction/overview/) is a time-series database for collecting and storing metrics and evaluating alerts. Prometheus stores metrics in the [Cortex](https://cortexmetrics.io/) instance of the org infrastructure cluster for long-term storage. Prometheus adds labels as key-value pairs and collects metrics from Kubernetes nodes, pods, bare metal machines, network switches, and storage appliances.   
`Alertmanager` |  [Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/) is a user-defined manager system that sends alerts when logs or metrics indicate system components fail or do not operate normally. It manages Prometheus alerts routing, silencing, and aggregation.   
`Loki` |  [Loki](https://grafana.com/docs/loki/latest/) is a time-series database that stores and aggregates logs from various sources. It indexes logs for efficient querying.  
`Grafana` |  [Grafana](https://grafana.com/docs/grafana/latest/) provides a user interface (UI) for viewing metrics that Prometheus collects and querying audit and operational logs from the corresponding Loki instances. The UI lets you visualize dashboards of metrics and alerts.  
`Fluent Bit` |  [Fluent Bit](https://docs.fluentbit.io/manual) is a processor that pulls logs from various components or locations and sends them into Loki. It runs on every node of all clusters.   
  
## Identify deployment failures

If your deployment is running and healthy, the components run in the `READY` state.

Work through the following steps to identify deployment failures:

  1. Confirm the current state of a component:
         
         kubectl get -n obs-system TYPE/COMPONENT
         

Replace the following:

     * `TYPE`: the component type
     * `COMPONENT`: the component name

You get an output similar to the following:
    
    NAME       READY  AGE
    COMPONENT  1/1    23h
    

If the component is healthy, the `READY` column of the output shows `N/N` as a value. If the `READY` column doesn't show a value, it doesn't necessarily indicate failure. The service might need more time to process.

  2. Check the pods in each component:
         
         kubectl get pods -n obs-system | awk 'NR==1 | /COMPONENT/'
         

Replace `COMPONENT` with the component name.

You get an output similar to the following:
         
         NAME       READY  STATUS   RESTARTS  AGE
         COMPONENT  1/1    Running  0         23h
         

Verify that the `READY` column shows `N/N` as a value, the `STATUS` column shows a `Running` value, and the number of `RESTARTS` does not exceed a value of `2`.

A high number of restarts indicates the following symptoms:

     * The pods fail and Kubernetes restarts them.
     * The `STATUS` column shows the `CrashLoopBackoff` value.

To resolve the failing status, view the logs of the pods.

If a pod is in a state of `PENDING`, this state indicates one or more of the following symptoms:

     * The pod is waiting for network access to download the necessary container.
     * A configuration issue prevents the pod from starting. For example, a `Secret` value that the pod requires is missing.
     * Your Kubernetes cluster has run out of resources to schedule the pod, which occurs if many applications are running on the cluster.
  3. Determine the cause of a `PENDING` state:
         
         kubectl describe -n obs-system pod/POD_NAME
         

Replace `POD_NAME` with the name of the pod that shows the `PENDING` state.

The output shows more details about the pod.

  4. Navigate to the `Events` section of the output to view a table listing the recent events of the pod and a summary on the cause of the `PENDING` state.

The following output shows a sample `Events` section for a Grafana `StatefulSet` object:
         
         Events:
           Type    Reason            Age                From                    Message
           ----    ------            ----               ----                    -------
           Normal  SuccessfulCreate  13s (x3 over 12d)  statefulset-controller  create Pod grafana-0 in StatefulSet grafana successful
         

If there are no events in your pod or any other resource for an extended time, you receive the following output:
         
         Events:         <none>
         




## Check that the Observability logging stack is running

Work through the following steps to verify that the logging stack is running:

  1. Verify that all Loki instances or pods have the Istio sidecar injected. Verify that all Fluent Bit pods named `anthos-audit-logs-forwarder-SUFFIX` and `anthos-log-forwarder-SUFFIX` have the Istio sidecar injected.

  2. Check that all Loki instances are running without errors in the org infrastructure cluster.

  3. Check the status of `anthos-audit-logs-forwarder` and `anthos-log-forwarder` `DaemonSet` objects to verify that all instances are running in all nodes without errors.

  4. Verify that you get the operational logs from `kube-apiserver-SUFFIX` containers and audit logs from the Kubernetes API server for the last five minutes in all clusters. To do so, run the following queries in the Grafana instance:

     * **Operational logs** : `sum (count_over_time({service_name="apiserver"} [5m])) by (cluster, fluentbit_pod)`
     * **Audit logs** : `sum (count_over_time({cluster=~".+"} [5m])) by (cluster, node)`

You must obtain non-zero values for all control plane nodes in the org infrastructure cluster.




## Check that the Observability monitoring stack is running

Work through the following steps to verify that the monitoring stack is running:

  1. Check that the Grafana instances are running in the org infrastructure cluster. The `grafana-0` pods must run without errors in the following namespaces:

     * `obs-system`
     * `infra-obs-obs-system`
     * `platform-obs-obs-system`
**Note:** Other `PROJECT_NAMESPACE-obs-system` namespaces might run Grafana instances. The instances vary by cluster.
  2. Ensure that all monitoring components are in the Istio Service Mesh. Work through the steps of the Identify deployment failures section. Each of the following pods must show all containers are ready in the `READY` column. For example, a value of `3/3` means that three containers out of three are ready. Additionally, the pods must have an `istio-proxy` container. If the pods don't meet these conditions, restart the pod:

Pod name | Number of containers ready  
---|---  
`cortex-__`| `2/2`  
`cortex-etcd-0` | `2/2`  
`cortex-proxy-server-` | `2/2`  
`cortex-tenant-__`| `2/2`  
`meta-blackbox-exporter-` | `2/2`  
`meta-grafana-0` | `3/3`  
`meta-grafana-proxy-server-__`| `2/2`  
`meta-prometheus-0` | `4/4`  
`cortex-alertmanager-` | `2/2`  
`cortex-compactor-__`| `2/2`  
`cortex-distributor-` | `2/2`  
`cortex-etcd-0` | `2/2`  
`cortex-ingester-__`| `2/2`  
`cortex-querier-` | `2/2`  
`cortex-query-frontend-__`| `2/2`  
`cortex-query-scheduler-` | `2/2`  
`cortex-ruler-` | `2/2`  
`cortex-store-gateway-__`| `2/2`  
`cortex-tenant-` | `2/2`  
`grafana-proxy-server-__`| `2/2`  
`meta-blackbox-exporter-` | `2/2`  
`meta-grafana-0` | `3/3`  
`meta-grafana-proxy-server-*` | `2/2`  
`meta-prometheus-0` | `4/4`  
  3. Ensure that Cortex is running without errors.




## Retrieve Observability logs

The following table contains the commands that you must run to retrieve the logs for each of the components the Observability platform deploys.

**Note:** Depending on the cluster or component name, the command might be slightly different.Component | Log-retrieval command  
---|---  
`grafana` | `kubectl logs -n obs-system statefulset/grafana`  
`anthos-prometheus-k8s` | `kubectl logs -n obs-system statefulset/anthos-prometheus-k8s`  
`alertmanager` | `kubectl logs -n obs-system statefulset/alertmanager`  
`ops-logs-loki-io` | `kubectl logs -n obs-system statefulset/ops-logs-loki-io`  
`ops-logs-loki-io-read` | `kubectl logs -n obs-system statefulset/ops-logs-loki-io-read`  
`ops-logs-loki-all` | `kubectl logs -n obs-system statefulset/ops-logs-loki-all`  
`ops-logs-loki-all-read` | `kubectl logs -n obs-system statefulset/ops-logs-loki-all-read`  
`audit-logs-loki-io` | `kubectl logs -n obs-system statefulset/audit-logs-loki-io`  
`audit-logs-loki-io-read` | `kubectl logs -n obs-system statefulset/audit-logs-loki-io-read`  
`audit-logs-loki-pa` | `kubectl logs -n obs-system statefulset/audit-logs-loki-pa`  
`audit-logs-loki-pa-read` | `kubectl logs -n obs-system statefulset/audit-logs-loki-pa-read`  
`audit-logs-loki-all` | `kubectl logs -n obs-system statefulset/audit-logs-loki-all`  
`audit-logs-loki-all-read` | `kubectl logs -n obs-system statefulset/audit-logs-loki-all-read`  
`anthos-log-forwarder` | `kubectl logs -n obs-system daemonset/anthos-log-forwarder`  
`anthos-audit-logs-forwarder` | `kubectl logs -n obs-system daemonset/anthos-audit-logs-forwarder`  
`oplogs-forwarder` | `kubectl logs -n obs-system daemonset/oplogs-forwarder`  
`logmon-operator` | `kubectl logs -n obs-system deployment/logmon-operator`  
  
To view the logs of a component's previous instance, add the `-p` flag at the end of each command. Adding the `-p` flag lets you review logs of a previous failed instance instead of the current running instance.

## View the configuration

The Observability stack uses Kubernetes API custom resources to configure monitoring and logging pipelines.

The `LoggingPipeline` custom resource is deployed in the org infrastructure cluster and configures Loki instances.

The following commands show the available actions that you can perform on the logging pipeline:

  * View the current configuration of your logging pipeline deployment:
        
        kubectl get loggingpipeline -n obs-system default -o yaml
        

  * Change the configuration of your logging pipeline deployment:
        
        kubectl edit loggingpipeline -n obs-system default
        




GDC uses a logging and monitoring operator named `logmon-operator` to manage the deployment of Observability components such as Prometheus and Fluent Bit. The API to the `logmon-operator` component is the `logmon` custom resource definition. The `logmon` custom resource definition instructs the `logmon-operator` on how to configure Observability for your deployment. This custom resource definition includes the properties of volumes to store your metrics, alert rules for Alertmanager, Prometheus configurations to collect metrics, and Grafana configurations for dashboards.

The following commands show the available actions that you can perform on the `logmon` custom resource definition:

  * View the current configuration for your Observability deployment:
        
        kubectl get logmon -n obs-system logmon-default -o yaml
        

  * Change the configuration of your Observability deployment:
        
        kubectl edit logmon -n obs-system logmon-default
        




The output from running either command might reference multiple Kubernetes `ConfigMap` objects for further configuration. For example, you can configure Alertmanager rules in a separate `ConfigMap` object, which is referenced in the `logmon` custom resource definition by name. You can change and view the Alertmanager configuration through the `logmon` custom resource definition named `gpc-alertmanager-config`.

To view the Alertmanager configuration, run:
    
    
    kubectl get configmap -n obs-system gpc-alertmanager-config -o yaml
    

## Common issues

This section contains common issues you might face when deploying the Observability platform.

### You cannot access Grafana

By default, Grafana is not exposed to machines external to your Kubernetes cluster. To temporarily access the Grafana interface from outside of the org infrastructure cluster, you can port-forward the `Service` to localhost. To port-forward the `Service`, run:
    
    
    kubectl port-forward -n gpc-system service/grafana 33000\:3000
    

In your web browser, navigate to `http://localhost:33000` to view the Grafana dashboard for your deployment. To end the process, press the `Control+C` keys.

### Grafana runs slowly

Grafana running slowly indicates the following:

  * Queries to Prometheus or Loki return excessive data.
  * Queries return more data than is reasonable to display on a single graph.



To resolve slow speeds within Grafana, check the queries on your custom Grafana dashboards. If the queries return more data than is reasonable to display on a single graph, consider reducing the amount of data shown to improve dashboard performance.

### Grafana dashboard shows no metrics or logs

Grafana showing no metrics or logs could be caused by the following reasons:

  * Grafana data sources are not properly set.
  * The system has connectivity issues to either monitoring or logging data sources.
  * The system is not collecting metrics or logs.



To view the logs and metrics, follow these steps:

  1. In the Grafana user interface, click settings **Dashboard settings**.
  2. Select **Data Sources**.
  3. On the **Data Sources** page, make sure you see the following sources:

Name | Organization | URL  
---|---|---  
`Audit Logs` | `All` | `http://audit-logs-loki-io-read.obs-system.svc:3100`  
`Operational Logs` | `Root` | `http://ops-logs-loki-io-read.obs-system.svc:3100`  
`Operational Logs` | `Org` | `http://ops-logs-loki-all-read.obs-system.svc:3100`  
`prometheus` |  | `http://anthos-prometheus-k8s.obs-system.svc:9090`  
  
Missing these data sources indicates that the Observability stack failed to configure Grafana correctly.

If you configured the data sources correctly but no data shows, this might indicate an issue with `Service` objects that collect metrics or logs to feed into Prometheus or Loki.

As Prometheus collects metrics, it follows a pull model to periodically query your `Service` objects for metrics and store the values found. For Prometheus to discover your `Service` objects for metric collection, the following must be true:

  * All pods for `Service` objects are annotated with `'monitoring.gke.io/scrape: "true"'`.

**Note:** If your service is a deployment or a `StatefulSet` object, add the annotation to the service for Kubernetes to propagate it to your pods.
  * The Prometheus metric format exposes the pod metrics over HTTP. By default, Prometheus looks for these metrics at the endpoint `http://POD_NAME:80/metrics`. If needed, you can override the port, endpoint, and schema through annotations.




Fluent Bit collects logs and is intended to run on every node of your Kubernetes clusters. Fluent Bit sends the logs to Loki for long term storing.

If no logs are present in Grafana, try the following workarounds:

  * Check the logs of Loki instances to ensure they run without errors.

  * If the Loki instances are running properly but the logs do not appear, check the logs in Fluent Bit to ensure the service works as expected. To review how to pull logs, see Retrieve Observability logs.




### Alertmanager is not opening alerts

If Alertmanager fails to open alerts, work through the following steps:

  1. In your `configMap` object within the `gpc-system` namespace, ensure the label `logmon: system_metrics` exists.
  2. Verify that the `configMap` data section includes a key named `alertmanager.yml`. The value for the `alertmanager.yml` key must be the alert rules contained in your valid Alertmanager configuration file.
  3. Ensure the `logmon` custom resource definition named `logmon-default` in the `gpc-system` namespace contains a reference to the `configMap` object. The `logmon-default` custom resource definition must contain the name of the `configMap` object as shown in the following example:
         
         apiVersion: addons.gke.io/v1
         kind: Logmon
         spec:
           system_metrics:
             outputs:
               default_prometheus:
                 deployment:
                   components:
                     alertmanager:
                       alertmanagerConfigurationConfigmaps:
                         - alerts-config
         

The `alerts-config` value in the example is the name of your `configMap` object.




### Alertmanager is not sending alerts to the configured notification channels

A configuration error might prevent you from receiving notifications in the external software you configured as a notification channel, such as Slack, even if Alertmanager generates alerts in the Grafana instance.

To receive alerts in your external software, follow these steps:

  1. Check that the values in your Alertmanager configuration file are properly formatted. When Alertmanager triggers an alert, it queries a webhook on the external software.

  2. Ensure the webhook URLs that connect to the external software are correct. If the URLs are correct, ensure the software is configured to accept webhooks. You might need to generate an API key to access the external service API, or your current API key might be expired, and you need to refresh it.

  3. If the external service is outside of your GDC air-gapped appliance deployment, ensure your org infrastructure cluster has its egress rules configured. This configuration lets Alertmanager send requests to a service outside of the internal Kubernetes network. Failure to verify the egress rules could result in Alertmanager being unable to find the external software.




### You cannot see metrics from your project-scoped workload

Work through the following steps to apply a workaround and get metrics from your workload:

  1. Ensure the `MonitoringTarget` custom resource has a `Ready` status.
  2. To scrape your workload, you must declare all target information specified to the `MonitoringTarget` in the workloads pod specification. For example, if you declare that metrics are available on port `8080`, the workload pod must declare to Kubernetes that port `8080` is open. Otherwise, Prometheus ignores the workload.
  3. Prometheus runs multiple shards, which means that not all Prometheus pods are expected to scrape your pod. You can identify the shard number in the name of each Prometheus pod. As an example, `primary-prometheus-shard0-replica0-0` is part of shard `0`. Check for the pod you want to scrape from each Prometheus shard: 
     1. Port forward the `primary-prometheus-shardSHARD_NUMBER-replica0-0` pod of Prometheus in the `obs-system` namespace to gain access to the Prometheus UI. Replace `SHARD_NUMBER` in the pod name with increasing numbers every time you check a new shard.
     2. Go to the Prometheus UI in your web browser and follow these steps: 
        1. Click **Status** > **Targets**.
        2. Ensure the pod you want to scrape is in the list. If not, check the next shard. If there are no more shards to check, revalidate that Prometheus has enough information to discover it.
     3. Verify the `primary-prometheus-shardSHARD_NUMBER-replica0-0` pod of Prometheus logs errors in the `obs-system` namespace.
  4. Verify the `cortex-tenant` pod logs errors in the `obs-system` namespace.



### A dashboard was not created

Work through the following steps to apply a workaround and find why a dashboard is not created:

  1. Review the status of the `Dashboard` custom resource to look for any errors. The custom resource must have a `Ready` status.
  2. Ensure you are checking the correct Grafana instance. For example, if you deployed the dashboard in your project namespace named `my-namespace`, then the dashboard must be in the Grafana instance at the `https://GDCH_URL/my-namespace/grafana` endpoint.
  3. Check logs of the `fleet-admin-controller` in the `gpc-system` namespace. Look for any errors related to the dashboard by searching the dashboard name in the logs. If you find errors, the JSON file in your `configMap` object has an incorrect format, and you must correct it.
  4. Check the Grafana logs in the `PROJECT_NAME-obs-system` namespace to look for any errors. Dashboards query the Grafana REST API, so Grafana must be working for a dashboard to be created.



### Your alert is not opening

Work through the following steps to apply a workaround and find why an alert is not opening:

  1. Ensure Cortex and Loki are both in bucket-storage mode. Rules do not work unless the backend is backed by bucket storage.
  2. Verify the status of the `MonitoringRule` and `LoggingRule` custom resources is `Ready`.
  3. Check the following alerting conditions: 
     * **PromQL and LogQL expressions** : Compare all the functions you are using against the [Create alert rules](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/infrastructure/io-user/create-alert-rules) documentation to ensure your rules are configured as you want. Make sure that the expressions return a `true` or `false` value.
     * **Duration** : The `for` field of the custom resource defines how long a condition must be true. The `interval` field defines how often to evaluate the condition. Check the values of these fields against each other and ensure your conditions are logical.
  4. Check the Grafana UI to see if the alert is open using the **Alerts** page.
  5. If Grafana shows that the alert is open, check your notification channels and ensure Alertmanager can contact them to produce the alert.



### Expected logs are not available

Work through the following steps if you don't see operational logs from your component:

  1. Check if your component is running and producing logs.
  2. Check if your component logs should be collected as a built-in functionality. If not, ensure you have the `LoggingTarget` custom resource deployed with a valid specification and with a `Ready` status.



Work through the following steps if you don't see audit logs from your component:

  1. If your component writes logs to a file, ensure the file actually exists at the filesystem of the node on the path `/var/log/audit/SERVICE_NAME/NAMESPACE/ACCESS_LEVEL/audit.log`.
  2. Verify that the `anthos-audit-logs-forwarder-SUFFIX` pod on the same node has no errors.
  3. If your component uses a syslog endpoint to receive logs, ensure you have the `AuditLoggingTarget` custom resource deployed with a valid specification and with a `Ready` status.



## Identify predefined alert rules

This section contains information about the predefined alerting rules that exist in Observability components to notify you about system failures.

**Note:** Each of the predefined alerts in the following tables represents an operational incident.

### Predefined alert rules in Loki

The following table provides the preinstalled alerting rules in Loki for audit logging failures:

Preinstalled alerting rules in Loki for audit logging failures **Name** | **Type** | **Description**  
---|---|---  
`FluentBitAuditLoggingWriteFailure` | Critical | Fluent Bit failed to forward audit logs in the last five minutes.  
`LokiAuditLoggingWriteFailure` | Critical | Loki failed to write audit logs to backend storage.  
  
When one or more of these alerts are displayed, the system has lost at least one audit record.

### Predefined alert rules in Prometheus

The following table provides the preinstalled alerting rules in Prometheus for Kubernetes components:

Preinstalled alerting rules in Prometheus **Name** | **Type** | **Description**  
---|---|---  
`KubeAPIDown` | Critical | The Kube API has disappeared from the Prometheus target discovery for 15 minutes.  
`KubeClientErrors` | Warning | The errors ratio from the Kubernetes API server client has been greater than 0.01 for 15 minutes.  
`KubeClientErrors` | Critical | The errors ratio from the Kubernetes API server client has been greater than 0.1 for 15 minutes.  
`KubePodCrashLooping` | Warning | The Pod has been in a crash-looping state for longer than 15 minutes.  
`KubePodNotReady` | Warning | The Pod has been in an unready state for longer than 15 minutes.  
`KubePersistentVolumeFillingUp` | Critical | The free bytes of a claimed `PersistentVolume` object are less than 0.03.  
`KubePersistentVolumeFillingUp` | Warning | The free bytes of a claimed `PersistentVolume` object are less than 0.15.  
`KubePersistentVolumeErrors` | Critical | The persistent volume has been in a `Failed` or `Pending` phase for five minutes.  
`KubeNodeNotReady` | Warning | The node has not been ready for more than 15 minutes.  
`KubeNodeCPUUsageHigh` | Critical | The CPU usage of the node is greater than 80%.  
`KubeNodeMemoryUsageHigh` | Critical | The memory usage of the node is greater than 80%.  
`NodeFilesystemSpaceFillingUp` | Warning | The file system usage of the node is greater than 60%.  
`NodeFilesystemSpaceFillingUp` | Critical | The file system usage of the node is greater than 85%.  
`CertManagerCertExpirySoon` | Warning | A certificate is expiring in 21 days.  
`CertManagerCertNotReady` | Critical | A certificate is not ready to serve traffic after 10 minutes.  
`CertManagerHittingRateLimits` | Critical | You reached a rate limit when creating or renewing certificates for five minutes.  
`DeploymentNotReady` | Critical | A Deployment on the org infrastructure cluster has been in a non-ready state for longer than 15 minutes.  
`StatefulSetNotReady` | Critical | A `StatefulSet` object on the org infrastructure cluster has been in a non-ready state for longer than 15 minutes.  
`AuditLogsForwarderDown` | Critical | The `anthos-audit-logs-forwarder` DaemonSet has been down for longer than 15 minutes.  
`AuditLogsLokiDown` | Critical | The `audit-logs-loki` StatefulSet has been in a non-ready state for longer than 15 minutes.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
