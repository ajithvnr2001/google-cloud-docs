---
url: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/environment-hybrid-pattern/
title: Environment hybrid pattern \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:21.247727+00:00
---

# Environment hybrid pattern  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/environment-hybrid-pattern/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Environment hybrid pattern Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-01-23 UTC

With the _environment hybrid_ architecture pattern, you keep the production environment of a workload in the existing data center. You then use the public cloud for your development and testing environments, or other environments. This pattern relies on the redundant deployment of the same applications across multiple computing environments. The goal of the deployment is to help increase capacity, agility, and resiliency.

When assessing which workloads to migrate, you might notice cases when running a specific application in the public cloud presents challenges:

  * Jurisdictional or regulatory constraints might require that you keep data in a specific country.
  * Third-party licensing terms might prevent you from operating certain software in a cloud environment.
  * An application might require access to hardware devices that are available only locally.



In such cases, consider not only the production environment but all environments that are involved in the lifecycle of an application, including development, testing, and staging systems. These restrictions often apply to the production environment and its data. They might not apply to other environments that don't use the actual data. Check with the compliance department of your organization or the equivalent team.

The following diagram shows a typical _environment hybrid_ architecture pattern:

![Data flowing from a development environment hosted in Google Cloud to a production environment located on-premises or in another cloud environment.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-patterns-and-practices/environment-hybrid.svg)

Running development and test systems in different environments than your production systems might seem risky and could deviate from your existing best practices or from your attempts to minimize differences between your environments. While such concerns are justified, they don't apply if you distinguish between the stages of the development and testing processes:

Although development, testing, and deployment processes differ for each application, they usually involve variations of the following stages:

  * **Development** : Creating a release candidate.
  * **Functional testing or user acceptance testing** : Verifying that the release candidate meets functional requirements.
  * **Performance and reliability testing** : Verifying that the release candidate meets nonfunctional requirements. It's also known as load testing.
  * **Staging or deployment testing** : Verifying that the deployment procedure works.
  * **Production** : Releasing new or updated applications.



Performing more than one of these stages in a single environment is rarely practical, so each stage usually requires one or more dedicated environments.

**Note:** The term _staging environment_ is often confused with _testing environment_.

The primary purpose of a testing environment is to run functional tests. The primary purpose of a staging environment is to test if your application deployment procedures work as intended. By the time a release reaches a staging environment, your functional testing should be complete. Staging is the last step before you deploy software to your production deployment.

