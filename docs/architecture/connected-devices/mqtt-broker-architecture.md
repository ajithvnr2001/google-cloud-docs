---
url: https://docs.cloud.google.com/architecture/connected-devices/mqtt-broker-architecture/
title: Standalone MQTT broker architecture on Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:52.948308+00:00
---

# Standalone MQTT broker architecture on Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/connected-devices/mqtt-broker-architecture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Standalone MQTT broker architecture on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-08-09 UTC

[MQTT](https://mqtt.org/) is an OASIS standard protocol for connected device applications that provides bidirectional messaging using a publish-and-subscribe broker architecture. The MQTT protocol is lightweight to reduce the network overhead, and MQTT clients are very small to minimize the use of resources on constrained devices. One solution for organizations who want to support connected device applications on Google Cloud is to run a standalone MQTT broker on Compute Engine or GKE. To deploy an MQTT broker in your organization, you need to make several key decisions which affect the overall architecture; in particular, load-balancing and the deployment environment. This document describes an architecture for deploying an MQTT broker, the core application in an MQTT deployment, on Google Cloud. It also describes the decisions that you need to make when you deploy this broker, and how they impact the architecture.

This document is part of a series of documents that provide information about IoT architectures on Google Cloud. The other documents in this series include the following:

  * [Connected device architectures on Google Cloud overview](https://docs.cloud.google.com/architecture/connected-devices)
  * Standalone MQTT broker architecture on Google Cloud (this document)
  * [IoT platform product architecture on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/iot-platform-product-architecture)
  * [Best practices for running an IoT backend on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/bps-running-iot-backend-securely)
  * [Device on Pub/Sub architecture to Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/device-pubsub-architecture)
  * [Best practices for automatically provisioning and configuring edge and bare metal systems and servers](https://docs.cloud.google.com/architecture/connected-devices/best-practices-provisioning-configuring-bare-metal)



The following diagram shows an MQTT broker architecture running on Google Cloud.

![MQTT broker architecture diagram \(explained in following text\).](https://docs.cloud.google.com/static/architecture/images/mqtt_broker_arch.svg)

The architecture in the preceding image is composed as follows:

  * The MQTT broker is deployed as a cluster of three instances that are connected to the Cloud Load Balancing service. For the cloud load balancer, you can choose from one of several load-balancing products, which are described later in this document.
  * The broker cluster includes a device credential store and a device authentication and authorization service. The cluster connects with the backend workloads through Dataflow or Pub/Sub.
  * On the client side, edge gateways provide bidirectional communication between edge devices and the MQTT broker cluster through MQTT over TLS.



Generally, we recommend that you deploy the MQTT broker application for this architecture in a cluster for scalability. Factors such as the clustering functionality, the scale-up and scale-down cluster management, data synchronization, and network partition handling are addressed by the specific broker implementations.

## Architectural considerations and choices

The following sections describe the different architectural choices and considerations that you must make for a standalone MQTT broker architecture, and the impact that these choices have on the architecture.

### Connected devices

Internet-connected edge devices publish their telemetry events and other information to the MQTT broker. To implement the standalone MQTT broker architecture that's described in this document, the device needs to have an MQTT client, the server certificate public key for TLS authentication, and the credentials needed to authenticate with the MQTT broker.

In addition, edge devices generally have connectors to local sensors, to on-premises data systems, and to other devices that do not have internet access or IP connectivity. For example, the edge device can serve as a gateway for other local constrained devices connected to the gateway using BLE, to a wired connection, or to another near-field protocol. A detailed specification of the connected device architecture is outside the scope of this guide.

## Load balancing

In the architecture, an external load-balancing service is configured between the public network and the MQTT broker cluster. This service provides several important networking functions, including distribution of incoming connections across backend nodes, session encryption, and authentication.

Google Cloud supports several load balancer types. To choose the best load balancer for your architecture, consider the following:

  * **mTLS**. mTLS handles both encryption and device authentication methods, while standard TLS handles only encryption and requires a separate device authentication method:

    * If your application uses mTLS for device authentication and needs to terminate the TLS tunnel, we recommend that you use a [regional external passthrough Network Load Balancer](https://docs.cloud.google.com/load-balancing/docs/network) or an [external proxy Network Load Balancer with a target TCP proxy](https://docs.cloud.google.com/load-balancing/docs/tcp). External proxy Network Load Balancers terminate the TLS session and proxy the connection to the broker node, along with any authentication credentials that are contained in the message. If you need the client connection information as part of the authentication scheme, you can preserve it in the backend connection by [enabling the PROXY protocol](https://docs.cloud.google.com/load-balancing/docs/tcp/setting-up-tcp#proxy-protocol).
    * If your application doesn't use mTLS, we recommend that you use an [external proxy Network Load Balancer with a target SSL proxy](https://docs.cloud.google.com/load-balancing/docs/tcp) to offload the external TLS and SSL processing to the load balancer. External proxy Network Load Balancers terminate the TLS session and proxy the connection to the broker node, along with any authentication credentials that are contained in the message. If you need the client connection information as part of the authentication scheme, you can preserve it in the backend connection by [enabling the PROXY protocol](https://docs.cloud.google.com/load-balancing/docs/ssl/setting-up-ssl#proxy-protocol).
  * **HTTP(S) endpoints**. If you need to expose HTTP(S) endpoints, we recommend that you configure a separate [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) for these endpoints.




For more information about the load balancer types that Cloud Load Balancing supports, see [Summary of Google Cloud load balancers](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview#summary-of-google-cloud-load-balancers).

### Load balancing strategy

Any load-balancing service distributes connections from edge devices across the nodes in the cluster according to one of several algorithms or [_balancing modes_](https://docs.cloud.google.com/load-balancing/docs/backend-service#balancing-mode). For MQTT, a [_session affinity_](https://docs.cloud.google.com/load-balancing/docs/network/networklb-backend-service#session-affinity) load-balancing strategy is better than random load balancing. Because MQTT client-server connections are persistent bidirectional sessions, state is maintained on the broker node that stops the connection. In a clustered configuration, if a client disconnects and then reconnects to a different node, the session state is moved to the new node, which adds load on the cluster. This issue can be largely avoided by using session affinity load balancing. If clients frequently change their IP addresses, the connection can break, but in most cases session affinity is better for MQTT. Session affinity is available in all Cloud Load Balancing products.

## Device authentication and credential management

MQTT broker applications handle device authentication and access control separately from Google Cloud. A broker application also provides its own credential store and management interface. The MQTT protocol supports basic username and password authentication in the initial Connect packet, and these fields are also frequently used by broker implementations to support other forms of authentication such as X.509 Certificate or JWT authentication. MQTT 5.0 also adds support for enhanced authentication methods that use challenge and response-style authentication. The authentication method that's used depends on the choice of MQTT broker application and your connected device use case.

Regardless of the authentication method that the broker uses, the broker maintains a device credential store. This store can be in a local SQL database or a flat file. Some brokers also support the use of a managed database service such as Cloud SQL. You need a separate service to manage the device credential store and handle any integrations with other authentication services such as IAM. The development of this service is outside the scope of this guide.

For more information about authentication and credential management, see [Best practices for running an IoT backend on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/bps-running-iot-backend-securely).

## Backend workloads

Any connected device use case includes one or more backend applications that use the data ingested from the connected devices. Sometimes, these applications also need to send commands and configuration updates to the devices. In the standalone MQTT broker architecture in this document, incoming data and outgoing commands are both routed through the MQTT broker. There are different topics within the broker's topic hierarchy to differentiate between the data and the commands.

Data and commands can be sent between the broker and the backend applications in one of several ways. If the application itself supports MQTT, or if it can be modified to support MQTT, the application can subscribe directly to the broker as a client. This approach enables you to use the MQTT Pub/Sub bidirectional messaging capability directly by using your application to receive data from and send commands to the connected devices.

If your application does not support MQTT, there are several other options. In the architecture described in this document, Apache Beam provides an MQTT driver, which allows bidirectional integration with Dataflow and other Beam deployments. Many brokers also have plugin capabilities that support integration with services like Google Pub/Sub. These are typically one-way integrations for data integration, although some brokers support bidirectional integration.

## Use cases

An MQTT broker architecture is particularly well suited for the device use cases that are described in the following sections.

### Standards-based data ingestion from heterogeneous devices

When you want to collect and analyze data from a large fleet of heterogeneous devices, an MQTT broker is often a good solution. Because MQTT is a widely adopted and implemented standard, many edge devices have built-in support for it, and lightweight MQTT clients are available to add MQTT support to devices that don't. The publish-and-subscribe paradigm is also a part of the MQTT standard, so MQTT-enabled devices can take advantage of this architecture without additional implementation work. By contrast, devices that connect to Pub/Sub must implement the Pub/Sub API or use the Pub/Sub SDK. Running a standards-compliant MQTT broker on Google Cloud thus provides a simple solution for collecting data from a wide range of devices.

When your connected devices are not controlled by your application but by a third party, you might not have access to the device system software, and the management of the device itself would be the other party's responsibility. In that circumstance, we recommend that you run an MQTT broker and provide authentication credentials to the third party to set up the device-to-cloud communication channel.

### Bidirectional communication for multi-party application integration

The bidirectional messaging capability of MQTT makes it very suitable for a multiparty-mobile-application use case such as on-demand food delivery or a large-scale web chat application. MQTT has low protocol overhead, and MQTT clients have low resource demands. MQTT also features publish-and-subscribe routing, multiple quality of service (QoS) levels, built-in message retention, and broad protocol support. An MQTT broker can be the core component of a scalable messaging platform for on-demand services applications and similar use cases.

### Edge-to-cloud integrated messaging

Because of the standardization and low overhead that MQTT offers, it can also be a good solution for integrating on-premises and cloud-based messaging applications. For instance, a factory operator can deploy multiple MQTT brokers in the on-premises environment to connect to sensors, machines, gateways, and other devices that are behind the firewall. The local MQTT broker can handle all bidirectional command and control and telemetry messaging for the on-premises infrastructure. The local broker can also be connected by two-way subscription to a parallel MQTT broker cluster in the cloud, allowing communication between the cloud and the edge environment without exposing the on-premises devices and systems to the public internet.

## What's next

  * Learn how to connect devices and build IoT applications on Google Cloud using [Intelligent Products Essentials](https://docs.cloud.google.com/architecture/intelligent-products-essentials-architecture).
  * Learn about practices for [automatically provisioning and configuring edge and bare metal systems and servers](https://docs.cloud.google.com/architecture/best-practices-provisioning-configuring-bare-metal).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-08-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-08-09 UTC."],[],[]] 
