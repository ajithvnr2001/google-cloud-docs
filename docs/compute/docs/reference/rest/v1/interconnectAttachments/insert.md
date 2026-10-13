---
url: https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments/insert/
title: Method: interconnectAttachments.insert \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:16.908840+00:00
---

# Method: interconnectAttachments.insert  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/v1/interconnectAttachments/insert/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: interconnectAttachments.insert Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Response body
    * JSON representation
      * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
        * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Creates an InterconnectAttachment in the specified project using the data included in the request.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`POST https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/interconnectAttachments`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` Name of the region for this request.  
  
### Query parameters

Parameters  
---  
`requestId` |  `string` An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid [UUID](https://tools.ietf.org/html/rfc4122) with the exception that zero UUID is not supported (`00000000-0000-0000-0000-000000000000`).  
`validateOnly` |  `boolean` If true, the request will not be committed.  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "description": string,
      "selfLink": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "interconnect": string,
      "router": string,
      "region": string,
      "googleReferenceId": string,
      "mtu": integer,
      "privateInterconnectInfo": {
        "tag8021q": integer
      },
      "operationalStatus": enum,
      "cloudRouterIpAddress": string,
      "customerRouterIpAddress": string,
      "type": enum,
      "pairingKey": string,
      "adminEnabled": boolean,
      "vlanTag8021q": integer,
      "edgeAvailabilityDomain": enum,
      "candidateSubnets": [
        string
      ],
      "bandwidth": enum,
      "partnerMetadata": {
        "partnerName": string,
        "interconnectName": string,
        "portalUrl": string
      },
      "labels": {
        string: string,
        ...
      },
      "labelFingerprint": string,
      "state": enum,
      "partnerAsn": string,
      "encryption": enum,
      "ipsecInternalAddresses": [
        string
      ],
      "dataplaneVersion": integer,
      "satisfiesPzs": boolean,
      "stackType": enum,
      "cloudRouterIpv6Address": string,
      "customerRouterIpv6Address": string,
      "candidateIpv6Subnets": [
        string
      ],
      "cloudRouterIpv6InterfaceId": string,
      "customerRouterIpv6InterfaceId": string,
      "subnetLength": integer,
      "remoteService": string,
      "configurationConstraints": {
        "bgpMd5": enum,
        "bgpPeerAsnRanges": [
          {
            "min": integer,
            "max": integer
          }
        ]
      },
      "attachmentGroup": string,
      "l2Forwarding": {
        "applianceMappings": {
          string: {
            "name": string,
            "applianceIpAddress": string,
            "innerVlanToApplianceMappings": [
              {
                "innerVlanTags": [
                  string
                ],
                "innerApplianceIpAddress": string
              }
            ]
          },
          ...
        },
        "network": string,
        "geneveHeader": {
          "vni": integer
        },
        "defaultApplianceIpAddress": string,
        "tunnelEndpointIpAddress": string
      },
      "candidateCloudRouterIpAddress": string,
      "candidateCustomerRouterIpAddress": string,
      "candidateCloudRouterIpv6Address": string,
      "candidateCustomerRouterIpv6Address": string,
      "params": {
        "resourceManagerTags": {
          string: string,
          ...
        }
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#interconnectAttachment` for interconnect attachments.  
`description` |  `string` An optional description of this resource.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`interconnect` |  `string` URL of the underlying Interconnect object that this attachment's traffic will traverse through. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `interconnect`:

  * `resourcemanager.projects.get`

  
`router` |  `string` URL of the Cloud Router to be used for dynamic routing. This router must be in the same region as this InterconnectAttachment. The InterconnectAttachment will automatically connect the Interconnect to the network & region within which the Cloud Router is configured. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `router`:

  * `resourcemanager.projects.get`

  
