---
url: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/addSubnetwork/
title: Method: services.addSubnetwork \u00a0|\u00a0 Service Infrastructure \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:36.043118+00:00
---

# Method: services.addSubnetwork  |  Service Infrastructure  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/addSubnetwork/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Service Infrastructure ](https://docs.cloud.google.com/service-infrastructure)
  * [ Reference ](https://docs.cloud.google.com/service-infrastructure/docs/apis)



Send feedback 

#  Method: services.addSubnetwork Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * SecondaryIpRangeSpec
    * JSON representation
  * Try it!



For service producers, provisions a new subnet in a peered service's shared VPC network in the requested region and with the requested size that's expressed as a CIDR range (number of leading bits of ipV4 network mask). The method checks against the assigned allocated ranges to find a non-conflicting IP address range. The method will reuse a subnet if subsequent calls contain the same subnet name, region, and prefix length. This method will make producer's tenant project to be a shared VPC service project as needed.

### HTTP request

`POST https://servicenetworking.googleapis.com/v1/{parent=services/*/*/*}:addSubnetwork`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. A tenant project in the service producer organization, in the following format: services/{service}/{collection-id}/{resource-id}. {collection-id} is the cloud resource collection type that represents the tenant project. Only `projects` are supported. {resource-id} is the tenant project numeric id, such as `123456`. {service} the name of the peering service, such as `service-peering.example.com`. This service must already be enabled in the service consumer's project. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `servicenetworking.services.addSubnetwork`

  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "consumerNetwork": string,
      "subnetwork": string,
      "region": string,
      "ipPrefixLength": integer,
      "description": string,
      "subnetworkUsers": [
        string
      ],
      "consumer": string,
      "requestedAddress": string,
      "secondaryIpRangeSpecs": [
        {
          object ([SecondaryIpRangeSpec](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/addSubnetwork#SecondaryIpRangeSpec))
        }
      ],
      "privateIpv6GoogleAccess": string,
      "requestedRanges": [
        string
      ],
      "outsideAllocationPublicIpRange": string,
      "purpose": string,
      "checkServiceNetworkingUsePermission": boolean,
      "useCustomComputeIdempotencyWindow": boolean,
      "computeIdempotencyWindow": string,
      "allowSubnetCidrRoutesOverlap": boolean,
      "role": string,
      "internalRange": string,
      "skipRequestedAddressValidation": boolean
    }  
  
Fields  
---  
`consumerNetwork` |  `string` Required. The name of the service consumer's VPC network. The network must have an existing private connection that was provisioned through the connections.create method. The name must be in the following format: `projects/{project}/global/networks/{network}`, where {project} is a project number, such as `12345`. {network} is the name of a VPC network in the project.  
`subnetwork` |  `string` Required. A name for the new subnet. For information about the naming requirements, see [subnetwork](https://cloud.google.com/compute/docs/reference/rest/v1/subnetworks) in the Compute API documentation.  
`region` |  `string` Required. The name of a [region](https://cloud.google.com/compute/docs/regions-zones) for the subnet, such `europe-west1`.  
`ipPrefixLength` |  `integer` Required. The prefix length of the subnet's IP address range. Use CIDR range notation, such as `29` to provision a subnet with an `x.x.x.x/29` CIDR range. The IP address range is drawn from a pool of available ranges in the service consumer's allocated range. Google Compute Engine disallows subnets with prefix_length > 29  
`description` |  `string` Optional. Description of the subnet.  
`subnetworkUsers[]` |  `string` A list of members that are granted the `roles/servicenetworking.subnetworkAdmin` role on the subnet.  
`consumer` |  `string` Required. A resource that represents the service consumer, such as `projects/123456`. The project number can be different from the value in the consumer network parameter. For example, the network might be part of a Shared VPC network. In those cases, Service Networking validates that this resource belongs to that Shared VPC.  
`requestedAddress` |  `string` Optional. The starting address of a range. The address must be a valid IPv4 address in the x.x.x.x format. This value combined with the IP prefix range is the CIDR range for the subnet. The range must be within the allocated range that is assigned to the private connection. If the CIDR range isn't available, the call fails.  
`secondaryIpRangeSpecs[]` |  `object (`[SecondaryIpRangeSpec](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/services/addSubnetwork#SecondaryIpRangeSpec)`)` Optional. A list of secondary IP ranges to be created within the new subnetwork.  
`privateIpv6GoogleAccess` |  `string` Optional. The private IPv6 google access type for the VMs in this subnet. For information about the access types that can be set using this field, see [subnetwork](https://cloud.google.com/compute/docs/reference/rest/v1/subnetworks) in the Compute API documentation.  
`requestedRanges[]` |  `string` Optional. The name of one or more allocated IP address ranges associated with this private service access connection. If no range names are provided all ranges associated with this connection will be considered. If a CIDR range with the specified IP prefix length is not available within these ranges, the call fails.  
`outsideAllocationPublicIpRange` |  `string` Optional. Enable outside allocation using public IP addresses. Any public IP range may be specified. If this field is provided, consumer allocated ranges aren't used for this primary IP range.  
`purpose` |  `string` Optional. Defines the purpose field of the subnet, e.g. 'PRIVATE_SERVICE_CONNECT'. For information about the purposes that can be set using this field, see [subnetwork](https://cloud.google.com/compute/docs/reference/rest/v1/subnetworks) in the Compute API documentation.  
`checkServiceNetworkingUsePermission` |  `boolean` Optional. The IAM permission check determines whether the consumer project has 'servicenetworking.services.use' permission or not.  
`useCustomComputeIdempotencyWindow` |  `boolean` Optional. Specifies if Service Networking should use a custom window for Compute Engine API requests. If false, Service Networking uses a 300 second (5 minute) idempotency window. If true, Service Networking uses the custom idempotency window provided in field computeIdempotencyWindow.  
`computeIdempotencyWindow` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Specifies a custom time window for subnetwork request idempotency. If two equivalent concurrent requests are made, the Compute Engine API ignores one request if the other has already been completed or is in progress. Only requests with matching computeIdempotencyWindow have guaranteed idempotency. Changing this time window between requests results in undefined behavior. Zero (or empty) value with custom_compute_idempotency_window=true specifies no idempotency (i.e. no request ID is provided to the Compute Engine API). Maximum value of 14 days.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`allowSubnetCidrRoutesOverlap` |  `boolean` Optional. Defines the allowSubnetCidrRoutesOverlap field of the subnet, e.g. Available in alpha and beta according to [Compute API documentation](https://cloud.google.com/compute/docs/reference/rest/beta/subnetworks/insert)  
`role` |  `string` Optional. Defines the role field of the subnet, e.g. 'ACTIVE'. For information about the roles that can be set using this field, see [subnetwork](https://cloud.google.com/compute/docs/reference/rest/v1/subnetworks) in the Compute API documentation.  
`internalRange` |  `string` Optional. The url of an internal range. Eg: `projects/<project_number>/locations/global/internalRanges/<internal_range_name>`. If specified, it means that the subnetwork CIDR is created using the combination of requestedAddress and ipPrefixLength. Note that the subnet CIDR has to be within the CIDR range of this internal range.  
`skipRequestedAddressValidation` |  `boolean` Optional. Skips validating if the requestedAddress is in use by SN VPC's peering group. Compute Engine will still perform this check and fail the request if the requestedAddress is in use. Note that Compute Engine does not check for the existence of dynamic routes when performing this check. Caller of this API should make sure that there are no dynamic routes overlapping with the requestedAddress/prefix_length IP address range otherwise the created subnet could cause misrouting.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/service-infrastructure/docs/service-networking/reference/rest/v1/operations#Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/service.management`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## SecondaryIpRangeSpec

JSON representation  
---  
      
    
    {
      "rangeName": string,
      "ipPrefixLength": integer,
      "requestedAddress": string,
      "outsideAllocationPublicIpRange": string
    }  
  
Fields  
---  
`rangeName` |  `string` Required. A name for the secondary IP range. The name must be 1-63 characters long, and comply with RFC1035. The name must be unique within the subnetwork.  
`ipPrefixLength` |  `integer` Required. The prefix length of the secondary IP range. Use CIDR range notation, such as `30` to provision a secondary IP range with an `x.x.x.x/30` CIDR range. The IP address range is drawn from a pool of available ranges in the service consumer's allocated range.  
`requestedAddress` |  `string` Optional. The starting address of a range. The address must be a valid IPv4 address in the x.x.x.x format. This value combined with the IP prefix range is the CIDR range for the secondary IP range. The range must be within the allocated range that is assigned to the private connection. If the CIDR range isn't available, the call fails.  
`outsideAllocationPublicIpRange` |  `string` Optional. Enable outside allocation using public IP addresses. Any public IP range may be specified. If this field is provided, consumer allocated ranges aren't used for this secondary IP range.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-10 UTC."],[],[]] 
