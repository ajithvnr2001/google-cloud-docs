---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/overview/
title: About Google Distributed Cloud air-gapped appliance \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:15.898901+00:00
---

# About Google Distributed Cloud air-gapped appliance  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  About Google Distributed Cloud air-gapped appliance Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud (GDC) air-gapped appliance is an integrated hardware and software platform designed for tactical edge environments outside a data center. It creates an isolated "sovereign cloud in a box" that is physically disconnected from the internet. This appliance lets you deploy virtual machines (VMs), container-based workloads, and managed services like Vertex AI within a secure and air-gapped environment.

The appliance weighs about 100 lbs (~45.3 kg) and can be carried by two people. The appliance is not operational while it is moved from one location to the next. It might be moved on and off vehicles and might be subject to rougher treatment than in a data center. While the appliance is running, it might be in an uncontrolled environment subject to more temperature variations and dust than a data center, such as a tent or a repurposed building.

The device can run disconnected on an air-gapped customer network with access to other resources, or a local network without an uplink. It can also run connected to a network that is routable to a Distributed Cloud data center instance.

Google Distributed Cloud air-gapped appliance offers the following features:

**Advanced AI capabilities** : Enhance the performance of mission-critical applications by using built-in [AI solutions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-overview) like translation, speech, and optical character recognition (OCR). For example, use OCR and translation features to scan and translate documents written in different languages, making them accessible and understandable in the field.

**Rugged and portable design** : Built to withstand harsh environmental conditions, including extreme temperatures, shock, and vibration, Google Distributed Cloud air-gapped appliance has a rugged and portable design that meets stringent accreditation requirements like MIL-STD-810H, ensuring reliable operation even in challenging scenarios.

**Full isolation** : Designed to operate without any connectivity to Google Cloud or the public internet. The appliance remains fully functional in disconnected environments, such as DDIL, preserving the security and isolation of the infrastructure, services, and the APIs that it manages. This isolation makes the appliance ideal for processing sensitive data, while meeting strict regulatory, compliance, and sovereignty requirements.

**Integrated cloud services** : Infrastructure-as-a-services (IaaS) features like compute, networking, and storage, and Google Cloud services like data transfer.

**Data security** : Robust security features like encryption, data isolation, firewalls, and secure boot to protect sensitive information.

**Department of Defense (DoD) Impact Level 5 (IL5) accreditation** : The appliance achieved Impact Level 5 accreditation, the highest level of security controls and protection required for unclassified, but sensitive information.

## Differences between GDC air-gapped appliance and GDC air-gapped

There are several key differences between GDC air-gapped appliance and GDC air-gapped running in a data center.

### Tenancy

The appliance is single tenant and only supports one GDC air-gapped organization.

### Cluster model

Google Distributed Cloud air-gapped appliance operates a single cluster that encompasses all three of its bare metal nodes. A dedicated management API server, which runs as pod workloads on the cluster, hosts management plane APIs. User workloads, which include both VMs and Kubernetes pods, can run on this cluster.

### Networking

GDC air-gapped appliance devices have a different integration pattern with customer networks than data center installations. Data center devices are typically installed complete with a network configuration plan authored and implemented by networking professionals. GDC air-gapped appliance devices are typically brought to a location and plugged into an existing customer network. The network that the device is connected to changes as the device is moved from one location to another. Though the appliance uses different networking hardware than the data center solution, you can connect the appliance to an external network using the provided hardware.

### System management

GDC air-gapped appliance has a different lifecycle from the GDC air-gapped data center. For the appliance, Google (or our delegates) installs the system, and then hands it to the customer. The customer performs some Infrastructure Operator (IO) configuration tasks such as configuring identity and networking, and then can use the device. The customer is responsible for several IO tasks such as update or system monitoring.

## Hardware

**Important:** To access the URLs on this page, you must connect to the internet. The URLs are provided for use when you have such access.

GDC air-gapped appliance is a small form factor device that consists of a chassis that holds three blades and a networking switch. The case has carry handles and wheels so that it can be transported and used in rugged environments.

### Hardware components

The front profile of the appliance has a switch on the top with blades in the middle and power outlets at the bottom:

  * A: TOR switch
  * B: Three server blades
  * C: Power supply unit with redundancy
  * D: HP Edgeline system



![Front profile of the appliance](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/appliance/images/front_profile.png)

## Software

GDC air-gapped appliance offers the following software and services:

### Services

The available services include the following:

  * Compute 
    * [Virtual machine](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vms/vm-introduction) hosting
    * GKE on GDC for deploying [containers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/containers/containers-intro)
  * AI/ML 
    * [Vertex AI OCR](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-ocr) API
    * [Vertex AI Speech-to-Text](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-stt) API
    * [Vertex AI Translate](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/application/ao-user/vertex-ai-translation) API
    * [Machine learning](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/user/dl-container) using a Google-provided deep learning container
  * Security 
    * [Identity and access management](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/connect-identity)
    * [Encryption at transit and at rest](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/encrypt-data)
  * Storage 
    * [Block and object storage](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/storage-overview)
  * Networking 
    * Load balancing (internal and external)
    * Network security policies
  * [Logging and monitoring](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/obs-overview)



### Storage

GDC air-gapped appliance provides block and object storage with software-defined storage. Block and object storage share the same underlying storage pool and capacity. 

### NTP server

GDC air-gapped appliance does not have a built-in NTP server, but customers can provide their own NTP server. The network switch can act as an NTP relay when there is an upstream NTP server. Customers can point the network NTP switch to a NTP server on the local network.

### Data transfer and replication

GDC air-gapped appliance can transfer data to and from GDC air-gapped private clouds. As the devices are used in the field or remote locations, data might be required in the field while disconnected, and then transferred from the cloud to the device when connected.

### User interface

GDC air-gapped appliance uses a similar user interface as GDC air-gapped, without the features that are not included in GDC air-gapped appliance.

### Logging and observability

GDC air-gapped appliance keeps an audit log of system access events. This log does not require writing to special media such as write-once, read-many (WORM) compliant storage. The audit log manually syncs to GDC air-gapped when a connection is available and is stored in a common location with GDC air-gapped logs.

For broader logging and observability, raw system logs are available for the device logs and are accessible to administrators. Application Operators can use Kubernetes logging for their workloads.

### Security and encryption

GDC air-gapped appliance includes a set of Yubikeys for disk encryption, shipped separately from the appliance. If the customer has a Hardware Security Module (HSM) available, the system supports storing keys in that HSM. This allows customer control of keys for encrypting data at rest.

### Identity and access

GDC air-gapped appliance devices are delivered with an embedded Keycloak identity provider optionally installed with an administrator account. You can also connect to your own external identity provider. Administrators can add users in Keycloak or their own identity provider and grant permissions in the GDC console.

### HA and backup

GDC air-gapped appliance has limited high availability and redundancy for data storage.

## Personas

In Google Distributed Cloud air-gapped appliance, there are four personas:

  * **Google Infrastructure Operators**(G_IO) install the system hardware and software and perform the initial configuration before delivering the device to customers. They also securely wipe the device when returned.
  * **Customer Infra Operators** (C_IO) manage the system including authentication, networking, and system configuration.
  * **Platform Administrators** (PA) grant permissions to AO users, manage projects, and troubleshoot VMs and clusters.
  * **Application Operators** (AO) manage workloads, applications, and projects.



Personas are not roles but are collections of user roles mapped to specific permissions, which are assigned to individual users.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
