---
url: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1
title: Package com.google.events.cloud.beyondcorp.appconnectors.v1 (0.16.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:49:59.286097+00:00
---

# Package com.google.events.cloud.beyondcorp.appconnectors.v1 (0.16.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Package com.google.events.cloud.beyondcorp.appconnectors.v1 (0.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 0.16.0 (latest) ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1)
  * [ 0.15.0 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.15.0/com.google.events.cloud.beyondcorp.appconnectors.v1)
  * [ 0.14.1 ](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/0.14.1/com.google.events.cloud.beyondcorp.appconnectors.v1)



## Classes 

### [AppConnector](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.AppConnector)

A BeyondCorp connector resource that represents an application facing component deployed proximal to and with direct access to the application instances. It is used to establish connectivity between the remote enterprise environment and GCP. It initiates connections to the applications and can proxy the data from users over the connection.

Protobuf type `google.events.cloud.beyondcorp.appconnectors.v1.AppConnector`

### [AppConnector.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.AppConnector.Builder)

A BeyondCorp connector resource that represents an application facing component deployed proximal to and with direct access to the application instances. It is used to establish connectivity between the remote enterprise environment and GCP. It initiates connections to the applications and can proxy the data from users over the connection.

Protobuf type `google.events.cloud.beyondcorp.appconnectors.v1.AppConnector`

### [AppConnector.PrincipalInfo](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.AppConnector.PrincipalInfo)

PrincipalInfo represents an Identity oneof.

Protobuf type ` google.events.cloud.beyondcorp.appconnectors.v1.AppConnector.PrincipalInfo`

### [AppConnector.PrincipalInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.AppConnector.PrincipalInfo.Builder)

PrincipalInfo represents an Identity oneof.

Protobuf type ` google.events.cloud.beyondcorp.appconnectors.v1.AppConnector.PrincipalInfo`

### [AppConnector.PrincipalInfo.ServiceAccount](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.AppConnector.PrincipalInfo.ServiceAccount)

ServiceAccount represents a GCP service account.

Protobuf type ` google.events.cloud.beyondcorp.appconnectors.v1.AppConnector.PrincipalInfo.ServiceAccount`

### [AppConnector.PrincipalInfo.ServiceAccount.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.AppConnector.PrincipalInfo.ServiceAccount.Builder)

ServiceAccount represents a GCP service account.

Protobuf type ` google.events.cloud.beyondcorp.appconnectors.v1.AppConnector.PrincipalInfo.ServiceAccount`

### [AppConnectorEventData](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.AppConnectorEventData)

The data within all AppConnector events.

Protobuf type `google.events.cloud.beyondcorp.appconnectors.v1.AppConnectorEventData`

### [AppConnectorEventData.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.AppConnectorEventData.Builder)

The data within all AppConnector events.

Protobuf type `google.events.cloud.beyondcorp.appconnectors.v1.AppConnectorEventData`

### [Data](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.Data)

### [ResourceInfo](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.ResourceInfo)

ResourceInfo represents the information/status of an app connector resource. Such as:

  * remote_agent
    * container
      * runtime
      * appgateway
        * appconnector
          * appconnection
            * tunnel
        * logagent



Protobuf type `google.events.cloud.beyondcorp.appconnectors.v1.ResourceInfo`

### [ResourceInfo.Builder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.ResourceInfo.Builder)

ResourceInfo represents the information/status of an app connector resource. Such as:

  * remote_agent
    * container
      * runtime
      * appgateway
        * appconnector
          * appconnection
            * tunnel
        * logagent



Protobuf type `google.events.cloud.beyondcorp.appconnectors.v1.ResourceInfo`

## Interfaces 

### [AppConnector.PrincipalInfo.ServiceAccountOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.AppConnector.PrincipalInfo.ServiceAccountOrBuilder)

### [AppConnector.PrincipalInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.AppConnector.PrincipalInfoOrBuilder)

### [AppConnectorEventDataOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.AppConnectorEventDataOrBuilder)

### [AppConnectorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.AppConnectorOrBuilder)

### [ResourceInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.ResourceInfoOrBuilder)

## Enums 

### [AppConnector.PrincipalInfo.TypeCase](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.AppConnector.PrincipalInfo.TypeCase)

### [AppConnector.State](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.AppConnector.State)

Represents the different states of a AppConnector.

Protobuf enum `google.events.cloud.beyondcorp.appconnectors.v1.AppConnector.State`

### [HealthStatus](https://docs.cloud.google.com/java/docs/reference/google-cloudevent-types/latest/com.google.events.cloud.beyondcorp.appconnectors.v1.HealthStatus)

HealthStatus represents the health status.

Protobuf enum `google.events.cloud.beyondcorp.appconnectors.v1.HealthStatus`

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
