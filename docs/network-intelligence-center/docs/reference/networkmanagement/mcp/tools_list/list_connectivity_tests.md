---
url: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/list_connectivity_tests/
title: MCP Tools Reference: networkmanagement.googleapis.com \u00a0|\u00a0 Network Intelligence Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:22:46.870783+00:00
---

# MCP Tools Reference: networkmanagement.googleapis.com  |  Network Intelligence Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/list_connectivity_tests/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Reference ](https://docs.cloud.google.com/network-intelligence-center/docs/apis)



Send feedback 

#  MCP Tools Reference: networkmanagement.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_connectivity_tests`

Lists all Connectivity Tests owned by a project.

The following sample demonstrate how to use `curl` to invoke the `list_connectivity_tests` MCP tool. 

Curl Request  
---  
      
    
                      
    curl --location 'https://networkmanagement.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_connectivity_tests",
        "arguments": {
          // provide these details according to the tool's MCP specification
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'
                      
  
## Input Schema

Request for the `ListConnectivityTests` method.

### ListConnectivityTestsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string,
      "filter": string,
      "orderBy": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The parent resource of the Connectivity Tests: `projects/{project_id}/locations/global`  
`pageSize` |  `integer` Number of `ConnectivityTests` to return.  
`pageToken` |  `string` Page token from an earlier query, as returned in `next_page_token`.  
`filter` |  `string` Lists the `ConnectivityTests` that match the filter expression. A filter expression filters the resources listed in the response. The expression must be of the form `<field> <operator> <value>` where operators: `<`, `>`, `<=`, `>=`, `!=`, `=`, `:` are supported (colon `:` represents a HAS operator which is roughly synonymous with equality).  can refer to a proto or JSON field, or a synthetic field. Field names can be camelCase or snake_case.Examples: - Filter by name: name = "projects/proj-1/locations/global/connectivityTests/test-1

  * Filter by labels:
  * Resources that have a key called `foo` labels.foo:*
  * Resources that have a key called `foo` whose value is `bar` labels.foo = bar

  
`orderBy` |  `string` Field to use to sort the list.  
  
## Output Schema

Response for the `ListConnectivityTests` method.

### ListConnectivityTestsResponse

JSON representation  
---  
      
    
    {
      "resources": [
        {
          object ([ConnectivityTest](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.ConnectivityTest))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`resources[]` |  `object (`[ConnectivityTest](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.ConnectivityTest)`)` List of Connectivity Tests.  
`nextPageToken` |  `string` Page token to fetch the next set of Connectivity Tests.  
`unreachable[]` |  `string` Locations that could not be reached (when querying all locations with `-`).  
  
### ConnectivityTest

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "source": {
        object ([Endpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.Endpoint))
      },
      "destination": {
        object ([Endpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.Endpoint))
      },
      "protocol": string,
      "relatedProjects": [
        string
      ],
      "displayName": string,
      "labels": {
        string: string,
        ...
      },
      "createTime": string,
      "updateTime": string,
      "reachabilityDetails": {
        object ([ReachabilityDetails](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.ReachabilityDetails))
      },
      "probingDetails": {
        object ([ProbingDetails](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.ProbingDetails))
      },
      "roundTrip": boolean,
      "returnReachabilityDetails": {
        object ([ReachabilityDetails](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.ReachabilityDetails))
      },
      "bypassFirewallChecks": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. Unique name of the resource using the form: `projects/{project_id}/locations/global/connectivityTests/{test_id}`  
`description` |  `string` The user-supplied description of the Connectivity Test. Maximum of 512 characters.  
`source` |  `object (`[Endpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.Endpoint)`)` Required. Source specification of the Connectivity Test.You can use a combination of source IP address, URI of a supported endpoint, project ID, or VPC network to identify the source location.Reachability analysis might proceed even if the source location is ambiguous. However, the test result might include endpoints or use a source that you don't intend to test.  
`destination` |  `object (`[Endpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.Endpoint)`)` Required. Destination specification of the Connectivity Test.You can use a combination of destination IP address, URI of a supported endpoint, project ID, or VPC network to identify the destination location.Reachability analysis proceeds even if the destination location is ambiguous. However, the test result might include endpoints or use a destination that you don't intend to test.  
`protocol` |  `string` IP Protocol of the test. When not provided, "TCP" is assumed.  
`relatedProjects[]` |  `string` Other projects that may be relevant for reachability analysis. This is applicable to scenarios where a test can cross project boundaries.  
`displayName` |  `string` Output only. The display name of a Connectivity Test.  
`labels` |  `map (key: string, value: string)` Resource labels to represent user-provided metadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the test was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the test's configuration was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`reachabilityDetails` |  `object (`[ReachabilityDetails](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.ReachabilityDetails)`)` Output only. The reachability details of this test from the latest run. The details are updated when creating a new test, updating an existing test, or triggering a one-time rerun of an existing test.  
`probingDetails` |  `object (`[ProbingDetails](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.ProbingDetails)`)` Output only. The probing details of this test from the latest run, present for applicable tests only. The details are updated when creating a new test, updating an existing test, or triggering a one-time rerun of an existing test.  
`roundTrip` |  `boolean` Whether run analysis for the return path from destination to source. Default value is false.  
`returnReachabilityDetails` |  `object (`[ReachabilityDetails](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.ReachabilityDetails)`)` Output only. The reachability details of this test from the latest run for the return path. The details are updated when creating a new test, updating an existing test, or triggering a one-time rerun of an existing test.  
`bypassFirewallChecks` |  `boolean` Whether the analysis should skip firewall checking. Default value is false.  
  
### Endpoint

JSON representation  
---  
      
    
    {
      "ipAddress": string,
      "port": integer,
      "instance": string,
      "forwardingRule": string,
      "gkeMasterCluster": string,
      "fqdn": string,
      "cloudSqlInstance": string,
      "redisInstance": string,
      "redisCluster": string,
      "gkePod": string,
      "cloudFunction": {
        object ([CloudFunctionEndpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.CloudFunctionEndpoint))
      },
      "appEngineVersion": {
        object ([AppEngineVersionEndpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.AppEngineVersionEndpoint))
      },
      "cloudRunRevision": {
        object ([CloudRunRevisionEndpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.CloudRunRevisionEndpoint))
      },
      "network": string,
      "networkType": enum (NetworkType),
      "projectId": string,
    
      // Union field _forwarding_rule_target can be only one of the following:
      "forwardingRuleTarget": enum (ForwardingRuleTarget)
      // End of list of possible types for union field _forwarding_rule_target.
    
      // Union field _load_balancer_id can be only one of the following:
      "loadBalancerId": string
      // End of list of possible types for union field _load_balancer_id.
    
      // Union field _load_balancer_type can be only one of the following:
      "loadBalancerType": enum (LoadBalancerType)
      // End of list of possible types for union field _load_balancer_type.
    }  
  
Fields  
---  
`ipAddress` |  `string` The IP address of the endpoint, which can be an external or internal IP.  
`port` |  `integer` The IP protocol port of the endpoint. Only applicable when protocol is TCP or UDP.  
`instance` |  `string` A Compute Engine instance URI.  
`forwardingRule` |  `string` A forwarding rule and its corresponding IP address represent the frontend configuration of a Google Cloud load balancer. Forwarding rules are also used for protocol forwarding, Private Service Connect and other network services to provide forwarding information in the control plane. Applicable only to destination endpoint. Format: `projects/{project}/global/forwardingRules/{id}` or `projects/{project}/regions/{region}/forwardingRules/{id}`  
`gkeMasterCluster` |  `string` A cluster URI for [Google Kubernetes Engine cluster control plane](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture).  
`fqdn` |  `string` DNS endpoint of [Google Kubernetes Engine cluster control plane](https://cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture). Requires gke_master_cluster to be set, can't be used simultaneoulsly with ip_address or network. Applicable only to destination endpoint.  
`cloudSqlInstance` |  `string` A [Cloud SQL](https://cloud.google.com/sql) instance URI.  
`redisInstance` |  `string` A [Redis Instance](https://cloud.google.com/memorystore/docs/redis) URI. Applicable only to destination endpoint.  
`redisCluster` |  `string` A [Redis Cluster](https://cloud.google.com/memorystore/docs/cluster) URI. Applicable only to destination endpoint.  
`gkePod` |  `string` A [GKE Pod](https://cloud.google.com/kubernetes-engine/docs/concepts/pod) URI.  
`cloudFunction` |  `object (`[CloudFunctionEndpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.CloudFunctionEndpoint)`)` A [Cloud Function](https://cloud.google.com/functions). Applicable only to source endpoint.  
`appEngineVersion` |  `object (`[AppEngineVersionEndpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.AppEngineVersionEndpoint)`)` An [App Engine](https://cloud.google.com/appengine) [service version](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions). Applicable only to source endpoint.  
`cloudRunRevision` |  `object (`[CloudRunRevisionEndpoint](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.CloudRunRevisionEndpoint)`)` A [Cloud Run](https://cloud.google.com/run) [revision](https://cloud.google.com/run/docs/reference/rest/v1/namespaces.revisions/get) Applicable only to source endpoint.  
`network` |  `string` A VPC network URI. For source endpoints, used according to the `network_type`. For destination endpoints, used only when the source is an external IP address endpoint, and the destination is an internal IP address endpoint.  
`networkType` |  `enum (`NetworkType`)` For source endpoints, type of the network where the endpoint is located. Not relevant for destination endpoints.  
`projectId` |  `string` For source endpoints, endpoint project ID. Used according to the `network_type`. Not relevant for destination endpoints.  
Union field `_forwarding_rule_target`.`_forwarding_rule_target` can be only one of the following:  
`forwardingRuleTarget` |  `enum (`ForwardingRuleTarget`)` Output only. Specifies the type of the target of the forwarding rule.  
Union field `_load_balancer_id`.`_load_balancer_id` can be only one of the following:  
`loadBalancerId` |  `string` Output only. ID of the load balancer the forwarding rule points to. Empty for forwarding rules not related to load balancers.  
Union field `_load_balancer_type`.`_load_balancer_type` can be only one of the following:  
`loadBalancerType` |  `enum (`LoadBalancerType`)` Output only. Type of the load balancer the forwarding rule points to.  
  
### CloudFunctionEndpoint

JSON representation  
---  
      
    
    {
      "uri": string
    }  
  
Fields  
---  
`uri` |  `string` A [Cloud Function](https://cloud.google.com/functions) name.  
  
### AppEngineVersionEndpoint

JSON representation  
---  
      
    
    {
      "uri": string
    }  
  
Fields  
---  
`uri` |  `string` An [App Engine](https://cloud.google.com/appengine) [service version](https://cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions) name.  
  
### CloudRunRevisionEndpoint

JSON representation  
---  
      
    
    {
      "uri": string,
      "serviceUri": string
    }  
  
Fields  
---  
`uri` |  `string` A [Cloud Run](https://cloud.google.com/run) [revision](https://cloud.google.com/run/docs/reference/rest/v1/namespaces.revisions/get) URI. The format is: projects/{project}/locations/{location}/revisions/{revision}  
`serviceUri` |  `string` Output only. The URI of the Cloud Run service that the revision belongs to. The format is: projects/{project}/locations/{location}/services/{service}  
  
### LabelsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### ReachabilityDetails

JSON representation  
---  
      
    
    {
      "result": enum (Result),
      "verifyTime": string,
      "error": {
        object ([Status](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.Status))
      },
      "traces": [
        {
          object ([Trace](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.Trace))
        }
      ]
    }  
  
Fields  
---  
`result` |  `enum (`Result`)` The overall result of the test's configuration analysis.  
`verifyTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time of the configuration analysis.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`error` |  `object (`[Status](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.Status)`)` The details of a failure or a cancellation of reachability analysis.  
`traces[]` |  `object (`[Trace](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.Trace)`)` Result may contain a list of traces if a test has multiple possible paths in the network, such as when destination endpoint is a load balancer with multiple backends.  
  
### Status

JSON representation  
---  
      
    
    {
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
  
Fields  
---  
`code` |  `integer` The status code, which should be an enum value of `google.rpc.Code`.  
`message` |  `string` A developer-facing error message, which should be in English. Any user-facing error message should be localized and sent in the `google.rpc.Status.details` field, or localized by the client.  
`details[]` |  `object` A list of messages that carry the error details. There is a common set of message types for APIs to use.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
  
### Any

JSON representation  
---  
      
    
    {
      "typeUrl": string,
      "value": string
    }  
  
Fields  
---  
`typeUrl` |  `string` Identifies the type of the serialized Protobuf message with a URI reference consisting of a prefix ending in a slash and the fully-qualified type name.Example: type.googleapis.com/google.protobuf.StringValueThis string must contain at least one `/` character, and the content after the last `/` must be the fully-qualified name of the type in canonical form, without a leading dot. Do not write a scheme on these URI references so that clients do not attempt to contact them.The prefix is arbitrary and Protobuf implementations are expected to simply strip off everything up to and including the last `/` to identify the type. `type.googleapis.com/` is a common default prefix that some legacy implementations require. This prefix does not indicate the origin of the type, and URIs containing it are not expected to respond to any requests.All type URL strings must be legal URI references with the additional restriction (for the text format) that the content of the reference must consist only of alphanumeric characters, percent-encoded escapes, and characters in the following set (not including the outer backticks): `/-.~_!$&()*+,;=`. Despite our allowing percent encodings, implementations should not unescape them to prevent confusion with existing parsers. For example, `type.googleapis.com%2FFoo` should be rejected.In the original design of `Any`, the possibility of launching a type resolution service at these type URLs was considered but Protobuf never implemented one and considers contacting these URLs to be problematic and a potential security issue. Do not attempt to contact type URLs.  
`value` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Holds a Protobuf serialization of the type described by type_url.A base64-encoded string.  
  
### Trace

JSON representation  
---  
      
    
    {
      "endpointInfo": {
        object ([EndpointInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.EndpointInfo))
      },
      "steps": [
        {
          object ([Step](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.Step))
        }
      ],
      "forwardTraceId": integer
    }  
  
Fields  
---  
`endpointInfo` |  `object (`[EndpointInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.EndpointInfo)`)` Derived from the source and destination endpoints definition specified by user request, and validated by the data plane model. If there are multiple traces starting from different source locations, then the endpoint_info may be different between traces.  
`steps[]` |  `object (`[Step](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.Step)`)` A trace of a test contains multiple steps from the initial state to the final state (delivered, dropped, forwarded, or aborted).The steps are ordered by the processing sequence within the simulated network state machine. It is critical to preserve the order of the steps and avoid reordering or sorting them.  
`forwardTraceId` |  `integer` ID of trace. For forward traces, this ID is unique for each trace. For return traces, it matches ID of associated forward trace. A single forward trace can be associated with none, one or more than one return trace.  
  
### EndpointInfo

JSON representation  
---  
      
    
    {
      "sourceIp": string,
      "destinationIp": string,
      "protocol": string,
      "sourcePort": integer,
      "destinationPort": integer,
      "sourceNetworkUri": string,
      "destinationNetworkUri": string,
      "sourceAgentUri": string
    }  
  
Fields  
---  
`sourceIp` |  `string` Source IP address.  
`destinationIp` |  `string` Destination IP address.  
`protocol` |  `string` IP protocol in string format, for example: "TCP", "UDP", "ICMP".  
`sourcePort` |  `integer` Source port. Only valid when protocol is TCP or UDP.  
`destinationPort` |  `integer` Destination port. Only valid when protocol is TCP or UDP.  
`sourceNetworkUri` |  `string` URI of the network where this packet originates from.  
`destinationNetworkUri` |  `string` URI of the network where this packet is sent to.  
`sourceAgentUri` |  `string` URI of the source telemetry agent this packet originates from.  
  
### Step

JSON representation  
---  
      
    
    {
      "description": string,
      "state": enum (State),
      "causesDrop": boolean,
      "projectId": string,
    
      // Union field step_info can be only one of the following:
      "instance": {
        object ([InstanceInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.InstanceInfo))
      },
      "firewall": {
        object ([FirewallInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.FirewallInfo))
      },
      "route": {
        object ([RouteInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.RouteInfo))
      },
      "endpoint": {
        object ([EndpointInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.EndpointInfo))
      },
      "googleService": {
        object ([GoogleServiceInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.GoogleServiceInfo))
      },
      "forwardingRule": {
        object ([ForwardingRuleInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.ForwardingRuleInfo))
      },
      "hybridSubnet": {
        object ([HybridSubnetInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.HybridSubnetInfo))
      },
      "vpnGateway": {
        object ([VpnGatewayInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.VpnGatewayInfo))
      },
      "vpnTunnel": {
        object ([VpnTunnelInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.VpnTunnelInfo))
      },
      "interconnectAttachment": {
        object ([InterconnectAttachmentInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.InterconnectAttachmentInfo))
      },
      "vpcConnector": {
        object ([VpcConnectorInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.VpcConnectorInfo))
      },
      "directVpcEgressConnection": {
        object ([DirectVpcEgressConnectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.DirectVpcEgressConnectionInfo))
      },
      "serverlessExternalConnection": {
        object ([ServerlessExternalConnectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.ServerlessExternalConnectionInfo))
      },
      "deliver": {
        object ([DeliverInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.DeliverInfo))
      },
      "forward": {
        object ([ForwardInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.ForwardInfo))
      },
      "abort": {
        object ([AbortInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.AbortInfo))
      },
      "drop": {
        object ([DropInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.DropInfo))
      },
      "loadBalancer": {
        object ([LoadBalancerInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.LoadBalancerInfo))
      },
      "network": {
        object ([NetworkInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.NetworkInfo))
      },
      "gkeMaster": {
        object ([GKEMasterInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.GKEMasterInfo))
      },
      "gkePod": {
        object ([GkePodInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.GkePodInfo))
      },
      "ipMasqueradingSkipped": {
        object ([IpMasqueradingSkippedInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.IpMasqueradingSkippedInfo))
      },
      "gkeNetworkPolicy": {
        object ([GkeNetworkPolicyInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.GkeNetworkPolicyInfo))
      },
      "gkeNetworkPolicySkipped": {
        object ([GkeNetworkPolicySkippedInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.GkeNetworkPolicySkippedInfo))
      },
      "cloudSqlInstance": {
        object ([CloudSQLInstanceInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.CloudSQLInstanceInfo))
      },
      "redisInstance": {
        object ([RedisInstanceInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.RedisInstanceInfo))
      },
      "redisCluster": {
        object ([RedisClusterInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.RedisClusterInfo))
      },
      "cloudFunction": {
        object ([CloudFunctionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.CloudFunctionInfo))
      },
      "appEngineVersion": {
        object ([AppEngineVersionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.AppEngineVersionInfo))
      },
      "cloudRunRevision": {
        object ([CloudRunRevisionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.CloudRunRevisionInfo))
      },
      "nat": {
        object ([NatInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.NatInfo))
      },
      "proxyConnection": {
        object ([ProxyConnectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.ProxyConnectionInfo))
      },
      "loadBalancerBackendInfo": {
        object ([LoadBalancerBackendInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.LoadBalancerBackendInfo))
      },
      "storageBucket": {
        object ([StorageBucketInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.StorageBucketInfo))
      },
      "serverlessNeg": {
        object ([ServerlessNegInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.ServerlessNegInfo))
      },
      "ngfwPacketInspection": {
        object ([NgfwPacketInspectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.NgfwPacketInspectionInfo))
      }
      // End of list of possible types for union field step_info.
    }  
  
Fields  
---  
`description` |  `string` A description of the step. Usually this is a summary of the state.  
`state` |  `enum (`State`)` Each step is in one of the pre-defined states.  
`causesDrop` |  `boolean` This is a step that leads to the final state Drop.  
`projectId` |  `string` Project ID that contains the configuration this step is validating.  
Union field `step_info`. Configuration or metadata associated with each step. The configuration is filtered based on viewer's permission. If a viewer has no permission to view the configuration in this step, for non-final states a special state is populated (VIEWER_PERMISSION_MISSING), and for final state the configuration is cleared. `step_info` can be only one of the following:  
`instance` |  `object (`[InstanceInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.InstanceInfo)`)` Display information of a Compute Engine instance.  
`firewall` |  `object (`[FirewallInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.FirewallInfo)`)` Display information of a Compute Engine firewall rule.  
`route` |  `object (`[RouteInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.RouteInfo)`)` Display information of a Compute Engine route.  
`endpoint` |  `object (`[EndpointInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.EndpointInfo)`)` Display information of the source and destination under analysis. The endpoint information in an intermediate state may differ with the initial input, as it might be modified by state like NAT, or Connection Proxy.  
`googleService` |  `object (`[GoogleServiceInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.GoogleServiceInfo)`)` Display information of a Google service  
`forwardingRule` |  `object (`[ForwardingRuleInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.ForwardingRuleInfo)`)` Display information of a Compute Engine forwarding rule.  
`hybridSubnet` |  `object (`[HybridSubnetInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.HybridSubnetInfo)`)` Display information of a hybrid subnet.  
`vpnGateway` |  `object (`[VpnGatewayInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.VpnGatewayInfo)`)` Display information of a Compute Engine VPN gateway.  
`vpnTunnel` |  `object (`[VpnTunnelInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.VpnTunnelInfo)`)` Display information of a Compute Engine VPN tunnel.  
`interconnectAttachment` |  `object (`[InterconnectAttachmentInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.InterconnectAttachmentInfo)`)` Display information of an interconnect attachment.  
`vpcConnector` |  `object (`[VpcConnectorInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.VpcConnectorInfo)`)` Display information of a VPC connector.  
`directVpcEgressConnection` |  `object (`[DirectVpcEgressConnectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.DirectVpcEgressConnectionInfo)`)` Display information of a serverless direct VPC egress connection.  
`serverlessExternalConnection` |  `object (`[ServerlessExternalConnectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.ServerlessExternalConnectionInfo)`)` Display information of a serverless public (external) connection.  
`deliver` |  `object (`[DeliverInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.DeliverInfo)`)` Display information of the final state "deliver" and reason.  
`forward` |  `object (`[ForwardInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.ForwardInfo)`)` Display information of the final state "forward" and reason.  
`abort` |  `object (`[AbortInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.AbortInfo)`)` Display information of the final state "abort" and reason.  
`drop` |  `object (`[DropInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.DropInfo)`)` Display information of the final state "drop" and reason.  
`loadBalancer  
**(deprecated)**` |  `object (`[LoadBalancerInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.LoadBalancerInfo)`)` This item is deprecated!Display information of the load balancers. Deprecated in favor of the `load_balancer_backend_info` field, not used in new tests.  
`network` |  `object (`[NetworkInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.NetworkInfo)`)` Display information of a Google Cloud network.  
`gkeMaster` |  `object (`[GKEMasterInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.GKEMasterInfo)`)` Display information of a Google Kubernetes Engine cluster master.  
`gkePod` |  `object (`[GkePodInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.GkePodInfo)`)` Display information of a Google Kubernetes Engine Pod.  
`ipMasqueradingSkipped` |  `object (`[IpMasqueradingSkippedInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.IpMasqueradingSkippedInfo)`)` Display information of the reason why GKE Pod IP masquerading was skipped.  
`gkeNetworkPolicy` |  `object (`[GkeNetworkPolicyInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.GkeNetworkPolicyInfo)`)` Display information of a GKE Network Policy.  
`gkeNetworkPolicySkipped` |  `object (`[GkeNetworkPolicySkippedInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.GkeNetworkPolicySkippedInfo)`)` Display information of the reason why GKE Network Policy evaluation was skipped.  
`cloudSqlInstance` |  `object (`[CloudSQLInstanceInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.CloudSQLInstanceInfo)`)` Display information of a Cloud SQL instance.  
`redisInstance` |  `object (`[RedisInstanceInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.RedisInstanceInfo)`)` Display information of a Redis Instance.  
`redisCluster` |  `object (`[RedisClusterInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.RedisClusterInfo)`)` Display information of a Redis Cluster.  
`cloudFunction` |  `object (`[CloudFunctionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.CloudFunctionInfo)`)` Display information of a Cloud Function.  
`appEngineVersion` |  `object (`[AppEngineVersionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.AppEngineVersionInfo)`)` Display information of an App Engine service version.  
`cloudRunRevision` |  `object (`[CloudRunRevisionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.CloudRunRevisionInfo)`)` Display information of a Cloud Run revision.  
`nat` |  `object (`[NatInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.NatInfo)`)` Display information of a NAT.  
`proxyConnection` |  `object (`[ProxyConnectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.ProxyConnectionInfo)`)` Display information of a ProxyConnection.  
`loadBalancerBackendInfo` |  `object (`[LoadBalancerBackendInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.LoadBalancerBackendInfo)`)` Display information of a specific load balancer backend.  
`storageBucket` |  `object (`[StorageBucketInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.StorageBucketInfo)`)` Display information of a Storage Bucket. Used only for return traces.  
`serverlessNeg` |  `object (`[ServerlessNegInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.ServerlessNegInfo)`)` Display information of a Serverless network endpoint group backend. Used only for return traces.  
`ngfwPacketInspection` |  `object (`[NgfwPacketInspectionInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.NgfwPacketInspectionInfo)`)` Display information of a layer 7 packet inspection by the firewall.  
  
### InstanceInfo

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "interface": string,
      "networkUri": string,
      "internalIp": string,
      "externalIp": string,
      "networkTags": [
        string
      ],
      "serviceAccount": string,
      "pscNetworkAttachmentUri": string,
      "running": boolean,
      "status": enum (Status)
    }  
  
Fields  
---  
`displayName` |  `string` Name of a Compute Engine instance.  
`uri` |  `string` URI of a Compute Engine instance.  
`interface` |  `string` Name of the network interface of a Compute Engine instance.  
`networkUri` |  `string` URI of a Compute Engine network.  
`internalIp` |  `string` Internal IP address of the network interface.  
`externalIp` |  `string` External IP address of the network interface.  
`networkTags[]` |  `string` Network tags configured on the instance.  
`serviceAccount  
**(deprecated)**` |  `string` This item is deprecated!Service account authorized for the instance.  
`pscNetworkAttachmentUri` |  `string` URI of the PSC network attachment the NIC is attached to (if relevant).  
`running  
**(deprecated)**` |  `boolean` This item is deprecated!Indicates whether the Compute Engine instance is running. Deprecated: use the `status` field instead.  
`status` |  `enum (`Status`)` The status of the instance.  
  
### FirewallInfo

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "direction": string,
      "action": string,
      "priority": integer,
      "networkUri": string,
      "targetTags": [
        string
      ],
      "targetServiceAccounts": [
        string
      ],
      "policy": string,
      "policyUri": string,
      "firewallRuleType": enum (FirewallRuleType),
      "policyPriority": integer,
      "targetType": enum (TargetType)
    }  
  
Fields  
---  
`displayName` |  `string` The display name of the firewall rule. This field might be empty for firewall policy rules.  
`uri` |  `string` The URI of the firewall rule. This field is not applicable to implied VPC firewall rules.  
`direction` |  `string` Possible values: INGRESS, EGRESS  
`action` |  `string` Possible values: ALLOW, DENY, APPLY_SECURITY_PROFILE_GROUP  
`priority` |  `integer` The priority of the firewall rule.  
`networkUri` |  `string` The URI of the VPC network that the firewall rule is associated with. This field is not applicable to hierarchical firewall policy rules.  
`targetTags[]` |  `string` The target tags defined by the VPC firewall rule. This field is not applicable to firewall policy rules.  
`targetServiceAccounts[]` |  `string` The target service accounts specified by the firewall rule.  
`policy` |  `string` The name of the firewall policy that this rule is associated with. This field is not applicable to VPC firewall rules and implied VPC firewall rules.  
`policyUri` |  `string` The URI of the firewall policy that this rule is associated with. This field is not applicable to VPC firewall rules and implied VPC firewall rules.  
`firewallRuleType` |  `enum (`FirewallRuleType`)` The firewall rule's type.  
`policyPriority` |  `integer` The priority of the firewall policy that this rule is associated with. This field is not applicable to VPC firewall rules and implied VPC firewall rules.  
`targetType` |  `enum (`TargetType`)` Target type of the firewall rule.  
  
### RouteInfo

JSON representation  
---  
      
    
    {
      "routeType": enum (RouteType),
      "nextHopType": enum (NextHopType),
      "routeScope": enum (RouteScope),
      "displayName": string,
      "uri": string,
      "region": string,
      "destIpRange": string,
      "nextHop": string,
      "networkUri": string,
      "priority": integer,
      "instanceTags": [
        string
      ],
      "srcIpRange": string,
      "destPortRanges": [
        string
      ],
      "srcPortRanges": [
        string
      ],
      "protocols": [
        string
      ],
      "nextHopUri": string,
      "nextHopNetworkUri": string,
      "originatingRouteUri": string,
      "originatingRouteDisplayName": string,
      "nccHubRouteUri": string,
    
      // Union field _ncc_hub_uri can be only one of the following:
      "nccHubUri": string
      // End of list of possible types for union field _ncc_hub_uri.
    
      // Union field _ncc_spoke_uri can be only one of the following:
      "nccSpokeUri": string
      // End of list of possible types for union field _ncc_spoke_uri.
    
      // Union field _advertised_route_source_router_uri can be only one of the
      // following:
      "advertisedRouteSourceRouterUri": string
      // End of list of possible types for union field
      // _advertised_route_source_router_uri.
    
      // Union field _advertised_route_next_hop_uri can be only one of the following:
      "advertisedRouteNextHopUri": string
      // End of list of possible types for union field
      // _advertised_route_next_hop_uri.
    }  
  
Fields  
---  
`routeType` |  `enum (`RouteType`)` Type of route.  
`nextHopType` |  `enum (`NextHopType`)` Type of next hop.  
`routeScope  
**(deprecated)**` |  `enum (`RouteScope`)` This item is deprecated!Indicates where route is applicable. Deprecated, routes with NCC_HUB scope are not included in the trace in new tests.  
`displayName` |  `string` Name of a route.  
`uri` |  `string` URI of a route. SUBNET, STATIC, PEERING_SUBNET (only for peering network) and POLICY_BASED routes only.  
`region` |  `string` Region of the route. DYNAMIC, PEERING_DYNAMIC, POLICY_BASED and ADVERTISED routes only. If set for POLICY_BASED route, this is a region of VLAN attachments for Cloud Interconnect the route applies to. If set to "all" for POLICY_BASED route, the route applies to VLAN attachments of Cloud Interconnect in all regions.  
`destIpRange` |  `string` Destination IP range of the route.  
`nextHop  
**(deprecated)**` |  `string` This item is deprecated!String type of the next hop of the route (for example, "VPN tunnel"). Deprecated in favor of the next_hop_type and next_hop_uri fields, not used in new tests.  
`networkUri` |  `string` URI of a VPC network where route is located.  
`priority` |  `integer` Priority of the route.  
`instanceTags[]` |  `string` Instance tags of the route.  
`srcIpRange` |  `string` Source IP address range of the route. POLICY_BASED routes only.  
`destPortRanges[]` |  `string` Destination port ranges of the route. POLICY_BASED routes only.  
`srcPortRanges[]` |  `string` Source port ranges of the route. POLICY_BASED routes only.  
`protocols[]` |  `string` Protocols of the route. POLICY_BASED routes only.  
`nextHopUri` |  `string` URI of the next hop resource.  
`nextHopNetworkUri` |  `string` URI of a VPC network where the next hop resource is located.  
`originatingRouteUri` |  `string` For PEERING_SUBNET and PEERING_STATIC routes, the URI of the originating SUBNET/STATIC route.  
`originatingRouteDisplayName` |  `string` For PEERING_SUBNET, PEERING_STATIC and PEERING_DYNAMIC routes, the name of the originating SUBNET/STATIC/DYNAMIC route.  
`nccHubRouteUri` |  `string` For PEERING_SUBNET and PEERING_DYNAMIC routes that are advertised by NCC Hub, the URI of the corresponding route in NCC Hub's routing table.  
Union field `_ncc_hub_uri`.`_ncc_hub_uri` can be only one of the following:  
`nccHubUri` |  `string` URI of the NCC Hub the route is advertised by. PEERING_SUBNET and PEERING_DYNAMIC routes that are advertised by NCC Hub only.  
Union field `_ncc_spoke_uri`.`_ncc_spoke_uri` can be only one of the following:  
`nccSpokeUri` |  `string` URI of the destination NCC Spoke. PEERING_SUBNET and PEERING_DYNAMIC routes that are advertised by NCC Hub only.  
Union field `_advertised_route_source_router_uri`.`_advertised_route_source_router_uri` can be only one of the following:  
`advertisedRouteSourceRouterUri` |  `string` For ADVERTISED dynamic routes, the URI of the Cloud Router that advertised the corresponding IP prefix.  
Union field `_advertised_route_next_hop_uri`.`_advertised_route_next_hop_uri` can be only one of the following:  
`advertisedRouteNextHopUri  
**(deprecated)**` |  `string` This item is deprecated!For ADVERTISED routes, the URI of their next hop, i.e. the URI of the hybrid endpoint (VPN tunnel, Interconnect attachment, NCC router appliance) the advertised prefix is advertised through, or URI of the source peered network. Deprecated in favor of the next_hop_uri field, not used in new tests.  
  
### GoogleServiceInfo

JSON representation  
---  
      
    
    {
      "sourceIp": string,
      "googleServiceType": enum (GoogleServiceType)
    }  
  
Fields  
---  
`sourceIp` |  `string` Source IP address.  
`googleServiceType` |  `enum (`GoogleServiceType`)` Recognized type of a Google Service.  
  
### ForwardingRuleInfo

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "matchedProtocol": string,
      "matchedPortRange": string,
      "vip": string,
      "target": string,
      "networkUri": string,
      "region": string,
      "loadBalancerName": string,
      "pscServiceAttachmentUri": string,
      "pscGoogleApiTarget": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of the forwarding rule.  
`uri` |  `string` URI of the forwarding rule.  
`matchedProtocol` |  `string` Protocol defined in the forwarding rule that matches the packet.  
`matchedPortRange` |  `string` Port range defined in the forwarding rule that matches the packet.  
`vip` |  `string` VIP of the forwarding rule.  
`target` |  `string` Target type of the forwarding rule.  
`networkUri` |  `string` Network URI.  
`region` |  `string` Region of the forwarding rule. Set only for regional forwarding rules.  
`loadBalancerName` |  `string` Name of the load balancer the forwarding rule belongs to. Empty for forwarding rules not related to load balancers (like PSC forwarding rules).  
`pscServiceAttachmentUri` |  `string` URI of the PSC service attachment this forwarding rule targets (if applicable).  
`pscGoogleApiTarget` |  `string` PSC Google API target this forwarding rule targets (if applicable).  
  
### HybridSubnetInfo

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "region": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a hybrid subnet.  
`uri` |  `string` URI of a hybrid subnet.  
`region` |  `string` Name of a Google Cloud region where the hybrid subnet is configured.  
  
### VpnGatewayInfo

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "networkUri": string,
      "ipAddress": string,
      "vpnTunnelUri": string,
      "region": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a VPN gateway.  
`uri` |  `string` URI of a VPN gateway.  
`networkUri` |  `string` URI of a Compute Engine network where the VPN gateway is configured.  
`ipAddress` |  `string` IP address of the VPN gateway.  
`vpnTunnelUri` |  `string` A VPN tunnel that is associated with this VPN gateway. There may be multiple VPN tunnels configured on a VPN gateway, and only the one relevant to the test is displayed.  
`region` |  `string` Name of a Google Cloud region where this VPN gateway is configured.  
  
### VpnTunnelInfo

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "sourceGateway": string,
      "remoteGateway": string,
      "remoteGatewayIp": string,
      "sourceGatewayIp": string,
      "networkUri": string,
      "region": string,
      "routingType": enum (RoutingType)
    }  
  
Fields  
---  
`displayName` |  `string` Name of a VPN tunnel.  
`uri` |  `string` URI of a VPN tunnel.  
`sourceGateway` |  `string` URI of the VPN gateway at local end of the tunnel.  
`remoteGateway` |  `string` URI of a VPN gateway at remote end of the tunnel.  
`remoteGatewayIp` |  `string` Remote VPN gateway's IP address.  
`sourceGatewayIp` |  `string` Local VPN gateway's IP address.  
`networkUri` |  `string` URI of a Compute Engine network where the VPN tunnel is configured.  
`region` |  `string` Name of a Google Cloud region where this VPN tunnel is configured.  
`routingType` |  `enum (`RoutingType`)` Type of the routing policy.  
  
### InterconnectAttachmentInfo

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "interconnectUri": string,
      "region": string,
      "cloudRouterUri": string,
      "type": enum (Type),
      "l2AttachmentMatchedIpAddress": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of an Interconnect attachment.  
`uri` |  `string` URI of an Interconnect attachment.  
`interconnectUri` |  `string` URI of the Interconnect where the Interconnect attachment is configured.  
`region` |  `string` Name of a Google Cloud region where the Interconnect attachment is configured.  
`cloudRouterUri` |  `string` URI of the Cloud Router to be used for dynamic routing.  
`type` |  `enum (`Type`)` The type of interconnect attachment this is.  
`l2AttachmentMatchedIpAddress` |  `string` Appliance IP address that was matched for L2_DEDICATED attachments.  
  
### VpcConnectorInfo

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "location": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a VPC connector.  
`uri` |  `string` URI of a VPC connector.  
`location` |  `string` Location in which the VPC connector is deployed.  
  
### DirectVpcEgressConnectionInfo

JSON representation  
---  
      
    
    {
      "networkUri": string,
      "subnetworkUri": string,
      "selectedIpRange": string,
      "selectedIpAddress": string,
      "region": string
    }  
  
Fields  
---  
`networkUri` |  `string` URI of direct access network.  
`subnetworkUri` |  `string` URI of direct access subnetwork.  
`selectedIpRange` |  `string` Selected IP range.  
`selectedIpAddress` |  `string` Selected starting IP address, from the selected IP range.  
`region` |  `string` Region in which the Direct VPC egress is deployed.  
  
### ServerlessExternalConnectionInfo

JSON representation  
---  
      
    
    {
      "selectedIpAddress": string
    }  
  
Fields  
---  
`selectedIpAddress` |  `string` Selected starting IP address, from the Google dynamic address pool.  
  
### DeliverInfo

JSON representation  
---  
      
    
    {
      "target": enum (Target),
      "resourceUri": string,
      "ipAddress": string,
      "storageBucket": string,
      "pscGoogleApiTarget": string,
      "googleServiceType": enum (GoogleServiceType)
    }  
  
Fields  
---  
`target` |  `enum (`Target`)` Target type where the packet is delivered to.  
`resourceUri` |  `string` URI of the resource that the packet is delivered to.  
`ipAddress` |  `string` IP address of the target (if applicable).  
`storageBucket` |  `string` Name of the Cloud Storage Bucket the packet is delivered to (if applicable).  
`pscGoogleApiTarget` |  `string` PSC Google API target the packet is delivered to (if applicable).  
`googleServiceType` |  `enum (`GoogleServiceType`)` Recognized type of a Google Service the packet is delivered to (if applicable).  
  
### ForwardInfo

JSON representation  
---  
      
    
    {
      "target": enum (Target),
      "resourceUri": string,
      "ipAddress": string
    }  
  
Fields  
---  
`target` |  `enum (`Target`)` Target type where this packet is forwarded to.  
`resourceUri` |  `string` URI of the resource that the packet is forwarded to.  
`ipAddress` |  `string` IP address of the target (if applicable).  
  
### AbortInfo

JSON representation  
---  
      
    
    {
      "cause": enum (Cause),
      "resourceUri": string,
      "ipAddress": string,
      "projectsMissingPermission": [
        string
      ]
    }  
  
Fields  
---  
`cause` |  `enum (`Cause`)` Causes that the analysis is aborted.  
`resourceUri` |  `string` URI of the resource that caused the abort.  
`ipAddress` |  `string` IP address that caused the abort.  
`projectsMissingPermission[]` |  `string` List of project IDs the user specified in the request but lacks access to. In this case, analysis is aborted with the PERMISSION_DENIED cause.  
  
### DropInfo

JSON representation  
---  
      
    
    {
      "cause": enum (Cause),
      "resourceUri": string,
      "sourceIp": string,
      "destinationIp": string,
      "region": string,
      "sourceGeolocationCode": string,
      "destinationGeolocationCode": string
    }  
  
Fields  
---  
`cause` |  `enum (`Cause`)` Cause that the packet is dropped.  
`resourceUri` |  `string` URI of the resource that caused the drop.  
`sourceIp` |  `string` Source IP address of the dropped packet (if relevant).  
`destinationIp` |  `string` Destination IP address of the dropped packet (if relevant).  
`region` |  `string` Region of the dropped packet (if relevant).  
`sourceGeolocationCode` |  `string` Geolocation (region code) of the source IP address (if relevant).  
`destinationGeolocationCode` |  `string` Geolocation (region code) of the destination IP address (if relevant).  
  
### LoadBalancerInfo

JSON representation  
---  
      
    
    {
      "loadBalancerType": enum (LoadBalancerType),
      "healthCheckUri": string,
      "backends": [
        {
          object ([LoadBalancerBackend](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.LoadBalancerBackend))
        }
      ],
      "backendType": enum (BackendType),
      "backendUri": string
    }  
  
Fields  
---  
`loadBalancerType` |  `enum (`LoadBalancerType`)` Type of the load balancer.  
`healthCheckUri  
**(deprecated)**` |  `string` This item is deprecated!URI of the health check for the load balancer. Deprecated and no longer populated as different load balancer backends might have different health checks.  
`backends[]` |  `object (`[LoadBalancerBackend](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.LoadBalancerBackend)`)` Information for the loadbalancer backends.  
`backendType` |  `enum (`BackendType`)` Type of load balancer's backend configuration.  
`backendUri` |  `string` Backend configuration URI.  
  
### LoadBalancerBackend

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "healthCheckFirewallState": enum (HealthCheckFirewallState),
      "healthCheckAllowingFirewallRules": [
        string
      ],
      "healthCheckBlockingFirewallRules": [
        string
      ]
    }  
  
Fields  
---  
`displayName` |  `string` Name of a Compute Engine instance or network endpoint.  
`uri` |  `string` URI of a Compute Engine instance or network endpoint.  
`healthCheckFirewallState` |  `enum (`HealthCheckFirewallState`)` State of the health check firewall configuration.  
`healthCheckAllowingFirewallRules[]` |  `string` A list of firewall rule URIs allowing probes from health check IP ranges.  
`healthCheckBlockingFirewallRules[]` |  `string` A list of firewall rule URIs blocking probes from health check IP ranges.  
  
### NetworkInfo

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "matchedSubnetUri": string,
      "matchedIpRange": string,
      "region": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a Compute Engine network.  
`uri` |  `string` URI of a Compute Engine network.  
`matchedSubnetUri` |  `string` URI of the subnet matching the source IP address of the test.  
`matchedIpRange` |  `string` The IP range of the subnet matching the source IP address of the test.  
`region` |  `string` The region of the subnet matching the source IP address of the test.  
  
### GKEMasterInfo

JSON representation  
---  
      
    
    {
      "clusterUri": string,
      "clusterNetworkUri": string,
      "internalIp": string,
      "externalIp": string,
      "dnsEndpoint": string
    }  
  
Fields  
---  
`clusterUri` |  `string` URI of a GKE cluster.  
`clusterNetworkUri` |  `string` URI of a GKE cluster network.  
`internalIp` |  `string` Internal IP address of a GKE cluster control plane.  
`externalIp` |  `string` External IP address of a GKE cluster control plane.  
`dnsEndpoint` |  `string` DNS endpoint of a GKE cluster control plane.  
  
### GkePodInfo

JSON representation  
---  
      
    
    {
      "podUri": string,
      "ipAddress": string,
      "networkUri": string
    }  
  
Fields  
---  
`podUri` |  `string` URI of a GKE Pod. For Pods in regional Clusters, the URI format is: `projects/{project}/locations/{location}/clusters/{cluster}/k8s/namespaces/{namespace}/pods/{pod}` For Pods in zonal Clusters, the URI format is: `projects/{project}/zones/{zone}/clusters/{cluster}/k8s/namespaces/{namespace}/pods/{pod}`  
`ipAddress` |  `string` IP address of a GKE Pod. If the Pod is dual-stack, this is the IP address relevant to the trace.  
`networkUri` |  `string` URI of the network containing the GKE Pod.  
  
### IpMasqueradingSkippedInfo

JSON representation  
---  
      
    
    {
      "reason": enum (Reason),
      "nonMasqueradeRange": string
    }  
  
Fields  
---  
`reason` |  `enum (`Reason`)` Reason why IP masquerading was not applied.  
`nonMasqueradeRange` |  `string` The matched non-masquerade IP range. Only set if reason is DESTINATION_IP_IN_CONFIGURED_NON_MASQUERADE_RANGE or DESTINATION_IP_IN_DEFAULT_NON_MASQUERADE_RANGE.  
  
### GkeNetworkPolicyInfo

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "direction": string,
      "action": string
    }  
  
Fields  
---  
`displayName` |  `string` The name of the Network Policy.  
`uri` |  `string` The URI of the Network Policy. Format for a Network Policy in a zonal cluster: `projects/<project_id>/zones/<zone>/clusters/<cluster>/k8s/namespaces/<namespace>/networking.k8s.io/networkpolicies/<networkpolicy>` Format for a Network Policy in a regional cluster: `projects/<project_id>/locations/<location>/clusters/<cluster>/k8s/namespaces/<namespace>/networking.k8s.io/networkpolicies/<networkpolicy>`  
`direction` |  `string` Possible values: INGRESS, EGRESS  
`action` |  `string` Possible values: ALLOW, DENY  
  
### GkeNetworkPolicySkippedInfo

JSON representation  
---  
      
    
    {
      "reason": enum (Reason)
    }  
  
Fields  
---  
`reason` |  `enum (`Reason`)` Reason why Network Policy evaluation was skipped.  
  
### CloudSQLInstanceInfo

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "networkUri": string,
      "internalIp": string,
      "externalIp": string,
      "region": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a Cloud SQL instance.  
`uri` |  `string` URI of a Cloud SQL instance.  
`networkUri` |  `string` URI of a Cloud SQL instance network or empty string if the instance does not have one.  
`internalIp` |  `string` Internal IP address of a Cloud SQL instance.  
`externalIp` |  `string` External IP address of a Cloud SQL instance.  
`region` |  `string` Region in which the Cloud SQL instance is running.  
  
### RedisInstanceInfo

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "networkUri": string,
      "primaryEndpointIp": string,
      "readEndpointIp": string,
      "region": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a Cloud Redis Instance.  
`uri` |  `string` URI of a Cloud Redis Instance.  
`networkUri` |  `string` URI of a Cloud Redis Instance network.  
`primaryEndpointIp` |  `string` Primary endpoint IP address of a Cloud Redis Instance.  
`readEndpointIp` |  `string` Read endpoint IP address of a Cloud Redis Instance (if applicable).  
`region` |  `string` Region in which the Cloud Redis Instance is defined.  
  
### RedisClusterInfo

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "networkUri": string,
      "discoveryEndpointIpAddress": string,
      "secondaryEndpointIpAddress": string,
      "location": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a Redis Cluster.  
`uri` |  `string` URI of a Redis Cluster in format "projects/{project_id}/locations/{location}/clusters/{cluster_id}"  
`networkUri` |  `string` URI of the network containing the Redis Cluster endpoints in format "projects/{project_id}/global/networks/{network_id}".  
`discoveryEndpointIpAddress` |  `string` Discovery endpoint IP address of a Redis Cluster.  
`secondaryEndpointIpAddress` |  `string` Secondary endpoint IP address of a Redis Cluster.  
`location` |  `string` Name of the region in which the Redis Cluster is defined. For example, "us-central1".  
  
### CloudFunctionInfo

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "location": string,
      "versionId": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a Cloud Function.  
`uri` |  `string` URI of a Cloud Function.  
`location` |  `string` Location in which the Cloud Function is deployed.  
`versionId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Latest successfully deployed version id of the Cloud Function.  
  
### AppEngineVersionInfo

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "runtime": string,
      "environment": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of an App Engine version.  
`uri` |  `string` URI of an App Engine version.  
`runtime` |  `string` Runtime of the App Engine version.  
`environment` |  `string` App Engine execution environment for a version.  
  
### CloudRunRevisionInfo

JSON representation  
---  
      
    
    {
      "displayName": string,
      "uri": string,
      "location": string,
      "serviceUri": string
    }  
  
Fields  
---  
`displayName` |  `string` Name of a Cloud Run revision.  
`uri` |  `string` URI of a Cloud Run revision.  
`location` |  `string` Location in which this revision is deployed.  
`serviceUri` |  `string` URI of Cloud Run service this revision belongs to.  
  
### NatInfo

JSON representation  
---  
      
    
    {
      "type": enum (Type),
      "protocol": string,
      "networkUri": string,
      "oldSourceIp": string,
      "newSourceIp": string,
      "oldDestinationIp": string,
      "newDestinationIp": string,
      "oldSourcePort": integer,
      "newSourcePort": integer,
      "oldDestinationPort": integer,
      "newDestinationPort": integer,
      "routerUri": string,
      "natGatewayName": string,
      "cloudNatGatewayType": enum (CloudNatGatewayType)
    }  
  
Fields  
---  
`type` |  `enum (`Type`)` Type of NAT.  
`protocol` |  `string` IP protocol in string format, for example: "TCP", "UDP", "ICMP".  
`networkUri` |  `string` URI of the network where NAT translation takes place.  
`oldSourceIp` |  `string` Source IP address before NAT translation.  
`newSourceIp` |  `string` Source IP address after NAT translation.  
`oldDestinationIp` |  `string` Destination IP address before NAT translation.  
`newDestinationIp` |  `string` Destination IP address after NAT translation.  
`oldSourcePort` |  `integer` Source port before NAT translation. Only valid when protocol is TCP or UDP.  
`newSourcePort` |  `integer` Source port after NAT translation. Only valid when protocol is TCP or UDP.  
`oldDestinationPort` |  `integer` Destination port before NAT translation. Only valid when protocol is TCP or UDP.  
`newDestinationPort` |  `integer` Destination port after NAT translation. Only valid when protocol is TCP or UDP.  
`routerUri` |  `string` Uri of the Cloud Router. Only valid when type is CLOUD_NAT.  
`natGatewayName` |  `string` The name of Cloud NAT Gateway. Only valid when type is CLOUD_NAT.  
`cloudNatGatewayType` |  `enum (`CloudNatGatewayType`)` Type of Cloud NAT gateway. Only valid when `type` is CLOUD_NAT.  
  
### ProxyConnectionInfo

JSON representation  
---  
      
    
    {
      "protocol": string,
      "oldSourceIp": string,
      "newSourceIp": string,
      "oldDestinationIp": string,
      "newDestinationIp": string,
      "oldSourcePort": integer,
      "newSourcePort": integer,
      "oldDestinationPort": integer,
      "newDestinationPort": integer,
      "subnetUri": string,
      "networkUri": string
    }  
  
Fields  
---  
`protocol` |  `string` IP protocol in string format, for example: "TCP", "UDP", "ICMP".  
`oldSourceIp` |  `string` Source IP address of an original connection.  
`newSourceIp` |  `string` Source IP address of a new connection.  
`oldDestinationIp` |  `string` Destination IP address of an original connection  
`newDestinationIp` |  `string` Destination IP address of a new connection.  
`oldSourcePort` |  `integer` Source port of an original connection. Only valid when protocol is TCP or UDP.  
`newSourcePort` |  `integer` Source port of a new connection. Only valid when protocol is TCP or UDP.  
`oldDestinationPort` |  `integer` Destination port of an original connection. Only valid when protocol is TCP or UDP.  
`newDestinationPort` |  `integer` Destination port of a new connection. Only valid when protocol is TCP or UDP.  
`subnetUri` |  `string` Uri of proxy subnet.  
`networkUri` |  `string` URI of the network where connection is proxied.  
  
### LoadBalancerBackendInfo

JSON representation  
---  
      
    
    {
      "name": string,
      "instanceUri": string,
      "backendServiceUri": string,
      "instanceGroupUri": string,
      "networkEndpointGroupUri": string,
      "backendBucketUri": string,
      "pscServiceAttachmentUri": string,
      "pscGoogleApiTarget": string,
      "healthCheckUri": string,
      "healthCheckFirewallsConfigState": enum (HealthCheckFirewallsConfigState)
    }  
  
Fields  
---  
`name` |  `string` Display name of the backend. For example, it might be an instance name for the instance group backends, or an IP address and port for zonal network endpoint group backends.  
`instanceUri` |  `string` URI of the backend instance (if applicable). Populated for instance group backends, and zonal NEG backends.  
`backendServiceUri` |  `string` URI of the backend service this backend belongs to (if applicable).  
`instanceGroupUri` |  `string` URI of the instance group this backend belongs to (if applicable).  
`networkEndpointGroupUri` |  `string` URI of the network endpoint group this backend belongs to (if applicable).  
`backendBucketUri` |  `string` URI of the backend bucket this backend targets (if applicable).  
`pscServiceAttachmentUri` |  `string` URI of the PSC service attachment this PSC NEG backend targets (if applicable).  
`pscGoogleApiTarget` |  `string` PSC Google API target this PSC NEG backend targets (if applicable).  
`healthCheckUri` |  `string` URI of the health check attached to this backend (if applicable).  
`healthCheckFirewallsConfigState` |  `enum (`HealthCheckFirewallsConfigState`)` Output only. Health check firewalls configuration state for the backend. This is a result of the static firewall analysis (verifying that health check traffic from required IP ranges to the backend is allowed or not). The backend might still be unhealthy even if these firewalls are configured. Please refer to the documentation for more information: <https://cloud.google.com/load-balancing/docs/firewall-rules>  
  
### StorageBucketInfo

JSON representation  
---  
      
    
    {
      "bucket": string
    }  
  
Fields  
---  
`bucket` |  `string` Cloud Storage Bucket name.  
  
### ServerlessNegInfo

JSON representation  
---  
      
    
    {
      "negUri": string
    }  
  
Fields  
---  
`negUri` |  `string` URI of the serverless network endpoint group.  
  
### NgfwPacketInspectionInfo

JSON representation  
---  
      
    
    {
      "securityProfileGroupUri": string
    }  
  
Fields  
---  
`securityProfileGroupUri` |  `string` URI of the security profile group associated with this firewall packet inspection.  
  
### ProbingDetails

JSON representation  
---  
      
    
    {
      "result": enum (ProbingResult),
      "verifyTime": string,
      "error": {
        object ([Status](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.Status))
      },
      "abortCause": enum (ProbingAbortCause),
      "sentProbeCount": integer,
      "successfulProbeCount": integer,
      "endpointInfo": {
        object ([EndpointInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.EndpointInfo))
      },
      "probingLatency": {
        object ([LatencyDistribution](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.LatencyDistribution))
      },
      "destinationEgressLocation": {
        object ([EdgeLocation](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.EdgeLocation))
      },
      "edgeResponses": [
        {
          object ([SingleEdgeResponse](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.SingleEdgeResponse))
        }
      ],
      "probedAllDevices": boolean
    }  
  
Fields  
---  
`result` |  `enum (`ProbingResult`)` The overall result of active probing.  
`verifyTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time that reachability was assessed through active probing.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`error` |  `object (`[Status](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.Status)`)` Details about an internal failure or the cancellation of active probing.  
`abortCause` |  `enum (`ProbingAbortCause`)` The reason probing was aborted.  
`sentProbeCount` |  `integer` Number of probes sent.  
`successfulProbeCount` |  `integer` Number of probes that reached the destination.  
`endpointInfo` |  `object (`[EndpointInfo](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.EndpointInfo)`)` The source and destination endpoints derived from the test input and used for active probing.  
`probingLatency` |  `object (`[LatencyDistribution](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.LatencyDistribution)`)` Latency as measured by active probing in one direction: from the source to the destination endpoint.  
`destinationEgressLocation` |  `object (`[EdgeLocation](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.EdgeLocation)`)` The EdgeLocation from which a packet, destined to the internet, will egress the Google network. This will only be populated for a connectivity test which has an internet destination address. The absence of this field _must not_ be used as an indication that the destination is part of the Google network.  
`edgeResponses[]` |  `object (`[SingleEdgeResponse](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.SingleEdgeResponse)`)` Probing results for all edge devices.  
`probedAllDevices` |  `boolean` Whether all relevant edge devices were probed.  
  
### LatencyDistribution

JSON representation  
---  
      
    
    {
      "latencyPercentiles": [
        {
          object ([LatencyPercentile](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.LatencyPercentile))
        }
      ]
    }  
  
Fields  
---  
`latencyPercentiles[]` |  `object (`[LatencyPercentile](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.LatencyPercentile)`)` Representative latency percentiles.  
  
### LatencyPercentile

JSON representation  
---  
      
    
    {
      "percent": integer,
      "latencyMicros": string
    }  
  
Fields  
---  
`percent` |  `integer` Percentage of samples this data point applies to.  
`latencyMicros` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` percent-th percentile of latency observed, in microseconds. Fraction of percent/100 of samples have latency lower or equal to the value of this field.  
  
### EdgeLocation

JSON representation  
---  
      
    
    {
      "metropolitanArea": string
    }  
  
Fields  
---  
`metropolitanArea` |  `string` Name of the metropolitan area.  
  
### SingleEdgeResponse

JSON representation  
---  
      
    
    {
      "result": enum (ProbingResult),
      "sentProbeCount": integer,
      "successfulProbeCount": integer,
      "probingLatency": {
        object ([LatencyDistribution](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.LatencyDistribution))
      },
      "destinationEgressLocation": {
        object ([EdgeLocation](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.EdgeLocation))
      },
      "destinationRouter": string
    }  
  
Fields  
---  
`result` |  `enum (`ProbingResult`)` The overall result of active probing for this egress device.  
`sentProbeCount` |  `integer` Number of probes sent.  
`successfulProbeCount` |  `integer` Number of probes that reached the destination.  
`probingLatency` |  `object (`[LatencyDistribution](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.LatencyDistribution)`)` Latency as measured by active probing in one direction: from the source to the destination endpoint.  
`destinationEgressLocation` |  `object (`[EdgeLocation](https://docs.cloud.google.com/network-intelligence-center/docs/reference/networkmanagement/mcp/tools_list/create_connectivity_test#Input.Schema.EdgeLocation)`)` The EdgeLocation from which a packet, destined to the internet, will egress the Google network. This will only be populated for a connectivity test which has an internet destination address. The absence of this field _must not_ be used as an indication that the destination is part of the Google network.  
`destinationRouter` |  `string` Router name in the format '{router}.{metroshard}'. For example: pf01.aaa01, pr02.aaa01.  
  
### Tool Annotations

Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-17 UTC."],[],[]] 
