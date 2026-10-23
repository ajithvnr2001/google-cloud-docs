---
url: https://docs.cloud.google.com/architecture/connected-devices/device-pubsub-architecture/
title: Device on Pub/Sub connection to Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:38.924940+00:00
---

# Device on Pub/Sub connection to Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/connected-devices/device-pubsub-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Device on Pub/Sub connection to Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-08-09 UTC

Rather than implementing a specific architecture to connect devices to analytics applications, some organizations might benefit from connecting directly to Pub/Sub from edge devices. We recommend this approach for organizations that have a small number of connected devices that aggregate data from a larger number of devices and sensors in a local or on-premises network. This approach is also recommended when your organization has connected devices that are in a more secure environment, such as a factory. This document outlines the high-level architectural considerations that you need to make to use this approach to connect devices to Google Cloud products.

This document is part of a series of documents that provide information about IoT architectures on Google Cloud. The other documents in this series include the following:

  * [Connected device architectures on Google Cloud overview](https://docs.cloud.google.com/architecture/connected-devices)
  * [Standalone MQTT broker architecture on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/mqtt-broker-architecture)
  * [IoT platform product architecture on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/iot-platform-product-architecture)
  * [Best practices for running an IoT backend on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/bps-running-iot-backend-securely)
  * Device on Pub/Sub architecture to Google Cloud (this document)
  * [Best practices for automatically provisioning and configuring edge and bare metal systems and servers](https://docs.cloud.google.com/architecture/connected-devices/best-practices-provisioning-configuring-bare-metal)



## Architecture

The following diagram shows a connected aggregation device or gateway that connects directly to Pub/Sub.

![Aggregation device or gateway architecture connected to Pub/Sub \(flow of events explained in following text\).](https://docs.cloud.google.com/static/architecture/images/device_pubsub_1.svg)

The flow of events in the preceding diagram is as follows:

  * You use the Identity and Access Management API to create a new key pair for a service account. The public key is stored in IAM. However, you must download the private key securely and store it in the gateway device so that it can be used for authentication.
  * The aggregation device collects data from multiple other remote devices and sensors located within a secure local network. The remote devices communicate with the gateway using a local edge protocol such as MODBUS, BACNET, OPC-UA, or another local protocol.
  * The aggregation device sends data to Pub/Sub over either HTTPS or gRPC. These API calls are signed using the service account private key held on the aggregation device.



### Architectural considerations and choices

Because Pub/Sub is a serverless data streaming service, you can use it to create bidirectional systems that are composed of event producers and consumers (known as publishers and subscribers). In some connected device scenarios, you only need a scalable publish and subscribe service to create an effective data architecture. The following sections describe the considerations and choices that you need to make when you implement a device to Pub/Sub architecture on Google Cloud.

## Ingestion endpoints

Pub/Sub provides prebuilt [client libraries](https://docs.cloud.google.com/pubsub/docs/reference/libraries) in multiple languages that implement the REST and gRPC APIs. It supports two protocols for message ingestion: [REST (HTTP) and gRPC](https://docs.cloud.google.com/pubsub/docs/reference/service_apis_overview). For a connected device to send and receive data through Pub/Sub, the device must be able to interact with one of these endpoints.

Many software applications have built-in support for REST APIs, so connecting with the Pub/Sub REST API is often the easiest solution. In some use cases, however, gRPC can be a more efficient and faster alternative. Because it uses serialized protocol buffers for the message payload instead of JSON, XML, or another text-based format, gRPC is better suited for the low-bandwidth applications that are commonly found in connected device use cases. gRPC API connections are also faster than REST for data transmission, and gRPC supports simultaneous bidirectional communication. One study found that gRPC is up to [seven times faster than REST](https://medium.com/@EmperorRXF/evaluating-performance-of-rest-vs-grpc-1b8bdf0b22da#:%7E:text=gRPC%20is%20roughly%207%20times,of%20HTTP%2F2%20by%20gRPC.). As a result, for many connected device scenarios, gRPC is a better option if a gRPC connector is available or can be implemented for the connected device application.

### Device authentication and credential management

Pub/Sub supports a number of [authentication methods](https://docs.cloud.google.com/pubsub/docs/authentication) for access from outside Google Cloud.

If your architecture includes an [external identity provider](https://docs.cloud.google.com/iam/docs/workload-identity-federation#providers) such as Active Directory or a local Kubernetes cluster, you can use [workload identity federation](https://docs.cloud.google.com/iam/docs/workload-identity-federation) to manage access to Pub/Sub. This approach lets you create short-lived access tokens for connected devices. You can also grant IAM roles to your connected devices, without the management and security overhead of using service account keys.

In cases when an external identity provider is not available, service account keys are the only option for authentication. Service account keys can become a security risk if not managed correctly, so we recommend that you follow security best practices for deploying service account keys to connected devices. To learn more, see [Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). Service accounts are also a limited resource and any cloud project has a limited quota of [user-managed service accounts](https://docs.cloud.google.com/iam/docs/service-accounts#user-managed). Consequently, this approach is only an option for deployments that have a small number of devices that need to be connected.

### Backend applications

After data is ingested into a Pub/Sub topic, the data is available to any application that runs on Google Cloud that has the appropriate credentials and access privileges. No additional connectors are necessary other than the Pub/Sub API in your application. Messages can be made available to multiple applications across your backend infrastructure for parallel processing or alerting, as well as archival storage and other analytics.

## Use cases

The following sections describe example scenarios where a direct connection from devices to Pub/Sub is well suited for connected device use cases.

### Bulk data ingestion from an on-premises data historian

A device to Pub/Sub connection is best suited for applications which have a small number of endpoints that transmit large volumes of data. An [operational data historian](https://en.wikipedia.org/wiki/Operational_historian) is a good example of an on-premises system that stores a lot of data which needs to be transmitted to Google Cloud. For this use case, a small number of endpoints must be authenticated, typically one to a few connected devices, which is within the typical parameters for service account authentication. These systems also commonly have modular architectures, which lets you implement the Pub/Sub API connection that you need to communicate with Google Cloud.

### Local gateway data aggregation for a factory

Aggregation of factory sensor data in a local gateway is another use case well suited for a direct Pub/Sub connection. In this case, a local data management and aggregation system are deployed on a gateway device in the factory. This system is typically a software product that connects to a wide variety of local sensors and machines. The product collects the data and frequently transforms it into a standardized representation before passing it on to the cloud application.

Many devices can be connected in this scenario. However, those devices are usually only connected to the local gateway and are managed by the software on that device, so there's no need for a cloud-based management application. Unlike in an MQTT broker architecture, in this use case, the gateway plays an active role in aggregating and transforming the data.

When the gateway connects to Google Cloud, it authenticates with Pub/Sub through a service account key. The gateway sends the aggregated and transformed data to the cloud application for further processing. The number of connected gateways is also typically in the range of tens to hundreds of devices, which is within the typical range for service account authentication.

## What's next

  * Learn [best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys).
  * Read [an overview of identity federation for external workloads](https://docs.cloud.google.com/iam/docs/workload-identity-federation).
  * Learn more about [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview)
  * Explore reference architectures, diagrams, and best practices for Google Cloud. Take a look at our [Cloud Architecture Center](https://docs.cloud.google.com/architecture).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-08-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-08-09 UTC."],[],[]] 
