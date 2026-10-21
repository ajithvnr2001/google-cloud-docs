---
url: https://docs.cloud.google.com/compute/docs/autoscaler/viewing-autoscaler-logs/
title: View autoscaler logs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:03:15.769665+00:00
---

# View autoscaler logs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/autoscaler/viewing-autoscaler-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  View autoscaler logs Stay organized with collections  Save and categorize content based on your preferences. 

When you enable autoscaling, the autoscaler makes scaling decisions based on the options that you specify. Each scaling decision is logged by [Cloud Logging](https://docs.cloud.google.com/logging/docs). Read these logs in the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) to better understand the autoscaler's scaling decisions.

Using the Logs Explorer, you can see events related to:

  * Autoscaler recommendation for resizing a managed instance group (MIG). If the autoscaler calculates a new recommended size for a MIG, the change in the recommended size is described in the autoscaler logs. See Resize log entry.
  * Changes in autoscaler status. For example, if the autoscaler was working as expected but then encountered an issue, the change in status would be described in the autoscaler logs. See Status change log entry.



## Before you begin

  * Read the [Autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler) documentation.
  * Have an active autoscaler for which you want to view logs.
  * Review how to use the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface).
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




## View autoscaler logs

To view autoscaler logs, use the Google Cloud console, the gcloud CLI, or REST.

###  Console 

If you've turned on autoscaling, then you can see autoscaling logs in the [Google Cloud console](https://console.cloud.google.com/).

  1. Go to the **Logs Explorer** page. 

