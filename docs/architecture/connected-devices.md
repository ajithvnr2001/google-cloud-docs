---
url: https://docs.cloud.google.com/architecture/connected-devices/
title: Connected device architectures on Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:07.463435+00:00
---

# Connected device architectures on Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/connected-devices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Connected device architectures on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-09-09 UTC

To maximize the value of data from their connected devices, organizations need to be able to perform data analysis. There are many ways for organizations to connect their devices to their analytics applications, and the benefits of specific connected device architectures can vary depending on the use case of your organization. To help guide you, this document describes a set of connected device architectures on Google Cloud. These architectures address a broad range of use cases and requirements for connected devices.

This document is part of a series of documents that provide information about IoT architectures on Google Cloud. The other documents in this series include the following:

  * Connected device architectures on Google Cloud overview (this document).
  * [A standalone MQTT Broker](https://docs.cloud.google.com/architecture/connected-devices/mqtt-broker-architecture): An [MQTT](https://mqtt.org/) broker provides bidirectional communication between connected devices and Google Cloud projects, and between the devices.
  * [An IoT platform architecture on Google Cloud:](https://docs.cloud.google.com/architecture/connected-devices/iot-platform-product-architecture) An IoT platform provides additional device management capabilities along with data connectivity, which is important when you deploy a large fleet of connected devices.
  * [A direct connection to Pub/Sub](https://docs.cloud.google.com/architecture/connected-devices/device-pubsub-architecture): For data ingestion, the best choice might be for your devices to connect directly to Pub/Sub.
  * [Best practices for running an IoT backend on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/bps-running-iot-backend-securely).
  * [Best practices for automatically provisioning and configuring edge and bare metal systems and servers](https://docs.cloud.google.com/architecture/connected-devices/best-practices-provisioning-configuring-bare-metal).



## Connected device architectures summary

This document groups connected device use cases into three categories, based on the following dimensions that you need to consider when you plan a connected device architecture:

  * **Number of devices:** It's important to consider how many devices are directly connected to your application. If your application has many end devices (such as machines, sensors, or cameras), and if these devices are connected to an intermediate gateway or other device (such as a mobile phone), it's important to identify whether those end devices must be represented and managed in your application. In some cases you might need to represent each individual device; in other cases, only the intermediate device might need to be represented.

  * **Fleet management:** Consider whether you need capabilities like device status monitoring, software and firmware updates, configuration management, and other fleet management features. These requirements help to determine your choice of application architecture.

  * **Inter-device messaging:** Device communication through your application architecture is an important factor. For example, some applications depend on communication between the connected devices through your application architecture. Other applications have data flows that occur strictly between each device and your application, with no messaging between devices.




## Summary table

Understanding the characteristics of your application can help you to choose the best architecture for your use case. To help guide your choice, the following table summarizes the support that each of the connected architectures that are described in this series offers:

| Device support limits | Inter-device messaging | Fleet management support  
---|---|---|---  
MQTT Broker | Millions | Recommended | Not supported  
IoT platform | Millions | Some support | Recommended  
Device to Pub/Sub | Hundreds | Some support | Not supported  
  
## What's next

  * Read about the best connected device architecture for your use case: 
    * [A standalone MQTT Broker](https://docs.cloud.google.com/architecture/connected-devices/mqtt-broker-architecture):
    * [An IoT platform architecture on Google Cloud](https://docs.cloud.google.com/architecture/connected-devices/iot-platform-product-architecture).
    * [A direct connection to Pub/Sub](https://docs.cloud.google.com/architecture/connected-devices/device-pubsub-architecture).
  * Learn how to connect devices and build IoT applications on Google Cloud using [Intelligent Products Essentials](https://docs.cloud.google.com/architecture/intelligent-products-essentials-architecture).
  * Learn about practices for [automatically provisioning and configuring edge and bare metal systems and servers](https://docs.cloud.google.com/architecture/best-practices-provisioning-configuring-bare-metal).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-09-09 UTC."],[],[]] 
