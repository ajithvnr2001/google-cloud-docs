---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/globalNetworkEndpointGroups/listNetworkEndpoints/
title: Method: globalNetworkEndpointGroups.listNetworkEndpoints \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:04:48.087682+00:00
---

# Method: globalNetworkEndpointGroups.listNetworkEndpoints  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/globalNetworkEndpointGroups/listNetworkEndpoints/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: globalNetworkEndpointGroups.listNetworkEndpoints Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Lists the network endpoints in the specified network endpoint group.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`POST https://compute.googleapis.com/compute/v1/projects/{project}/global/networkEndpointGroups/{networkEndpointGroup}/listNetworkEndpoints?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`networkEndpointGroup` |  `string` The name of the network endpoint group from which you want to generate a list of included network endpoints. It should comply with RFC1035.  
  
### Query parameters

Parameters  
---  
`maxResults` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The maximum number of results per page that should be returned. If the number of available results is larger than `maxResults`, Compute Engine returns a `nextPageToken` that can be used to get the next page of results in subsequent list requests. Acceptable values are `0` to `500`, inclusive. (Default: `500`)  
`pageToken` |  `string` Specifies a page token to use. Set `pageToken` to the `nextPageToken` returned by a previous list request to get the next page of results.  
`filter` |  `string` A filter expression that filters resources listed in the response. Most Compute resources support two types of filter expressions: expressions that support regular expressions and expressions that follow API improvement proposal [AIP-160](https://google.aip.dev/160). These two types of filter expressions cannot be mixed in one request.If you want to use AIP-160, your expression must specify the field name, an operator, and the value that you want to use for filtering. The value must be a string, a number, or a boolean. The operator must be either `=`, `!=`, `>`, `<`, `<=`, `>=` or `:`.For example, if you are filtering Compute Engine instances, you can exclude instances named `example-instance` by specifying `name != example-instance`.The `:*` comparison can be used to test whether a key has been defined. For example, to find all objects with `owner` label use:
    
    
    labels.owner:*
    

You can also filter nested fields. For example, you could specify `scheduling.automaticRestart = false` to include instances only if they are not scheduled for automatic restarts. You can use filtering on nested fields to filter based on [resource labels](https://docs.cloud.google.com/compute/docs/labeling-resources).To filter on multiple expressions, provide each separate expression within parentheses. For example:
    
    
    (scheduling.automaticRestart = true)
    (cpuPlatform = "Intel Skylake")
    

By default, each expression is an `AND` expression. However, you can include `AND` and `OR` expressions explicitly. For example:
    
    
    (cpuPlatform = "Intel Skylake") OR
    (cpuPlatform = "Intel Broadwell") AND
    (scheduling.automaticRestart = true)
    

If you want to use a regular expression, use the `eq` (equal) or `ne` (not equal) operator against a single un-parenthesized expression with or without quotes or against multiple parenthesized expressions. Examples:`fieldname eq unquoted literal` `fieldname eq 'single quoted literal'` `fieldname eq "double quoted literal"` `(fieldname1 eq literal) (fieldname2 ne "literal")`The literal value is interpreted as a regular expression using Google [RE2](https://github.com/google/re2/wiki/Syntax) library syntax. The literal value must match the entire field.For example, to filter for instances that do not end with name "instance", you would use `name ne .*instance`.You cannot combine constraints on multiple fields using regular expressions.  
`orderBy` |  `string` Sorts list results by a certain order. By default, results are returned in alphanumerical order based on the resource name.You can also sort results in descending order based on the creation timestamp using `orderBy="creationTimestamp desc"`. This sorts results based on the `creationTimestamp` field in reverse chronological order (newest result first). Use this to sort resources like operations so that the newest operation is returned first.Currently, only sorting by `name` or `creationTimestamp desc` is supported.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "items": [
        {
          "networkEndpoint": {
            "ipAddress": string,
            "ipv6Address": string,
            "fqdn": string,
            "port": integer,
            "clientDestinationPort": integer,
            "instance": string,
            "annotations": {
              string: string,
              ...
            }
          },
          "healths": [
            {
              "forwardingRule": {
                "forwardingRule": string
              },
              "backendService": {
                "backendService": string
              },
              "healthCheck": {
                "healthCheck": string
              },
              "healthCheckService": {
                "healthCheckService": string
              },
              "healthState": enum,
              "ipv6HealthState": enum
            }
          ]
        }
      ],
      "nextPageToken": string,
      "warning": {
        "code": enum,
        "message": string,
        "data": [
          {
            "key": string,
            "value": string
          }
        ]
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. The resource type, which is always `compute#networkEndpointGroupsListNetworkEndpoints` for the list of network endpoints in the specified network endpoint group.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items[]` |  `object` A list of NetworkEndpointWithHealthStatus resources.  
`items[].networkEndpoint` |  `object` Output only. The network endpoint.  
`items[].networkEndpoint.ipAddress` |  `string` Optional IPv4 address of network endpoint. The IP address must belong to a VM in Compute Engine (either the primary IP or as part of an aliased IP range). If the IP address is not specified, then the primary IP address for the VM instance in the network that the network endpoint group belongs to will be used.This field is redundant and need not be set for network endpoints of type `GCE_VM_IP`. If set, it must be set to the primary internal IP address of the attached VM instance that matches the subnetwork of the NEG. The primary internal IP address from any NIC of a multi-NIC VM instance can be added to a NEG as long as it matches the NEG subnetwork.  
`items[].networkEndpoint.ipv6Address` |  `string` Optional IPv6 address of network endpoint.  
`items[].networkEndpoint.fqdn` |  `string` Optional fully qualified domain name of network endpoint. This can only be specified when `NetworkEndpointGroup.network_endpoint_type` is `NON_GCP_FQDN_PORT`.  
`items[].networkEndpoint.port` |  `integer` Optional port number of network endpoint. If not specified, the defaultPort for the network endpoint group will be used.This field can not be set for network endpoints of type `GCE_VM_IP`.  
`items[].networkEndpoint.clientDestinationPort` |  `integer` Represents the port number to which PSC consumer sends packets.Optional. Only valid for network endpoint groups created with `GCE_VM_IP_PORTMAP` endpoint type.  
`items[].networkEndpoint.instance` |  `string` The name or a URL of VM instance of this network endpoint. Optional, the field presence depends on the network endpoint type. The field is required for network endpoints of type `GCE_VM_IP` and `GCE_VM_IP_PORT`.The instance must be in the same zone of network endpoint group (for zonal NEGs) or in the zone within the region of the NEG (for regional NEGs). If the `ipAddress` is specified, it must belongs to the VM instance.The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt) or be a valid URL pointing to an existing instance.  
`items[].networkEndpoint.annotations` |  `map (key: string, value: string)` Optional metadata defined as annotations on the network endpoint.  
`items[].healths[]` |  `object` Output only. The health status of network endpoint.Optional. Displayed only if the network endpoint has centralized health checking configured.  
`items[].healths[].forwardingRule` |  `object` URL of the forwarding rule associated with the health state of the network endpoint.  
`items[].healths[].forwardingRule.forwardingRule` |  `string`  
`items[].healths[].backendService` |  `object` URL of the backend service associated with the health state of the network endpoint.  
`items[].healths[].backendService.backendService` |  `string`  
`items[].healths[].healthCheck` |  `object` URL of the health check associated with the health state of the network endpoint.  
`items[].healths[].healthCheck.healthCheck` |  `string`  
`items[].healths[].healthCheckService` |  `object` URL of the health check service associated with the health state of the network endpoint.  
`items[].healths[].healthCheckService.healthCheckService` |  `string`  
`items[].healths[].healthState` |  `enum` Health state of the network endpoint determined based on the health checks configured.  
`items[].healths[].ipv6HealthState` |  `enum` Health state of the ipv6 network endpoint determined based on the health checks configured.  
`nextPageToken` |  `string` Output only. This token allows you to get the next page of results for list requests. If the number of results is larger than `maxResults`, use the `nextPageToken` as a value for the query parameter `pageToken` in the next list request. Subsequent list requests will have their own `nextPageToken` to continue paging through the results.  
`warning` |  `object` Output only. Informational warning message.  
`warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`warning.message` |  `string` Output only. A human-readable description of the warning code.  
`warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.globalNetworkEndpointGroups.get`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
