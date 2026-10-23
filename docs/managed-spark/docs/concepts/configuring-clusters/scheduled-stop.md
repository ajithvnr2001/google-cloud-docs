---
url: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/scheduled-stop/
title: Cluster Scheduled Stop \u00a0|\u00a0 Managed Service for Apache Spark \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:00.698418+00:00
---

# Cluster Scheduled Stop  |  Managed Service for Apache Spark  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/scheduled-stop/

"Managed Service for Apache Spark" is the new name for the product formerly known as "Dataproc on Compute Engine" (cluster deployment) and "Google Cloud Serverless for Apache Spark" (serverless deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Spark ](https://docs.cloud.google.com/managed-spark/docs)
  * [ Guides ](https://docs.cloud.google.com/managed-spark/docs/overview/key-concepts)



Send feedback 

#  Cluster Scheduled Stop Stay organized with collections  Save and categorize content based on your preferences. 

To avoid incurring [Google Cloud charges](https://docs.cloud.google.com/managed-spark/docs/resources/pricing) for an inactive cluster, or the need to delete and recreate a cluster to avoid incurring cluster charges, use the Managed Service for Apache Spark cluster scheduled stop feature, which stops all cluster VMs. You aren't charged for stopped VMs, but charges continue for associated resources, such as persistent disks.

Stopping a cluster stops all cluster VMs and causes any running jobs to fail. WHen a cluster is stopped, you can't update the cluster, submit jobs to the cluster, or access optional components on the cluster using the [Managed Service for Apache Spark Component Gateway](https://docs.cloud.google.com/managed-spark/docs/concepts/accessing/gateways). After stopping a cluster, you can [restart](https://docs.cloud.google.com/managed-spark/docs/guides/start-stop) the cluster, and resume work.

Cluster scheduled stop is available for clusters created with 2.2.42+ , 2.1.76+, and 2.0.57+, and later image versions.

## Features

  * You can stop clusters after a specified idle period, at a specified future time, or after a specified period from the cluster creation request.

  * Cluster scheduled stop supports clusters with secondary workers and zero scale clusters.

  * You can update or cancel the cluster scheduled stop configuration.




## Limitations and considerations

  * Cluster scheduled stop isn't supported for clusters with [local SSDs](https://docs.cloud.google.com/managed-spark/docs/concepts/compute/local-ssds).
  * Although you can update a cluster scheduled stop configuration, an initiated stop operation will continue. To check if the stop operation has started, examine cluster logs in Cloud Logging.
  * Updating a stop schedule on a cluster that has past scheduled stop time removes the scheduled stop configuration. To re-enable the scheduled stop, include a future time in your update request.



## Actions that disable cluster scheduled stop

While a cluster is running, the following actions disable cluster scheduled stop until the disabling action is reversed:

  * Removing IAM [Managed Service for Apache Spark Service Agent role](https://docs.cloud.google.com/iam/docs/roles-permissions/dataproc#dataproc.serviceAgent) on the [Dataproc Service Agent service account](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#service_agent_control_plane_identity)
  * Disabling the Managed Service for Apache Spark API in the cluster project
  * Enabling [VPC-Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs) if the Managed Service for Apache Spark [Service Agent service account (Control plane identity)](https://docs.cloud.google.com/managed-spark/docs/concepts/iam/principals#service_agent_control_plane_identity) isn't within the perimeter boundary



## Cluster idle time calculation

For a cluster to be considered idle, the following conditions must be met:

  * cluster creation is finished (time taken for cluster provisioning and startup is excluded from the idle time calculation)
  * no jobs are running on the cluster
  * the cluster isn't in a `STOPPED` state



Submitting a job to the cluster or stopping a cluster resets the idle time calculation.

The `dataproc:dataproc.cluster-ttl.consider-yarn-activity` [cluster property](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/cluster-properties#service_properties) affects the calculation of cluster idle time, as follows:

  * This property is enabled (set to `true`) by default.
  * When this property is enabled, both YARN and Managed Service for Apache Spark Jobs API activity must be idle to start and continue incrementing the cluster idle time calculation. 
    * YARN activity includes pending and running YARN applications.
    * Managed Service for Apache Spark Jobs API activity includes pending and running jobs submitted to the Managed Service for Apache Spark Jobs API.
  * When this property is set to `false`, the cluster idle time calculation starts and continues only when Managed Service for Apache Spark Jobs API activity is idle.



## Use Cluster Scheduled Stop

### Google Cloud console

You can set scheduled stop values when you create a cluster using the Google Cloud console as follows:

  1. Open the [**Create cluster**](https://console.cloud.google.com/dataproc/clusters/create) page. 
  2. Under **Define cost control settings** Select **Set an optional retention policy to control costs** , then select cluster stop (or cluster deletion) settings. 



### gcloud CLI

You can set scheduled stop values when you create a cluster using the Google Cloud CLI or Managed Service for Apache Spark API. After you create the cluster, you can update the cluster to change or delete cluster scheduled stop values previously set on the cluster.

Flag | Description | Finest Granularity | Min Value | Max Value  
---|---|---|---|---  
`--stop-max-idle`**1** | Applies to cluster create and cluster update commands. The duration from the moment when the cluster enters the idle state (after creation or startup) to the moment when the cluster begins to stop. Provide the duration in `IntegerUnit` format, where the unit can be "s, m, h, d" (seconds, minutes, hours, days, respectively). Examples: "30m" or "1d" (30 minutes or 1 day from when the cluster becomes idle). | 1 second | 5 minutes | 14 days  
`--no-stop-max-idle` | Applies to cluster update command only. Cancels cluster scheduled stop by previously set `--stop-max-idle` flag | Not applicable | Not applicable | Not applicable  
`--stop-expiration-time`**2** | Applies to cluster create and cluster update commands. The time to begin stopping the cluster in [ISO 8601 datetime format](https://www.iso.org/iso-8601-date-and-time-format.html). You can generate the datetime in correct format using the [Timestamp Generator](http://www.timestampgenerator.com/). For example, "2017-08-22T13:31:48-08:00" specifies an expiration time of 13:21:48 in the UTC -8:00 time zone.| 1 second| 10 minutes from the current time  | 14 days from the current time  
`--stop-max-age`**2** | Applies to cluster create and cluster update commands. The duration from the moment of submitting the cluster create request to the moment when the cluster begins to stop. Provide the duration in `IntegerUnit` format, where the unit can be "s, m, h, d" (seconds, minutes, hours, days). Examples: "30m": 30 minutes from now; "1d": 1 day from now. | 1 second | 10 minutes | 14 days  
Notes: 

  1. You can pass the `stop-max-idle` flag with either the `stop-expiration-time` or `stop-max-age` flag in your cluster create or update request. The first to become true takes effect to stop the cluster.
  2. You can pass either thec`stop-expiration-time` flag or the `stop-max-age` flag to the cluster create or update command, but not both.



Cluster creation example:
    
    
    gcloud dataproc clusters create CLUSTER_NAME \
        --region=REGION \
        --stop-max-idle=DURATION \
        --stop-expiration-time=TIME \
        ... other flags ...
    

Cluster update example:

For example:
    
    
    gcloud dataproc clusters update CLUSTER_NAME \
        --region=REGION \
        --stop-max-idle=DURATION \
        --no-stop-max-age \
        ... other flags
    

### REST API

You can create or update scheduled stop values on a cluster by setting the Managed Service for Apache Spark API [ClusterLifecycleConfig](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/ClusterConfig#lifecycleconfig) fields and values listed in the following table as part of a Managed Service for Apache Spark [cluster.create](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/create) or [cluster.patch](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/patch) API request.

Flag | Description | Finest Granularity | Min Value | Max Value  
---|---|---|---|---  
`idleStopTtl`**1** | Applies to cluster create and cluster update commands. The duration from the moment when the cluster enters the idle state after the cluster is created or updated to the moment when the cluster begins to stop. Provide a duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". Submit a `cluster.patch` request with an empty duration to cancel a previously set `idleDeleteTtl` value. | 1 second | 5 minutes  
| 14 days  
`autoStopTime`**2** | Applies to cluster create and cluster update commands. The time to begin stopping the cluster. Provide a timestamp in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z". | 1 second | 10 minutes from the current time | 14 days from the current time  
`autoStopTtl`**2** | The duration from the moment of submitting the cluster create or update request to the moment when the cluster begins to stop. Provide a duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s". | 1 second | 10 minutes.  
Submit a `cluster.patch` request with an empty duration to cancel a previously set `autoStopTtl` value. | 14 days  
Notes: 

  1. You can pass the `stop-max-idle` flag with either the `stop-expiration-time` or `stop-max-age` flag in your cluster create or update request. The first to become true takes effect to stop the cluster.
  2. You can pass either thec`stop-expiration-time` flag or the `stop-max-age` flag to the cluster create or update command, but not both.



### Using scheduled stop with scheduled deletion

If you use both cluster scheduled stop with [cluster scheduled deletion](https://docs.cloud.google.com/managed-spark/docs/concepts/configuring-clusters/scheduled-deletion), when creating or updating a cluster, note the following constraints:

  * The `stop-max-idle` period must be shorter than or equal to the `delete-max-idle` period, or the period resulting from `delete-max-age` or `delete-expiration-time`.

  * The `stop-max-age` and `stop-expiration-time` must be later than `delete-max-age` and `delete-expiration-time` respectively.




## View Scheduled Stop cluster settings

### Google Cloud console

  * You can view cluster scheduled stop settings by selecting the cluster name from the Managed Service for Apache Spark [Clusters page](https://console.cloud.google.com/dataproc/clusters) in the Google Cloud console.
  * From the clusters details page, select the **Configuration** tab. Go to the cluster configuration list to view scheduled stop settings.



### gcloud CLI

You can use the `gcloud dataproc clusters list` command to confirm that a cluster has scheduled stop enabled.
    
    
     gcloud dataproc clusters list \
         --region=REGION
    

Sample output:
    
    
    ...
    NAME         WORKER_COUNT ... SCHEDULED_STOP
    CLUSTER_ID   NUMBER       ... enabled
    ...
    

You can use the `gcloud dataproc clusters describe` command to check cluster `LifecycleConfig` scheduled stop settings. 
    
    
    gcloud dataproc clusters describe CLUSTER_NAME \
        --region=REGION
    

Sample output:
    
    
    ...
    lifecycleConfig:
      autoStopTime: '2018-11-28T19:33:48.146Z'
      idleStopTtl: 1800s
      idleStartTime: '2018-11-28T18:33:48.146Z'
    ...
    

The `autoStopTime` and `idleStopTtl` values are set by the user. Managed Service for Apache Spark generates the `idleStartTime` value, which is the latest cluster idle start time.

While Managed Service for Apache Spark calculates `idleStartTime` based on the cessation of job activity, the mechanism for scheduled cluster stopping considers both the `idleStartTime` and the cluster's last start time. Specifically, if a cluster is stopped either by a user or by Managed Service for Apache Spark, the idle calculation for the scheduled stop feature is reset. This means the countdown to a scheduled stop restarts upon the cluster next start. However, the `idleStartTime` itself isn't reset when a stopped cluster is restarted. It continues to reflect the last occurrence of job inactivity prior to the stop.

Therefore, two conditions must be met for Managed Service for Apache Spark to stop a cluster based on the `idleStopTtl`:

  1. The cluster must have been idle for the duration specified by `idleStopTtl` since it was last started. 
  2. The cluster must have been idle for the duration specified by `idleStopTtl` since the last `idleStartTime` reset. 



### REST API

You can make a [`clusters.list`](https://docs.cloud.google.com/managed-spark/docs/reference/rest/v1/projects.regions.clusters/list) request to confirm that a cluster has scheduled stop enabled.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
