---
url: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/logs-metrics/
title: Logs and metrics \u00a0|\u00a0 Google Distributed Cloud connected, version 1.8.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:30:40.975521+00:00
---

# Logs and metrics  |  Google Distributed Cloud connected, version 1.8.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/logs-metrics/

Select versionkeyboard_arrow_down

  * [ 1.13.0 ](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs)
  * [ 1.12.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.12.0/docs)
  * [ 1.11.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.11.0/docs)
  * [ 1.10.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.10.0/docs)
  * [ 1.9.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.9.0/docs)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ 1.7.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.1/docs)
  * [ 1.7.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.7.0/docs)
  * [ 1.6.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.1/docs)
  * [ 1.6.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.6.0/docs)
  * [ 1.5.1 ](https://docs.cloud.google.com/distributed-cloud/connected/1.5.1/docs)

For version information, see the [Distributed Cloud connected release notes](https://docs.cloud.google.com/distributed-cloud/connected/latest/docs/release-notes). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Connected ](https://docs.cloud.google.com/distributed-cloud/connected)
  * [ 1.8.0 ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs)
  * [ Guides ](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/overview)



Send feedback 

#  Logs and metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how Google Distributed Cloud connected logs various types of information about its operation and how to view that information. The collection of some types of logs and metrics incur additional charges. For more information, see [Billing for logs and metrics](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/pricing#logs).

## Configure logging and monitoring

Before you can start gathering logs and metrics, you must do the following:

  1. Enable the logging APIs by using the following commands:
         
         gcloud services enable opsconfigmonitoring.googleapis.com --project PROJECT_ID
         gcloud services enable logging.googleapis.com --project PROJECT_ID
         gcloud services enable monitoring.googleapis.com --project PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the target Google Cloud project.

  2. Grant the roles required to write logs and metrics:
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --role roles/opsconfigmonitoring.resourceMetadata.writer \
             --member "serviceAccount:PROJECT_ID.svc.id.goog[kube-system/metadata-agent]"
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --role roles/logging.logWriter \
              --member "serviceAccount:PROJECT_ID.svc.id.goog[kube-system/stackdriver-log-forwarder]"
         
         gcloud projects add-iam-policy-binding PROJECT_ID \
             --role roles/monitoring.metricWriter \
             --member "serviceAccount:PROJECT_ID.svc.id.goog[kube-system/gke-metrics-agent]"
         

Replace `PROJECT_ID` with the ID of the target Google Cloud project.




## Logs

This section lists the Cloud Logging resource types supported by Distributed Cloud. To view Distributed Cloud logs, use the [Logs Explorer](https://console.cloud.google.com/logs) in the Google Cloud console. Distributed Cloud logging is always enabled.

The Distributed Cloud connected logged resource types are the following standard Kubernetes resources:

  * `k8s_container`
  * `k8s_node`



You can also capture and retrieve Distributed Cloud connected logs by using the Cloud Logging API. For information about how to configure this logging mechanism, see the documentation for [Cloud Logging client libraries](https://docs.cloud.google.com/logging/docs/reference/libraries).

## Metrics

This section lists the Cloud Monitoring metrics supported by Distributed Cloud. To view Distributed Cloud metrics, use the [Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer) in the Google Cloud console.

### Distributed Cloud connected cluster metrics

For Distributed Cloud connected clusters, Distributed Cloud connected provides the following types of metrics generated by Distributed Cloud connected nodes:

  * **Resource metrics** provide information about Distributed Cloud connected node and Pod performance, such as CPU load and memory usage.
  * **System application metrics** provide information about Distributed Cloud connected system workloads, such as `coredns`.



For a list of these metrics, see [Google Distributed Cloud and Google Distributed Cloud metrics](https://docs.cloud.google.com/monitoring/api/metrics_anthos).

Distributed Cloud connected does not provide metrics generated by the Kubernetes control planes associated with Distributed Cloud connected clusters.

### Distributed Cloud connected hardware metrics

Distributed Cloud connected provides metrics for Distributed Cloud connected hardware by using the following resource types:

  * `edgecontainer.googleapis.com/Machine`
  * `edgecontainer.googleapis.com/Rack`



#### `Machine` resource metrics

Distributed Cloud connected writes the following Cloud Monitoring API metrics for the `edgecontainer.googleapis.com/Machine` resource:

Metric | Description  
---|---  
`/machine/cpu/total_cores`

  * Kind: `GAUGE`
  * Type: `INT`

| Total count of physical processor cores present on the machine.  
`/machine/cpu/usage_time`

  * Kind: `CUMULATIVE`
  * Type: `DOUBLE`
  * Unit: `Seconds`

| Cumulative CPU usage time for all cores on the machine. Type can be `workload` (customer workloads) or `system` (everything else).  
`/machine/cpu/utilization`

  * Kind: `GAUGE`
  * Type: `DOUBLE`

| CPU utilization percentage on the machine. Range is 0 to 1. Type can be `workload` (customer workloads) or `system` (everything else).  
`/machine/memory/total_bytes`

  * Kind: `GAUGE`
  * Type: `INT64`

| Byte count of total memory on the machine.  
`/machine/memory/used_bytes`

  * Kind: `GAUGE`
  * Type: `INT64`

| Byte count of used memory on the machine. `memory_type` is either `evictable` (reclaimable by the kernel) or `non-evictable` (not reclaimable).  
`/machine/memory/utilization`

  * Kind: `GAUGE`
  * Type: `DOUBLE`

| Memory utilization percentage on the machine. Range is 0 to 1. `memory_type` is either `evictable` (reclaimable by the kernel) or `non-evictable` (not reclaimable).  
`/machine/network/up`

  * Kind: `GAUGE`
  * Type: `BOOL`

| Indicates whether the network interface is up and running. Includes primary cards, secondary cards, and ports.  
`/machine/network/link_speed`

  * Kind: `GAUGE`
  * Type: `DOUBLE`
  * Unit: Bytes per second

| Link speed of the primary network interface card.  
`/machine/network/received_bytes_count`

  * Kind: `CUMULATIVE`
  * Type: `DOUBLE`

| Received byte count for the primary network interface card.  
`/machine/network/sent_bytes_count`

  * Kind: `CUMULATIVE`
  * Type: `DOUBLE`

| Sent byte count for the primary network interface card.  
`/machine/network/connectivity`

  * Kind: `GAUGE`
  * Type: `BOOL`

| Indicates whether the primary network interface card has internet connectivity.  
`/machine/disk/total_bytes`

  * Kind: `GAUGE`
  * Type: `INT64`

| Byte count of total disk space on the machine.  
`/machine/disk/used_bytes`

  * Kind: `GAUGE`
  * Type: `INT64`

| Byte count of used disk space on the machine.  
`/machine/disk/utilization`

  * Kind: `GAUGE`
  * Type: `DOUBLE`

| Disk space utilization percentage on the machine. Range is 0 to 1.  
`/machine/restart_count`

  * Kind: `CUMULATIVE`
  * Type: `INT`

| Number of restarts that the machine has undergone.  
`/machine/uptime`

  * Kind: `GAUGE`
  * Type: `INT`
  * Unit: `Seconds`

| Machine uptime since the last restart.  
`/machine/connected`

  * Kind: `GAUGE`
  * Type: `INT64`

| Indicates whether the machine is connected to Google Cloud.  
  
#### `Rack` resource metrics

Distributed Cloud connected writes the following Cloud Monitoring API metrics for the `edgecontainer.googleapis.com/Rack` resource:

Metric | Description  
---|---  
`/router/bgp_up`

  * Kind: `GAUGE`
  * Type: `BOOL`

| Indicates whether the BGP peering session on the router is up and healthy. `router_id` identifies the specific router (up to 2 per rack).  
`/router/connected`

  * Kind: `GAUGE`
  * Type: `BOOL`

| Indicates whether the BGP router is connected to Google Cloud. `router_id` identifies the specific router (up to 2 per rack).  
  
## Export custom application logs and metrics

Distributed Cloud connected automatically exports logs for applications running on Distributed Cloud connected workloads. To export metrics for an application running on Distributed Cloud connected workloads, you must annotate it as described in the next section.

### Annotate the workload to enable metrics export

To enable the collection of custom metrics from an application, add the following annotations to the application's Service or Deployment manifest:

  * `prometheus.io/scrape: "true"`
  * `prometheus.io/path: "ENDPOINT_PATH"`. Replace `ENDPOINT_PATH` with the full path to the target application's metric endpoint.
  * `prometheus.io/port: "PORT_NUMBER"`: the port on which the application's metric endpoint listens for connections.



### Run an example application

In this section, you create an application that writes custom logs and exposes a custom metric endpoint.

  1. Save the following Service and Deployment manifests to a file named `my-app.yaml`. Notice that the Service has the annotation `prometheus.io/scrape: "true"`:
         
         kind: Service
         apiVersion: v1
         metadata:
           name: "monitoring-example"
           namespace: "default"
           annotations:
             prometheus.io/scrape: "true"
         spec:
           selector:
             app: "monitoring-example"
           ports:
             - name: http
               port: 9090
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: "monitoring-example"
           namespace: "default"
           labels:
             app: "monitoring-example"
         spec:
           replicas: 1
           selector:
             matchLabels:
               app: "monitoring-example"
           template:
             metadata:
               labels:
                 app: "monitoring-example"
             spec:
               containers:
               - image: gcr.io/google-samples/prometheus-dummy-exporter:latest
                 name: prometheus-example-exporter
                 imagePullPolicy: Always
                 command:
                 - /bin/sh
                 - -c
                 - ./prometheus-dummy-exporter --metric-name=example_monitoring_up --metric-value=1 --port=9090
                 resources:
                   requests:
                     cpu: 100m
         

  2. Create the Deployment and the Service:
         
         kubectl --kubeconfig apply -f my-app.yaml




### View application logs

###  Console 

  1. In the Google Cloud console, go to the **Logs Explorer** page. 

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Click **Resource**.

  3. In the **All resource types** list, select `Kubernetes Container`.

  4. For **Cluster name** , select the name of your user cluster.

  5. For **Namespace name** , select `default`.

  6. Click **Add** , and then click **Run query**.

  7. In the **Query results** section, you can see log entries from the `monitoring-example` Deployment. For example:
         
         {
           "textPayload": "2020/11/14 01:24:24 Starting to listen on :9090\n",
           "insertId": "1oa4vhg3qfxidt",
           "resource": {
             "type": "k8s_container",
             "labels": {
               "pod_name": "monitoring-example-7685d96496-xqfsf",
               "cluster_name": ...,
               "namespace_name": "default",
               "project_id": ...,
               "location": "us-west1",
               "container_name": "prometheus-example-exporter"
             }
           },
           "timestamp": "2020-11-14T01:24:24.358600252Z",
           "labels": {
             "k8s-pod/pod-template-hash": "7685d96496",
             "k8s-pod/app": "monitoring-example"
           },
           "logName": "projects/.../logs/stdout",
           "receiveTimestamp": "2020-11-14T01:24:39.562864735Z"
         }
         




###  gcloud 

  1. Use the `gcloud logging read` command:
         
         gcloud logging read 'resource.labels.project_id="PROJECT_ID" AND \
             resource.type="k8s_container" AND resource.labels.namespace_name="default"'

Replace `PROJECT_ID` with the ID of your project.

  2. In the output, you can see log entries from the `monitoring-example` Deployment. For example:
         
         insertId: 1oa4vhg3qfxidt
         labels:
           k8s-pod/app: monitoring-example
           k8s- pod/pod-template-hash: 7685d96496
         logName: projects/.../logs/stdout
         receiveTimestamp: '2020-11-14T01:24:39.562864735Z'
         resource:
           labels:
             cluster_name: ...
             container_name: prometheus-example-exporter
             location: us-west1
             namespace_name: default
             pod_name: monitoring-example-7685d96496-xqfsf
             project_id: ...
           type: k8s_container
         textPayload: |
           2020/11/14 01:24:24 Starting to listen on :9090
         timestamp: '2020-11-14T01:24:24.358600252Z'
         




### View application metrics

Your example application exposes a custom metric named `example_monitoring_up`. You can view the values of that metric in the Google Cloud console.

  1. In the Google Cloud console, go to the **Metrics explorer** page. 

[Go to Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. For **Resource type** , select `Kubernetes Pod`.

  3. For **Metric** , select `external/prometheus/example_monitoring_up`.

  4. In the chart, you can see that `example_monitoring_up` has a repeated value of 1.




## Collect metrics with Prometheus

Distributed Cloud connected supports the [Prometheus](https://prometheus.io) metrics solution for collecting metrics on your Distributed Cloud connected workloads.

For this purpose, Distributed Cloud connected creates an unmanaged namespace with the name `prom-monitoring` when you create a Distributed Cloud connected cluster. We recommend that you use this namespace to deploy Prometheus. You can also copy the required resources from the `prom-monitoring` namespace to a namespace of your choice and deploy Prometheus there.

### Configure Prometheus metrics scraping

To collect Distributed Cloud connected metrics with Prometheus, you must configure Prometheus metrics scraping. To do so, mount the `prometheus-scrape-config` ConfigMap in your Prometheus Pod and add the scrape configuration from the ConfigMap to your Prometheus configuration. For example:
    
    
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: prometheus-deployment
      namespace: prom-monitoring
      labels:
        app: prom-monitoring
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: prom-monitoring
      template:
        metadata:
          labels:
            app: prom-monitoring
        spec:
          containers:
            - name: prometheus
              image: prom/prometheus:main
              args:
                - "--config.file=/etc/prometheus/prometheus.yml"
                - "--storage.tsdb.path=/prometheus/"
              ports:
                - containerPort: 9090
              volumeMounts:
                - name: prometheus-config-volume
                  mountPath: /etc/prometheus/
                - name: prometheus-scrape-config-volume
                  mountPath: /etc/prometheus/scrape/
                - name: prometheus-storage-volume
                  mountPath: /prometheus/
                - name: prometheus-scrape-token
                  mountPath: /var/run/secrets/kubernetes.io/stackdriver-prometheus-scrape
                - name: stackdriver-prometheus-scrape-cert
                  mountPath: /certs/stackdriver-prometheus-scrape
                - name: metrics-providers-ca
                  mountPath: /certs/metrics-providers
                - name: stackdriver-prometheus-etcd-scrape
                  mountPath: /stackdriver-prometheus-etcd-scrape
          volumes:
            - name: prometheus-storage-volume
              emptyDir: {}
            - name: prometheus-config-volume
              configMap:
                defaultMode: 420
                name: prometheus-config
            - name: prometheus-scrape-config-volume
              configMap:
                defaultMode: 420
                name: prometheus-scrape-config
            - name: prometheus-scrape-token
              secret:
                defaultMode: 420
                secretName: prometheus-scrape
            - name: stackdriver-prometheus-scrape-cert
              secret:
                defaultMode: 420
                secretName: stackdriver-prometheus-scrape-cert
            - name: metrics-providers-ca
              secret:
                defaultMode: 420
                items:
                - key: ca.crt
                  path: ca.crt
                secretName: metrics-providers-ca
            - name: stackdriver-prometheus-etcd-scrape
              secret:
                defaultMode: 420
                optional: true
                secretName: stackdriver-prometheus-etcd-scrape
    

To collect workload metrics with Prometheus, you must add annotations to the Services and Pods executing the target workloads as follows:

  * To send metrics to both Cloud Monitoring and Prometheus, use the annotations described in [Export custom logs and metrics](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/logs-metrics#export_custom_application_logs_and_metrics).

  * To send metrics only to Prometheus, use the following annotations:



    
    
    prometheus.io/unmanaged_scrape: "true"
    prometheus.io/unmanaged_path: "ENDPOINT_PATH"
    prometheus.io/unmanaged_port: "PORT_NUMBER"
    

## Collect logs with Kafka

Distributed Cloud connected supports the [Apache Kafka](https://kafka.apache.org/) solution for collecting logs on workloads running on your Distributed Cloud connected deployment.

You must have a functional Kafka deployment before completing the steps in this section. Your Kafka brokers must advertise their listeners in `PLAINTEXT` mode. SSL/SASL-related variables are not supported.

To configure a cluster for Kafka logging, you must create a JSON file that configures add-ons that you want to run on the cluster. Specify this file when creating a cluster using the `--system-addons-config` flag. If you need to modify the Kafka configuration, you must delete and re-create the cluster with the new Kafka settings.

Add the following section to the system add-ons configuration file:
    
    
    {
            "systemAddonsConfig": {
              "unmanagedKafkaConfig": {
                "brokers": "BROKERS",
                "topics": "TOPICS"
         "topic_key": "TOPIC_KEY, 
              }
          }
    }
    

Replace the following:

  * `BROKERS`: a comma-separated list of broker IP address and port pairs in `ip_address:port` format.
  * `TOPICS`: a comma-separated list Kafka topics.
  * `TOPIC_KEY`: a Kafka topic key; this allows Kafka to select a topic if multiple topics exist.



If Kafka is not collecting logs after you've created your Distributed Cloud connected cluster, check the following:

  * **Server side:** Check the error logs on your Kafka deployment for indications of a problem.
  * **Client side:** [Contact Google Support](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/getting-support) to retrieve and examine system Pod logs.



## What's next

  * [Audit logging](https://docs.cloud.google.com/distributed-cloud/connected/1.8.0/docs/audit-logging)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
