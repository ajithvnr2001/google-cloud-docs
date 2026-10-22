---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/overview/
title: Overview \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:49.499332+00:00
---

# Overview  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Overview

Manufacturing Data Engine (MDE) is an end-to-end solution that delivers scalable and seamless connectivity between the factory floor and the cloud, in combination with [Manufacturing Connect (MC)](https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/manufacturing-connect).

MDE provides a zero code pre-configured set of Google Cloud infrastructure that is able to ingest, process, and store data from industrial devices in the cloud based on the user's configuration. After the machine and processed data is available in Google Cloud, it is possible to use Google Cloud tools and technologies to extract value from that data.

Acquiring industrial data has traditionally been a high-complexity and high-cost process that adds unnecessary time and cost to any cloud-based industrial information management use case. MDE is a flexible solution that makes that process shorter, more efficient, and more predictable.

MDE handles the end-to-end need of ingesting, contextualizing, storing, and using factory data on the cloud. Together with Manufacturing Connect (MC), it also extends directly to the source of data - the machines and systems on the factory floor, across any automation vendor standard.

MDE is delivered as a packaged solution. A script deploys all the required components and the integration code into your Google Cloud project. This unlocks maximum flexibility for you to modify and extend the architecture based on your needs.

## Manufacturing solutions

MDE is a core component within a suite of interconnected manufacturing solutions. While some other components can function independently, its true power lies in its integration. These components work together to create a comprehensive manufacturing data platform. Data is collected, processed, analyzed, and used to drive insights and improve operational performance.

