---
url: https://docs.cloud.google.com/compute/docs/reference/rest/beta/publicDelegatedPrefixes/get/
title: Method: publicDelegatedPrefixes.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:19:42.216074+00:00
---

# Method: publicDelegatedPrefixes.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/beta/publicDelegatedPrefixes/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: publicDelegatedPrefixes.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Returns the specified PublicDelegatedPrefix resource in the given region.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/beta/projects/{project}/regions/{region}/publicDelegatedPrefixes/{publicDelegatedPrefix}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` Name of the region of this request.  
`publicDelegatedPrefix` |  `string` Name of the PublicDelegatedPrefix resource to return.  
  
### Request body

The request body must be empty.

### Response body

A PublicDelegatedPrefix resource represents an IP block within a PublicAdvertisedPrefix that is configured within a single cloud scope (global or region). IPs in the block can be allocated to resources within that scope. Public delegated prefixes may be further broken up into smaller IP blocks in the same scope as the parent block.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "selfLink": string,
      "region": string,
      "ipCidrRange": string,
      "status": enum,
      "parentPrefix": string,
      "publicDelegatedSubPrefixs": [
        {
          "name": string,
          "description": string,
          "region": string,
          "status": enum,
          "ipCidrRange": string,
          "delegateeProject": string,
          "isAddress": boolean,
          "mode": enum,
          "allocatablePrefixLength": integer,
          "ipv6AccessType": enum,
          "purpose": enum,
          "enableEnhancedIpv4Allocation": boolean
        }
      ],
      "isLiveMigration": boolean,
      "fingerprint": string,
      "mode": enum,
      "allocatablePrefixLength": integer,
      "byoipApiVersion": enum,
      "networkTier": enum,
      "ipv6AccessType": enum,
      "purpose": enum,
      "enableEnhancedIpv4Allocation": boolean
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#publicDelegatedPrefix` for public delegated prefixes.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource type. The server generates this identifier.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`region` |  `string` Output only. URL of the region where the public delegated prefix resides. This field applies only to the region resource. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.  
`ipCidrRange` |  `string` The IP address range, in CIDR format, represented by this public delegated prefix.  
`status` |  `enum` Output only. The status of the public delegated prefix, which can be one of following values: 

  * `INITIALIZING` The public delegated prefix is being initialized and addresses cannot be created yet.
  * `READY_TO_ANNOUNCE` The public delegated prefix is a live migration prefix and is active.
  * `ANNOUNCED` The public delegated prefix is announced and ready to use.
  * `DELETING` The public delegated prefix is being deprovsioned.
  * `ACTIVE` The public delegated prefix is ready to use.

  
`parentPrefix` |  `string` The URL of parent prefix. Either PublicAdvertisedPrefix or PublicDelegatedPrefix.  
`publicDelegatedSubPrefixs[]` |  `object` The list of sub public delegated prefixes that exist for this public delegated prefix.  
`publicDelegatedSubPrefixs[].name` |  `string` The name of the sub public delegated prefix.  
`publicDelegatedSubPrefixs[].description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`publicDelegatedSubPrefixs[].region` |  `string` Output only. The region of the sub public delegated prefix if it is regional. If absent, the sub prefix is global.  
`publicDelegatedSubPrefixs[].status` |  `enum` Output only. The status of the sub public delegated prefix.  
`publicDelegatedSubPrefixs[].ipCidrRange` |  `string` The IP address range, in CIDR format, represented by this sub public delegated prefix.  
`publicDelegatedSubPrefixs[].delegateeProject` |  `string` Name of the project scoping this PublicDelegatedSubPrefix.  
`publicDelegatedSubPrefixs[].isAddress` |  `boolean` Whether the sub prefix is delegated to create Address resources in the delegatee project.  
`publicDelegatedSubPrefixs[].mode` |  `enum` The PublicDelegatedSubPrefix mode for IPv6 only.  
`publicDelegatedSubPrefixs[].allocatablePrefixLength` |  `integer` The allocatable prefix length supported by this PublicDelegatedSubPrefix.  
`publicDelegatedSubPrefixs[].ipv6AccessType` |  `enum` Output only. The internet access type for IPv6 Public Delegated Sub Prefixes. Inherited from parent prefix.  
`publicDelegatedSubPrefixs[].purpose` |  `enum` Output only. The purpose of the sub public delegated prefix. Inherited from parent prefix.  
`publicDelegatedSubPrefixs[].enableEnhancedIpv4Allocation` |  `boolean` Output only. Whether this PDP supports enhanced IPv4 allocations. Applicable for IPv4 PDPs only.  
`isLiveMigration` |  `boolean` If true, the prefix will be live migrated.  
`fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a new `PublicDelegatedPrefix`. An up-to-date fingerprint must be provided in order to update the `PublicDelegatedPrefix`, otherwise the request will fail with error `412 conditionNotMet`.To see the latest fingerprint, make a `get()` request to retrieve a PublicDelegatedPrefix.A base64-encoded string.  
`mode` |  `enum` The public delegated prefix mode for IPv6 only.  
`allocatablePrefixLength` |  `integer` The allocatable prefix length supported by this public delegated prefix. This field is optional and cannot be set for prefixes in DELEGATION mode. It cannot be set for IPv4 prefixes either, and it always defaults to 32.  
`byoipApiVersion` |  `enum` Output only. The version of BYOIP API.  
`networkTier` |  `enum` Network tier of the public delegated prefix. If populated, it must match the network tier of the parent public advertised prefix. If not populated, it defaults to the network tier of the parent public advertised prefix.  
`ipv6AccessType` |  `enum` Output only. The internet access type for IPv6 Public Delegated Prefixes. Inherited from parent prefix.  
`purpose` |  `enum` Immutable. The purpose of the public delegated prefix.This field can only be set for the top-level global public delegated prefix. It is an output-only field for the sub-delegates that inherit the value from the top-level global public delegated prefix. Once the value is set, it cannot be changed.The field cannot be set for regional public delegated prefixes.The supported values are: 

  * `APPLICATION_AND_PROXY_LOAD_BALANCERS`: The global public delegated prefix can only be used by Global External Application and Proxy Load Balancers to allocate addresses for forwarding rules. This is the default value.
  * `PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP0`: The global public delegated prefix can only be used by Global External Passthrough Network Load Balancers to allocate Availability Group 0 addresses for forwarding rules.
  * `PASSTHROUGH_LOAD_BALANCER_AVAILABILITY_GROUP1`: The global public delegated prefix can only be used by Global External Passthrough Network Load Balancers to allocate Availability Group 1 addresses for forwarding rules.

  
`enableEnhancedIpv4Allocation` |  `boolean` Output only. Whether this PDP supports enhanced IPv4 allocations. Applicable for IPv4 PDPs only.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.publicDelegatedPrefixes.get`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
