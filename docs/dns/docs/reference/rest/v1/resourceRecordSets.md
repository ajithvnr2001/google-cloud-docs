---
url: https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets/
title: REST Resource: resourceRecordSets \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:20.589518+00:00
---

# REST Resource: resourceRecordSets  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Reference ](https://docs.cloud.google.com/dns/docs/apis)



Send feedback 

#  REST Resource: resourceRecordSets Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ResourceRecordSet
    * JSON representation
    * RRSetRoutingPolicy
      * JSON representation
    * GeoPolicy
      * JSON representation
    * GeoPolicyItem
      * JSON representation
    * HealthCheckTargets
      * JSON representation
    * LoadBalancerTarget
      * JSON representation
    * LoadBalancerType
    * IpProtocol
    * WrrPolicy
      * JSON representation
    * WrrPolicyItem
      * JSON representation
    * PrimaryBackupPolicy
      * JSON representation
  * Methods



## Resource: ResourceRecordSet

A unit of data that is returned by the DNS servers.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": string,
      "ttl": integer,
      "rrdatas": [
        string
      ],
      "signatureRrdatas": [
        string
      ],
      "routingPolicy": {
        object ([RRSetRoutingPolicy](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.RRSetRoutingPolicy))
      },
      "kind": string
    }  
  
