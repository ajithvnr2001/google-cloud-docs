---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/tiered-hybrid-pattern/
title: Tiered hybrid pattern \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:44.948968+00:00
---

# Tiered hybrid pattern  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/tiered-hybrid-pattern/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Tiered hybrid pattern Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-23 UTC

The architecture components of an application can be categorized as either _frontend_ or _backend_. In some scenarios, these components can be hosted to operate from different computing environments. As part of the _tiered hybrid_ architecture pattern, the computing environments are located in an on-premises private computing environment and in Google Cloud.

Frontend application components are directly exposed to end users or devices. As a result, these applications are often performance sensitive. To develop new features and improvements, software updates can be frequent. Because frontend applications usually rely on backend applications to store and manage data—and possibly business logic and user input processing—they're often [stateless](https://docs.cloud.google.com/architecture/framework#use_a_stateless_architecture) or manage only limited volumes of data.

To be accessible and usable, you can build your frontend applications with various frameworks and technologies. Some key factors for a successful frontend application include application performance, response speed, and browser compatibility.

Backend application components usually focus on storing and managing data. In some architectures, business logic might be incorporated within the backend component. New releases of backend applications tend to be less frequent than releases for frontend applications. Backend applications have the following challenges to manage:

  * Handling a large volume of requests
  * Handling a large volume of data
  * Securing data
  * Maintaining current and updated data across all the system replicas



