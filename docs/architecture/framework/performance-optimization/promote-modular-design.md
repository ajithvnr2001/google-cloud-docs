---
url: https://docs.cloud.google.com/architecture/framework/performance-optimization/promote-modular-design/
title: Promote modular design \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:21.696656+00:00
---

# Promote modular design  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/framework/performance-optimization/promote-modular-design/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Promote modular design Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-06 UTC

This principle in the performance optimization pillar of the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) provides recommendations to help you promote a modular design. Modular components and clear interfaces can enable flexible scaling, independent updates, and future component separation.

## Principle overview

Understand the dependencies between the application components and the system components to design a scalable system.

Modular design enables flexibility and resilience, regardless of whether a monolithic or microservices architecture was initially deployed. By decomposing the system into well-defined, independent modules with clear interfaces, you can scale individual components to meet specific demands.

Targeted scaling can help optimize resource utilization and reduce costs in the following ways:

  * Provisions only the necessary resources to each component, and allocates fewer resources to less-demanding components.
  * Adds more resources during high-traffic periods to maintain the user experience.
  * Removes under-utilized resources without compromising performance.



Modularity also enhances maintainability. Smaller, self-contained units are easier to understand, debug, and update, which can lead to faster development cycles and reduced risk.

While modularity offers significant advantages, you must evaluate the potential performance trade-offs. The increased communication between modules can introduce latency and overhead. Strive for a balance between modularity and performance. A highly modular design might not be universally suitable. When performance is critical, a more tightly coupled approach might be appropriate. System design is an [iterative process](https://docs.cloud.google.com/architecture/framework/performance-optimization), in which you continuously review and refine your modular design.

## Recommendations

To promote modular designs, consider the recommendations in the following sections.

### Design for loose coupling

Design a [loosely coupled architecture](https://docs.cloud.google.com/architecture/microservices-architecture-refactoring-monoliths). Independent components with minimal dependencies can help you build [scalable and resilient applications](https://docs.cloud.google.com/architecture/scalable-and-resilient-apps). As you plan the boundaries for your services, you must consider the availability and scalability requirements. For example, if one component has requirements that are different from your other components, you can design the component as a standalone service. Implement a plan for graceful failures for less-important subprocesses or services that don't impact the response time of the primary services.

### Design for concurrency and parallelism

Design your application to support multiple tasks concurrently, like processing multiple user requests or running background jobs while users interact with your system. Break large tasks into smaller chunks that can be processed at the same time by multiple service instances. Task concurrency lets you use features like autoscaling to increase the resource allocation in products like the following:

  * [Compute Engine](https://docs.cloud.google.com/compute/docs/autoscaler)
  * [GKE](https://docs.cloud.google.com/spanner/docs/autoscaling-overview)
  * [BigQuery](https://docs.cloud.google.com/bigquery/docs/slots-autoscaling-intro)
  * [Spanner](https://docs.cloud.google.com/spanner/docs/autoscaling-overview)



### Balance modularity for flexible resource allocation

Where possible, ensure that each component uses only the necessary resources (like memory, storage, and processing power) for specific operations. Resource over-allocation can result in unnecessary costs, while resource under-allocation can compromise performance.

### Use well-defined interfaces

Ensure modular components communicate effectively through clear, standardized interfaces (like APIs and message queues) to reduce overhead from translation layers or from extraneous traffic.

### Use stateless models

A stateless model can help ensure that you can handle each request or interaction with the service independently from previous requests. This model facilitates scalability and recoverability, because you can grow, shrink, or restart the service without losing the data necessary for in-progress requests or processes.

### Choose complementary technologies

Choose technologies that complement the modular design. Evaluate programming languages, frameworks, and databases for their modularity support.

For more information, see the following resources:

  * [Re-architecting to cloud native](https://cloud.google.com/resources/rearchitecting-to-cloud-native)
  * [Introduction to microservices](https://docs.cloud.google.com/architecture/microservices-architecture-introduction)



[ Previous arrow_back  Take advantage of elasticity  ](https://docs.cloud.google.com/architecture/framework/performance-optimization/elasticity)

[ Next Continuously monitor and improve performance  arrow_forward  ](https://docs.cloud.google.com/architecture/framework/performance-optimization/continuously-monitor-and-improve-performance)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-06 UTC."],[],[]] 
