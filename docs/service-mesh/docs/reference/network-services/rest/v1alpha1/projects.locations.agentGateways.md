---
url: https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways
title: REST Resource: projects.locations.agentGateways \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:49:57.130835+00:00
---

# REST Resource: projects.locations.agentGateways  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/service-mesh/docs/apis)



Send feedback 

#  REST Resource: projects.locations.agentGateways Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AgentGateway
    * JSON representation
  * GoogleManaged
    * JSON representation
  * GovernedAccessPath
  * SelfManaged
    * JSON representation
  * Protocol
  * NetworkConfig
    * JSON representation
  * Egress
    * JSON representation
  * DnsPeeringConfig
    * JSON representation
  * AgentGatewayOutputCard
    * JSON representation
  * Methods



## Resource: AgentGateway

AgentGateway represents the agent gateway resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "description": string,
      "etag": string,
      "protocols": [
        enum ([Protocol](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways#Protocol))
      ],
      "registries": [
        string
      ],
      "networkConfig": {
        object ([NetworkConfig](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways#NetworkConfig))
      },
      "agentGatewayCard": {
        object ([AgentGatewayOutputCard](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways#AgentGatewayOutputCard))
      },
    
      // Union field deployment_mode can be only one of the following:
      "googleManaged": {
        object ([GoogleManaged](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways#GoogleManaged))
      },
      "selfManaged": {
        object ([SelfManaged](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways#SelfManaged))
      }
      // End of list of possible types for union field deployment_mode.
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the AgentGateway resource. It matches pattern `projects/*/locations/*/agentGateways/<agentGateway>`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Set of label tags associated with the AgentGateway resource.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`description` |  `string` Optional. A free-text description of the resource. Max length 1024 characters.  
`etag` |  `string` Optional. Etag of the resource. If this is provided, it must match the server's etag. If the provided etag does not match the server's etag, the request will fail with a 409 ABORTED error.  
`protocols[]` |  `enum (`[Protocol](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways#Protocol)`)` Required. List of protocols supported by an Agent Gateway  
`registries[]` |  `string` Optional. A list of Agent registries containing the agents, MCP servers and tools governed by the Agent Gateway. Note: Currently limited to project-scoped registries Must be of format `//agentregistry.googleapis.com/projects/{project}/locations/{location}/  
`networkConfig` |  `object (`[NetworkConfig](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways#NetworkConfig)`)` Optional. Network configuration for the AgentGateway.  
`agentGatewayCard` |  `object (`[AgentGatewayOutputCard](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways#AgentGatewayOutputCard)`)` Output only. Field for populated AgentGateway card.  
Union field `deployment_mode`. Deployment mode of the network proxy. Exactly one of the fields in this `oneof` must be set. `deployment_mode` can be only one of the following:  
`googleManaged` |  `object (`[GoogleManaged](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways#GoogleManaged)`)` Optional. Proxy is orchestrated and managed by GoogleCloud in a tenant project.  
`selfManaged` |  `object (`[SelfManaged](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways#SelfManaged)`)` Optional. Attach to existing Application Load Balancers or Secure Web Proxies.  
  
## GoogleManaged

Configuration for Google Managed deployment mode. Proxy is orchestrated and managed by GoogleCloud in a tenant project.

JSON representation  
---  
      
    
    {
      "governedAccessPath": enum ([GovernedAccessPath](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways#GovernedAccessPath))
    }  
  
Fields  
---  
`governedAccessPath` |  `enum (`[GovernedAccessPath](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways#GovernedAccessPath)`)` Optional. Operating Mode of Agent Gateway.  
  
## GovernedAccessPath

GovernedAccessPath defines the type of access to protect.

Enums  
---  
`GOVERNED_ACCESS_PATH_UNSPECIFIED` | Governed access path is not specified.  
`AGENT_TO_ANYWHERE` | Govern agent conections to destinations.  
`CLIENT_TO_AGENT` | Protect connection to Agent or Tool.  
  
## SelfManaged

Configuration for Self Managed deployment mode. Attach to existing Application Load Balancers or Secure Web Proxies.

JSON representation  
---  
      
    
    {
      "resourceUri": string
    }  
  
Fields  
---  
`resourceUri` |  `string` Optional. A supported Google Cloud networking proxy in the Project and Location  
  
## Protocol

Enums of all supported protocols

Enums  
---  
`PROTOCOL_UNSPECIFIED` | Unspecified protocol.  
`MCP` | Message Control Plane protocol.  
  
## NetworkConfig

NetworkConfig contains network configurations for the AgentGateway.

JSON representation  
---  
      
    
    {
      "egress": {
        object ([Egress](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways#Egress))
      },
      "dnsPeeringConfig": {
        object ([DnsPeeringConfig](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways#DnsPeeringConfig))
      }
    }  
  
Fields  
---  
`egress` |  `object (`[Egress](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways#Egress)`)` Optional. Optional PSC-Interface network attachment for connectivity to your private VPCs network.  
`dnsPeeringConfig` |  `object (`[DnsPeeringConfig](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways#DnsPeeringConfig)`)` Optional. Optional DNS peering configuration for connectivity to your private VPC network.  
  
## Egress

Configuration for Egress

JSON representation  
---  
      
    
    {
      "networkAttachment": string
    }  
  
Fields  
---  
`networkAttachment` |  `string` Optional. The URI of the Network Attachment resource.  
  
## DnsPeeringConfig

DNS peering config for the user VPC network.

JSON representation  
---  
      
    
    {
      "domains": [
        string
      ],
      "targetProject": string,
      "targetNetwork": string
    }  
  
Fields  
---  
`domains[]` |  `string` Required. Domain names for which DNS queries should be forwarded to the target network.  
`targetProject` |  `string` Required. Target project ID to which DNS queries should be forwarded to. This can be the same project that contains the AgentGateway or a different project.  
`targetNetwork` |  `string` Required. Target network in 'target project' to which DNS queries should be forwarded to. Must be in format of `projects/{project}/global/networks/{network}`.  
  
## AgentGatewayOutputCard

AgentGatewayOutputCard contains informational output-only fields

JSON representation  
---  
      
    
    {
      "mtlsEndpoint": string,
      "rootCertificates": [
        string
      ],
      "serviceExtensionsServiceAccount": string
    }  
  
Fields  
---  
`mtlsEndpoint` |  `string` Output only. mTLS Endpoint associated with this AgentGateway  
`rootCertificates[]` |  `string` Output only. Root Certificates for Agents to validate this AgentGateway  
`serviceExtensionsServiceAccount` |  `string` Output only. Service Account used by Service Extensions to operate.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways/create)`

|  Creates a new AgentGateway in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways/delete)`

|  Deletes a single AgentGateway.  
  
### `[get](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways/get)`

|  Gets details of a single AgentGateway.  
  
### `[list](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways/list)`

|  Lists AgentGateways in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/service-mesh/docs/reference/network-services/rest/v1alpha1/projects.locations.agentGateways/patch)`

|  Updates the parameters of a single AgentGateway.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-01 UTC."],[],[]] 