[Go to Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Pull down the **Resource** drop-down menu and select **Autoscaler**.



You can also navigate to the **Logs Explorer** page from your MIG as follows:

  1. In the Google Cloud console, go to the **Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

  2. Click the name of the MIG for which you want to view the logs.

  3. Click **Monitoring** tab.

  4. In the **Monitoring** tab, the **Logs** panel is at the bottom of the page. Expand the panel by clicking the keyboard_capslock **Toggle panel "Logs"** at the end of this panel.

  5. To open the **Logs explorer** page, click open_in_new **View in logs explorer**.

The log explorer opens with a default query to fetch all autoscaler logs of the MIG.




###  gcloud 

To look up all logs related to autoscaling, use the [`logging read` command](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read). For example:
    
    
    gcloud logging read "resource.type=autoscaler" --limit 10 \
        --format json
    

To view the autoscaler logs of a specific MIG, specify the `instance_group_manager_name` as follows:
    
    
    gcloud logging read "resource.type=autoscaler AND \
        **resource.labels.instance_group_manager_name=example-igm** " \
        --limit 10 --format json
    

To view the log entries related to autoscaler resize actions, specify the `compute.autoscalers.resize` method name:
    
    
    gcloud logging read "resource.type=autoscaler AND \
        resource.labels.instance_group_manager_name=example-igm AND \
        **protoPayload.methodName=compute.autoscalers.resize"** \
        --limit 10 --format json
    

To view the log entries related to autoscaler status changes, specify the `compute.autoscalers.changeStatus` method name:
    
    
    gcloud logging read "resource.type=autoscaler AND \
        resource.labels.instance_group_manager_name=example-igm AND \
        **protoPayload.methodName=compute.autoscalers.changeStatus"** \
        --limit 10 --format json
    

###  REST 

Make a request to the [Logging V2 API](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/entries/list). The request body must contain the `filter` parameter to use when searching for logs and the `project` you want to view logs for. For example, to make a request to get a list of resize actions of a specific MIG:
    
    
    POST https://logging.googleapis.com/v2/entries:list
    
    {
      "filter": "resource.type=autoscaler AND
        resource.labels.instance_group_manager_name=example-igm AND
        protoPayload.methodName=compute.autoscalers.resize",
      "pageSize": 10,
      "resourceNames": [
        "projects/example-project"
      ]
    }
    

To make a request to get a list of status changes of a specific MIG:
    
    
    POST https://logging.googleapis.com/v2/entries:list
    
    {
      "filter": "resource.type=autoscaler AND
        resource.labels.instance_group_manager_name=example-igm AND
        protoPayload.methodName=compute.autoscalers.changeStatus",
      "pageSize": 10,
      "resourceNames": [
        "projects/example-project"
      ]
    }
    

## Resize log entry

When the autoscaler calculates a [recommended size](https://docs.cloud.google.com/compute/docs/autoscaler#recommended_size) for your MIG, Compute Engine creates a log entry. This entry includes the new and old recommended sizes, and the reason for the change in recommendation.

The following is an example of a log entry for a zonal MIG. In this example, based on predictive autoscaling the autoscaler calculated `3` VMs to achieve the CPU utilization target of `35%`. But, the maximum number of instances configured in the autoscaling policy is only `2`. So, the autoscaler limits the recommended size to `2`.
    
    
        {
        insertId: "1l68z7sg4jw7kzo"
        logName: "projects/example-project/logs/cloudaudit.googleapis.com%2Fsystem_event"
        protoPayload: {
          @type: "type.googleapis.com/google.cloud.audit.AuditLog"
          metadata: {
            @type: "type.googleapis.com/autoscaler.AutoscalerSizeChangeExplanation"
            autoscalingMode: "ON"
            **autoscalingReason** : {
              scalingLimit: {
                limitPolicy: {
                  maxNumReplicas: 2
                }
                limitSize: 2
                name: "MAX_INSTANCES"
              }
              scalingSignal: {
                calculatedSize: 3
                calculationDetails: {
                  servingSize: 1
                  signalTarget: 0.35
                  signalValue: 1.03533
                }
                name: "PREDICTED_CPU_UTILIZATION"
                signalPolicy: {
                  coolDownPeriodSec: 15
                  cpuUtilization: {
                    predictiveMethod: "OPTIMIZE_AVAILABILITY"
                    utilizationTarget: 0.35
                  }
                }
              }
              summary: "The autoscaler's recommended size changed from 1 to 2
              because the autoscaler predicted that in 15 seconds the average CPU
              utilization across 1 serving instance will be 103.533%, which is above
              the utilization target of 35%. The calculated size was 3 to achieve
              the target CPU utilization but the size was limited by the maximum
              number of instances set in the autoscaling policy."
            }
            **newSize: 2
            oldSize: 1**
          }
          **methodName: "compute.autoscalers.resize"**
          resourceName: "projects/example-project/zones/us-east1-d/autoscalers/example-autoscaler"
          serviceName: "compute.googleapis.com"
        }
        receiveTimestamp: "2022-06-13T22:34:43.045973046Z"
        resource: {
          labels: {
            autoscaler_id: "1234567890123456789"
            autoscaler_name: "example-autoscaler"
            instance_group_manager_id: "1357908642148074125"
            instance_group_manager_name: "example-igm"
            location: "us-east1-d"
            project_id: "example-project"
          }
          type: "autoscaler"
        }
        severity: "INFO"
        timestamp: "2022-06-13T22:34:42.810216614Z"
        }
    

The following table describes the fields from the log entry:

Property | Value | `autoscalingMode` | The [autoscaling mode](https://docs.cloud.google.com/compute/docs/autoscaler#autoscaling_mode) at the time when the entry was logged. Regardless of the mode, the autoscaler calculates the [recommended size](https://docs.cloud.google.com/compute/docs/autoscaler#recommended_size), which is represented by `newSize` in the log. Depending on the autoscaling mode, the autoscaler resizes the MIG as follows: 

  * `ON`: The autoscaler resizes the MIG to `newSize`.
  * `OFF`: The autoscaler does not resize the MIG.
  * `ONLY_SCALE_OUT`: The autoscaler resizes the MIG only if `newSize` is greater than the target size of the MIG.

  
---|---  
`autoscalingReason` | Details about the reason for autoscaling.   
`autoscalingReason.scalingLimit` | Details about the autoscaling feature that limited the `calculatedSize`, which is the size that autoscaler calculated based on the autoscaling signal. The autoscaling features that can limit the `calculatedSize` are maximum or minimum number of instances, the [scale-in controls](https://docs.cloud.google.com/compute/docs/autoscaler#scale-in_controls), or the [stabilization period](https://docs.cloud.google.com/compute/docs/autoscaler#stabilization_period). If no limit applies to `calculatedSize`, then the `scalingLimit` field does not appear in the logs.   
`autoscalingReason.scalingLimit.limitPolicy` | The configuration of the autoscaling feature that limited the `calculatedSize`. The `limitPolicy` field is not set when stabilization limits the `calculatedSize` because stabilization is a default feature of autoscaling.   
`autoscalingReason.scalingLimit.limitSize` | The number of VMs based on the autoscaling feature that limited the `calculatedSize`.   
`autoscalingReason.scalingLimit.name` | The name of the autoscaling feature that limited the `calculatedSize`.  
`autoscalingReason.scalingSignal` | Details about the autoscaling signal that is used to calculate the number of VMs the MIG should have. If the autoscaling policy has [multiple signals](https://docs.cloud.google.com/compute/docs/autoscaler/multiple-signals), then the autoscaler considers the signal that requires the largest number of VMs.   
`autoscalingReason.scalingSignal.calculatedSize` | The number of VMs that the MIG should have based on the autoscaling signal. If `scalingLimit` applies, then the autoscaler limits `calculatedSize` to `scalingLimit.limitSize`.   
`autoscalingReason.scalingSignal.calculationDetails` | Details used to determine the `calculatedSize`. 

  * `servingSize`: The number of VMs in the MIG excluding the VMs that are still in their [initialization period](https://docs.cloud.google.com/compute/docs/autoscaler#cool_down_period). 
  * `signalTarget`: The target value that the autoscaler maintains for CPU utilization (real-time), predicted CPU utilization, load balancing utilization, or a metric configured with utilization target. 
  * `singleInstanceAssignment`: If scaling is based on a metric value that represents the total amount of work to be done, then [ `singleInstanceAssignment`](https://docs.cloud.google.com/compute/docs/autoscaler/scaling-cloud-monitoring-metrics#configure_autoscaling_based_on_metrics) is the quantity of work that each VM can handle. 
  * `signalValue`: The value of the autoscaling signal. If `signalTarget` is set, then the autoscaler compares the `signalValue` with the `signalTarget` to calculate how many VMs are needed, which is represented by `calculatedSize`. 

  
`autoscalingReason.scalingSignal.name` | The name of the autoscaling signal based on which the autoscaler calculated the number of VMs, represented by `calculatedSize` in the log.   
`autoscalingReason.scalingSignal.signalPolicy` | The configuration of the autoscaling signal based on which the autoscaler determined the `calculatedSize`.   
`autoscalingReason.summary` | A description of the reason for autoscaling.   
`newSize` | The current recommended size of the MIG. Depending on the `autoscalingMode`, the autoscaler resizes the MIG to the `newSize` as follows: 

  * `ON`: The autoscaler resizes the MIG to `newSize`.
  * `OFF`: The autoscaler does not resize the MIG.
  * `ONLY_SCALE_OUT`: The autoscaler resizes the MIG only if `newSize` is greater than the target size of the MIG.

  
`oldSize` | The previous recommended size of the MIG.   
  
For information about the other fields in the log entry, see [Format of audit log entries](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#format_of_audit_log_entries).

## Status change log entry

When the status of the autoscaler changes, Compute Engine creates a log entry capturing the old and new status messages. You can use these status messages to find out why your autoscaler is not behaving as you expect or to debug past issues you noticed. For some of the common status messages, see [Commonly returned status messages](https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions#commonly_returned_status_messages).

The following fields in the `protoPayload` describe the old and new statuses:

  * `metadata.newStatus.details`: The new status of the autoscaler.
  * `metadata.oldStatus.details`: The previous status of the autoscaler.



The following is an example of a log entry that describes a status change. In this example, you might notice the new status message indicating problems with your load balancing configuration.
    
    
        {
          insertId: "ivho6kg4icqfio"
          logName: "projects/example-project/logs/cloudaudit.googleapis.com%2Fsystem_event"
          protoPayload: {
            metadata: {
              @type: "type.googleapis.com/autoscaler.AutoscalerStatusChange"
              **newStatus** : {
                details: "The autoscaler is configured to scale based on a load
                balancing signal but the instance group has not received any
                utilization data from the load balancer or the utilization is
                constantly 0. Check that the load balancing configuration is
                working"
              }
              **oldStatus** : {
                details: "OK"
              },
              **methodName: "compute.autoscalers.changeStatus"**
              resourceName: "projects/example-project/zones/us-east1-b/autoscalers/example-autoscaler"
              serviceName: "compute.googleapis.com"
            }
            receiveTimestamp: "2022-06-08T03:54:12.332329320Z"
            resource: {
              labels: {
                autoscaler_id: "1234567890123456789"
                autoscaler_name: "example-autoscaler"
                instance_group_manager_id: "1357908642148074125"
                instance_group_manager_name: "example-igm"
                location: "us-east1-b"
                project_id: "example-project"
              }
              type: "autoscaler"
            }
            severity: "INFO"
            timestamp: "2022-06-08T03:54:10.675416812Z"
          }
        }
    

For information about the other fields in the log entry, see [Format of audit log entries](https://docs.cloud.google.com/logging/docs/audit/understanding-audit-logs#format_of_audit_log_entries).

## What's next

  * [Update your autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#updating-an-autoscaler) using information that you received from the logs.
  * Learn how [autoscaler makes decisions](https://docs.cloud.google.com/compute/docs/autoscaler/understanding-autoscaler-decisions).
  * Review [autoscaling options](https://docs.cloud.google.com/compute/docs/autoscaler).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
