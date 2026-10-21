---
url: https://docs.cloud.google.com/monitoring/dashboards/event-types/
title: Event types \u00a0|\u00a0 Cloud Monitoring \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:43:57.664629+00:00
---

# Event types  |  Cloud Monitoring  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/monitoring/dashboards/event-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Monitoring ](https://docs.cloud.google.com/monitoring/docs)
  * [ Guides ](https://docs.cloud.google.com/monitoring/docs/monitoring-overview)



Send feedback 

#  Event types Stay organized with collections  Save and categorize content based on your preferences. 

Event annotations on charts in Cloud Monitoring let you correlate metric trends with system activities, such as deployments, failovers, or crashes. An _event_ is an activity that affects the operation of a system and is identified from open alerts, Personalized Service Health, or log entries. Dashboards can display multiple annotations, and each annotation can list multiple events. The **Observability** tabs for services such as Compute Engine and Google Kubernetes Engine can also display annotations, but not all event types are supported.

For each listed event type, this document includes links to troubleshooting content and log queries that you can use in the Logs Explorer or in a [log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert). For setup instructions, see [Show events on a dashboard](https://docs.cloud.google.com/monitoring/dashboards/show-events).

## Example of a dashboard with annotations

The following screenshot illustrates a chart that shows several log-based events and one Service Health event:

![Chart showing warning and informational event annotations.](https://docs.cloud.google.com/static/monitoring/images/dashboard-show-warn-info-events.png)

## Alert event types

This section describes the alert event types that can be shown on a dashboard.

### Alert opened

Alert opened events help you correlate your charted data to when [alerts](https://docs.cloud.google.com/monitoring/alerts/incidents-events) opened. An alert opened event is shown when the following are true:

  * The corresponding alert was opened during the time range specified by the dashboard.
  * The corresponding alert isn't closed.



Alerts that were opened outside the time range specified by the dashboard aren't shown. Similarly, an alert opened event isn't shown when the corresponding alert was opened and then closed within the time range specified by the dashboard.

The tooltip for an alert opened event includes the following:

  * Name of the alerting policy.
  * Summary information, when this information is available. For example, this information might include the threshold and the measured value.
  * The duration of the alert, and the date and time when the alert was opened.
  * Metric and resource labels. The tooltip might not show all labels.
  * A **View** button, which opens the **Details** page for the alert.



## Google Kubernetes Engine event types

This section describes the Google Kubernetes Engine event types that can be shown on a dashboard.

### Patched or updated GKE workload

This event type helps you troubleshoot GKE workload deployment or statefulset changes, as these events can correlate with performance regressions or other performance issues. This event type is shown when a workload is created, updated, or deleted.

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    log_id(cloudaudit.googleapis.com%2Factivity)
    resource.type=k8s_cluster protoPayload.methodName=(
        io.k8s.apps.v1.deployments.create OR io.k8s.apps.v1.deployments.patch OR
        io.k8s.apps.v1.deployments.update OR io.k8s.apps.v1.deployments.delete OR
        io.k8s.apps.v1.statefulsets.create OR io.k8s.apps.v1.statefulsets.patch OR
        io.k8s.apps.v1.statefulsets.update OR io.k8s.apps.v1.statefulsets.delete OR
        io.k8s.apps.v1.daemonsets.create OR io.k8s.apps.v1.daemonsets.patch OR
        io.k8s.apps.v1.daemonsets.update OR io.k8s.apps.v1.daemonsets.delete
    )
    -protoPayload.authenticationInfo.principalEmail=("system:addon-manager" OR "system:serviceaccount:kube-system:namespace-controller")
    -protoPayload.request.metadata.namespace=(kube-system OR gmp-system OR gmp-public OR gke-gmp-system OR istio-system)
    -protoPayload.response.metadata.namespace=(kube-system OR gmp-system OR gmp-public OR gke-gmp-system OR istio-system)
    -protoPayload.resourceName=~"namespaces/(kube-system|gmp-system|gmp-public|gke-gmp-system|istio-system)"
    
    

For additional information, see [Overview of deploying workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploying-workloads-overview) and [View observability metrics](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-observability-metrics).

### Crash of a GKE pod

This event type helps you identify and troubleshoot GKE pod crashes. Pod crashes can be caused by memory exhaustion or an application error. This event type is shown when any of the following occur:

  * Pod status is `CrashLoopBackOff`.
  * Pod terminates with a non-zero exit code.
  * Pod terminates with an out-of-memory condition.
  * Pod is evicted.
  * Readiness or liveness probe fails.



If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    (
        log_id(events)
        (
            (resource.type=k8s_pod jsonPayload.reason=(BackOff OR Unhealthy OR Killing OR Evicted)) OR
            (resource.type=k8s_node jsonPayload.reason=OOMKilling)
        )
        severity=WARNING
    ) OR (
        log_id(cloudaudit.googleapis.com%2Factivity) resource.type=k8s_cluster
        (protoPayload.methodName=io.k8s.core.v1.pods.eviction.create OR
            (protoPayload.methodName=io.k8s.core.v1.pods.delete
            protoPayload.response.status.containerStatuses.state.terminated.exitCode:*
            -protoPayload.response.status.containerStatuses.state.terminated.exitCode=0
            )
        )
    )
    

For troubleshooting information, see [Troubleshoot: CrashLoopBackOff](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting#CrashLoopBackOff).

### Failure to schedule a GKE pod

This event type helps you identify and troubleshoot pods that can't be scheduled on a node. This event type is shown when pod scheduling fails for any of the following reasons:

  * Insufficient node CPU.
  * Insufficient node memory.
  * No nodes for taints or tolerations.
  * Nodes at the maximum pod limit.
  * Node pool at maximum size.



If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    (
        log_id(events) resource.type=k8s_pod jsonPayload.reason=(NotTriggerScaleUp OR FailedScheduling)
    ) OR (
        log_id(container.googleapis.com/cluster-autoscaler-visibility)
        resource.type=k8s_cluster jsonPayload.noDecisionStatus.noScaleUp:*
    )
    
    

For troubleshooting information, see [Troubleshoot: Pod unschedulable](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting#PodUnschedulable).

### Failure to create a GKE container

This event type helps you identify and troubleshoot failures to create a GKE container. Container creation might fail due to reasons such as failed volume mounts or failed image pulls.

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    log_id(events) resource.type=k8s_pod jsonPayload.reason=(Failed OR FailedMount) severity=WARNING
    

For troubleshooting information about image pulls, see [Troubleshoot image pulls](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/image-pulls).

### Pod autoscaler scale up and down

This event gives you visibility into Horizontal Pod Autoscaler rescales, which increase or decrease the number of running pods for a workload. For more information, see [Horizontal Pod autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/horizontalpodautoscaler).

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    resource.type=k8s_cluster log_id(events)
    jsonPayload.involvedObject.kind=HorizontalPodAutoscaler jsonPayload.reason=SuccessfulRescale
    

### Cluster autoscaler scale up and down

This event gives you visibility into when the cluster autoscaler scales up or down the number of nodes in a node pool of your cluster. For more information, see [About cluster autoscaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-autoscaler) and [Viewing cluster autoscaler events](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler-visibility).

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    (resource.type=k8s_cluster log_id(container.googleapis.com%2Fcluster-autoscaler-visibility)
    jsonPayload.decision:*)
    

### Cluster create and delete

This event tracks GKE cluster creation and deletion actions. For more information, see [Create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster), [Creating a zonal cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster), and [Deleting a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deleting-a-cluster).

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    resource.type=gke_cluster log_id(cloudaudit.googleapis.com%2Factivity)
    protoPayload.methodName=(
        google.container.v1alpha1.ClusterManager.CreateCluster OR
        google.container.v1beta1.ClusterManager.CreateCluster OR
        google.container.v1.ClusterManager.CreateCluster OR
        google.container.v1alpha1.ClusterManager.DeleteCluster OR
        google.container.v1beta1.ClusterManager.DeleteCluster OR
        google.container.v1.ClusterManager.DeleteCluster
    )
    operation.first=true
    

### Cluster update

This event tracks GKE cluster updates. Updates include automatic control plane version upgrades as well as manual upgrades and cluster configuration changes. For more information, see [Manually upgrading a cluster or node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) and [Standard cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades).

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    resource.type=gke_cluster log_id(cloudaudit.googleapis.com%2Factivity)
    (
        protoPayload.methodName=(
            google.container.internal.ClusterManagerInternal.PatchCluster OR
            google.container.internal.ClusterManagerInternal.UpdateClusterInternal OR
            google.container.internal.ClusterManagerInternal.UpdateCluster
        )
    ) OR (
        protoPayload.methodName=(
            google.container.v1beta1.ClusterManager.UpdateCluster OR
            google.container.v1.ClusterManager.UpdateCluster
        )
        operation.first=true
    )
    protoPayload.metadata.operationType=(UPGRADE_MASTER OR REPAIR_CLUSTER OR UPDATE_CLUSTER)
    

### Node pool update

This event tracks GKE node pool updates. Updates include automatic node pool version upgrades as well as manual upgrades, configuration changes, and resizes. For more information, see [Manually upgrading a cluster or node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) and [Standard cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades).

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    resource.type=gke_nodepool log_id(cloudaudit.googleapis.com%2Factivity)
    (
        protoPayload.methodName=(
            google.container.internal.ClusterManagerInternal.UpdateClusterInternal OR
            google.container.internal.ClusterManagerInternal.RepairNodePool
        )
    ) OR (
        protoPayload.methodName=(
            google.container.v1beta1.ClusterManager.UpdateNodePool OR
            google.container.v1.ClusterManager.UpdateNodePool OR
            google.container.v1beta1.ClusterManager.SetNodePoolSize OR
            google.container.v1.ClusterManager.SetNodePoolSize OR
            google.container.v1beta1.ClusterManager.SetNodePoolManagement OR
            google.container.v1.ClusterManager.SetNodePoolManagement OR
            google.container.v1beta1.ClusterManager.SetNodePoolAutoscaling OR
            google.container.v1.ClusterManager.SetNodePoolAutoscaling
        )
        operation.first=true
    )
    

## Cloud Run event types

This section describes the Cloud Run event types that can be shown on a dashboard.

### Cloud Run deployment

This event type helps you identify and troubleshoot Cloud Run deployment failures. Deployment might fail due to reasons such as a deleted service account, incorrect permissions, a failed container import, or a container that failed to start.

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    log_id(cloudaudit.googleapis.com%2Factivity) resource.type=cloud_run_revision
    protoPayload.methodName=google.cloud.run.v1.Services.ReplaceService
    

For troubleshooting information, see [Troubleshoot: Cloud Run issues](https://docs.cloud.google.com/run/docs/troubleshooting#deployment).

## Cloud SQL event types

This section describes the Cloud SQL event types that can be shown on a dashboard.

### Cloud SQL failover

This event type helps you identify when manual or automatic failovers occur. A _failover_ occurs when there is an instance or zone failure and the standby instance becomes the new primary instance. During a failover, Cloud SQL automatically switches to serving data from the standby instance.

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    resource.type=cloudsql_database
    (
        (
            log_id(cloudaudit.googleapis.com%2Factivity)
            protoPayload.methodName=cloudsql.instances.failover
            operation.last=true
        ) OR (
            log_id(cloudaudit.googleapis.com%2Fsystem_event)
            protoPayload.methodName=cloudsql.instances.autoFailover
        )
    )
    

For additional information, see [About high availability](https://docs.cloud.google.com/sql/docs/mysql/high-availability).

### Cloud SQL start or stop

This event type helps you identify when a Cloud SQL instance has been manually started, stopped, or restarted. When an instance is stopped, all connections, open files, and running operations are also stopped.

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    log_id(cloudaudit.googleapis.com%2Factivity) resource.type=cloudsql_database
    protoPayload.methodName=cloudsql.instances.update operation.last=true
    protoPayload.metadata.intents.intent=(START_INSTANCE OR STOP_INSTANCE)
    

For additional information, see [About high availability](https://docs.cloud.google.com/sql/docs/mysql/high-availability) and [Start, stop, and restart instances](https://docs.cloud.google.com/sql/docs/mysql/start-stop-restart-instance).

### Cloud SQL storage

This event type helps you identify events related to Cloud SQL storage, including when database storage is full, and when a database is shut down due to reaching storage capacity. Databases at storage capacity and without automatic storage enabled might be shut down to prevent data corruption.

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    resource.type=cloudsql_database
    (
        (
            (log_id(cloudsql.googleapis.com%2Fpostgres.log) OR log_id(cloudsql.googleapis.com%2Fmysql.err))
            textPayload=~"No space left on device"
            severity=(ERROR OR EMERGENCY)
        ) OR (
            log_id(cloudaudit.googleapis.com%2Fsystem_event)
            protoPayload.methodName=cloudsql.instances.databaseShutdownOutOfStorage
        )
    )
    

## Cloud Interconnect event types

This section describes the Cloud Interconnect event types that can be shown on a dashboard.

### Interconnect maintenance started

This event type tracks the start of infrastructure maintenance for an interconnect. For the duration of the maintenance event, Border Gateway Protocol (BGP) sessions on virtual local area network (VLAN) attachments go down.

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    log_id("maintenance.googleapis.com/maintenance_events")
    jsonPayload.resource.type="compute.googleapis.com/Interconnect"
    jsonPayload.state="RUNNING"
    labels."maintenance.googleapis.com/updated_fields" : "state"
    

For more information, see [Infrastructure maintenance events](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/infrastructure-maintenance-events).

### Interconnect maintenance completed

This event type tracks the end of infrastructure maintenance for an interconnect. The Ethernet MAC addresses of the edge device can change after certain maintenance events.

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    log_id("maintenance.googleapis.com/maintenance_events")
    jsonPayload.resource.type="compute.googleapis.com/Interconnect"
    jsonPayload.state="SUCCEEDED"
    labels."maintenance.googleapis.com/updated_fields" : "state"
    

For more information, see [Infrastructure maintenance events](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/infrastructure-maintenance-events).

## Cloud VPN event types

This section describes the Cloud VPN event types that can be shown on a dashboard.

### VPN maintenance

This event type tracks infrastructure maintenance for a VPN task. This includes events for both maintenance started and maintenance completed.

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    log_id("cloud.googleapis.com/ipsec_events")
    resource.type="vpn_gateway"
    (
        textPayload:"Starting VPN task maintenance" OR
        textPayload:"VPN task maintenance Completed"
    )
    

### VPN traffic selectors narrowed

This event type helps identify when traffic selectors are narrowed for a Child SA. This includes events for both local and remote traffic selectors.

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    log_id("cloud.googleapis.com/ipsec_events")
    resource.type="vpn_gateway"
    (
        textPayload:"Warning: Local traffic selectors narrowed for Child SA" OR
        textPayload:"Warning: Remote traffic selectors narrowed for Child SA"
    )
    

## Compute Engine event types

This section describes the Compute Engine event types that can be shown on a dashboard.

### Virtual machine terminations

This event type helps you identify virtual machine (VM) terminations, including manually triggered resets and stops, guest OS terminations, maintenance terminations, and host errors.

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    resource.type=gce_instance
    (
        (
            log_id(cloudaudit.googleapis.com%2Factivity)
            protoPayload.methodName=(
                beta.compute.instances.reset OR v1.compute.instances.reset OR
                beta.compute.instances.stop OR v1.compute.instances.stop
            )
            operation.first=true
        ) OR (
            log_id(cloudaudit.googleapis.com%2Fsystem_event)
            protoPayload.methodName=(
                compute.instances.hostError OR
                compute.instances.guestTerminate OR
                compute.instances.terminateOnHostMaintenance
            )
        )
    )
    

For additional information, see [Stop and start a VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance) and [Troubleshooting VM shutdowns and reboots](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-reboots).

### VM instance start failure

This event tracks Compute Engine VM instance start failures. The event shows start failures due to stockouts, IP space exhaustion, quota exceeded, or shielded-VM integrity errors.

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    resource.type=gce_instance
    (
        (
            log_id(cloudaudit.googleapis.com%2Factivity)
            protoPayload.methodName=(beta.compute.instances.insert OR v1.compute.instances.insert)
            protoPayload.status.message=(ZONE_RESOURCE_POOL_EXHAUSTED OR IP_SPACE_EXHAUSTED OR QUOTA_EXCEEDED)
        ) OR (
            log_id(compute.googleapis.com%2Fshielded_vm_integrity)
            severity="ERROR"
        )
    )
    

### VM instance guest OS error

This event tracks specific Compute Engine VM instance Guest OS errors as recorded by the serial console logs. The errors tracked are full disks, failed file system mounts, and boot failures that activate Linux emergency mode.

For these events to be visible, you must enable serial port output logging to Cloud Logging by setting `serial-port-logging-enable=true` in the VM or in the project metadata. For more information, see [Enabling and disabling serial port output logging](https://docs.cloud.google.com/compute/docs/troubleshooting/viewing-serial-port-output#enable-stackdriver).

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    resource.type=gce_instance
    log_id(serialconsole.googleapis.com%2Fserial_port_1_output)
    textPayload=~("No space left on device" OR "Failed to mount" OR "You are in emergency mode")
    

### Managed instance group update

This event type helps you identify when your Managed Instance Group (MIG) has been updated. For example, VMs have been added or removed, or the size limit has been updated. For more information, see [Automatically apply VM configuration updates in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups).

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    resource.type=gce_instance_group_manager
    log_id(cloudaudit.googleapis.com%2Factivity) operation.first=true
    protoPayload.methodName=(beta.compute.instanceGroupManagers.patch OR v1.compute.instanceGroupManagers.patch)
    

For additional information, see [Work with managed instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances) and [Troubleshooting managed instance groups](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-migs).

### Managed instance group autoscaler

This event tracks scaling decisions made by the autoscaler of a MIG. These decisions could include changes in the recommended size for a MIG, or a change in the status of the autoscaler itself. For more information, see [Autoscaling groups of instances](https://docs.cloud.google.com/compute/docs/autoscaler).

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    resource.type=autoscaler log_id(cloudaudit.googleapis.com%2Fsystem_event)
    protoPayload.methodName=(compute.autoscalers.resize OR compute.autoscalers.changeStatus)
    

## Personalized Service Health event types

This section describes the Personalized Service Health event types that can be displayed on a dashboard.

**Note:** To display Personalized Service Health events, you must enable the Service Health API. For information about how to enable this API, see [Show events: Before you begin](https://docs.cloud.google.com/monitoring/dashboards/show-events#before_you_begin).

### Google Cloud incident

When you are troubleshooting, you might want to differentiate between failures caused by a service that you own and one caused by a Google Cloud service that you use. When you enable [Personalized Service Health](https://docs.cloud.google.com/service-health/docs/overview) annotations on a dashboard, you can view disruptions, or service health events, for Google Cloud services. For a list of services that are integrated with Service Health, see [Supported Google products](https://docs.cloud.google.com/service-health/docs/supported-products).

Unlike other event types, Google Cloud incidents aren't identified by analyzing your log entries. If you want to get notified when these events occur, then create an alerting policy. You can select a preconfigured alerting policy by using options on the **Service Health Dashboard** page. For more information, see [Quickstart: Set up an alert](https://docs.cloud.google.com/service-health/docs/configure-alerts-dashboard).

Monitoring identifies Google Cloud incidents by issuing a request to the Service Health API, and then filtering the response to those incidents that are relevant to the data you are viewing. The request has the following configuration:

  * The [`Relevance`](https://docs.cloud.google.com/service-health/docs/reference/rest/v1beta/projects.locations.events#Relevance) enumeration is set to `RELATED`, `IMPACTED`, or `PARTIALLY_RELATED`. This restriction ensures that your dashboard only displays events for the Google Cloud services that your Google Cloud project is using.

  * The [`DetailedState`](https://docs.cloud.google.com/service-health/docs/reference/rest/v1beta/projects.locations.events#detailedstate) enumeration isn't set to `FALSE_POSITIVE`.




Service Health annotations are displayed with a start time and a duration. The duration is displayed by changing the background color of the chart. The tooltip for a Google Cloud incident identifies the following:

  * The Google Cloud service.
  * Whether the incident is open or resolved.
  * Date and start time of the event.
  * Chips that display the number of affected products and locations. To list the affected products or locations, place your pointer on the corresponding chip.
  * A **View** button, which when selected opens the details page for the incident.



For information about how to issue a request to the Service Health API, see [Check for disruptions with Service Health](https://docs.cloud.google.com/service-health/docs/service-health-disruption).

For troubleshooting information, see [Troubleshoot common issues in Service Health](https://docs.cloud.google.com/service-health/docs/troubleshooting).

## Uptime check event types

This section describes the uptime check event types that can be shown on a dashboard.

**Note:** For these event types to be available, the uptime check must be able to log failures. You can enable logging by configuring the response validation fields when you create or modify an uptime check. For more information on creating uptime checks, see [Create public uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks).

### Uptime check failure

This event type helps you identify uptime check failures from configured regions.

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    log_id(monitoring.googleapis.com%2Fuptime_checks)
    (
      resource.type=uptime_url OR resource.type=gce_instance OR
      resource.type=gae_app OR resource.type=k8s_service OR
      resource.type=servicedirectory_service OR resource.type=cloud_run_revision OR
      resource.type=aws_ec2_instance OR resource.type=aws_elb_load_balancer
    )
    labels.uptime_result_type=UptimeCheckResult
    severity=NOTICE
    

For troubleshooting information, see [Troubleshoot synthetic monitors and uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks/troubleshoot).

## Agent for SAP event types

This section describes the Agent for SAP event types that can be shown on a dashboard.

**Note:** For these event types to be visible, you must redirect the agent's logs to Cloud Logging. This setting is enabled by default. For more details, see [Configure the Agent for SAP](https://docs.cloud.google.com/sap/docs/show-sap-events-on-dashboard#install-configure-agent-for-sap).

### SAP Availability

This event type helps you identify events related to Agent for SAP availability. These events are triggered when SAP HANA, SAP NetWeaver, or Pacemaker Cluster availability changes.

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    log_id(google-cloud-sap-agent)
    (
      resource.type=generic_node OR resource.type=gce_instance OR
      resource.type=aws_ec2_instance OR resource.type=baremetalsolution.googleapis.com/Instance
    )
    jsonPayload.metricEvent=true
    jsonPayload.metric=(workload.googleapis.com/sap/hana/service OR workload.googleapis.com/sap/hana/availability OR
      workload.googleapis.com/sap/nw/service OR workload.googleapis.com/sap/nw/availability OR
      workload.googleapis.com/sap/cluster/nodes OR workload.googleapis.com/sap/cluster/resources)
    

### SAP Backint

This event type helps you identify events related to Agent for SAP Backint. Any Backint backup or recovery writes an event detailing success or failure along with the transfer statistics. Log backups and recoveries are only shown on failure, while data backups and recoveries are shown on both success and failure.
    
    
    log_id(google-cloud-sap-agent-backint)
    (
      resource.type=generic_node OR resource.type=gce_instance OR
      resource.type=aws_ec2_instance OR resource.type=baremetalsolution.googleapis.com/Instance
    )
    (jsonPayload.fileType=data OR (jsonPayload.fileType=log AND jsonPayload.success=false))
    jsonPayload.message=SAP_BACKINT_FILE_TRANSFER
    

### SAP Operations

This event type helps you identify events related to Agent for SAP operations. These events are triggered when SAP HANA replication status changes.

If you want to [create a log-based alerting policy](https://docs.cloud.google.com/monitoring/dashboards/show-events#create-alert) for this event type, then use the following query:
    
    
    log_id(google-cloud-sap-agent)
    (
      resource.type=generic_node OR resource.type=gce_instance OR
      resource.type=aws_ec2_instance OR resource.type=baremetalsolution.googleapis.com/Instance
    )
    jsonPayload.metricEvent=true
    jsonPayload.metric=workload.googleapis.com/sap/hana/ha/replication
    

## What's next

To learn how to show events on your dashboards, see [Show events on a dashboard](https://docs.cloud.google.com/monitoring/dashboards/show-events).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
