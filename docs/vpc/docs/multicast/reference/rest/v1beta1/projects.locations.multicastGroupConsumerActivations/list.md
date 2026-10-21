---
url: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupConsumerActivations/list/
title: Method: projects.locations.multicastGroupConsumerActivations.list \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:29:08.656788+00:00
---

# Method: projects.locations.multicastGroupConsumerActivations.list  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupConsumerActivations/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Reference ](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest)



Send feedback 

#  Method: projects.locations.multicastGroupConsumerActivations.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation



Lists multicast group consumer activations in a given project and location.

### HTTP request

`GET https://networkservices.googleapis.com/v1beta1/{parent=projects/*/locations/*}/multicastGroupConsumerActivations`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource for which to list multicast group consumer activations. Use the following format: `projects/*/locations/*`.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. The maximum number of multicast group consumer activations to return per call.  
`pageToken` |  `string` Optional. A page token from an earlier query, as returned in `nextPageToken`.  
`filter` |  `string` Optional. A filter expression that filters the resources listed in the response. The expression must be of the form `<field> <operator> <value>` where operators: `<`, `>`, `<=`, `>=`, `!=`, `=`, `:` are supported (colon `:` represents a HAS operator which is roughly synonymous with equality).  can refer to a proto or JSON field, or a synthetic field. Field names can be camelCase or snake_case.Examples: * Filter by name: name = "RESOURCE_NAME" * Filter by labels: * Resources that have a key named `foo` labels.foo:* * Resources that have a key named `foo` whose value is `bar` labels.foo = bar  
`orderBy` |  `string` Optional. A field used to sort the results by a certain order.  
  
### Request body

The request body must be empty.

### Response body

Response message for `[multicastGroupConsumerActivations.list](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupConsumerActivations/list#google.cloud.networkservices.v1beta1.MulticastService.ListMulticastGroupConsumerActivations)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "multicastGroupConsumerActivations": [
        {
          object ([MulticastGroupConsumerActivation](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupConsumerActivations#MulticastGroupConsumerActivation))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`multicastGroupConsumerActivations[]` |  `object (`[MulticastGroupConsumerActivation](https://docs.cloud.google.com/vpc/docs/multicast/reference/rest/v1beta1/projects.locations.multicastGroupConsumerActivations#MulticastGroupConsumerActivation)`)` The list of multicast group consumer activations.  
`nextPageToken` |  `string` A page token from an earlier query, as returned in `nextPageToken`.  
`unreachable[]` |  `string` Locations that could not be reached.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-22 UTC."],[],[]] 
