---
url: https://docs.cloud.google.com/healthcare-api/docs/concepts/hl7v2/
title: HL7v2 \u00a0|\u00a0 Cloud Healthcare API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:38.002543+00:00
---

# HL7v2  |  Cloud Healthcare API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/healthcare-api/docs/concepts/hl7v2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Cloud Healthcare API ](https://docs.cloud.google.com/healthcare-api/docs)
  * [ Guides ](https://docs.cloud.google.com/healthcare-api/docs/introduction)



Send feedback 

#  HL7v2 Stay organized with collections  Save and categorize content based on your preferences. 

Health Level Seven International Version 2 (HL7v2) is a clinical messaging format that provides data about events that occur inside an organization.

See the [HL7 Version 2 Product Suite documentation](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=185) for more details on HL7v2.

## HL7v2 stores

An _HL7v2 store_ is a data store that resides within a dataset. HL7v2 stores hold HL7v2 messages.

The [`HL7V2Store`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores) resource provides a representation of an HL7v2 store's attributes. For each of your HL7v2 stores, you can choose options such as:

  * Whether to publish changes to the HL7v2 store (if, for example, your application receives a new message) to a [Pub/Sub](https://docs.cloud.google.com/healthcare-api/docs/how-tos/pubsub) topic.
  * How to parse messages ingested into an HL7v2 store.



## HL7v2 messages

Raw HL7v2 messages can be difficult to read. For example, take the following message:
    
    
    MSH|^~\&|FROM_APP|FROM_FACILITY|TO_APP|TO_FACILITY|20180101000000||ADT^A01|20180101000000|P|2.5|
    EVN|A01|20110613083617|
    PID|1|843125^^^^MRN|21004053^^^^MRN~2269030303^^^^ORGNMBR||SULLY^BRIAN||19611209|M|||123 MAIN ST^^CITY^STATE^12345|
    PV1||I|H73 RM1^1^^HIGHWAY 01 CLINIC||||5148^MARY QUINN|||||||||Y||||||||||||||||||||||||||||20180101000000|
    

The Cloud Healthcare API can:

  1. Parse a message.
  2. Extract several fields from the message header segment (MSH) to allow for filtering.
  3. Represent the message's content as JSON data for further processing or data exchange.



The [`Message`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages) resource provides a representation of an HL7v2 message. It includes information such as:

  * The time when the message was created
  * Who created the message
  * What data the message contains



The `Message` resource for the preceding message looks like this:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/datasets/DATASET_ID/hl7V2Stores/HL7V2_STORE_ID/messages/W5_pxOBkoLoCxiFxE4cg8zwEWRzMlOzIfaLBrZPf0Zg=",
      "data": "TVNIfF5+XCZ8RlJPTV9BUFB8RlJPTV9GQUNJTElUWXxUT19BUFB8VE9fRkFDSUxJVFl8MjAxODAxMDEwMDAwMDB8fEFEVF5BMDF8MjAxODAxMDEwMDAwMDB8UHwyLjV8DUVWTnxBMDF8MjAxMTA2MTMwODM2MTd8DVBJRHwxfDg0MzEyNV5eXl5NUk58MjEwMDQwNTNeXl5eTVJOfjIyNjkwMzAzMDNeXl5eT1JHTk1CUnx8U1VMTFleQlJJQU58fDE5NjExMjA5fE18fHwxMjMgTUFJTiBTVF5eQ0lUWV5TVEFURV4xMjM0NXwNUFYxfHxJfEg3MyBSTTFeMV5eSElHSFdBWSAwMSBDTElOSUN8fHx8NTE0OF5NQVJZIFFVSU5OfHx8fHx8fHx8WXx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHx8fHwyMDE4MDEwMTAwMDAwMHw=",
      "sendFacility": "FROM_FACILITY",
      "sendTime": "2018-01-01T00:00:00Z",
      "messageType": "ADT",
      "createTime": "2018-01-01T00:00:00Z",
      "patientIds": [
        {
          "value": "843125",
          "type": "MRN"
        },
        {
          "value": "21004053",
          "type": "MRN"
        },
        {
          "value": "2269030303",
          "type": "ORGNMBR"
        }
      ],
      "parsedData": {
        "segments": [
          {
            "segmentId": "MSH",
            "fields": {
              "5": "TO_FACILITY",
              "2": "FROM_APP",
              "3": "FROM_FACILITY",
              "0": "MSH",
              "1": "^~\\&",
              "10": "P",
              "4": "TO_APP",
              "9": "20180101000000",
              "8.1": "ADT",
              "11": "2.5",
              "8.2": "A01",
              "6": "20180101000000"
            }
          },
          {
            "segmentId": "EVN",
            "fields": {
              "1": "A01",
              "2": "20110613083617",
              "0": "EVN"
            }
          },
          {
            "segmentId": "PID",
            "fields": {
              "1": "1",
              "3[0].1": "21004053",
              "3[1].1": "2269030303",
              "3[0].5": "MRN",
              "0": "PID",
              "11.4": "STATE",
              "11.5": "12345",
              "2.1": "843125",
              "2.5": "MRN",
              "5.1": "SULLY",
              "11.3": "CITY",
              "8": "M",
              "11.1": "123 MAIN ST",
              "3[1].5": "ORGNMBR",
              "7": "19611209",
              "5.2": "BRIAN"
            }
          },
          {
            "segmentId": "PV1",
            "fields": {
              "44": "20180101000000",
              "7.1": "5148",
              "16": "Y",
              "2": "I",
              "3.2": "1",
              "3.4": "HIGHWAY 01 CLINIC",
              "7.2": "MARY QUINN",
              "3.1": "H73 RM1",
              "0": "PV1"
            }
          }
        ]
      }
    }
    

### Creating and ingesting messages

You can store HL7v2 messages in an HL7v2 store using the following methods:

  * [`messages.create`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/create): creates a [`Message`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages) resource and stores it in the HL7v2 store. This method's response contains the message body.

  * [`messages.ingest`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages/ingest): ingests a [`Message`](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages) resource and stores it in the HL7v2 store. This method's response contains the message body and an acknowledgement field, `hl7ack`, which verifies that the message was accepted.

Note the following important information about the `hl7ack` field's value:

    * The value contains a response type. An `AA` response type indicates `Application Accept`, meaning that the message was validated and successfully ingested.
    * The sending facility and the receiving facility are reversed.
    * The value contains the original message's [control ID](https://www.hl7.org/documentcenter/public_temp_7890F70A-1C23-BA17-0C771A64EC211E18/wg/conf/HL7MSH.htm#MessControl).



If your application requires an `ACK` response, use `messages.ingest`. If your application does not require an `ACK` response, use `messages.create`. `ACK` responses are not persisted in HL7v2 stores.

When you create or ingest an HL7v2 message, the message is assigned an ID by the server. You can use this ID when interacting with the message (for example, to delete the message or label it with user-defined labels).

## MLLP and the Google Cloud MLLP adapter

The [minimal lower layer protocol (MLLP)](http://www.hl7.org/implement/standards/product_brief.cfm?product_id=55) is the standard used for transmitting HL7v2 messages over TCP/IP connections within a network, such as a hospital.

MLLP does not offer an exact mapping to the Cloud Healthcare API [HL7v2 REST API](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores.messages), which uses HTTP. Therefore, an MLLP adapter must be used to convert messages transmitted over MLLP into a format that an HTTP/REST API can accept. To transmit messages over MLLP and then to the Cloud Healthcare API, use the Google Cloud [MLLP adapter](https://github.com/GoogleCloudPlatform/mllp/). For a tutorial using this MLLP adapter, see [Transmitting HL7v2 messages over TCP/IP connections](https://docs.cloud.google.com/healthcare-api/docs/how-tos/mllp-adapter).

If your application requires that a trusted authority signs the HL7v2 message, use the Google Cloud [Binary Authorization MLLP Adapter](https://github.com/GoogleCloudPlatform/mllp/blob/master/mllp_adapter/docs/binary_authz.md). For a tutorial using this MLLP adapter, see [Transmitting HL7v2 messages over TCP/IP connections with Binary Authorization](https://docs.cloud.google.com/healthcare-api/docs/how-tos/mllp-adapter-binary-auth).

The adapter does not parse or inspect the HL7v2 messages; the Cloud Healthcare API parses and validates the messages as they are ingested into an [HL7v2 store](https://docs.cloud.google.com/healthcare-api/docs/reference/rest/v1/projects.locations.datasets.hl7V2Stores). You can then do further validation on the message by [viewing](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-messages#getting_hl7v2_message_contents) it or [labeling](https://docs.cloud.google.com/healthcare-api/docs/how-tos/hl7v2-messages#labeling_an_hl7v2_message) it for analysis.

While it runs, the adapter keeps a long-lived TCP connection open between the care system network and the adapter. It also exposes a TCP socket for accepting HL7v2 messages over MLLP. The adapter determines message boundaries by detecting the start and end block bytes of each message, as defined in the [MLLP standard](https://www.hl7.org/implement/standards/product_brief.cfm?product_id=55).

When the MLLP adapter receives an HL7v2 message from the care system over the TCP connection, it ingests the message into the HL7v2 store. The store then synchronously responds to the MLLP adapter with either `ACK` or `NACK`. An `ACK` is sent if the message is properly formed and has a valid header segment. The MLLP adapter sends the `ACK` or `NACK` response to the care system.

The MLLP adapter can also listen to a Pub/Sub subscription associated with the HL7v2 store. When an HL7v2 message is created or ingested into the store, the MLLP adapter receives the notification and publishes the message to the care system.

### MLLP and security

MLLP does not natively support any encryption or authentication. Therefore, a TCP connection that uses MLLP should be wrapped in a secure connection using a [virtual private network (VPN)](https://en.wikipedia.org/wiki/Virtual_private_network). You can use [Cloud VPN](https://docs.cloud.google.com/vpn) to create a secure connection between the GKE cluster on which the MLLP adapter runs and your on-premises application. For more information, see [Configuring Cloud VPN](https://docs.cloud.google.com/healthcare-api/docs/how-tos/mllp-adapter#configuring_cloud_vpn).

### HL7v2, MLLP, and Pub/Sub

A fundamental aspect of using HL7v2 with the Cloud Healthcare API involves the configuration of [Pub/Sub notifications](https://docs.cloud.google.com/healthcare-api/docs/concepts/pubsub). By using a subscriber application with Pub/Sub, you can receive notifications when an HL7v2 message is created or ingested into an HL7v2 store.

Read [Configuring Pub/Sub notifications](https://docs.cloud.google.com/healthcare-api/docs/how-tos/pubsub) to see how to use Pub/Sub topics with the Cloud Healthcare API HL7v2 implementation.

### HL7v2, MLLP, and Google Cloud architecture

The following diagram shows how an HL7v2 message is sent from a care system and ingested into the Cloud Healthcare API. The MLLP adapter is deployed to [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine) and the message is transmitted over a VPN using Cloud VPN. After ingestion, a subscriber application subscribed to the HL7v2 store's Pub/Sub topic receives a notification that the message was ingested. The Cloud Healthcare API also generates an `ACK` for the MLLP adapter and sends it back through the VPN tunnel and into the care system.

The HL7v2 message sent from the care system is an "ADT" message, which is a common message in HL7v2. When a care system sends an ADT message, it does not expect a new message to be generated and returned from the remote/on-premises system.

![mllp_adapter](https://docs.cloud.google.com/static/healthcare-api/images/mllp_adapter.svg)

The diagram shows the following:

  1. The on-premises care system.
  2. An ADT HL7v2 message leaves the care system.
  3. The HL7v2 message is ingested through the MLLP adapter into an HL7v2 store.
  4. The HL7v2 store's configured Pub/Sub topic receives a notification that a message was ingested.
  5. A subscriber application listens for notifications of HL7v2 message ingestions from its Pub/Sub topic.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
