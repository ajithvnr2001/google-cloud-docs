---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/log-monitoring/
title: Configure logging and monitoring \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:14:31.633295+00:00
---

# Configure logging and monitoring  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/log-monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Configure logging and monitoring Stay organized with collections  Save and categorize content based on your preferences. 

Distributed Cloud software only for bare metal supports multiple options for cluster logging and monitoring, including cloud-based managed services, open source tools, and validated compatibility with third-party commercial solutions. This page explains these options and provides basic guidance on selecting the right solution for your environment.

This page is for Admins and architects and Operators who want to monitor the health of deployed applications or services, such as for service level objective (SLO) compliance. To learn more about common roles and example tasks that are referenced in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

## Options for Google Distributed Cloud

You have several logging and monitoring options for your cluster:

  * Cloud Logging and Cloud Monitoring, enabled by default on bare metal system components.
  * Prometheus and Grafana are available from the Cloud Marketplace.
  * Validated configurations with third-party solutions.



### Cloud Logging and Cloud Monitoring

Google Cloud Observability is the built-in observability solution for Google Cloud. It offers a fully managed logging solution, metrics collection, monitoring, dashboarding, and alerting. Cloud Monitoring monitors Google Distributed Cloud clusters in a similar way as cloud-based GKE clusters.

Cloud Logging and Cloud Monitoring are enabled by default when you create clusters with the required service accounts and Identity and Access Management (IAM) roles. You can't disable Cloud Logging and Cloud Monitoring. For more information about service accounts and the required roles, see [Configure service accounts](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-sa#configuring-sa).

**Note:** The [GKE dashboards](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics) only display information for GKE clusters running on Google Cloud. They don't display information for Google Distributed Cloud.

The agents can be configured to change the following:

  * Scope of logging and monitoring, from only system components (the default) to both system components and applications.
  * Level of metrics collected, from only an optimized set of metrics (the default) to all metrics.



See Configure Stackdriver agents for Google Distributed Cloud on this document for more information.

Logging and Monitoring provide a single, easy-to-configure, powerful cloud-based observability solution. We highly recommend Logging and Monitoring when running workloads on Google Distributed Cloud. For applications with components running on Google Distributed Cloud and standard on-premises infrastructure, you might consider other solutions for an end-to-end view of those applications.

