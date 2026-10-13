---
url: https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/get/
title: Method: routers.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:06:59.865065+00:00
---

# Method: routers.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/v1/routers/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: routers.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
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
  * Authorization scopes
  * IAM Permissions
  * Try it!



Returns the specified Router resource.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/routers/{router}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` Name of the region for this request.  
`router` |  `string` Name of the Router resource to return.  
  
### Request body

The request body must be empty.

### Response body

Represents a Cloud Router resource.

For more information about Cloud Router, read the [Cloud Router overview](https://cloud.google.com/network-connectivity/docs/router/concepts/overview).

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "name": string,
      "description": string,
      "region": string,
      "network": string,
      "nccGateway": string,
      "interfaces": [
        {
          "name": string,
          "linkedVpnTunnel": string,
          "linkedInterconnectAttachment": string,
          "ipRange": string,
          "managementType": enum,
          "privateIpAddress": string,
          "redundantInterface": string,
          "subnetwork": string,
          "ipVersion": enum
        }
      ],
      "bgpPeers": [
        {
          "name": string,
          "interfaceName": string,
          "ipAddress": string,
          "peerIpAddress": string,
          "peerAsn": integer,
          "advertisedRoutePriority": integer,
          "advertiseMode": enum,
          "advertisedGroups": [
            enum
          ],
          "advertisedIpRanges": [
            {
              "range": string,
              "description": string
            }
          ],
          "managementType": enum,
          "enable": enum,
          "bfd": {
            "sessionInitializationMode": enum,
            "minTransmitInterval": integer,
            "minReceiveInterval": integer,
            "multiplier": integer
          },
          "routerApplianceInstance": string,
          "enableIpv6": boolean,
          "ipv6NexthopAddress": string,
          "peerIpv6NexthopAddress": string,
          "md5AuthenticationKeyName": string,
          "customLearnedRoutePriority": integer,
          "customLearnedIpRanges": [
            {
              "range": string
            }
          ],
          "enableIpv4": boolean,
          "ipv4NexthopAddress": string,
          "peerIpv4NexthopAddress": string,
          "exportPolicies": [
            string
          ],
          "importPolicies": [
            string
          ]
        }
      ],
      "bgp": {
        "asn": integer,
        "advertiseMode": enum,
        "advertisedGroups": [
          enum
        ],
        "advertisedIpRanges": [
          {
            "range": string,
            "description": string
          }
        ],
        "keepaliveInterval": integer,
        "identifierRange": string
      },
      "selfLink": string,
      "nats": [
        {
          "name": string,
          "type": enum,
          "autoNetworkTier": enum,
          "endpointTypes": [
            enum
          ],
          "sourceSubnetworkIpRangesToNat": enum,
          "subnetworks": [
            {
              "name": string,
              "sourceIpRangesToNat": [
                enum
              ],
              "secondaryIpRangeNames": [
                string
              ]
            }
          ],
          "sourceSubnetworkIpRangesToNat64": enum,
          "nat64Subnetworks": [
            {
              "name": string
            }
          ],
          "natIps": [
            string
          ],
          "drainNatIps": [
            string
          ],
          "natIpAllocateOption": enum,
          "minPortsPerVm": integer,
          "maxPortsPerVm": integer,
          "enableDynamicPortAllocation": boolean,
          "udpIdleTimeoutSec": integer,
          "icmpIdleTimeoutSec": integer,
          "tcpEstablishedIdleTimeoutSec": integer,
          "tcpTransitoryIdleTimeoutSec": integer,
          "tcpTimeWaitTimeoutSec": integer,
          "effectiveTcpTimeWaitTimeoutSec": integer,
          "logConfig": {
            "enable": boolean,
            "filter": enum
          },
          "rules": [
            {
              "ruleNumber": integer,
              "description": string,
              "match": string,
              "action": {
                "sourceNatActiveIps": [
                  string
                ],
                "sourceNatDrainIps": [
                  string
                ],
                "sourceNatActiveRanges": [
                  string
                ],
                "sourceNatDrainRanges": [
                  string
                ]
              }
            }
          ],
          "enableEndpointIndependentMapping": boolean
        }
      ],
      "encryptedInterconnectRouter": boolean,
      "md5AuthenticationKeys": [
        {
          "name": string,
          "key": string
        }
      ],
      "params": {
        "resourceManagerTags": {
          string: string,
          ...
        }
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of resource. Always `compute#router` for routers.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`region` |  `string` Output only. URI of the region where the router resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.  
`network` |  `string` URI of the network to which this router belongs.  
`nccGateway` |  `string` URI of the nccGateway to which this router associated.  
`interfaces[]` |  `object` Router interfaces. To create a BGP peer that uses a router interface, the interface must have one of the following fields specified: 

  * linkedVpnTunnel
  * linkedInterconnectAttachment
  * subnetwork

