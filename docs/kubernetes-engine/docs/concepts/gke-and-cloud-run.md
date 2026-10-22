---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-and-cloud-run/
title: GKE and Cloud Run \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:01:05.141756+00:00
---

# GKE and Cloud Run  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-and-cloud-run/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  GKE and Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Google Cloud offers two major platforms for running containerized applications: GKE for running containers on Kubernetes clusters, and [Cloud Run](https://docs.cloud.google.com/run/docs) for running containers directly on Google Cloud infrastructure. But when should you use one or the other? And can you use both? This page provides a comparison of the two platforms and their advantages, and helps you find out if a single-platform or hybrid strategy will work for you.

This page is designed for infrastructure administrators and application operators who run a diverse set of containerized workloads, and want to leverage the strengths of both Google Kubernetes Engine (GKE) and Cloud Run to deploy applications to the Google Cloud Platform.

Before reading this page, ensure that you're familiar with:

  * [Basic Kubernetes concepts](https://docs.cloud.google.com/kubernetes-engine/docs/learn/get-started-with-kubernetes)

  * Stateless and stateful workloads




## Why use GKE and Cloud Run together?

GKE and Cloud Run offer different advantages for running containerized applications, and cater to different levels of workload complexity. However, you don't need to choose between the two platforms. You can simultaneously leverage the strengths of both GKE and Cloud Run by migrating your workloads between the two platforms as the need arises. A hybrid strategy like this can empower you to optimize costs, performance, and management overhead.

The following are some benefits of using both runtimes to deploy your workloads:

  * GKE and Cloud Run offer a relatively high level of portability:

    * Both platforms use standard container images as deployment artifacts. You can use the same image for your application in either platform without any modifications, thus enabling seamless migration of workloads between GKE and Cloud Run. You don't need to update your [continuous integration setup](https://docs.cloud.google.com/build/docs/overview) to migrate between GKE and Cloud Run as long as container images are stored in [Artifact Registry](https://docs.cloud.google.com/artifact-registry).

    * GKE and Cloud Run both use a declarative API model. The [Cloud Run Admin API v1](https://docs.cloud.google.com/run/docs/reference/rest/v1/namespaces.services) is designed to be compatible with the Kubernetes API. This means you can use familiar Kubernetes concepts like Deployments, Services, and horizontal Pod autoscalers to manage your Cloud Run service. This similarity makes it easier to translate configurations between the two platforms.

    * Resources are represented in YAML files with the same declarative and standard structure, and can therefore easily be migrated between runtimes. Here's an [example](https://docs.cloud.google.com/run/docs/migrate/from-kubernetes#side-by-side) comparing the YAML files of a Kubernetes deployment and a Cloud Run service.

  * Both GKE and Cloud Run integrate seamlessly with [Cloud Logging](https://docs.cloud.google.com/logging) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring), providing you with a centralized view on the Google Cloud console to observe application metrics regardless of their platform. You can also use [service-level objectives (SLO) monitoring](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring) on both platforms, and view a unified display of the SLOs on the Cloud Monitoring dashboard.

  * You can implement continuous delivery to either GKE resources or Cloud Run services by using [Cloud Deploy](https://docs.cloud.google.com/deploy). Or, if you prefer, simultaneously deploy your application to both GKE and Cloud Run using [parallel deployment](https://docs.cloud.google.com/deploy/docs/parallel).

  * You can facilitate [advanced traffic management](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global) by using external and internal load balancers for services on GKE and Cloud Run. This includes the ability to expose external endpoints so that you can deploy and run different URLs for the same application across both platforms. You can also split traffic to the same service across GKE and Cloud Run, enabling a seamless migration from one platform to another.

  * Google Cloud provides security tools to improve your security posture when using both runtimes. [OS scanning](https://docs.cloud.google.com/artifact-analysis/docs/scan-os-automatically) lets you scan containers for vulnerabilities before deploying to either platform. A central [Binary Authorization](https://docs.cloud.google.com/binary-authorization) policy can enforce integration with the GKE and Cloud Run control plane to allow or block image deployment based on the policies that you define. With [VPC Service Controls](https://docs.cloud.google.com/security/vpc-service-controls), security teams can define fine-grained perimeter controls across your GKE and Cloud Run resources.




## Compare GKE and Cloud Run

To take advantage of the best features of GKE and Cloud Run, and know when to move workloads between them, it's important to understand how the two services differ from one another.

Feature | GKE | Cloud Run  
---|---|---  
Deployment and management | Manage the Kubernetes clusters, including node configuration, networking, scaling, and upgrades. Google Cloud manages the underlying infrastructure and provides tools for simplifying cluster operations, but you're still responsible for the core Kubernetes aspects. | Run containers directly on top of Google Cloud's scalable infrastructure. All you have to do is provide source code or a container image, and Cloud Run can build the container for you. You don't have to create a cluster, or provision and manage infrastructure.  
Control and flexibility | Full control over the Kubernetes cluster. You can create advanced customizations of node configurations, network policies, security settings, and add-ons. | Limited control over the underlying infrastructure. You can configure things like environment variables, concurrency and network connections, but you can't customize the underlying infrastructure or environment. Ideal for simplicity and speed.  
Application types |  Supports both stateless and stateful applications, and is ideal for complex applications with specific resource needs. | Best suited for stateless, request or event-driven services, web services, and functions.  
Pricing model | Pay-per-cluster per hour, irrespective of the mode of operation (Standard or Autopilot), cluster size or topology. | Pay-per-use, rounded up to the nearest 100 millisecond.  
  
## Use case

Consider that you are a platform administrator of a retail company building a large ecommerce platform. You have the following containerized workloads to deploy:

  * **Frontend website and mobile app** : A stateless web application handling product browsing, search, and checkout.

  * **Product inventory management** : A stateful service managing product availability and updates.

  * **Recommendation engine** : A complex microservice generating personalized product recommendations for each user.

  * **Batch processing jobs** : Includes periodic tasks like updating product catalogs and analyzing user behavior.




These workloads represent a mix of stateless and stateful services, so you decide to take advantage of both GKE and Cloud Run for optimal performance. Here's one way you can implement a hybrid approach for your workloads.

  1. After reading the [criteria](https://docs.cloud.google.com/run/docs/fit-for-run) for suitability of Cloud Run workloads, you decide to use **Cloud Run** for the website and mobile app, and the batch processing jobs. Deploying these services on Cloud Run has the following benefits:

     * Automatic scaling as traffic spikes and large batch jobs are handled without manual intervention.

     * Cost efficiency with a pay-per-use model. You only pay when users are browsing or checking out, and when resources are used during batch job execution.

     * Faster deployments as updates are available instantly, improving user experience.

     * Easy integration with other Google Cloud services. For example, for event-driven processing, you can use [Cloud Run functions](https://docs.cloud.google.com/functions/docs/concepts/overview) to initiate batch processing jobs on Cloud Run, and enable seamless workflows.

  2. Product inventory management is a stateful service that requires fine-grained control and potentially custom storage solutions. You decide to use **GKE** to deploy this service as it offers persistent storage and lets you attach volumes for product data persistence and reliability.

  3. The recommendation engine is a complex microservice that benefits from **GKE**. With GKE, you can manage complex dependencies, and exercise fine-grained control over resource allocation and scaling.




GKE is best suited for complex microservices architectures, stateful applications, workloads requiring custom infrastructure or network configurations, and scenarios where deep control over Kubernetes is essential. Cloud Run is best suited for event-driven apps. It's ideal for stateless web services, APIs, batch jobs, and other workloads that benefit from pay-per-use pricing.

The preceding example demonstrates how combining GKE and Cloud Run can provide a powerful and flexible solution for your ecommerce platform. You gain the benefits of both platforms; serverless efficiency for stateless workloads, and Kubernetes control for complex microservices and stateful components.

For a unified view of the disparate components that are deployed with a hybrid approach and to see how they work together as a cohesive application, you can use [App Hub](https://docs.cloud.google.com/app-hub/docs/overview). For more information, see [App Hub supported resources](https://docs.cloud.google.com/app-hub/docs/supported-resources).

## Considerations

GKE and Cloud Run complement each other, addressing different needs within a complex application landscape.

The following are some considerations when adopting a hybrid approach to deploying workloads:

  * Run stateless microservices on Cloud Run for cost efficiency and scalability.

  * Deploy complex stateful applications requiring deep customization on GKE.

  * If you use a private network on Google Cloud, to access resources in your GKE cluster from your Cloud Run service, you can send a request to a [Virtual Private Cloud (VPC)](https://docs.cloud.google.com/vpc/docs/vpc) network by using Direct VPC egress. To access Kubernetes Services in the GKE cluster, the Cloud Run service must be connected to the cluster's VPC network, and the Kubernetes Service must use an [internal passthrough Network Load Balancer](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/internal-load-balancing).

  * To migrate traffic between Cloud Run and GKE, you can expose external endpoints behind a [Global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https). When you implement this load balancer in front of services in both runtimes, you're able to deploy the same application across both Cloud Run and GKE, enabling you to gradually shift traffic from one platform to the other.

  * To expose Cloud Run services in Virtual Private Cloud behind private IPs, use an internal load balancer.




Remember, if your workloads are already on Cloud Run, you can always migrate to GKE as needed.

## When not to use GKE and Cloud Run together

While GKE and Cloud Run offer a compelling approach for many containerized workloads, there are situations where using them together might not be the best fit. Here are some examples when you might decide not to adopt a hybrid approach:

  * **Tightly-coupled microservices** : If your microservices are highly dependent on each other and require frequent, low-latency communication, managing them across separate platforms can introduce complexities. Frequent network calls between platforms could add overhead and potential bottlenecks, impacting performance.

  * **Legacy applications with custom dependencies** : If your application relies on specific libraries, frameworks, or configurations not supported by Cloud Run, using it for parts of the application might require significant refactoring or workarounds. This can negate the serverless benefits and introduce platform-specific maintenance overhead.

  * **Budget constraints with predictable workloads** : If your workload has consistent resource requirements and you're on a tight budget, GKE's pay-per-node model might be more cost-effective than Cloud Run's pay-per-use billing. If you have predictable workloads, you might not fully use the automatic scaling benefits of Cloud Run, making GKE's fixed cost more attractive.




The best approach ultimately depends on your specific needs and priorities. Carefully evaluate your application's requirements, resource constraints, and team expertise before deciding on a hybrid GKE and Cloud Run architecture.

## What's next

  * Learn how to convert your Cloud Run service into a Kubernetes deployment in [Migrate from Cloud Run to GKE](https://docs.cloud.google.com/run/docs/migrate/to-gke).

  * Package your Kubernetes deployment into a Cloud Run-compatible container following [Migrate from Kubernetes to Cloud Run](https://docs.cloud.google.com/run/docs/migrate/from-kubernetes).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
