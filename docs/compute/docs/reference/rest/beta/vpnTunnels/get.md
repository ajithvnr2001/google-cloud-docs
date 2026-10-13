---
url: https://docs.cloud.google.com/compute/docs/reference/rest/beta/vpnTunnels/get/
title: Method: vpnTunnels.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:37.168662+00:00
---

# Method: vpnTunnels.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/beta/vpnTunnels/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: vpnTunnels.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Returns the specified VpnTunnel resource.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/beta/projects/{project}/regions/{region}/vpnTunnels/{vpnTunnel}`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` Name of the region for this request.  
`vpnTunnel` |  `string` Name of the VpnTunnel resource to return.  
  
### Request body

The request body must be empty.

### Response body

Represents a Cloud VPN Tunnel resource.

For more information about VPN, read the [ the Cloud VPN Overview](https://cloud.google.com/network-connectivity/docs/vpn/concepts/overview).

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
      "targetVpnGateway": string,
      "vpnGateway": string,
      "vpnGatewayInterface": integer,
      "peerExternalGateway": string,
      "peerExternalGatewayInterface": integer,
      "peerGcpGateway": string,
      "router": string,
      "peerIp": string,
      "sharedSecret": string,
      "sharedSecretHash": string,
      "status": enum,
      "selfLink": string,
      "ikeVersion": integer,
      "detailedStatus": string,
      "localTrafficSelector": [
        string
      ],
      "remoteTrafficSelector": [
        string
      ],
      "labels": {
        string: string,
        ...
      },
      "labelFingerprint": string,
      "cipherSuite": {
        "phase1": {
          "encryption": [
            string
          ],
          "integrity": [
            string
          ],
          "prf": [
            string
          ],
          "dh": [
            string
          ]
        },
        "phase2": {
          "encryption": [
            string
          ],
          "integrity": [
            string
          ],
          "pfs": [
            string
          ]
        }
      },
      "params": {
        "resourceManagerTags": {
          string: string,
          ...
        }
      },
      "capacityTier": enum
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of resource. Always `compute#vpnTunnel` for VPN tunnels.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`region` |  `string` Output only. URL of the region where the VPN tunnel resides. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.  
`targetVpnGateway` |  `string` URL of the Target VPN gateway with which this VPN tunnel is associated. Provided by the client when the VPN tunnel is created. This field can be set only for Classic VPN tunnels.  
`vpnGateway` |  `string` URL of the VPN gateway with which this VPN tunnel is associated. Provided by the client when the VPN tunnel is created. This must be used (instead of targetVpnGateway) if a High Availability VPN gateway resource is created.  
`vpnGatewayInterface` |  `integer` The interface ID of the VPN gateway with which this VPN tunnel is associated. Possible values are: `0`, `1`.  
`peerExternalGateway` |  `string` URL of the peer side external VPN gateway to which this VPN tunnel is connected. Provided by the client when the VPN tunnel is created. This field is exclusive with the field peerGcpGateway.  
`peerExternalGatewayInterface` |  `integer` The interface ID of the external VPN gateway to which this VPN tunnel is connected. Provided by the client when the VPN tunnel is created. Possible values are: `0`, `1`, `2`, `3`. The number of IDs in use depends on the external VPN gateway redundancy type.  
`peerGcpGateway` |  `string` URL of the peer side HA VPN gateway to which this VPN tunnel is connected. Provided by the client when the VPN tunnel is created. This field can be used when creating highly available VPN from VPC network to VPC network, the field is exclusive with the field peerExternalGateway. If provided, the VPN tunnel will automatically use the same vpnGatewayInterface ID in the peer Google Cloud VPN gateway.  
`router` |  `string` URL of the router resource to be used for dynamic routing.  
`peerIp` |  `string` IP address of the peer VPN gateway. Only IPv4 is supported. This field can be set only for Classic VPN tunnels.  
`sharedSecret` |  `string` Shared secret used to set the secure session between the Cloud VPN gateway and the peer VPN gateway.  
`sharedSecretHash` |  `string` Hash of the shared secret.  
`status` |  `enum` Output only. The status of the VPN tunnel, which can be one of the following: 

  * PROVISIONING: Resource is being allocated for the VPN tunnel.
  * WAITING_FOR_FULL_CONFIG: Waiting to receive all VPN-related configs from the user. Network, TargetVpnGateway, VpnTunnel, ForwardingRule, and Route resources are needed to setup the VPN tunnel.
  * FIRST_HANDSHAKE: Successful first handshake with the peer VPN.
  * ESTABLISHED: Secure session is successfully established with the peer VPN.
  * NETWORK_ERROR: Deprecated, replaced by NO_INCOMING_PACKETS
  * AUTHORIZATION_ERROR: Auth error (for example, bad shared secret).
  * NEGOTIATION_FAILURE: Handshake failed.
  * DEPROVISIONING: Resources are being deallocated for the VPN tunnel.
  * FAILED: Tunnel creation has failed and the tunnel is not ready to be used.
  * NO_INCOMING_PACKETS: No incoming packets from peer.
  * REJECTED: Tunnel configuration was rejected, can be result of being denied access.
  * ALLOCATING_RESOURCES: Cloud VPN is in the process of allocating all required resources.
  * STOPPED: Tunnel is stopped due to its Forwarding Rules being deleted for Classic VPN tunnels or the project is in frozen state.
  * PEER_IDENTITY_MISMATCH: Peer identity does not match peer IP, probably behind NAT.
  * TS_NARROWING_NOT_ALLOWED: Traffic selector narrowing not allowed for an HA-VPN tunnel.

  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`ikeVersion` |  `integer` IKE protocol version to use when establishing the VPN tunnel with the peer VPN gateway. Acceptable IKE versions are `1` or `2`. The default version is `2`.  
`detailedStatus` |  `string` Output only. Detailed status message for the VPN tunnel.  
`localTrafficSelector[]` |  `string` Local traffic selector to use when establishing the VPN tunnel with the peer VPN gateway. The value should be a CIDR formatted string, for example: `192.168.0.0/16`. The ranges must be disjoint. Only IPv4 is supported for Classic VPN tunnels. This field is output only for HA VPN tunnels.  
`remoteTrafficSelector[]` |  `string` Remote traffic selectors to use when establishing the VPN tunnel with the peer VPN gateway. The value should be a CIDR formatted string, for example: 192.168.0.0/16. The ranges should be disjoint. Only IPv4 is supported for Classic VPN tunnels. This field is output only for HA VPN tunnels.  
`labels` |  `map (key: string, value: string)` Labels for this resource. These can only be added or modified by the `setLabels` method. Each label key/value pair must comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Label values may be empty.  
`labelFingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` A fingerprint for the labels being applied to this VpnTunnel, which is essentially a hash of the labels set used for optimistic locking. The fingerprint is initially generated by Compute Engine and changes after every request to modify or update labels. You must always provide an up-to-date fingerprint hash in order to update or change labels, otherwise the request will fail with error `412 conditionNotMet`.To see the latest fingerprint, make a `get()` request to retrieve a VpnTunnel.A base64-encoded string.  
`cipherSuite` |  `object` User specified list of ciphers to use for the phase 1 and phase 2 of the IKE protocol.  
`cipherSuite.phase1` |  `object`  
`cipherSuite.phase1.encryption[]` |  `string`  
`cipherSuite.phase1.integrity[]` |  `string`  
`cipherSuite.phase1.prf[]` |  `string`  
`cipherSuite.phase1.dh[]` |  `string`  
`cipherSuite.phase2` |  `object`  
`cipherSuite.phase2.encryption[]` |  `string`  
`cipherSuite.phase2.integrity[]` |  `string`  
`cipherSuite.phase2.pfs[]` |  `string`  
`params` |  `object` Input only. [Input Only] Additional params passed with the request, but not persisted as part of resource payload.  
`params.resourceManagerTags` |  `map (key: string, value: string)` Tag keys/values directly bound to this resource. Tag keys and values have the same definition as resource manager tags. The field is allowed for INSERT only. The keys/values to set on the resource should be specified in either ID { : } or Namespaced format { : }. For example the following are valid inputs: * {"tagKeys/333" : "tagValues/444", "tagKeys/123" : "tagValues/456"} * {"123/environment" : "production", "345/abc" : "xyz"} Note: * Invalid combinations of ID & namespaced format is not supported. For instance: {"123/environment" : "tagValues/444"} is invalid. * Inconsistent format is not supported. For instance: {"tagKeys/333" : "tagValues/444", "123/env" : "prod"} is invalid.  
`capacityTier` |  `enum` Capacity tier of the VPN tunnel. This is used for IPsec over Interconnect tunnels to indicate different bandwidth limits.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.vpnTunnels.get`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
