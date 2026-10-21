---
url: https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-mig/
title: Configure a Compute Engine MIG \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:56:01.894592+00:00
---

# Configure a Compute Engine MIG  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-mig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)



Send feedback 

#  Configure a Compute Engine MIG Stay organized with collections  Save and categorize content based on your preferences. 

A Compute Engine managed instance group (MIG) is a collection of VM instances that use load balancing and automated services, such as autoscaling and autohealing. With a MIG, you can manage a group of VM instances as one entity. For more information, see the following:

  * [Compute Engine overview](https://docs.cloud.google.com/compute/docs/overview)
  * [Managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups)



This document describes the connections and parameters you can configure when using App Design Center to create a Compute Engine MIG. The configuration parameters are based on the [terraform-google-vm](https://github.com/terraform-google-modules/terraform-google-vm/tree/main/modules/mig) Terraform module.

## Component connections

The following table includes the components that you can connect to a Compute Engine MIG, and the resulting updates to your application and its generated Terraform code.

Connected component | Application updates | Background information  
---|---|---  
[Global Cloud Load Balancing backend](https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-global-backend) | 

  * The load balancer can distribute incoming traffic to the Compute Engine MIG.
  * The Compute Engine MIG is added to the Cloud Load Balancing backend service groups field.

| [Set up a classic Application Load Balancer with a managed instance group backend](https://docs.cloud.google.com/load-balancing/docs/https/ext-https-lb-simple)  
[Regional Cloud Load Balancing backend](https://docs.cloud.google.com/application-design-center/docs/configure-load-balancing-regional-backend) | 

  * The load balancer can distribute incoming traffic to the Compute Engine MIG.
  * The Compute Engine MIG is added to the Cloud Load Balancing backend service groups field.

| [Set up a regional external Application Load Balancer with VM instance group backends](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-lb)  
[Compute Engine instance template](https://docs.cloud.google.com/application-design-center/docs/configure-compute-engine-instance) | 

  * The Compute Engine instance template is used to create instances in the managed instance group.
  * The instance template self link is added to the Compute Engine MIG.

| [Basic scenarios for creating managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-managed-instances)  
  
## Required configuration parameters

If your template includes a Compute Engine MIG component, you must configure the following parameters before you deploy.

Parameter name | Description and constraints | Background information  
---|---|---  
**Project ID** | The project where you want to create the Compute Engine MIG. | [Configure components](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#configure_components)  
**Region** | [region](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.region) | [About Regional MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs)  
**Instance Template** | [instanceTemplate](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.instance_template) | [About Instance Templates](https://docs.cloud.google.com/compute/docs/instance-templates)  
  
## Optional configuration parameters

The following parameters are optional. To display advanced parameters, in the **Configuration** area, select **Show advanced fields**.

Feature | Parameter name | Description and constraint information | Background information  
---|---|---|---  
| **MIG name** | [name](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.name) | [mig_name](https://github.com/terraform-google-modules/terraform-google-vm/tree/main/modules/mig#inputs)  
| **Hostname** | Hostname prefix for instances. | [hostname](https://github.com/terraform-google-modules/terraform-google-vm/tree/main/modules/mig#inputs)  
| **Target Size** | [targetSize](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.target_size) | [Create a MIG with autoscaling enabled.](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-basic-autoscaling)  
| **Max Replicas** | [autoscalingPolicy.maxNumReplicas](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers#Autoscaler.FIELDS.inlinedField_1) | [Create a MIG with autoscaling enabled](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-basic-autoscaling)  
| **Min replicas** | [autoscalingPolicy.minNumReplicas](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers#Autoscaler.FIELDS.inlinedField) | [Create a MIG with autoscaling enabled](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-basic-autoscaling)  
| **Autoscaling Mode** | [autoscalingPolicy.mode](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers#Autoscaler.FIELDS.inlinedField_20) | [Autoscaling mode](https://docs.cloud.google.com/compute/docs/autoscaler#autoscaling_mode)  
| **Target Pools** | [targetPools[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.target_pool) | [Add a managed instance group to a target pool](https://docs.cloud.google.com/compute/docs/instance-groups/adding-an-instance-group-to-a-load-balancer#add_a_managed_instance_group_to_a_target_pool)  
| **Distribution Policy Target Shape** | [distributionPolicy.targetShape](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_2) | [feedbackRegional MIG target distribution shape](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape)  
| **Distribution Policy Zones** | [distributionPolicy.zones[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField) | [Set a target distribution shape for VMs in a regional MIG](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-set-target-distribution-shape)  
Stateful Disks | **Device Name** | [statefulPolicy.preservedState.disks[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_59) | [Configuring stateful persistent disks in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs)  
**Delete Rule** | [statefulPolicy.preservedState.disks[].autoDelete](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_60) | [Configuring stateful persistent disks in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-disks-in-migs)  
Stateful IPs | **Interface Name** | [statefulPolicy.preservedState.internalIPs[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_61) | [Configuring stateful IP addresses in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs)  
**Delete Rule** | [statefulPolicy.preservedState.internalIPs[].autoDelete](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_62) | [Configuring stateful IP addresses in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs)  
**Is External** | [statefulPolicy.preservedState.externalIPs[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_63) | [Configuring stateful IP addresses in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/configuring-stateful-ip-addresses-in-migs)  
Update Policy | **Max Surge Fixed** | [updatePolicy.maxSurge.fixed](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_48) | [Maximum surge](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#max_surge)  
**Instance Redistribution Type** | [updatePolicy.instanceRedistributionType](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_44) | [Proactive instance redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#proactive_instance_redistribution)  
**Max Surge Percent** | [updatePolicy.maxSurge.percent](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_49) | [Maximum surge](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#max_surge)  
**Max Unavailable Fixed** | [updatePolicy.maxUnavailable.fixed](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_52) | [Maximum unavailable](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#max_unavailable)  
**Max Unavailable Percent** | [updatePolicy.maxUnavailable.percent](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_53) | [Maximum unavailable](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#max_unavailable)  
**Min Ready Sec** | [updatePolicy.minReadySec](https://docs.cloud.google.com/compute/docs/reference/rest/beta/instanceGroupManagers/update#body.request_body.FIELDS.inlinedField_59) | [Minimum wait time](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#minimum_wait_time)  
**Replacement Method** | [updatePolicy.replacementMethod](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_55) | [Replacement method](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#replacement_method)  
**Minimal Action** | [updatePolicy.minimalAction](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_45) | [Minimal action](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#minimal_action)  
**Type** | [updatePolicy.type](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_43) | [Update type](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#type)  
**Most Disruptive Allowed Action** | [updatePolicy.mostDisruptiveAllowedAction](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_46) | [Most disruptive allowed action](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#most_disruptive_allowed_actionS)  
| **Health Check Name** | [name](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.name) | [Health checks overview](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts)  
Health Check | **Type** | [type](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.type) | [Health check categories, protocols, and ports](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#categories_protocols_ports)  
**Initial Delay Seconds** | [autoHealingPolicies[].initialDelaySec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers/patch#body.request_body.FIELDS.inlinedField_42) | [Configure an autohealing policy in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#configure_autohealing_policy)  
**Check Interval Sec** | [checkIntervalSec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.check_interval_sec) | [Configure an autohealing policy in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#configure_autohealing_policy)  
**Healthy Threshold** | [healthyThreshold](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.healthy_threshold) | [Configure an autohealing policy in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#configure_autohealing_policy)  
**Timeout Sec** | [timeoutSec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.timeout_sec) | [What makes a good autohealing health check](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#what_makes_a_good_autohealing_health_check)  
**Unhealthy Threshold** | [unhealthyThreshold](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.unhealthy_threshold) | [Configure an autohealing policy in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/autohealing-instances-in-migs#configure_autohealing_policy)  
**Response** | [httpsHealthCheck.response](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.inlinedField_25) | [Success criteria for HTTP, HTTPS, and HTTP/2](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-http)  
**Proxy Header** | [httpsHealthCheck.proxyHeader](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.inlinedField_24) | [Headers](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#headers)  
**Port** | [httpsHealthCheck.port](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.inlinedField_26) | [Health check categories, protocols, and ports](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#categories_protocols_ports)  
**Request** | [tcpHealthCheck.request](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.inlinedField_3) | [Success criteria for HTTP, HTTPS, and HTTP/2](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-http)  
**Request Path** | [httpsHealthCheck.requestPath](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.inlinedField_23) | [Success criteria for HTTP, HTTPS, and HTTP/2](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#criteria-protocol-http)  
**Host** | [httpsHealthCheck.host](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.inlinedField_22) | [Headers](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#headers)  
**Enable Logging** | [logConfig.enable](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionHealthChecks#HealthCheck.FIELDS.inlinedField_37) | [Health check logging information](https://docs.cloud.google.com/load-balancing/docs/health-check-logging)  
| **Autoscaler Name** | [name](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers#Autoscaler.FIELDS.name) | If empty, the name is derived from _hostname_.  
| **Autoscaling Enabled** | Create an autoscaler for the MIG. | [Autoscaling groups of instances](https://docs.cloud.google.com/compute/docs/autoscaler)  
| **Cooldown Period** | [autoscalingPolicy.coolDownPeriodSec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers#Autoscaler.FIELDS.inlinedField_8) | [Initialization period](https://docs.cloud.google.com/compute/docs/autoscaler#cool_down_period)  
Autoscaling CPU | **Target** | [autoscalingPolicy.cpuUtilization.utilizationTarget](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers#Autoscaler.FIELDS.inlinedField_10) | [Scaling based on CPU utilization](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cpu)  
**Predictive Method** | [autoscalingPolicy.cpuUtilization.predictiveMethod](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers#Autoscaler.FIELDS.inlinedField_11) | [Predictive autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler#predictive_mode)  
Autoscaling Metric | **Name** | [name](https://www.terraform.io/docs/providers/google/r/compute_autoscaler#metric) | [Autoscale to maintain a metric at a target value](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cloud-monitoring-metrics#configure_utilization_target)  
**Target** | [autoscalingPolicy.customMetricUtilizations[].utilizationTarget](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers#Autoscaler.FIELDS.inlinedField_13) | [Autoscale to maintain a metric at a target value](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cloud-monitoring-metrics#configure_utilization_target)  
**Type** | [autoscalingPolicy.customMetricUtilizations[].utilizationTargetType](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers#Autoscaler.FIELDS.inlinedField_17) | [Autoscale to maintain a metric at a target value](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cloud-monitoring-metrics#configure_utilization_target)  
Scaling Schedules | **Disabled** | [autoscalingPolicy.scalingSchedules[].disabled](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers#Autoscaler.FIELDS.inlinedField_26) | [Scaling based on schedules](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules)  
**Duration Sec** | [autoscalingPolicy.scalingSchedules[].durationSec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers#Autoscaler.FIELDS.inlinedField_25) | [Scaling schedule settings](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules#schedule_configuration_options)  
**Min Required Replicas** | [autoscalingPolicy.scalingSchedules[].minRequiredReplicas](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers#Autoscaler.FIELDS.inlinedField_22) | [Scaling schedule settings](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules#schedule_configuration_options)  
**Name** | [autoscalingPolicy.scalingSchedules[]](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers#Autoscaler.FIELDS.inlinedField_21) | [Creating a scaling schedule](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules#creating_a_scaling_schedule)  
**Schedule** | [autoscalingPolicy.scalingSchedules[].schedule](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers#Autoscaler.FIELDS.inlinedField_23) | [Scaling schedule settings](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules#schedule_configuration_options)  
**Time Zone** | [autoscalingPolicy.scalingSchedules[].timeZone](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers#Autoscaler.FIELDS.inlinedField_24) | [Scaling schedule settings](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules#schedule_configuration_options)  
Autoscaling Scale in Control | **Fixed Replicas** | [autoscalingPolicy.scaleInControl.maxScaledInReplicas.fixed](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers#Autoscaler.FIELDS.inlinedField_4) | [Configure scale-in controls](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#configuring_scale-in_controls)  
**Percent Replicas** | [autoscalingPolicy.scaleInControl.maxScaledInReplicas.percent](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers#Autoscaler.FIELDS.inlinedField_5) | [Configure scale-in controls](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#configuring_scale-in_controls)  
**Time Window Sec** | [autoscalingPolicy.scaleInControl.timeWindowSec](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers#Autoscaler.FIELDS.inlinedField_7) | [Configure scale-in controls](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#configuring_scale-in_controls)  
Named Ports | **Name** | [namedPorts[].name](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_56) | [Named ports](https://docs.cloud.google.com/load-balancing/docs/backend-service#named-ports)  
**Port** | [namedPorts[].port](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_57) | [Named ports](https://docs.cloud.google.com/load-balancing/docs/backend-service#named-ports)  
| **Wait for Instances** | Whether to wait for all instances to be created/updated before returning. If set to true, when the operation fails, Terraform continues trying until the timeout is reached. | [wait_for_instances](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_group_manager#wait_for_instances-1)  
MIG Timeouts | **Create** | Timeout for Terraform instance creation. | [create](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_group_manager#create-1)  
**Update** | Timeout for Terraform instance update. | [update](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_group_manager#update-1)  
**Delete** | Timeout for Terraform instance deletion. | [delete](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance_group_manager#delete-1)  
Labels | **Key** | [allInstancesConfig.properties.labels](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_11) | [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources)  
**Value** | [allInstancesConfig.properties.labels](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionInstanceGroupManagers#InstanceGroupManager.FIELDS.inlinedField_11) | [Organize resources using labels](https://docs.cloud.google.com/compute/docs/labeling-resources)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
