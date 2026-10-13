---
url: https://docs.cloud.google.com/compute/docs/reference/rest/beta/networkEndpointGroups/aggregatedList/
title: Method: networkEndpointGroups.aggregatedList \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:09:24.439673+00:00
---

# Method: networkEndpointGroups.aggregatedList  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/beta/networkEndpointGroups/aggregatedList/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: networkEndpointGroups.aggregatedList Stay organized with collections  Save and categorize content based on your preferences. 

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



Retrieves the list of network endpoint groups and sorts them by zone.

To prevent failure, Google recommends that you set the `returnPartialSuccess` parameter to `true`.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/beta/projects/{project}/aggregated/networkEndpointGroups`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
  
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
`returnPartialSuccess` |  `boolean` Opt-in for partial success behavior which provides partial results in case of failure. The default value is false.For example, when partial success behavior is enabled, aggregatedList for a single zone scope either returns all resources in the zone or no resources, with an error code.  
`includeAllScopes` |  `boolean` Indicates whether every visible scope for each scope type (zone, region, global) should be included in the response. For new resource types added after this field, the flag has no effect as new resource types will always include every visible scope for each scope type in response. For resource types which predate this field, if this flag is omitted or false, only scopes of the scope types where the resource type is expected to be found will be included.  
`serviceProjectNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The Shared VPC service project id or service project number for which aggregated list request is invoked for subnetworks list-usable api.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "items": {
        string: {
          "networkEndpointGroups": [
            {
              "kind": string,
              "id": string,
              "creationTimestamp": string,
              "selfLink": string,
              "name": string,
              "description": string,
              "networkEndpointType": enum,
              "size": integer,
              "loadBalancer": {
                "zone": string,
                "network": string,
                "subnetwork": string,
                "defaultPort": integer
              },
              "region": string,
              "zone": string,
              "network": string,
              "subnetwork": string,
              "defaultPort": integer,
              "annotations": {
                string: string,
                ...
              },
              "cloudRun": {
                "service": string,
                "tag": string,
                "urlMask": string
              },
              "appEngine": {
                "service": string,
                "version": string,
                "urlMask": string
              },
              "cloudFunction": {
                "function": string,
                "urlMask": string
              },
              "serverlessDeployment": {
                "platform": string,
                "resource": string,
                "version": string,
                "urlMask": string
              },
              "pscTargetService": string,
              "pscData": {
                "consumerPscAddress": string,
                "pscConnectionId": string,
                "pscConnectionStatus": enum,
                "producerPort": integer
              }
            }
          ],
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
        },
        ...
      },
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
      },
      "unreachables": [
        string
      ]
    }  
  
