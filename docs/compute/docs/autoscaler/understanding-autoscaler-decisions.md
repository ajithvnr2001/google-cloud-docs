---
url: https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions/
title: Understand autoscaler decisions \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T16:02:00.472321+00:00
---

# Understand autoscaler decisions  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Understand autoscaler decisions Stay organized with collections  Save and categorize content based on your preferences. 

Autoscaling automatically adds VMs (scales out) or removes VMs (scales in) from your [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups). This document explains how an autoscaler determines when to scale your MIGs.

## How autoscalers calculate recommended size and affect target size

When you configure an autoscaler for a MIG, the autoscaler constantly monitors the group and calculates a _recommended size_ —the number of VMs required to serve the observed load. The MIG then uses this recommendation to set the group's _target size_.

### Calculation of recommended size

The autoscaler recalculates the recommended size constantly based on the following:

  * By default, the autoscaler sets the recommended size to handle peak load observed over the [stabilization period](https://docs.cloud.google.com/compute/docs/autoscaler#stabilization_period).
  * If [predictive autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling) is enabled, the autoscaler forecasts future load based on historical CPU utilization and sets the recommended size based on the prediction.



You can check the recommended size by [viewing the **Group size** chart](https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#monitoring_autoscaling_charts_and_logs) on Google Cloud console. If you use Google Cloud CLI or Compute Engine API, then [get the autoscaler information](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#get_information_about_an_autoscaler) and look for the `recommendedSize` field in the output.

### Constraints on recommended size

The final recommended size is subject to the following constraints:

  * **Minimum and maximum instances** : The size must be within the bounds set in your autoscaling policy.
  * **Scale-in controls** : If you've configured the [scale-in controls](https://docs.cloud.google.com/compute/docs/autoscaler#scale-in_controls) in the autoscaling policy, then the autoscaler limits how much the recommended size can decrease at once to prevent sudden capacity drops.



### Effect on target size

The MIG's response to the recommended size depends on the [`mode`](https://docs.cloud.google.com/compute/docs/autoscaler#autoscaling_mode) of the autoscaler:

  * **`ON`** : The MIG sets its target size to the recommended size and scales the group accordingly.
  * **`ONLY_SCALE_OUT`** : The target size only increases if the recommended size increases. It does not decrease even if the recommended size drops.
  * **`OFF`** : The target size remains unchanged. The autoscaler still calculates the recommended size in the background but doesn't apply it to the target size.



If you delete the autoscaler configuration, the autoscaler stops calculating a recommended size.

## Gaps between target and actual utilization metrics

When using an autoscaling policy with [metrics-based signals](https://docs.cloud.google.com/compute/docs/autoscaler#target_utilization), you might notice that, for smaller instance groups, the actual utilization of the instance group and the target utilization might seem far apart. This is because an autoscaler always acts conservatively by rounding up or down when it interprets utilization data and determines how many instances to add or remove. This prevents the autoscaler from adding an insufficient number of resources or removing too many resources.

For example, if you set a utilization target of 0.7 and your application exceeds the utilization target, the autoscaler might determine that adding 1.5 virtual machine (VM) instances would decrease the utilization to close to 0.7. Because you cannot add 1.5 VM instances, the autoscaler rounds up and adds two instances. This might decrease the average CPU utilization to a value lower than 0.7 but ensures that your app has enough resources to support it.

Similarly, if the autoscaler determines that removing 1.5 VM instances would increase your utilization too close to 0.7, it will remove just one instance.

For larger groups with more VM instances, the utilization is divided up over a larger number of instances, and adding or removing VM instances causes less of a gap between actual utilization and target utilization.

If you use schedule-based autoscaling with another autoscaling signal, an active schedule might require more VMs than your utilization needs. In these situations, your actual utilization is lower than your target utilization because the autoscaling schedule determines the recommended size of the instance group.

## Delays in scaling out

When you configure autoscaling, you specify an [initialization period](https://docs.cloud.google.com/compute/docs/autoscaler#cool_down_period) that reflects the length of time it takes for your VMs to initialize. The autoscaler only recommends scaling out if the average utilization from instances that are not initializing is greater than the target utilization.

If you set an initialization period value that is significantly longer than the time it takes for an instance to initialize, then your autoscaler might ignore legitimate utilization data, and it might underestimate the required size of your group.

## Delays in scaling in

For the purposes of scaling in, the autoscaler calculates the group's recommended target size based on peak load over the [stabilization period](https://docs.cloud.google.com/compute/docs/autoscaler#stabilization_period).

Observing the usage during the stabilization period helps the autoscaler:

  * Ensure that usage information collected from the instance group is stable.
  * Prevent behavior where an autoscaler continuously adds or removes instances at an excessive rate.
  * Safely remove instances by determining that the smaller group size is enough to support peak load from the stabilization period.



The stabilization period might appear as a delay in scaling in, but it is actually a built-in feature of autoscaling. The stabilization period also ensures that if a new instance is added to the managed instance group, the instance runs for the duration of the stabilization period before it is eligible for deletion.

[Initialization periods](https://docs.cloud.google.com/compute/docs/autoscaler#cool_down_period) for new instances are ignored when deciding whether to scale in a group.

### Connection draining causing delays

If the group is part of a [backend service](https://docs.cloud.google.com/compute/docs/load-balancing/http/backend-service) that has [enabled connection draining](https://docs.cloud.google.com/compute/docs/load-balancing/enabling-connection-draining), it can take up to an additional 60 seconds after the connection draining duration has elapsed before the VM instance is removed or deleted.

## Scale-in controls

When you [configure autoscaler scale-in controls](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#configure_scale_in_controls), you control the speed of scaling in. The autoscaler never scales in faster than your configured rate:

![Autoscaler with and without scale-in controls.](https://docs.cloud.google.com/static/compute/images/autoscaler/autoscaler-with-and-without-scale-in-controls.svg)

  1. When load declines, the autoscaler maintains the size for the group at a level required to serve the peak load observed in the ([stabilization period](https://docs.cloud.google.com/compute/docs/autoscaler#stabilization_period)). This works the same with and without scale-in controls.
  2. An autoscaler without scale-in controls keeps only enough instances required to handle recently observed load. After the stabilization period, the autoscaler removes all unneeded instances in one step. With a sudden drop in load this can lead to a dramatic reduction of instance group size.
  3. An autoscaler with scale-in controls limits how many VM instances can be removed in a configured period of time (here 10 VMs in 20 minutes). This slows down the instance reduction rate.
  4. With a new load spike, the autoscaler adds new instances to handle the load. However, due to a long initialization time, the new VMs are not ready to serve the load. With scale-in controls, the previous capacity was kept, allowing existing VMs to serve the spike.



You control the scale-in rate by configuring the Autoscaler's _maximum allowed reduction_ within a _trailing time window_ , specifically:

  * **Maximum allowed reduction** (`maxScaledInReplicas`: number or % of VM instances). The number of instances that your workload can afford to lose (from the group's peak size) within the specified trailing time window. Use this parameter to constrain how much your group can be scaled in so that you can still serve a likely load spike until more instances start serving. The lower the maximum allowed reduction, the slower the rate of scale in.
  * **Trailing time window** (`timeWindowSec`: seconds). Time during which a load spike is likely to follow a temporary decline and during which you don't want your group size to scale in beyond the maximum allowed reduction. Use this parameter to define the time window in which autoscaler will look for the peak size sufficient to serve historical load. Autoscaler won't resize below the maximum allowed reduction subtracted from the peak size observed in the trailing time window. With a longer trailing time window, the autoscaler considers more historical peak load, which makes scaling in more conservative and stable.



When you set scale-in controls, the autoscaler constrains scale-in operations to the maximum allowed reduction from the peak size observed in the trailing time window. The autoscaler uses the following steps:

  1. Continuously monitors the historical peak size observed in the trailing time window.
  2. Uses the maximum allowed reduction to calculate the constrained scale-in size (peak size: `maxScaledInReplicas`)
  3. Sets the group's [recommended size](https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#how_autoscalers_calculate_recommended_size_and_affect_target_size) to the constrained scale-in size. For example, if an autoscaler would resize an instance group to 20 VMs but scale-in constraints only allow a scale in to 40 VMs, then the recommended size is set to 40 VMs.



With scale-in controls, the autoscaler continuously monitors the peak size of an instance group within the configured trailing time window to identify the sufficient size to serve historical load. The autoscaler does not scale in beyond the maximum allowed reduction measured from the observed peak size:

![Autoscaler with scale-in controls.](https://docs.cloud.google.com/static/compute/images/autoscaler/autoscaler-with-scale-in-controls.svg)

For example, in the preceding diagram, scale-in controls are configured for a 20 VM maximum allowed reduction in a 30-minute trailing time window:

  1. When load goes down autoscaler removes 20 VMs, which is the maximum allowed reduction configured in scale-in controls.
  2. As the load goes up and down, the autoscaler constantly monitors the last 30 minutes trailing time window for the peak size sufficient to serve historical load. This peak size is used as a base for scale-in controls to limit scale-in rate. If, in the last 30 minutes, peak size was 70 VMs and the maximum allowed reduction is set to 20 VMs, the autoscaler can scale in to 50 VMs. If the current size is 65 VMs, the autoscaler can remove only 15 VMs.
  3. As load decreases, the autoscaler continues to remove VM instances but limits the rate to at most 20 VMs from the peak instance group size measured in the last 30 minutes.



The maximum allowed reduction in group size might happen all at once, so you should configure the maximum allowed reduction so that your application can afford losing that many instances at once. Use the maximum allowed reduction parameter to indicate how much reduction in serving capacity your application can tolerate.

By limiting the number of VM instances that autoscaling can remove and by increasing the observed trailing time window, applications with load spikes and long initialization times should experience improved availability. In particular, the instance group size doesn't drop abruptly in response to a significant drop in load and instead decreases gradually over time. If load spikes soon after a scale in has occurred, the remaining number of VMs should still be able to absorb the spike within your tolerance. In addition, fewer VMs must be started in order to sufficiently serve the spike.

You can configure scale-in controls for autoscaling of both zonal and regional MIGs. The configuration is the same for both cases. Scale-in controls work for any group size.

### Scale-in controls versus autoscaler stabilization

Configuring scale-in controls does not mean switching off the autoscaler's [stabilization mechanism](https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#delays_in_scaling_in). The autoscaler always maintains the instance group size at a level required to serve peak load, observed during the stabilization period. Scale-in controls give you an additional mechanism to control the rate at which an instance group is resized.

| Stabilization period | Scale-in controls:  
Trailing time window   
---|---|---  
Configurable? | Yes, configurable | Yes, configurable  
What is monitored? | Monitors _peak load_ over the previous duration set by the stabilization period. | Monitors _peak size_ of the instance group in the previous period set by trailing time window.   
How does this help? | Ensures that the instance group size remains sufficient to serve the peak load that was observed during the stabilization period.  | Ensures that the instance group size is not reduced by more VM instances than your workload can tolerate when handling load spikes over a specified time window.   
  
### Scale-in controls with autoscaler mode

There are two similar yet slightly different scenarios when your MIG is not autoscaled and you want to turn on autoscaling. These depend on whether you are configuring autoscaling for the first time or whether autoscaling is configured but [temporarily restricted or off](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#turn_off_or_restrict_an_autoscaler).

#### Configure autoscaler for the first time

When you have a non-autoscaled MIG and you configure autoscaling from scratch, the autoscaler uses the current MIG size as a starting point. Before scaling in, the autoscaler uses the stabilization period and then it uses scale-in controls to constrain the scale-in rate:

![Configuring autoscaler for the first time.](https://docs.cloud.google.com/static/compute/images/autoscaler/autoscaler-initializing-with-scale-in-controls.svg)

#### Change autoscaler mode

With [autoscaling mode](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#turn_off_or_restrict_an_autoscaler), you can temporarily turn off or restrict autoscaling activities. The autoscaler's configuration persists and the autoscaler continues to perform background calculations while the autoscaler is off or restricted. The autoscaler takes into account scale-in controls in its background calculations while in off or restricted mode. All autoscaling activities resume using the most recent calculations when you turn autoscaling on again or when you lift the restriction:

![Resuming autoscaler including scale-in controls.](https://docs.cloud.google.com/static/compute/images/autoscaler/autoscaler-resuming-with-scale-in-controls.svg)

  1. Autoscaler turned ON behaves as usual (with scale-in controls in this case).
  2. When you turn autoscaler OFF, it still calculates the recommended instance group size based on load. Autoscaler calculations still consider scale-in controls. However, the autoscaler does not apply size calculations when autoscaler is OFF. The instance group size stays constant until autoscaler is ON again.
  3. When you turn the autoscaler ON again it immediately applies the previously calculated size. This allows faster scaling to the correct size. Re-enabling the autoscaler can cause an abrupt scale in (here from 80 to 40 VM instances). This is safe because background calculations already consider scale-in controls.



## Autoscale a MIG to zero instances

An autoscaler can scale in your MIG to zero instances depending on the `minNumReplicas` field, autoscaling signals, and schedules that you configure in the autoscaling policy.

### Conditions for an autoscaler to scale in a MIG to zero

An autoscaler can scale in a MIG to zero instances when _all_ of the following conditions are met:

  * The minimum number of instances (`autoscalingPolicy.minNumReplicas`) is set to `0`.

  * No active schedules that require more than zero instances.

  * The autoscaling policy must not use any of the following metrics that depend on running instances. If the policy includes these metrics, then the autoscaler requires at least one instance in the group to obtain a signal, and the group won't scale in to zero instances.

    * Average CPU utilization
    * HTTP load balancing serving capacity
    * Cloud Monitoring metrics collected from each instance in the MIG



You can also manually resize a MIG to zero instances, even if the autoscaling policy includes metrics collected from each instance in the MIG. To manually resize the MIG, see [Manually setting the size of a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#resize_managed_group)

### Condition for an autoscaler to scale out a MIG from zero

When a MIG's target size is zero, either set by the autoscaler or resized manually, the autoscaler can scale out the MIG only when a scaling signal or an active schedule requires more than zero instances.

If the only scaling signal in the policy is based on metrics collected from each instance, then the MIG can't scale out from zero because no instances exist in the group to generate the metrics. In such cases, to increase the MIG's target size, you must [manually set the size of the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#resize_managed_group).

## Predictive autoscaling

To learn about predictive autoscaling, including [how it works](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling#how_predictive_autoscaling_works), see [Scaling based on predictions](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling).

## Autoscaler prepares to stop instances

When the autoscaler scales in a MIG, the MIG determines which VM instances to delete. The MIG prioritizes VM instances for deletion based on several factors. For more information about these factors, see [Factors that affect the deletion of VM instances](https://docs.cloud.google.com/compute/docs/instance-groups/working-with-managed-instances#factors_affecting_vm_deletion).

Before an instance is stopped, you might want to make sure these instances perform certain tasks, such as closing any existing connections, gracefully shut down any apps or app servers, uploading logs. You can instruct your instance to perform these tasks using a [shutdown script](https://docs.cloud.google.com/compute/docs/shutdownscript). A shutdown script runs, on a [best-effort basis](https://docs.cloud.google.com/compute/docs/shutdownscript#time_period), in the brief period between when the stopping request is made and when the instance is actually stopped. During this period, Compute Engine attempts to run your shutdown script to perform any tasks you provide in the script.

This is particularly useful if you are using load balancing with your managed instance group. If your instance becomes unhealthy, it might take some time for the load balancer to recognize that the instance is unhealthy, causing the load balancer to continue sending new requests to the instance. With a shutdown script, the instance can report that it is unhealthy while it is shutting down so that the load balancer can stop sending traffic to the instance. For more information about load balancing health checks, see the [health checks overview](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts).

For more information about shutdown scripts, see [Shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript).

For more information about instance shutdown, read documentation on [stopping](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stopping_an_instance) or [deleting](https://docs.cloud.google.com/compute/docs/instances/deleting-instance) an instance.

## Monitor autoscaling charts and logs

Compute Engine provides several charts and logs that let you monitor your managed instance group's behavior at any point in time.

You can access the charts and logs in the Google Cloud console.

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the managed instance group that you want to view.

  3. On the managed instance group page, select the **Monitoring** tab.

The **Monitoring** tab shows charts and logs as follows:

     * The charts display the evolution of the following metrics:

       * Group size
       * Autoscaler utilization
       * CPU utilization
       * Disk I/O (bytes)
       * Disk I/O (operations)
       * Network bytes
       * Network packets

For additional contextual details about the metric displayed in a chart, hold the pointer over the help icon next to the title of that chart.

     * The **Logs** panel that is available at the bottom of the page shows a list of event logs for your managed instance group. To view the logs, on this panel, click the keyboard_capslock **Toggle panel "Logs"** icon.

All charts and logs are bound to a single timeframe. You can analyze the charts and logs for a particular event or a specific time range as follows:

     * To zoom in on a particular event, drag on any chart. The logs panel also refreshes to show the logs from the selected time range on the chart.

     * To view the charts and logs in a specific time range, use the time range selector.




### Monitor group size

The **Group size** chart lets you monitor the number of running instances in a MIG. In this chart, the **Instances** line indicates the number of running instances.

If you've configured autoscaling, the chart also displays the following sizes:

  * **Configured min size** : the minimum number of instances (`minNumReplicas`) that you set in the autoscaling policy.
  * **Configured max size** : the maximum number of instances (`maxNumReplicas`) that you set in the autoscaling policy.
  * **Recommended size** : the recommended target size calculated by the autoscaler.



For more information about autoscaling policy, see [Autoscaling groups of instances](https://docs.cloud.google.com/compute/docs/autoscaler#autoscaling_policy).

### Monitor autoscaling events

**Preview — Group size events**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The **Group size** chart includes a **Group size events** timeline. This timeline displays events such as the autoscaler scaling the group in or out. Hovering over an event block in the timeline displays a card with the corresponding event details that includes the following:

  * **Timestamp** : the timestamp of the event.

  * **Event type and sizes** : scale in or scale out. Next to the event type is the old size and the new size after the event—for example, `6 VMs arrow_forward 1 VM`.

  * **Scaling signal** : the signal that triggered the event—for example, CPU utilization.

  * **Signal value** : the actual value of the scaling signal.

  * **Signal target** : the target value of the scaling signal.

  * **Calculated size** : the number of instances that the autoscaler calculated to achieve the signal target.

  * **Limited by** : any autoscaling configuration that constrained the new size—for example, the MIG's minimum or maximum number of instances. If the autoscaler doesn't apply any constraints to the new size, then the card doesn't show this detail.




The following figure shows an example of an autoscaler event timeline. In this example, the card shows a scale in event in which the group size is reduced from `4` VMs to `1` VM.

**Note:** The graph uses metrics that are sampled every minute. Due to this sampling frequency, the data in the graph can be delayed up to 90 seconds after the corresponding group size events are shown in the timeline.

![Autoscaler events timeline.](https://docs.cloud.google.com/static/compute/images/autoscaler/autoscaler-events-timeline.png)

**Figure 1.** Group size chart showing the events timeline.

Depending on the time range you are viewing, the timeline might group events that are close together. In this case, the chart shows the number of grouped events. For example, if a card shows **5 events** , it means five autoscaling events occurred within that time range. To view those events as separate blocks on the timeline, zoom in on the graph. You can also view the details of the grouped events by clicking the **View events** in the card.

### Monitor predictive autoscaling

Compute Engine provides a chart to monitor the autoscaler predictions. To view this chart, click the **Group size** title in the first chart and select **Predictive autoscaling**.

If autoscaling is enabled, you can view how the autoscaler predictions determine the size of your instance group. If autoscaling is not enabled, you can still see the autoscaler predictions and use them to inform your decisions regarding your group size.

Use the following information to understand this chart.

  * The blue line indicates the number of instances in the managed instance group.
  * The green line shows the number of instances predicted by autoscaler. 
    * If the green line is below the blue line, there is a large amount of capacity available and your VM instances are likely under utilized.
    * If the green line is above the blue line, then there is little, if any, remaining capacity and you should add more instances to the instance group.
  * The dashed horizontal red lines indicate the minimum and maximum number of instances allowed in your instance group.



## View status messages

When the autoscaler experiences an issue scaling, it returns a warning or error message. You can review these status messages in one of two ways.

**View status messages on the Instance groups page**

You can view status messages directly on the **Instance groups** page in the [Google Cloud console](https://console.cloud.google.com/).

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Look for any instance groups that have the caution icon preceding their names.

For example:

![Status messages on instance groups page.](https://docs.cloud.google.com/static/compute/images/statusmessagesinstancegroupspage.png)

  3. Hold the pointer over a status icon to get details of the status message.




**View status messages on the Instance group overview page**

You can go directly to the overview page of a specific instance group to view relevant status messages.

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the instance group for which you want to view status messages.
  3. On the instance group page, view the status message below the instance group name.



## Commonly returned status messages

When the autoscaler experiences an issue scaling, it returns a warning or error message. Here are some commonly returned messages and what they mean.

`All instances in the instance group are unhealthy (not in RUNNING state). If this is an error, check the instances.`
    All of the instances in the instance group have a state that is something other than `RUNNING`. If this is intentional, then you can ignore this message. If this is not intentional, troubleshoot the instance group.
`The number of instances has reached the maxNumReplicas. The autoscaler cannot add more instances.`
    When you created the autoscaler, you indicated the maximum number of instances the instance group can have. The autoscaler is attempting to scale out the instance group to meet demand but has reached the `maxNumReplicas`. For information about how to update `maxNumReplicas` to a larger number, see [Updating an autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#updating-an-autoscaler).
`The monitoring metric that was specified does not exist or does not have the required labels. Check the metric.`
    

You are autoscaling using a Cloud Monitoring metric but the metric you provided does not exist, lacks the necessary labels, or is not accessible to the [Compute Engine Service Agent](https://docs.cloud.google.com/compute/docs/access/service-accounts#compute_engine_service_account).

    

  * Depending on whether the metric is a standard or custom metric, different labels are required. See the documentation for [Scaling based on a Monitoring metric](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-stackdriver-monitoring-metrics) for more information.


    

  * [Verify](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#viewing-console) that the Compute Engine Service Agent has the `compute.serviceAgent` IAM role. To add it, see [Autoscaler prerequisites](https://docs.cloud.google.com/compute/docs/autoscaler#prerequisites).


`Quota for some resources is exceeded. Increase the quota or delete resources to free up more quota.`
    

You can get information about your available quota on the [Quota page](https://console.cloud.google.com/iam-admin/quotas) in the Google Cloud console.

`Autoscaling does not work with an HTTP/S load balancer configured for maxRate.`
    

The instance group is being load balanced using the `maxRate` configuration but the autoscaler does not support this mode. Either change the configuration or disable autoscaling. To learn more about `maxRate`, read the [Restrictions and guidelines](https://docs.cloud.google.com/compute/docs/load-balancing/http/backend-service#restrictions_and_guidance) in the load balancing documentation.

`The autoscaler is configured to scale based on a load balancing signal but the instance group has not received any queries from the load balancer. Check that the load balancing configuration is working.`
    

The instance group is being load balanced but the group has no incoming queries. The service might be experiencing a period of idleness, in which case there is nothing to worry about. However, this message can also be caused by misconfiguration; for example an autoscaled instance group might be the target of more than one load balancer, which is not supported. For a full list of guidelines, see [Restrictions and guidelines](https://docs.cloud.google.com/compute/docs/load-balancing/http/backend-service#restrictions_and_guidance) in the load balancing documentation.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
