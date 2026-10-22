---
url: https://docs.cloud.google.com/app-hub/docs/key-concepts/
title: Key concepts \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:16.201988+00:00
---

# Key concepts  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/key-concepts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  Key concepts Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the key terms and concepts related to [Application-centric Google Cloud](https://docs.cloud.google.com/app-hub/docs/application-centric-google-cloud).

## Application (also, App Hub application)

A logical grouping of services and workloads that together deliver a business function. In this grouping, services expose the end-to-end business functionality that workloads provide. For example, you can group all of the components that make up your online store or your chatbot into a single application.

  * In App Hub, you define applications by grouping existing Google Cloud resources as application components.

  * In Application Design Center, you define applications by creating, customizing, and configuring an instance of an application template called an application draft. You can then deploy the application from that draft. [Learn about using App Design Center](https://docs.cloud.google.com/application-design-center/docs/overview#how-to-use).




## Application management boundary (also, boundary)

The collection of one or more Google Cloud projects or folders whose underlying resources App Hub can discover and you can group in applications. This collection defines the boundary where App Hub can manage application components.

You define the configuration of this boundary. For example, you can set the boundary to a single project or an entire folder of projects. To learn which application setup model best fits your business needs, see [Choose your application setup model](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub).

During setup, you define this boundary by creating attachments within the management project.

## App-enabled folder

A Google Cloud folder that you configure to act as an application management boundary. This folder contains a management project to manage the applications within it.

## Asset

In Application Design Center, a component that provides supporting resources for an application, such as for managing access controls or configurations. For example, an asset can be a service account that acts as an identity to control access permissions for your application, or a Secret Manager secret that you use to manage API keys securely.

To learn which resources you can add and configure as application components, see [the list of App Design Center supported assets](https://docs.cloud.google.com/application-design-center/docs/supported-resources).

## Attachment

A persistent configuration that you create within a management project to add a project or folder as a member of the application management boundary. 

You must attach a project or a folder to the management project to make them part of the boundary. For single project and folder attachments, App Hub automatically manages the integration to the boundary. For all other attachments, you must create them manually.

## Catalog

In Application Design Center, a collection of templates that you can share between different spaces.

## Component (also, application component)

A [Google Cloud resource](https://docs.cloud.google.com/docs/overview#gcp_resources) that you use to compose an application. Components are categorized as services, workloads, or assets.

  * In App Hub, you discover resources within the application management boundary that can function as services or workloads. You can then register these resources as components of an application.

  * In Application Design Center, you use components as building blocks to create reusable application templates. You can then deploy standardized application infrastructure from these templates.




## Design canvas

In Application Design Center, the interface that you use to add components and create an application diagram.

## Draft (also, application draft)

In Application Design Center, an instance that you create from a template. You can customize and deploy your application draft.

## Host project (Legacy)

A Google Cloud project that you choose to act as the central management point for App Hub applications. To make a project a host project, you typically enable the App Hub API on this specific project and then grant it permissions to access other projects.

After you've set up a host project, you manually connect other Google Cloud projects, known as service projects, to it. This connection is what allows App Hub to see and manage the resources residing in those service projects, enabling you to group them into logical applications within App Hub.

The host project is a legacy application setup model. In this legacy model, the host project is equivalent to the management project, and the collection of the host project and service projects serves as an example of a multiple-project application management boundary.

## Management project

A Google Cloud project that centralizes all application management tasks and metadata. In the Google Cloud console, the management project of a folder-level boundary has a unique icon (![ ](https://docs.cloud.google.com/static/hub/images/mgmt-project.png)). In this project you manage APIs, access control, billing, quotas, and define your application management boundary.

To learn how to incorporate the management project in your Google Cloud resource hierarchy, see [Choose your application setup model](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub).

An application management boundary set to a single project is defined as a standalone management project because you attach the project to itself for this boundary type. 

## Service

An application component that refers to a network or API interface that exposes functionality to clients. Services act as interfaces to workloads. For example, a service can be a load balancer that exposes a stable IP address and port, a Pub/Sub topic, or a Vertex AI model.

App Hub supports two registration type (`RegistrationType`) property values for services:

  * **Exclusive** (`EXCLUSIVE`): services that you can only register to one application.
  * **Shared** (`SHARED`): services that you can register to multiple applications.

Shared services support foundational infrastructure components like GKE clusters that are inherently shared across multiple applications. Even after being registered to an application, shared services can have a _discovered_ [registration status](https://docs.cloud.google.com/app-hub/docs/overview#registration-status) in App Hub for other applications to use them.




To learn which resources you can register as exclusive or shared services, see [the list of App Hub supported services](https://docs.cloud.google.com/app-hub/docs/supported-resources#services).

To learn which resources you can add and configure as application components, see [the list of App Design Center supported services](https://docs.cloud.google.com/application-design-center/docs/supported-resources).

The registration type is an output-only field that you cannot modify. For more information about the registration type property, see [Properties and attributes](https://docs.cloud.google.com/app-hub/docs/overview#properties-and-attributes).

## Service project (Legacy)

A Google Cloud project that contains application components your applications use, such as virtual machines, Google Kubernetes Engine clusters, or load balancers.

To let App Hub see and manage these resources, you must manually connect this service project to a host project. A service project can only be connected to one host project at a time.

The service project concept is part of a legacy model. In this model, the combination of the host project and all of its connected service projects forms a multiple-project application management boundary.

## Space

In Application Design Center, a dedicated area for a team to collaborate, create templates, and deploy applications.

## Template (also, application template)

In Application Design Center, a reusable and deployable architecture for an application that you build using application components. An application template can be one of the following types:

  * [Standard](https://docs.cloud.google.com/application-design-center/docs/design-application-templates): consists of components and connections.
  * [Composite](https://docs.cloud.google.com/application-design-center/docs/design-composite-templates): consists of standard application templates, components, and connections.



## Workload

An application component that provides compute resources to run the binary deployments and code for a discrete part of an application's business logic. For example, a workload for an ecommerce application might handle payment processing and run as a Google Kubernetes Engine deployment or a Compute Engine managed instance group (MIG). A workload for an AI agent might have functional type and extended metadata [properties](https://docs.cloud.google.com/app-hub/docs/overview#properties-and-attributes).

To learn which resources you can register as workloads, see [the list of App Hub supported workloads](https://docs.cloud.google.com/app-hub/docs/supported-resources#workloads).

To learn which resources you can add and configure as application components, see [the list of App Design Center supported workloads](https://docs.cloud.google.com/application-design-center/docs/supported-resources).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
