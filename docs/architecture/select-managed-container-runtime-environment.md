---
url: https://docs.cloud.google.com/architecture/select-managed-container-runtime-environment/
title: Select a managed container runtime environment \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:38.364377+00:00
---

# Select a managed container runtime environment  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/select-managed-container-runtime-environment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Select a managed container runtime environment Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-08-30 UTC

This document helps you to assess your application requirements and choose between [Cloud Run](https://docs.cloud.google.com/run) and [Google Kubernetes Engine (GKE) Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview), based on technical and organizational considerations. This document is for cloud architects who need to choose a Google Cloud target container runtime environment for their workloads. It assumes that you're familiar with Kubernetes and Google Cloud, and that you have some knowledge of cloud serverless runtime environments like Cloud Run, Cloud Run functions, or AWS Lambda.

Google Cloud offers several runtime environment options that have a range of capabilities. The following diagram shows the range of Google Cloud managed offerings:

![Google Cloud offerings from most managed to least managed.](https://docs.cloud.google.com/static/architecture/images/select-managed-container-runtime-environment-offerings.svg)

The diagram shows the following:

  * **Most-managed runtime environments** (the focus of this guide):

    * [Cloud Run](https://docs.cloud.google.com/run), which includes [Cloud Run functions](https://docs.cloud.google.com/functions).
    * [GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview).

These options are managed by Google, with no user management of underlying compute infrastructure.

  * **Least-managed runtime environments** :

    * [GKE Standard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode#why-standard), which is optimized for enterprise workloads and offers single-cluster scalability up to 65,000 nodes.
    * [Compute Engine](https://docs.cloud.google.com/compute), which includes the accelerator-optimized [A3 family of virtual machines](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a3-vms) for machine learning (ML) and high performance computing (HPC) workloads.

These options require some degree of user-level infrastructure management, such as the virtual machines (VMs) that underlie the compute capabilities. VMs in GKE Standard are the Kubernetes cluster nodes. VMs in Compute Engine are the core platform offering, which you can customize to suit your requirements.




This guide helps you to choose between the most-managed runtime environments, Cloud Run and GKE Autopilot. For a broader view of Google Cloud runtime environments, see the [Google Cloud Application Hosting Options](https://cloud.google.com/hosting-options) guide.

## Overview of environments

This section provides an overview of Cloud Run and GKE Autopilot capabilities. Cloud Run and GKE Autopilot are both tightly integrated within Google Cloud, so there is a lot of commonality between the two. Both platforms support multiple options for load balancing with Google's highly reliable and scalable [load balancing services](https://docs.cloud.google.com/load-balancing). They also both support [VPC networking](https://docs.cloud.google.com/vpc/docs/vpc), [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap), and [Google Cloud Armor](https://docs.cloud.google.com/armor) for when more granular, private networking is a requirement. Both platforms charge you only for the exact resources that you use for your applications.

From a software delivery perspective, as container runtime environments, Cloud Run and GKE Autopilot are supported by services that make up the Google Cloud container ecosystem. These services include [Cloud Build](https://docs.cloud.google.com/build), [Artifact Registry](https://docs.cloud.google.com/artifact-registry), [Binary Authorization](https://docs.cloud.google.com/binary-authorization), and continuous delivery with [Cloud Deploy](https://docs.cloud.google.com/deploy), to help ensure that your applications are safely and reliably deployed to production. This means that you and your teams own the build and deployment decisions.

Because of the commonality between the two platforms, you might want to take advantage of the strengths of each by adopting a flexible approach to where you deploy your applications, as detailed in the guide [Use GKE and Cloud Run together](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gke-and-cloud-run). The following sections describe unique aspects of Cloud Run and Autopilot.

### Cloud Run

[Cloud Run](https://docs.cloud.google.com/run) is a serverless managed compute platform that lets you run your applications directly on top of Google's scalable infrastructure. Cloud Run provides automation and scaling for two main kinds of applications:

  * [**Cloud Run services**](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run#services): For code that responds to web requests.
  * [**Cloud Run jobs**](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run#cloud-run-jobs): For code that performs one or more background tasks and then exits when the work is done.



With these two deployment models, Cloud Run can support a wide range of application architectures while enabling best practices and letting developers focus on code.

Cloud Run also supports deploying application code from the following sources:

  * Individual lightweight functions
  * Full applications from source code
  * Containerized applications



Cloud Run incorporates a build-and-deploy capability that supports both FaaS and the ability to build from source, alongside the prebuilt container runtime capability. When you use Cloud Run in this way, the steps of [building and deploying](https://cloud.google.com/blog/products/serverless/build-and-deploy-an-app-to-cloud-run-with-a-single-command) the application container image that will be executed are entirely automatic, and they don't require custom configuration from you.

### GKE Autopilot

[GKE Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) is the default and recommended cluster mode of operation in [GKE](https://docs.cloud.google.com/kubernetes-engine). Autopilot lets you run applications on Kubernetes without the overhead of managing infrastructure. When you use Autopilot, Google manages key underlying aspects of your cluster configuration, including node provisioning and scaling, default security posture, and other preconfigured settings. With Autopilot managing node resources, you pay only for the resources that are requested by your workloads. Autopilot continuously monitors and optimizes infrastructure resourcing to ensure the best fit while providing an [SLA](https://cloud.google.com/blog/products/devops-sre/sre-fundamentals-sli-vs-slo-vs-sla) for your workloads.

GKE Autopilot supports workloads that might not be a good fit for Cloud Run. For example, GKE Autopilot commonly supports long-lived or stateful workloads.

## Choose a runtime environment

In general, if the characteristics of your workload are suitable for a managed platform, the serverless runtime environment of Cloud Run is ideal. Using Cloud Run can result in less infrastructure to manage, less self-managed configuration, and therefore lower operational overhead. Unless you specifically want or need Kubernetes, we recommend that you consider serverless first as your target runtime environment. Although Kubernetes provides the powerful abstraction of an open platform, using it adds complexity. If you don't need Kubernetes, then we recommend that you consider whether your application is a good fit for serverless. If there are criteria that make your workload less suitable for serverless, then we recommend using Autopilot.

The following sections provide more detail about some of the criteria that can help you answer these questions, particularly the question of whether the workload is a fit for serverless. Given the commonality between Autopilot and Cloud Run that's described in the preceding sections, migration between the platforms is a straightforward task when there aren't any technical or other blockers. To explore migration options in more detail, see [Migrate from Cloud Run to GKE](https://docs.cloud.google.com/run/docs/migrate/to-gke) and [Migrate from Kubernetes to Cloud Run](https://docs.cloud.google.com/run/docs/migrate/from-kubernetes).

When you choose a runtime environment for your workload, you need to factor in technical considerations and organizational considerations. Technical considerations are characteristics of your application or the Google Cloud runtime environment. Organizational considerations are non-technical characteristics of your organization or team that might influence your decision.

### Technical considerations

Some of the technical considerations that will influence your choice of platform are the following:

  * **Control and configurability** : Granularity of control of the execution environment.
  * **Network traffic management and routing** : Configurability of interactions over the network.
  * **Horizontal and vertical scalability** : Support for dynamically growing and shrinking capacity.
  * **Support for stateful applications** : Capabilities for storing persistent state.
  * **CPU architecture** : Support for different CPU types.
  * **Accelerator offload (GPUs and TPUs)** : Ability to offload computation to dedicated hardware.
  * **High memory, CPU, and other resource capacity** : Level of various resources consumed.
  * **Explicit dependency on Kubernetes** : Requirements for Kubernetes API usage.
  * **Complex RBAC for multi-tenancy** : Support for sharing pooled resources.
  * **Maximum container task timeout time** : Execution duration of long-lived applications or components.



The following sections detail these technical considerations to help you choose a runtime environment.

#### Control and configurability

Compared to Cloud Run, GKE Autopilot provides more granular control of the execution environment for your workloads. Within the context of a [Pod](https://kubernetes.io/docs/concepts/workloads/pods/), Kubernetes provides many configurable primitives that you can tune to meet your application requirements. Configuration options include [privilege level](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/), [quality of service parameters](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/), [custom handlers for container lifecycle events](https://kubernetes.io/docs/tasks/configure-pod-container/attach-handler-lifecycle-event/), and [process namespace sharing](https://kubernetes.io/docs/tasks/configure-pod-container/share-process-namespace/) between multiple containers.

Cloud Run directly supports a subset of the [Kubernetes Pod API surface](https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/), which is described in the [reference YAML for the Cloud Run Service object](https://docs.cloud.google.com/run/docs/reference/yaml/v1#service) and in the [reference YAML for the Cloud Run Job object](https://docs.cloud.google.com/run/docs/reference/yaml/v1#job). These reference guides can help you to evaluate the two platforms alongside your application requirements.

The [container contract for the Cloud Run execution environment](https://docs.cloud.google.com/run/docs/container-contract) is relatively straightforward and will suit most serving workloads. However, the contract specifies some requirements that must be fulfilled. If your application or its dependencies can't fulfill those requirements, or if you require a finer degree of control over the execution environment, then Autopilot might be more suitable.

If you want to reduce the time that you spend on configuration and administration, consider choosing Cloud Run as your runtime environment. Cloud Run has fewer configuration options than Autopilot, so it can help you to maximize developer productivity and reduce operational overhead.

#### Network traffic management and routing

Both Cloud Run and GKE Autopilot [integrate with Google Cloud Load Balancing](https://docs.cloud.google.com/load-balancing). However, GKE Autopilot additionally provides a [rich and powerful set of primitives](https://kubernetes.io/docs/concepts/services-networking/) for configuring the networking environment for service-to-service communications. The configuration options include granular permissions and segregation at the network layer by using [namespaces](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/) and [network policies](https://kubernetes.io/docs/concepts/services-networking/network-policies/), port remapping, and built-in DNS service discovery within the cluster. GKE Autopilot also supports the highly configurable and flexible [Gateway API](https://gateway-api.sigs.k8s.io/). This functionality provides powerful control over the way that traffic is routed into and between services in the cluster.

Because Autopilot is highly configurable, it can be the best option if you have multiple services with a high degree of networking codependency, or complex requirements around how traffic is routed between your application components. An example of this pattern is a distributed application that is decomposed into numerous [microservices](https://en.wikipedia.org/wiki/Microservices) that have complex patterns of interdependence. In such scenarios, Autopilot networking configuration options can help you to manage and control the interactions between services.

#### Horizontal and vertical scalability

Cloud Run and GKE Autopilot both support manual and automatic horizontal scaling for services and jobs. Horizontal scaling provides increased processing power when required, and it removes the added processing power when it isn't needed. For a typical workload, Cloud Run can usually scale out more quickly than GKE Autopilot to respond to spikes in the number of requests per second. As an example, the video demonstration ["What's New in Serverless Compute?"](https://www.youtube.com/watch?v=Zfnhg1wneiA&t=2308s) shows Cloud Run scaling from zero to over 10,000 instances in approximately 10 seconds. To increase the speed of horizontal scaling on Kubernetes (at some additional cost), Autopilot lets you [provision extra compute capacity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/capacity-provisioning).

If your application can't scale by adding more instances to increase the level of resources that are available, then it might be a better fit for Autopilot. Autopilot supports [vertical scaling](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/verticalpodautoscaler) to dynamically vary the amount of processing power that's available without increasing the number of running instances of the application.

Cloud Run can automatically scale your applications down to zero replicas while they aren't being used, which is helpful for certain use cases that have a special focus on cost optimization. Because of the [characteristics of how your applications can scale to zero](https://docs.cloud.google.com/run/docs/about-instance-autoscaling), there are [multiple optimization steps](https://docs.cloud.google.com/run/docs/tips/general#optimize_performance) that you can take to minimize the time between the arrival of a request and the time at which your application is up and running, and able to process the request.

#### Support for stateful applications

Autopilot offers complete Kubernetes Volume support, backed by Persistent Disks that let you run a broad range of stateful deployments, including self-managed databases. Both Cloud Run and GKE Autopilot let you connect with other services like Filestore and Cloud Storage buckets. They also both include the ability to mount object-store buckets into the file system with [Cloud Storage FUSE](https://docs.cloud.google.com/storage/docs/gcs-fuse).

Cloud Run uses an in-memory file system, which might not be a good fit for applications that require a _persistent_ local file system. In addition, the local in-memory file system is shared with the memory of your application. Therefore, both the ephemeral file system and the application and container memory usage contribute towards exhausting the memory limit. You can avoid this issue if you use a [dedicated in-memory volume](https://docs.cloud.google.com/run/docs/configuring/in-memory-volumes) with a size limit.

A Cloud Run service or job container has a maximum [task timeout](https://docs.cloud.google.com/run/docs/configuring/request-timeout). A container running within a pod in an Autopilot cluster can be rescheduled, subject to any constraints that are configured with [Pod Disruption Budgets (PDBs)](https://kubernetes.io/docs/tasks/run-application/configure-pdb/). However, pods can run for up to seven days when they're [protected from eviction](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/extended-duration-pods) caused by node auto-upgrades or scale-down events. Typically, task timeout is more likely to be a consideration for batch workloads in Cloud Run. For long-lived workloads, and for batch tasks that can't be completed within the maximum task duration, Autopilot might be the best option.

#### CPU architecture

All Google Cloud compute platforms support x86 CPU architecture. Cloud Run doesn't support [Arm architecture processors](https://en.wikipedia.org/wiki/ARM_architecture_family), but Autopilot supports managed nodes that are backed by [Arm architecture](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-arm-workloads). If your workload requires Arm architecture, you will need to use Autopilot.

#### Accelerator offload

Autopilot [supports the use of GPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-gpus) and [the use of TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tpus-autopilot), including the ability to consume [reserved resources](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations). Cloud Run [supports the use of GPUs](https://docs.cloud.google.com/run/docs/configuring/services/gpu) with some [limitations](https://docs.cloud.google.com/run/docs/configuring/services/gpu#before-you-begin).

#### High memory, CPU, and other resource requirements

Compared to [GKE Autopilot resource request limits](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-resource-requests#compute-class-min-max), the maximum CPU and memory resources that can be consumed by a single Cloud Run service or job (a single instance) is [limited](https://docs.cloud.google.com/run/quotas). Depending on the characteristics of your workloads, Cloud Run might have other limits that constrain the resources that are available. For example, the startup timeout and the maximum number of outbound connections might be limited with Cloud Run. With Autopilot, some limits might not apply or they might have higher permitted values.

#### Explicit dependency on Kubernetes

Some applications, libraries, or frameworks might have an explicit dependency on Kubernetes. The Kubernetes dependency might be a result of one of the following:

  1. The application requirements (for example, the application calls Kubernetes APIs, or uses Kubernetes [custom resources](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/)).
  2. The requirements of the tooling that's used to configure or deploy the application (such as [Helm](https://helm.sh/)).
  3. The support requirements of a third-party creator or supplier.



In these scenarios, Autopilot is the target runtime environment because Cloud Run doesn't support Kubernetes.

#### Complex RBAC for multi-tenancy

If your organization has particularly complex organizational structures or requirements for multi-tenancy, then use Autopilot so that you can take advantage of Kubernetes' [Role-Based Access Control (RBAC)](https://kubernetes.io/docs/reference/access-authn-authz/rbac/). For a simpler option, you can use the security and segregation capabilities that are built in to Cloud Run.

### Organizational considerations

The following are some of the organizational considerations that will influence your choice of environment:

  * **Broad technical strategy** : Your organization's technical direction.
  * **Leveraging the Kubernetes ecosystem** : Interest in leveraging the OSS community.
  * **Existing in-house tooling** : Incumbent use of certain tooling.
  * **Development team profiles** : Developer skill-sets and experience.
  * **Operational support** : Operations teams' capabilities and focus.



The following sections detail these organizational considerations to help you choose an environment.

#### Broad technical strategy

Organizations or teams might have agreed-upon strategies for preferring certain technologies over others. For example, if a team has an agreement to standardize where possible on either serverless or Kubernetes, that agreement might influence or even dictate a target runtime environment.

If a given workload isn't a good fit for the runtime environment that's specified in the strategy, you might decide to do one or more of the following, with the accompanying caveats:

  * **Rearchitect the workload**. However, if the workload isn't a good fit, doing so might result in non-optimal performance, cost, security, or other characteristics.
  * **Register the workload as an exception to the strategic direction**. However, if exceptions are overused, doing so can result in a disparate technology portfolio.
  * **Reconsider the strategy**. However, doing so can result in policy overhead that can impede or block progress.



#### Leveraging the Kubernetes ecosystem

As part of the broad technical strategy described earlier, organizations or teams might decide to select Kubernetes as their platform of choice because of the significant and growing ecosystem. This choice is distinct from selecting Kubernetes because of technical application dependencies, as described in the preceding section Explicit dependency on Kubernetes. The consideration to use the Kubernetes ecosystem places emphasis on an active community, rich third-party tooling, and strong standards and portability. Leveraging the Kubernetes ecosystem can accelerate your development velocity and reduce time to market.

#### Existing in-house tooling

In some cases, it can be advantageous to use existing tooling ecosystems in your organization or team (for any of the environments). For example, if you're using Kubernetes, you might opt to continue using deployment tooling like [ArgoCD](https://argo-cd.readthedocs.io/en/stable/), security and policy tooling like [Gatekeeper](https://open-policy-agent.github.io/gatekeeper/website/), and package management like [Helm](https://helm.sh/). Existing tooling might include established rules for organizational compliance automation and other functionality that might be costly or require a long lead-time to implement for an alternative target environment.

#### Development team profiles

An application or workload team might have prior experience with Kubernetes that can accelerate the team's velocity and capability to deliver on Autopilot. It can take time for a team to become proficient with a new runtime environment. Depending on the operating model, doing so can potentially lead to lower platform reliability during the upskilling period.

For a growing team, hiring capability might influence an organization's choice of platform. In some markets, Kubernetes skills might be scarce and therefore command a hiring premium. Choosing an environment such as Cloud Run can help you to streamline the hiring process and allow for more rapid team growth within your budget.

#### Operational support

When you choose a runtime environment, consider the experience and abilities of your [SRE](https://sre.google/), DevOps, and platforms teams, and other operational staff. The capabilities of the operational teams to effectively support the production environment are crucial from a reliability perspective. It's also critical that operational teams can support pre-production environments to ensure that developer velocity isn't impeded by downtime, reliance on manual processes, or cumbersome deployment mechanisms.

If you use Kubernetes, a central operations or platform engineering team can handle [Autopilot Kubernetes upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot). Although the upgrades are automatic, operational staff will typically closely monitor them to ensure minimal disruptions to your workloads. Some organizations choose to [manually upgrade control plane versions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot#manual-upgrade). GKE also includes capabilities to streamline and simplify the management of applications across multiple clusters.

In contrast to Autopilot, Cloud Run doesn't require ongoing management overhead or upgrades of the control plane. By using Cloud Run, you can simplify your operations processes. By selecting a single runtime environment, you can further simplify your operations processes. If you opt to use multiple runtime environments, you need to ensure that the team has the capacity, capabilities, and interest to support those runtime environments.

## Selection

To begin the selection process, talk with the various stakeholders. For each application, assemble a working group that consists of developers, operational staff, representatives of any central technology governance group, internal application users and consumers, security, cloud financial optimization teams, and other roles or groups within your organization that might be relevant. You might choose to circulate an information-gathering survey to collate application characteristics, and share the results in advance of the session. We recommend that you select a small working group that includes only the required stakeholders. All representatives might not be required for every working session.

You might also find it useful to include representatives from other teams or groups that have experience in building and running applications on either Autopilot or Cloud Run, or both. Use the technical and organizational considerations from this document to guide your conversation and evaluate your application's suitability for each of the potential platforms.

We recommend that you schedule a check-in after some months have passed to confirm or revisit the decision based on the outcomes of deploying your application in the new environment.

## What's next

  * Learn more about these runtime environments with the [GKE Autopilot Qwik Start](https://www.cloudskillsboost.google/catalog_lab/4069) and the [Cloud Run lab](https://www.cloudskillsboost.google/catalog_lab/3137).
  * Read more about migrating [from Cloud Run to GKE](https://docs.cloud.google.com/run/docs/migrate/to-gke) and from [Kubernetes to Cloud Run](https://docs.cloud.google.com/run/docs/migrate/from-kubernetes).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Henry Bell](https://www.linkedin.com/in/henry-bell-uk) | Cloud Solutions Architect

Other contributors: 

  * [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect
  * [Gari Singh](https://www.linkedin.com/in/garisingh) | Outbound Product Manager
  * [Maridi (Raju) Makaraju](https://www.linkedin.com/in/mmraju) | Supportability Tech Lead
  * [Parag Doshi](https://www.linkedin.com/in/paragdoshi) | Key Enterprise Architect
  * Daniel Stamer | Customer Engineer, Digital Natives
  * [Steren Giannini](https://www.linkedin.com/in/steren) | Group Product Manager
  * [Victor Szalvay](https://www.linkedin.com/in/victorszalvay) | Senior Product Manager
  * [William Denniss](https://www.linkedin.com/in/williamdenniss) | Group Product Manager



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-08-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-08-30 UTC."],[],[]] 