You can create a router interface without any of these fields specified. However, you cannot create a BGP peer that uses that interface.   
`interfaces[].name` |  `string` Name of this interface entry. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`interfaces[].linkedVpnTunnel` |  `string` URI of the linked VPN tunnel, which must be in the same region as the router. Each interface can have one linked resource, which can be a VPN tunnel, an Interconnect attachment, or a subnetwork.  
`interfaces[].linkedInterconnectAttachment` |  `string` URI of the linked Interconnect attachment. It must be in the same region as the router. Each interface can have one linked resource, which can be a VPN tunnel, an Interconnect attachment, or a subnetwork.  
`interfaces[].ipRange` |  `string` IP address and range of the interface. 

  * For Internet Protocol version 4 (IPv4), the IP range must be in the [RFC3927](https://www.ietf.org/rfc/rfc3927.txt) link-local IP address space. The value must be a CIDR-formatted string, for example, `169.254.0.1/30`. Note: Do not truncate the IP address, as it represents the IP address of the interface.
  * For Internet Protocol version 6 (IPv6), the value must be a unique local address (ULA) range from `fdff:1::/64` with a mask length of 126 or less. This value should be a CIDR-formatted string, for example, `fdff:1::1/112`. Within the router's VPC, this IPv6 prefix will be reserved exclusively for this connection and cannot be used for any other purpose.

  
`interfaces[].managementType` |  `enum` Output only. The resource that configures and manages this interface. 

  * MANAGED_BY_USER is the default value and can be managed directly by users.
  * MANAGED_BY_ATTACHMENT is an interface that is configured and managed by Cloud Interconnect, specifically, by an InterconnectAttachment of type PARTNER. Google automatically creates, updates, and deletes this type of interface when the PARTNER InterconnectAttachment is created, updated, or deleted.

  
`interfaces[].privateIpAddress` |  `string` The regional private internal IP address that is used to establish BGP sessions to a VM instance acting as a third-party Router Appliance, such as a Next Gen Firewall, a Virtual Router, or an SD-WAN VM.  
`interfaces[].redundantInterface` |  `string` Name of the interface that will be redundant with the current interface you are creating. The redundantInterface must belong to the same Cloud Router as the interface here. To establish the BGP session to a Router Appliance VM, you must create two BGP peers. The two BGP peers must be attached to two separate interfaces that are redundant with each other. The redundantInterface must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the redundantInterface must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`interfaces[].subnetwork` |  `string` The URI of the subnetwork resource that this interface belongs to, which must be in the same region as the Cloud Router. When you establish a BGP session to a VM instance using this interface, the VM instance must belong to the same subnetwork as the subnetwork specified here.  
`interfaces[].ipVersion` |  `enum` IP version of this interface.  
`bgpPeers[]` |  `object` BGP information that must be configured into the routing stack to establish BGP peering. This information must specify the peer ASN and either the interface name, IP address, or peer IP address. Please refer to [RFC4273](https://tools.ietf.org/html/rfc4273).  
`bgpPeers[].name` |  `string` Name of this BGP peer. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`bgpPeers[].interfaceName` |  `string` Name of the interface the BGP peer is associated with.  
`bgpPeers[].ipAddress` |  `string` IP address of the interface inside Google Cloud Platform.  
`bgpPeers[].peerIpAddress` |  `string` IP address of the BGP interface outside Google Cloud Platform.  
`bgpPeers[].peerAsn` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Peer BGP Autonomous System Number (ASN). Each BGP interface may use a different value.  
`bgpPeers[].advertisedRoutePriority` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The priority of routes advertised to this BGP peer. Where there is more than one matching route of maximum length, the routes with the lowest priority value win.  
`bgpPeers[].advertiseMode` |  `enum` User-specified flag to indicate which mode to use for advertisement.  
`bgpPeers[].advertisedGroups[]` |  `enum` User-specified list of prefix groups to advertise in custom mode, which currently supports the following option: 

  * ALL_SUBNETS: Advertises all of the router's own VPC subnets. This excludes any routes learned for subnets that use VPC Network Peering.

Note that this field can only be populated if advertiseMode is CUSTOM and overrides the list defined for the router (in the "bgp" message). These groups are advertised in addition to any specified prefixes. Leave this field blank to advertise no custom groups.   
`bgpPeers[].advertisedIpRanges[]` |  `object` User-specified list of individual IP ranges to advertise in custom mode. This field can only be populated if advertiseMode is CUSTOM and overrides the list defined for the router (in the "bgp" message). These IP ranges are advertised in addition to any specified groups. Leave this field blank to advertise no custom IP ranges.  
`bgpPeers[].advertisedIpRanges[].range` |  `string` The IP range to advertise. The value must be a CIDR-formatted string.  
`bgpPeers[].advertisedIpRanges[].description` |  `string` User-specified description for the IP range.  
`bgpPeers[].managementType` |  `enum` Output only. The resource that configures and manages this BGP peer. 

  * MANAGED_BY_USER is the default value and can be managed by you or other users
  * MANAGED_BY_ATTACHMENT is a BGP peer that is configured and managed by Cloud Interconnect, specifically by an InterconnectAttachment of type PARTNER. Google automatically creates, updates, and deletes this type of BGP peer when the PARTNER InterconnectAttachment is created, updated, or deleted.

  
`bgpPeers[].enable` |  `enum` The status of the BGP peer connection.  If set to FALSE, any active session with the peer is terminated and all associated routing information is removed. If set to TRUE, the peer connection can be established with routing information. The default is TRUE.  
`bgpPeers[].bfd` |  `object` BFD configuration for the BGP peering.  
`bgpPeers[].bfd.sessionInitializationMode` |  `enum` The BFD session initialization mode for this BGP peer.  If set to ACTIVE, the Cloud Router will initiate the BFD session for this BGP peer. If set to PASSIVE, the Cloud Router will wait for the peer router to initiate the BFD session for this BGP peer. If set to DISABLED, BFD is disabled for this BGP peer. The default is DISABLED.  
`bgpPeers[].bfd.minTransmitInterval` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The minimum interval, in milliseconds, between BFD control packets transmitted to the peer router. The actual value is negotiated between the two routers and is equal to the greater of this value and the corresponding receive interval of the other router.  If set, this value must be between 1000 and 30000.  The default is 1000.  
`bgpPeers[].bfd.minReceiveInterval` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The minimum interval, in milliseconds, between BFD control packets received from the peer router. The actual value is negotiated between the two routers and is equal to the greater of this value and the transmit interval of the other router.  If set, this value must be between 1000 and 30000.  The default is 1000.  
`bgpPeers[].bfd.multiplier` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The number of consecutive BFD packets that must be missed before BFD declares that a peer is unavailable.  If set, the value must be a value between 5 and 16.  The default is 5.  
`bgpPeers[].routerApplianceInstance` |  `string` URI of the VM instance that is used as third-party router appliances such as Next Gen Firewalls, Virtual Routers, or Router Appliances. The VM instance must be located in zones contained in the same region as this Cloud Router. The VM instance is the peer side of the BGP session.  
`bgpPeers[].enableIpv6` |  `boolean` Enable IPv6 traffic over BGP Peer. It is enabled by default if the peerIpAddress is version 6.  
`bgpPeers[].ipv6NexthopAddress` |  `string` IPv6 address of the interface inside Google Cloud Platform.  
`bgpPeers[].peerIpv6NexthopAddress` |  `string` IPv6 address of the BGP interface outside Google Cloud Platform.  
`bgpPeers[].md5AuthenticationKeyName` |  `string` Present if MD5 authentication is enabled for the peering. Must be the name of one of the entries in the Router.md5_authentication_keys. The field must comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).  
`bgpPeers[].customLearnedRoutePriority` |  `integer` The user-defined custom learned route priority for a BGP session. This value is applied to all custom learned route ranges for the session. You can choose a value from `0` to `65335`. If you don't provide a value, Google Cloud assigns a priority of `100` to the ranges.  
`bgpPeers[].customLearnedIpRanges[]` |  `object` A list of user-defined custom learned route IP address ranges for a BGP session.  
`bgpPeers[].customLearnedIpRanges[].range` |  `string` The custom learned route IP address range. Must be a valid CIDR-formatted prefix. If an IP address is provided without a subnet mask, it is interpreted as, for IPv4, a `/32` singular IP address range, and, for IPv6, `/128`.  
`bgpPeers[].enableIpv4` |  `boolean` Enable IPv4 traffic over BGP Peer. It is enabled by default if the peerIpAddress is version 4.  
`bgpPeers[].ipv4NexthopAddress` |  `string` IPv4 address of the interface inside Google Cloud Platform.  
`bgpPeers[].peerIpv4NexthopAddress` |  `string` IPv4 address of the BGP interface outside Google Cloud Platform.  
`bgpPeers[].exportPolicies[]` |  `string` routers.list of export policies applied to this peer, in the order they must be evaluated. The name must correspond to an existing policy that has ROUTE_POLICY_TYPE_EXPORT type.  
`bgpPeers[].importPolicies[]` |  `string` routers.list of import policies applied to this peer, in the order they must be evaluated. The name must correspond to an existing policy that has ROUTE_POLICY_TYPE_IMPORT type.  
`bgp` |  `object` BGP information specific to this router.  
`bgp.asn` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` Local BGP Autonomous System Number (ASN). Must be an [RFC6996](https://www.ietf.org/rfc/rfc6996.txt) private ASN, either 16-bit or 32-bit. The value will be fixed for this router resource. All VPN tunnels that link to this router will have the same local ASN.  
`bgp.advertiseMode` |  `enum` User-specified flag to indicate which mode to use for advertisement. The options are DEFAULT or CUSTOM.  
`bgp.advertisedGroups[]` |  `enum` User-specified list of prefix groups to advertise in custom mode. This field can only be populated if advertiseMode is CUSTOM and is advertised to all peers of the router. These groups will be advertised in addition to any specified prefixes. Leave this field blank to advertise no custom groups.  
`bgp.advertisedIpRanges[]` |  `object` User-specified list of individual IP ranges to advertise in custom mode. This field can only be populated if advertiseMode is CUSTOM and is advertised to all peers of the router. These IP ranges will be advertised in addition to any specified groups. Leave this field blank to advertise no custom IP ranges.  
`bgp.advertisedIpRanges[].range` |  `string` The IP range to advertise. The value must be a CIDR-formatted string.  
`bgp.advertisedIpRanges[].description` |  `string` User-specified description for the IP range.  
`bgp.keepaliveInterval` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The interval in seconds between BGP keepalive messages that are sent to the peer.  Hold time is three times the interval at which keepalive messages are sent, and the hold time is the maximum number of seconds allowed to elapse between successive keepalive messages that BGP receives from a peer.  BGP will use the smaller of either the local hold time value or the peer's hold time value as the hold time for the BGP connection between the two peers.  If set, this value must be between 20 and 60. The default is 20.  
`bgp.identifierRange` |  `string` Explicitly specifies a range of valid BGP Identifiers for this Router. It is provided as a link-local IPv4 range (from 169.254.0.0/16), of size at least /30, even if the BGP sessions are over IPv6. It must not overlap with any IPv4 BGP session ranges.  Other vendors commonly call this "router ID".  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`nats[]` |  `object` A list of NAT services created in this router.  
`nats[].name` |  `string` Unique name of this Nat service. The name must be 1-63 characters long and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).  
`nats[].type` |  `enum` Indicates whether this NAT is used for public or private IP translation. If unspecified, it defaults to PUBLIC.  
`nats[].autoNetworkTier` |  `enum` The network tier to use when automatically reserving NAT IP addresses. Must be one of: PREMIUM, STANDARD. If not specified, then the current [ project-level default tier](https://cloud.google.com/network-tiers/docs/set-network-tier#setting_the_tier_for_all_resources_in_a_project) is used.  
`nats[].endpointTypes[]` |  `enum` routers.list of NAT-ted endpoint types supported by the Nat Gateway. If the list is empty, then it will be equivalent to include ENDPOINT_TYPE_VM  
`nats[].sourceSubnetworkIpRangesToNat` |  `enum` Specify the Nat option, which can take one of the following values: 

  * ALL_SUBNETWORKS_ALL_IP_RANGES: All of the IP ranges in every Subnetwork are allowed to Nat.
  * ALL_SUBNETWORKS_ALL_PRIMARY_IP_RANGES: All of the primary IP ranges in every Subnetwork are allowed to Nat.
  * LIST_OF_SUBNETWORKS: A list of Subnetworks are allowed to Nat (specified in the field subnetwork below)

The default is SUBNETWORK_IP_RANGE_TO_NAT_OPTION_UNSPECIFIED. Note that if this field contains ALL_SUBNETWORKS_ALL_IP_RANGES then there should not be any other Router.Nat section in any Router for this network in this region.   
`nats[].subnetworks[]` |  `object` A list of Subnetwork resources whose traffic should be translated by NAT Gateway. It is used only when LIST_OF_SUBNETWORKS is selected for the SubnetworkIpRangeToNatOption above.  
`nats[].subnetworks[].name` |  `string` URL for the subnetwork resource that will use NAT.  
`nats[].subnetworks[].sourceIpRangesToNat[]` |  `enum` Specify the options for NAT ranges in the Subnetwork. All options of a single value are valid except NAT_IP_RANGE_OPTION_UNSPECIFIED. The only valid option with multiple values is: ["PRIMARY_IP_RANGE", "LIST_OF_SECONDARY_IP_RANGES"] Default: [ALL_IP_RANGES]  
`nats[].subnetworks[].secondaryIpRangeNames[]` |  `string` A list of the secondary ranges of the Subnetwork that are allowed to use NAT. This can be populated only if "LIST_OF_SECONDARY_IP_RANGES" is one of the values in sourceIpRangesToNat.  
`nats[].sourceSubnetworkIpRangesToNat64` |  `enum` Specify the Nat option for NAT64, which can take one of the following values: 

  * ALL_IPV6_SUBNETWORKS: All of the IP ranges in every Subnetwork are allowed to Nat.
  * LIST_OF_IPV6_SUBNETWORKS: A list of Subnetworks are allowed to Nat (specified in the field nat64Subnetwork below)

The default is NAT64_OPTION_UNSPECIFIED. Note that if this field contains NAT64_ALL_V6_SUBNETWORKS no other Router.Nat section in this region can also enable NAT64 for any Subnetworks in this network. Other Router.Nat sections can still be present to enable NAT44 only.   
`nats[].nat64Subnetworks[]` |  `object` routers.list of Subnetwork resources whose traffic should be translated by NAT64 Gateway. It is used only when LIST_OF_IPV6_SUBNETWORKS is selected for the SubnetworkIpRangeToNat64Option above.  
`nats[].nat64Subnetworks[].name` |  `string` URL for the subnetwork resource that will use NAT64.  
`nats[].natIps[]` |  `string` A list of URLs of the IP resources used for this Nat service. These IP addresses must be valid static external IP addresses assigned to the project.  
`nats[].drainNatIps[]` |  `string` A list of URLs of the IP resources to be drained. These IPs must be valid static external IPs that have been assigned to the NAT. These IPs should be used for updating/patching a NAT only.  
`nats[].natIpAllocateOption` |  `enum` Specify the NatIpAllocateOption, which can take one of the following values: 

  * MANUAL_ONLY: Uses only Nat IP addresses provided by customers. When there are not enough specified Nat IPs, the Nat service fails for new VMs.
  * AUTO_ONLY: Nat IPs are allocated by Google Cloud Platform; customers can't specify any Nat IPs. When choosing AUTO_ONLY, then natIp should be empty.

  
`nats[].minPortsPerVm` |  `integer` Minimum number of ports allocated to a VM from this NAT config. If not set, a default number of ports is allocated to a VM. This is rounded up to the nearest power of 2. For example, if the value of this field is 50, at least 64 ports are allocated to a VM.  
`nats[].maxPortsPerVm` |  `integer` Maximum number of ports allocated to a VM from this NAT config when Dynamic Port Allocation is enabled.  If Dynamic Port Allocation is not enabled, this field has no effect.  If Dynamic Port Allocation is enabled, and this field is set, it must be set to a power of two greater than minPortsPerVm, or 64 if minPortsPerVm is not set.  If Dynamic Port Allocation is enabled and this field is not set, a maximum of 65536 ports will be allocated to a VM from this NAT config.  
`nats[].enableDynamicPortAllocation` |  `boolean` Enable Dynamic Port Allocation.  If not specified, it is disabled by default.  If set to true, 

  * Dynamic Port Allocation will be enabled on this NAT config.
  * enableEndpointIndependentMapping cannot be set to true.
  * If minPorts is set, minPortsPerVm must be set to a power of two greater than or equal to 32. If minPortsPerVm is not set, a minimum of 32 ports will be allocated to a VM from this NAT config.

  
`nats[].udpIdleTimeoutSec` |  `integer` Timeout (in seconds) for UDP connections. Defaults to 30s if not set.  
`nats[].icmpIdleTimeoutSec` |  `integer` Timeout (in seconds) for ICMP connections. Defaults to 30s if not set.  
`nats[].tcpEstablishedIdleTimeoutSec` |  `integer` Timeout (in seconds) for TCP established connections. Defaults to 1200s if not set.  
`nats[].tcpTransitoryIdleTimeoutSec` |  `integer` Timeout (in seconds) for TCP transitory connections. Defaults to 30s if not set.  
`nats[].tcpTimeWaitTimeoutSec` |  `integer` Timeout (in seconds) for TCP connections that are in TIME_WAIT state. Defaults to 120s if not set.  
`nats[].effectiveTcpTimeWaitTimeoutSec` |  `integer` Output only. Effective timeout (in seconds) for TCP connections that are in TIME_WAIT state. This value is equal to tcpTimeWaitTimeoutSec. If tcpTimeWaitTimeoutSec isn't set, the effective timeout is 30s or 120s. The field is output only.  
`nats[].logConfig` |  `object` Configure logging on this NAT.  
`nats[].logConfig.enable` |  `boolean` Indicates whether or not to export logs. This is false by default.  
`nats[].logConfig.filter` |  `enum` Specify the desired filtering of logs on this NAT. If unspecified, logs are exported for all connections handled by this NAT. This option can take one of the following values: 

  * ERRORS_ONLY: Export logs only for connection failures.
  * TRANSLATIONS_ONLY: Export logs only for successful connections.
  * ALL: Export logs for all connections, successful and unsuccessful.

  
`nats[].rules[]` |  `object` A list of rules associated with this NAT.  
`nats[].rules[].ruleNumber` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` An integer uniquely identifying a rule in the list. The rule number must be a positive value between 0 and 65000, and must be unique among rules within a NAT.  
`nats[].rules[].description` |  `string` An optional description of this rule.  
`nats[].rules[].match` |  `string` CEL expression that specifies the match condition that egress traffic from a VM is evaluated against. If it evaluates to true, the corresponding `action` is enforced.The following examples are valid match expressions for public NAT:`inIpRange(destination.ip, '1.1.0.0/16') || inIpRange(destination.ip, '2.2.0.0/16')``destination.ip == '1.1.0.1' || destination.ip == '8.8.8.8'`The following example is a valid match expression for private NAT:`nexthop.hub == '//networkconnectivity.googleapis.com/projects/my-project/locations/global/hubs/hub-1'`  
`nats[].rules[].action` |  `object` The action to be enforced for traffic that matches this rule.  
`nats[].rules[].action.sourceNatActiveIps[]` |  `string` A list of URLs of the IP resources used for this NAT rule. These IP addresses must be valid static external IP addresses assigned to the project. This field is used for public NAT.  
`nats[].rules[].action.sourceNatDrainIps[]` |  `string` A list of URLs of the IP resources to be drained. These IPs must be valid static external IPs that have been assigned to the NAT. These IPs should be used for updating/patching a NAT rule only. This field is used for public NAT.  
`nats[].rules[].action.sourceNatActiveRanges[]` |  `string` A list of URLs of the subnetworks used as source ranges for this NAT Rule. These subnetworks must have purpose set to PRIVATE_NAT. This field is used for private NAT.  
`nats[].rules[].action.sourceNatDrainRanges[]` |  `string` A list of URLs of subnetworks representing source ranges to be drained. This is only supported on patch/update, and these subnetworks must have previously been used as active ranges in this NAT Rule. This field is used for private NAT.  
`nats[].enableEndpointIndependentMapping` |  `boolean`  
`encryptedInterconnectRouter` |  `boolean` Indicates if a router is dedicated for use with encrypted VLAN attachments (interconnectAttachments).  
`md5AuthenticationKeys[]` |  `object` Keys used for MD5 authentication.  
`md5AuthenticationKeys[].name` |  `string` Name used to identify the key.Must be unique within a router. Must be referenced by exactly one bgpPeer. Must comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).  
`md5AuthenticationKeys[].key` |  `string` [Input only] Value of the key.For patch and update calls, it can be skipped to copy the value from the previous configuration. This is allowed if the key with the same name existed before the operation. Maximum length is 80 characters. Can only contain printable ASCII characters.  
`params` |  `object` Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload.  
`params.resourceManagerTags` |  `map (key: string, value: string)` Tag keys/values directly bound to this resource. The field is allowed for INSERT only. The keys/values to set on the resource should be specified in either ID { : } or Namespaced format { : }. For example the following are valid inputs: * {"tagKeys/333" : "tagValues/444", "tagKeys/123" : "tagValues/456"} * {"123/environment" : "production", "345/abc" : "xyz"} Note: * Invalid combinations of ID & namespaced format is not supported. For instance: {"123/environment" : "tagValues/444"} is invalid. * Inconsistent format is not supported. For instance: {"tagKeys/333" : "tagValues/444", "123/env" : "prod"} is invalid.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.routers.get`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
