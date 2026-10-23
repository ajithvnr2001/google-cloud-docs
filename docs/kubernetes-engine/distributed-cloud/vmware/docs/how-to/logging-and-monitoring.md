---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/logging-and-monitoring/
title: Configure logging and monitoring \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:05.242097+00:00
---

# Configure logging and monitoring  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/logging-and-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Configure logging and monitoring Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to configure logging and monitoring for system components in Google Distributed Cloud (software only) for VMware.

By default, Cloud Logging, Cloud Monitoring, and Google Cloud Managed Service for Prometheus are enabled.

For more information about the options, see [Logging and monitoring overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/logging-and-monitoring).

## Monitored resources

Monitored resources are how Google represents resources such as clusters, nodes, Pods, and containers. To learn more, refer to Cloud Monitoring's [Monitored resource types](https://docs.cloud.google.com/monitoring/api/resources#tag_k8s_cluster) documentation.

To query for logs and metrics, you'll need to know at least these resource labels:

  * `project_id`: [Project ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#identifying_projects) of the cluster's [logging-monitoring project](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/multiple-gcp-projects#logging_monitoring_project). You provided this value in the `stackdriver.projectID` field of your cluster configuration file.

  * `location`: A Google Cloud region where you want to route and store your Cloud Monitoring metrics. You specify the region during installation in the [`stackdriver.clusterLocation`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#stackdriver-clusterlocation-field) field of your cluster configuration file. We recommend choosing a region that's near your on-premises data center.

You specify the Cloud Logging logs routing and storage location in the Log Router configuration. For more information about logs routing, see [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview).

  * `cluster_name`: Cluster name that you chose when you created the cluster.

You can retrieve the `cluster_name` value for either the admin or the user cluster by inspecting the Stackdriver custom resource:
        
        kubectl get stackdriver stackdriver --namespace kube-system \
        --kubeconfig CLUSTER_KUBECONFIG --output yaml | grep 'clusterName:'
        

where

    * `CLUSTER_KUBECONFIG` is the path to the admin cluster's or user cluster's kubeconfig file for which the cluster name is required.



## Logs and metrics routing

Stackdriver log forwarder (`stackdriver-log-forwarder`) sends logs from each node machine to Cloud Logging. Similarly, GKE metrics agent (`gke-metrics-agent`) sends metrics from each node machine to Cloud Monitoring. Before the logs and metrics are sent, the Stackdriver Operator (`stackdriver-operator`) attaches the value from the `clusterLocation` field in the `stackdriver` custom resource to each log entry and metric before they're routed to Google Cloud. Additionally, the logs and metrics are associated with the Google Cloud project specified in the `stackdriver` custom resource spec (`spec.projectID`).

All metrics and log entries sent by stackdriver agents are routed to a global ingestion endpoint. From there, the data is forwarded to the closest reachable regional Google Cloud endpoint to ensure the reliability of the data transport.

After the global endpoint receives the metric or log entry, what happens next is service-dependent:

  * **How logs routing is configured** : when the logging endpoint receives a log message, Cloud Logging passes the message through the Log Router. The sinks and filters in the Log Router configuration determine how to route the message. You can route log entries to destinations like regional Logging buckets, which store the log entry, or to Pub/Sub. For more information about how log routing works and how to configure it, see [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview).

Neither the `clusterLocation` field in the `stackdriver` custom resource or the `clusterOperations.location` field in the Cluster spec are considered in this routing process. For logs, `clusterLocation` is used to label log entries only, which can be helpful for filtering in Logs Explorer.

  * **How metrics routing is configured** : when the metrics endpoint receives a metric entry, the entry is routed automatically to be stored in the location specified by the metric. The location in the metric came from the `clusterLocation` field in the `stackdriver` custom resource.

  * **Plan your configuration** : when you configure your Cloud Logging and Cloud Monitoring, configure Log Router and specify an appropriate `clusterLocation` with locations that best support your needs. For example, if you want logs and metrics to go to the same location, set `clusterLocation` to the same Google Cloud region that Log Router is using for your Google Cloud project.

  * **Update your configuration when needed** : you can make changes anytime to the destination settings for logs and metrics due to business requirements, such as disaster recovery plans. Changes to the Log Router configuration in Google Cloud take effect quickly. The `location` and `projectID` fields in the `clusterOperations` section of the Cluster resource are immutable, so they can't be updated after you create your cluster. We don't recommend that you change values in the `stackdriver` resource directly. This resource is reverted to the original cluster creation state whenever a cluster operation, such as an upgrade, triggers a reconciliation.


The `stackdriver` resource gets values for the `clusterLocation` and `projectID` fields from the [`stackdriver.clusterLocation`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#stackdriver-clusterlocation-field) and [`stackdriver.projectID`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#stackdriver-projectid-field) fields in the `clusterOperations` section of the Cluster resource at cluster creation time. 

## Use Cloud Logging

You don't have to take any action to enable Cloud Logging for a cluster. However, you must specify the Google Cloud project where you want to view logs. In the cluster configuration file, you specify the Google Cloud project in the `stackdriver` section.

You can access logs using the [Logs Explorer](https://console.cloud.google.com/logs/query) in the Google Cloud console. For example, to access a container's logs:

  1. Open the [Logs Explorer](https://console.cloud.google.com/logs/query) in Google Cloud console for your project.
  2. Find logs for a container by: 
     1. Clicking on the top-left log catalog drop-down box and selecting **Kubernetes Container**.
     2. Selecting the cluster name, then the namespace, and then a container from the hierarchy.



### View logs for controllers in the bootstrap cluster

  1. In the Google Cloud console, go to the segment **Logs Explorer** page: 

[Go to **Logs Explorer**](https://console.cloud.google.com/logs/query)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. To view all logs for controllers in the bootstrap cluster, run the following query in the query editor:
         
         "ADMIN_CLUSTER_NAME"
         resource.type="k8s_container"
         resource.labels.cluster_name="gkectl-bootstrap-cluster"
         

  3. To view the logs for a specific pod, edit the query to include that pod's name:
         
         resource.type="k8s_container"
         resource.labels.cluster_name="gkectl-bootstrap-cluster"
         resource.labels.pod_name="POD_NAME"
         




## Use Cloud Monitoring

You don't have to take any action to enable Cloud Monitoring for a cluster. However, you must specify the Google Cloud project where you want to view metrics. In the cluster configuration file, you specify the Google Cloud project in the `stackdriver` section.

You can choose from over 1,500 metrics by using Metrics Explorer. To access Metrics Explorer, do the following:

  1. In the Google Cloud console, select **Monitoring** , or use the following button:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Select **Resources** > **Metrics Explorer**.




You can also view metrics in dashboards in the Google Cloud console. For information about creating dashboards and viewing metrics, see [Creating dashboards](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/monitoring-dashboards).

**Note:** The [GKE dashboards](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics) only display information for GKE clusters running on Google Cloud. They don't display information for Google Distributed Cloud.

### View fleet-level monitoring data

For an overall view of your fleet's resource utilization using Cloud Monitoring data, including your Google Distributed Cloud clusters, you can use the Google Kubernetes Engine overview in the Google Cloud console. See [Manage clusters from the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/connect-to-cluster-console) to find out more.

### Default Cloud Monitoring quota limits

Google Distributed Cloud monitoring has a default limit of 6000 API calls per minute for each project. If you exceed this limit, your metrics may not be displayed. If you need a higher monitoring limit, [request one through the Google Cloud console.](https://docs.cloud.google.com/docs/quotas/help/request_increase)

## Configure the Stackdriver custom resource

When you create a cluster, Google Distributed Cloud [automatically creates](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/logging-and-monitoring#stackdriver_gkeop) a Stackdriver custom resource. You can edit the spec in the custom resource to override the default values for CPU and memory requests and limits for a Stackdriver component, and you can separately override the default storage size and storage class.

### Override the default CPU and memory requests and limits for a Stackdriver component

Clusters with high pod density introduce higher logging and monitoring overhead. In extreme cases, Stackdriver components may report close to the CPU and memory utilization limit or even may be subject to constant restarts due to resource limits. In this case, to override the default values for CPU and memory requests and limits for a Stackdriver component, use the following steps:

  1. Run the following command to open your Stackdriver custom resource in a command-line editor:
         
         kubectl -n kube-system edit stackdriver stackdriver

  2. In the Stackdriver custom resource, add the `resourceAttrOverride` section under the `spec` field:
         
         resourceAttrOverride:
               DAEMONSET_OR_DEPLOYMENT_NAME/CONTAINER_NAME:
                 LIMITS_OR_REQUESTS:
                   RESOURCE: RESOURCE_QUANTITY

Note that the `resourceAttrOverride` section overrides all existing default limits and requests for the component you specify. The following components are supported by `resourceAttrOverride`:

     * `gke-metrics-agent/gke-metrics-agent`
     * `stackdriver-log-forwarder/stackdriver-log-forwarder`
     * `stackdriver-metadata-agent-cluster-level/metadata-agent`
     * `node-exporter/node-exporter`
     * `kube-state-metrics/kube-state-metrics`

An example file looks like the following:
    
    apiVersion: addons.gke.io/v1alpha1
    kind: Stackdriver
    metadata:
      name: stackdriver
      namespace: kube-system
    spec:
      projectID: my-project
      clusterName: my-cluster
      clusterLocation: us-west-1a
      resourceAttrOverride:
        gke-metrics-agent/gke-metrics-agent:
          requests:
            cpu: 110m
            memory: 240Mi
          limits:
            cpu: 200m
            memory: 4.5Gi

  3. To save changes to the Stackdriver custom resource, save and quit your command-line editor.

  4. Check the health of your Pod:
         
         kubectl -n kube-system get pods -l "managed-by=stackdriver"

A response for a healthy Pod looks like the following:
         
         gke-metrics-agent-4th8r                1/1     Running   1   40h

  5. Check the Pod spec of the component to make sure the resources are set correctly.
         
         kubectl -n kube-system describe pod POD_NAME

Replace `POD_NAME` with the name of the Pod you just changed. For example, `gke-metrics-agent-4th8r`.

The response looks like the following:
         
         Name:         gke-metrics-agent-4th8r
           Namespace:    kube-system
           ...
           Containers:
             gke-metrics-agent:
               Limits:
                 cpu: 200m
                 memory: 4.5Gi
               Requests:
                 cpu: 110m
                 memory: 240Mi
               ...




### Disable optimized metrics

By default, the metrics agents running in the cluster collect and report an optimized set of container, kubelet and kube-state-metrics metrics to Google Cloud Observability (formerly Stackdriver). If you require additional metrics, we recommend that you find a replacement from the list of [Google Distributed Cloud metrics](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/metrics-anthos).

Here are some examples of replacements you might use:

Disabled metric | Replacements  
---|---  
`kube_pod_start_time` | `container/uptime`  
`kube_pod_container_resource_requests` | `container/cpu/request_cores`   
`container/memory/request_bytes`  
`kube_pod_container_resource_limits` | `container/cpu/limit_cores`   
`container/memory/limit_bytes`  
  
To disable the optimized metrics default setting (not recommended), do the following:

  1. Open your Stackdriver custom resource in a command-line editor:
         
         kubectl -n kube-system edit stackdriver stackdriver

  2. Set the `optimizedMetrics` field to `false`:
         
         apiVersion: addons.gke.io/v1alpha1
         kind: Stackdriver
         metadata:
           name: stackdriver
           namespace: kube-system
         spec:
           projectID: my-project
           clusterName: my-cluster
           clusterLocation: us-west-1a
           optimizedMetrics: false

  3. Save changes, and quit your command-line editor.




### Override storage size defaults

To override these defaults, do the following:

  1. Open your Stackdriver custom resource in a command-line editor:
         
         kubectl --kubeconfig=KUBECONFIG -n kube-system edit stackdriver stackdriver

  2. Add the `storageSizeOverride` field under the `spec` section. You can use the component `stackdriver-prometheus-k8s` or `stackdriver-prometheus-app`. The section takes this format:
         
         storageSizeOverride:
         STATEFULSET_NAME: SIZE
         

This example uses the statefulset `stackdriver-prometheus-k8s` and size `120Gi`.
         
         apiVersion: addons.gke.io/v1alpha1
         kind: Stackdriver
         metadata:
           name: stackdriver
           namespace: kube-system
         spec:
           projectID: my-project
           clusterName: my-cluster
           clusterLocation: us-west-1a
           storageSizeOverride:
             stackdriver-prometheus-k8s: 120Gi
           

  3. Save, and quit your command-line editor.

  4. Check the health of your Pods:
         
         kubectl --kubeconfig=KUBECONFIG -n kube-system get pods | grep stackdriver

For example, a healthy Pod looks like the following: 
         
         stackdriver-prometheus-k8s-0                                2/2     Running   0          5d19h

  5. Check the Pod spec of the component to make sure the storage size is correctly overridden.
         
         kubectl --kubeconfig=KUBECONFIG -n kube-system describe statefulset STATEFULSET_NAME

The response looks like the following:
         
         Volume Claims:
          Name:          my-statefulset-persistent-volume-claim
          StorageClass:  my-storage-class
          Labels:
          Annotations:
          Capacity:      120Gi
          Access Modes:  [ReadWriteOnce]          




### Override storage class defaults

**Prerequisite**

You must first [create a StorageClass](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/default-storage-class#create_storageclass) you want to use.

To override the default storage class for persistent volumes claimed by logging and monitoring components:

  1. Open your Stackdriver custom resource in a command-line editor:
         
         kubectl --kubeconfig=KUBECONFIG -n kube-system edit stackdriver stackdriver

where KUBECONFIG is the path to your kubeconfig file for the cluster. This can be either an admin cluster or user cluster.

  2. Add the `storageClassName` field under the `spec` section:
         
         storageClassName: STORAGECLASS_NAME

Note that the `storageClassName` field overrides the existing default storage class, and applies to all logging and monitoring components with persistent volumes claimed. An example file looks like the following:
         
         apiVersion: addons.gke.io/v1alpha1
         kind: Stackdriver
         metadata:
           name: stackdriver
           namespace: kube-system
         spec:
           projectID: my-project
           clusterName: my-cluster
           clusterLocation: us-west-1a
           proxyConfigSecretName: my-secret-name
           enableVPC: 
           optimizedMetrics: true
           storageClassName: my-storage-class

  3. Save changes.

  4. Check the health of your Pods:
         
         kubectl --kubeconfig=KUBECONFIG -n kube-system get pods | grep stackdriver

For example, a healthy Pod looks like the following:
         
         stackdriver-prometheus-k8s-0                                1/1     Running   0          5d19h

  5. Check the Pod spec of a component to make sure the storage class is set correctly.
         
         kubectl --kubeconfig=KUBECONFIG -n kube-system describe statefulset STATEFULSET_NAME

For example, using the stateful set `stackdriver-prometheus-k8s`, the response looks like the following:
         
         Volume Claims:
          Name:          stackdriver-prometheus-data
          StorageClass:  my-storage-class
          Labels:
          Annotations:
          Capacity:      120Gi
          Access Modes:  [ReadWriteOnce]          




## Use Google Cloud Managed Service for Prometheus

Google Cloud Managed Service for Prometheus is part of Cloud Monitoring and is available as an option for system components. The benefits of Managed Service for Prometheus include the following:

  * You can continue to use your existing Prometheus-based monitoring without altering your alerts and Grafana dashboards.

  * If you use both GKE and Google Distributed Cloud, you can use the same [Prometheus Query Language (PromQL)](https://prometheus.io/docs/prometheus/latest/querying/basics/) for metrics on all your clusters. You can also use the **PromQL** tab in [Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer) in the Google Cloud console.




### Enable and disable Managed Service for Prometheus

Starting with Google Distributed Cloud release 1.30.0-gke.1930, Managed Service for Prometheus is always enabled. In earlier versions, you can edit the Stackdriver resource, `stackdriver`, to enable or disable Managed Service for Prometheus. To disable Managed Service for Prometheus for cluster versions prior to 1.30.0-gke.1930, set `spec.featureGates.enableGMPForSystemMetrics` in the `stackdriver` resource to `false`.

### View metric data

When `enableGMPForSystemMetrics` is set to `true`, metrics for the following components have a different format for how they are stored and queried in Cloud Monitoring:

  * kube-apiserver
  * kube-scheduler
  * kube-controller-manager
  * kubelet and cadvisor
  * kube-state-metrics
  * node-exporter



In the new format, you can query the preceding metrics by using [Prometheus Query Language (PromQL)](https://docs.cloud.google.com/monitoring/promql).

Example PromQL query:
    
    
    histogram_quantile(0.95, sum(rate(apiserver_request_duration_seconds_bucket[5m])) by (le))
    

### Configure Grafana dashboards with Managed Service for Prometheus

To use Grafana with metrics data from Managed Service for Prometheus, follow the steps in [Query using Grafana](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query) to authenticate and configure a Grafana data source to query data from Managed Service for Prometheus.

A set of sample Grafana dashboards are provided in the [anthos-samples](https://github.com/GoogleCloudPlatform/anthos-samples/tree/master/gmp-grafana-dashboards) repository on GitHub. To install the sample dashboards, do the following:

  1. Download the sample JSON files:
         
         git clone https://github.com/GoogleCloudPlatform/anthos-samples.git
         cd anthos-samples/gmp-grafana-dashboards
         

  2. If your Grafana data source was created with a name different with `Managed Service for Prometheus`, change the `datasource` field in all the JSON files:
         
         sed -i "s/Managed Service for Prometheus/[DATASOURCE_NAME]/g" ./*.json
         

Replace [DATASOURCE_NAME] with the name of the data source in your Grafana that was pointed to the Prometheus `frontend` service.

  3. Access Grafana UI from your browser, and select **\+ Import** after the **Dashboards** menu.

![Navigating to dashboard import in Grafana.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/images/grafana-welcome.png)

  4. Either upload the JSON file, or copy and paste the file content and select **Load**. After the file content is successfully loaded, select **Import**. Optionally you can also change the dashboard name and UID before importing.

![Importing dashboard in Grafana.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/images/grafana-import.png)

  5. The imported dashboard loads successfully if your Google Distributed Cloud and the data source are configured correctly. For example, the following screenshot shows the dashboard configured by `cluster-capacity.json`.

![Cluster capacity dashboard in Grafana.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/images/grafana-cluster-capacity.png)




### Additional resources

For more information about Managed Service for Prometheus, see the following:

  * [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus)

  * [GKE control plane metrics are PromQL compatible](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-control-plane-metrics-are-generally-available)

  * [Using Managed Service for Prometheus for user applications on Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/application-logging-monitoring#enable_managed_service_for_prometheus)




#### Known issue

In user clusters, Prometheus and Grafana get automatically disabled during upgrades. However, the configuration and metrics data are not lost.

To work around this issue, after the upgrade, open `monitoring-sample` for editing and set `enablePrometheus` to `true`.

### Access monitoring metrics from Grafana dashboards

Grafana displays metrics gathered from your clusters. To view these metrics, you need to access Grafana's dashboards:

  1. Get the name of the Grafana Pod running in a user cluster's `kube-system` namespace:
         
         kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] -n kube-system get pods

where [USER_CLUSTER_KUBECONFIG] is the user cluster's kubeconfig file.

  2. The Grafana Pod has an HTTP server listening on TCP localhost port 3000. Forward a local port to port 3000 in the Pod, so that you can view Grafana's dashboards from a web browser.

For example, suppose the name of the Pod is `grafana-0`. To forward port 50000 to port 3000 in the Pod, enter this command::
         
         kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] -n kube-system port-forward grafana-0 50000:3000

  3. From a web browser, navigate to `http://localhost:50000`.

  4. On the login page, enter `admin` for username and password.

  5. If login is successful, you will see a prompt to change the password. After you have changed the default password, the user cluster's Grafana Home Dashboard should load.

  6. To access other dashboards, click the **Home** drop-down menu in the top-left corner of the page.




For an example of using Grafana, see Create a Grafana dashboard.

### Access alerts

Prometheus Alertmanager collects alerts from the Prometheus server. You can view these alerts in a Grafana dashboard. To view the alerts, you need to access the dashboard:

  1. The container in the `alertmanager-0` Pod listens on TCP port 9093. Forward a local port to port 9093 in the Pod:
         
         kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] port-forward \
            -n kube-system alertmanager-0 50001:9093

  2. From a web browser, navigate to `http://localhost:50001`.




### Change Prometheus Alertmanager configuration

You can change Prometheus Alertmanager's default configuration by editing your user cluster's `monitoring.yaml` file. You should do this if you want to direct alerts to a specific destination, rather than keep them in the dashboard. You can learn how to configure Alertmanager in Prometheus' [Configuration](https://prometheus.io/docs/alerting/configuration/#configuration-file) documentation.

To change the Alertmanager configuration, perform the following steps:

  1. Make a copy of the user cluster's `monitoring.yaml` manifest file:
         
         kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] -n kube-system \
            get monitoring monitoring-sample -o yaml > monitoring.yaml

  2. To configure Alertmanager, make changes to the fields under `spec.alertmanager.yml`. When you're finished, save the changed manifest.

  3. Apply the manifest to your cluster:
         
         kubectl apply --kubeconfig [USER_CLUSTER_KUBECONIFG] -f monitoring.yaml




### Create a Grafana dashboard

You've deployed an application that exposes a metric, verified that the metric is exposed, and verified that Prometheus scrapes the metric. Now you can add the application-level metric to a custom Grafana dashboard.

To create a Grafana dashboard, perform the following steps:

  1. If necessary, gain access to Grafana.
  2. From the Home Dashboard, click the **Home** drop-down menu in the top-left corner of the page.
  3. From the right-side menu, click **New dashboard**.
  4. From the **New panel** section, click **Graph**. An empty graph dashboard appears.
  5. Click **Panel title** , then click **Edit**. The bottom **Graph** panel opens to the **Metrics** tab.
  6. From the **Data Source** drop-down menu, select **user**. Click **Add query** , and enter `foo` in the **search** field.
  7. Click the **Back to dashboard** button in the top-right corner of the screen. Your dashboard is displayed.
  8. To save the dashboard, click **Save dashboard** in the top-right corner of the screen. Choose a name for the dashboard, then click **Save**.



### Disabling Prometheus and Grafana

Starting from version 1.16, Prometheus and Grafana are no longer controlled by the `enablePrometheus` field in the `monitoring-sample` object. See Using Prometheus and Grafana for details.

### Example: Adding application-level metrics to a Grafana dashboard

The following sections walk you through adding metrics for an application. In this section, you complete the following tasks:

  * Deploy an example application that exposes a metric called `foo`.
  * Verify that Prometheus exposes and scrapes the metric.
  * Create a custom Grafana dashboard.



### Deploy the example application

The example application runs in a single Pod. The Pod's container exposes a metric, `foo`, with a constant value of `40`.

Create the following Pod manifest, `pro-pod.yaml`:
    
    
    apiVersion: v1
    kind: Pod
    metadata:
      name: prometheus-example
      annotations:
        prometheus.io/scrape: 'true'
        prometheus.io/port: '8080'
        prometheus.io/path: '/metrics'
    spec:
      containers:
      - image: registry.k8s.io/prometheus-dummy-exporter:v0.1.0
        name: prometheus-example
        command:
        - /bin/sh
        - -c
        - ./prometheus_dummy_exporter --metric-name=foo --metric-value=40 --port=8080
    

Then apply the Pod manifest to your user cluster:
    
    
    kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] apply -f pro-pod.yaml
    

### Verify that the metric is exposed and scraped

  1. The container in the `prometheus-example` pod listens on TCP port 8080. Forward a local port to port 8080 in the Pod:
         
         kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] port-forward prometheus-example 50002:8080

  2. To verify that the application exposes the metric, run the following command:
         
         curl localhost:50002/metrics | grep foo
         

The command returns the following output:
         
         # HELP foo Custom metric
         # TYPE foo gauge
         foo 40

  3. The container in the `prometheus-0` Pod listens on TCP port 9090. Forward a local port to port 9090 in the Pod:
         
         kubectl --kubeconfig [USER_CLUSTER_KUBECONFIG] port-forward prometheus-0 50003:9090

  4. To verify that Prometheus is scraping the metric, navigate to http://localhost:50003/targets, which should take you to the `prometheus-0` Pod under the `prometheus-io-pods` target group.

  5. To view metrics in Prometheus, navigate to http://localhost:50003/graph. From the **search** field, enter `foo`, then click **Execute**. The page should display the metric.




## Known issue: Cloud Monitoring error condition

(Issue ID 159761921)

Under certain conditions, the default Cloud Monitoring pod, deployed by default in each new cluster, can become unresponsive. When clusters are upgraded, for example, storage data can become corrupted when pods in `statefulset/prometheus-stackdriver-k8s` are restarted.

Specifically, monitoring pod `stackdriver-prometheus-k8s-0` can be caught in a loop when corrupted data prevents `prometheus-stackdriver-sidecar` writing to the cluster storage `PersistentVolume`.

You can manually diagnose and recover the error following the steps below.

### Diagnose the Cloud Monitoring failure

When the monitoring pod has failed, the logs will report the following:

`{"log":"level=warn ts=2020-04-08T22:15:44.557Z caller=queue_manager.go:534 component=queue_manager msg=\"Unrecoverable error sending samples to remote storage\" err=\"rpc error: code = InvalidArgument desc = One or more TimeSeries could not be written: One or more points were written more frequently than the maximum sampling period configured for the metric.: timeSeries[0-114]; Unknown metric: kubernetes.io/anthos/scheduler_pending_pods: timeSeries[196-198]\"\n","stream":"stderr","time":"2020-04-08T22:15:44.558246866Z"}`

`{"log":"level=info ts=2020-04-08T22:15:44.656Z caller=queue_manager.go:229 component=queue_manager msg=\"Remote storage stopped.\"\n","stream":"stderr","time":"2020-04-08T22:15:44.656798666Z"}`

`{"log":"level=error ts=2020-04-08T22:15:44.663Z caller=main.go:603 err=\"corruption after 29032448 bytes: unexpected non-zero byte in padded page\"\n","stream":"stderr","time":"2020-04-08T22:15:44.663707748Z"}`

`{"log":"level=info ts=2020-04-08T22:15:44.663Z caller=main.go:605 msg=\"See you next time!\"\n","stream":"stderr","time":"2020-04-08T22:15:44.664000941Z"}`

### Recover from the Cloud Monitoring error

To recover Cloud Monitoring manually:

  1. Stop cluster monitoring. Scale down the `stackdriver` operator to prevent monitoring reconciliation: 
         
         kubectl --kubeconfig /ADMIN_CLUSTER_KUBCONFIG --namespace kube-system scale deployment stackdriver-operator --replicas 0

  2. Delete the monitoring pipeline workloads: 
         
         kubectl --kubeconfig /ADMIN_CLUSTER_KUBCONFIG --namespace kube-system delete statefulset stackdriver-prometheus-k8s

  3. Delete the monitoring pipeline PersistentVolumeClaims (PVCs): 
         
         kubectl --kubeconfig /ADMIN_CLUSTER_KUBCONFIG --namespace kube-system delete pvc -l app=stackdriver-prometheus-k8s

  4. Restart cluster monitoring. Scale up the stackdriver operator to reinstall a new monitoring pipeline and resume reconciliation: 
         
         kubectl --kubeconfig /ADMIN_CLUSTER_KUBCONFIG --namespace kube-system scale deployment stackdriver-operator --replicas=1




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