**Note:** We collect only cluster logs and system component metrics by default, with the option to enable application logging and monitoring.

  * For details about architecture, configuration, and what data is replicated to your Google Cloud project by default, see How Logging and Monitoring for Google Distributed Cloud works.

  * For more information about Logging, see the [Cloud Logging](https://docs.cloud.google.com/logging/docs) documentation.

  * For more information about Monitoring, see the [ Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) documentation.

  * To learn how to view and use Cloud Monitoring resource utilization metrics from Google Distributed Cloud at fleet level, see [Use the Google Kubernetes Engine overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/enterprise-overview-dashboard).




### Prometheus and Grafana

Prometheus and Grafana are two popular open source monitoring products available in the [Cloud Marketplace](https://console.cloud.google.com/marketplace/details/google/prometheus):

  * [Prometheus](https://prometheus.io/docs/introduction/overview/) collects application and system metrics.

  * [Alertmanager](https://prometheus.io/docs/alerting/alertmanager/) handles sending alerts with several different alerting mechanisms.

  * [Grafana](https://grafana.com/docs/) is a dashboarding tool.




We recommend that you use Google Cloud Managed Service for Prometheus, which is based in Cloud Monitoring, for all your monitoring needs. With Google Cloud Managed Service for Prometheus you can monitor [system components](https://docs.cloud.google.com/monitoring/api/metrics_kubernetes) without charge. Google Cloud Managed Service for Prometheus is also compatible with Grafana. However, if you prefer a pure local monitoring system, you can choose to install Prometheus and Grafana in your clusters.

If you installed Prometheus locally and want to collect metrics from system components, you need to give permission to your local Prometheus instance to access the metrics endpoints of system components:

  * Bind the service account for your Prometheus instance to the predefined `gke-metrics-agent` ClusterRole, and use service account token as credential to scrape metrics from the following system components:

    * `kube-apiserver`
    * `kube-scheduler`
    * `kube-controller-manager`
    * `kubelet`
    * `node-exporter`
  * Use the client key and cert stored in the `kube-system/stackdriver-prometheus-etcd-scrape` secret to authenticate the metric scrape from etcd.

  * Create a NetworkPolicy to allow access from your namespace to kube-state-metrics.




### Third-party solutions

Google has worked with several third-party logging and monitoring solution providers to help their products work well with Google Distributed Cloud. These include Datadog, Elastic, and Splunk. Additional validated third parties will be added in the future.

The following solution guides are available for using third-party solutions with Google Distributed Cloud:

  * [Monitoring Google Distributed Cloud with the Elastic Stack](https://docs.cloud.google.com/solutions/partners/monitoring-gke-on-prem-with-the-elastic-stack)
  * [Collect logs on Google Distributed Cloud with Splunk Connect](https://docs.cloud.google.com/solutions/logging-anthos-with-splunk-connect)



## How Logging and Monitoring for Google Distributed Cloud works

Cloud Logging and Cloud Monitoring are installed and activated in each cluster when you create a new admin or user cluster.

The Stackdriver agents include several components on each cluster:

  * **Stackdriver Operator** (`stackdriver-operator-*`). Manages the lifecycle for all other Stackdriver agents deployed onto the cluster.

  * **Stackdriver Custom Resource.** A resource that is automatically created as part of the Google Distributed Cloud installation process.

  * **GKE Metrics Agent** (`gke-metrics-agent-*`). An OpenTelemetry Collector based DaemonSet that scrapes metrics from each node to Cloud Monitoring. A `node-exporter` DaemonSet and a `kube-state-metrics` deployment are also included to provide more metrics about the cluster.

  * **Stackdriver Log Forwarder** (`stackdriver-log-forwarder-*`). A Fluent Bit DaemonSet that forwards logs from each machine to the Cloud Logging. The log Forwarder buffers the log entries on the node locally and re-sends them for up to 4 hours. If the buffer gets full or if the Log Forwarder can't reach the Cloud Logging API for more than 4 hours, logs are dropped.

**Note:** The Metadata Agent is available for Preview and is covered by the [Pre-GA Offerings Terms](https://cloud.google.com/terms/service-terms#1) of the Google Cloud Terms of Service. Pre-GA products may have limited support, and changes to pre-GA products may not be compatible with other pre-GA versions. For more information, see the [launch stage descriptions](https://cloud.google.com/products#product-launch-stages).
  * **Metadata Agent** (`stackdriver-metadata-agent-`). A deployment that sends metadata for Kubernetes resources such as pods, deployments, or nodes to the Config Monitoring for Ops API. This addition of metadata lets you query your metrics data by deployment name, node name, or even Kubernetes service name.




You can see the agents installed by Stackdriver by running the following command:
    
    
    kubectl -n kube-system get pods -l "managed-by=stackdriver"
    

The output of this command is similar to the following:
    
    
    kube-system   gke-metrics-agent-4th8r                                     1/1     Running   1 (40h ago)   40h
    kube-system   gke-metrics-agent-8lt4s                                     1/1     Running   1 (40h ago)   40h
    kube-system   gke-metrics-agent-dhxld                                     1/1     Running   1 (40h ago)   40h
    kube-system   gke-metrics-agent-lbkl2                                     1/1     Running   1 (40h ago)   40h
    kube-system   gke-metrics-agent-pblfk                                     1/1     Running   1 (40h ago)   40h
    kube-system   gke-metrics-agent-qfwft                                     1/1     Running   1 (40h ago)   40h
    kube-system   kube-state-metrics-9948b86dd-6chhh                          1/1     Running   1 (40h ago)   40h
    kube-system   node-exporter-5s4pg                                         1/1     Running   1 (40h ago)   40h
    kube-system   node-exporter-d9gwv                                         1/1     Running   2 (40h ago)   40h
    kube-system   node-exporter-fhbql                                         1/1     Running   1 (40h ago)   40h
    kube-system   node-exporter-gzf8t                                         1/1     Running   1 (40h ago)   40h
    kube-system   node-exporter-tsrpp                                         1/1     Running   1 (40h ago)   40h
    kube-system   node-exporter-xzww7                                         1/1     Running   1 (40h ago)   40h
    kube-system   stackdriver-log-forwarder-8lwxh                             1/1     Running   1 (40h ago)   40h
    kube-system   stackdriver-log-forwarder-f7cgf                             1/1     Running   2 (40h ago)   40h
    kube-system   stackdriver-log-forwarder-fl5gf                             1/1     Running   1 (40h ago)   40h
    kube-system   stackdriver-log-forwarder-q5lq8                             1/1     Running   2 (40h ago)   40h
    kube-system   stackdriver-log-forwarder-www4b                             1/1     Running   1 (40h ago)   40h
    kube-system   stackdriver-log-forwarder-xqgjc                             1/1     Running   1 (40h ago)   40h
    kube-system   stackdriver-metadata-agent-cluster-level-5bb5b6d6bc-z9rx7   1/1     Running   1 (40h ago)   40h
    

### Configuration requirements for Logging and Monitoring

There are several configuration requirements to enable Cloud Logging and Cloud Monitoring with Google Distributed Cloud. These steps are included in [Configuring a service account for use with Logging and Monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/configure-sa#logmon-config-sa) on the Enabling Google services page, and in the following list:

  1. A Cloud Monitoring Workspace must be created within the Google Cloud project. This is accomplished by clicking **Monitoring** in Google Cloud console and following the workflow.
  2. You need to enable the following Stackdriver APIs:

     * [Stackdriver API](https://console.cloud.google.com/apis/api/stackdriver.googleapis.com/overview)
     * [Cloud Monitoring API](https://console.cloud.google.com/apis/api/monitoring.googleapis.com/overview)
     * [Cloud Logging API](https://console.cloud.google.com/apis/api/logging.googleapis.com/overview)
     * [Config Monitoring for Ops API](https://console.cloud.google.com/apis/api/opsconfigmonitoring.googleapis.com/overview)
  3. You need to assign the following IAM roles to the service account used by the Stackdriver agents:

     * `logging.logWriter`
     * `monitoring.metricWriter`
     * `stackdriver.resourceMetadata.writer`
     * `monitoring.dashboardEditor`
     * `opsconfigmonitoring.resourceMetadata.writer`



### Logs and metrics routing

Stackdriver log forwarder (`stackdriver-log-forwarder`) sends logs from each node machine to Cloud Logging. Similarly, GKE metrics agent (`gke-metrics-agent`) sends metrics from each node machine to Cloud Monitoring. Before the logs and metrics are sent, the Stackdriver Operator (`stackdriver-operator`) attaches the value from the `clusterLocation` field in the `stackdriver` custom resource to each log entry and metric before they're routed to Google Cloud. Additionally, the logs and metrics are associated with the Google Cloud project specified in the `stackdriver` custom resource spec (`spec.projectID`).

All metrics and log entries sent by stackdriver agents are routed to a global ingestion endpoint. From there, the data is forwarded to the closest reachable regional Google Cloud endpoint to ensure the reliability of the data transport.

After the global endpoint receives the metric or log entry, what happens next is service-dependent:

  * **How logs routing is configured** : when the logging endpoint receives a log message, Cloud Logging passes the message through the Log Router. The sinks and filters in the Log Router configuration determine how to route the message. You can route log entries to destinations like regional Logging buckets, which store the log entry, or to Pub/Sub. For more information about how log routing works and how to configure it, see [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview).

Neither the `clusterLocation` field in the `stackdriver` custom resource or the `clusterOperations.location` field in the Cluster spec are considered in this routing process. For logs, `clusterLocation` is used to label log entries only, which can be helpful for filtering in Logs Explorer.

  * **How metrics routing is configured** : when the metrics endpoint receives a metric entry, the entry is routed automatically to be stored in the location specified by the metric. The location in the metric came from the `clusterLocation` field in the `stackdriver` custom resource.

  * **Plan your configuration** : when you configure your Cloud Logging and Cloud Monitoring, configure Log Router and specify an appropriate `clusterLocation` with locations that best support your needs. For example, if you want logs and metrics to go to the same location, set `clusterLocation` to the same Google Cloud region that Log Router is using for your Google Cloud project.

  * **Update your configuration when needed** : you can make changes anytime to the destination settings for logs and metrics due to business requirements, such as disaster recovery plans. Changes to the Log Router configuration in Google Cloud take effect quickly. The `location` and `projectID` fields in the `clusterOperations` section of the Cluster resource are immutable, so they can't be updated after you create your cluster. We don't recommend that you change values in the `stackdriver` resource directly. This resource is reverted to the original cluster creation state whenever a cluster operation, such as an upgrade, triggers a reconciliation.


The `stackdriver` resource gets values for the `clusterLocation` and `projectID` fields from the [`location`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#clusteroperations-location) and [`projectID`](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/cluster-config-ref#clusteroperations-projectid) fields in the `clusterOperations` section of the Cluster resource at cluster creation time. 

#### Cloud Monitoring metrics

For a list of metrics collected by Cloud Monitoring, see [View Google Distributed Cloud metrics](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/metrics-anthos).

#### Metrics Server

[Metrics Server](https://github.com/kubernetes-sigs/metrics-server) is the source of the container resource metrics for various autoscaling pipelines. Metrics Server retrieves metrics from kubelets and exposes them through the Kubernetes Metrics API. HPA and VPA then use these metrics to determine when to trigger autoscaling. Metrics server is scaled using addon- resizer.

In extreme cases where high pod density creates too much logging and monitoring overhead, Metrics Server might be stopped and restarted due to resource limitations. In this case, you can allocate more resources to metrics server by editing the `metrics-server-config` configmap in gke-managed-metrics-server namespace, and changing the value for `cpuPerNode` and `memoryPerNode`.
    
    
    kubectl edit cm metrics-server-config -n gke-managed-metrics-server
    

The example content of the ConfigMap is:
    
    
    apiVersion: v1
    data:
      NannyConfiguration: |-
        apiVersion: nannyconfig/v1alpha1
        kind: NannyConfiguration
        cpuPerNode: 3m
        memoryPerNode: 20Mi
    kind: ConfigMap
    

**Note:** Only `cpuPerNode` and `memoryPerNode` need to be modified. Changing `baseCPU` and `baseMemory` is not recommended.

After updating the ConfigMap, recreate the metrics-server pods with the following command:
    
    
    kubectl delete pod -l k8s-app=metrics-server -n gke-managed-metrics-server
    

**Note:** The edit on `metrics-server-config` may be reverted during a cluster update or upgrade. See the [known issue](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/troubleshooting/known-issues#metrsrv-conf-revert) section for more information.

## Configure the Stackdriver custom resource

When you create a cluster, Google Distributed Cloud [automatically creates](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/log-monitoring#stackdriver_gkeop) a Stackdriver custom resource. You can edit the spec in the custom resource to override the default values for CPU and memory requests and limits for a Stackdriver component, and you can separately override the default storage size and storage class.

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

By default, the metrics agents running in the cluster collect and report an optimized set of container, kubelet and kube-state-metrics metrics to Google Cloud Observability (formerly Stackdriver). If you require additional metrics, we recommend that you find a replacement from the list of [Google Distributed Cloud metrics](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/metrics-anthos).

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




### Configure Stackdriver agents for Google Distributed Cloud

The Stackdriver agents installed with Google Distributed Cloud collect data about system components for the purposes of maintaining and troubleshooting issues with your clusters. The following sections describe Stackdriver configuration and operating modes.

#### System Components Only (Default Mode)

Upon installation, Stackdriver agents are configured by default to collect logs and metrics, including performance details (for example, CPU and memory utilization), and similar metadata, for Google-provided system components. These include all workloads in the admin cluster, and for user clusters, workloads in the kube-system, gke-system, gke-connect, istio-system, and config-management- system namespaces.

#### System Components and Applications

To enable application logging and monitoring on top of the default mode, follow the steps in [Enable application logging and monitoring](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/application-logging-monitoring).

#### Optimized metrics (Default metrics)

By default, the `kube-state-metrics` deployments running in the cluster collect and report an optimized set of kube metrics to Google Cloud Observability (formerly Stackdriver).

Fewer resources are needed to collect this optimized set of metrics, which improves overall performance and scalability.

##### Excluded kube metrics

The following kube metrics are excluded from the optimized metrics:

  * kube_certificatesigningrequest_cert_length
  * kube_certificatesigningrequest_condition
  * kube_certificatesigningrequest_created
  * kube_certificatesigningrequest_labels
  * kube_configmap_annotations
  * kube_configmap_info
  * kube_configmap_labels
  * kube_configmap_metadata_resource_version
  * kube_daemonset_annotations
  * kube_daemonset_created
  * kube_daemonset_labels
  * kube_daemonset_metadata_generation
  * kube_daemonset_status_observed_generation
  * kube_deployment_annotations
  * kube_deployment_created
  * kube_deployment_labels
  * kube_deployment_spec_paused
  * kube_deployment_spec_strategy_rollingupdate_max_surge
  * kube_deployment_spec_strategy_rollingupdate_max_unavailable
  * kube_deployment_status_condition
  * kube_deployment_status_replicas_ready
  * kube_endpoint_annotations
  * kube_endpoint_created
  * kube_endpoint_info
  * kube_endpoint_labels
  * kube_endpoint_ports
  * kube_horizontalpodautoscaler_annotations
  * kube_horizontalpodautoscaler_info
  * kube_horizontalpodautoscaler_labels
  * kube_horizontalpodautoscaler_metadata_generation
  * kube_horizontalpodautoscaler_status_condition
  * kube_job_annotations
  * kube_job_complete
  * kube_job_created
  * kube_job_info
  * kube_job_labels
  * kube_job_owner
  * kube_job_spec_completions
  * kube_job_spec_parallelism
  * kube_job_status_completion_time
  * kube_job_status_start_time
  * kube_job_status_succeeded
  * kube_lease_owner
  * kube_lease_renew_time
  * kube_limitrange
  * kube_limitrange_created
  * kube_mutatingwebhookconfiguration_info
  * kube_namespace_labels
  * kube_networkpolicy_annotations
  * kube_networkpolicy_labels
  * kube_networkpolicy_spec_egress_rules
  * kube_networkpolicy_spec_ingress_rules
  * kube_node_annotations
  * kube_node_role
  * kube_persistentvolume_annotations
  * kube_persistentvolume_labels
  * kube_persistentvolumeclaim_access_mode
  * kube_persistentvolumeclaim_annotations
  * kube_persistentvolumeclaim_labels
  * kube_pod_annotations
  * kube_pod_completion_time
  * kube_pod_container_resource_limits
  * kube_pod_container_resource_requests
  * kube_pod_container_state_started
  * kube_pod_created
  * kube_pod_init_container_info
  * kube_pod_init_container_resource_limits
  * kube_pod_init_container_resource_requests
  * kube_pod_init_container_status_last_terminated_reason
  * kube_pod_init_container_status_ready
  * kube_pod_init_container_status_restarts_total
  * kube_pod_init_container_status_running
  * kube_pod_init_container_status_terminated
  * kube_pod_init_container_status_terminated_reason
  * kube_pod_init_container_status_waiting
  * kube_pod_init_container_status_waiting_reason
  * kube_pod_labels
  * kube_pod_owner
  * kube_pod_restart_policy
  * kube_pod_spec_volumes_persistentvolumeclaims_readonly
  * kube_pod_start_time
  * kube_poddisruptionbudget_annotations
  * kube_poddisruptionbudget_created
  * kube_poddisruptionbudget_labels
  * kube_poddisruptionbudget_status_expected_pods
  * kube_poddisruptionbudget_status_observed_generation
  * kube_poddisruptionbudget_status_pod_disruptions_allowed
  * kube_replicaset_annotations
  * kube_replicaset_created
  * kube_replicaset_labels
  * kube_replicaset_metadata_generation
  * kube_replicaset_owner
  * kube_replicaset_status_observed_generation
  * kube_resourcequota_created
  * kube_secret_annotations
  * kube_secret_info
  * kube_secret_labels
  * kube_secret_metadata_resource_version
  * kube_secret_type
  * kube_service_annotations
  * kube_service_created
  * kube_service_info
  * kube_service_labels
  * kube_service_spec_type
  * kube_statefulset_annotations
  * kube_statefulset_created
  * kube_statefulset_labels
  * kube_statefulset_status_current_revision
  * kube_statefulset_status_update_revision
  * kube_storageclass_annotations
  * kube_storageclass_created
  * kube_storageclass_info
  * kube_storageclass_labels
  * kube_validatingwebhookconfiguration_info
  * kube_validatingwebhookconfiguration_metadata_resource_version
  * kube_volumeattachment_created
  * kube_volumeattachment_info
  * kube_volumeattachment_labels
  * kube_volumeattachment_spec_source_persistentvolume
  * kube_volumeattachment_status_attached
  * kube_volumeattachment_status_attachment_metadata



The complete set of Google Distributed Cloud metrics is documented in [View Anthos metrics](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/metrics-anthos).

To disable optimized metrics (not recommended), override the default setting in your Stackdriver custom resource.

## Use Google Cloud Managed Service for Prometheus

Google Cloud Managed Service for Prometheus is part of Cloud Monitoring and is available as an option for system components. The benefits of Google Cloud Managed Service for Prometheus include the following:

  * You can continue to use your existing Prometheus-based monitoring without altering your alerts and Grafana dashboards.

  * If you use both GKE and Google Distributed Cloud, you can use the same [Prometheus Query Language (PromQL)](https://prometheus.io/docs/prometheus/latest/querying/basics/) for metrics on all your clusters. You can also use the **PromQL** tab in [Metrics Explorer](https://console.cloud.google.com/monitoring/metrics-explorer) in the Google Cloud console.




### Enable and disable Google Cloud Managed Service for Prometheus

Starting with Google Distributed Cloud release 1.30.0-gke.1930, Google Cloud Managed Service for Prometheus is always enabled. In earlier versions, you can edit the Stackdriver resource, `stackdriver`, to enable or disable Google Cloud Managed Service for Prometheus. To disable Google Cloud Managed Service for Prometheus for cluster versions prior to 1.30.0-gke.1930, set `spec.featureGates.enableGMPForSystemMetrics` in the `stackdriver` resource to `false`.

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
    

### Configure Grafana dashboards with Google Cloud Managed Service for Prometheus

To use Grafana with metrics data from Google Cloud Managed Service for Prometheus, follow the steps in [Query using Grafana](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus/query) to authenticate and configure a Grafana data source to query data from Google Cloud Managed Service for Prometheus.

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

For more information about Google Cloud Managed Service for Prometheus, see the following:

  * [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus)

  * [GKE control plane metrics are PromQL compatible](https://cloud.google.com/blog/products/containers-kubernetes/kubernetes-control-plane-metrics-are-generally-available)

  * [Using Google Cloud Managed Service for Prometheus for user applications on Google Distributed Cloud](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/application-logging-monitoring#enable_managed_service_for_prometheus)




### Log tags

Many Google Distributed Cloud logs have an `F` tag:
    
    
    logtag: "F"
    

This tag means that the log entry is complete or _full_. To learn more about this tag, see [Log format](https://github.com/kubernetes/design-proposals-archive/blob/main/node/kubelet-cri-logging.md#proposed-solution) in the Kubernetes design proposals on GitHub.

### Pricing

In a Google Distributed Cloud cluster, system logs and metrics include the following:

  * Logs and metrics from all components in an admin cluster.
  * Logs and metrics from components in these namespaces in a user cluster: `kube-system`, `gke-system`, `gke-connect`, `knative-serving`, `istio-system`, `monitoring-system`, `config-management-system`, `gatekeeper-system`, `cnrm-system`.



For more information, see [Pricing for Google Cloud Observability](https://cloud.google.com/stackdriver/pricing).

To learn about credit for Cloud Logging metrics, [contact sales for pricing](https://cloud.google.com/contact/?form=anthos).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
