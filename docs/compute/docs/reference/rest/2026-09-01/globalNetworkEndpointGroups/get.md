---
url: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/globalNetworkEndpointGroups/get/
title: Method: globalNetworkEndpointGroups.get \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:04:44.302915+00:00
---

# Method: globalNetworkEndpointGroups.get  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/reference/rest/2026-09-01/globalNetworkEndpointGroups/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  Method: globalNetworkEndpointGroups.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



API Version : 2026-09-01

Returns the specified network endpoint group.

### HTTP request

Choose an endpoint:

globalafrica-south1asia-east1asia-east2asia-northeast1asia-northeast2asia-northeast3asia-south1asia-south2asia-southeast1asia-southeast2asia-southeast3australia-southeast1australia-southeast2europe-central2europe-north1europe-north2europe-southwest1europe-west1europe-west10europe-west12europe-west2europe-west3europe-west4europe-west6europe-west8europe-west9me-central1me-central2me-west1northamerica-northeast1northamerica-northeast2northamerica-south1southamerica-east1southamerica-west1us-central1us-east1us-east4us-east5us-south1us-west1us-west2us-west3us-west4

  
`GET https://compute.googleapis.com/compute/v1/projects/{project}/global/networkEndpointGroups/{networkEndpointGroup}?$apiVersion=2026-09-01`

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`project` |  `string` Project ID for this request.  
`networkEndpointGroup` |  `string` The name of the network endpoint group. It should comply with RFC1035.  
  
### Request body

The request body must be empty.

### Response body

Represents a collection of network endpoints.

A network endpoint group (NEG) defines how a set of endpoints should be reached, whether they are reachable, and where they are located. For more information about using NEGs for different use cases, see [Network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs).

Note: Use the following APIs to manage network endpoint groups: 

  * To manage NEGs with zonal scope (such as zonal NEGs, hybrid connectivity NEGs): [zonal API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networkEndpointGroups/insert)
  * To manage NEGs with regional scope (such as regional internet NEGs, serverless NEGs, Private Service Connect NEGs): [regional API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionNetworkEndpointGroups/insert)
  * To manage NEGs with global scope (such as global internet NEGs): [global API](https://docs.cloud.google.com/compute/docs/reference/rest/v1/globalNetworkEndpointGroups/insert)



If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "kind": string,
      "id": string,
      "creationTimestamp": string,
      "selfLink": string,
      "name": string,
      "description": string,
      "networkEndpointType": enum,
      "size": integer,
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
      "pscTargetService": string,
      "pscData": {
        "consumerPscAddress": string,
        "pscConnectionId": string,
        "pscConnectionStatus": enum,
        "producerPort": integer
      }
    }  
  
