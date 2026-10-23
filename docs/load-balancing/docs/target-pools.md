---
url: https://docs.cloud.google.com/load-balancing/docs/target-pools/
title: Using target pools \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:57.259788+00:00
---

# Using target pools  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/target-pools/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Using target pools Stay organized with collections  Save and categorize content based on your preferences. 

A target pool is a group of backend instances that receive incoming traffic from regional external passthrough Network Load Balancers. All backend instances of a target pool must reside in the same Google Cloud region. [Regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network) can use either a backend service or a target pool to define the group of backend instances. If you're creating new regional external passthrough Network Load Balancers, we recommend [using backend services](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service).

This page describes configuration options for target pool backends. When a regional external passthrough Network Load Balancer's forwarding rule directs traffic to a target pool, the load balancer chooses an instance from the target pool based on a [hash](https://docs.cloud.google.com/load-balancing/docs/network#load_distribution_algorithm) of the source IP address, the source port, the destination IP address, and the destination port.

If you intend your target pool to contain a single virtual machine (VM), consider using the [protocol forwarding](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding) feature instead of load balancing.

**Note:** This page describes how to configure a specific load balancer component or feature before or after you've already created a load balancer. Working with specific components is useful for advanced configurations and necessary for some configuration options. Before using the information on this page, know the [type of Google Cloud load balancer](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) that you need.

## Target pool properties

Target pools work with forwarding rules that handle `TCP` and `UDP` traffic. You must create a target pool before you can use it with a forwarding rule.