To ensure that test results are meaningful and that they apply to the production deployment, the set of environments that you use throughout an application's lifecycle must satisfy the following rules, to the extent possible:

  * All environments are _functionally equivalent_. That is, the architecture, APIs, and versions of operating systems and libraries are equivalent, and systems behave the same across environments. This equivalence avoids situations where applications work in one environment but fail in another, or where defects aren't reproducible.
  * Environments that are used for performance and reliability testing, staging, and production are [_non-functionally equivalent_](https://en.wikipedia.org/wiki/Non-functional_requirement). That is, their performance, scale, and configuration, and the way they're operated and maintained, are either the same or differ only in insignificant ways. Otherwise, performance and staging tests become meaningless.



In general, it's fine if the environments that are used for development and functional testing differ non-functionally from the other environments.

As illustrated in the following diagram, the test and development environments are built on Google Cloud. A managed database, like Cloud SQL, can be used as an option for development and testing in Google Cloud. Development and testing can use the same database engine and version in the on-premises environment, one that's functionally equivalent, or a new version that's rolled out to the production environment after the testing stage. However, because the underlying infrastructure of the two environments aren't identical, this approach to performance load testing isn't valid.

![Development and QA teams send data through Google Cloud test and QA instances to an invalid on-premises production system.](https://docs.cloud.google.com/static/architecture/images/hybrid-multicloud-patterns-and-practices/test-dev.svg)

The following scenarios can fit well with the environment hybrid pattern:

  * Achieve functional equivalence across all environments by relying on Kubernetes as a common runtime layer where applicable and feasible. Google Kubernetes Engine (GKE) can be a key enabling technology for this approach. 
    * Ensure workload portability and abstract away differences between computing environments. With a [zero trust service mesh](https://docs.cloud.google.com/architecture/network-hybrid-multicloud#zero_trust_distributed_architecture), you can control and maintain the required communication separation between the different environments.
  * Run development and functional testing environments in the public cloud. These environments can be functionally equivalent to the remaining environments but might differ in nonfunctional aspects, like performance. This concept is illustrated in the preceding diagram.
  * Run environments for production, staging, and performance (load testing) and reliability testing in the private computing environment, ensuring functional and nonfunctional equivalence.



## Design Considerations

  * **Business needs** : Each deployment and release strategy for applications has its own advantages and disadvantages. To ensure that the approach that you select aligns with your specific requirements, base your selections on a thorough assessment of your business needs and constraints.
  * **Environment differences** : As part of this pattern, the main goal of using this cloud environment is for development and testing. The final state is to host the tested application in the private on-premises environment (production). To avoid developing and testing a capability that might function as expected in the cloud environment and fail in the production environment (on-premises), the technical team must know and understand the architectures and capabilities of both environments. This includes dependencies on other applications and on the hardware infrastructure—for example, security systems that perform traffic inspection.
  * **Governance** : To control what your company is allowed to develop in the cloud and what data they can use for testing, use an approval and governance process. This process can also help your company make sure that it doesn't use any cloud features in your development and testing environments that don't exist in your on-premises production environment.
  * **Success criteria** : There must be clear, predefined, and measurable testing success criteria that align with the software [quality assurance](https://en.wikipedia.org/wiki/Software_quality_assurance) standards for your organization. Apply these standards to any application that you develop and test.
  * **Redundancy** : Although development and testing environments might not require as much reliability as the production environment, they still need redundant capabilities and the ability to test different failure scenarios. Your failure-scenario requirements might drive the design to include redundancy as part of your development and testing environment.



## Advantages

Running development and functional testing workloads in the public cloud has several advantages:

  * You can automatically start and stop environments as the need arises. For example, you can provision an entire environment for each commit or pull request, allow tests to run, and then turn it off again. This approach also offers the following advantages: 
    * You can reduce costs by stopping virtual machine (VM) instances when they're inactive, or by provisioning environments only on demand.
    * You can speed up development and testing by starting [ephemeral environments](https://docs.cloud.google.com/build/docs/overview#build_security) for each pull-request. Doing so also reduces maintenance overhead and reduces inconsistencies in the build environment.
  * Running these environments in the public cloud helps build familiarity and confidence in the cloud and related tools, which might help with migrating other workloads. This approach is particularly helpful if you decide to explore [Workload portability](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns/other-considerations#workload_portability) using containers and Kubernetes—for example, using [GKE](https://docs.cloud.google.com/anthos/docs/concepts/overview) across environments.



#### Best practices

To implement the environment hybrid architecture pattern successfully, consider the following recommendations:

  * Define your application communication requirements, including the optimal network and security design. Then, use the [_mirrored network_ pattern](https://docs.cloud.google.com/architecture/hybrid-multicloud-secure-networking-patterns/mirrored-pattern) to help you design your network architecture to prevent direct communications between systems from different environments. If communication is required across environments, it has to be in a controlled manner.
  * The application deployment and testing strategy you choose should align with your business objectives and requirements. This might involve rolling out changes without downtime or implementing features gradually to a specific environment or user group before wider release.

  * To make workloads portable and to abstract away differences between environments, you might use containers with Kubernetes. For more information, see [GKE hybrid environment reference architecture](https://docs.cloud.google.com/anthos/docs/architecture/anthos-hybrid-environment).

  * Establish a common tool chain that works across computing environments for deploying, configuring, and operating workloads. Using Kubernetes gives you this consistency.

  * Ensure that CI/CD pipelines are consistent across computing environments, and that the exact same set of binaries, packages, or containers is deployed across those environments.

  * When using Kubernetes, use a CI system such as [Tekton](https://tekton.dev/docs/) to implement a deployment pipeline that deploys to clusters and works across environments. For more information, see [DevOps solutions on Google Cloud](https://docs.cloud.google.com/solutions/devops).

  * To help you with the continuous release of secure and reliable applications, incorporate security as an integral part of the DevOps process (DevSecOps). For more information, see [Deliver and secure your internet-facing application in less than an hour using Dev(Sec)Ops Toolkit](https://cloud.google.com/blog/products/networking/introducing-the-devsecops-toolkit).

  * Use the same tools for logging and monitoring across Google Cloud and existing cloud environments. Consider using open source monitoring systems. For more information, see [Hybrid and multicloud monitoring and logging patterns](https://docs.cloud.google.com/architecture/hybrid-and-multi-cloud-monitoring-and-logging-patterns).

  * If different teams manage test and production workloads, using separate tooling might be acceptable. However, using the same tools with different view permissions can help reduce your training effort and complexity.

  * When you choose database, storage, and messaging services for functional testing, use products that have a managed equivalent on Google Cloud. Relying on managed services helps decrease the administrative effort of maintaining development and testing environments.

  * To protect sensitive information, we recommend encrypting all communications in transit. If encryption is required at the connectivity layer, various options are available that are based on the selected hybrid connectivity solution. These options include VPN tunnels, HA VPN over Cloud Interconnect, and MACsec for Cloud Interconnect.




The following table shows which Google Cloud products are compatible with common OSS products.

OSS product | Compatible with Google Cloud product  
---|---  
Apache HBase | Bigtable  
Apache Beam | Dataflow  
CDAP | Cloud Data Fusion  
Apache Hadoop | Managed Service for Apache Spark  
MySQL, PostgreSQL | Cloud SQL  
Redis Cluster, Redis, Memcached | Memorystore  
Network File System (NFS) | Filestore  
JMS, Kafka | Pub/Sub  
Kubernetes | GKE   
  
[ Previous arrow_back  Edge hybrid pattern  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/edge-hybrid-pattern)

[ Next Business continuity hybrid and multicloud patterns  arrow_forward  ](https://docs.cloud.google.com/architecture/hybrid-multicloud-patterns-and-practices/business-continuity-patterns)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-01-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-01-23 UTC."],[],[]] 
