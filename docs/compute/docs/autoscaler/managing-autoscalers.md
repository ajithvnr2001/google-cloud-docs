---
url: https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers/
title: Manage autoscalers \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:40:37.173271+00:00
---

# Manage autoscalers  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Manage autoscalers Stay organized with collections  Save and categorize content based on your preferences. 

If you use [managed instance groups (MIGs)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups), read this document to learn how to create, configure, and delete your MIG's [autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Create an autoscaler

Creating an autoscaler is slightly different depending on which autoscaling policy you want to use. For instructions on creating an autoscaler, see:

  * [Scaling based on CPU utilization](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cpu)
  * [Scaling based on load balancing serving capacity](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-load-balancing)
  * [Scaling based on Cloud Monitoring metrics](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-stackdriver-monitoring-metrics)
  * [Scaling based on schedules](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules)



## Get information about an autoscaler

To get more information about a particular autoscaler, use the console, the [`gcloud compute instance-groups managed describe`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe) sub-command, or the `get` method for a [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers/get) or [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers/get) autoscaler REST resource.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.autoscalers.get` on the project
  * `compute.instanceGroupManagers.get` on the instance group



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of a MIG from the list to open that group's overview page.
  3. Click **Details** to view the group's details, including its autoscaling settings.



###  gcloud 

Use the [`instance-groups managed describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe):
    
    
    gcloud compute instance-groups managed describe INSTANCE_GROUP_NAME

If an autoscaler is attached to the group, the command returns details about the autoscaler:
    
    
    ...
    autoscaler:
      autoscalingPolicy:
        coolDownPeriodSec: 60
        cpuUtilization:
          utilizationTarget: 0.6
        maxNumReplicas: 20
        minNumReplicas: 10
        mode: ON
        scaleInControl:
          timeWindowSec: 300
          maxScaledInReplicas:
            fixed: 3
            calculated: 3
    ...

###  REST 

