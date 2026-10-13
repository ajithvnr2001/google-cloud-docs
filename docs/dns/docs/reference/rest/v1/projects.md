---
url: https://docs.cloud.google.com/dns/docs/reference/rest/v1/projects/
title: REST Resource: projects \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:20.468635+00:00
---

# REST Resource: projects  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/reference/rest/v1/projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Reference ](https://docs.cloud.google.com/dns/docs/apis)



Send feedback 

#  REST Resource: projects Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ProjectsGetResponse
    * JSON representation
  * Project
    * JSON representation
  * Quota
    * JSON representation
  * Methods



## Resource: ProjectsGetResponse

JSON representation  
---  
      
    
    {
      "project": {
        object ([Project](https://docs.cloud.google.com/dns/docs/reference/rest/v1/projects#Project))
      }
    }  
  
Fields  
---  
`project` |  `object (`[Project](https://docs.cloud.google.com/dns/docs/reference/rest/v1/projects#Project)`)`  
  
## Project

A project resource. The project is a top level container for resources including Cloud DNS ManagedZones. Projects can be created only in the APIs console.

JSON representation  
---  
      
    
    {
      "number": string,
      "id": string,
      "quota": {
        object ([Quota](https://docs.cloud.google.com/dns/docs/reference/rest/v1/projects#Quota))
      },
      "kind": string
    }  
  
Fields  
---  
`number` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Unique numeric identifier for the resource; defined by the server (output only).  
`id` |  `string` User assigned unique identifier for the resource (output only).  
`quota` |  `object (`[Quota](https://docs.cloud.google.com/dns/docs/reference/rest/v1/projects#Quota)`)` Quotas assigned to this project (output only).  
`kind` |  `string`  
  
## Quota

Limits associated with a Project.

JSON representation  
---  
      
    
    {
      "managedZones": integer,
      "rrsetsPerManagedZone": integer,
      "rrsetAdditionsPerChange": integer,
      "rrsetDeletionsPerChange": integer,
      "totalRrdataSizePerChange": integer,
      "resourceRecordsPerRrset": integer,
      "dnsKeysPerManagedZone": integer,
      "whitelistedKeySpecs": [
        {
          object ([DnsKeySpec](https://docs.cloud.google.com/dns/docs/reference/rest/v1/DnsKeySpec))
        }
      ],
      "networksPerManagedZone": integer,
      "managedZonesPerNetwork": integer,
      "policies": integer,
      "networksPerPolicy": integer,
      "targetNameServersPerPolicy": integer,
      "targetNameServersPerManagedZone": integer,
      "peeringZonesPerTargetNetwork": integer,
      "responsePolicies": integer,
      "networksPerResponsePolicy": integer,
      "nameserversPerDelegation": integer,
      "gkeClustersPerManagedZone": integer,
      "managedZonesPerGkeCluster": integer,
      "gkeClustersPerPolicy": integer,
      "responsePolicyRulesPerResponsePolicy": integer,
      "gkeClustersPerResponsePolicy": integer,
      "itemsPerRoutingPolicy": integer,
      "internetHealthChecksPerManagedZone": integer,
      "kind": string
    }  
  
Fields  
---  
`managedZones` |  `integer` Maximum allowed number of managed zones in the project.  
`rrsetsPerManagedZone` |  `integer` Maximum allowed number of ResourceRecordSets per zone in the project.  
`rrsetAdditionsPerChange` |  `integer` Maximum allowed number of ResourceRecordSets to add per ChangesCreateRequest.  
`rrsetDeletionsPerChange` |  `integer` Maximum allowed number of ResourceRecordSets to delete per ChangesCreateRequest.  
`totalRrdataSizePerChange` |  `integer` Maximum allowed size for total rrdata in one ChangesCreateRequest in bytes.  
`resourceRecordsPerRrset` |  `integer` Maximum allowed number of ResourceRecords per ResourceRecordSet.  
`dnsKeysPerManagedZone` |  `integer` Maximum allowed number of DnsKeys per ManagedZone.  
`whitelistedKeySpecs[]` |  `object (`[DnsKeySpec](https://docs.cloud.google.com/dns/docs/reference/rest/v1/DnsKeySpec)`)` DNSSEC algorithm and key length types that can be used for DnsKeys.  
`networksPerManagedZone` |  `integer` Maximum allowed number of networks to which a privately scoped zone can be attached.  
`managedZonesPerNetwork` |  `integer` Maximum allowed number of managed zones which can be attached to a network.  
`policies` |  `integer` Maximum allowed number of policies per project.  
`networksPerPolicy` |  `integer` Maximum allowed number of networks per policy.  
`targetNameServersPerPolicy` |  `integer` Maximum allowed number of alternative target name servers per policy.  
`targetNameServersPerManagedZone` |  `integer` Maximum allowed number of target name servers per managed forwarding zone.  
`peeringZonesPerTargetNetwork` |  `integer` Maximum allowed number of consumer peering zones per target network owned by this producer project  
`responsePolicies` |  `integer` Maximum allowed number of response policies per project.  
`networksPerResponsePolicy` |  `integer` Maximum allowed number of networks per response policy.  
`nameserversPerDelegation` |  `integer` Maximum number of nameservers per delegation, meant to prevent abuse  
`gkeClustersPerManagedZone` |  `integer` Maximum allowed number of GKE clusters to which a privately scoped zone can be attached.  
`managedZonesPerGkeCluster` |  `integer` Maximum allowed number of managed zones which can be attached to a GKE cluster.  
`gkeClustersPerPolicy` |  `integer` Maximum allowed number of GKE clusters per policy.  
`responsePolicyRulesPerResponsePolicy` |  `integer` Maximum allowed number of rules per response policy.  
`gkeClustersPerResponsePolicy` |  `integer` Maximum allowed number of GKE clusters per response policy.  
`itemsPerRoutingPolicy` |  `integer` Maximum allowed number of items per routing policy.  
`internetHealthChecksPerManagedZone` |  `integer`  
`kind` |  `string`  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1/projects/get)`

|  Fetches the representation of an existing Project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-25 UTC."],[],[]] 