`region` |  `string` Output only. URL of the region where the regional interconnect attachment resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.  
`googleReferenceId  
**(deprecated)**` |  `string` Output only. Google reference ID, to be used when raising support tickets with Google or otherwise to debug backend connectivity issues. [Deprecated] This field is not used.  
`mtu` |  `integer` Maximum Transmission Unit (MTU), in bytes, of packets passing through this interconnect attachment. Valid values are 1440, 1460, 1500, and 8896. If not specified, the value will default to 1440.  
`privateInterconnectInfo` |  `object` Output only. Information specific to an InterconnectAttachment. This property is populated if the interconnect that this is attached to is of type DEDICATED.  
`privateInterconnectInfo.tag8021q` |  `integer` Output only. 802.1q encapsulation tag to be used for traffic between Google and the customer, going to and from this network and region.  
`operationalStatus` |  `enum` Output only. The current status of whether or not this interconnect attachment is functional, which can take one of the following values: 

  * OS_ACTIVE: The attachment has been turned up and is ready to use.
  * OS_UNPROVISIONED: The attachment is not ready to use yet, because turnup is not complete.

  
`cloudRouterIpAddress` |  `string` Output only. IPv4 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.  
`customerRouterIpAddress` |  `string` Output only. IPv4 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.  
`type` |  `enum` The type of interconnect attachment this is, which can take one of the following values: 

  * DEDICATED: an attachment to a Dedicated Interconnect.
  * PARTNER: an attachment to a Partner Interconnect, created by the customer.
  * PARTNER_PROVIDER: an attachment to a Partner Interconnect, created by the partner.


* L2_DEDICATED: a L2 attachment to a Dedicated Interconnect.  
`pairingKey` |  `string` [Output only for type PARTNER. Input only for PARTNER_PROVIDER. Not present for DEDICATED]. The opaque identifier of a PARTNER attachment used to initiate provisioning with a selected partner. Of the form "XXXXX/region/domain"  
`adminEnabled` |  `boolean` Determines whether this Attachment will carry packets. Not present for PARTNER_PROVIDER.  
`vlanTag8021q` |  `integer` The IEEE 802.1Q VLAN tag for this attachment, in the range 2-4093. Only specified at creation time.  
`edgeAvailabilityDomain` |  `enum` Input only. Desired availability domain for the attachment. Only available for type PARTNER, at creation time, and can take one of the following values: 

  * AVAILABILITY_DOMAIN_ANY
  * AVAILABILITY_DOMAIN_1
  * AVAILABILITY_DOMAIN_2

For improved reliability, customers should configure a pair of attachments, one per availability domain. The selected availability domain will be provided to the Partner via the pairing key, so that the provisioned circuit will lie in the specified domain. If not specified, the value will default to AVAILABILITY_DOMAIN_ANY.   
`candidateSubnets[]` |  `string` Input only. Up to 16 candidate prefixes that can be used to restrict the allocation of cloudRouterIpAddress and customerRouterIpAddress for this attachment. All prefixes must be within link-local address space (169.254.0.0/16) and must be /29 or shorter (/28, /27, etc). Google will attempt to select an unused /29 from the supplied candidate prefix(es). The request will fail if all possible /29s are in use on Google's edge. If not supplied, Google will randomly select an unused /29 from all of link-local space.  
`bandwidth` |  `enum` Provisioned bandwidth capacity for the interconnect attachment. For attachments of type DEDICATED, the user can set the bandwidth. For attachments of type PARTNER, the Google Partner that is operating the interconnect must set the bandwidth. Output only for PARTNER type, mutable for PARTNER_PROVIDER and DEDICATED, and can take one of the following values: 

  * BPS_50M: 50 Mbit/s
  * BPS_100M: 100 Mbit/s
  * BPS_200M: 200 Mbit/s
  * BPS_300M: 300 Mbit/s
  * BPS_400M: 400 Mbit/s
  * BPS_500M: 500 Mbit/s
  * BPS_1G: 1 Gbit/s
  * BPS_2G: 2 Gbit/s
  * BPS_5G: 5 Gbit/s
  * BPS_10G: 10 Gbit/s
  * BPS_20G: 20 Gbit/s
  * BPS_50G: 50 Gbit/s
  * BPS_100G: 100 Gbit/s
  * BPS_400G: 400 Gbit/s

  
`partnerMetadata` |  `object` Informational metadata about Partner attachments from Partners to display to customers. Output only for PARTNER type, mutable for PARTNER_PROVIDER, not available for DEDICATED.  
`partnerMetadata.partnerName` |  `string` Plain text name of the Partner providing this attachment. This value may be validated to match approved Partner values.  
`partnerMetadata.interconnectName` |  `string` Plain text name of the Interconnect this attachment is connected to, as displayed in the Partner's portal. For instance "Chicago 1". This value may be validated to match approved Partner values.  
`partnerMetadata.portalUrl` |  `string` URL of the Partner's portal for this Attachment. Partners may customise this to be a deep link to the specific resource on the Partner portal. This value may be validated to match approved Partner values.  
`labels` |  `map (key: string, value: string)` Labels for this resource. These can only be added or modified by the `setLabels` method. Each label key/value pair must comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `labels`:

  * `compute.interconnectAttachments.setLabels`

  
`labelFingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A fingerprint for the labels being applied to this InterconnectAttachment, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error `412 conditionNotMet`.To see the latest fingerprint, make a `get()` request to retrieve an InterconnectAttachment.A base64-encoded string.  
`state` |  `enum` Output only. The current state of this attachment's functionality. Enum values ACTIVE and UNPROVISIONED are shared by DEDICATED/PRIVATE, PARTNER, and PARTNER_PROVIDER interconnect attachments, while enum values PENDING_PARTNER, PARTNER_REQUEST_RECEIVED, and PENDING_CUSTOMER are used for only PARTNER and PARTNER_PROVIDER interconnect attachments. This state can take one of the following values: 

  * ACTIVE: The attachment has been turned up and is ready to use.
  * UNPROVISIONED: The attachment is not ready to use yet, because turnup is not complete.
  * PENDING_PARTNER: A newly-created PARTNER attachment that has not yet been configured on the Partner side.
  * PARTNER_REQUEST_RECEIVED: A PARTNER attachment is in the process of provisioning after a PARTNER_PROVIDER attachment was created that references it.
  * PENDING_CUSTOMER: A PARTNER or PARTNER_PROVIDER attachment that is waiting for a customer to activate it.
  * DEFUNCT: The attachment was deleted externally and is no longer functional. This could be because the associated Interconnect was removed, or because the other side of a Partner attachment was deleted.

  
`partnerAsn` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional BGP ASN for the router supplied by a Layer 3 Partner if they configured BGP on behalf of the customer. Output only for PARTNER type, input only for PARTNER_PROVIDER, not available for DEDICATED.  
`encryption` |  `enum` Indicates the user-supplied encryption option of this VLAN attachment (interconnectAttachment). Can only be specified at attachment creation for PARTNER or DEDICATED attachments. Possible values are: 

  * `NONE` \- This is the default value, which means that the VLAN attachment carries unencrypted traffic. VMs are able to send traffic to, or receive traffic from, such a VLAN attachment.
  * `IPSEC` \- The VLAN attachment carries only encrypted traffic that is encrypted by an IPsec device, such as an HA VPN gateway or third-party IPsec VPN. VMs cannot directly send traffic to, or receive traffic from, such a VLAN attachment. To use _HA VPN over Cloud Interconnect_ , the VLAN attachment must be created with this option.

  
`ipsecInternalAddresses[]` |  `string` A list of URLs of addresses that have been reserved for the VLAN attachment. Used only for the VLAN attachment that has the encryption option as IPSEC. The addresses must be regional internal IP address ranges. When creating an HA VPN gateway over the VLAN attachment, if the attachment is configured to use a regional internal IP address, then the VPN gateway's IP address is allocated from the IP address range specified here. For example, if the HA VPN gateway's interface 0 is paired to this VLAN attachment, then a regional internal IP address for the VPN gateway interface 0 will be allocated from the IP address specified for this VLAN attachment. If this field is not specified when creating the VLAN attachment, then later on when creating an HA VPN gateway on this VLAN attachment, the HA VPN gateway's IP address is allocated from the regional external IP address pool.  
`dataplaneVersion` |  `integer` Output only. Dataplane version for this InterconnectAttachment. This field is only present for Dataplane version 2 and higher. Absence of this field in the API output indicates that the Dataplane is version 1.  
`satisfiesPzs` |  `boolean` Output only. Reserved for future use.  
`stackType` |  `enum` The stack type for this interconnect attachment to identify whether the IPv6 feature is enabled or not. If not specified, `IPV4_ONLY` will be used.This field can be both set at interconnect attachments creation and update interconnect attachment operations.  
`cloudRouterIpv6Address` |  `string` Output only. IPv6 address + prefix length to be configured on Cloud Router Interface for this interconnect attachment.  
`customerRouterIpv6Address` |  `string` Output only. IPv6 address + prefix length to be configured on the customer router subinterface for this interconnect attachment.  
`candidateIpv6Subnets[]` |  `string` This field is not available.  
`cloudRouterIpv6InterfaceId` |  `string` This field is not available.  
`customerRouterIpv6InterfaceId` |  `string` This field is not available.  
`subnetLength` |  `integer` Input only. Length of the IPv4 subnet mask. Allowed values: 

  * 29 (default)
  * 30

The default value is 29, except for Cross-Cloud Interconnect connections that use an InterconnectRemoteLocation with a constraints.subnetLengthRange.min equal to 30. For example, connections that use an Azure remote location fall into this category. In these cases, the default value is 30, and requesting 29 returns an error. Where both 29 and 30 are allowed, 29 is preferred, because it gives Google Cloud Support more debugging visibility.  
`remoteService` |  `string` Output only. If the attachment is on a Cross-Cloud Interconnect connection, this field contains the interconnect's remote location service provider. Example values: "Amazon Web Services" "Microsoft Azure".The field is set only for attachments on Cross-Cloud Interconnect connections. Its value is copied from the InterconnectRemoteLocation remoteService field.  
`configurationConstraints` |  `object` Output only. Constraints for this attachment, if any. The attachment does not work if these constraints are not met.  
`configurationConstraints.bgpMd5` |  `enum` Output only. Whether the attachment's BGP session requires/allows/disallows BGP MD5 authentication. This can take one of the following values: MD5_OPTIONAL, MD5_REQUIRED, MD5_UNSUPPORTED.For example, a Cross-Cloud Interconnect connection to a remote cloud provider that requires BGP MD5 authentication has the interconnectRemoteLocation attachmentConfigurationConstraints.bgp_md5 field set to MD5_REQUIRED, and that property is propagated to the attachment. Similarly, if BGP MD5 is MD5_UNSUPPORTED, an error is returned if MD5 is requested.  
`configurationConstraints.bgpPeerAsnRanges[]` |  `object` Output only. interconnectAttachments.list of ASN ranges that the remote location is known to support. Formatted as an array of inclusive ranges {min: min-value, max: max-value}. For example, [{min: 123, max: 123}, {min: 64512, max: 65534}] allows the peer ASN to be 123 or anything in the range 64512-65534.This field is only advisory. Although the API accepts other ranges, these are the ranges that we recommend.  
`configurationConstraints.bgpPeerAsnRanges[].min` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)`  
`configurationConstraints.bgpPeerAsnRanges[].max` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)`  
`attachmentGroup` |  `string` Output only. URL of the AttachmentGroup that includes this Attachment.  
`l2Forwarding` |  `object` L2 Interconnect Attachment related config. This field is required if the type is L2_DEDICATED.The configuration specifies how VLAN tags (like dot1q, qinq, or dot1ad) within L2 packets are mapped to the destination appliances IP addresses. The packet is then encapsulated with the appliance IP address and sent to the edge appliance.  
`l2Forwarding.applianceMappings[]` |  `map (key: string, value: object)` Optional. A map of VLAN tags to appliances and optional inner mapping rules. If VLANs are not explicitly mapped to any appliance, the defaultApplianceIpAddress is used.Each VLAN tag can be a single number or a range of numbers in the range of 1 to 4094, e.g., "1" or "4001-4094". Non-empty and non-overlapping VLAN tag ranges are enforced, and violating operations will be rejected.The VLAN tags in the Ethernet header must use an ethertype value of 0x88A8 or 0x8100.  
`l2Forwarding.applianceMappings[].name` |  `string` Optional. The name of this appliance mapping rule.  
`l2Forwarding.applianceMappings[].applianceIpAddress` |  `string` Optional. A single IPv4 or IPv6 address used as the destination IP address for ingress packets that match on a VLAN tag, but do not match a more specific inner VLAN tag.Unset field (null-value) indicates both VLAN tags are required to be mapped. Otherwise, defaultApplianceIpAddress is used.  
`l2Forwarding.applianceMappings[].innerVlanToApplianceMappings[]` |  `object` Optional. Used to match against the inner VLAN when the packet contains two VLAN tags.A list of mapping rules from inner VLAN tags to IP addresses. If the inner VLAN is not explicitly mapped to an IP address range, the applianceIpAddress is used.  
`l2Forwarding.applianceMappings[].innerVlanToApplianceMappings[].innerVlanTags[]` |  `string` Required in this object. Used to match the inner VLAN tag on the packet. Each entry can be a single number or a range of numbers in the range of 1 to 4094, e.g., ["1", "4001-4094"] is valid. Non-empty and Non-overlapping VLAN tag ranges are enforced, and violating operations will be rejected.The inner VLAN tags must have an ethertype value of 0x8100.  
`l2Forwarding.applianceMappings[].innerVlanToApplianceMappings[].innerApplianceIpAddress` |  `string` Required in this object. A single IPv4 or IPv6 address used as the destination IP address for ingress packets that match on both VLAN tags.  
`l2Forwarding.network` |  `string` Required. Resource URL of the network to which this attachment belongs. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `network`:

  * `compute.networks.use`

  
`l2Forwarding.geneveHeader` |  `object` Optional. It represents the structure of a Geneve (Generic Network Virtualization Encapsulation) header, as defined in [RFC8926](https://datatracker.ietf.org/doc/html/rfc8926). It encapsulates packets from various protocols (e.g., Ethernet, IPv4, IPv6) for use in network virtualization environments.  
`l2Forwarding.geneveHeader.vni` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Optional. VNI is a 24-bit unique virtual network identifier, from 0 to 16,777,215.  
`l2Forwarding.defaultApplianceIpAddress` |  `string` Optional. A single IPv4 or IPv6 address used as the default destination IP when there is no VLAN mapping result found.Unset field (null-value) indicates the unmatched packet should be dropped.  
`l2Forwarding.tunnelEndpointIpAddress` |  `string` Required. A single IPv4 or IPv6 address. This address will be used as the source IP address for packets sent to the appliances, and must be used as the destination IP address for packets that should be sent out through this attachment.  
`candidateCloudRouterIpAddress` |  `string` Single IPv4 address + prefix length to be configured on the cloud router interface for this interconnect attachment. 

  * Both candidateCloudRouterIpAddress and candidateCustomerRouterIpAddress fields must be set or both must be unset.
  * Prefix length of both candidateCloudRouterIpAddress and candidateCustomerRouterIpAddress must be the same.
  * Max prefix length is 31.

  
`candidateCustomerRouterIpAddress` |  `string` Single IPv4 address + prefix length to be configured on the customer router interface for this interconnect attachment.  
`candidateCloudRouterIpv6Address` |  `string` Single IPv6 address + prefix length to be configured on the cloud router interface for this interconnect attachment. 

  * Both candidateCloudRouterIpv6Address and candidateCustomerRouterIpv6Address fields must be set or both must be unset.
  * Prefix length of both candidateCloudRouterIpv6Address and candidateCustomerRouterIpv6Address must be the same.
  * Max prefix length is 126.

  
`candidateCustomerRouterIpv6Address` |  `string` Single IPv6 address + prefix length to be configured on the customer router interface for this interconnect attachment.  
`params` |  `object` Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload.  
`params.resourceManagerTags` |  `map (key: string, value: string)` Tag keys/values directly bound to this resource. Tag keys and values have the same definition as [resource manager tags](https://cloud.google.com/resource-manager/docs/tags/tags-overview). The field is allowed for INSERT only. The keys/values to set on the resource should be specified in either ID { : } or Namespaced format { : }. For example the following are valid inputs: * {"tagKeys/333" : "tagValues/444", "tagKeys/123" : "tagValues/456"} * {"123/environment" : "production", "345/abc" : "xyz"} Note: * Invalid combinations of ID & namespaced format is not supported. For instance: {"123/environment" : "tagValues/444"} is invalid. * Inconsistent format is not supported. For instance: {"tagKeys/333" : "tagValues/444", "123/env" : "prod"} is invalid.  
  
### Response body

Represents an Operation resource.

Google Compute Engine has three Operation resources:

  * [Global](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalOperations)
  * [Regional](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionOperations)
  * [Zonal](https://docs.cloud.google.com/compute/docs/reference/rest/v1/zoneOperations)



You can use an operation resource to manage asynchronous API requests. For more information, read [Handling API responses](https://docs.cloud.google.com/compute/docs/api/how-tos/api-requests-responses#handling_api_responses).

Operations can be global, regional or zonal. 

  * For global operations, use the `globalOperations` resource.
  * For regional operations, use the `regionOperations` resource.
  * For zonal operations, use the `zoneOperations` resource.



For more information, read [ Global, Regional, and Zonal Resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources).

Note that completed Operation resources have a limited [ retention period.](https://cloud.google.com/compute/docs/instances/viewing-compute-operations#operation-retention-period)

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "zone": string,
      "clientOperationId": string,
      "operationType": string,
      "targetLink": string,
      "targetId": string,
      "status": enum,
      "statusMessage": string,
      "user": string,
      "progress": integer,
      "insertTime": string,
      "startTime": string,
      "endTime": string,
      "error": {
        "errors": [
          {
            "code": string,
            "location": string,
            "message": string,
            "errorDetails": [
              {
                "errorInfo": {
                  "reason": string,
                  "domain": string,
                  "metadatas": {
                    string: string,
                    ...
                  }
                },
                "quotaInfo": {
                  "metricName": string,
                  "limitName": string,
                  "dimensions": {
                    string: string,
                    ...
                  },
                  "limit": number,
                  "futureLimit": number,
                  "rolloutStatus": enum
                },
                "help": {
                  "links": [
                    {
                      "description": string,
                      "url": string
                    }
                  ]
                },
                "localizedMessage": {
                  "locale": string,
                  "message": string
                }
              }
            ]
          }
        ]
      },
      "warnings": [
        {
          "code": enum,
          "message": string,
          "data": [
            {
              "key": string,
              "value": string
            }
          ]
        }
      ],
      "httpErrorStatusCode": integer,
      "httpErrorMessage": string,
      "selfLink": string,
      "region": string,
      "description": string,
      "operationGroupId": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "setCommonInstanceMetadataOperationMetadata": {
        "clientOperationId": string,
        "perLocationOperations": {
          string: {
            "state": enum,
            "error": {
              "code": integer,
              "message": string,
              "details": [
                {
                  "@type": string,
                  field1: ...,
                  ...
                }
              ]
            }
          },
          ...
        }
      },
      "instancesBulkInsertOperationMetadata": {
        "perLocationStatus": {
          string: {
            "status": enum,
            "targetVmCount": integer,
            "createdVmCount": integer,
            "failedToCreateVmCount": integer,
            "deletedVmCount": integer
          },
          ...
        }
      },
      "getVersionOperationMetadata": {
        "inlineSbomInfo": {
          "currentComponentVersions": {
            string: string,
            ...
          },
          "targetComponentVersions": {
            string: string,
            ...
          }
        }
      },
      "getHealthOperationMetadata": {
        "healthInfo": {
          "healthStatus": enum,
          "unhealthyReason": enum,
          "repairCategory": enum,
          "availabilitySloStatus": enum,
          "updateTime": string
        }
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#operation` for Operation resources.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the operation. This identifier is defined by the server.  
`creationTimestamp` |  `string` [Deprecated] This field is deprecated.  
`name` |  `string` Output only. Name of the operation.  
`zone` |  `string` Output only. The URL of the zone where the operation resides. Only applicable when performing per-zone operations.  
`clientOperationId` |  `string` Output only. The value of `requestId` if you provided it in the request. Not present otherwise.  
`operationType` |  `string` Output only. The type of operation, such as `insert`, `update`, or `delete`, and so on.  
`targetLink` |  `string` Output only. The URL of the resource that the operation modifies. For operations related to creating a snapshot, this points to the disk that the snapshot was created from.  
`targetId` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique target ID, which identifies a specific incarnation of the target resource.  
`status` |  `enum` Output only. The status of the operation, which can be one of the following: `PENDING`, `RUNNING`, or `DONE`.  
`statusMessage` |  `string` Output only. An optional textual description of the current status of the operation.  
`user` |  `string` Output only. User who requested the operation, for example: `user@example.com` or `alice_smith_identifier (global/workforcePools/example-com-us-employees)`.  
`progress` |  `integer` Output only. An optional progress indicator that ranges from 0 to 100. There is no requirement that this be linear or support any granularity of operations. This should not be used to guess when the operation will be complete. This number should monotonically increase as the operation progresses.  
`insertTime` |  `string` Output only. The time that this operation was requested. This value is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`startTime` |  `string` Output only. The time that this operation was started by the server. This value is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`endTime` |  `string` Output only. The time that this operation was completed. This value is in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`error` |  `object` Output only. If errors are generated during processing of the operation, this field will be populated.  
`error.errors[]` |  `object` Output only. The array of errors encountered while processing this operation.  
`error.errors[].code` |  `string` Output only. The error type identifier for this error.  
`error.errors[].location` |  `string` Output only. Indicates the field in the request that caused the error. This property is optional.  
`error.errors[].message` |  `string` Output only. An optional, human-readable error message.  
`error.errors[].errorDetails[]` |  `object` Output only. An optional list of messages that contain the error details. There is a set of defined message types to use for providing details.The syntax depends on the error code. For example, QuotaExceededInfo will have details when the error code is QUOTA_EXCEEDED.  
`error.errors[].errorDetails[].errorInfo` |  `object` Error information containing structured domain, reason, and metadata.  
`error.errors[].errorDetails[].errorInfo.reason` |  `string` The reason of the error. This is a constant value that identifies the proximate cause of the error. Error reasons are unique within a particular domain of errors. This should be at most 63 characters and match a regular expression of `[A-Z][A-Z0-9_]+[A-Z0-9]`, which represents UPPER_SNAKE_CASE.  
`error.errors[].errorDetails[].errorInfo.domain` |  `string` The logical grouping to which the "reason" belongs. The error domain is typically the registered service name of the tool or product that generates the error. Example: "pubsub.googleapis.com". If the error is generated by some common infrastructure, the error domain must be a globally unique value that identifies the infrastructure. For Google API infrastructure, the error domain is "googleapis.com".  
`error.errors[].errorDetails[].errorInfo.metadatas` |  `map (key: string, value: string)` Additional structured details about this error.Keys must match a regular expression of `[a-z][a-zA-Z0-9-_]+` but should ideally be lowerCamelCase. Also, they must be limited to 64 characters in length. When identifying the current value of an exceeded limit, the units should be contained in the key, not the value. For example, rather than `{"instanceLimit": "100/request"}`, should be returned as, `{"instanceLimitPerRequest": "100"}`, if the client exceeds the number of instances that can be created in a single (batch) request.  
`error.errors[].errorDetails[].quotaInfo` |  `object` Details about quota limits and metrics when a quota is exceeded.  
`error.errors[].errorDetails[].quotaInfo.metricName` |  `string` The Compute Engine quota metric name.  
`error.errors[].errorDetails[].quotaInfo.limitName` |  `string` The name of the quota limit.  
`error.errors[].errorDetails[].quotaInfo.dimensions` |  `map (key: string, value: string)` The map holding related quota dimensions.  
`error.errors[].errorDetails[].quotaInfo.limit` |  `number` Current effective quota limit. The limit's unit depends on the quota type or metric.  
`error.errors[].errorDetails[].quotaInfo.futureLimit` |  `number` Future quota limit being rolled out. The limit's unit depends on the quota type or metric.  
`error.errors[].errorDetails[].quotaInfo.rolloutStatus` |  `enum` Rollout status of the future quota limit.  
`error.errors[].errorDetails[].help` |  `object` Links and information to help the user resolve the error.  
`error.errors[].errorDetails[].help.links[]` |  `object` URL(s) pointing to additional information on handling the current error.  
`error.errors[].errorDetails[].help.links[].description` |  `string` Describes what the link offers.  
`error.errors[].errorDetails[].help.links[].url` |  `string` The URL of the link.  
`error.errors[].errorDetails[].localizedMessage` |  `object` A localized human-readable error message intended for end users.  
`error.errors[].errorDetails[].localizedMessage.locale` |  `string` The locale used following the specification defined at <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>. Examples are: "en-US", "fr-CH", "es-MX"  
`error.errors[].errorDetails[].localizedMessage.message` |  `string` The localized error message in the above locale.  
`warnings[]` |  `object` Output only. If warning messages are generated during processing of the operation, this field will be populated.  
`warnings[].code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`warnings[].message` |  `string` Output only. A human-readable description of the warning code.  
`warnings[].data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`warnings[].data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`warnings[].data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`httpErrorStatusCode` |  `integer` Output only. If the operation fails, this field contains the HTTP error status code that was returned. For example, a `404` means the resource was not found.  
`httpErrorMessage` |  `string` Output only. If the operation fails, this field contains the HTTP error message that was returned, such as `NOT FOUND`.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`region` |  `string` Output only. The URL of the region where the operation resides. Only applicable when performing regional operations.  
`description` |  `string` Output only. A textual description of the operation, which is set when the operation is created.  
`operationGroupId` |  `string` Output only. An ID that represents a group of operations, such as when a group of operations results from a `bulkInsert` API request.  
Output only. Service-specific metadata attached to this operation. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`setCommonInstanceMetadataOperationMetadata` |  `object` Output only. If the operation is for projects.setCommonInstanceMetadata, this field will contain information on all underlying zonal actions and their state.  
`setCommonInstanceMetadataOperationMetadata.clientOperationId` |  `string` Output only. The client operation id.  
`setCommonInstanceMetadataOperationMetadata.perLocationOperations[]` |  `map (key: string, value: object)` Output only. Status information per location (location name is key). Example key: zones/us-central1-a  
`setCommonInstanceMetadataOperationMetadata.perLocationOperations[].state` |  `enum` Output only. Status of the action, which can be one of the following: `PROPAGATING`, `PROPAGATED`, `ABANDONED`, `FAILED`, or `DONE`.  
`setCommonInstanceMetadataOperationMetadata.perLocationOperations[].error` |  `object` Output only. If state is `ABANDONED` or `FAILED`, this field is populated.  
`setCommonInstanceMetadataOperationMetadata.perLocationOperations[].error.code` |  `integer` The status code, which should be an enum value of `google.rpc.Code`.  
`setCommonInstanceMetadataOperationMetadata.perLocationOperations[].error.message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `google.rpc.Status.details` field, or localized by the client.  
`setCommonInstanceMetadataOperationMetadata.perLocationOperations[].error.details[]` |  `object` A list of messages that carry the error details. There is a common set of message types for APIs to use.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`instancesBulkInsertOperationMetadata` |  `object`  
`instancesBulkInsertOperationMetadata.perLocationStatus[]` |  `map (key: string, value: object)` Status information per location (location name is key). Example key: zones/us-central1-a  
`instancesBulkInsertOperationMetadata.perLocationStatus[].status` |  `enum` Output only. Creation status of BulkInsert operation - information if the flow is rolling forward or rolling back.  
`instancesBulkInsertOperationMetadata.perLocationStatus[].targetVmCount` |  `integer` Output only. Count of VMs originally planned to be created.  
`instancesBulkInsertOperationMetadata.perLocationStatus[].createdVmCount` |  `integer` Output only. Count of VMs successfully created so far.  
`instancesBulkInsertOperationMetadata.perLocationStatus[].failedToCreateVmCount` |  `integer` Output only. Count of VMs that started creating but encountered an error.  
`instancesBulkInsertOperationMetadata.perLocationStatus[].deletedVmCount` |  `integer` Output only. Count of VMs that got deleted during rollback.  
`getVersionOperationMetadata` |  `object`  
`getVersionOperationMetadata.inlineSbomInfo` |  `object`  
`getVersionOperationMetadata.inlineSbomInfo.currentComponentVersions` |  `map (key: string, value: string)` A mapping of components to their currently-applied versions or other appropriate identifiers.  
`getVersionOperationMetadata.inlineSbomInfo.targetComponentVersions` |  `map (key: string, value: string)` A mapping of components to their target versions or other appropriate identifiers.  
`getHealthOperationMetadata` |  `object` Output only. Metadata for GetHealth operations.  
`getHealthOperationMetadata.healthInfo` |  `object` Output only. The health information.  
`getHealthOperationMetadata.healthInfo.healthStatus` |  `enum` Output only. The health status.  
`getHealthOperationMetadata.healthInfo.unhealthyReason` |  `enum` Output only. The reason for unhealthy status.  
`getHealthOperationMetadata.healthInfo.repairCategory` |  `enum` Output only. The repair category.  
`getHealthOperationMetadata.healthInfo.availabilitySloStatus` |  `enum` Output only. The availability SLO status.  
`getHealthOperationMetadata.healthInfo.updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when health info was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
End of mutually exclusive fields.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.interconnectAttachments.create`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