Target pools use [legacy HTTP health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts#category_and_protocol).

A target pool is made up of the following properties:

`name`
    The name of this target pool. The name must be unique in this project, from 1-63 characters long and match the regular expression: `[a-z]([-a-z0-9]*[a-z0-9])?`, which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.
`description`
    _Optional._ A user-defined description of this target pool.
`region`
    

The fully qualified URL of the target pool's region. The region should be the same region where your backend instances reside. For example:

"region" : "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION"

`healthChecks[ ]`
    

_Optional._ An optional list of health checks for this target pool. Only one health check can be attached to a particular target pool. See [Health checking](https://docs.cloud.google.com/load-balancing/docs/health-checks) for more information.

`instances[ ]`
    

A list of instance URLs that should handle traffic for this target pool. All instances must reside in the same region as the target pool, but instances can belong to different zones within a single region. For example:
    
    
    "instances" : [
      "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE",
      "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE-2"
    ]

`sessionAffinity`
    

_Optional._ Controls the method used to select a backend virtual machine instance. You can only set this value during the creation of the target pool. Once set, you cannot modify this value. The hash method selects a backend based on a subset of the following 5 values:

  * Source / Destination IP
  * Source / Destination Port
  * Layer 4 Protocol (TCP, UDP)



Possible hashes are:

`NONE` (i.e., no hash specified) (default)
    5-tuple hashing, which uses the source and destination IPs, source and destination ports, and protocol. Each new connection can end up on any instance, but all traffic for a given connection will stay on the same instance, if the instance stays healthy.
`CLIENT_IP_PROTO`
    3-tuple hashing, which uses the source and destination IPs and the protocol. All connections from a client will end up on the same instance as long as they use the same protocol and the instance stays healthy.
`CLIENT_IP`
    2-tuple hashing, which uses the source and destination IPs. All connections from a client will end up on the same instance regardless of protocol as long as the instance stays healthy.

5-tuple hashing provides a good distribution of traffic across many virtual machines. However, a second session from the same client may arrive on a different instance because the source port may change. If you want all sessions from the same client to reach the same backend, as long as the backend stays healthy, you can specify `CLIENT_IP_PROTO` or `CLIENT_IP` options.

In general, if you select a 3-tuple or 2-tuple method, it will provide for better session affinity than the default 5-tuple method, but the overall traffic may not be as evenly distributed.

**Fragmented UDP packets** : If you are load balancing UDP traffic that is likely to be fragmented, set session affinity to `CLIENT_IP_PROTO` or `CLIENT_IP`. Don't use `NONE` (5-tuple hashing). This is because UDP fragments other than the first one don't carry the port number, and the load balancer may drop the fragments without the port. See [Load balancing and fragmented UDP packets](https://docs.cloud.google.com/load-balancing/docs/network/networklb-target-pools#load_balancing_and_fragmented_udp_packets) for more information.

**Caution:** If a large percentage of your clients are behind a proxy server, don't use `CLIENT_IP_PROTO` or `CLIENT_IP`. Using them sends all traffic from those clients to the same instance.
`backupPool`
    

_Optional._ A fully qualified URL to another target pool resource. A backup pool is a target pool that another target pool references. You must also define `failoverRatio` to use this feature. If the ratio of healthy virtual machines in your target pool falls below the `failoverRatio`, the regional external passthrough Network Load Balancer sends traffic to your backup pool. You can only provide one backup pool per target pool. The backup pool must be in the same region as the target pool. If the ratio of healthy instances in your target pool falls below your configured failover ratio, the regional external passthrough Network Load Balancer uses the following rules to route your traffic:

  1. If the ratio of healthy instances to total instances in the target pool is less than the failover ratio, traffic is sent to healthy instances in the backup pool.
  2. If the ratio of healthy instances to total instances in the target pool is less than the failover ratio but there are no remaining healthy instances in the backup pool, traffic is sent to the remaining healthy instances in the target pool.
  3. If the target pool is not empty and if all instances in both the target pool and the backup pool fail their health checks, traffic is sent to all instances in the target pool, as a last resort.
  4. If the target pool is empty and if all instances in the backup pool fail their health checks, traffic is sent to all instances in the backup pool, as a last resort.



Only one level of failover is supported. For example, if target pool A has backup pool B, and backup pool B has backup pool C, then traffic intended for target pool A can only be directed to backup pool B and not to backup pool C.

`failoverRatio`
    

_Optional._ A float between `0.0` and `1.0`, which determines when this target pool is declared unhealthy. For example, if this value is set to `0.1`, then this target pool is declared unhealthy if the number of healthy instances are less than `0.1` (10%). If the failover ratio is `0.0`, then at least one backend must be healthy for the pool to be considered healthy. If the failover ratio is set to `1.0`, then all instances must be healthy for the pool to be considered healthy. You must define this if you define the `backupPool` field.

## Failover conditions

Conditions | New connections go to  
---|---  
Failover ratio !=0, healthy VMs in target pool >= FR  | target pool  
Failover ratio =0, healthy VMs in target pool > 0  | target pool   
Failover ratio !=0, healthy VMs in target pool < FR, and at least one VM in the backup pool is healthy  | backup pool  
Failover ratio =0, healthy VMs in target pool = 0, and at least one VM in the backup pool is healthy  | backup pool  
At least one VM is in the target pool, and all VMs in the target pool are unhealthy, and all VMs in the backup pool are unhealthy  | target pool (last resort)  
No VMs are in the target pool, and all VMs in the backup pool are unhealthy | backup pool (last resort)  
No VMs are in the target pool, and no VMs are in the backup pool | Traffic is dropped  
  
## Create a target pool

###  Console 

Target pools can't be created in the Google Cloud console. You can create a target pool by using the Google Cloud CLI or the API.

To learn how to create a target pool-based regional external passthrough Network Load Balancer by using the Google Cloud CLI, see [Set up a regional external passthrough Network Load Balancer with a target pool](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network).

###  gcloud 

To use `gcloud compute` to create a target pool, use the [`target-pools create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-pools/create):
    
    
      gcloud compute target-pools create TARGET_POOL \
          [--backup-pool=BACKUP_POOL] \
          [--description=DESCRIPTION] \
          [--failover-ratio=FAILOVER_RATIO] \
          [--http-health-check=HEALTH_CHECK] \
          [--region=REGION]
          [--session-affinity=SESSION_AFFINITY; default="NONE"]
    

Replace the following:

  * `TARGET_POOL`: a name for the target pool
  * `BACKUP_POOL`: a name for the backup target pool
  * `DESCRIPTION`: a description of the target pool
  * `FAILOVER_RATIO`: a value between 0.0 and 1.0, which determines when the target pool is declared unhealthy
  * `HEALTH_CHECK`: a health check for this target pool
  * `REGION`: a region of the target pool
  * `SESSION_AFFINITY`: the method used to select a backend virtual machine instance



###  API 

To create a target pool in the API, make a `HTTP POST` request to the following URI: 
    
    
      https://www.googleapis.com/v1/compute/projects/PROJECT_ID/regions/REGION/targetPools
      {
        "name": name,
        "instances": [
           "https://www.googleapis.com/v1/compute/project/PROJECT_ID/zones/ZONE/instances/INSTANCE",
           "https://www.googleapis.com/v1/compute/project/PROJECT_ID/zones/ZONE/instances/INSTANCE-2",
        ]
      }
     

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID
  * `ZONE`: the zone that the target pool's instances are in
  * `INSTANCE`, `INSTANCE-2`: the instances to be added to the target pool



## Add or remove an instance from a target pool

###  Console 

Target pools can't be edited in the Google Cloud console. You can edit a target pool by using the Google Cloud CLI or the API.

###  gcloud 

To use `gcloud compute` to add instances to a target pool, use the [`target-pools add-instances` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-pools/add-instances):
    
    
      gcloud compute target-pools add-instances TARGET_POOL \
          --instances=INSTANCE,[INSTANCE-2,...]
    

Replace the following:

  * `TARGET_POOL`: the name of the target pool
  * `INSTANCE`, `INSTANCE-2`: the name of the instance (or instances) to be added to the target pool



To remove instances, use the [`target-pools remove-instances` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-instances):
    
    
      gcloud compute target-pools remove-instances TARGET_POOL \
          --instances=INSTANCE,[INSTANCE-2,...]
    

Replace the following:

  * `TARGET_POOL`: the name of the target pool
  * `INSTANCE`, `INSTANCE-2`: the name of the instance (or instances) to be removed from the target pool

**Note:** Removing an instance from a target pool without draining it first breaks all TCP sessions to that instance. To remove an instance safely, first drain the instance by making it fail its [health check](https://docs.cloud.google.com/load-balancing/docs/health-checks). After TCP sessions close, remove the instance from the pool.

###  API 

In the API, send a POST request to the following URIs:
    
    
      https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/targetPools/TARGET_POOL/removeInstance
      https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/targetPools/TARGET_POOL/addInstance
    

The body of your request should include the fully qualified URIs to the instances that you want to add or remove:
    
    
      {
       "instances": [
          {"instance": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE"},
          {"instance": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE-2"}
        ]
      }
     

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID
  * `TARGET_POOL`: the name of the target pool to be updated
  * `REGION`: the region that the target pool is in
  * `ZONE`: the zone that the updated instances are in
  * `INSTANCE`, `INSTANCE-2`: the instances to be added to the target pool



For more information, see the API reference documentation for the [`targetPools.addInstance`](https://docs.cloud.google.com/compute/docs/reference/latest/targetPools/addInstance) and [`targetPools.removeInstance`](https://docs.cloud.google.com/compute/docs/reference/latest/targetPools/removeInstance) methods.

## List target pools

###  Console 

To see a list of target pools, use the load balancing advanced menu.

On the **Advanced** load balancing page, go to the **Target pools** tab.   
[Go to Target pools](https://console.cloud.google.com/loadbalancing/advanced/targetPools/list)

The page displays a list of target pools.

###  gcloud 

To use `gcloud compute` to list existing target pools, use the [`target-pools list` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-pools/list):
    
    
      gcloud compute target-pools list
    

For more verbose output, use the `describe` command and specify a pool name.

###  API 

In the API, send a GET request to the following URI:
    
    
      https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/targetPools
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID
  * `REGION`: the region that the target pool is in



## Describe a target pool

###  Console 

To get information about a target pool, use the load balancing advanced menu.

  1. On the **Advanced** load balancing page, go to the **Target pools** tab.   
[Go to Target pools](https://console.cloud.google.com/loadbalancing/advanced/targetPools/list)
  2. To see detailed information, click the name of the target pool.



###  gcloud 

To use `gcloud compute` to get information about a single target pool, use the [`target-pools describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-pools/describe):
    
    
      gcloud compute target-pools describe TARGET_POOL
    

Replace `TARGET_POOL` with the name of the target pool.

###  API 

In the API, send an empty GET request to the following URI:
    
    
      https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/targetPools/TARGET_POOL
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID
  * `TARGET_POOL`: the name of the target pool to be updated
  * `REGION`: the region that the target pool is in



## Get the health status of instances

###  Console 

To get the health status of instances in a target pool, use the load balancing advanced menu.

  1. On the **Advanced** load balancing page, go to the **Target pools** tab.   
[Go to Target pools](https://console.cloud.google.com/loadbalancing/advanced/targetPools/list)
  2. Click the name of the target pool.
  3. The **Target pool details** page lists all the instances and their health status.



###  gcloud 

To use `gcloud compute` to check the current health status of an instance in your target pool or of all instances in the target pool, you can use the [`gcloud compute target-pools get-health` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-pools/get-health):
    
    
      gcloud compute target-pools get-health TARGET_POOL
    

Replace `TARGET_POOL` with the name of the target pool.

The command returns the health status as determined by the configured health check, either healthy or unhealthy.

###  API 

In the API, make an HTTP POST request to the following URI with the instance specified in the request body:
    
    
      https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/targetPools/TARGET_POOL/getHealth
    
      {
        "instance": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE"
      }
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID
  * `TARGET_POOL`: the name of the target pool to be updated
  * `REGION`: the region that the target pool is in
  * `ZONE`: the zone that the instance are in
  * `INSTANCE`: the instance whose health check status you are checking



## Delete a target pool

To delete a target pool, you must first make sure that the target pool is not being referenced by any forwarding rules. If a forwarding rule is referencing a target pool, you must delete the forwarding rule to remove the reference.

###  Console 

To use the Google Cloud console to delete a target pool, use the Load balancing advanced menu.

  1. On the **Advanced** load balancing page, go to the **Target pools** tab.   
[Go to Target pools](https://console.cloud.google.com/loadbalancing/advanced/targetPools/list)
  2. Click the name of the target pool.
  3. Click **Delete**.
  4. In the **Delete a target pool** window, click **Delete**.



###  gcloud 

To use `gcloud compute` to delete a target pool, use the [`target-pools delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-pools/delete):
    
    
      gcloud compute target-pools delete TARGET_POOL
    

Replace `TARGET_POOL` with the name of the target pool to be deleted.

###  API 

In the API, send an empty DELETE request to the following URI:
    
    
      https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/targetPools/TARGET_POOL
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID
  * `TARGET_POOL`: the name of the target pool to be updated
  * `REGION`: the region that the target pool is in



## Add or remove a health check from a target pool

Health check objects are standalone, global resources that can be associated or disassociated from any target pool.

If a target pool has no associated health check, the regional external passthrough Network Load Balancer will treat all instances as healthy and send traffic to all instances in the target pool. However, if you query for the health status of a target pool without a health check, the status will return as `unhealthy` to indicate that the target pool does not have a health check. We recommend that your target pools should have associated health checks to help you manage your instances.

Regional external passthrough Network Load Balancers use [legacy HTTP health checks](https://docs.cloud.google.com/load-balancing/docs/health-check-concepts) to determine the health of instances in the target pool. A regional external passthrough Network Load Balancer can only use a legacy HTTP health check, not a legacy HTTPS health check.

###  Console 

When using the Google Cloud console, you can create a legacy HTTP health check while [creating a regional external passthrough Network Load Balancer with a target pool backend](https://docs.cloud.google.com/load-balancing/docs/network/setting-up-network).

You _cannot_ use the Google Cloud console **Health checks** page to create a standalone legacy health check.

###  gcloud 

To use `gcloud compute` to add a health check to a target pool, use the [`target-pools add-health-checks` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-pools/add-health-checks):
    
    
      gcloud compute target-pools add-health-checks TARGET_POOL \
          --http-health-check=HEALTH_CHECK
    

Replace the following:

  * `TARGET_POOL`: the name of the target pool
  * `HEALTH_CHECK`: the legacy HTTP health check to be used with this target pool



To remove a health check, use the [`target-pools remove-health-checks` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-pools/remove-health-checks):
    
    
      gcloud compute target-pools remove-health-checks TARGET_POOL \
        --http-health-check=HEALTH_CHECK
    

Replace the following:

  * `TARGET_POOL`: the name of the target pool
  * `HEALTH_CHECK`: the legacy HTTP health check to be removed from this target pool



###  API 

To associate or disassociate a health check using the API, make a `HTTP POST` request to the appropriate URIs:
    
    
      https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/targetPools/TARGET_POOL/removeHealthCheck
      https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/targetPools/TARGET_POOL/addHealthCheck
    

The body of your request should contain the health check to associate or disassociate:
    
    
      {
        "healthCheck": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/httpHealthChecks/HEALTH_CHECK"
      }
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID
  * `TARGET_POOL`: the name of the target pool to be updated
  * `REGION`: the region that the target pool is in
  * `HEALTH_CHECK`: the legacy HTTP health check to be associated or disassociated with the target pool



For more information, see the API reference documentation for [`targetPools.addHealthCheck`](https://docs.cloud.google.com/compute/docs/reference/latest/targetPools/addHealthCheck) and [`targetPools.removeHealthCheck`](https://docs.cloud.google.com/compute/docs/reference/latest/targetPools/removeHealthCheck).

## Add or remove a backup target pool

When you first create a target pool, you can choose to apply a backup target pool that receives traffic if your target pool becomes unhealthy.

If you have never set up a backup target pool before, you should also set up [health checks](https://docs.cloud.google.com/load-balancing/docs/health-checks) for the feature to work correctly.

**Note:** If your target pool has the `sessionAffinity` field set, resizing the target pool could cause requests that come from the same IP to go to a different instance initially. Eventually, all connections from the IP will go to the same virtual machine, as the old connections close.

###  Console 

Target pools can't be edited in the Google Cloud console. You can edit a target proxy by using the Google Cloud CLI or the API.

###  gcloud 

To use `gcloud compute` to update the backup pool resource, use the [`target-pools set-backup` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/target-pools/set-backup):
    
    
      gcloud compute target-pools set-backup TARGET_POOL \
          --backup-pool=BACKUP_POOL \
          --failover-ratio=FAILOVER_RATIO
    

Replace the following:

  * `TARGET_POOL`: the name of the target pool
  * `BACKUP_POOL`: a name for the backup target pool
  * `FAILOVER_RATIO`: a value between 0.0 and 1.0, which determines when the target pool is declared unhealthy



###  API 

To make a request to update or remove a backup pool through the API, send a POST request to the following URI:
    
    
      POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/targetPools/TARGET_POOL/setBackup?failoverRatio=FAILOVER_RATIO
    
      {
        "target": "https://www.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/targetPools/BACKUP_POOL"
      }
    

Replace the following:

  * `PROJECT_ID`: the Google Cloud project ID
  * `TARGET_POOL`: the name of the target pool to be updated
  * `REGION`: the region that the target pool is in
  * `BACKUP_POOL`: the name of the backup pool to be associated with the target pool
  * `FAILOVER_RATIO`: the failover ratio



If you define an empty target or don't define a failover ratio, the backup pool behavior is disabled for this target pool.

## What's next

  * For more information about target pools, see the API reference documentation for [`targetPools.setBackup`](https://docs.cloud.google.com/compute/docs/reference/latest/targetPools/setBackup).
  * For more information about forwarding rules, see [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