Fields  
---  
`kind` |  `string` Output only. The resource type, which is always `compute#networkEndpointGroupAggregatedList` for aggregated lists of network endpoint groups.  
`id` |  `string` Output only. Unique identifier for the resource; defined by the server.  
`items` |  `map (key: string, value: object)` A list of NetworkEndpointGroupsScopedList resources.**Key:** The name of the scope that contains this set of network endpoint groups.  
`items.networkEndpointGroups[]` |  `object` Output only. The list of [network endpoint groups](https://docs.cloud.google.com/compute/docs/reference/rest/beta/networkEndpointGroups) that are contained in this scope.  
`items.networkEndpointGroups[].kind` |  `string` Output only. Type of the resource. Always `compute#networkEndpointGroup` for network endpoint group.  
`items.networkEndpointGroups[].id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`items.networkEndpointGroups[].creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`items.networkEndpointGroups[].selfLink` |  `string` Output only. Server-defined URL for the resource.  
`items.networkEndpointGroups[].name` |  `string` Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`items.networkEndpointGroups[].description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`items.networkEndpointGroups[].networkEndpointType` |  `enum` Type of network endpoints in this network endpoint group. Can be one of `GCE_VM_IP`, `GCE_VM_IP_PORT`, `NON_GCP_PRIVATE_IP_PORT`, `INTERNET_FQDN_PORT`, `INTERNET_IP_PORT`, `SERVERLESS`, `PRIVATE_SERVICE_CONNECT`, `GCE_VM_IP_PORTMAP`.  
`items.networkEndpointGroups[].size` |  `integer` Output only. Number of network endpoints in the network endpoint group.  
`items.networkEndpointGroups[].loadBalancer  
**(deprecated)**` |  `object` This field is only valid when the network endpoint group is used for load balancing. [Deprecated] This field is deprecated.  
`items.networkEndpointGroups[].loadBalancer  
**(deprecated)**.zone  
**(deprecated)**` |  `string` Output only. The URL of the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the network endpoint group is located. [Deprecated] This field is deprecated.  
`items.networkEndpointGroups[].loadBalancer  
**(deprecated)**.network  
**(deprecated)**` |  `string` The URL of the network to which all network endpoints in the NEG belong. For networkEndpointType `GCE_VM_IP_PORT`, `GCE_VM_IP_PORTMAP` or `NON_GCP_PRIVATE_IP_PORT`, if this field is not specified, a default network will be used. This field cannot be set for NEGs with networkEndpointType set to `SERVERLESS` or `PRIVATE_SERVICE_CONNECT` and for global NEGs. For all other network endpoint types, this field is required. [Deprecated] This field is deprecated.  
`items.networkEndpointGroups[].loadBalancer  
**(deprecated)**.subnetwork  
**(deprecated)**` |  `string` Optional URL of the subnetwork to which all network endpoints in the NEG belong. [Deprecated] This field is deprecated.  
`items.networkEndpointGroups[].loadBalancer  
**(deprecated)**.defaultPort  
**(deprecated)**` |  `integer` The default port used if the port number is not specified in the network endpoint.If the network endpoint type is either `GCE_VM_IP`, `SERVERLESS` or `PRIVATE_SERVICE_CONNECT`, this field must not be specified. [Deprecated] This field is deprecated.  
`items.networkEndpointGroups[].region` |  `string` Output only. The URL of the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the network endpoint group is located.  
`items.networkEndpointGroups[].zone` |  `string` Output only. The URL of the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the network endpoint group is located.  
`items.networkEndpointGroups[].network` |  `string` The URL of the network to which all network endpoints in the NEG belong. For networkEndpointType `GCE_VM_IP_PORT`, `GCE_VM_IP_PORTMAP` or `NON_GCP_PRIVATE_IP_PORT`, if this field is not specified, a default network will be used. This field cannot be set for NEGs with networkEndpointType set to `SERVERLESS` or `PRIVATE_SERVICE_CONNECT` and for global NEGs. For all other network endpoint types, this field is required.  
`items.networkEndpointGroups[].subnetwork` |  `string` Optional URL of the subnetwork to which all network endpoints in the NEG belong.  
`items.networkEndpointGroups[].defaultPort` |  `integer` The default port used if the port number is not specified in the network endpoint.Optional. If the network endpoint type is either `GCE_VM_IP`, `SERVERLESS` or `PRIVATE_SERVICE_CONNECT`, this field must not be specified.  
`items.networkEndpointGroups[].annotations` |  `map (key: string, value: string)` Optional. Metadata defined as annotations on the network endpoint group.  
`items.networkEndpointGroups[].cloudRun` |  `object` Optional. Only valid when `networkEndpointType` is `SERVERLESS`. Only one of `cloudRun`, `appEngine` or `cloudFunction` may be set.``  
`items.networkEndpointGroups[].cloudRun.service` |  `string` [Cloud Run service](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#backend-service) is the main resource of Cloud Run.The `service` must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).Example value: "run-service".  
`items.networkEndpointGroups[].cloudRun.tag` |  `string` Optional [Cloud Run tag](https://docs.cloud.google.com/load-balancing/docs/tags) represents the "named-revision" to provide additional fine-grained traffic routing information.The `tag` must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).Example value: "revision-0010".  
`items.networkEndpointGroups[].cloudRun.urlMask` |  `string` An [URL mask](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#url_masks) is one of the main components of the Cloud Function.A template to parse `<service>` and `<tag>` fields from a request URL. URL mask allows for routing to multiple Run services without having to create multiple network endpoint groups and backend services.For example, request URLs `foo1.domain.com/bar1` and `foo1.domain.com/bar2` can be backed by the same Serverless Network Endpoint Group (NEG) with URL mask `<tag>.domain.com/<service>`. The URL mask will parse them to `{ service="bar1", tag="foo1" }` and `{ service="bar2", tag="foo2" }` respectively.  
`items.networkEndpointGroups[].appEngine` |  `object` Optional. Only valid when `networkEndpointType` is `SERVERLESS`. Only one of `cloudRun`, `appEngine` or `cloudFunction` may be set.  
`items.networkEndpointGroups[].appEngine.service` |  `string` Optional serving [service](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services).The `service` name is case-sensitive and must be 1-63 characters long.Example value: `default`, `my-service`.  
`items.networkEndpointGroups[].appEngine.version` |  `string` Optional serving [version](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions).The `version` name is case-sensitive and must be 1-100 characters long.Example value: `v1`, `v2`.  
`items.networkEndpointGroups[].appEngine.urlMask` |  `string` An [URL mask](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#url_masks) is one of the main components of the Cloud Function.A template to parse `service` and `version` fields from a request URL. URL mask allows for routing to multiple App Engine services without having to create multiple Network Endpoint Groups and backend services.For example, the request URLs `foo1-dot-appname.appspot.com/v1` and `foo1-dot-appname.appspot.com/v2` can be backed by the same Serverless NEG with URL mask `<service>-dot-appname.appspot.com/<version>`. The URL mask will parse them to `{ service = "foo1", version = "v1" }` and `{ service = "foo1", version = "v2" }` respectively.  
`items.networkEndpointGroups[].cloudFunction` |  `object` Optional. Only valid when `networkEndpointType` is `SERVERLESS`. Only one of `cloudRun`, `appEngine` or `cloudFunction` may be set.  
`items.networkEndpointGroups[].cloudFunction.function` |  `string` A user-defined name of the [Cloud Function](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions).The `function` name is case-sensitive and must be 1-63 characters long.Example value: `func1`.  
`items.networkEndpointGroups[].cloudFunction.urlMask` |  `string` An [URL mask](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#url_masks) is one of the main components of the Cloud Function.A template to parse `function` field from a request URL. URL mask allows for routing to multiple Cloud Functions without having to create multiple Network Endpoint Groups and backend services.For example, request URLs `mydomain.com/function1` and `mydomain.com/function2` can be backed by the same Serverless NEG with URL mask `/<function>`. The URL mask will parse them to `{ function = "function1" }` and `{ function = "function2" }` respectively.  
`items.networkEndpointGroups[].serverlessDeployment` |  `object` Only valid when `networkEndpointType` is `SERVERLESS`. Only one of `cloudRun`, `appEngine`, `cloudFunction` or `serverlessDeployment` may be set.  
`items.networkEndpointGroups[].serverlessDeployment.platform` |  `string` The platform of the backend target(s) of this NEG. The only supported value is API Gateway: `apigateway.googleapis.com`.  
`items.networkEndpointGroups[].serverlessDeployment.resource` |  `string` The user-defined name of the workload/instance. This value must be provided explicitly or in the `urlMask`. The resource identified by this value is platform-specific and is as follows:

  1. API Gateway: The `gateway` ID
  2. App Engine: The `service` name
  3. Cloud Functions: The `function` name
  4. Cloud Run: The `service` name

  
`items.networkEndpointGroups[].serverlessDeployment.version` |  `string` The optional resource version. The version identified by this value is platform-specific and is follows:

  1. API Gateway: Unused
  2. App Engine: The service version
  3. Cloud Functions: Unused
  4. Cloud Run: The service tag

  
`items.networkEndpointGroups[].serverlessDeployment.urlMask` |  `string` An [URL mask](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#url_masks) is one of the main components of the Cloud Function.A template to parse platform-specific fields from a request URL. URL mask allows for routing to multiple resources on the same serverless platform without having to create multiple Network Endpoint Groups and backend resources. The fields parsed by this template are platform-specific and are as follows:

  1. API Gateway: The `gateway` ID
  2. App Engine: The `service` and `version`
  3. Cloud Functions: The `function` name
  4. Cloud Run: The `service` and `tag`

  
`items.networkEndpointGroups[].pscTargetService` |  `string` The target service url used to set up private service connection to a Google API or a PSC Producer Service Attachment. An example value is: `asia-northeast3-cloudkms.googleapis.com`.Optional. Only valid when `networkEndpointType` is `PRIVATE_SERVICE_CONNECT`.  
`items.networkEndpointGroups[].pscData` |  `object` Optional. Only valid when `networkEndpointType` is `PRIVATE_SERVICE_CONNECT`.  
`items.networkEndpointGroups[].pscData.consumerPscAddress` |  `string` Output only. Address allocated from given subnetwork for PSC. This IP address acts as a VIP for a PSC NEG, allowing it to act as an endpoint in L7 PSC-XLB.  
`items.networkEndpointGroups[].pscData.pscConnectionId` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The PSC connection id of the PSC Network Endpoint Group Consumer.  
`items.networkEndpointGroups[].pscData.pscConnectionStatus` |  `enum` Output only. The connection status of the PSC Forwarding Rule.  
`items.networkEndpointGroups[].pscData.producerPort` |  `integer` The psc producer port is used to connect PSC NEG with specific port on the PSC Producer side; should only be used for the PRIVATE_SERVICE_CONNECT NEG type  
`items.warning` |  `object` Output only. An informational warning that replaces the list of network endpoint groups when the list is empty.  
`items.warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`items.warning.message` |  `string` Output only. A human-readable description of the warning code.  
`items.warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`items.warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`items.warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`nextPageToken` |  `string` Output only. This token allows you to get the next page of results for list requests. If the number of results is larger than `maxResults`, use the `nextPageToken` as a value for the query parameter `pageToken` in the next list request. Subsequent list requests will have their own `nextPageToken` to continue paging through the results.  
`selfLink` |  `string` Output only. Server-defined URL for this resource.  
`warning` |  `object` Output only. Informational warning message.  
`warning.code` |  `enum` Output only. A warning code, if applicable. For example, Compute Engine returns `NO_RESULTS_ON_PAGE` if there are no results in the response.  
`warning.message` |  `string` Output only. A human-readable description of the warning code.  
`warning.data[]` |  `object` Output only. Metadata about this warning in `key: value` format. For example: 
    
    
    "data": [  {  "key": "scope",  "value": "zones/us-east1-d"  }]  
  
`warning.data[].key` |  `string` Output only. A key that provides more detail on the warning being returned. For example, for warnings where there are no results in a list request for a particular zone, this key might be `scope` and the key value might be the zone name. Other examples might be a key indicating a deprecated resource and a suggested replacement, or a warning about invalid network settings (for example, if an instance attempts to perform IP forwarding but is not enabled for IP forwarding).  
`warning.data[].value` |  `string` Output only. A warning data value corresponding to the key.  
`unreachables[]` |  `string` Output only. Unreachable resources.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/compute.readonly`
  * ` https://www.googleapis.com/auth/compute`
  * ` https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

In addition to any permissions specified on the fields above, authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions:

  * `compute.networkEndpointGroups.list`



To find predefined roles that contain those permissions, see [Compute Engine IAM Roles](https://docs.cloud.google.com/compute/docs/access/iam).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
