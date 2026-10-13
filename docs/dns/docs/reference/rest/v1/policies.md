---
url: https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies/
title: REST Resource: policies \u00a0|\u00a0 Cloud DNS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:19.423319+00:00
---

# REST Resource: policies  |  Cloud DNS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud DNS ](https://docs.cloud.google.com/dns/docs)
  * [ Reference ](https://docs.cloud.google.com/dns/docs/apis)



Send feedback 

#  REST Resource: policies Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Policy
    * JSON representation
  * Network
    * JSON representation
  * AlternativeNameServerConfig
    * JSON representation
  * TargetNameServer
    * JSON representation
  * ForwardingPath
  * Dns64Config
    * JSON representation
  * Scope
    * JSON representation
  * Methods



## Resource: Policy

A policy is a collection of DNS rules applied to one or more Virtual Private Cloud resources.

JSON representation  
---  
      
    
    {
      "id": string,
      "name": string,
      "enableInboundForwarding": boolean,
      "description": string,
      "networks": [
        {
          object ([Network](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies#Network))
        }
      ],
      "alternativeNameServerConfig": {
        object ([AlternativeNameServerConfig](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies#AlternativeNameServerConfig))
      },
      "enableLogging": boolean,
      "dns64Config": {
        object ([Dns64Config](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies#Dns64Config))
      },
      "kind": string
    }  
  
Fields  
---  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Unique identifier for the resource; defined by the server (output only).  
`name` |  `string` User-assigned name for this policy.  
`enableInboundForwarding` |  `boolean` Allows networks bound to this policy to receive DNS queries sent by VMs or applications over VPN connections. When enabled, a virtual IP address is allocated from each of the subnetworks that are bound to this policy.  
`description` |  `string` A mutable string of at most 1024 characters associated with this resource for the user's convenience. Has no effect on the policy's function.  
`networks[]` |  `object (`[Network](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies#Network)`)` policies.list of network names specifying networks to which this policy is applied.  
`alternativeNameServerConfig` |  `object (`[AlternativeNameServerConfig](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies#AlternativeNameServerConfig)`)` Sets an alternative name server for the associated networks. When specified, all DNS queries are forwarded to a name server that you choose. Names such as .internal are not available when an alternative name server is specified.  
`enableLogging` |  `boolean` Controls whether logging is enabled for the networks bound to this policy. Defaults to no logging if not set.  
`dns64Config` |  `object (`[Dns64Config](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies#Dns64Config)`)` Configurations related to DNS64 for this policy.  
`kind` |  `string`  
  
## Network

JSON representation  
---  
      
    
    {
      "networkUrl": string,
      "kind": string
    }  
  
Fields  
---  
`networkUrl` |  `string` The fully qualified URL of the VPC network to bind to. This should be formatted like <https://www.googleapis.com/compute/v1/projects/{project}/global/networks/{network>}  
`kind` |  `string`  
  
## AlternativeNameServerConfig

JSON representation  
---  
      
    
    {
      "targetNameServers": [
        {
          object ([TargetNameServer](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies#TargetNameServer))
        }
      ],
      "kind": string
    }  
  
Fields  
---  
`targetNameServers[]` |  `object (`[TargetNameServer](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies#TargetNameServer)`)` Sets an alternative name server for the associated networks. When specified, all DNS queries are forwarded to a name server that you choose. Names such as .internal are not available when an alternative name server is specified.  
`kind` |  `string`  
  
## TargetNameServer

JSON representation  
---  
      
    
    {
      "ipv4Address": string,
      "forwardingPath": enum ([ForwardingPath](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies#ForwardingPath)),
      "ipv6Address": string,
      "kind": string
    }  
  
Fields  
---  
`ipv4Address` |  `string` IPv4 address to forward queries to.  
`forwardingPath` |  `enum (`[ForwardingPath](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies#ForwardingPath)`)` Forwarding path for this TargetNameServer. If unset or set to DEFAULT, Cloud DNS makes forwarding decisions based on address ranges; that is, RFC1918 addresses go to the VPC network, non-RFC1918 addresses go to the internet. When set to PRIVATE, Cloud DNS always sends queries through the VPC network for this target.  
`ipv6Address` |  `string` IPv6 address to forward to. Does not accept both fields (ipv4 & ipv6) being populated. Public preview as of November 2022.  
`kind` |  `string`  
  
## ForwardingPath

Enums  
---  
`default` | Cloud DNS makes forwarding decision based on IP address ranges; that is, RFC1918 addresses forward to the target through the VPC and non-RFC1918 addresses forward to the target through the internet  
`private` | Cloud DNS always forwards to this target through the VPC.  
  
## Dns64Config

DNS64 policies

JSON representation  
---  
      
    
    {
      "scope": {
        object ([Scope](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies#Scope))
      },
      "kind": string
    }  
  
Fields  
---  
`scope` |  `object (`[Scope](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies#Scope)`)` The scope to which DNS64 config will be applied to.  
`kind` |  `string`  
  
## Scope

JSON representation  
---  
      
    
    {
      "allQueries": boolean,
      "kind": string
    }  
  
Fields  
---  
`allQueries` |  `boolean` Controls whether DNS64 is enabled globally for all networks bound to the policy.  
`kind` |  `string`  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies/create)`

|  Creates a new policy.  
  
### `[delete](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies/delete)`

|  Deletes a previously created policy.  
  
### `[get](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies/get)`

|  Fetches the representation of an existing policy.  
  
### `[list](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies/list)`

|  Enumerates all policies associated with a project.  
  
### `[patch](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies/patch)`

|  Applies a partial update to an existing policy.  
  
### `[update](https://docs.cloud.google.com/dns/docs/reference/rest/v1/policies/update)`

|  Updates an existing policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-25 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-25 UTC."],[],[]] 