![Manufacturing solutions high level overview](https://docs.cloud.google.com/static/manufacturing-data-engine/images/go-cortex-mfg-l100.png)

The end-to-end suite is composed of components built by Google and components built by Litmus Automation exclusively for Google.

  * **Manufacturing Data Engine** : It serves as the acquisition, transformation and storage layer of the suite. MDE provides a secure, efficient and reliable data lake containing all manufacturing information, and acts as a data hub for all use cases to connect and access manufacturing information.
  * **Manufacturing Connect (MC)** : Cloud component to remotely manage all Manufacturing Connect edge (MCe) instances. It also acts as a web interface for the configuration of the MDE solution. For more information, see [MC documentation (opens in a new tab)](https://mc-docs.litmus.io/).

**Note:** A standalone web interface for MDE is available as well for customers without MC or MCe.
  * **Manufacturing Connect edge (MCe)** : Edge to cloud gateway capable of translating more than 270 industrial communication protocols into standardized Pub/Sub messages. Additional features include edge processing and storage capabilities. For more information, see [MCe documentation (opens in a new tab)](https://mc-docs.litmus.io/manufacturing-connect-edge).

  * **Manufacturing Analytics and Insights** : A prebuilt LookerML integration with MDE. It enables immediately using Looker as BI tool to explore and analyze MDE factory data.

  * **Machine Anomaly Detection** : Based on Time Series Insights API.

  * **Visual Inspection AI** : An edge solution based on the Cloud Vision API.




The components of the manufacturing suite are designed to work seamlessly together. They share a common configuration and are semantically interoperable, ensuring smooth data flow and consistent behavior across the suite. However, you also have the **flexibility to use these components individually** based on your specific needs.

MDE and the rest of the components are configurable. Users can define their specific data requirements and the system adjusts to those specifications without having to modify the code underlying the solution. Configuration can be updated using the MC user interface, the standalone MDE web interface, or the MDE configuration API.

## Key benefits

The key benefits of MDE include:

  * **Time-to-value** : Fast deployment in standard Google Cloud environments. Machine connectivity (if not yet in place) can be also quickly set up using MC.
  * **Scalability** : Useful from Proof of Concepts (PoCs) to global enterprise deployments across hundreds of factories.
  * **Efficiency** : By capturing data once in MDE as a "factory abstraction layer", all use cases can be driven from MDE. Fine-grained control over storage and processing enables cost efficient setups.
  * **Full flexibility** : Can work with any edge stack, just requires data to land in Pub/Sub directly or using Message Queuing Telemetry Transport (MQTT) bridge, with custom definition parsers to map incoming data schemas to the MDE standard.
  * **Adaptability** : As MDE deploys fully in your own Google Cloud tenant project, all MDE components (such as Pub/Sub, Dataflow, and BigQuery) are transparent and can be used as if you had built the platform yourself.
  * **Ownership** : Since all the components of MDE are deployed within your Google Cloud tenant project, you remain in full control over your data and processing.
  * **Extensibility** : All Google Cloud integrations (such as BigQuery connectors) are usable with MDE by default. You can additionally enable MDE-specific extensions for specific use cases (built by Google or partners) and build your own.
  * **Cost-Effective** : There are no extra costs for using MDE. You only pay for your cloud consumption, which starts at a minimal level for PoCs. However, consider that using MC incurs an additional cost. For more information, see [MC Cloud Marketplace](https://console.cloud.google.com/marketplace/product/litmus-public/intelligent-manufacturing-connect).



## Use cases

Production planning, order tracking, progress, and process parameter control are use cases that are typically covered by automation systems. We seek to augment and complement, rather than replace such systems. With Google Cloud you can gain valuable new insights that can be fed into your existing automation systems, such as SCADA, allowing you to take action and improve OEE and other important KPIs.

When it comes to Manufacturing Execution Systems (MES), companies have different approaches. Some stick with their existing on-premise MES, while others are moving to cloud-based solutions. MDE is a solid foundation to quickly implement key MES features if required.

The use cases enabled by MDE fall primarily into three categories:

  * **Analytical use cases** : Combine MDE with Google Cloud data analytics products to produce reports, calculate KPIs, and create real-time dashboards using data streamed from the manufacturing floor.
  * **Machine learning use cases** : Build on Google Cloud Machine Learning (ML) products and platforms to create, train, and execute ML models that are relevant to optimize any aspect of the manufacturing operation.
  * **Integration use cases** : Connect manufacturing data with digital twin solutions or other enterprise systems to provide an integrated view of the manufacturing data with other perspectives available in the company.



## Capabilities

MDE fulfills the following capabilities:

  * **Data ingestion** : Either from MC or any other commercial or proprietary edge stack.
  * **Edge Data Processing** : MCe processes and stores data locally for immediate analysis.
  * **Cloud Data Integration** : MC transforms data into MQTT and Pub/Sub messages, seamlessly integrating with Google Cloud.
  * **Syntactic standardization** : Uses standard data storage schemas for a variety of data archetypes, driving reusability of the data across use cases such as: 
    * Self-service analytics for factory managers and maintenance personnel.
    * Fully managed, ML-based anomaly detection that can be enabled for individual sensor streams (automatic fingerprinting, no setup required).
  * **Semantic flexibility** : Uses integrated data contextualization engine to optionally enrich incoming sensors or variable data streams, enabling multiple user-definable contextualization perspectives based on the following standards: 
    * ISA-95 hierarchy
    * Digital Twins Definition Language (DTDL)
    * OPC Unified Architecture (OPC-UA) companion specs
    * Asset Administration Shell (AAS)
  * **Data Transformation and Enrichment** : Maps, transforms, and contextualizes data according to user-defined schemas.
  * **Real-time Analytics** : Calculates streaming analytics and transformations based on user configurations.
  * **Data Storage and Output** : Stores processed data in BigQuery, Bigtable, and Cloud Storage, and outputs to Pub/Sub.
  * **Monitoring and Management** : Provides a user-friendly interface to monitor and manage the entire solution.
  * **Flexible Configuration** : Offers a straightforward interface for configuring data flows and processing pipelines.
  * **Accessible through API and web interface** : for programmatic access, automation, and management.



## Components

![high-level-architecture](https://docs.cloud.google.com/static/manufacturing-data-engine/images/architecture.png)

The following are components of MDE:

  * **Configuration Manager** : Manages the user configurations and exposes them to other solution components.
  * **Message Mapper** : Processes incoming messages and classifies them into source message classes, as well as performs Whistle transformations.
  * **Metadata Manager** : Manages metadata buckets and instances, and participates in record processing.
  * **Batch Ingestion Cloud Storage Bucket** : Bucket for uploading files for batch ingestion.
  * **Cloud Storage Reader** : Responsible for reading batch data from files uploaded to Cloud Storage.
  * **Cloud Storage Writer** : Responsible for writing raw source messages to the Cloud Storage archive, as well as processed records to the Cloud Storage sink.
  * **Bigtable Writer** : Responsible for writing records to the Bigtable sink.
  * **BigQuery Writer** : Responsible for writing records to the BigQuery sink.
  * **Pub/Sub Topics** : Pub/Sub is the message broker of MDE that is used to route messages between the different components of the solution. Several topics and subscriptions are created to ensure the routing of the incoming messages is done according to the user configuration. All messages arrive in the system using the `input-messages` topic.
  * **Databases and Storage** : MDE manages BigQuery datasets, Bigtable tables, and Cloud Storage objects.
  * **Federation API** : MDE provides an API to access all data repositories using a common interface. This allows users to query their data independently of where it is stored and enables them using the same configuration language to create specific queries to the manufacturing information.



## Data engine in the factory

Typically a single instance of MDE would serve all factories. The underlying Google Cloud components (such as Pub/Sub) are global and scalable to enable this approach. If you choose to still deploy multiple instances, Google Cloud database products such as BigQuery enable accessing global data across multiple instances. The Manufacturing Connect edge (MCe) instances are deployed as gateways usually on factory level. Multiple MCe can be interconnected by using the built-in NATS integration.

### Use of MES for machine performance, events and traceability

MDE complements your existing MES system rather than replacing it. It uses it as a data source and sink. MDE gets important context or metadata from it (such as active recipe, schedules, events, and others), and uses these data points as tags similar to sensor values. This context data is required to make sense of the machine sensor data (for example, the expected sensor pattern is different based on the recipe. That is, what the machine is producing). MDE output (for example, ML predictions) can absolutely be integrated back to the MES, for example for alerting.

### Integration of MQTT with MDE

There are several options in the Google Cloud marketplace, which among other factors, depend on the MQTT broker vendor. [HiveMQ](https://www.hivemq.com/solutions/the-leading-mqtt-broker-primed-for-google-cloud/), for example, provides a Pub/Sub extension. You can also build your own custom MQTT bridge or use [Dataflow](https://docs.cloud.google.com/dataflow/docs/guides/templates/provided/mqtt-to-pubsub).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
