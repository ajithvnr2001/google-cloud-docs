---
url: https://docs.cloud.google.com/load-balancing/docs/enabling-connection-draining/
title: Connection draining \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:41.638404+00:00
---

# Connection draining  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/enabling-connection-draining/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Connection draining Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** This page describes how to configure a specific load balancer component or feature before or after you've already created a load balancer. Working with specific components is useful for advanced configurations and necessary for some configuration options. Before using the information on this page, know the [type of Google Cloud load balancer](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) that you need.

Connection draining is a process that ensures that existing, in-progress requests are given time to complete when a virtual machine (VM) instance is removed from an instance group or when an endpoint is removed from network endpoint groups (NEGs) that are zonal in scope.

The information on this page applies only to instance groups and the following types of NEGs that are zonal in scope:

  * [Zonal NEG](https://docs.cloud.google.com/load-balancing/docs/negs#zonal-neg)
  * [Hybrid connectivity NEG](https://docs.cloud.google.com/load-balancing/docs/negs#hybrid-neg)



Connection draining applies whenever you do the following:

  * You remove a [VM](https://docs.cloud.google.com/compute/docs/instance-groups/creating-groups-of-unmanaged-instances#removing_vms) or an [endpoint](https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-zonal-negs#deleting-endpoints) from a backend group (instance group or NEG).
  * You remove an instance from a managed instance group by performing a [`resize()`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/resize), [`deleteInstances()`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/deleteInstances), [`recreateInstances()`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/recreateInstances), or [`abandonInstances()`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instanceGroupManagers/abandonInstances) call.
  * You remove a Dynamic NIC from a VM that is part of an instance group backend.
  * Google Cloud deletes an instance as part of [autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler).
  * You perform an update to the managed instance group using the [Managed Instance Group Updater](https://docs.cloud.google.com/compute/docs/instance-groups/updating-managed-instance-groups).



Connection draining doesn't apply when a backend group (instance group or zonal NEG) is removed from a load balancer's backend service.

## How connection draining works

To enable connection draining, you set a _connection draining timeout_ on the backend service. The timeout duration must be from 0 to 3600 seconds, inclusive.

It can take up to 60 seconds after your specified timeout duration has passed for the instance to be terminated.

The following is a list of specifications about connection draining:

  * Connection draining is available for backend services that are part of the following load balancers:

    * [External Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/https)
    * [Internal Application Load Balancers](https://docs.cloud.google.com/load-balancing/docs/l7-internal)
    * [External proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/tcp)
    * [Internal proxy Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/tcp/internal-proxy)
    * [Global external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/global-networklb-architecture)
    * [Backend service-based Regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service)
    * [Internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal)

All Passthrough Network Load Balancers support connection draining for TCP, UDP, and other non-TCP protocols.

  * Connection draining is also available for backend services that are part of [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/concepts) deployments.

  * When a connection draining timeout is set, and an instance is removed from the instance group or an endpoint is removed from a zonal NEG, Google Cloud load balancers and Cloud Service Mesh behave in the following way:

    * No new connections are sent to the removed instance or endpoint.

    * **Application Load Balancers** : For the specified duration of the timeout, existing requests to the VM or endpoint marked for removal are given time to complete. The load balancer doesn't send new connections to this VM or endpoint. After the timeout duration is reached, the load balancer stops sending all traffic to the removed VM or endpoint.

    * **Proxy Network Load Balancers** : For the specified duration of the timeout, existing TCP connections to the VM or endpoint marked for removal continue to work during the configured connection draining period. The load balancer doesn't send new connections to this VM or endpoint. After the timeout duration is reached, existing TCP connections to the removed VM or endpoint remain active and the proxy closes all existing TCP connections within 10 minutes, the default idle timeout.

    * **Passthrough Network Load Balancers** : For the specified duration of the connection draining timeout, packets belonging to existing connections are routed to the VM or endpoint marked for removal. Once the timeout expires, the load balancer removes the connection tracking entry. After the connection tracking table entry has been removed, subsequent packets for the connection are routed to a different backend VM or endpoint by following the backend selection and connection tracking process. For TCP connections, the different backend has no record of an existing connection, so it might send a TCP reset (`RST`) packet to close the connection and allow the client to open a new connection to the load balancer. Note that passthrough Network Load Balancers by themselves cannot send `RST` or `FIN` packets to close a connection.

  * If you enable connection draining on multiple backend services that share the same instance groups or NEGs, the largest timeout value is used. For example, suppose that the same instance group or zonal NEG is a backend for two backend services, where one backend service has a connection draining timeout of 100 seconds, and the other backend service has a connection draining timeout of 200 seconds. Google Cloud uses 200 seconds as the effective connection draining timeout before terminating them. If the backend is a managed instance group, operations that delete the instance are delayed by at least 200 seconds.

  * If you don't set a connection draining timeout, or if the connection draining timeout is set to zero (0), Google Cloud ends existing connections on the removed instance or endpoint as quickly as possible.

  * If you're using connection pooling, you might see that new requests, using a previously established connection, are still being received on VMs that are getting drained, causing connection errors when those VMs are eventually deleted.




## Enable connection draining

To enable connection draining, complete the following steps.

###  Console 

### Update a load balancer

  1. Go to the Load balancing page in the Google Cloud console.   
[Go to Load balancing](https://console.cloud.google.com/networking/loadbalancing/list)
  2. On the **Load Balancers** tab, for the load balancer that you'd like to update, click more_vert, and then click **Edit** edit.
  3. Click **Backend configuration**.
  4. In the **Backend configuration** pane, click edit.
  5. At the bottom of the **Edit backend service** pane, click **Advanced configurations**.
  6. In the **Connection draining timeout** field, enter a value from `0` \- `3600`. A setting of `0` disables connection draining.



### Update Cloud Service Mesh

  1. Go to the Cloud Service Mesh page in the Google Cloud console.   
[Go to Cloud Service Mesh](https://console.cloud.google.com/net-services/trafficdirector/services/list)
  2. Click the **Name** of your service.
  3. On the **Service details** page, click **Edit** edit.
  4. At the bottom of your service, click **Advanced configurations**.
  5. In the **Connection draining timeout** field, enter a value from `0` \- `3600`. A setting of `0` disables connection draining.
  6. Click **Save**.



###  gcloud 

Enable connection draining on a new or existing backend service by using the `--connection-draining-timeout` flag. The following examples demonstrate how to change the connection draining timeout:

  * For an existing [global or cross-region load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer#choose-lb-table):
        
        gcloud compute backend-services update BACKEND_SERVICE \
            --global \
            --connection-draining-timeout=CONNECTION_TIMEOUT_SECS
        



  * For an existing [regional load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer#choose-lb-table):
        
        gcloud compute backend-services update BACKEND_SERVICE \
            --region=REGION \
            --connection-draining-timeout=CONNECTION_TIMEOUT_SECS
        




Replace the placeholders with valid values:

  * `BACKEND_SERVICE`: the backend service that you're updating
  * `REGION`: if applicable, the region of the backend service that you're updating
  * `CONNECTION_TIMEOUT_SECS`: the number of seconds to wait before existing connections to instances or endpoints are terminated, between `0` \- `3600` seconds, inclusive. A setting of `0` disables connection draining. The connection draining timeout applies to all backends of the backend service.

You can also use the `gcloud compute backend-services edit` command to update an existing backend service.




###  API 

To enable connection draining in the API when creating or updating an instance or endpoint, make a request to the respective API URI to include the `connectionDraining` field in your request body. The following examples demonstrate how to set that attribute by editing an existing backend service. For information about other required attributes, see the documentation for each load balancer.

  * For an existing [global or cross-region load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer#choose-lb-table):
        
        PATCH https://www.googleapis.com/compute/v1/projects/PROJECT_ID/global/backendServices
        

**Note:** Classic Application Load Balancers and classic proxy Network Load Balancers always use _global_ backend services, even when backends are in only one region because the load balancer is set to use the Standard Network Tier.


  * For an existing [regional load balancer](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer#choose-lb-table):
        
        PATCH https://www.googleapis.com/compute/v1/projects/PROJECT_ID/region/REGION/backendServices
        
        {
           "name": "BACKEND_SERVICE",
           "connectionDraining": {
             "drainingTimeoutSec": CONNECTION_TIMEOUT_SECS
           }
        }
        

Replace the following:

    * `PROJECT_ID`: the project ID that contains your load balancer or Cloud Service Mesh deployment
    * `BACKEND_SERVICE`: the backend service used by your load balancer or Cloud Service Mesh deployment
    * `CONNECTION_TIMEOUT_SECS`: the number of seconds to wait before instances or endpoints are removed from the instance group or NEG, between 0 to 3600 seconds, inclusive. This timeout duration applies to all instance groups or NEGs that are referenced by the backend service.



## What's next

  * For general information on backend services, see [Backend services overview](https://docs.cloud.google.com/load-balancing/docs/backend-service).

  * [Backend selection and connection tracking process for regional external passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/network/ext-netlb-traffic-distribution#connection-tracking)

  * [Backend selection and connection tracking process for internal passthrough Network Load Balancers](https://docs.cloud.google.com/load-balancing/docs/internal/int-netlb-traffic-distribution#connection-tracking)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
