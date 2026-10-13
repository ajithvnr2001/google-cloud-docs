---
url: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments
title: REST Resource: organizations.endpointAttachments \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:54:41.133721+00:00
---

# REST Resource: organizations.endpointAttachments  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  REST Resource: organizations.endpointAttachments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: EndpointAttachment
    * JSON representation
  * ConnectionState
  * Methods



## Resource: EndpointAttachment

Apigee endpoint attachment. For more information, see [Southbound networking patterns](https://cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints).

JSON representation  
---  
      
    
    {
      "name": string,
      "location": string,
      "host": string,
      "state": enum (State),
      "connectionState": enum ([ConnectionState](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments#ConnectionState)),
    
      // Union field destination can be only one of the following:
      "serviceAttachment": string
      // End of list of possible types for union field destination.
    }  
  
Fields  
---  
`name` |  `string` Name of the endpoint attachment. Use the following structure in your request: `organizations/{org}/endpointAttachments/{endpointAttachment}`  
`location` |  `string` Required. Location of the endpoint attachment.  
`host` |  `string` Output only. Host that can be used in either the HTTP target endpoint directly or as the host in target server.  
`state` |  `enum (`State`)` Output only. State of the endpoint attachment. Values other than `ACTIVE` mean the resource is not ready to use.  
`connectionState` |  `enum (`[ConnectionState](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments#ConnectionState)`)` Output only. State of the endpoint attachment connection to the service attachment.  
Union field `destination`.`destination` can be only one of the following:  
`serviceAttachment` |  `string` Format: projects/*/regions/*/serviceAttachments/*  
  
## ConnectionState

The connection state for the underlying connectivity of the Endpoint Attachment. Values may be added to this enum in the future. Clients should be prepared to handle new, unrecognized enum values.

Enums  
---  
`CONNECTION_STATE_UNSPECIFIED` | The connection state has not been set.  
`UNAVAILABLE` | The connection state is unavailable at this time, possibly because the endpoint attachment is currently being provisioned.  
`PENDING` | The connection is pending acceptance by the PSC producer.  
`ACCEPTED` | The connection has been accepted by the PSC producer.  
`REJECTED` | The connection has been rejected by the PSC producer.  
`CLOSED` | The connection has been closed by the PSC producer and will not serve traffic going forward.  
`FROZEN` | The connection has been frozen by the PSC producer and will not serve traffic.  
`NEEDS_ATTENTION` | The connection has been accepted by the PSC producer, but it is not ready to serve the traffic due to producer side issues.  
`ACCEPTED_LIMITED_CAPACITY` | The connection has been accepted by the PSC producer, but it will only serve capacity limited traffic. The producer needs to take further actions to increase capacity for this connection.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments/create)`

|  Creates an endpoint attachment.  
  
### `[delete](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments/delete)`

|  Deletes an endpoint attachment.  
  
### `[get](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments/get)`

|  Gets the endpoint attachment.  
  
### `[list](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments/list)`

|  Lists the endpoint attachments in an organization.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
