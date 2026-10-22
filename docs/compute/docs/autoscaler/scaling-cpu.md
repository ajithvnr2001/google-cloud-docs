---
url: https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cpu/
title: Scaling based on CPU utilization \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:07:38.332430+00:00
---

# Scaling based on CPU utilization  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cpu/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Scaling based on CPU utilization Stay organized with collections  Save and categorize content based on your preferences. 

The simplest form of autoscaling is to scale a [managed instance group (MIG)](https://docs.cloud.google.com/compute/docs/instance-groups#managed_instance_groups) based on the CPU utilization of its instances.

You can also autoscale a MIG based on the [load balancing serving capacity](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-load-balancing), [Monitoring metrics](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-stackdriver-monitoring-metrics), or [schedules](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-schedules).

## Before you begin

  * Review the autoscaler [limitations](https://docs.cloud.google.com/compute/docs/autoscaler#specifications).
  * Read about autoscaler [fundamentals](https://docs.cloud.google.com/compute/docs/autoscaler#fundamentals).
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




## Scaling based on CPU utilization

You can autoscale based on the average CPU utilization of a managed instance group (MIG). Using this policy tells the autoscaler to collect the CPU utilization of the instances in the group and determine whether it needs to scale. You set the target CPU utilization the autoscaler should maintain and the autoscaler works to maintain that level.

The autoscaler treats the target CPU utilization level as a fraction of the average use of all vCPUs over time in the instance group. If the average utilization of your total vCPUs exceeds the target utilization, the autoscaler adds more VM instances. If the average utilization of your total vCPUs is less than the target utilization, the autoscaler removes instances. For example, setting a 0.75 target utilization tells the autoscaler to maintain an average utilization of 75% among all vCPUs in the instance group.

To calculate the average CPU utilization of an instance group, the autoscaler uses the `compute.googleapis.com/instance/cpu/utilization` metric, which reports CPU utilization as measured by the hypervisor. The autoscaler doesn't use the CPU utilization that tools such as `top`, Task Manager, or the Ops Agent report from inside the guest operating system. These values can differ from the hypervisor-level measurement.

**Caution:** If your application takes a long time to initialize on new VMs, Google recommends that you don't set a target CPU utilization of 85% or higher. In such a case, if your application sees an increase in traffic, your MIG's CPUs might be at risk of getting overloaded while your application slowly initializes on the new VMs that the autoscaler adds.

You can also scale based on forecasted CPU utilization. For more information, and to see if this is suitable for your workload, see [Scaling based on predictions](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling).

### Enable autoscaling based on CPU utilization

To enable autoscaling based on CPU utilization, use one of the following options. If you want to configure a stabilization period to control the pace of scaling in, then you must use either Google Cloud CLI or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.autoscalers.create` on the project
  * `compute.instanceGroupManagers.use` on the project



###  Console 

  1. In the console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. If you have an instance group, click the name of the instance group, and then click **Edit**. On the edit instance group page, do the following:

     1. Click **Group size & autosclaing** to expand the section.
     2. Click **Configure autoscaling**.
  3. If you don't have an instance group, click **Create instance group** and do the following:

     1. In the **Name** field, specify a name for the group.
     2. In the **Instance template** list, select a template.
     3. In the **Location** section, depending on whether you're creating a zonal or regional MIG, choose an option as follows:

        * For a zonal MIG, select **Single zone** , and then select a region and a zone.
        * For a regional MIG, select **Multiple zones** , and then select a region and zones.
  4. In the **Autoscaling** section, a CPU utilization autoscaling signal is added by default. You can either use the default values for the signal or do the following:

     1. Specify the minimum and the maximum numbers of instances that you want the autoscaler to create in this group.
     2. To edit the target CPU utilization, click the CPU utilization signal to expand the section and specify the percentage.

        1. Under **Predictive autoscaling** , select **Off**. To learn more about predictive autoscaling, and whether it is suitable for your workload, see [Scaling based on predictions](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling).
     3. Click **Done**.

  5. You can use the **Initialization period** to tell the autoscaler how long it takes for your application to initialize. Specifying an accurate initialization period improves autoscaler decisions. For example, when scaling out, the autoscaler ignores data from VMs that are still initializing because those VMs might not yet represent normal usage of your application. The default initialization period is 60 seconds. 

  6. Click **Save**.




###  gcloud 

Use the [`set-autoscaling`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-autoscaling) sub-command to enable autoscaling for a managed instance group. For example, the following command creates an autoscaler that has a target CPU utilization of 60%. Along with the `--target-cpu-utilization` parameter, the `--max-num-replicas` parameter is also required when creating an autoscaler:

**Note:** If autoscaling is already enabled for a managed instance group, the [`set-autoscaling`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/set-autoscaling) command updates the existing autoscaler to the new specifications.
    
    
    gcloud compute instance-groups managed set-autoscaling example-managed-instance-group \
        --max-num-replicas 20 \
        --target-cpu-utilization 0.60 \
        --cool-down-period 90 \
        --stabilization-period 240
    

Optionally, set the following flags to control autoscaling: 

  * You can use the `--cool-down-period` flag to set the initialization period, which tells the autoscaler how long it takes for your application to initialize. Specifying an accurate initialization period improves autoscaler decisions. For example, when scaling out, the autoscaler ignores data from VMs that are still initializing because those VMs might not yet represent normal usage of your application. The default initialization period is 60 seconds. 
  * You can use the `--stabilization-period` flag to set the stabilization period, which determines the duration for your MIG to scale in. A shorter stabilization period indicates quicker VM deletion to scale in. The value must be between `0` seconds and `3600` seconds. The default value is `600` seconds. For more information, see [Best practices for stabilization period](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#stabilization-period-best-practices).



Optionally, you can enable predictive autoscaling to scale out ahead of predicted load. To learn whether predictive autoscaling is suitable for your workload, see [Scaling based on predictions](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling).

You can verify that autoscaling is successfully enabled by using the [`instance-groups managed describe` sub-command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed/describe), which describes the corresponding managed instance group and provides information about any autoscaling features for that instance group:
    
    
    gcloud compute instance-groups managed describe example-managed-instance-group

For a list of available `gcloud` commands and flags, see the [`gcloud` reference](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instance-groups/managed).

###  REST 

**Note:** Although autoscaling is a feature of managed instance groups, it is a separate API resource. Keep that in mind when you construct API requests for autoscaling.

To create an autoscaler, use the [`autoscalers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/autoscalers/insert) for a zonal MIG or the [`regionAutoscalers.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionAutoscalers/insert) for a regional MIG.

The following example creates an autoscaler for a zonal MIG:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/autoscalers

Your request body must contain the `name`, `target`, and `autoscalingPolicy` fields. `autoscalingPolicy` must define `cpuUtilization` and `maxNumReplicas`.

Optionally, set the following fields to control autoscaling: 

  * You can use the `coolDownPeriodSec` field to set the initialization period, which tells the autoscaler how long it takes for your application to initialize. Specifying an accurate initialization period improves autoscaler decisions. For example, when scaling out, the autoscaler ignores data from VMs that are still initializing because those VMs might not yet represent normal usage of your application. The default initialization period is 60 seconds. 
  * You can use the `stabilizationPeriodSec` field to set the stabilization period, which determines the duration for your MIG to scale in. A shorter stabilization period indicates quicker VM deletion to scale in. The value must be between `0` seconds and `3600` seconds. The default value is `600` seconds. For more information, see [Best practices for stabilization period](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#stabilization-period-best-practices).



Optionally, you can enable predictive autoscaling to scale out ahead of predicted load. To learn whether predictive autoscaling is suitable for your workload, see [Scaling based on predictions](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling).
    
    
    {
      "name": "example-autoscaler",
      "target": "https://www.googleapis.com/compute/v1/projects/myproject/zones/us-central1-f/instanceGroupManagers/example-managed-instance-group",
      "autoscalingPolicy": {
        "maxNumReplicas": 10,
        "cpuUtilization": {
          "utilizationTarget": 0.6
        },
        "coolDownPeriodSec": 90,
        "stabilizationPeriodSec": 240
      }
    }
    

For more information about enabling autoscaling based on CPU utilization, complete the tutorial, [Using autoscaling for highly scalable apps](https://docs.cloud.google.com/compute/docs/tutorials/high-scalability-autoscaling).

### How autoscaler handles heavy CPU utilization

During periods of heavy CPU utilization, if utilization is close to 100%, the autoscaler estimates that the group might already be heavily overloaded. In these cases, the autoscaler increases the number of virtual machines by 50% at most.

**Note:** This behavior might change in the future. Google recommends that you not rely on this behavior.

## What's next

  * Learn how to enable [predictive autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler/predictive-autoscaling).
  * Learn about [managing autoscalers](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers).
  * Learn [how autoscalers make decisions](https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions).
  * Learn how to use [multiple autoscaling signals](https://docs.cloud.google.com/compute/docs/autoscaler/multiple-policies) to scale your group.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
