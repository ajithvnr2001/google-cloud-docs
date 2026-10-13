---
url: https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/
title: REST Resource: managedZones \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:18.536724+00:00
---

# REST Resource: managedZones  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Reference ](https://docs.cloud.google.com/dns/docs/apis)



Send feedback 

#  REST Resource: managedZones Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ManagedZone
    * JSON representation
    * DnsSecConfig
      * JSON representation
    * State
    * NonExistenceType
    * Visibility
    * PrivateVisibilityConfig
      * JSON representation
    * Network
      * JSON representation
    * GKECluster
      * JSON representation
    * ForwardingConfig
      * JSON representation
    * NameServerTarget
      * JSON representation
    * ForwardingPath
    * PeeringConfig
      * JSON representation
    * TargetNetwork
      * JSON representation
    * ReverseLookupConfig
      * JSON representation
    * ServiceDirectoryConfig
      * JSON representation
    * Namespace
      * JSON representation
    * CloudLoggingConfig
      * JSON representation
  * Methods



## Resource: ManagedZone

A zone is a subtree of the DNS namespace under one administrative responsibility. A ManagedZone is a resource that represents a DNS zone hosted by the Cloud DNS service.

JSON representation  
---  
      
    
    {
      "name": string,
      "dnsName": string,
      "description": string,
      "id": string,
      "nameServers": [
        string
      ],
      "creationTime": string,
      "dnssecConfig": {
        object ([DnsSecConfig](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.DnsSecConfig))
      },
      "nameServerSet": string,
      "visibility": enum ([Visibility](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.Visibility)),
      "privateVisibilityConfig": {
        object ([PrivateVisibilityConfig](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.PrivateVisibilityConfig))
      },
      "forwardingConfig": {
        object ([ForwardingConfig](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.ForwardingConfig))
      },
      "labels": {
        string: string,
        ...
      },
      "peeringConfig": {
        object ([PeeringConfig](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.PeeringConfig))
      },
      "reverseLookupConfig": {
        object ([ReverseLookupConfig](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.ReverseLookupConfig))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.ServiceDirectoryConfig))
      },
      "cloudLoggingConfig": {
        object ([CloudLoggingConfig](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.CloudLoggingConfig))
      },
      "kind": string
    }  
  
Fields  
---  
`name` |  `string` User assigned name for this resource. Must be unique within the project. The name must be 1-63 characters long, must begin with a letter, end with a letter or digit, and only contain lowercase letters, digits or dashes.  
`dnsName` |  `string` The DNS name of this managed zone, for instance "example.com.".  
`description` |  `string` A mutable string of at most 1024 characters associated with this resource for the user's convenience. Has no effect on the managed zone's function.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Unique identifier for the resource; defined by the server (output only)  
`nameServers[]` |  `string` Delegate your managedZone to these virtual name servers; defined by the server (output only)  
`creationTime` |  `string` The time that this resource was created on the server. This is in RFC3339 text format. Output only.  
`dnssecConfig` |  `object (`[DnsSecConfig](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.DnsSecConfig)`)` DNSSEC configuration.  
`nameServerSet` |  `string` Optionally specifies the NameServerSet for this ManagedZone. A NameServerSet is a set of DNS name servers that all host the same ManagedZones. Most users leave this field unset. If you need to use this field, contact your account team.  
`visibility` |  `enum (`[Visibility](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.Visibility)`)` The zone's visibility: public zones are exposed to the Internet, while private zones are visible only to Virtual Private Cloud resources.  
`privateVisibilityConfig` |  `object (`[PrivateVisibilityConfig](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.PrivateVisibilityConfig)`)` For privately visible zones, the set of Virtual Private Cloud resources that the zone is visible from.  
`forwardingConfig` |  `object (`[ForwardingConfig](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.ForwardingConfig)`)` The presence for this field indicates that outbound forwarding is enabled for this zone. The value of this field contains the set of destinations to forward to.  
`labels` |  `map (key: string, value: string)` User labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`peeringConfig` |  `object (`[PeeringConfig](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.PeeringConfig)`)` The presence of this field indicates that DNS Peering is enabled for this zone. The value of this field contains the network to peer with.  
`reverseLookupConfig` |  `object (`[ReverseLookupConfig](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.ReverseLookupConfig)`)` The presence of this field indicates that this is a managed reverse lookup zone and Cloud DNS resolves reverse lookup queries using automatically configured records for VPC resources. This only applies to networks listed under privateVisibilityConfig.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.ServiceDirectoryConfig)`)` This field links to the associated service directory namespace. Do not set this field for public zones or forwarding zones.  
`cloudLoggingConfig` |  `object (`[CloudLoggingConfig](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.CloudLoggingConfig)`)`  
`kind` |  `string`  
  