Fields  
---  
`name` |  `string` For example, www.example.com.  
`type` |  `string` The identifier of a supported record type. See the list of [Supported DNS record types](https://docs.cloud.google.com/dns/docs/records-overview#supported_dns_record_types).  
`ttl` |  `integer` Number of seconds that this `ResourceRecordSet` can be cached by resolvers.  
`rrdatas[]` |  `string` As defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1) -- see [examples](https://docs.cloud.google.com/dns/records/json-record).  
`signatureRrdatas[]` |  `string` As defined in RFC 4034 (section 3.2).  
`routingPolicy` |  `object (`[RRSetRoutingPolicy](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.RRSetRoutingPolicy)`)` Configures dynamic query responses based on either the geo location of the querying user or a weighted round robin based routing policy. A valid `ResourceRecordSet` contains only `rrdata` (for static resolution) or a `routingPolicy` (for dynamic resolution).  
`kind` |  `string`  
  
### RRSetRoutingPolicy

A RRSetRoutingPolicy represents ResourceRecordSet data that is returned dynamically with the response varying based on configured properties such as geolocation or by weighted random selection.

JSON representation  
---  
      
    
    {
      "healthCheck": string,
      "kind": string,
    
      // Union field routing_data can be only one of the following:
      "geo": {
        object ([GeoPolicy](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.GeoPolicy))
      },
      "wrr": {
        object ([WrrPolicy](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.WrrPolicy))
      },
      "primaryBackup": {
        object ([PrimaryBackupPolicy](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.PrimaryBackupPolicy))
      }
      // End of list of possible types for union field routing_data.
    }  
  
Fields  
---  
`healthCheck` |  `string` The fully qualified URL of the HealthCheck to use for this RRSetRoutingPolicy. Format this URL like `https://www.googleapis.com/compute/v1/projects/{project}/global/healthChecks/{healthCheck}`.<https://cloud.google.com/compute/docs/reference/rest/v1/healthChecks>  
`kind` |  `string`  
Union field `routing_data`.`routing_data` can be only one of the following:  
`geo` |  `object (`[GeoPolicy](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.GeoPolicy)`)`  
`wrr` |  `object (`[WrrPolicy](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.WrrPolicy)`)`  
`primaryBackup` |  `object (`[PrimaryBackupPolicy](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.PrimaryBackupPolicy)`)`  
  
### GeoPolicy

Configures a `RRSetRoutingPolicy` that routes based on the geo location of the querying user.

JSON representation  
---  
      
    
    {
      "items": [
        {
          object ([GeoPolicyItem](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.GeoPolicyItem))
        }
      ],
      "enableFencing": boolean,
      "kind": string
    }  
  
Fields  
---  
`items[]` |  `object (`[GeoPolicyItem](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.GeoPolicyItem)`)` The primary geo routing configuration. If there are multiple items with the same location, an error is returned instead.  
`enableFencing` |  `boolean` Without fencing, if health check fails for all configured items in the current geo bucket, we failover to the next nearest geo bucket. With fencing, if health checking is enabled, as long as some targets in the current geo bucket are healthy, we return only the healthy targets. However, if all targets are unhealthy, we don't failover to the next nearest bucket; instead, we return all the items in the current bucket even when all targets are unhealthy.  
`kind` |  `string`  
  
### GeoPolicyItem

ResourceRecordSet data for one geo location.

JSON representation  
---  
      
    
    {
      "location": string,
      "rrdatas": [
        string
      ],
      "signatureRrdatas": [
        string
      ],
      "healthCheckedTargets": {
        object ([HealthCheckTargets](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.HealthCheckTargets))
      },
      "kind": string
    }  
  
Fields  
---  
`location` |  `string` The geo-location granularity is a GCP region. This location string should correspond to a GCP region. e.g. "us-east1", "southamerica-east1", "asia-east1", etc.  
`rrdatas[]` |  `string`  
`signatureRrdatas[]` |  `string` DNSSEC generated signatures for all the `rrdata` within this item. When using health-checked targets for DNSSEC-enabled zones, you can only use at most one health-checked IP address per item.  
`healthCheckedTargets` |  `object (`[HealthCheckTargets](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.HealthCheckTargets)`)` For A and AAAA types only. Endpoints to return in the query result only if they are healthy. These can be specified along with `rrdata` within this item.  
`kind` |  `string`  
  
### HealthCheckTargets

HealthCheckTargets describes endpoints to health-check when responding to Routing Policy queries. Only the healthy endpoints will be included in the response.

Set either `internalLoadBalancer` or `externalEndpoints`. Do not set both.

JSON representation  
---  
      
    
    {
      "internalLoadBalancers": [
        {
          object ([LoadBalancerTarget](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.LoadBalancerTarget))
        }
      ],
      "externalEndpoints": [
        string
      ]
    }  
  
Fields  
---  
`internalLoadBalancers[]` |  `object (`[LoadBalancerTarget](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.LoadBalancerTarget)`)` Configuration for internal load balancers to be health checked.  
`externalEndpoints[]` |  `string` The Internet IP addresses to be health checked. The format matches the format of ResourceRecordSet.rrdata as defined in RFC 1035 (section 5) and RFC 1034 (section 3.6.1)  
  
### LoadBalancerTarget

The configuration for an individual load balancer to health check.

JSON representation  
---  
      
    
    {
      "loadBalancerType": enum ([LoadBalancerType](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.LoadBalancerType)),
      "ipAddress": string,
      "port": string,
      "ipProtocol": enum ([IpProtocol](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.IpProtocol)),
      "networkUrl": string,
      "project": string,
      "region": string,
      "kind": string
    }  
  
Fields  
---  
`loadBalancerType` |  `enum (`[LoadBalancerType](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.LoadBalancerType)`)` The type of load balancer specified by this target. This value must match the configuration of the load balancer located at the LoadBalancerTarget's IP address, port, and region. Use the following:   


  * **regionalL4ilb** : for a regional internal passthrough Network Load Balancer. 
  * **regionalL7ilb** : for a regional internal Application Load Balancer. 
  * **globalL7ilb** : for a global internal Application Load Balancer. 

  
`ipAddress` |  `string` The frontend IP address of the load balancer to health check.  
`port` |  `string` The configured port of the load balancer.  
`ipProtocol` |  `enum (`[IpProtocol](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.IpProtocol)`)` The protocol of the load balancer to health check.  
`networkUrl` |  `string` The fully qualified URL of the network that the load balancer is attached to. This should be formatted like `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`.  
`project` |  `string` The project ID in which the load balancer is located.  
`region` |  `string` The region in which the load balancer is located.  
`kind` |  `string`  
  
### LoadBalancerType

LoadBalancerType indicates the type of load balancer to be health checked.

Enums  
---  
`none` |   
`globalL7ilb` | Indicates the load balancer is a Cross-Region Application Load Balancer.  
`regionalL4ilb` | Indicates the load balancer is a Regional Network Passthrough Load Balancer.  
`regionalL7ilb` | Indicates the load balancer is a Regional Application Load Balancer.  
  
### IpProtocol

The protocol of the load balancer to health check.

Enums  
---  
`undefined` |   
`tcp` | Indicates the load balancer is accessible via TCP.  
`udp` | Indicates the load balancer is accessible via UDP.  
  
### WrrPolicy

Configures a RRSetRoutingPolicy that routes in a weighted round robin fashion.

JSON representation  
---  
      
    
    {
      "items": [
        {
          object ([WrrPolicyItem](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.WrrPolicyItem))
        }
      ],
      "kind": string
    }  
  
Fields  
---  
`items[]` |  `object (`[WrrPolicyItem](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.WrrPolicyItem)`)`  
`kind` |  `string`  
  
### WrrPolicyItem

A routing block which contains the routing information for one WRR item.

JSON representation  
---  
      
    
    {
      "weight": number,
      "rrdatas": [
        string
      ],
      "signatureRrdatas": [
        string
      ],
      "healthCheckedTargets": {
        object ([HealthCheckTargets](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.HealthCheckTargets))
      },
      "kind": string
    }  
  
Fields  
---  
`weight` |  `number` The weight corresponding to this `WrrPolicyItem` object. When multiple `WrrPolicyItem` objects are configured, the probability of returning an `WrrPolicyItem` object's data is proportional to its weight relative to the sum of weights configured for all items. This weight must be non-negative.  
`rrdatas[]` |  `string`  
`signatureRrdatas[]` |  `string` DNSSEC generated signatures for all the `rrdata` within this item. When using health-checked targets for DNSSEC-enabled zones, you can only use at most one health-checked IP address per item.  
`healthCheckedTargets` |  `object (`[HealthCheckTargets](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.HealthCheckTargets)`)` Endpoints that are health checked before making the routing decision. The unhealthy endpoints are omitted from the result. If all endpoints within a bucket are unhealthy, we choose a different bucket (sampled with respect to its weight) for responding. If DNSSEC is enabled for this zone, only one of `rrdata` or `healthCheckedTargets` can be set.  
`kind` |  `string`  
  
### PrimaryBackupPolicy

Configures a RRSetRoutingPolicy such that all queries are responded with the primaryTargets if they are healthy. And if all of them are unhealthy, then we fallback to a geo localized policy.

JSON representation  
---  
      
    
    {
      "primaryTargets": {
        object ([HealthCheckTargets](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.HealthCheckTargets))
      },
      "backupGeoTargets": {
        object ([GeoPolicy](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.GeoPolicy))
      },
      "trickleTraffic": number,
      "kind": string
    }  
  
Fields  
---  
`primaryTargets` |  `object (`[HealthCheckTargets](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.HealthCheckTargets)`)` Endpoints that are health checked before making the routing decision. Unhealthy endpoints are omitted from the results. If all endpoints are unhealthy, we serve a response based on the `backupGeoTargets`.  
`backupGeoTargets` |  `object (`[GeoPolicy](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets#ResourceRecordSet.GeoPolicy)`)` Backup targets provide a regional failover policy for the otherwise global primary targets. If serving state is set to `BACKUP`, this policy essentially becomes a geo routing policy.  
`trickleTraffic` |  `number` When serving state is `PRIMARY`, this field provides the option of sending a small percentage of the traffic to the backup targets.  
`kind` |  `string`  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets/create)`

|  Creates a new ResourceRecordSet.  
  
### `[delete](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets/delete)`

|  Deletes a previously created ResourceRecordSet.  
  
### `[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets/get)`

|  Fetches the representation of an existing ResourceRecordSet.  
  
### `[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets/list)`

|  Enumerates ResourceRecordSets that you have created but not yet deleted.  
  
### `[patch](https://docs.cloud.google.com/dns/docs/reference/rest/v1/resourceRecordSets/patch)`

|  Applies a partial update to an existing ResourceRecordSet.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-25 UTC."],[],[]] 
