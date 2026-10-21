---
url: https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/manufacturing-connect/
title: Manufacturing Connect \u00a0|\u00a0 Manufacturing Data Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:59:36.954829+00:00
---

# Manufacturing Connect  |  Manufacturing Data Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/manufacturing-data-engine/docs/concepts/manufacturing-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Manufacturing Data Engine ](https://docs.cloud.google.com/manufacturing-data-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/manufacturing-data-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manufacturing Connect

Manufacturing Connect (MC) is a software component designed by [Litmus Automation](http://www.litmus.io) and developed exclusively for Google Cloud. MC **solves factory connectivity** in a modern, scalable, and vendor independent way. With a library of [270+ supported automation protocols](https://mc-docs.litmus.io/manufacturing-connect-edge/industrial-systems-connection-guide) (and the option to add more), entire factories can be quickly connected to Manufacturing Data Engine (MDE).

In case a specific equipment is not covered in MC's [extensive library](https://mc-docs.litmus.io/manufacturing-connect-edge/industrial-systems-connection-guide), a new driver can be built by Litmus Automation upon request - typically in a few weeks.

MC has two principal components:

  * **Manufacturing Connect edge (MCe)** : A software stack that is deployed within the factory.
  * **MC** : A cloud-based app that deploys in customers' Google Cloud tenants for managing all edge instances _and_ MDE from a single web interface.



![mc](https://docs.cloud.google.com/static/manufacturing-data-engine/images/mc.png)

## Relationship with MDE

  * **For customers using both MC and MDE** : The MC web interface includes the interface to MDE, enabling a seamless edge-to-cloud user experience.

  * **For customers using MDE only (without MC)** : Starting with MDE v1.3, a standalone web interface for MDE is included in the release package. Like in previous releases, API-based configuration and management remains available in addition to the web interface.




## Factory network connection

MC can be deployed in multiple ways to comply with your factory network topology. Both Google and our partner Litmus Automation are happy to advise you on the best model for your circumstances:

  * Decentralized (close to individual lines) or centralized (such as in a factory data center).
  * As a container, virtual machine (VM), or operating system.

**Note:** MC is compatible with GKE Enterprise environments.

## Node RED component

MCe offers an analytics editor based on Node RED integration. It comes with a number of common transformations, KPI calculations, and basic threshold-based rules. Using it is entirely optional, but supports customers that like to do some initial calculations at the edge to provide calculated values with low latency (and independent of internet connection status) to other on-premise systems (such as Manufacturing Execution Systems (MES)).

## Integration with other edge systems

SCADA and MES systems are typically designed with integration in mind, and offer interfaces that IMC can connect to (such as OPC UA, Modbus, and more). These systems often contain beneficial metadata (for example, active recipe on the manufacturing line) that is important to store on Google Cloud to process machine sensor data in the right context.

You can set the sampling rate from Programmable Logic Controllers (PLCs) and transmission rate for data upload to Google Cloud. Sampling rate can be defined in MC (up to many times per second). Data upload to Google Cloud is generally event-driven, typically once per second.

### PLCs connection from one edge deployment

Depends on the underlying hardware or virtual machine size, and additional factors such as sampling rate. Generally 10,000 tags (PLC register values) per edge deployment are a good rule of thumb to work with.

## Manufacturing Connect edge (MCe)

MCe acts as a bridge between the physical world of your factory and the digital world of Google Cloud, enabling you to use data for improved efficiency, productivity, and insights.

### Hardware requirements

The setup of MC and MCe typically take a few hours at most, including connecting to a number of PLCs. A key driver of the overall timeline is obtaining and setting up firewall permissions. Some customers are able to complete this within a day, while others take a few weeks to navigate company-internal processes.

For more information about hardware requirements, see the [MCe Installation and Configuration overview](https://mc-docs.litmus.io/manufacturing-connect-edge).

### Secure connection

Communication between MCe and Google Cloud are performed over PKI encrypted channels for Pub/Sub. The Pub/Sub connection is authenticated using a service account key.

Additionally to the encryption, the network traffic between MC and Pub/Sub can be routed through private connectivity options between onPrem and Cloud (Interconnect or VPN) to private endpoints of Google APIs. In such a scenario, the traffic between corporate networks and Google Cloud is not crossing the public internet by being processed only within the customer's private network perimeters.

## Litmus Automation

Google partnered with Litmus Automation to create the MC, an integrated edge-to-cloud offering in a Google Cloud exclusive product. However, MC is sold, supported, and maintained by Litmus Automation. With the deep integration with MDE, customers benefit from ease of use and speed to deploy.

For updating MCe, Litmus provides updated files that can be rolled out to edge deployments. Configurations are persisted between updates (when using official release versions).

You can direct any questions to the following help resources by Litmus Automation:

  * [Manufacturing Connect on Google Cloud Marketplace](https://console.cloud.google.com/marketplace/product/litmus-public/intelligent-manufacturing-connect).
  * [Litmus Automation Help Center](https://mfgconnect.litmus.io/hc/en-us) including documentation and contact for enquiries and support.
  * [Supported protocols and drivers](https://mc-docs.litmus.io/manufacturing-connect-edge/industrial-systems-connection-guide).

**Note:** Besides MC, Google offers various alternative partner-based solutions (such as OSIsoft) with ready-to-use connectors to set up factory-to-cloud connectivity. Additionally, MDE can be integrated with most custom edge stacks as required.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