Use the [`instanceGroupManagers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/get). For a regional MIG, replace `zones/ZONE` with `regions/REGION`.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instanceGroupManagers/INSTANCE_GROUP_NAME

If an autoscaler is attached to the group, the request returns a link to the autoscaler resource.
    
    
    200 OK
    
    {
      ...
      "status": {
        ...
        "autoscaler": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-east1-c/autoscalers/example-group"
      },
    }

To retrieve details about the autoscaler resource, use the [`autoscalers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers/get) for a zonal MIG or the [`regionAutoscalers.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers/get) for a regional MIG.
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/autoscalers/example-autoscaler
    
    
    200 OK
    
    {
     "kind": "compute#autoscaler",
     "id": "8744945839459481093",
     "creationTimestamp": "2018-09-28T13:02:50.553-07:00",
     "name": "example-group",
     "target": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-east1-c/instanceGroupManagers/example-group",
     "autoscalingPolicy": {
      "minNumReplicas": 10,
      "maxNumReplicas": 20,
      "mode": "ON",
      "scaleInControl": {
        "timeWindowSec": 60,
        "maxScaledInReplicas": {
          "calculated": 3,
          "percent": 15
        }
      },
      "coolDownPeriodSec": 60,
      "cpuUtilization": {
       "utilizationTarget": 0.6
      }
     },
     "zone": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-east1-c",
     "selfLink": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-east1-c/autoscalers/example-group",
     "status": "ACTIVE"
    }
    

## Update an autoscaler

When you update an autoscaler, it might take some time for the changes to propagate, and it might be a couple of minutes before your new autoscaler settings are reflected.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.autoscalers.get` on the project
  * `compute.autoscalers.update` on the project
  * `compute.instanceGroupManagers.use` on the project



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of a MIG from the list to open that group's overview page.
  3. Click **Edit**.
  4. Click **Group size & autoscaling** to view and update the group's autoscaling settings.
  5. Click **Save** when you are done.



###  gcloud 

Use the [`update-autoscaling` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-autoscaling).
    
    
    gcloud compute instance-groups managed update-autoscaling INSTANCE_GROUP_NAME \
            --max-num-replicas MAX_NUM ...

For instructions on how to create an autoscaler, see Creating an autoscaler.

###  REST 

To update an autoscaler resource, use the [`autoscalers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers/patch) for a zonal MIG or [`regionAutoscalers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers/patch) for a regional MIG. Provide a request body that contains the new configuration.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/my-project/zones/us-central1-f/autoscalers?autoscaler=example-autoscaler
    
    {
     "autoscalingPolicy": {
      "maxNumReplicas": 20
     }
    }
    
    
    200 OK
    
    {
     "kind": "compute#operation",
     "id": "4244494732310423322",
     "name": "operation-1556912627871-58800f8216ed7-74ab1720-7d360603",
     "zone": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-f",
     "operationType": "compute.autoscalers.patch",
     "targetLink": "https://www.googleapis.com/compute/v1/projects/my-project/zones/us-central1-f/autoscalers/example-autoscaler",
     "targetId": "340775527929467142",
     "status": "RUNNING",
     ...
    }

When you perform any requests that modify data, a [zoneOperations](https://docs.cloud.google.com/compute/docs/reference/latest/zoneOperations) or [regionOperations](https://docs.cloud.google.com/compute/docs/reference/latest/regionOperations) resource is returned, and you can query the operation to check the status of your change.

## Use predictive autoscaling

Predictive autoscaling uses historical data to scale out your group ahead of anticipated load. It works best if your workload meets the following criteria:

  * Your application takes a long time to initialize—for example, if you configure an [initialization period](https://docs.cloud.google.com/compute/docs/autoscaler#cool_down_period) of more than 2 minutes.
  * Your workload varies predictably with daily or weekly cycles.



For more information, see [Scaling based on predictions](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling).

## Turn off or restrict an autoscaler

Turn off an autoscaler to temporarily prevent it from scaling your MIG, or restrict your autoscaler so that it can only scale out your MIG. This feature is useful when you want to:

  * Investigate VM instances without interference from scaling in.
  * Reconfigure multiple properties of your MIG without scaling actions being triggered while your group is only partially reconfigured.
  * Maintain MIG capacity for a fast rollback while redirecting a workload to a new MIG.
  * Enable [predictive autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling) later. Predictive autoscaling requires an autoscaling policy in order to start gathering load history on which to base predictions. The autoscaler detects this history even when its mode is set to `OFF`.



If and when you re-enable the autoscaler, the autoscaler automatically returns to normal operation.

Use the instructions provided in this section to set the autoscaler's mode. The following modes are available:

  * **Off** : Temporarily disables autoscaling. Use this mode to prevent automatic changes of the MIG's size. The autoscaling configuration remains intact so you can re-enable autoscaling later.
  * **Only scale out** : Restrict autoscaling only to adding new VM instances. Use this mode to protect the group from shrinking and allow the group to provision extra VMs when load increases.
  * **On** : Enables all autoscaling operations per its policy.

**Note:** The autoscaler calculates the recommended group size regardless of its mode. You can check the recommended size by [viewing the **Group size** chart](https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#monitoring_autoscaling_charts_and_logs) on Google Cloud console. If you use Google Cloud CLI or Compute Engine API, then [get the autoscaler information](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#get_information_about_an_autoscaler) and look for the `recommendedSize` field in the output.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.autoscalers.get` on the project
  * `compute.autoscalers.update` on the project
  * `compute.instanceGroupManagers.use` on the project



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page. 

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of a MIG from the list to open that group's overview page.
  3. Click **Edit**.
  4. Click **Group size & autoscaling** to view and update the group's autoscaling settings.
  5. In the **Autoscaling** section, set the **Autoscaling mode** to disable or restrict autoscaling for the group, or to turn the autoscaler back on.
  6. Click **Save** when you are done.



###  gcloud 

To disable, restrict, or re-enable an autoscaler, use the [`update-autoscaling` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-autoscaling) with the `--mode` flag.
    
    
    gcloud compute instance-groups managed update-autoscaling INSTANCE_GROUP_NAME \
            --mode MODE 

Replace the following:

  * `MODE`: 
    * `off` to disable the autoscaler but maintain its configuration
    * `only-scale-out` to restrict the autoscaler to adding VM instances only
    * `on` to re-enable all autoscaler activities according to its policy



###  REST 

To update the mode of an autoscaler resource, use the [`autoscalers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers/patch) for a zonal MIG or the [`regionAutoscalers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers/patch) for a regional MIG. Provide a request body that includes the `autoscalingPolicy.mode` property.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/my-project/regions/us-central1/autoscalers?autoscaler=my-autoscaler
    
    {
      "autoscalingPolicy": {
        "mode":"MODE"
      }
    }

Replace the following:

  * `MODE`: 
    * `OFF` to disable the autoscaler but maintain its configuration
    * `ONLY_SCALE_OUT` to restrict the autoscaler to adding instances only
    * `ON` to re-enable all autoscaler activities according to its policy



When you set the autoscaling mode to `ONLY_SCALE_OUT`, the autoscaler behaves as follows:

  * The autoscaler does not decrease the MIG's `targetSize` value regardless of decreases in load or changes to the autoscaler configuration.
  * If you manually change the target size of a zonal MIG, the autoscaler overrides your manually provided size if it is smaller than the autoscaler's recommended size.
  * You cannot manually change the target size of a regional MIG.
  * If you set the `autoscalingPolicy.maxNumReplicas` field to a lower value than the group's current `targetSize` value while the autoscaler's mode is set to `ONLY_SCALE_OUT`, the autoscaler does not reduce the number of instances in the group. As usual, the autoscaler continuously recomputes the group's recommended size and might decrease the group's recommended size to comply with the new maximum, but the group is not scaled in.
  * The `autoscalers.status` field reports a warning: "Autoscaling operates in a restricted mode: ONLY_SCALE_OUT."



When you set the autoscaler's mode to `OFF`, the autoscaler behaves as follows:

  * The autoscaler does not change the MIG's `targetSize` value in response to changes in load or in autoscaler configuration. As usual, the autoscaler continuously recomputes the group's recommended size and might decrease the group's recommended size to comply with the new maximum, but the group is not scaled in.
  * You can manually change the target size of a zonal or a regional MIG. The `minNumReplicas` and `maxNumReplicas` values of the autoscaling policy don't affect the size you set.
  * If you turn off autoscaling for a regional MIG in which [proactive instance redistribution](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#proactive_instance_redistribution) is enabled, and if the MIG has an uneven distribution of instances across zones, then the group proactively deletes or creates instances in its zones to reestablish an even distribution.
  * The `autoscalers.status` field reports a warning: "Autoscaling operates in a restricted mode: OFF."



## Control the scale-in rate of an autoscaler

If your workloads take many minutes to initialize, you can configure the following to reduce the risk of response latency and outages due to abrupt scale-in events:

  * [Scale-in controls](https://docs.cloud.google.com/compute/docs/autoscaler#scale-in_controls): If you routinely expect a load spike to follow soon after a decline in load, then you can limit the scale-in rate by configuring the scale-in controls. Limiting the scale-in rate prevents the autoscaler from reducing a MIG's size by more VM instances than your workload can tolerate to lose.

  * [Stabilization period](https://docs.cloud.google.com/compute/docs/autoscaler#stabilization_period): If you want to prevent premature removal of instances or allow quicker scale in to reduce costs, you can configure the stabilization period. This period controls how long the autoscaler waits to scale in instances after a decrease in load.




### Configure scale-in controls

Configuring scale-in controls is optional. By default, scale-in controls are not configured. When not configured, the autoscaler still relies on its default [stabilization mechanism](https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#delays_in_scaling_in). That is, it maintains the recommended size at a level required to serve peak load, observed during the stabilization period.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.autoscalers.create` on the project to create an autoscaler.
  * `compute.autoscalers.update` on the project to update an autoscaler.
  * `compute.instanceGroupManagers.use` on the project.



###  Console 

To configure scale-in controls for an autoscaled MIG:

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of an autoscaled MIG from the list to open that group's overview page.

  3. Click **Edit**.

  4. Click **Group size & autoscaling** to view and update the group's autoscaling settings.

  5. In the **Scale-in controls** section, select **Enable scale-in controls**.

  6. In the **Don't scale in by more than** field, specify the maximum number or percent of instances that can be removed from the group at a time.

  7. In the **Over the course of** section, specify how often instances can be removed from the group.

  8. Click **Save**.




###  gcloud 

You can configure scale-in controls when creating an autoscaler or when updating an autoscaler.

**Configuring scale-in controls when creating an autoscaler**

Set scale-in controls when creating an autoscaler for a MIG by using the `--scale-in-control` flag with the [`gcloud compute instance-groups managed set-autoscaling` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-autoscaling). For example, use the following command to configure autoscaling for an `example-group`:
    
    
    gcloud compute instance-groups managed set-autoscaling INSTANCE_GROUP_NAME \
        --target-cpu-utilization 0.6 \
        --max-num-replicas 50 \
        --scale-in-control max-scaled-in-replicas=MAX_SCALE_IN_REPLICAS,time-window=TIME_WINDOW
    

**Configuring scale-in controls when updating an autoscaler**

Update scale-in controls in a MIG's existing autoscaler by using the `--scale-in-control` flag with the [`gcloud compute instance-groups managed update-autoscaling` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-autoscaling). For example, use the following command to set scale-in controls in an existing autoscaling configuration for `example-group`:
    
    
    gcloud compute instance-groups managed update-autoscaling INSTANCE_GROUP_NAME \
        --scale-in-control max-scaled-in-replicas=MAX_SCALE_IN_REPLICAS,time-window=TIME_WINDOW
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG to update.
  * `MAX_SCALE_IN_REPLICAS`: the maximum number of VMs allowed to be deducted from the peak size, taken from the specified trailing time window. The specified number of VM instances can be scaled in all at once, so your service should be able to afford losing this many VMs all at once. You can specify either a number of VMs or a percentage. Use the `%` sign for percentages; for example: `50%`.
  * `TIME_WINDOW`: trailing time window to take the peak size from. Autoscaling won't scale in by more than the maximum allowed number of replicas from the peak size taken during this trailing time window. The value must be between `60` and `3600`.



For example, say you set the time window to 1800 seconds (30 minutes). When calculating the current recommended size for the MIG, the autoscaler uses the following logic:

  * Take the peak size from the last 30 minutes (for example, 100 VMs)
  * Take `max-scaled-in-replicas` (for example, 10 VMs)
  * Set the lower bound of the recommended size to: peak size minus `max-scaled-in-replicas` (100 - 10 = 90 VMs)



###  REST 

Configure scale-in controls by setting the `maxScaledInReplicas` and `timeWindowSec` fields within the `autoscalingPolicy.scaleInControl` structure in a [zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers) or [regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers) autoscaler resource. There are no default values for these fields, you must provide values for both fields.

You can configure scale-in controls when creating an autoscaler or when updating an autoscaler.

**Configuring scale-in controls when creating an autoscaler**

For a zonal MIG, use the [`autoscalers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers/insert). For a regional MIG, use the [`regionAutoscalers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers/insert).
    
    
    POST
    https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/autoscalers
    
    {
      "name": "AUTOSCALER_NAME",
      "target": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME",
      "autoscalingPolicy": {
        "minNumReplicas": 1,
        "maxNumReplicas": 5,
        "coolDownPeriodSec": 60,
        "cpuUtilization": {
          "utilizationTarget": 0.8
        },
        **"scaleInControl": {
          "maxScaledInReplicas": {
               "fixed": MAX_SCALE_IN_REPLICAS
          },
          "timeWindowSec": TIME_WINDOW
        }**
      }
    }
    

For more information about creating an autoscaler, refer to the following articles:

  * [Scaling based on CPU or load balancing serving capacity](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cpu-load-balancing)
  * [Scaling based on Cloud Monitoring metric](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-stackdriver-monitoring-metrics).



**Configuring scale-in controls when updating an autoscaler**

For a zonal MIG, use the [`autoscalers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers/patch). For a regional MIG, use the [`regionAutoscalers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers/patch).
    
    
    PATCH
    https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/autoscalers?autoscaler=AUTOSCALER_NAME
    
    {
      "autoscalingPolicy": {
        "minNumReplicas": 1,
        "maxNumReplicas": 5,
        "coolDownPeriodSec": 60,
        "cpuUtilization": {
          "utilizationTarget": 0.8
        },
        **"scaleInControl": {
          "maxScaledInReplicas": {
               "fixed": MAX_SCALE_IN_REPLICAS
          },
          "timeWindowSec": TIME_WINDOW
        }**
      }
    }
    

Replace the following:

  * `AUTOSCALER_NAME`: the name of the autoscaler to create. You can name your autoscaler after the MIG that will use it or name it something else.
  * `INSTANCE_GROUP_NAME`: the name of the MIG to add the autoscaler to. For a regional MIG, replace `zones/ZONE` with `regions/REGION`.
  * `MAX_SCALE_IN_REPLICAS`: the maximum number of VMs allowed to be deducted from the peak recommended target size, taken from the specified trailing time window. The specified number of VM instances can be scaled in all at once, so your service should be able to afford to lose this many VMs all at once. You can specify either a number of VMs or a percentage. Use the `maxScaledInReplicas.percentage` to specify a percent value.
  * `TIME_WINDOW`: the trailing time window to take the peak recommended size from. Autoscaling won't scale in by more than the maximum allowed number of replicas from the peak recommended size taken during this trailing time window. Specify this value in seconds within the range of `60` and `3600`; for example: `1800`.



For example, say you set the time window to 1800 seconds (30 minutes). When calculating the current recommended size for the MIG, the autoscaler uses the following logic:

  * Take the peak size from the last 30 minutes (for example, 100 VMs)
  * Take `max-scaled-in-replicas` (for example, 10 VMs)
  * Set the lower bound of the recommended size to: peak size minus `max-scaled-in-replicas` (100 - 10 = 90 VMs)



For more information about how scale-in controls work, see [Understanding autoscaler decisions](https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#scale-in_controls).

#### Get current configuration of scale-in controls

To get the current configuration of scale-in controls, see [Getting information about an autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#get_information_about_an_autoscaler).

#### Remove scale-in controls

You can remove scale-in controls to lift restrictions on the timing and magnitude of scale-in operations using the Google Cloud CLI or the Compute Engine API.

Without scale-in controls, the autoscaler still relies on its default [stabilization mechanism](https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#delays_in_scaling_in). Specifically, it maintains a recommended size at a level required to serve peak load, observed during the stabilization period.

###  Console 

To remove scale-in controls for an autoscaled MIG:

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of an autoscaled MIG from the list to open that group's overview page.

  3. Click **Edit**.

  4. Click **Group size & autoscaling** to view and update the group's autoscaling settings.

  5. In the **Scale-in controls** section, clear the **Enable scale-in controls** checkbox.

  6. Click **Save**.




###  gcloud 

Remove scale-in controls by using the `--clear-scale-in-control` flag with the [`gcloud compute instance-groups managed update-autoscaling` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-autoscaling). For example, use the following command to remove scale-in controls from the autoscaling configuration for `example-group`:
    
    
    gcloud compute instance-groups managed update-autoscaling example-group \
        --clear-scale-in-control
    

###  REST 

To remove scale-in controls, use the [`autoscalers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers/patch) for a zonal MIG or use the [`regionAutoscalers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers/patch) for a regional MIG, and provide empty configuration for scale-in controls.
    
    
    PATCH
    https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/autoscalers?autoscaler=AUTOSCALER_NAME
    
    {
      "autoscalingPolicy": {
        "scaleInControl": null
      }
    }
    

Replace the following:

  * `AUTOSCALER_NAME`: the name of the autoscaler to update. To get a list of existing autoscalers and their target MIGs, use the [`autoscalers.aggregatedList` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers/aggregatedList).



### Configure stabilization period

The default stabilization period is `600` seconds. You can configure this value between `0` seconds and `3600` seconds (one hour).

To configure the stabilization period, use one of the following options:

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.autoscalers.create` on the project to create an autoscaler.
  * `compute.autoscalers.update` on the project to update an autoscaler.
  * `compute.instanceGroupManagers.use` on the project.



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of an autoscaled MIG from the list to open that group's overview page.

  3. Click **Edit**.

  4. Click **Group size & autoscaling** to expand the section.

  5. If the MIG doesn't have an autoscaler configured, click **Configure Autoscaling** and do the following:

     1. In the **Minimum number of instances** and **Maximum number of instances** fields, enter the number of instances that the autoscaler should maintain.

     2. A CPU utilization signal is included by default; you can edit it or click **Add a signal** to create another.

     3. In the **Stabilization period** field, enter the duration in seconds. The default value is `600` seconds.

  6. If an autoscaling configuration already exists, in the **Stabilization period** field, enter the duration in seconds. The default value is `600` seconds.

  7. Click **Save**.




###  gcloud 

You can configure the stabilization period when creating or updating an autoscaler.

**Configure stabilization period when creating an autoscaler**

Use the [`gcloud compute instance-groups managed set-autoscaling` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-autoscaling) and include the `--stabilization-period` flag to set the stabilization period.
    
    
    gcloud compute instance-groups managed set-autoscaling INSTANCE_GROUP_NAME \
        --target-cpu-utilization 0.6 \
        --max-num-replicas 50 \
        --stabilization-period STABILIZATION_PERIOD
    

**Configure stabilization period when updating an autoscaler**

Use the [`gcloud compute instance-groups managed update-autoscaling` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/update-autoscaling) and include the `--stabilization-period` flag.
    
    
    gcloud compute instance-groups managed update-autoscaling INSTANCE_GROUP_NAME \
        --stabilization-period STABILIZATION_PERIOD
    

Replace the following:

  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `STABILIZATION_PERIOD`: the duration in seconds. The value must be between `0` and `3600`. For more information, see Best practices for stabilization period in this document.



###  REST 

To configure the stabilization period, use one of the following resources:

  * For a regional MIG, use the [`regionAutoscalers` REST resource](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers)

  * For a zonal MIG, use the [`autoscalers` REST resource](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers)




You can configure the stabilization period when creating or updating an autoscaler.

**Configure the stabilization period when creating an autoscaler**

  * For a zonal MIG, use the [`autoscalers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers/insert).

  * For a regional MIG, use the [`regionAutoscalers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers/insert).



    
    
    POST
    https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/autoscalers
    
    {
      "name": "AUTOSCALER_NAME",
      "target": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/instanceGroupManagers/INSTANCE_GROUP_NAME",
      "autoscalingPolicy": {
        "minNumReplicas": 1,
        "maxNumReplicas": 5,
        "coolDownPeriodSec": 60,
        "cpuUtilization": {
          "utilizationTarget": 0.8
        },
        "stabilizationPeriodSec": STABILIZATION_PERIOD
      }
    }
    

**Configure the stabilization period when updating an autoscaler**

  * For a zonal MIG, use the [`autoscalers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers/patch).

  * For a regional MIG, use the [`regionAutoscalers.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers/patch).



    
    
    PATCH
    https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/autoscalers?autoscaler=AUTOSCALER_NAME
    
    {
      "autoscalingPolicy": {
        "minNumReplicas": 1,
        "maxNumReplicas": 5,
        "coolDownPeriodSec": 60,
        "cpuUtilization": {
          "utilizationTarget": 0.8
        },
        "stabilizationPeriodSec": STABILIZATION_PERIOD
      }
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `AUTOSCALER_NAME`: the name of the autoscaler.
  * `INSTANCE_GROUP_NAME`: the name of the MIG.
  * `STABILIZATION_PERIOD`: the duration in seconds. The value must be between `0` and `3600`. For more information, see Best practices for stabilization period in this document.



#### Best practices for stabilization period

As a best practice, configure the stabilization period depending on the type of your workload as follows:

  * **Volatile workloads** : If your application has highly varying traffic, then maintain the default stabilization period of 600 seconds (10 minutes) or longer. This duration can help avoid the overhead of frequent instance creation and deletion.

  * **Fast-scaling web services** : If your application initializes quickly (in seconds) and you want to reduce costs aggressively, then consider reducing the stabilization period to between `180` and `240` seconds. This duration can help to scale in quickly.

  * **Workloads with session affinity** : If your application requires the same VM instance to handle client requests for an extended period, even after load decreases, then use a longer stabilization period—for example, `1800` seconds.

  * **Setting to`0`**: Only set the stabilization period to `0` if your application can handle immediate capacity reductions without impacting user latency, and you have no concerns about the overhead of frequent instance creation and deletion caused by rapid fluctuations in load signals.




Additionally, we recommend that you set a stabilization period that is longer than the [initialization period](https://docs.cloud.google.com/compute/docs/autoscaler#cool_down_period) to avoid deleting instances before new ones are fully ready to serve.

## Delete an autoscaler

You can permanently delete your autoscaler resource, and its history. If you want to temporarily stop autoscaling and keep your autoscaler resource and its configuration and history, disable your autoscaler instead.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.autoscalers.delete` on the project



###  Console 

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of a MIG from the list to open that group's overview page.

  3. Click **Edit**.

  4. Click **Group size & autoscaling** to view and update the group's autoscaling settings.

  5. In the **Autoscaling mode** list, select **Delete autoscaling configuration** to stop the autoscaler and delete its configuration.

  6. Click **Save** when you are done.




###  gcloud 

Use the [`stop-autoscaling` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/stop-autoscaling) to stop an autoscaler and delete its configuration.
    
    
    gcloud compute instance-groups managed stop-autoscaling INSTANCE_GROUP_NAME

Stopping an autoscaler deletes it from the MIG. If you want to restart the autoscaler, you must recreate it by using the [`set-autoscaling` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-autoscaling).

If you delete a MIG using the gcloud CLI, any autoscalers attached to the MIG are also deleted.

###  REST 

To stop an autoscaler and delete its configuration, use the [`autoscalers.delete` method](https://docs.cloud.google.com/compute/docs/reference/latest/autoscalers/delete) for a zonal MIG or use the [`regionAutoscalers.delete` method](https://docs.cloud.google.com/compute/docs/reference/latest/regionAutoscalers/delete) for a regional MIG.
    
    
     DELETE https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/autoscalers/AUTOSCALER_NAME

## Feedback

We want to learn about your use cases, challenges, and feedback about autoscaling. Share your feedback with our team at [mig-discuss@google.com](mailto:mig-discuss@google.com).

## What's next

  * Learn [how autoscalers make decisions](https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions).
  * Learn how to use [multiple autoscaling signals](https://docs.cloud.google.com/compute/docs/autoscaler/multiple-policies) to scale your group.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