Fields  
---  
`kind` |  `string` Output only. Type of the resource. Always `compute#networkEndpointGroup` for network endpoint group.  
`id` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The unique identifier for the resource. This identifier is defined by the server.  
`creationTimestamp` |  `string` Output only. Creation timestamp in [RFC3339](https://www.ietf.org/rfc/rfc3339.txt) text format.  
`selfLink` |  `string` Output only. Server-defined URL for the resource.  
`name` |  `string` Name of the resource; provided by the client when the resource is created. The name must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Specifically, the name must be 1-63 characters long and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` which means the first character must be a lowercase letter, and all following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be a dash.  
`description` |  `string` An optional description of this resource. Provide this property when you create the resource.  
`networkEndpointType` |  `enum` Type of network endpoints in this network endpoint group. Can be one of `GCE_VM_IP`, `GCE_VM_IP_PORT`, `NON_GCP_PRIVATE_IP_PORT`, `INTERNET_FQDN_PORT`, `INTERNET_IP_PORT`, `SERVERLESS`, `PRIVATE_SERVICE_CONNECT`, `GCE_VM_IP_PORTMAP`.  
`size` |  `integer` Output only. Number of network endpoints in the network endpoint group.  
`region` |  `string` Output only. The URL of the [region](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the network endpoint group is located.  
`zone` |  `string` Output only. The URL of the [zone](https://docs.cloud.google.com/compute/docs/regions-zones#available) where the network endpoint group is located.  
`network` |  `string` The URL of the network to which all network endpoints in the NEG belong. For networkEndpointType `GCE_VM_IP_PORT`, `GCE_VM_IP_PORTMAP` or `NON_GCP_PRIVATE_IP_PORT`, if this field is not specified, a default network will be used. This field cannot be set for NEGs with networkEndpointType set to `SERVERLESS` or `PRIVATE_SERVICE_CONNECT` and for global NEGs. For all other network endpoint types, this field is required.  
`subnetwork` |  `string` Optional URL of the subnetwork to which all network endpoints in the NEG belong.  
`defaultPort` |  `integer` The default port used if the port number is not specified in the network endpoint.Optional. If the network endpoint type is either `GCE_VM_IP`, `SERVERLESS` or `PRIVATE_SERVICE_CONNECT`, this field must not be specified.  
`annotations` |  `map (key: string, value: string)` Optional. Metadata defined as annotations on the network endpoint group.  
`cloudRun` |  `object` Optional. Only valid when `networkEndpointType` is `SERVERLESS`. Only one of `cloudRun`, `appEngine` or `cloudFunction` may be set.``  
`cloudRun.service` |  `string` [Cloud Run service](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#backend-service) is the main resource of Cloud Run.The `service` must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).Example value: "run-service".  
`cloudRun.tag` |  `string` Optional [Cloud Run tag](https://docs.cloud.google.com/load-balancing/docs/tags) represents the "named-revision" to provide additional fine-grained traffic routing information.The `tag` must be 1-63 characters long, and comply with [RFC1035](https://www.ietf.org/rfc/rfc1035.txt).Example value: "revision-0010".  
`cloudRun.urlMask` |  `string` An [URL mask](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#url_masks) is one of the main components of the Cloud Function.A template to parse `<service>` and `<tag>` fields from a request URL. URL mask allows for routing to multiple Run services without having to create multiple network endpoint groups and backend services.For example, request URLs `foo1.domain.com/bar1` and `foo1.domain.com/bar2` can be backed by the same Serverless Network Endpoint Group (NEG) with URL mask `<tag>.domain.com/<service>`. The URL mask will parse them to `{ service="bar1", tag="foo1" }` and `{ service="bar2", tag="foo2" }` respectively.  
`appEngine` |  `object` Optional. Only valid when `networkEndpointType` is `SERVERLESS`. Only one of `cloudRun`, `appEngine` or `cloudFunction` may be set.  
`appEngine.service` |  `string` Optional serving [service](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services).The `service` name is case-sensitive and must be 1-63 characters long.Example value: `default`, `my-service`.  
`appEngine.version` |  `string` Optional serving [version](https://docs.cloud.google.com/appengine/docs/admin-api/reference/rest/v1/apps.services.versions).The `version` name is case-sensitive and must be 1-100 characters long.Example value: `v1`, `v2`.  
`appEngine.urlMask` |  `string` An [URL mask](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#url_masks) is one of the main components of the Cloud Function.A template to parse `service` and `version` fields from a request URL. URL mask allows for routing to multiple App Engine services without having to create multiple Network Endpoint Groups and backend services.For example, the request URLs `foo1-dot-appname.appspot.com/v1` and `foo1-dot-appname.appspot.com/v2` can be backed by the same Serverless NEG with URL mask `<service>-dot-appname.appspot.com/<version>`. The URL mask will parse them to `{ service = "foo1", version = "v1" }` and `{ service = "foo1", version = "v2" }` respectively.  
`cloudFunction` |  `object` Optional. Only valid when `networkEndpointType` is `SERVERLESS`. Only one of `cloudRun`, `appEngine` or `cloudFunction` may be set.  
`cloudFunction.function` |  `string` A user-defined name of the [Cloud Function](https://docs.cloud.google.com/functions/docs/reference/rest/v1/projects.locations.functions).The `function` name is case-sensitive and must be 1-63 characters long.Example value: `func1`.  
`cloudFunction.urlMask` |  `string` An [URL mask](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts#url_masks) is one of the main components of the Cloud Function.A template to parse `function` field from a request URL. URL mask allows for routing to multiple Cloud Functions without having to create multiple Network Endpoint Groups and backend services.For example, request URLs `mydomain.com/function1` and `mydomain.com/function2` can be backed by the same Serverless NEG with URL mask `/<function>`. The URL mask will parse them to `{ function = "function1" }` and `{ function = "function2" }` respectively.  
`pscTargetService` |  `string` The target service url used to set up private service connection to a Google API or a PSC Producer Service Attachment. An example value is: `asia-northeast3-cloudkms.googleapis.com`.Optional. Only valid when `networkEndpointType` is `PRIVATE_SERVICE_CONNECT`.  
`pscData` |  `object` Optional. Only valid when `networkEndpointType` is `PRIVATE_SERVICE_CONNECT`.  
`pscData.consumerPscAddress` |  `string` Output only. Address allocated from given subnetwork for PSC. This IP address acts as a VIP for a PSC NEG, allowing it to act as an endpoint in L7 PSC-XLB.  
`pscData.pscConnectionId` |  `string ([uint64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The PSC connection id of the PSC Network Endpoint Group Consumer.  
`pscData.pscConnectionStatus` |  `enum` Output only. The connection status of the PSC Forwarding Rule.  
`pscData.producerPort` |  `integer` The psc producer port is used to connect PSC NEG with specific port on the PSC Producer side; should only be used for the PRIVATE_SERVICE_CONNECT NEG type  
  
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
