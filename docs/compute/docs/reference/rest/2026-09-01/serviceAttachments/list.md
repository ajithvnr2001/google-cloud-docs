---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/serviceAttachments/list/
title: Method: serviceAttachments.list \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:41:31.249045+00:00
---

# Method: serviceAttachments.list  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/serviceAttachments/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: serviceAttachments.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
      * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Lists the ServiceAttachments for a project in the given scope.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/regions/{region}/serviceAttachments?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`region` |  `string` Name of the region of this request.  
  
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
          "kind": string,
          "id": string,
          "creationTimestamp": string,
          "name": string,
          "description": string,
          "selfLink": string,
          "region": string,
          "producerForwardingRule": string,
          "targetService": string,
          "connectionPreference": enum,
          "connectedEndpoints": [
            {
              "status": enum,
              "pscConnectionId": string,
              "endpoint": string,
              "endpointWithId": string,
              "consumerNetwork": string,
              "propagatedConnectionCount": integer,
              "natIps": [
                string
              ]
            }
          ],
          "natSubnets": [
            string
          ],
          "enableProxyProtocol": boolean,
          "consumerRejectLists": [
            string
          ],
          "consumerAcceptLists": [
            {
              "projectIdOrNum": string,
              "networkUrl": string,
              "endpointUrl": string,
              "connectionLimit": integer
            }
          ],
          "pscServiceAttachmentId": {
            "high": string,
            "low": string
          },
          "fingerprint": string,
          "domainNames": [
            string
          ],
          "reconcileConnections": boolean,
          "propagatedConnectionLimit": integer,
          "metadata": {
            string: string,
            ...
          },
          "natIpsPerEndpoint": integer
        }
      ],
      "nextPageToken": string,
      "selfLink": string,
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
`kind` |  `string` Output only. Type of the resource. Always `compute#serviceAttachment` for service attachments.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items[]` |  `object` A list of ServiceAttachment resources.  
`items[].kind` |  `string` Output only. Type of the resource. Always `compute#serviceAttachment` for service attachments.  
`items[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource type. The server generates this identifier.  
`items[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items[].name` |  `string` Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`items[].description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`items[].selfLink` |  `string` Output only. Server-defined URL for the resource.  
`items[].region` |  `string` Output only. URL of the region where the service attachment resides. This field applies only to the region resource. You must specify this field as part of the HTTP request URL. It is not settable as a field in the request body.  
`items[].producerForwardingRule  
**(deprecated)**` |  `string` The URL of a forwarding rule with loadBalancingScheme INTERNAL* that is serving the endpoint identified by this service attachment.  
`items[].targetService` |  `string` The URL of a service serving the endpoint identified by this service attachment.  
`items[].connectionPreference` |  `enum` The connection preference of service attachment. The value can be set to `ACCEPT_AUTOMATIC`. An `ACCEPT_AUTOMATIC` service attachment is one that always accepts the connection from consumer forwarding rules.  
`items[].connectedEndpoints[]` |  `object` Output only. An array of connections for all the consumers connected to this service attachment.  
`items[].connectedEndpoints[].status` |  `enum` The status of a connected endpoint to this service attachment.  
`items[].connectedEndpoints[].pscConnectionId` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` The PSC connection id of the connected endpoint.  
`items[].connectedEndpoints[].endpoint` |  `string` The url of a connected endpoint.  
`items[].connectedEndpoints[].endpointWithId` |  `string` The url of a connected endpoint with resource id.  
`items[].connectedEndpoints[].consumerNetwork` |  `string` The url of the consumer network.  
`items[].connectedEndpoints[].propagatedConnectionCount` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The number of consumer Network Connectivity Center spokes that the connected Private Service Connect endpoint has propagated to.  
`items[].connectedEndpoints[].natIps[]` |  `string` NAT IPs of the connected PSC endpoint and those of other endpoints propagated from it.  
`items[].natSubnets[]` |  `string` An array of URLs where each entry is the URL of a subnet provided by the service producer to use for NAT in this service attachment.  
`items[].enableProxyProtocol` |  `boolean` If true, enable the proxy protocol which is for supplying client TCP/IP address data in TCP connections that traverse proxies on their way to destination servers.  
`items[].consumerRejectLists[]` |  `string` Specifies a list of projects or networks that are not allowed to connect to this service attachment. The project can be specified using its project ID or project number and the network can be specified using its URL. A given service attachment can manage connections at either the project or network level. Therefore, both the reject and accept lists for a given service attachment must contain either only projects or only networks.  
`items[].consumerAcceptLists[]` |  `object` Specifies which consumer projects or networks are allowed to connect to the service attachment. Each project or network has a connection limit. A given service attachment can manage connections at either the project or network level. Therefore, both the accept and reject lists for a given service attachment must contain either only projects or only networks or only endpoints.  
`items[].consumerAcceptLists[].projectIdOrNum` |  `string` The project id or number for the project to set the limit for.  
`items[].consumerAcceptLists[].networkUrl` |  `string` The network URL for the network to set the limit for.  
`items[].consumerAcceptLists[].endpointUrl` |  `string` The URL for the PSC endpoint to accept  
`items[].consumerAcceptLists[].connectionLimit` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The value of the limit to set. For endpointUrl, the limit should be no more than 1.  
`items[].pscServiceAttachmentId` |  `object` Output only. An 128-bit global unique ID of the PSC service attachment.  
`items[].pscServiceAttachmentId.high` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)`  
`items[].pscServiceAttachmentId.low` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)`  
`items[].fingerprint` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking. This field will be ignored when inserting a `ServiceAttachment`. An up-to-date fingerprint must be provided in order to patch/update the ServiceAttachment; otherwise, the request will fail with error `412 conditionNotMet`. To see the latest fingerprint, make a `get()` request to retrieve the ServiceAttachment.A base64-encoded string.  
`items[].domainNames[]` |  `string` If specified, the domain name will be used during the integration between the PSC connected endpoints and the Cloud DNS. For example, this is a valid domain name: "p.mycompany.com.". Current max number of domain names supported is 1.  
`items[].reconcileConnections` |  `boolean` This flag determines whether a consumer accept/reject list change can reconcile the statuses of existing ACCEPTED or REJECTED PSC endpoints. 

  * If false, connection policy update will only affect existing PENDING PSC endpoints. Existing ACCEPTED/REJECTED endpoints will remain untouched regardless how the connection policy is modified .
  * If true, update will affect both PENDING and ACCEPTED/REJECTED PSC endpoints. For example, an ACCEPTED PSC endpoint will be moved to REJECTED if its project is added to the reject list.

For newly created service attachment, this boolean defaults to false.   
`items[].propagatedConnectionLimit` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The number of consumer spokes that connected Private Service Connect endpoints can be propagated to through Network Connectivity Center. This limit lets the service producer limit how many propagated Private Service Connect connections can be established to this service attachment from a single consumer.If the connection preference of the service attachment is ACCEPT_MANUAL, the limit applies to each project or network that is listed in the consumer accept list. If the connection preference of the service attachment is ACCEPT_AUTOMATIC, the limit applies to each project that contains a connected endpoint.If unspecified, the default propagated connection limit is 250.  
`items[].metadata` |  `map (key: string, value: string)` Metadata of the service attachment.  
`items[].natIpsPerEndpoint` |  `integer ([uint32](https://developers.google.com/discovery/v1/type-format) format)` The number of NAT IP addresses to be allocated per connected endpoint. If not specified, the default value is 1.  
`nextPageToken` |  `string` Output only. This token allows you to get the next page of results for list requests. If the number of results is larger than `maxResults`, use the `nextPageToken` as a value for the query parameter `pageToken` in the next list request. Subsequent list requests will have their own `nextPageToken` to continue paging through the results.  
`selfLink` |  `string` Output only. Server-defined URL for this resource.  
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

  * `compute.serviceAttachments.list`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-01 UTC."],[],[]] 
