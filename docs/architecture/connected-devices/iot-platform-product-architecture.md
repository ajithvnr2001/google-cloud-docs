---
url: https://docs.cloud.google.com/architecture/connected-devices/iot-platform-product-architecture/
title: IoT platform product architecture on Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:46.880428+00:00
---

# IoT platform product architecture on Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/connected-devices/iot-platform-product-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  IoT platform product architecture on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-08-09 UTC

IoT platform products typically provide basic MQTT and HTTPS data connectivity. They also let you provision devices, and they provide authentication and management, telemetry storage and visualization, data processing, and alerting. Organizations often use IoT platforms when a standalone MQTT broker isn't sufficient for a use case and a more complete IoT platform product is needed. An IoT platform provides a unified interface for managing a heterogeneous collection of devices. This interface is important for many connected device applications, and it's a key difference between an IoT platform and a standalone MQTT broker. This document outlines the basic architectural considerations and recommendations that you need to make before you deploy an IoT platform product architecture on Google Cloud.

This document is part of a series of documents that provide information about IoT architectures on Google Cloud. The other documents in this series include the following:

  * [Connected device architectures on Google Cloud overview](https://docs.cloud.google.com/architecture/connected-devices)
  * [Standalone MQTT broker architecture on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/mqtt-broker-architecture)
  * IoT platform product architecture on Google Cloud (this document)
  * [Best practices for running an IoT backend on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/bps-running-iot-backend-securely)
  * [Device on Pub/Sub architecture to Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/device-pubsub-architecture)
  * [Best practices for automatically provisioning and configuring edge and bare metal systems and servers](https://docs.cloud.google.com/architecture/connected-devices/best-practices-provisioning-configuring-bare-metal)



The following diagram shows an example architecture with a generic IoT platform product running on Google Cloud.

![A generic IoT platform architecture \(flow of events explained in following text.](https://docs.cloud.google.com/static/architecture/images/iot_diagram_one.svg)

As shown in the preceding diagram, the IoT platform deploys an MQTT broker or endpoint for device connectivity. The IoT platform is connected to an external proxy Network Load Balancer to distribute traffic from the edge devices. Additional IoT applications can connect to the IoT platform through Pub/Sub, or by using the Dataflow MQTT connector.

The IoT platform provides a set of device management services. As shown in the diagram, these services are as follows:

  * Device credential store
  * Rules engine
  * Device authentication and authorization
  * Device configuration management
  * Device registry
  * Device update management



IoT platform products also generally include services such as digital twin features, low-code development interfaces, alerting and notification capabilities, and other analytics functionality.

### Architectural considerations and choices

The following sections describe the architectural choices that you can make for an IoT platform product architecture, and the impact of these choices.

## Ingestion endpoints

Most commercial IoT platform applications include an MQTT endpoint, and usually also an HTTPS endpoint for data ingestion from connected devices.

### MQTT

An IoT platform implements an MQTT endpoint in one of the following ways:

  * A connector between MQTT and another message service
  * An MQTT broker which implements the full MQTT specification



When you evaluate commercial IoT platforms, it's important to know which of the preceding approaches the vendor has chosen for the product so that you can determine the implications for your use case.

In some cases, the MQTT endpoint only connects the MQTT clients with a backend messaging service, such as Kafka or Pub/Sub. This type of endpoint usually does not implement the complete MQTT protocol specification, and often doesn't include features such as QoS levels 1 and 2, or shared subscriptions. The advantage of this approach is that it decreases complexity in the IoT platform, because there's no separate MQTT broker application. Operational costs are lower, and maintenance is simpler than if the platform uses a separate MQTT broker. However, because of the reduced support for more advanced MQTT protocol features, this approach means that there is less flexibility and functionality for MQTT message transport than a standalone MQTT broker that implements the complete MQTT specification.

Other IoT platforms provide a complete MQTT broker as part of the platform, as shown in the example architecture in this document. This broker might be one of the existing open source brokers, or a proprietary broker implementation. A full MQTT broker provides the full bidirectional MQTT capability described earlier, but a full broker can add complexity and operational costs to the management of the IoT platform.

### HTTPS and other supplementary protocols

In addition to MQTT, many IoT platforms provide more data ingestion endpoints than those that are shown in the main architecture that this document describes.

HTTPS is a common alternative protocol to MQTT for connected device use cases. It has higher overhead than MQTT, but it's more widely supported by mobile devices such as phones, and by web browsers and other applications. It's frequently used in certain connected device applications, and it's supported by open source platforms like [Eclipse Hono](https://www.eclipse.org/hono/) and many commercial products.

Many constrained device applications use ([Constrained Application Protocol (CoAP), defined in RFC 7252](https://www.rfc-editor.org/rfc/rfc7252)) as an MQTT alternative. CoAP targets low-overhead and small-footprint clients for embedded devices and sensors. Many commercial IoT platform applications also provide a CoAP endpoint.

## Load balancing

For more information about choosing the best load balancer for your architecture, see the [load balancing section of the Standalone MQTT broker architecture on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/mqtt-broker-architecture#load_balancing) because those considerations are applicable to this case as well.

## Device authentication and credential management

Management of device credentials and authentication is a key part of the operation of an IoT platform. The authentication methods supported by connected devices vary widely across applications and device form factors. It's important to select the appropriate authentication method for the target use case, and implement the chosen authentication scheme correctly.

Unlike a standalone MQTT Broker, an IoT platform provides integrated services to manage device identity and credentials. Most IoT platforms use X.509 client certificate authentication for authentication, JWT token-based authentication (often combined with OAuth 2.0), and username and password authentication. Some platforms also support integration with an external LDAP authentication provider.

For some constrained devices, JWT or username and password authentication might be more appropriate, because these schemes require fewer resources on a connected device. When you use either JWT or username and password authentication, it's important that you encrypt the network connection separately to mTLS authentication, because an encrypted connection is not required by either of these authentication methods. X.509 certificate authentication, by contrast, consumes more resources on the connected device, but is typically used in an mTLS-encrypted connection and thus provides a high level of security.

Provisioning the authentication credentials on the edge device at manufacturing time is also an important part of the connected device authentication scheme, but is outside the scope of this document.

For more information about authentication and credential management, see [Best practices for running an IoT backend on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/bps-running-iot-backend-securely).

## Manage connected devices

Typically, connected devices publish telemetry events and state information to the platform through one of the ingestion endpoints such as MQTT. If you're using a multi-protocol IoT platform, devices can communicate using any of the supported protocols.

We recommend that your organization use an IoT platform that has the following capabilities:

  * **Software and system updates:** The delivery and rollback of firmware, software, and application updates to the connected devices. These updates usually also involve storage and management of the updates themselves.
  * **Configuration updates:** The delivery, storage, and rollback of updates to the configuration of applications deployed on the connected devices.
  * **Credential creation and management:** The creation of new device credentials, delivery of those credentials to the connected device, auditing of device access attempts and activity, and revocation of compromised or expired credentials at the appropriate time.
  * **Rules engine and data processing:** The definition and execution of data-driven rules and other data processing steps. This capability often includes some type of low-code interface for defining rules and data processing pipelines.



### Backend workloads

Most IoT platforms provide their own internal data storage and transport capabilities that let you connect to your backend workloads and applications. AMQP, RabbitMQ, and Kafka are commonly used to provide internal data transport. These can all be connected to Pub/Sub using the Pub/Sub SDK. You can also use an integrated database system such as PostgreSQL to store data in the platform. In many cases, the IoT platform can be configured to use one of the Cloud Storage products directly, such as Cloud SQL, Firebase, or BigQuery.

If the IoT platform has a complete MQTT broker, backend applications can also communicate with devices by using the MQTT capability of the platform. If the application supports MQTT, the application can connect with the broker as a subscriber. If there is no MQTT support, Apache Beam provides an MQTT driver, which enables bidirectional integration with Dataflow as well as other Beam deployments.

## Use cases

The following sections describe example scenarios where an IoT platform is a better architectural choice than a standalone MQTT broker or a direct connection to Pub/Sub.

### Smart appliance management

Applications that manage multiple smart appliances are well-suited to an IoT platform. An example of such an application is a platform to manage kitchen appliances such as dishwashers and coffee makers. These devices generally connect to a cloud-based application, either directly over Wi-Fi or through a local gateway that uses a Bluetooth Low Energy (BLE) or another local protocol. The management capabilities of an IoT platform are important here, for monitoring the state of each device, managing software updates and security patches, and capturing device activity to provide critical intelligence to the manufacturer and the customer. These capabilities are beyond the scope of a basic MQTT broker. At a minimum, a device information repository, a device state database, a telemetry datastore, and an analytics interface are all critical to building a successful smart appliance platform.

### Logistics and asset tracking

For a logistics and asset tracking application, an IoT platform product offers more complete functionality than a basic MQTT broker, so is a better choice for this use case. Monitoring the current and past state and location of a large fleet of assets depends on a robust device state database and identity management system. As new assets are deployed, they need to be connected to the platform with as little friction as possible, and subsequently monitored throughout the asset lifecycle. In many cases, the application also collects other sensor information about the asset, such as local temperature, humidity and atmospheric pressure, or 3D positioning and acceleration data to detect unexpected movements or drops. All this data must be ingested and associated with the correct asset for analysis in any backend application, so the full-featured device management provided by the IoT platform is an important capability.

## What's next

  * Read about connecting devices and building IoT applications on Google Cloud using [Intelligent Products Essentials](https://docs.cloud.google.com/architecture/intelligent-products-essentials-architecture).
  * Learn about practices for [automatically provisioning and configuring edge and bare metal systems and servers](https://docs.cloud.google.com/architecture/best-practices-provisioning-configuring-bare-metal).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-08-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-08-09 UTC."],[],[]] 
