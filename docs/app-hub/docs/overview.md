---
url: https://docs.cloud.google.com/app-hub/docs/overview/
title: App Hub overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:45:15.191651+00:00
---

# App Hub overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  App Hub overview Stay organized with collections  Save and categorize content based on your preferences. 

As you develop your cloud infrastructure, you might organize your Google Cloud resources across multiple projects. You might also have many resources within one or multiple projects that provide an integrated business function that you want to group logically. The resource hierarchy in Google Cloud can make it challenging to manage and organize your infrastructure for these grouping purposes. App Hub provides an application-centric way to group and manage services and workloads, helping you align your infrastructure with your business functions.

App Hub acts as the foundational data model and central registry for your applications on Google Cloud. It creates a single source of truth that clarifies resource ownership, dependencies, and business context. This, in turn, supports other Google Cloud products with the application-centric context they need. For more information about this application-centric model and its features, see [Application-centric Google Cloud](https://docs.cloud.google.com/app-hub/docs/application-centric-google-cloud).

This document provides a conceptual overview of App Hub to help you understand its capabilities and benefits before you set up or administer it.

## Why use App Hub?

By shifting the focus from individual infrastructure resources to the applications they form, App Hub helps you streamline governance and operations at scale.

App Hub helps you implement the following application-centric capabilities:

  * **Streamline resource registration** : Register at once multiple services and workloads to an application. The limit for services and workloads that you can register at a time is 10.

  * **Organize and catalog your applications** : Group scattered Google Cloud resources from one or more projects into logical App Hub applications. You can then find properties and categorize these applications with attributes like owners, business criticality, and environment to improve discoverability and accountability. For more information, see Properties and attributes.

  * **Create a unified view for your teams** : By defining an application in App Hub, you provide essential context to other Google Cloud products. For example, you might enable the following features:

    * A central view of operations and insights in [Cloud Hub](https://docs.cloud.google.com/hub/docs/app-project-views), which displays alerts, incidents, and performance data in an application context.
    * AI-powered assistance from [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview), which uses App Hub's data model to help you design, operate, and troubleshoot your applications.
    * Application monitoring with [Google Cloud Observability](https://docs.cloud.google.com/stackdriver/docs/observability/about-application-monitoring) to help you troubleshoot errors and improve performance by displaying telemetry data for your applications and their components.
  * **Clarify ownership and dependencies** : Understand how your applications are composed and how their components depend on each other. This feature helps developers and operators visualize application architecture, identify owners, and resolve issues.




To learn more about how App Hub fits into the broader application lifecycle, see [Application-centric Google Cloud](https://docs.cloud.google.com/app-hub/docs/application-centric-google-cloud).

## App Hub concepts and data model

App Hub is built on a data model based on the following key concepts: applications, services, and workloads. These terms are common in the industry, but App Hub uses them in a specific way.

The following table compares the App Hub definition with common industry usage:

**Concept** | **App Hub definition** | **Common industry usage**  
---|---|---  
**Application** | A logical grouping of services and workloads that together deliver a business function.  | Can refer to a single deployable unit, a codebase, or a broad system.   
**Service** | A network or API interface that exposes functionality to clients and can route requests to workloads, such as a load balancer. Some services, such as GKE clusters, are designated as [shared services](https://docs.cloud.google.com/app-hub/docs/key-concepts#service) that you can register to multiple applications. This is indicated by their registration type property.  | Often refers to a microservice, a deployable component, or binary code with its own business logic and data.   
**Workload** | The compute resources where the binary deployments of your application are installed. The application code from these resources performs a discrete part of your business logic. For example, a workload can be a GKE deployment or a Compute Engine managed instance group (MIG) running the code of an AI agent.  | A more general term for any process or component that consumes computing resources.   
  
For more information about these and other Application-centric Google Cloud central concepts, see [Key concepts](https://docs.cloud.google.com/app-hub/docs/key-concepts). For a list of supported resources in App Hub that you can register as services or workloads in your applications, see [App Hub supported resources](https://docs.cloud.google.com/app-hub/docs/supported-resources).

You can define App Hub applications based on your geographic distribution requirements. Your location choice impacts which services and workloads you can register in applications and can be important for data residency requirements. You can designate the following locations:

  * **Global applications:** group services and workloads from multiple Google Cloud regions.
  * **Regional applications:** group services and workloads that all reside within a single region.



For a detailed comparison to help you choose the right location, see [Global and regional applications](https://docs.cloud.google.com/app-hub/docs/global-regional-applications).

Services and workloads show a registration status in your applications. Additionally, applications, services, and workloads can contain metadata in the form of properties and attributes.

You can view details of your deployed applications and their services and workloads, including location, registration status, and metadata. For more information, see [View details of services and workloads](https://docs.cloud.google.com/app-hub/docs/modify-app-hub-resources#view) and [View application details](https://docs.cloud.google.com/app-hub/docs/manage-applications#view-details).

### Registration status of services and workloads

The organizational structure of your Google Cloud resources affects how App Hub can manage services and workloads and lets you register them in applications. Services and workloads that you can [register](https://docs.cloud.google.com/app-hub/docs/register-resources) to an application have one of the following registration status:

  * **Discovered** : Services and workloads that you can register to an application because they are part of the [application management boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary) and that aren't registered to any other application or can be registered to multiple applications. The discovered status also includes services and workloads that you delete or unregister from an application but that you can register again.

**Note:** Even if you have registered shared services to an application, they can have a registration status of _discovered_ in other applications.
  * **Registered** : Services and workloads registered to an application and managed by App Hub. You can only register discovered services and workloads. After you register the service or workload, the registration status updates from _discovered_ to _registered_.

  * **Detached** : Services or workloads that have been registered to an application, but that App Hub can't manage or monitor because their underlying Google Cloud resources are no longer part of the application management boundary that you have defined. The registration status of services and workloads registered to an application can change to _detached_ for the following reasons:

    * The underlying resource is deleted. For example, if you delete a forwarding rule represented by a service, the service's registration status changes to _detached_.
    * A project or folder containing underlying resources for registered services or workloads is moved out of the application management boundary.

Detached services and workloads remain in the application until you [unregister](https://docs.cloud.google.com/app-hub/docs/modify-app-hub-resources#unregister) them.

If you move a project out of the application management boundary, its detached services and workloads can become discoverable for applications in a different boundary. You can [register](https://docs.cloud.google.com/app-hub/docs/register-resources#register-services-and-workloads) discoverable services and workloads again, adhering to the [resource hierarchy](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#resource-hierarchy) established by the application management boundary.




To select an application management boundary that fits your resource hierarchy in Google Cloud and let App Hub discover and register the services and workloads that your business needs, see [Choose your application setup model](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub). To view the registration status of services and workloads, see [View details of services and workloads](https://docs.cloud.google.com/app-hub/docs/modify-app-hub-resources#view).

### Properties and attributes

To enrich the data model, App Hub lets you expose properties and attributes to support application discoverability, accountability, and governance. Defining these values as application metadata helps you filter, manage, and apply policies to your application components at scale.

To view the properties and attributes of the services and workloads in your applications, see [View details of services and workloads](https://docs.cloud.google.com/app-hub/docs/modify-app-hub-resources#view).

The following are the definitions and features of properties and attributes:

  * **Properties** are immutable fields that describe the underlying infrastructure of a registered service or workload, such as the project ID, location, or type. These are discovered automatically and cannot be edited in App Hub. Key supported properties include:

    * ([Preview](https://cloud.google.com/products#product-launch-stages)) **Registration type** : for services, an output-only property that indicates if a service can be registered to one or multiple applications. The following are the possible values for this property:

      * `EXCLUSIVE`: you can only register the service to a single application.
      * `SHARED`: you can register the service to multiple applications. This value indicates that the service is a [shared service](https://docs.cloud.google.com/app-hub/docs/key-concepts#service).

To learn which services are shared or exclusive, see [the list of App Hub supported services](https://docs.cloud.google.com/app-hub/docs/supported-resources#services).

    * ([Preview](https://cloud.google.com/products#product-launch-stages)) **Functional type** : an output-only property that identifies the known function of a service or workload. For example, when an AI agent is deployed through a managed platform like [Vertex AI Agent Engine](https://docs.cloud.google.com/agent-builder/agent-engine/overview), App Hub automatically classifies the resource with the `AGENT` functional type value to indicate that the workload runs an AI agent.

    * ([Preview](https://cloud.google.com/products#product-launch-stages)) **Extended metadata** : an schema-driven property that provides rich, structured information about the service or workload. It refers to a key-value field that adds detailed, type-specific data. For example, workloads with a functional type value of `AGENT` can include `apphub.googleapis.com/AgentProperties` metadata, which contains information about an agent that is compatible with the [Agent2Agent (A2A) Agent Card](https://a2a-protocol.org/latest/specification/#5-agent-discovery-the-agent-card). For a list of supported metadata types and their schemas, see [Extended metadata schemas](https://docs.cloud.google.com/app-hub/docs/metadata-schemas). To learn how to visualize this metadata, see [View extended metadata schemas](https://docs.cloud.google.com/app-hub/docs/modify-app-hub-resources#view-schemas).

    * ([Preview](https://cloud.google.com/products#product-launch-stages)) **Identity** : an output-only property that contains the service account or managed workload identity name for a service or workload.

  * **Attributes** are mutable, user-defined metadata that you can apply to applications, services, and workloads to organize and govern them. You can add attributes to applications, services, and workloads when you [create an application and register resources to it](https://docs.cloud.google.com/app-hub/docs/register-resources). You can also [update service and workload attributes](https://docs.cloud.google.com/app-hub/docs/modify-app-hub-resources#update) and [update application attributes](https://docs.cloud.google.com/app-hub/docs/manage-applications#update). Key attributes include:

    * **Owners:** Contact information for developer, operator, and business teams. The supported owner types are:

      * `developer_owners`: Development team that owns development and coding.
      * `operator_owners`: Operator team that ensures runtime and operations integrity.
      * `business_owners`: Business team that ensures quality and user expectations are met.
    * **Criticality:** The importance of the component to your business. The supported values are:

      * `MISSION_CRITICAL`
      * `HIGH`
      * `MEDIUM`
      * `LOW`
    * **Environment:** The lifecycle stage of the component. The supported values are:

      * `PRODUCTION`
      * `STAGING`
      * `DEVELOPMENT`
      * `TEST`
**Note:** You cannot set or modify attributes for [shared services](https://docs.cloud.google.com/app-hub/docs/key-concepts#service).



## The App Hub resource model

To enable application-centric features, App Hub uses a resource model centered on the concepts of the [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project) and the [application management boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary).

  * Recommended: **Folder-level boundary** : If your components are organized within a Google Cloud folder structure, you can use a folder as your boundary. This approach aligns your application management boundary with your organization's structure by business unit, environment, or team, and automatically includes all projects within that folder.
  * ([Preview](https://cloud.google.com/products#product-launch-stages)) **Single-project boundary** : For small applications where all Google Cloud resources reside in one project, you can designate that single project as your boundary. This is the quickest way to get started with application management. You can define single-project boundaries by configuring the project as a standalone management project.
  * **(Legacy) Multiple-project boundary with a host project** : For existing users, App Hub supports a legacy model where you can designate a host project for application management by enabling the App Hub API on a Google Cloud project. Then, you manually connect other Google Cloud projects, known as service projects, to it for multi-project resource discovery.



This application management layer that App Hub introduces on top of your [resource hierarchy in Google Cloud](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) lets App Hub discover [supported resources](https://docs.cloud.google.com/app-hub/docs/supported-resources) within the boundary. You can choose a setup model for applications and set an application management boundary that best fits your resource hierarchy and governance needs.

For information about data handling in this resource organization and other application-centric features, see [Application-centric Google Cloud](https://docs.cloud.google.com/app-hub/docs/application-centric-google-cloud). For details about getting started and defining an application management boundary, see [Choose your application setup model](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub).

## What's next

  * To see which Google Cloud resources you can register in App Hub, see [Supported resources](https://docs.cloud.google.com/app-hub/docs/supported-resources).
  * To get started with defining an application management boundary, see [Choose your application setup model](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub).
  * To understand the permissions required to use App Hub, see [Roles and permissions](https://docs.cloud.google.com/app-hub/docs/roles-permissions).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
