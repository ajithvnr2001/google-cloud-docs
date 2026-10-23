---
url: https://docs.cloud.google.com/app-hub/docs/best-practices/
title: Best practices for application management \u00a0|\u00a0 App Hub \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:15:08.897533+00:00
---

# Best practices for application management  |  App Hub  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-hub/docs/best-practices/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ App Hub ](https://docs.cloud.google.com/app-hub/docs)
  * [ Guides ](https://docs.cloud.google.com/app-hub/docs/overview)



Send feedback 

#  Best practices for application management Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides best practices for designing, defining, and managing your App Hub applications in [Application-centric Google Cloud](https://docs.cloud.google.com/app-hub/docs/application-centric-google-cloud), using [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) and [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview). Following these practices is key to creating operable, governable, and efficient applications that align with your business objectives.

## Core principles of application management

Adhering to the following core principles helps you maximize the value you get from managing your Google Cloud infrastructure in an application-centric way:

  * **Define clear boundaries:** Set the [application management boundary](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary) in a way that is logical for your operations, monitoring, governance, and troubleshooting. Additionally, resources within this boundary that you use as [application components](https://docs.cloud.google.com/app-hub/docs/key-concepts#component) should ideally share a joint operational lifecycle or business value to simplify management and reduce risk.

For operational purposes, it's important to understand the difference between an _application management boundary_ and _observability scopes_.

    * The application management boundary defines the collection of projects that contain the Google Cloud resources you can use to design, create, and manage applications, as described in [Key concepts](https://docs.cloud.google.com/app-hub/docs/key-concepts).
    * Observability scopes in Google Cloud Observability let you view telemetry from multiple projects together.

Your log, metrics, and trace scopes should include data from the same projects that are included in your application management boundary. For more information about observability scopes, see [Configure observability scopes](https://docs.cloud.google.com/stackdriver/docs/observability/scopes).

  * **Reflect business capabilities:** Define your applications around business functions or end-to-end workflows, not just technical layers. An application should represent a distinct value stream for your business.

  * **Establish clear ownership and metadata:** Assign clear [attributes](https://docs.cloud.google.com/app-hub/docs/overview#properties-and-attributes) to each application to let teams effectively find, understand, and manage them in App Hub. These attributes support discoverability and governance. Discoverability means that relevant teams, such as developers and operators, can find applications. Governance clearly defines who owns and is accountable for each application.

In App Hub, you can define key attributes such as the following:

    * **Environment:** The stage in the application's lifecycle, such as Production, Staging, Test, or Development. This attribute helps teams filter and manage components based on their deployment stage.
    * **Criticality:** The business importance of the application and its components, such as whether they are mission critical. This attribute can inform monitoring and incident response priorities.
    * **Owners:** Contact information for the different teams responsible for the application, which fosters accountability, streamlines communication, and clarifies responsibilities.

Application Design Center supports these attributes and also includes location and configuration details for application components. Consistently applying those attributes and details is crucial for discovery, governance, and reporting.

  * **Design for evolution:** Application Design Center helps you design for evolution by letting you create reusable [templates](https://docs.cloud.google.com/app-hub/docs/key-concepts#template) for your applications. If you update the underlying template, you can then apply those changes by redeploying applications, which helps you meet demand, introduce new features, or make architectural changes, accommodating future growth and evolving infrastructure needs.

  * **Iterate and refine application models:** Regularly review and adjust your application definitions to reflect changes in your organization's structure, business priorities, and technical architecture. Cloud Hub provides centralized views of available updates for applications deployed from Application Design Center templates, helping you review and adjust your application definitions to reflect these evolving needs.




## Data model recommendations

By understanding how to model your real-world systems as applications, services, and workloads within [App Hub's framework](https://docs.cloud.google.com/app-hub/docs/overview), you can effectively use application management capabilities in your Google Cloud environment.

As you define your applications, it's important to apply the core principles of application management, such as using attributes to establish clear ownership and metadata.

To model your application components with this framework in mind, consider the following examples of recommended use cases.

### Example: Microservices-based application

An ecommerce system, such as the one described in the [OpenTelemetry demo](https://opentelemetry.io/docs/demo/architecture/) for an online store, is an example of a microservices-based application. We recommend modeling this kind of system as a single application. This approach provides a unified view of the entire business function, from product discovery to checkout. For example, consider the following model for existing resources running in Google Cloud:

  * **Application:** Create or define a single application in App Hub named, for example, `my-ecommerce-site`. This application represents the entire online store as a single, manageable unit. Register the following resources to the application to create a logical grouping of components that jointly delivers the business function of your online store:

    * **Microservices as workloads:** Register the individual microservices that make up the ecommerce system, such as **Ad** , **Cart** , and **Checkout** , as _workloads_ within the application. These are the compute resources with the binary code that perform a discrete part of the business logic, running as Google Kubernetes Engine (GKE) deployments.
    * **Network endpoints as services:** Register the network endpoints for these microservices, such as their load balancers, as _services_ of the application. These expose the online store functionality to clients.



Avoid registering each microservice as its own application. That approach fragments the business context and makes it difficult to get a comprehensive view of the health and performance of your online store.

By grouping all the microservices into a single application, you gain the following benefits:

  * **Comprehensive visibility:** You can monitor the health and performance of the entire ecommerce user journey, from the ad functionality to the checkout functionality, in a single, unified view.
  * **Clear business context:** The application aligns the infrastructure with the business function it serves, which is the online store. This approach makes it easier to understand the health and cost of the application.
  * **Simplified troubleshooting:** When an issue arises, you can see the dependencies between the different microservices within the application, accelerating root cause analysis.



### Example: Three-tier web application

A three-tier web application is an architectural pattern that separates an application into a frontend tier, a backend tier, and a database tier. This use case demonstrates how to model a complete business function as a single application, rather than treating each tier as an isolated component.

The following model maps technical layers into a three-tier web application:

  * **Application:** Create a single application, for example, `my-web-app`, to serve as the logical container for all the components that make up your web application.

  * **Services:** Register the network interfaces that expose functionality to other tiers or to users as services, for example:

    * The frontend load balancer that receives user traffic.
    * The internal load balancer that manages traffic between the frontend and backend.
    * The Cloud SQL or Spanner database instance, which exposes a data service to the backend logic tier.
  * **Workloads:** Register the compute resources that run your application's code as workloads, for example:

    * The Managed Instance Groups (MIGs) or Google Kubernetes Engine deployments that serve the frontend user interface.
    * The MIGs or Google Kubernetes Engine deployments that run the backend business logic.



By grouping all three tiers into a single application, you gain the following benefits:

  * **Unified observability:** You can monitor the health and performance of the entire application from a single dashboard in [Application Monitoring](https://docs.cloud.google.com/stackdriver/docs/observability/about-application-monitoring), rather than having to piece together data from three separate applications.
  * **Clear ownership:** You can assign business, developer, and operator owners to the `my-web-app` application, clarifying accountability for the entire business function.
  * **Simplified governance:** You can apply policies and access controls at the `my-web-app` level, supporting consistent governance across all tiers.



## Application design and governance strategies

Adopt the following strategies to make sure your App Hub and Application Design Center setup is scalable, governable, and aligned with your operational practices.

### Choose between global and regional applications

The location you choose for an application, either global or regional, is a fundamental decision that impacts data handling, latency, and compliance:

  * **Prioritize regional applications:** Whenever possible, define your applications as regional. This practice provides benefits like reduced latency, potential cost savings, and alignment with data residency requirements. Regional applications are recommended when all application components reside within a single Google Cloud region, providing an inherent compatibility with region-specific Google Cloud features and failure domains. For guidance on building highly available systems, see [Build highly available systems through resource redundancy](https://docs.cloud.google.com/architecture/framework/reliability/build-highly-available-systems).
  * **Use global applications strategically:** Opt for a global application only when your system's components are necessarily spread across multiple regions or involve global Google Cloud resources, like a global external Application Load Balancer.
  * **Decompose multi-region systems:** If you have resources in multiple regions that don't form a single cohesive global function, consider defining separate regional applications for components within each respective region. This practice maximizes the benefits of regionalization for each deployment.



For a detailed comparison between the different deployment geographies in App Hub, see [Global and regional applications](https://docs.cloud.google.com/app-hub/docs/global-regional-applications).

### Separate environments into distinct applications

To support isolation for security, permissions, and operational risk, represent different deployment environments, such as development, staging, and production, as distinct applications. For example, you could structure your applications as `my-app-dev`, `my-app-staging`, and `my-app-prod`.

Separating environments into distinct applications offers precise limits for access control, policy enforcement, and monitoring. Additionally, consistently using attributes, configuration details, and location on your application components enhances discoverability and enforces governance. These attributes provide rich metadata for filtering, reporting, and policy application. For example, the `Environment` attribute provides granular detail and resource-specific control for distinct deployment environment policies. For more information on this and other attributes, see [Properties and attributes](https://docs.cloud.google.com/app-hub/docs/overview#properties-and-attributes).

### Align application management boundaries with team structures

Represent your organizational structure, specifically the teams responsible for application development and operation, within your [application management boundaries](https://docs.cloud.google.com/app-hub/docs/key-concepts#app-mgmt-boundary).

This practice simplifies ownership and communication because the application model mirrors the framework that your business uses to define how tasks are divided, grouped, and coordinated to achieve its functions.

### Follow the application lifecycle

Integrate App Hub with Application Design Center for a seamless application lifecycle experience:

  * **You have pre-existing resources to register in an application:** Use App Hub to register your existing Google Cloud resources as services or workloads in applications. This practice provides unified visibility and operational control over your current infrastructure quickly. Optionally, you can later create a template in Application Design Center from a running application to standardize the architecture for future deployments.
  * **You don't have pre-existing resources to register in an application:** Use Application Design Center to design and deploy new applications from governed, reusable templates. When you deploy an application from an Application Design Center template, the components are automatically registered in App Hub so your application model accurately reflects the intended design. Application Design Center also helps you manage consistent application updates based on template revisions. If you update the template, you can redeploy the application to propagate the changes, supporting consistency and governance.



## Resource hierarchy considerations

Your [resource hierarchy in Google Cloud](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) is the foundation for practical application management. You introduce an application management layer on top of that hierarchy through the configuration of a [management project](https://docs.cloud.google.com/app-hub/docs/key-concepts#mgmt-project) to define your application management boundary. For an overview of how different products work together as part of Application-centric Google Cloud solutions, see [Application-centric Google Cloud](https://docs.cloud.google.com/app-hub/docs/application-centric-google-cloud).

Thoughtful planning of your Google Cloud resource hierarchy for application management is essential to establishing logical groupings. Your choice of a single project, a folder, or a set of projects to define your application management boundary fundamentally shapes governance, policy enforcement, and resource discovery. Moreover, Application-centric Google Cloud product support varies according to how you define this application management boundary.

To define the best application management boundary for your resource hierarchy and business needs and learn about product support for different resource structure patterns, see [Choose your application setup model](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub).

## Continuous refinement

Application designs are not static; they typically evolve with time. Regularly review and refine your applications to make sure they continue to align with your business functions, team structures, and changing architectures.

We recommend using insights from [Cloud Hub](https://docs.cloud.google.com/hub/docs/overview) and [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview) to identify optimization opportunities and adapt your applications accordingly. Use Application Design Center to model and deploy architectural changes and manage the lifecycle of your applications through templates.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
