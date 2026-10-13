---
url: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.iocAssociations
title: REST Resource: projects.locations.instances.iocAssociations \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:15:10.280265+00:00
---

# REST Resource: projects.locations.instances.iocAssociations  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.iocAssociations

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback 

#  REST Resource: projects.locations.instances.iocAssociations Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: IocAssociation
    * JSON representation
    * AssociationLocation
      * JSON representation
    * AssociationType
    * IocAssociationAlias
      * JSON representation
  * Methods



## Resource: IocAssociation

Associations represents different metadata about malware and threat actors involved with an IoC.

JSON representation  
---  
      
    
    {
      "name": string,
      "id": string,
      "countryCode": [
        string
      ],
      "regionCode": {
        object ([AssociationLocation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.iocAssociations#IocAssociation.AssociationLocation))
      },
      "type": enum ([AssociationType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.iocAssociations#IocAssociation.AssociationType)),
      "threatDisplayName": string,
      "description": string,
      "alias": [
        {
          object ([IocAssociationAlias](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.iocAssociations#IocAssociation.IocAssociationAlias))
        }
      ],
      "firstReferenceTime": string,
      "lastReferenceTime": string,
      "industriesAffected": [
        string
      ],
      "associatedActors": [
        {
          object ([IocAssociation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.iocAssociations#IocAssociation))
        }
      ],
      "roles": [
        string
      ],
      "operatingSystems": [
        string
      ],
      "iocs": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. Identifier. The resource name of this IocAssociation. Format: projects/{project}/locations/{location}/instances/{instance}/ iocAssociations/{iocAssociation}  
`id` |  `string` Output only. Association identifier. This can be used to request details of the IocAssociation from the Google Threat Intelligence API (<https://gtidocs.virustotal.com/reference/get-threat>)  
`countryCode[]  
**(deprecated)**` |  `string` This item is deprecated!Output only. Deprecated. Use regionCode instead. Country from which the threat actor originated.  
`regionCode` |  `object (`[AssociationLocation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.iocAssociations#IocAssociation.AssociationLocation)`)` Output only. Name of the country the threat is originating from.  
`type` |  `enum (`[AssociationType](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.iocAssociations#IocAssociation.AssociationType)`)` Output only. Signifies the type of association.  
`threatDisplayName` |  `string` Output only. Name of the threat actor/malware.  
`description` |  `string` Output only. Human readable description about the association.  
`alias[]` |  `object (`[IocAssociationAlias](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.iocAssociations#IocAssociation.IocAssociationAlias)`)` Output only. Different aliases of the threat actor given by different sources.  
`firstReferenceTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. First time the threat actor was referenced or seen.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`lastReferenceTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last time the threat actor was referenced or seen.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`industriesAffected[]` |  `string` Output only. List of industries the threat actor affects.  
`associatedActors[]  
**(deprecated)**` |  `object (`[IocAssociation](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.iocAssociations#IocAssociation)`)` This item is deprecated!Output only. List of associated threat actors for a malware. Not applicable for threat actors.  
`roles[]` |  `string` Output only. List of roles associated with the malware. Not applicable for threat actors.  
`operatingSystems[]` |  `string` Output only. List of operating systems that associated with the malware. Not applicable for threat actors.  
`iocs[]` |  `string` Output only. The resource names of the Iocs that are related to this IocAssociation. Format: projects/{project}/locations/{location}/instances/{instance}/iocs/{ioc}  
  
### AssociationLocation

Information about a location.

JSON representation  
---  
      
    
    {
      "city": string,
      "state": string,
      "countryOrRegion": string,
      "location": string,
      "desk": string,
      "floor": string,
      "regionCoordinates": {
        object ([LatLng](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Location#LatLng))
      }
    }  
  
Fields  
---  
`city` |  `string` Output only. The city.  
`state` |  `string` The state.  
`countryOrRegion` |  `string` The country or region.  
`location` |  `string` Custom location name (e.g. building or site name like "London Office"). For cloud environments, this is the region (e.g. "us-west2").  
`desk` |  `string` Desk name or individual location, typically for an employee in an office. (e.g. "IN-BLR-BCPC-11-1121D").  
`floor` |  `string` Floor name, number or a combination of the two for a building. (e.g. "1-A").  
`regionCoordinates` |  `object (`[LatLng](https://docs.cloud.google.com/chronicle/docs/reference/rest/Shared.Types/Location#LatLng)`)` Coordinates for the associated region.  
  
### AssociationType

Represents different possible Association types. Can be threat or malware. Used to represent Mandiant threat intelligence.

Enums  
---  
`ASSOCIATION_TYPE_UNSPECIFIED` | The default Association Type.  
`THREAT_ACTOR` | Association type Threat actor.  
`MALWARE` | Association type Malware.  
`SOFTWARE_TOOLKIT` | Association type Software toolkit.  
  
### IocAssociationAlias

Association Alias Used to represent Mandiant Threat intel.

JSON representation  
---  
      
    
    {
      "associationName": string,
      "provider": string
    }  
  
Fields  
---  
`associationName` |  `string` Output only. Name of the alias.  
`provider` |  `string` Output only. Name of the provider who gave the association's name.  
  
## Methods  
  
---  
  
### `[batchGet](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.iocAssociations/batchGet)`

|  Gets a batch (list) of IocAssociations given a list of names and a parent.  
  
### `[fetchRelated](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.iocAssociations/fetchRelated)`

|  List related Associations (Threat Actors or Malware Families) for a given threat resource.  
  
### `[get](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1beta/projects.locations.instances.iocAssociations/get)`

|  Get an Ioc Association by resource name.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-07 UTC."],[],[]] 
