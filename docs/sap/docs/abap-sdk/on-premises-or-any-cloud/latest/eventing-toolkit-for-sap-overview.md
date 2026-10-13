---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-overview/
title: Business Eventing Toolkit for SAP overview \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:34.495483+00:00
---

# Business Eventing Toolkit for SAP overview  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Business Eventing Toolkit for SAP overview Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/eventing-toolkit-for-sap-overview)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-overview)



The Business Eventing Toolkit for SAP provides event-driven integration between SAP and Google Cloud, enabling you publish your SAP events to Google Cloud. By publishing your SAP events to Google Cloud, you can maximize the value of your SAP events, such as:

  * Build real-time data streams from SAP events by using [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) for immediate insights.
  * Automate real-time responses to SAP events with serverless [Cloud Run functions](https://docs.cloud.google.com/functions).
  * Engage customers with real-time mobile notifications based on SAP events by using [Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging).
  * Extend SAP features by connecting your events to third-party APIs by using [Integration Connectors](https://docs.cloud.google.com/integration-connectors/docs/overview).



The Business Eventing Toolkit for SAP facilitates the integration of business systems by offering flexible event publishing:

  * **Publish events as CloudEvents** : To ensure consistent event handling and integration across different systems, the toolkit supports the [CloudEvents 1.0 specification](https://github.com/cloudevents/spec/tree/v1.0), an open standard for event data. Google Cloud services such as Cloud Run functions, Pub/Sub, and Firebase Cloud Messaging use the CloudEvents 1.0 specification. This enables efficient communication between SAP systems and Google Cloud services. The toolkit supports publishing your events in both structured encoding and binary encoding.

  * **Publish events as regular JSON** : To enable data exchange and integration between systems where CloudEvents compliance is not required, the toolkit supports publishing events in standard JSON format.




The Business Eventing Toolkit for SAP is shipped as a subpackage of the on-premises or any cloud edition of ABAP SDK for Google Cloud. To use the toolkit, you need to install the latest version of the SDK in your SAP environment. For information about the installation steps, see [Install and configure the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config).

The Business Eventing Toolkit for SAP is only available with the on-premises or any cloud edition of ABAP SDK for Google Cloud.

This document is intended for ABAP developers, SAP solution architects, and cloud architects. It assumes that you're familiar with the [ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/overview) and [CloudEvents Notations and Terminology](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md#notations-and-terminology).

## Key capabilities

The following list highlights the key capabilities of the Business Eventing Toolkit for SAP:

  * **Publish SAP events to Google Cloud** : Capture SAP standard events such as BOR events, change documents, and IDoc events, and publish them to Google Cloud with minimal configuration.

  * **CloudEvents 1.0 encoding and decoding** : Encode and decode API requests according to the CloudEvents 1.0 specification.

  * **Configure multiple Google Cloud services as targets** : Configure to publish events to multiple target Google Cloud services, including Cloud Run functions, Pub/Sub, Firebase Cloud Messaging (FCM), and Integration Connectors.

  * **Extend event-driven integration** : Extend event-driven integration to other Google Cloud targets and third-party systems.




## Key components

The following diagram illustrates the key components of the Business Eventing Toolkit for SAP and how business events originating in SAP are sent to Google Cloud by using the Business Eventing Toolkit for SAP:

![Key components of the Business Eventing Toolkit for SAP](https://docs.cloud.google.com/static/sap/docs/images/eventing-toolkit-for-sap-key-components.svg)

SAP events are generated through business process execution initiated by user actions, scheduled jobs, or internal system operations. The Business Eventing Toolkit for SAP then captures and handles these events. The event data is subsequently delivered to Google Cloud services through the ABAP SDK for Google Cloud. Furthermore, you can directly use the toolkit components to send event data to Google Cloud services in your custom developments.

The toolkit has the following main components:

### CloudEvents module

The CloudEvents module handles the encoding and decoding of CloudEvents using both structured and binary encodings. In structured encoding, the module serializes CloudEvent attributes and data into a single JSON-formatted payload. In binary encoding, CloudEvent attributes are mapped to transport-specific headers, and the data payload is transmitted directly.

You can configure default values for CloudEvent attributes to standardize how your event messages are encoded and decoded. By predefining attribute values, you can streamline event processing and integration with downstream systems, regardless of whether you're using structured or binary encoding.

The CloudEvent attribute values are stored against a unique "CloudEvent Default Attribute Key" in the CloudEvents module. As an ABAP developer, for sending a business event to Google Cloud, you use the `ENCODE_AS_CLOUD_EVENT` method within the Google Cloud API stub to pass the `CloudEvent Default Attribute Key` and optionally supply extension attribute values. This method retrieves CloudEvent attributes from the configuration and publishes the event as a CloudEvent with those attributes.

To override the default values defined in the configuration, when you publish an event as a CloudEvent, you can pass specific values for CloudEvent attributes in your code.

### Publisher module

The Publisher module contains routing rules and an event publisher that reads the routing rules and sends event data to the target endpoint. You map an "Event Key" to a specific "Event Processor Class" for the target endpoint.

The Publisher module includes prebuilt targets for the following Google Cloud services:

  * **Pub/Sub** : Enables publishing SAP events to Pub/Sub topics for asynchronous processing.
  * **Cloud Run functions** : Enables triggering serverless functions in response to SAP events.
  * **Firebase Cloud Messaging (FCM)** : Enables sending push notifications to mobile devices based on SAP events.
  * **Integration Connectors** : Enables sending events to the Integration Connectors API.



### SAP event listeners

The SAP event listeners capture any SAP events within your SAP system, such as changes to business objects or incoming data. You can integrate these listeners directly into your standard SAP transactions, including enhancement points for custom logic. You then map this SAP listener configuration to an "Event Key" defined in the target services configuration. This lets you send these SAP events to Google Cloud, enabling real-time integration.

The Business Eventing Toolkit for SAP supports capturing various SAP events, including the following:

  * **BOR events** : Events triggered by changes to SAP business objects. For example, a "customer created" or "sales order changed" event.
  * **RAP events** : Events raised within modern SAP cloud applications built with the RESTful ABAP programming model.
  * **Change documents** : Records of data changes within SAP, providing an audit trail. Whenever a field in a database table is modified, a change document is created, capturing the old and new values.
  * **IDoc events** : Events triggered when SAP receives data from external systems or sends data to external systems through IDocs.



## Pricing

The Business Eventing Toolkit for SAP is offered at no cost. However, you're responsible for the charges incurred from your use of Google Cloud services. To get a cost estimate, see the [Pricing calculator](https://cloud.google.com/products/calculator).

## What's next

  * Learn how to [install and configure the Business Eventing Toolkit for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-configuration).
  * Learn how to [publish events programmatically](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/eventing-toolkit-for-sap-publish-events).
  * Ask your questions and discuss the Business Eventing Toolkit for SAP with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
