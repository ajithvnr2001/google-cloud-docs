---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/validate/
title: Method: services.validate \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:08.166057+00:00
---

# Method: services.validate  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/validate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: services.validate Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * ConsumerProject
    * JSON representation
  * RangeReservation
    * JSON representation
  * Subnetwork
    * JSON representation
  * SecondaryIpRange
    * JSON representation
  * ValidationError
  * Try it!



Service producers use this method to validate if the consumer provided network, project and requested range are valid. This allows them to use a fail-fast mechanism for consumer requests, and not have to wait for services.addSubnetwork operation completion to determine if user request is invalid.

### HTTP request

`POST https://servicenetworking.googleapis.com/v1/{parent=services/*}:validate`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. This is in a form services/{service} where {service} is the name of the private access management service. For example 'service-peering.example.com'. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `servicenetworking.services.addSubnetwork`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "consumerNetwork": string,
      "validateNetwork": boolean,
      "consumerProject": {
        object ([ConsumerProject](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/validate#ConsumerProject))
      },
      "rangeReservation": {
        object ([RangeReservation](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/validate#RangeReservation))
      },
      "checkServiceNetworkingUsePermission": boolean
    }  
  
Fields  
---  
`consumerNetwork` |  `string` Required. The network that the consumer is using to connect with services. Must be in the form of projects/{project}/global/networks/{network} {project} is a project number, as in '12345' {network} is network name.  
`validateNetwork` |  `boolean` The validations will be performed in the order listed in the ValidationError enum. The first failure will return. If a validation is not requested, then the next one will be performed. SERVICE_NETWORKING_NOT_ENABLED and NETWORK_NOT_PEERED checks are performed for all requests where validation is requested. NETWORK_NOT_FOUND and NETWORK_DISCONNECTED checks are done for requests that have validateNetwork set to true.  
`consumerProject` |  `object (`[ConsumerProject](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/validate#ConsumerProject)`)` NETWORK_NOT_IN_CONSUMERS_PROJECT, NETWORK_NOT_IN_CONSUMERS_HOST_PROJECT, and HOST_PROJECT_NOT_FOUND are done when consumerProject is provided.  
`rangeReservation` |  `object (`[RangeReservation](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/validate#RangeReservation)`)` RANGES_EXHAUSTED, RANGES_NOT_RESERVED, and RANGES_DELETED_LATER are done when rangeReservation is provided.  
`checkServiceNetworkingUsePermission` |  `boolean` Optional. The IAM permission check determines whether the consumer has 'servicenetworking.services.use' permission or not.  
  
### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "isValid": boolean,
      "validationError": enum ([ValidationError](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/validate#ValidationError)),
      "existingSubnetworkCandidates": [
        {
          object ([Subnetwork](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/validate#Subnetwork))
        }
      ]
    }  
  
Fields  
---  
`isValid` |  `boolean` Indicates whether all the requested validations passed.  
`validationError` |  `enum (`[ValidationError](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/validate#ValidationError)`)` The first validation which failed.  
`existingSubnetworkCandidates[]` |  `object (`[Subnetwork](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/validate#Subnetwork)`)` List of subnetwork candidates from the request which exist with the `ipCidrRange`, `secondary_ip_cider_ranges`, and `outsideAllocation` fields set.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## ConsumerProject

Represents a consumer project.

JSON representation  
---  
      
    
    {
      "projectNum": string
    }  
  
Fields  
---  
`projectNum` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. Project number of the consumer that is launching the service instance. It can own the network that is peered with Google or, be a service project in an XPN where the host project has the network.  
  
## RangeReservation

Represents a range reservation.

JSON representation  
---  
      
    
    {
      "ipPrefixLength": integer,
      "secondaryRangeIpPrefixLengths": [
        integer
      ],
      "requestedRanges": [
        string
      ],
      "subnetworkCandidates": [
        {
          object ([Subnetwork](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/validate#Subnetwork))
        }
      ]
    }  
  
Fields  
---  
`ipPrefixLength` |  `integer` Required. The size of the desired subnet. Use usual CIDR range notation. For example, '29' to find unused x.x.x.x/29 CIDR range. The goal is to determine if one of the allocated ranges has enough free space for a subnet of the requested size. Google Compute Engine disallows subnets with prefix_length > 29  
`secondaryRangeIpPrefixLengths[]` |  `integer` Optional. The size of the desired secondary ranges for the subnet. Use usual CIDR range notation. For example, '29' to find unused x.x.x.x/29 CIDR range. The goal is to determine that the allocated ranges have enough free space for all the requested secondary ranges. Google ComputeEngine disallows subnets with prefix_length > 29  
`requestedRanges[]` |  `string` Optional. The name of one or more allocated IP address ranges associated with this private service access connection. If no range names are provided all ranges associated with this connection will be considered. If a CIDR range with the specified IP prefix length is not available within these ranges the validation fails.  
`subnetworkCandidates[]` |  `object (`[Subnetwork](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/validate#Subnetwork)`)` Optional. List of subnetwork candidates to validate. The required input fields are `name`, `network`, and `region`. Subnetworks from this list which exist will be returned in the response with the `ipCidrRange`, `secondary_ip_cider_ranges`, and `outsideAllocation` fields set.  
  
## Subnetwork

Represents a subnet that was created or discovered by a private access management service.

JSON representation  
---  
      
    
    {
      "name": string,
      "ipCidrRange": string,
      "network": string,
      "outsideAllocation": boolean,
      "secondaryIpRanges": [
        {
          object ([SecondaryIpRange](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/validate#SecondaryIpRange))
        }
      ],
      "region": string
    }  
  
Fields  
---  
`name` |  `string` Subnetwork name. See <https://cloud.google.com/compute/docs/vpc/>  
`ipCidrRange` |  `string` Subnetwork CIDR range in `10.x.x.x/y` format.  
`network` |  `string` In the Shared VPC host project, the VPC network that's peered with the consumer network. For example: `projects/1234321/global/networks/host-network`  
`outsideAllocation` |  `boolean` This is a discovered subnet that is not within the current consumer allocated ranges.  
`secondaryIpRanges[]` |  `object (`[SecondaryIpRange](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/validate#SecondaryIpRange)`)` List of secondary IP ranges in this subnetwork.  
`region` |  `string` GCP region where the subnetwork is located.  
  
## SecondaryIpRange

JSON representation  
---  
      
    
    {
      "rangeName": string,
      "ipCidrRange": string
    }  
  
Fields  
---  
`rangeName` |  `string` Name of the secondary IP range.  
`ipCidrRange` |  `string` Secondary IP CIDR range in `x.x.x.x/y` format.  
  
## ValidationError

Enums  
---  
`VALIDATION_ERROR_UNSPECIFIED` |   
`VALIDATION_NOT_REQUESTED` | In case none of the validations are requested.  
`SERVICE_NETWORKING_NOT_ENABLED` |   
`NETWORK_NOT_FOUND` | The network provided by the consumer does not exist.  
`NETWORK_NOT_PEERED` | The network has not been peered with the producer org.  
`NETWORK_PEERING_DELETED` | The peering was created and later deleted.  
`NETWORK_NOT_IN_CONSUMERS_PROJECT` | The network is a regular VPC but the network is not in the consumer's project.  
`NETWORK_NOT_IN_CONSUMERS_HOST_PROJECT` | The consumer project is a service project, and network is a shared VPC, but the network is not in the host project of this consumer project.  
`HOST_PROJECT_NOT_FOUND` | The host project associated with the consumer project was not found.  
`CONSUMER_PROJECT_NOT_SERVICE_PROJECT` | The consumer project is not a service project for the specified host project.  
`RANGES_EXHAUSTED` | The reserved IP ranges do not have enough space to create a subnet of desired size.  
`RANGES_NOT_RESERVED` | The IP ranges were not reserved.  
`RANGES_DELETED_LATER` | The IP ranges were reserved but deleted later.  
`COMPUTE_API_NOT_ENABLED` | The consumer project does not have the compute api enabled.  
`USE_PERMISSION_NOT_FOUND` | The consumer project does not have the permission from the host project.  
`SN_SERVICE_AGENT_PERMISSION_DENIED_ON_CONSUMER_PROJECT` | The Service Networking service agent {service-@service-networking.iam.gserviceaccount.com} does not have the Service Networking service agent role on the consumer project.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-10 UTC."],[],[]] 
