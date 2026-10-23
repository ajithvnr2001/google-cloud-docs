---
url: https://docs.cloud.google.com/migrate/containers/docs/anthos-migrate-benefits/
title: Benefits of migrating to containers \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:39.975373+00:00
---

# Benefits of migrating to containers  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/anthos-migrate-benefits/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Benefits of migrating to containers 

Migrate to Containers is a tool to containerize existing VM-based applications to run on [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine), [GKE Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview), [GKE Enterprise](https://docs.cloud.google.com/anthos), or [Cloud Run](https://docs.cloud.google.com/run/docs). By taking advantage of the GKE and GKE Enterprise ecosystems, Migrate to Containers provides a fast and simple way to move to modernized orchestration and application management. Modernization and management can be done without requiring access to source code, rewriting, or rearchitecting applications.

## Migrate to containers versus lift-and-shift to Compute Engine

Today, you can migrate VM workloads into VM instances in Compute Engine using [Migrate to VMs](https://docs.cloud.google.com/migrate/virtual-machines). This "lift and shift" method offers the simplest steps for cloud migration. This method consistently preserves the same operational model used for running and managing applications on-premises, modernizing only the underlying infrastructure.

While "lift and shift" is a viable option for certain workloads, many customers that are moving to the cloud want to take a step further. They are taking advantage of cloud-specific tools, methods, and managed services. In particular, they want to shift from VMs to containers, and manage their workloads on GKE or GKE Enterprise.

## Benefits of containers

Migrate to Containers lets you modernize application workloads by converting them to containers. There are several key benefits to containerizing workloads:

  * **Density.** Containers are much lighter than VMs since they don't contain the operating system, and therefore require considerably fewer compute and memory resources. Containers provide greater density of workloads across your clusters, fine-grained resource allocations, and overall **lower infrastructure costs.**
  * **Security optimized node kernel.** GKE and GKE Enterprise offer automatic operating system upgrades, freeing you from the burden of maintaining their operating system.
  * **Augment legacy apps with modern services.** GKE and GKE Enterprise let you use platform add-on services to seamlessly integrate up-to-date functionality with existing apps. For instance, you can take advantage of [Istio on GKE](https://docs.cloud.google.com/istio/docs/istio-on-gke/overview) or [Cloud Service Mesh](https://docs.cloud.google.com/anthos/service-mesh) to automate network and security policies without changing your application code. Also, you can use monitoring and logging with Cloud Logging and Cloud Monitoring by changing configurations and not changing your applications.
  * **Unified policy and integrated resource management.** GKE and GKE Enterprise let you focus on managing applications, not infrastructure. They offer the power of declarative desired-state management with powerful tagging strategies and selector policies.
  * **Modern image-based management and orchestration.** Migrate to Containers offers a unique capability to extract an image from the VM workload and construct a Docker image and related artifacts. This extraction in turn lets you modernize your application lifecycle and operations management, including integrating with a CI/CD pipeline. Integration with a CI/CD pipeline uses tools like Cloud Build to implement day-2 maintenance procedures. Furthermore, image-based management enables customers to perform rolling updates, dynamic scaling, self-healing, and more.



## What's next

  * Learn about [migration journey phases](https://docs.cloud.google.com/migrate/containers/docs/migration-journey).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