The [three-tier web app solution](https://console.cloud.google.com/products/solutions/details/three-tier-web-app) is one of the most popular implementations for building business web applications, like ecommerce websites containing different application components. This architecture contains the following tiers. Each tier operates independently, but they're closely linked and all function together.

  * Web frontend and presentation tier
  * Application tier
  * Data access or backend tier



Putting these layers into containers separates their technical needs, like scaling requirements, and helps to migrate them in a phased approach. Also, it lets you deploy them on platform-agnostic cloud services that can be portable across environments, use automated management, and scale with cloud managed platforms, like Cloud Run or Google Kubernetes Engine (GKE). Also, [Google Cloud-managed databases](https://cloud.google.com/products/databases) like Cloud SQL help to provide the backend as the database layer.

**Note:** The implementation of this architecture and the definition of its components can vary depending on whether you separate the tiers into individual systems and layers or combine them.

The tiered hybrid architecture pattern focuses on deploying existing frontend application components to the public cloud. In this pattern, you keep any existing backend application components in their private computing environment. Depending on the scale and the specific design of the application, you can migrate frontend application components on a case-by-case basis. For more information, see [Migrate to Google Cloud](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#the_migration_path).

If you have an existing application with backend and frontend components hosted in your on-premises environment, consider the limits of your current architecture. For example, as your application scales and the demands on its performance and reliability increase, you should start evaluating whether parts of your application should be refactored or moved to a different and more optimal architecture. The _tiered hybrid_ architecture pattern lets you shift some application workloads and components to the cloud before making a complete transition. It's also essential to consider the cost, time, and risk involved in such a migration.

The following diagram shows a typical _tiered hybrid_ architecture pattern.

![Data flow from an on-premises application frontend, to an application frontend in Google Cloud. Data then flows back to the on-premises environment.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-patterns-and-practices/tiered-hybrid.svg)

In the preceding diagram, client requests are sent to the application frontend that is hosted in Google Cloud. In turn, the application frontend sends data back to the on-premises environment where the application backend is hosted (ideally through an API gateway).

With the _tiered hybrid_ architecture pattern, you can take advantage of Google Cloud infrastructure and global services, as shown in the example architecture in the following diagram. The application frontend can be reached over Google Cloud. It can also add elasticity to the frontend by using auto-scaling to dynamically and efficiently respond to scaling demand without over provisioning infrastructure. There are different architectures that you can use to build and run scalable web apps on Google Cloud. Each architecture has advantages and disadvantages for different requirements.

For more information, watch [Three ways to run scalable web apps on Google Cloud](https://www.youtube.com/watch?v=PLu7M2rbkKA) on YouTube. To learn more about different ways to modernize your ecommerce platform on Google Cloud, see [How to build a digital commerce platform on Google Cloud](https://cloud.google.com/blog/topics/developers-practitioners/how-build-digital-commerce-platform-google-cloud).

![Data flow from users to an on-premises database server through a Cloud Load Balancing and Compute Engine.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-patterns-and-practices/multi-regional.svg)

In the preceding diagram, the application frontend is hosted on Google Cloud to provide a multi-regional and globally optimized user experience that uses global [load balancing](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer), autoscaling, and DDoS protection through [Google Cloud Armor](https://docs.cloud.google.com/armor).

Over time, the number of applications that you deploy to the public cloud might increase to the point where you might consider moving backend application components to the public cloud. If you expect to serve heavy traffic, opting for cloud-managed services might help you save engineering effort when managing your own infrastructure. Consider this option unless constraints or requirements mandate hosting backend application components on-premises. For example, if your backend data is subject to regulatory restrictions, you probably need to keep that data on-premises. Where applicable and compliant, however, using [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection) capabilities like [de-identification techniques](https://docs.cloud.google.com/sensitive-data-protection/docs/deidentify-sensitive-data), can help you move that data when necessary.

In the tiered hybrid architecture pattern, you also can use Google Distributed Cloud in some scenarios. Distributed Cloud lets you run GKE clusters on dedicated hardware that's provided and maintained by Google and is separate from Google Cloud data center. To ensure that Distributed Cloud meets your current and future requirements, know the limitations of Distributed Cloud when compared to a conventional cloud-based GKE zone.

## Advantages

Focusing on frontend applications first has several advantages including the following:

  * Frontend components depend on backend resources and occasionally on other frontend components.
  * Backend components don't depend on frontend components. Therefore, isolating and migrating frontend applications tends to be less complex than migrating backend applications.
  * Because frontend applications often are stateless or don't manage data by themselves, they tend to be less challenging to migrate than backends. 
    * Frontend components can be optimized as part of the migration to use [stateless architecture](https://docs.cloud.google.com/architecture/framework#use_a_stateless_architecture). For more information, watch [How to port stateful web apps to Cloud Run](https://www.youtube.com/watch?v=mgTI-paDNQ4) on YouTube.



Deploying existing or newly developed frontend applications to the public cloud offers several advantages:

  * Many frontend applications are subject to frequent changes. Running these applications in the public cloud simplifies the setup of a continuous integration/continuous deployment (CI/CD) process. You can use CI/CD to send updates in an efficient and automated manner. For more information, see [CI/CD on Google Cloud](https://docs.cloud.google.com/docs/ci-cd).
  * Performance-sensitive frontends with varying traffic load can benefit substantially from the load balancing, multi-regional deployments, [Cloud CDN](https://docs.cloud.google.com/cdn/docs/overview) caching, serverless, and autoscaling capabilities that a cloud-based deployment enables (ideally with [stateless architecture](https://docs.cloud.google.com/architecture/framework#use_a_stateless_architecture)).
  * Adopting microservices with containers using a cloud-managed platform, like GKE, lets you use modern architectures like [microfrontend](https://en.wikipedia.org/wiki/Microfrontend), which extend microservices to the frontend components.

Extending microservices is commonly used with frontends that involve multiple teams collaborating on the same application. That kind of team structure requires an iterative approach and continuous maintenance. Some of the advantages of using microfrontend are as follows:

    * It can be made into independent microservices modules for development, testing, and deployment.
    * It provides separation where individual development teams can select their preferred technologies and code.
    * It can foster rapid cycles of development and deployment without affecting the rest of the frontend components that might be managed by other teams.
  * Whether they're implementing user interfaces or APIs, or handling Internet of Things (IoT) data ingestion, frontend applications can benefit from the capabilities of cloud services like [Firebase](https://firebase.google.com/), [Pub/Sub](https://docs.cloud.google.com/pubsub), [Apigee](https://docs.cloud.google.com/apigee), [Cloud CDN](https://docs.cloud.google.com/cdn/docs), [App Engine](https://docs.cloud.google.com/appengine), or [Cloud Run](https://docs.cloud.google.com/run).

  * [Cloud-managed API proxies](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/understanding-apis-and-api-proxies#whatisanapiproxy) help to:

    * Decouple the app-facing API from your backend services, like microservices.
    * Shield apps from backend code changes.
    * Support your existing API-driven frontend architectures, like backend for frontend (BFF), microfrontend, and others.
    * Expose your APIs on Google Cloud or other environments by implementing API proxies on Apigee.



You can also apply the _tiered hybrid_ pattern in reverse, by deploying backends in the cloud while keeping frontends in private computing environments. Although it's less common, this approach is best applied when you're dealing with a heavyweight and monolithic frontend. In such cases, it might be easier to extract backend functionality iteratively, and to deploy these new backends in the cloud.

The third part of this series discusses possible networking patterns to enable such an architecture. [Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/what-is-hybrid) helps as a platform for building and managing API proxies in a hybrid deployment model. For more information, see [Loosely coupled architecture](https://dora.dev/devops-capabilities/technical/loosely-coupled-architecture/), including tiered monolithic and microservices architectures.

## Best practices

Use the information in this section as you plan for your tiered hybrid architecture.

## Best practices to reduce complexity

When you're applying the _tiered hybrid_ architecture pattern, consider the following best practices that can help to reduce its overall deployment and operational complexity:

  * Based on the assessment of the communication models of the identified applications, select the most efficient and effective communication solution for those applications.



Because most user interaction involves systems that connect across multiple computing environments, fast and low-latency connectivity between those systems is important. To meet availability and performance expectations, you should design for high availability, low latency, and appropriate throughput levels. From a security point of view, communication needs to be fine-grained and controlled. Ideally, you should expose application components using secure APIs. For more information, see [Gated egress](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/gated-egress).

  * To minimize communication latency between environments, select a [Google Cloud region](https://cloud.google.com/about/locations) that is geographically close to the private computing environment where your application backend components are hosted. For more information, see [Best practices for Compute Engine regions selection](https://docs.cloud.google.com/solutions/best-practices-compute-engine-region-selection).
  * Minimize high dependencies between systems that are running in different environments, particularly when communication is handled synchronously. These dependencies can slow performance, decrease overall availability, and potentially incur additional outbound data transfer charges.
  * With the _tiered hybrid_ architecture pattern, you might have larger volumes of inbound traffic from on-premises environments coming into Google Cloud compared to outbound traffic leaving Google Cloud. Nevertheless, you should know the anticipated [outbound data transfer](https://cloud.google.com/vpc/network-pricing#internet_egress) volume leaving Google Cloud. If you plan to use this architecture long term with high outbound data transfer volumes, consider using Cloud Interconnect. Cloud Interconnect can help to optimize connectivity performance and might reduce outbound data transfer charges for traffic that meets certain conditions. For more information, see [Cloud Interconnect pricing](https://cloud.google.com/network-connectivity/docs/interconnect/pricing).
  * To protect sensitive information, we recommend encrypting all communications [in transit](https://docs.cloud.google.com/architecture/landing-zones/decide-security#encrypt-transit). If encryption is required at the connectivity layer, you can use VPN tunnels, [HA VPN over Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/ha-vpn-interconnect), and [MACsec for Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/macsec-overview).
  * To overcome inconsistencies in protocols, APIs, and authentication mechanisms across diverse backends, we recommend, where applicable, to deploy an API gateway or proxy as a unifying [facade](https://cloud.google.com/apigee/resources/ebook/api-facade-pattern-register). This gateway or proxy acts as a centralized control point and performs the following measures:

    * Implements additional security measures.
    * Shields client apps and other services from backend code changes.
    * Facilitates audit trails for communication between all cross-environment applications and its decoupled components.
    * Acts as an [intermediate communication layer](https://docs.cloud.google.com/solutions/unlocking-legacy-applications#section-3) between legacy and modernized services. 
      * Apigee and [Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/what-is-hybrid) lets you host and manage enterprise-grade and hybrid gateways across on-premises environments, edge, other clouds, and Google Cloud environments.
  * To facilitate the establishment of hybrid setups, use Cloud Load Balancing with [hybrid connectivity](https://docs.cloud.google.com/load-balancing/docs/l7-internal#load_balancing_with_hybrid_connectivity). That means you can extend the benefits of cloud load balancing to services hosted on your on-premises compute environment. This approach enables phased workload migrations to Google Cloud with minimal or no service disruption, ensuring a smooth transition for the distributed services. For more information, see [Hybrid connectivity network endpoint groups overview](https://docs.cloud.google.com/load-balancing/docs/negs/hybrid-neg-concepts#hybrid_architecture).

  * Sometimes, using an API gateway, or a proxy and an [Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer) together, can provide a more robust solution for managing, securing, and distributing API traffic at scale. [Using Cloud Load Balancing with API gateways](https://docs.cloud.google.com/api-gateway/docs/gateway-serverless-neg) lets you accomplish the following:

    * Provide high-performing APIs with Apigee and Cloud CDN, to reduce latency, host APIs globally, and increase availability for peak traffic seasons. For more information, watch [Delivering high-performing APIs with Apigee and Cloud CDN](https://www.youtube.com/watch?v=lwiJUaGPCK4) on YouTube.
    * Implement advanced traffic management.
    * Use Cloud Armor as a DDoS protection and network security service to protect your APIs.
    * Manage efficient load balancing across gateways in multiple regions. For more information, watch [Securing APIs and Implementing multi-region failover with Private Service Connect and Apigee](https://www.youtube.com/watch?v=AatzC4ct7co) on YouTube.
  * Use [API management and service mesh](https://cloud.google.com/resources/api-management-and-service-mesh-report) to secure and control service communication and exposure with microservices architecture.

    * Use [Cloud Service Mesh](https://cloud.google.com/products/service-mesh) to allow for service-to-service communication that maintains the quality of service in a system composed of distributed services where you can manage authentication, authorization, and encryption between services.
    * Use an API management platform like Apigee that lets your organization and external entities consume those services by exposing them as APIs.
  * [Establish common identity](https://docs.cloud.google.com/architecture/authenticating-corporate-users-in-a-hybrid-environment) between environments so that systems can authenticate securely across environment boundaries.

  * Deploy CI/CD and configuration management systems in the public cloud. For more information, see [Mirrored networking architecture pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/mirrored-pattern).

  * To help increase operational efficiency, use consistent tooling and CI/CD pipelines across environments.




## Best practices for individual workload and application architectures

  * Although the focus lies on frontend applications in this pattern, stay aware of the need to modernize your backend applications. If the development pace of backend applications is substantially slower than for frontend applications, the difference can cause extra complexity.
  * Treating APIs as backend interfaces streamlines integrations, frontend development, service interactions, and hides backend system complexities. To address these challenges, [Apigee](https://docs.cloud.google.com/apigee) facilitates API gateway/proxy development and management for hybrid and multicloud deployments.
  * Choose the [rendering approach](https://developers.google.com/solutions/content-driven/hosting/rendering) for your frontend web application based on the content (static versus dynamic), the search engine optimization performance, and the expectations about page loading speeds.
  * When selecting an architecture for content-driven web applications, various options are available, including monolithic, serverless, event-based, and microservice architectures. To select the most suitable architecture, thoroughly assess these options against your current and future application requirements. To help you make an architectural decision that's aligned with your business and technical objectives, see [Comparison of different architectures for content-driven web application backends](https://developers.google.com/solutions/content-driven/backend/architecture#comparison_of_different_architectures_for_content-driven_web_application_backends), and [Key Considerations for web backends](https://developers.google.com/solutions/content-driven/backend#key_considerations_for_web_backends).
  * With a microservices architecture, you can use containerized applications with Kubernetes as the common runtime layer. With the tiered hybrid architecture pattern, you can run it in either of the following scenarios:

    * Across both environments (Google Cloud and your on-premises environments).

      * When using containers and Kubernetes across environments, you have the flexibility to modernize workloads and then migrate to Google Cloud at different times. That helps when a workload depends heavily on another and can't be migrated individually, or to use hybrid workload portability to use the best resources available in each environment. In all cases, GKE can be a key enabling technology. For more information, see [GKE hybrid environment](https://docs.cloud.google.com/anthos/docs/architecture/anthos-hybrid-environment).
    * In a Google Cloud environment for the migrated and modernized application components.

      * Use this approach when you have legacy backends on-premises that lack containerization support or require significant time and resources to modernize in the short-term.

For more information about designing and refactoring a monolithic app to a microservice architecture to modernize your web application architecture, see [Introduction to microservices](https://docs.cloud.google.com/architecture/microservices-architecture-introduction).

  * You can combine data storage technologies depending on the needs of your web applications. Using Cloud SQL for structured data and Cloud Storage for media files is a common approach to meet diverse data storage needs. That said, the choice depends heavily on your use case. For more information about data storage options for content-driven application backends and effective modalities, see [Data Storage Options for Content-Driven Web Apps](https://developers.google.com/solutions/content-driven/data-storage/options). Also, see [Your Google Cloud database options, explained](https://cloud.google.com/blog/topics/developers-practitioners/your-google-cloud-database-options-explained).




[ Previous arrow_back  Distributed architecture patterns  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/distributed-patterns)

[ Next Partitioned multicloud pattern  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/partitioned-multicloud-pattern)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-23 UTC."],[],[]] 
