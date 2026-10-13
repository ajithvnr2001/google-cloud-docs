---
url: https://docs.cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.appConnectors/resolveInstanceConfig/
title: Method: projects.locations.appConnectors.resolveInstanceConfig \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:04:29.040901+00:00
---

# Method: projects.locations.appConnectors.resolveInstanceConfig  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.appConnectors/resolveInstanceConfig/




#  Method: projects.locations.appConnectors.resolveInstanceConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * AppConnectorInstanceConfig
    * JSON representation
  * NotificationConfig
    * JSON representation
  * CloudPubSubNotificationConfig
    * JSON representation
  * ImageConfig
    * JSON representation
  * Try it!



Gets instance configuration for a given AppConnector. An internal method called by a AppConnector to get its container config.

### HTTP request

`GET https://beyondcorp.googleapis.com/v1/{appConnector=projects/*/locations/*/appConnectors/*}:resolveInstanceConfig`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`appConnector` |  `string` Required. BeyondCorp AppConnector name using the form: `projects/{projectId}/locations/{locationId}/appConnectors/{appConnector}` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `appConnector`:

  * `beyondcorp.appConnectors.list`

  
  
### Request body

The request body must be empty.

### Response body

Response message for BeyondCorp.ResolveInstanceConfig.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "instanceConfig": {
        object ([AppConnectorInstanceConfig](https://docs.cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.appConnectors/resolveInstanceConfig#AppConnectorInstanceConfig))
      }
    }  
  
Fields  
---  
`instanceConfig` |  `object (`[AppConnectorInstanceConfig](https://docs.cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.appConnectors/resolveInstanceConfig#AppConnectorInstanceConfig)`)` AppConnectorInstanceConfig.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## AppConnectorInstanceConfig

AppConnectorInstanceConfig defines the instance config of a AppConnector.

JSON representation  
---  
      
    
    {
      "sequenceNumber": string,
      "instanceConfig": {
        "@type": string,
        field1: ...,
        ...
      },
      "notificationConfig": {
        object ([NotificationConfig](https://docs.cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.appConnectors/resolveInstanceConfig#NotificationConfig))
      },
      "imageConfig": {
        object ([ImageConfig](https://docs.cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.appConnectors/resolveInstanceConfig#ImageConfig))
      }
    }  
  
Fields  
---  
`sequenceNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Required. A monotonically increasing number generated and maintained by the API provider. Every time a config changes in the backend, the sequenceNumber should be bumped up to reflect the change.  
`instanceConfig` |  `object` The SLM instance agent configuration.An object containing fields of an arbitrary type. An additional field `"@type"` contains a URI identifying the type. Example: `{ "id": 1234, "@type": "types.example.com/standard/id" }`.  
`notificationConfig` |  `object (`[NotificationConfig](https://docs.cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.appConnectors/resolveInstanceConfig#NotificationConfig)`)` NotificationConfig defines the notification mechanism that the remote instance should subscribe to in order to receive notification.  
`imageConfig` |  `object (`[ImageConfig](https://docs.cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.appConnectors/resolveInstanceConfig#ImageConfig)`)` ImageConfig defines the GCR images to run for the remote agent's control plane.  
  
## NotificationConfig

NotificationConfig defines the mechanisms to notify instance agent.

JSON representation  
---  
      
    
    {
    
      // Union field config can be only one of the following:
      "pubsubNotification": {
        object ([CloudPubSubNotificationConfig](https://docs.cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.appConnectors/resolveInstanceConfig#CloudPubSubNotificationConfig))
      }
      // End of list of possible types for union field config.
    }  
  
Fields  
---  
Union field `config`.`config` can be only one of the following:  
`pubsubNotification` |  `object (`[CloudPubSubNotificationConfig](https://docs.cloud.google.com/beyondcorp/docs/reference/rest/v1/projects.locations.appConnectors/resolveInstanceConfig#CloudPubSubNotificationConfig)`)` Cloud Pub/Sub Configuration to receive notifications.  
  
## CloudPubSubNotificationConfig

The configuration for Pub/Sub messaging for the AppConnector.

JSON representation  
---  
      
    
    {
      "pubsubSubscription": string
    }  
  
Fields  
---  
`pubsubSubscription` |  `string` The Pub/Sub subscription the AppConnector uses to receive notifications.  
  
## ImageConfig

ImageConfig defines the control plane images to run.

JSON representation  
---  
      
    
    {
      "targetImage": string,
      "stableImage": string
    }  
  
Fields  
---  
`targetImage` |  `string` The initial image the remote agent will attempt to run for the control plane. Format would be a gcr image path, e.g.: gcr.io/PROJECT-ID/my-image:tag1  
`stableImage` |  `string` The stable image that the remote agent will fallback to if the target image fails. Format would be a gcr image path, e.g.: gcr.io/PROJECT-ID/my-image:tag1  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-20 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-20 UTC."],[],[]] 