### DnsSecConfig

JSON representation  
---  
      
    
    {
      "state": enum ([State](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.State)),
      "defaultKeySpecs": [
        {
          object ([DnsKeySpec](https://docs.cloud.google.com/dns/docs/reference/rest/v1/DnsKeySpec))
        }
      ],
      "nonExistence": enum ([NonExistenceType](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.NonExistenceType)),
      "kind": string
    }  
  
Fields  
---  
`state` |  `enum (`[State](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.State)`)` Specifies whether DNSSEC is enabled, and what mode it is in.  
`defaultKeySpecs[]` |  `object (`[DnsKeySpec](https://docs.cloud.google.com/dns/docs/reference/rest/v1/DnsKeySpec)`)` Specifies parameters for generating initial DnsKeys for this ManagedZone. Can only be changed while the state is OFF.  
`nonExistence` |  `enum (`[NonExistenceType](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.NonExistenceType)`)` Specifies the mechanism for authenticated denial-of-existence responses. Can only be changed while the state is OFF.  
`kind` |  `string`  
  
### State

Enums  
---  
`off` | DNSSEC is disabled; the zone is not signed.  
`on` | DNSSEC is enabled; the zone is signed and fully managed.  
`transfer` | DNSSEC is enabled, but in a "transfer" mode.  
  
### NonExistenceType

Enums  
---  
`nsec` | Indicates that Cloud DNS will sign records in the managed zone according to RFC 4034 and respond with NSEC records for names that do not exist.  
`nsec3` | Indicates that Cloud DNS will sign records in the managed zone according to RFC 5155 and respond with NSEC3 records for names that do not exist.  
  
### Visibility

Enums  
---  
`public` | Indicates that records in this zone can be queried from the public internet.  
`private` | Indicates that records in this zone cannot be queried from the public internet. Access to private zones depends on the zone configuration.  
  
### PrivateVisibilityConfig

JSON representation  
---  
      
    
    {
      "networks": [
        {
          object ([Network](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.Network))
        }
      ],
      "gkeClusters": [
        {
          object ([GKECluster](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.GKECluster))
        }
      ],
      "kind": string
    }  
  
Fields  
---  
`networks[]` |  `object (`[Network](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.Network)`)` The list of VPC networks that can see this zone.  
`gkeClusters[]` |  `object (`[GKECluster](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.GKECluster)`)` The list of Google Kubernetes Engine clusters that can see this zone.  
`kind` |  `string`  
  
### Network

JSON representation  
---  
      
    
    {
      "networkUrl": string,
      "kind": string
    }  
  
Fields  
---  
`networkUrl` |  `string` The fully qualified URL of the VPC network to bind to. Format this URL like `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`  
`kind` |  `string`  
  
### GKECluster

JSON representation  
---  
      
    
    {
      "gkeClusterName": string,
      "kind": string
    }  
  
Fields  
---  
`gkeClusterName` |  `string` The resource name of the cluster to bind this ManagedZone to. This should be specified in the format like: projects/*/locations/*/clusters/*. This is referenced from GKE projects.locations.clusters.get API: <https://cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters/get>  
`kind` |  `string`  
  
### ForwardingConfig

JSON representation  
---  
      
    
    {
      "targetNameServers": [
        {
          object ([NameServerTarget](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.NameServerTarget))
        }
      ],
      "kind": string
    }  
  
Fields  
---  
`targetNameServers[]` |  `object (`[NameServerTarget](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.NameServerTarget)`)` managedZones.list of target name servers to forward to. Cloud DNS selects the best available name server if more than one target is given.  
`kind` |  `string`  
  
### NameServerTarget

JSON representation  
---  
      
    
    {
      "ipv4Address": string,
      "forwardingPath": enum ([ForwardingPath](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.ForwardingPath)),
      "ipv6Address": string,
      "domainName": string,
      "kind": string
    }  
  
Fields  
---  
`ipv4Address` |  `string` IPv4 address of a target name server.  
`forwardingPath` |  `enum (`[ForwardingPath](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.ForwardingPath)`)` Forwarding path for this NameServerTarget. If unset or set to DEFAULT, Cloud DNS makes forwarding decisions based on IP address ranges; that is, RFC1918 addresses go to the VPC network, non-RFC1918 addresses go to the internet. When set to PRIVATE, Cloud DNS always sends queries through the VPC network for this target.  
`ipv6Address` |  `string` IPv6 address of a target name server. Does not accept both fields (ipv4 & ipv6) being populated. Public preview as of November 2022.  
`domainName` |  `string` Fully qualified domain name for the forwarding target.  
`kind` |  `string`  
  
### ForwardingPath

Enums  
---  
`default` | Cloud DNS makes forwarding decisions based on address ranges; that is, RFC1918 addresses forward to the target through the VPC and non-RFC1918 addresses forward to the target through the internet  
`private` | Cloud DNS always forwards to this target through the VPC.  
  
### PeeringConfig

JSON representation  
---  
      
    
    {
      "targetNetwork": {
        object ([TargetNetwork](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.TargetNetwork))
      },
      "kind": string
    }  
  
Fields  
---  
`targetNetwork` |  `object (`[TargetNetwork](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.TargetNetwork)`)` The network with which to peer.  
`kind` |  `string`  
  
### TargetNetwork

JSON representation  
---  
      
    
    {
      "networkUrl": string,
      "deactivateTime": string,
      "kind": string
    }  
  
Fields  
---  
`networkUrl` |  `string` The fully qualified URL of the VPC network to forward queries to. This should be formatted like `https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network}`  
`deactivateTime` |  `string` The time at which the zone was deactivated, in RFC 3339 date-time format. An empty string indicates that the peering connection is active. The producer network can deactivate a zone. The zone is automatically deactivated if the producer network that the zone targeted is deleted. Output only.  
`kind` |  `string`  
  
### ReverseLookupConfig

JSON representation  
---  
      
    
    {
      "kind": string
    }  
  
Fields  
---  
`kind` |  `string`  
  
### ServiceDirectoryConfig

Contains information about Service Directory-backed zones.

JSON representation  
---  
      
    
    {
      "namespace": {
        object ([Namespace](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.Namespace))
      },
      "kind": string
    }  
  
Fields  
---  
`namespace` |  `object (`[Namespace](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones#ManagedZone.Namespace)`)` Contains information about the namespace associated with the zone.  
`kind` |  `string`  
  
### Namespace

JSON representation  
---  
      
    
    {
      "namespaceUrl": string,
      "deletionTime": string,
      "kind": string
    }  
  
Fields  
---  
`namespaceUrl` |  `string` The fully qualified URL of the namespace associated with the zone. Format must be `https://servicedirectory.googleapis.com/v1/projects/{project}/locations/{location}/namespaces/{namespace}`  
`deletionTime` |  `string` The time that the namespace backing this zone was deleted; an empty string if it still exists. This is in RFC3339 text format. Output only.  
`kind` |  `string`  
  
### CloudLoggingConfig

Cloud Logging configurations for publicly visible zones.

JSON representation  
---  
      
    
    {
      "enableLogging": boolean,
      "kind": string
    }  
  
Fields  
---  
`enableLogging` |  `boolean` If set, enable query logging for this ManagedZone. False by default, making logging opt-in.  
`kind` |  `string`  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/create)`

|  Creates a new ManagedZone.  
  
### `[delete](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/delete)`

|  Deletes a previously created ManagedZone.  
  
### `[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/get)`

|  Fetches the representation of an existing ManagedZone.  
  
### `[getIamPolicy](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/list)`

|  Enumerates ManagedZones that have been created but not yet deleted.  
  
### `[patch](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/patch)`

|  Applies a partial update to an existing ManagedZone.  
  
### `[setIamPolicy](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
### `[update](https://docs.cloud.google.com/dns/docs/reference/rest/v1/managedZones/update)`

|  Updates an existing ManagedZone.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-25 UTC."],[],[]] 
