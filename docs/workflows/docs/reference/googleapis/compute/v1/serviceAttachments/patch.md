---
url: https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/v1/serviceAttachments/patch/
title: Method: googleapis.compute.v1.serviceAttachments.patch \u00a0|\u00a0 Workflows \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:54:13.349934+00:00
---

# Method: googleapis.compute.v1.serviceAttachments.patch  |  Workflows  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/v1/serviceAttachments/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Workflows ](https://docs.cloud.google.com/workflows/docs)
  * [ Reference ](https://docs.cloud.google.com/workflows/docs/apis)



Send feedback 

#  Method: googleapis.compute.v1.serviceAttachments.patch Stay organized with collections  Save and categorize content based on your preferences. 

Patches the specified ServiceAttachment resource with the data included in the request. This method supports PATCH semantics and uses JSON merge patch format and processing rules.

This method waits—the workflow execution is paused—until the operation is complete, fails, or times out. The default timeout value is `1800` seconds (30 minutes) and can be changed to a maximum value of `31536000` seconds (one year) for long-running operations using the `connector_params` field. See the [Connectors reference](https://docs.cloud.google.com/workflows/docs/reference/googleapis).

The connector uses polling to monitor the long-running operation, which might generate additional billable steps. For more information about retries and long-running operations, refer to [Understand connectors](https://docs.cloud.google.com/workflows/docs/connectors).

The polling policy for the long-running operation can be configured. To set the connector-specific parameters (`connector_params`), refer to [Invoke a connector call](https://docs.cloud.google.com/workflows/docs/reference/googleapis#invoke_a_connector_call).

## Arguments

Parameters  
---  
`project` |  `string` Required. Project ID for this request.  
`region` |  `string` Required. The region scoping this request and should conform to RFC1035.  
`serviceAttachment` |  `string` Required. The resource id of the ServiceAttachment to patch. It should conform to RFC1035 resource name or be a string form on an unsigned long number.  
`requestId` |  `string` An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments. The request ID must be a valid UUID with the exception that zero UUID is not supported ( 00000000-0000-0000-0000-000000000000).  
`body` |  `object ([ServiceAttachment](https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/v1/Overview#ServiceAttachment))` Required.  
  
## Raised exceptions

Exceptions  
---  
`ConnectionError` | In case of a network problem (such as DNS failure or refused connection).  
`HttpError` | If the response status is >= 400 (excluding 429 and 503).  
`TimeoutError` | If a long-running operation takes longer to finish than the specified timeout limit.  
`TypeError` | If an operation or function receives an argument of the wrong type.  
`ValueError` | If an operation or function receives an argument of the right type but an inappropriate value. For example, a negative timeout.  
`OperationError` | If the long-running operation finished unsuccessfully.  
`ResponseTypeError` | If the long-running operation returned a response of the wrong type.  
  
## Response

If successful, the response contains an instance of [`Operation`](https://docs.cloud.google.com/workflows/docs/reference/googleapis/compute/v1/Overview#Operation).

## Subworkflow snippet

Some fields might be optional or required. To identify required fields, refer to the [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/serviceAttachments/patch).

### YAML
    
    
    - patch:
        call: googleapis.compute.v1.serviceAttachments.patch
        args:
            project: ...
            region: ...
            serviceAttachment: ...
            requestId: ...
            body:
                connectionPreference: ...
                consumerAcceptLists: ...
                consumerRejectLists: ...
                description: ...
                domainNames: ...
                enableProxyProtocol: ...
                fingerprint: ...
                name: ...
                natSubnets: ...
                producerForwardingRule: ...
                reconcileConnections: ...
                targetService: ...
        result: patchResult

### JSON
    
    
    [
      {
        "patch": {
          "call": "googleapis.compute.v1.serviceAttachments.patch",
          "args": {
            "project": "...",
            "region": "...",
            "serviceAttachment": "...",
            "requestId": "...",
            "body": {
              "connectionPreference": "...",
              "consumerAcceptLists": "...",
              "consumerRejectLists": "...",
              "description": "...",
              "domainNames": "...",
              "enableProxyProtocol": "...",
              "fingerprint": "...",
              "name": "...",
              "natSubnets": "...",
              "producerForwardingRule": "...",
              "reconcileConnections": "...",
              "targetService": "..."
            }
          },
          "result": "patchResult"
        }
      }
    ]

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
