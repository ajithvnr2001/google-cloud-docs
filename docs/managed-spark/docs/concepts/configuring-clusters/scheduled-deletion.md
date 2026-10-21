---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/scheduled-deletion/
title: Cluster Scheduled Deletion \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-18T05:42:44.862350+00:00
---

# Cluster Scheduled Deletion  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/scheduled-deletion/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Cluster Scheduled Deletion Stay organized with collections  Save and categorize content based on your preferences. 

To help avoid incurring [Google Cloud charges](https://docs.cloud.google.com/managed-spark/docs/resources/pricing) for an inactive cluster, use the Managed Service for Apache Spark Cluster Scheduled Deletion feature when you create a cluster. This feature provides options to delete a cluster upon the happening of the following events:

  * after a specified cluster idle period
  * at a specified future time
  * after a specified period that starts from the time of submission of the cluster creation request

**Note:** Jobs running on a cluster when the cluster is deleted will fail.

## Actions that disable scheduled deletion

While a cluster is running, the following actions disable scheduled deletion until the disabling action is reversed:

  * Removing IAM [Managed Service for Apache Spark Service Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) on the [Dataproc Service Agent service account](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#service_agent_control_plane_identity)
  * Disabling the Dataproc API in the cluster project
  * Enabling [Compute Engine VM deletion protection](https://docs.cloud.google.com/compute/docs/instances/preventing-accidental-vm-deletion) on a scheduled deletion cluster VM
  * Enabling [VPC-Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs) if the Managed Service for Apache Spark [Service Agent service account (Control plane identity)](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#service_agent_control_plane_identity) isn't within the perimeter boundary



## Calculate cluster idle time

You can use scheduled deletion to delete a cluster after a specified cluster idle time. Idle time is calculated after the cluster is created and cluster provisioning is complete. The idle time calculation starts when a cluster has no running jobs.

The `dataproc:dataproc.cluster-ttl.consider-yarn-activity` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#service_properties) affects the calculation of cluster idle time, as follows:

  * This property is enabled (set to `true`) by default.
  * When this property is enabled, both YARN and Dataproc Jobs API activity must be idle to start and continue incrementing the cluster idle time calculation. 
    * YARN activity includes pending and running YARN applications.
    * Dataproc Jobs API activity includes pending and running jobs submitted to the Dataproc Jobs API.
  * When this property is set to `false`, the cluster idle time calculation starts and continues only when Dataproc Jobs API activity is idle.



The `dataproc:dataproc.cluster-ttl.consider-yarn-activity` property applies to clusters created with image versions released on or after `1.4.64`, `1.5.39`, `2.0.13`, and later image versions. For clusters created with earlier image versions, only Dataproc Jobs API activity is considered in calculating cluster idle time.

## Use cluster scheduled deletion

You can set scheduled deletion values when you create a cluster using the Google Cloud CLI, Dataproc API, or Google Cloud console. After you create the cluster, you can update the cluster to change or delete scheduled deletion values previously set on the cluster.

**Note:** When updating a cluster, you can't combine other cluster update flags with scheduled deletion flags

### Google Cloud console

  1. Open the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Under **Define cost control settings** select **Set an optional retention policy to control costs** , then select scheduled deletion (or scheduled stop) settings.



### gcloud CLI

You can create or update scheduled deletion values on a cluster by passing the flags and values listed in the following table to the [`gcloud dataproc clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/create) or [`gcloud dataproc clusters update`](https://docs.cloud.google.com/sdk/gcloud/reference/dataproc/clusters/update) commands.

gcloud CLI flag | Description | Value granularity | Min value | Max value  
---|---|---|---|---  
`--delete-max-idle`**1** | Applies to cluster create and cluster update commands. The duration from the time when the cluster becomes idle after the cluster is created or updated and is in a ready-to-use state to the moment when the cluster starts to delete. Provide the duration in `IntegerUnit` format, where the unit can be "s, m, h, d" (seconds, minutes, hours, days). Example: "30m": 30 minutes from the moment when the cluster becomes idle. | 1 second | 5 minutes | 14 days  
`--no-delete-max-idle` | Applies to cluster update command only. Cancels cluster deletion by the previous `delete-max-idle` flag setting. | not applicable | not applicable | not applicable  
`--delete-expiration-time`**2** | Applies to cluster create and cluster update commands. The time to start deleting the cluster in [ISO 8601 datetime format](https://www.iso.org/iso-8601-date-and-time-format.html). To generate the datetime in correct format, you can use the [Timestamp Generator](http://www.timestampgenerator.com/). For example, "2017-08-22T13:31:48-08:00" specifies an expiration time of 13:21:48 in the UTC -8:00 time zone.| 1 second | 10 minutes from the current time  | 14 days from the current time  
`--delete-max-age`**2** | Applies to cluster create and cluster update commands. The duration from the moment of submitting the cluster create request to the moment when the cluster starts to delete. Provide the duration in `IntegerUnit` format, where the unit can be "s, m, h, d" (seconds, minutes, hours, days). Examples: "30m": 30 minutes from now; "1d": 1 day from now. | 1 second | 10 minutes | 14 days  
`--no-delete-max-age` | Applies to cluster update command only. Cancels cluster auto-deletion by the previous `delete-max-age` or `delete-expiration-time` flag setting. | Not applicable | Not applicable | Not applicable  
Notes: 

  1. You can pass the `delete-max-idle` flag with either the `delete-expiration-time` or `delete-max-age` flag in your cluster create or update request. The first to become true takes effect to delete the cluster.
  2. You can pass either the `delete-expiration-time` flag or the `delete-max-age` flag to the cluster create or update command, but not both.



Cluster creation example:
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --delete-max-idle=DURATION \
        --delete-expiration-time=TIME \
        ... other flags ...
    

Cluster update example:
    
    
    gcloud dataproc clusters update CLUSTER_NAME \
        --region=REGION \
        --delete-max-idle=DURATION \
        --no-delete-max-age \
        ... other flags
    

### REST API

You can create or update scheduled deletion values on a cluster by setting the Dataproc API [ClusterLifecycleConfig](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#lifecycleconfig) fields and values listed in the following table as part of a Managed Service for Apache Spark [cluster.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) or [cluster.patch](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/patch) API request.

API field | Description | Value granularity | Min value | Max value  
---|---|---|---|---  
`idleDeleteTtl`**1** | Applies to cluster create and cluster update commands. The duration from the time when the cluster becomes idle after the cluster is created or updated and is in a ready-to-use state to the moment when the cluster starts to delete. When updating a cluster with a new value, the new value must be greater than the previously set value. Provide a duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Submit an empty duration to cancel a previously set `idleDeleteTtl` value. | 1 second | 5 minutes | 14 days  
`autoDeleteTime`**2** | Applies to cluster create and cluster update commands. The time to start deleting the cluster. When updating a cluster with a new time, the new time must be later than the previously set time. When updating, if an empty value is set for `autoDeleteTime`, it cancels the existing auto delete.  
Provide a timestamp in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". | 1 second | 10 minutes from the current time | 14 days from the current time  
`autoDeleteTtl`**2** | The duration from the moment of submitting the cluster create or update request to the moment when the cluster starts to delete. When updating a cluster, the new scheduled deletion time (time of the update request plus the new duration) must be later than the previously set cluster deletion time. Submit an empty value to cancel a previously set `autoDeleteTtl` value. Provide a duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". | 1 second | 10 minutes  | 14 days  
Notes: 

  1. You can set or update both `idleDeleteTtl` and either `autoDeleteTime` or `autoDeleteTtl` in your cluster create or update request. The first to become true takes effect to delete the cluster.
  2. You can set or update either `autoDeleteTime` or `autoDeleteTtl` in your request, but not both.



## View Scheduled Deletion cluster settings

### Google Cloud console

  * You can view cluster scheduled deletion settings by selecting the cluster name from the Managed Service for Apache Spark [Clusters page](https://console.cloud.google.com/dataproc/clusters) in the Google Cloud console.
  * From the clusters details page, select the **Configuration** tab. Go to the cluster configuration list to view scheduled deletion settings.



### gcloud CLI

You can use the `gcloud dataproc clusters list` command to confirm that a cluster has scheduled deletion enabled.
    
    
     gcloud dataproc clusters list \
         --region=REGION
    

Sample output: 
    
    
    ...
    NAME         WORKER_COUNT ... SCHEDULED_DELETE
    CLUSTER_ID   NUMBER       ... enabled
    ...
    

You can use the `gcloud dataproc clusters describe` command to check the cluster `LifecycleConfig` scheduled deletion settings.
    
    
    gcloud dataproc clusters describe CLUSTER_NAME \
        --region=REGION
    
    
    
    ...
    lifecycleConfig:
      autoDeleteTime: '2018-11-28T19:33:48.146Z'
      idleDeleteTtl: 1800s
      idleStartTime: '2018-11-28T18:33:48.146Z'
    ...
    

The `autoDeleteTime` and `idleDeleteTtl` are the scheduled deletion configuration values set on the cluster. Managed Service for Apache Spark generates the `idleStartTime` value, which is the latest cluster idle start time. Managed Service for Apache Spark deletes the cluster if the cluster remains idle at `idleStartTime` \+ `idleDeleteTtl`.

### REST API

You can make a [clusters.list](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/list) request to confirm that a cluster has scheduled deletion enabled.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
