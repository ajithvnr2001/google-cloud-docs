---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-user-guide/
title: Modern CI/CD with GKE: A software delivery framework \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:02:14.285692+00:00
---

# Modern CI/CD with GKE: A software delivery framework  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-user-guide/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Modern CI/CD with GKE: A software delivery framework Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes a framework for implementing modern continuous integration/continuous delivery (CI/CD) processes on a multi-team software delivery platform that uses [Google Kubernetes Engine](https://cloud.google.com/kubernetes-engine).

You can then iterate on the platform to further improve performance for development and operations, including release velocity, platform reliability, and recovery time from failures.

This document is part of a series:

  * Modern CI/CD with GKE: A software delivery framework (this document)

  * [Modern CI/CD with GKE: Build a CI/CD system](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture) (reference architecture)

  * [Modern CI/CD with GKE: Apply the developer workflow](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-developer-workflow)




This document is intended for enterprise architects and application developers, as well as IT security, DevOps, and Site Reliability Engineering teams. Some experience with automated deployment tools and processes is useful for understanding the concepts in this document.

## A case for modern CI/CD

CI/CD is a software development approach that lets you automate the build, test, and deployment phases of software development by using a number of tools and repeatable processes.

In addition to CI/CD automation, Kubernetes and containers have enabled enterprises to achieve unprecedented improvements in the speed of development and deployment. Yet, even as Kubernetes and container adoption grows, many organizations don't fully realize the benefits in release velocity, stability, and operational efficiencies because their CI/CD practices don't take full advantage of Kubernetes or address operations and security concerns.

A truly modern CI/CD approach needs to encompass more than just automation. To fully realize improvements in speed and security, and to use the power of Kubernetes and containers, you need to streamline your application onboarding, CI/CD practices, and operational processes.

Using the consistent infrastructure offered by the GKE platform, uniform CI/CD methods, and best practices in implementation, your organization can gain the following benefits for development and operations:

  * Reducing lead time for changes.

    * Let operations and security teams create and update best practices for provisioning applications and provisioning policy across the platform.

    * Simplify application onboarding by giving teams fully functioning and deployable starter projects that have your organization's best practices built in.

  * Decreasing the time required to restore service.

    * Manage all configuration declaratively using GitOps for simplified audit, rollback, and review.

    * Standardize deployment and monitoring methodologies across the organization to decrease the time it takes to identify the contributing factors of a service-impacting issue.

  * Increasing deployment frequency.

    * Ensure that application developers can iterate independently in their own development sandboxes (or _landing zones_) without interfering with each other.

    * Use GitOps for deployment, improved release management, and change tracking.

    * Implement guard rails so that service teams are empowered to deploy frequently.

    * Create a progressive rollout process for deploying consistently across pre-production environments, giving developers the confidence they need to deploy changes to production.




To see how these benefits and concepts are realized with GKE and CI/CD, see the other documents in this series:

  * [Modern CI/CD with GKE: Building a CI/CD system](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture)

  * [Modern CI/CD with GKE: Applying the developer workflow](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-developer-workflow)




## Assess readiness for a modern approach

Before you implement modern CI/CD tools and processes with GKE, you need to assess whether your organization and teams are ready to adopt a new platform.

### Organizational traits

Adopting a modern platform requires the following support from your business leadership and technical teams:

  * **Leadership sponsor.** Adopting a software delivery platform is typically a large effort undertaken by multiple cross-functional teams. The process usually results in changes to roles and responsibilities as well as software development practices. To be successful in adopting these tools and techniques, you need strong support from one or more members of the leadership team. The most [effective leadership sponsors](https://docs.cloud.google.com/solutions/devops/devops-culture-westrum-organizational-culture) are those who view these changes as a continuous process of improvement and want to empower their teams instead of manage them.

  * **Technical and business strategy alignment.** We recommend that your business teams and technical teams align on the four key software delivery measures defined by [DevOps Research and Assessment (DORA)](https://docs.cloud.google.com/devops): lead time for changes, deployment frequency, time to restore service, and change failure rate. Aligning on those measures gives your business teams and technical teams a common goal, enabling them to jointly calculate return on investment, adjust the rate of change, and modify the level of investment.

  * **Resources.** To be successful, teams developing modern CI/CD practices and building tool chains need the necessary resources: time, people, and infrastructure. These teams need the time to [try and select the best processes and tools](https://docs.cloud.google.com/solutions/devops/devops-tech-teams-empowered-to-choose-tools). Ideally, these teams represent many different functions in the software delivery process and can pull in other resources from across the organization. Lastly, the teams need the ability to provision infrastructure, including cloud resources and software tools.

  * **Openness to adopt new tools.** Modern CI/CD tools and techniques often come with new tools and processes. Teams need to [experiment with those processes and tools](https://docs.cloud.google.com/solutions/devops/devops-process-team-experimentation) and be open to adopting them. A [feedback loop](https://docs.cloud.google.com/solutions/devops/devops-process-customer-feedback) is needed so that platform teams can hear from the application, operations, and security teams that are using the platform.

  * **Cultural readiness.** To be successful in deploying and adopting a modern CI/CD system with GKE, the organization and the technical teams developing the system need to be prepared to change how they operate and work together. For example, development and operations teams need to be willing to take more [responsibility for security](https://docs.cloud.google.com/solutions/devops/devops-tech-shifting-left-on-security), and security and operations teams need to be willing to [streamline change approval processes](https://docs.cloud.google.com/solutions/devops/devops-process-streamlining-change-approval).




### Technical capabilities

Adopting a modern CI/CD approach also requires that your teams are technically prepared in the following ways:

  * **Experience with containers.** Teams that are adopting modern CI/CD approaches need some experience with containers. Ideally, this experience includes development techniques for building container images and combining containers to build larger systems.

  * **Continuous integration strategy.** Teams need some experience using CI tools (such as Jenkins, TeamCity, Bamboo, and CircleCI) and performing some [continuous integration](https://docs.cloud.google.com/solutions/devops/devops-tech-continuous-integration) and [automated testing](https://docs.cloud.google.com/solutions/devops/devops-tech-test-automation). We recommend that organizations plan how to further enhance those processes.

  * **Deployment automation.** Teams need some experience with [deployment automation](https://docs.cloud.google.com/solutions/devops/devops-tech-deployment-automation). Examples of automated deployment tools include basic shell scripts, Terraform, Chef, or Puppet. Having a baseline knowledge of automated deployment tools and processes is critical for streamlining and automating deployments.

  * **Service-oriented architectures.** While it isn't a prerequisite to adoption of modern CI/CD processes, adoption of more [modular and service-oriented architectures](https://docs.cloud.google.com/solutions/devops/devops-tech-architecture) must be a long-term goal of organizations that want to adopt modern CI/CD tools and techniques with GKE. Service-based architectures have been shown to improve velocity and reliability.

  * **Modern source control.** Modern source control tools like Git let teams establish workflows like [trunk-based development](https://docs.cloud.google.com/solutions/devops/devops-tech-trunk-based-development), feature branches, and merge requests.




## Design modern CI/CD with GKE

This section describes a software delivery platform and its components. To improve software delivery performance, you need to implement CI/CD and other technical best practices that let teams release quickly and operate efficiently.

This section also discusses the infrastructure needed to support the software delivery lifecycle and how to consistently manage that infrastructure with GKE. Lastly, this section provides an example software delivery workflow and shows how starter repositories simplify the onboarding and implementation of best practices. The following design considerations are reviewed:

  * **Software delivery platform.** The framework and technical capabilities that make up the foundations of a high-velocity, reliable application release process.

  * **Platform infrastructure.** The infrastructure components and management considerations you need to build the platform and run your applications.

  * **Software delivery workflow.** How teams work together to build, test, and deploy code more efficiently.

  * **Code repositories.** Repositories that perform several functions including storing the actual business logic, application specific configuration, and code to build infrastructure. These could also be starter repositories that facilitate the adoption of best practices and help maintain consistency across automated processes.

  * **Application landing zones.** Logic entity that lets developers autonomously deploy and iterate on their applications using the guard rails that you put in place.

  * **Operating model.** Technical tools, processes, and methods for managing the infrastructure and applications that make up the platform.

  * **Governance.** Processes and considerations that you need to maintain and manage the software delivery platform.




### Software delivery platforms

A software delivery platform unifies the tools and streamlines the processes needed to build, deliver, deploy, and operate applications.

Responsibility for maintaining an application's configuration, stability, uptime, and scale varies between operators, security, and developer teams, but all of the components and teams need to work together to speed up releases. Although this document describes methods to improve source control management and application observability, it focuses mainly on continuous integration (CI), continuous delivery (CD), and configuration management.

To build a complete software delivery platform, you need each component in the following diagram:

![Management of the platform can be shared or performed by special teams.](https://docs.cloud.google.com/static/architecture/images/modern-cicd-gke-user-guide-software-delivery-platforms.svg)

Each of these components provides functionality to the system and applications running on the platform:

  * **Infrastructure monitoring.** The base level of monitoring needed when provisioning in order to verify the correct functioning of [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine) clusters, virtual machine (VM) instances, and other infrastructure required for applications to function.

  * **Container orchestration.** The platform that coordinates the deployment and operation of container-based applications. Examples of platforms for container orchestration are Kubernetes, GKE, or GKE Enterprise.

  * **Container registry.** The storage and access control for container images.

  * **CI.** The process of applying automated tasks to an application before deployment. CI tasks typically include building, packaging, and testing. The types of tasks vary based on the application and organization.

  * **CD.** Deployment processes that are highly automated and applied with high frequency. Example methodologies include manual approvals, canary deployments, blue-green deployments, or rolling deployments.

  * **Policy.** Security and infrastructure configuration policies defined by the operations and security teams and continuously applied and enforced by the platform.

  * **Source code management.** For example, version-controlled storage for code, configuration files, and policy definitions. In a modern CI/CD system, source code management is typically Git.

  * **Configuration management.** The system that is used in storing and applying application configuration for different environments.

  * **Application observability.** The application-level logging, monitoring, alerting, and tracing that developer, operator, and security teams use to troubleshoot and verify the proper operation of the applications.




### Platform infrastructure

To build a scalable software delivery platform, you need Kubernetes clusters for development, pre-production environments, and multiple production clusters. Clusters can serve many different functions:

  * **Development.** In these clusters, developers perform ad hoc deployments of their applications for testing and experimentation.

  * **The application environment.**

    * **Pre-production.** For each pre-production environment in your workflow, you should have a Kubernetes cluster to host your applications. These clusters should resemble the production clusters so that you can reduce or eliminate differences between the environments and, as a result, improve deployment success rates.

    * **Production.** These clusters run your production workloads. You should use multiple, geographically distributed clusters. Doing so improves reliability from infrastructure failures and eases Day 2 operations concerns, such as cluster upgrades and scaling.




The following diagram shows the high-level architecture: ![Three clusters span two Google Cloud regions.](https://docs.cloud.google.com/static/architecture/images/modern-cicd-gke-user-guide-platform-infrastructure.svg)

In this architecture, you manage the clusters for each environment through [Config Sync](https://docs.cloud.google.com/anthos-config-management/docs/config-sync-overview). Consistent cluster configuration is critical because it gives developer, operator, and security teams confidence that pre-production and production environments operate in similar ways. You can use Config Sync to store and apply common configurations across your fleet of clusters. After your cluster configuration is standardized, auditable, and scalable, you can focus on the software delivery workflow and onboarding and deploying applications.

You manage your deployments to dev, staging and production clusters through the application's CI/CD pipelines. The source control management serves as the coordination point for application code and configuration. The CI/CD pipelines and the container images for an application are isolated to that application's environment. You initialize application and configuration repositories by using starter repositories and automated tools. For example, you can use [Cloud Build to run Terraform](https://github.com/GoogleCloudPlatform/software-delivery-blueprint/blob/single-project-blueprint/app-factory-template/templates/application.tf.tpl) to onboard and initialize new applications automatically.

You deploy applications into their own landing zones on each cluster, so that applications are network- and identity-isolated. You initialize application landing zones across environments by using Config Sync, and you use [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview) or [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress) to make the production clusters seem like one cluster by creating a network mesh that spans many clusters.

### Software delivery workflow

A core component of the software delivery platform is the CI/CD system. When platform builders begin to define the CI/CD process, they need to ensure that each component produces or consumes artifacts that adhere to a standardized interface. Using a standardized interface simplifies the replacement of components when a better implementation comes to market.

When you create a platform for containerized applications, you can use the three standardized interfaces between components: Git repositories, Docker images, and Kubernetes manifests. These interfaces let you create a reusable and flexible CI/CD pipeline with a development, build, and release workflow, as the following diagram shows:

![The stages of the workflow include commit, generate, output, store, and apply.](https://docs.cloud.google.com/static/architecture/images/modern-cicd-anthos-user-guide-software-delivery-workflow.svg)

This workflow works as follows:

  1. Developers commit their application code to the code repositories.

  2. The CI system tests the code, creates a Docker image artifact, and stores the artifact in a registry.

  3. After the artifact is ready for deployment, a reference to it is added to the application configuration.

  4. That application configuration is rendered into a Kubernetes-readable format and stored in a code repository. Updates to this repository triggers a deployment pipeline that deploys the artifacts in an integrated development environment.

  5. After the testing in the integrated development environment is done, operators promote the deployment to the pre-production environment.

  6. After making sure the application is working as expected in the pre-production environment, operators obtain the approvals in the deployment pipeline and promote the release to the production environment.

  7. When operators make changes to the base configurations, those changes are applied across the organization. As operators commit changes to their repositories, application configuration updates (and subsequent deployments) can be triggered automatically. Or, the operators' changes can be picked up the next time developers deploy their changes.

  8. In parallel, security engineers can implement and tweak policies that define what can be deployed, and then commit those policies to their policy repository.




Using a GitOps methodology, you can require a declarative approach for any changes to applications and clusters. With this approach, all changes are subject to audit and review before they can be enforced. In this declarative model, you store your configuration files in a Git repository, which lets you maintain a log of changes, rollback failed deployments, and see the potential impact of changes being proposed.

In the associated [reference architecture](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture), you use [`kustomize`](https://github.com/kubernetes-sigs/kustomize#kustomize) to control the application configurations in your organization. The `kustomize` tool lets operators create so-called bases of application configurations that your development teams can tweak without needing to add or change any code in the base. By defining base configurations, platform teams can create and iterate on best practices for the organization. Operators and developers can iterate on their deployments independently, with developers applying the best practices set up by the operators. When operators need to implement a new best practice for the organization, they make the change in the base, and the change is automatically pulled in with the developers' next deployment.

### Code repositories

Source code repositories are at the heart of the CI/CD system. Operators, developers, and security engineers each have their own repositories to propagate changes into the platform. Using a Git repository as the basis for all changes in the system provides several benefits:

  * **Built-in auditability.** Commits contain information about when, what, and who changed the system.

  * **A simplified rollback process.** Git's revert capability lets you rollback to a previous state of the system.

  * **Versioning.** You can tag Git commits to denote a version of the system's state.

  * **Transactions.** You must explicitly resolve state conflicts and review them before you can integrate the changes into the state.




The following diagram shows how various teams interact with a centralized repository for all changes:

![Repositories include those for best practices as well as application and platform configuration.](https://docs.cloud.google.com/static/architecture/images/modern-cicd-gke-user-guide-code-repositories.svg)

The following sections explain how operators, developers, and security engineers employ the Git repository in a modern CI/CD system.

#### Operator repositories

Operator-managed repositories contain best practices for CI/CD and application configuration to help your teams onboard applications while adopting organizational best practices from the start. With operators managing repositories, developers can consume any updates to the organizational best practices with as little disruption to their workflow as possible.

Operators can encode their organizations' best practices into two repositories. The first repository is where operators maintain shared CI/CD pipeline best practices. In this repository, operators provide developers with a library of predefined tasks that they can use to build out their pipelines. The developers' application repositories automatically inherit these tasks and the logic within them; the tasks don't need to be manually copied over. Examples of the tasks that you can standardize across the organization include the following:

  * Artifact building and storage

  * Testing methodologies for various languages

  * Deployment steps

  * Policy checks

  * Security scanning




The second repository that operators maintain stores best practices for configuring an application. In the context of GKE, best practices involve ensuring a way to manage declarative manifests in the [Kubernetes resource model](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/). These manifests describe the intended state of the application. Operators can create base configurations for different types of applications, providing developers a streamlined path for deploying their apps according to organizational best practices.

#### Application repositories

Application repositories store the business logic of the application and any specialized configuration that is needed for the application to properly operate.

As operators create and maintain best practices in a codified way, developers can use those best practices. To do so, developers reference the tasks for CI/CD and the application bases that the operators created in their own repositories. After developers make their changes, operators can further customize the application's deployment by adding environment-specific configurations such as database URLs or resource labels and annotations.

Examples of the artifacts that you can store in application repositories include the following:

  * Application source code

  * A `Dockerfile` that describes how to build and run the application

  * The CI/CD pipeline definition

  * Extensions or modifications to the application configuration bases created by operators




#### Infrastructure as code repositories

Infrastructure as code repositories store the code to build out the infrastructure required to run the applications. The infrastructure might include networking and container orchestration platforms like GKE. Typically, infrastructure admins own these repositories. Operators can update them to implement best practices.

Examples of the artifacts that you can store in application repositories include the following:

  * Declarative language code (Terraform, Pulumi) that represents infrastructure objects.
  * Shell or python scripts that complement the declarative API definitions.

  * Extensions or modifications to the base infrastructure templates created by the infrastructure team.




#### Configuration and policy repositories

Ensuring a security-enhanced and consistent platform is a top priority for both operators and security engineers.

##### Configuration

Centralized configuration lets you propagate configuration changes throughout the system. Some common configuration items that you can manage centrally include the following:

  * Kubernetes namespaces

  * Quotas

  * Role-based access controls (RBAC)

  * Network policies




You should consistently enforce these types of configurations throughout your clusters so that application teams don't misuse or abuse the infrastructure. Using [a Git repository](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/concepts/sources-of-truth#git_repositories) to store configuration can enhance processes such as auditing and deploying configuration through methods such as GitOps. Tools like Config Sync can simplify the process of uniformly applying configurations across your infrastructure.

##### Policy

Because developers can extend the base configurations that operators create, you need a way to constrain the resources created in the clusters that make up the platform. In some cases, you might create a policy that lets developers create resources only if those resources meet specific requirements—for example, creating Kubernetes Service objects that cannot be configured for external load balancing.

In the associated [reference architecture](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture), you use [Policy Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/policy-controller) to enforce policies.

### Starter repositories

Starter repositories aid the adoption of CI/CD, infrastructure, and development best practices across the platform. Starter repositories can greatly reduce the cost associated with adopting best practices. The best practices, in turn, help to increase feature velocity, reliability, and team productivity. In the associated [reference architecture](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture), there are multiple [starter repositories](https://github.com/GoogleCloudPlatform/software-delivery-blueprint/tree/main/app-template-golang) for CI, CD, Kubernetes configurations, Go, Java, and Python starter applications and infrastructure.

#### Continuous integration

Organizations typically have a standard set of tasks that get applied to applications during CI. For example, in the reference implementation, the [base set of CI stages](https://github.com/GoogleCloudPlatform/software-delivery-blueprint/blob/main/app-template-golang/cloudbuild.yaml) are the following: compile code, and build a container image. Because those stages are defined in the starter repository, they're applied uniformly throughout the platform. Individual application teams can add additional steps.

#### Continuous delivery

Similar to CI, the process for CD typically has a standard set of steps for deploying applications through the dev, pre-production, and production environments. Regardless of the deployment methodologies employed, the starter repository lets platform teams uniformly apply those methodologies across applications and environments. In the reference implementation, the [deployment process](https://github.com/GoogleCloudPlatform/software-delivery-blueprint/blob/single-project-blueprint/app-template-python/skaffold.yaml) includes rollouts for dev, pre-production deployments, a production deployment across multiple clusters, and manual approvals for the production deployment using [Cloud Deploy](https://docs.cloud.google.com/deploy).

#### Application configuration

For a software delivery platform to be effective, you need a uniform and consistent way to apply application configuration. By using tools like `kustomize` and starter repositories for Kubernetes configurations, platforms can provide a consistent basis for application configuration. For example, in the reference implementation, the [ `kustomize` base configuration](https://github.com/GoogleCloudPlatform/software-delivery-blueprint/tree/main/app-template-golang/k8s/base) initializes the application environment repositories with a known-good base set of configurations. Individual application teams can then adapt the configurations to their needs.

#### Starter applications

Starter applications can help you reduce the overhead associated with adopting best practices—for example, observability and container best practices.

  * **Observability.** To efficiently operate an application and help ensure reliability, applications need to account for logging, metrics, and tracings. Starter applications help teams build in frameworks and strategies that promote observability.

  * **Container best practices.** When you build containerized applications, you should build small and clean container images. Best practices for containers include packaging a single application in an image, removing unnecessary tools from the image, and actively trying to produce small images from minimal base images.




The reference architecture provides a [basic Go app](https://github.com/GoogleCloudPlatform/software-delivery-blueprint/tree/main/app-template-golang), a [basic Java app](https://github.com/GoogleCloudPlatform/software-delivery-blueprint/tree/main/app-template-java), and a [basic Python app](https://github.com/GoogleCloudPlatform/software-delivery-blueprint/tree/main/app-template-python) as a starting point. You should add starter applications that are customized for the languages, technology stacks, and types of applications that your teams develop.

#### Infrastructure starter repositories

Infrastructure starter repositories come with the pre-written code required to create different infrastructure components. These repositories use standard templates and modules as decided by the infrastructure team.

For example, in the reference implementation, the [platform-template](https://github.com/GoogleCloudPlatform/software-delivery-blueprint/tree/main/platform-template) contains the starter code to build out a Google Cloud project, a Virtual Private Cloud, and a GKE cluster. This template is typically used by infrastructure teams to manage the infrastructure used by multiple application teams as a shared resource. Similarly, the [infra-template](https://github.com/GoogleCloudPlatform/software-delivery-blueprint/tree/main/infra-template) contains basic starter infrastructure code that an application might require, for example, a Cloud Storage or a Spanner database. This template is typically used by the application teams to manage infrastructure for their applications.

#### Shared template repositories

Shared template repositories provide standard task templates that anyone in an organization can reuse. For example, infrastructure as code modules like [Terraform modules](https://developer.hashicorp.com/terraform/language/modules) that can be used to create infrastructure resources like networks and compute.

### Application landing zones

When you use shared CI/CD, shared application configuration, and consistent policy and configuration across clusters, you can tie these capabilities together to create application landing zones.

A landing zone is a locked-down logic entity that lets developers deploy and iterate on their applications. Application landing zones use the guard rails that you put in place so that developers can operate autonomously. For each application, you create a Kubernetes namespace in each cluster of each environment (for example, for production, dev, or staging). This consistency helps operators to debug and maintain the environments over time.

The following diagram illustrates the concept of landing zones:

![The GKE cluster includes three namespaces for different environments and workloads.](https://docs.cloud.google.com/static/architecture/images/modern-cicd-gke-user-guide-application-landing-zones.svg)

### Operating model

When you operate a software delivery platform with modern CI/CD, it's important to keep the environments, infrastructure, and processes consistent and up to date. Therefore, you need to carefully plan and choose the operating model for the platform. You can choose from various models, such as clusters as a service, blueprints, or a multi-tenant infrastructure.

Because it's important to maintain a consistent infrastructure, limit sprawl, and enable teams to focus on delivering applications, we recommend that you deploy a multi-tenant infrastructure. Deploying applications on a multi-tenant infrastructure removes the need for application teams to manage infrastructure and lets operator and security teams focus on keeping the infrastructure consistent.

#### Considerations for multi-tenant infrastructure

When you build a multi-tenant software delivery platform, there are several things you might consider building into the platform:

  * **Workload isolation.** The concept of application landing zones is to provide a framework for isolating workloads. Landing zones are a combination of namespaces, network policies, and RBAC. All of these policies should be centrally managed and applied through Config Sync.

  * **Tenant usage monitoring.** To obtain cost breakdowns on individual namespaces and labels in a cluster, you can use [GKE usage metering](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering). GKE usage metering tracks information about resource requests and resource usage for a cluster's workloads, which you can further filter by namespaces and labels. When you enable GKE usage metering on the multi-tenant cluster, resource usage records are written to a [BigQuery](https://docs.cloud.google.com/bigquery/docs) table. You can export tenant-specific metrics to BigQuery datasets in the corresponding tenant project, and auditors can then analyze those metrics to determine cost breakdowns.

  * **Resource quotas.** To ensure that all tenants sharing a cluster have fair access to the cluster resources, you need to enforce [resources quotas](https://kubernetes.io/docs/concepts/policy/resource-quotas/). Create a resource quota for each namespace based on the number of Pods that each tenant deploys, and the amount of memory and CPU that each Pod requires.

  * **Multiple clusters for each environment.** To improve application and platform reliability, you should use multiple clusters for each pre-production and production environment. With multiple clusters available, you can roll out applications individually to clusters for additional levels of canary validation. Additionally, having multiple clusters eases concerns that are related to the lifecycle of cluster management and upgrades.

  * **Tenant-specific logging and monitoring.** To investigate the operations of their applications, tenants need access to logs and metrics. In a multi-tenant environment, logging and monitoring should be application-specific. For metrics and monitoring, you can use [Google Cloud Managed Service for Prometheus](https://docs.cloud.google.com/stackdriver/docs/managed-prometheus) and [Grafana](https://grafana.com/) for each namespace. For logs, you need to create a [sink](https://docs.cloud.google.com/logging/docs/export) in order to export log entries to BigQuery datasets, and then you filter the datasets by tenant namespace. Tenants can then access the exported data in BigQuery.




For more information about a multi-tenant infrastructure, see [Best practices for enterprise multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy#tenant-monitoring).

### Isolation boundaries

A software delivery platform is built and used by multiple teams which makes it important to have proper isolation boundaries among different components of the platform. Isolation boundaries help build a robust platform by providing the following traits:

  * **Decoupling responsibilities.** Each team manages the resources in their isolation boundaries without worrying about the rest. For example, the infrastructure team is only responsible to maintain GKE clusters. Operators or developers are only responsible for maintaining the CI/CD pipelines and application code.

  * **Granular access control.** If the resources are segregated by isolation boundaries, use granular access control to limit access.

  * **Reduces affected areas.** You can independently make changes to a component without affecting other components.

  * **Reduces manual errors.** Because the access control is granular, you can avoid manual errors like accidentally deploying to a production cluster from a dev environment.




These isolation boundaries could exist between different applications, infrastructure and applications, or even between an application's different environments.

### Governance

The main goal of software delivery platforms and modern CI/CD systems is to improve the efficiency of the overall software delivery process. In terms of managing the platform, you have two primary considerations: application onboarding, which generally falls under the category of governance; and ongoing development and maintenance of the platform (that is, treating the platform like a product).

#### Application onboarding and management

The goal of adopting modern CI/CD methodology and tools is to streamline the release process and the onboarding of new services. Onboarding new applications should be a straightforward process that you can perform with minimal input from operations and security teams. That doesn't mean that operations and security teams aren't involved but that their initial input from a deployment and security perspective is automatically handled through the provisioning process. Once onboarded, operations and security teams are naturally included in the release process through merge requests, policy updates, and enforcement of best practices.

It is recommended to create some automation to onboard a new application. This may include creating code repositories, CI/CD pipelines, landing zones, and any infrastructure required for the application. Automation decouples the complex dependencies of development teams on other teams in the organization and provides developers autonomy to self-service an application. This lets the developers start iterating on the application's code very quickly and not waste time in performing the tasks other than writing the code. The automation should enable developers to get the application running in a development environment. To take the application to higher environments, other teams should be involved and the review process should be followed.

In the associated [reference architecture](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture), this automation is referred to as Application Factory.

#### Platform as a product

The CI/CD workflow is a software product, except that the users of the product are development, operations, and security teams. With that in mind, the platform requires the same software development roles and processes, such as product owners, marketing (albeit internal facing), user feedback loops, and feature development cycles.

## Deploy CI/CD with GKE

As you begin to deploy modern CI/CD with GKE to the organization, choosing the best pilot applications is critical. Development, operations, and security teams also need to consider other factors as they work, which this section discusses.

### Selecting a pilot application

Choosing the first applications to move onto the platform can be a difficult first step. Good candidates for pilots are services that process data or handle requests but don't store data—for example caching layers, web frontends, or event-based processing applications. Typically, these applications are more resistant to small amounts of downtime and deployment errors that can occur any time you work with new deployment and configuration management techniques. As teams gain more experience with CI/CD and begin to experience benefits in reliability and velocity, you can begin to move core services onto the software delivery platform.

### Developer considerations

When you work in a modern CI/CD development process, features, changes, and deployments can occur both with increased frequency and more asynchronously. Development teams need to realize how changes impact downstream or dependent systems and how those changes are tested. Communication paths between development, operations, and security teams need to be fluid. It's a good practice to invest in better versioning practices both for applications and the data contracts by which the different services communicate. Along with improving communication methods and versioning, implementing features in [small pieces and utilizing feature branches and flags](https://docs.cloud.google.com/solutions/devops/devops-process-working-in-small-batches#how_to_work_in_small_batches) can improve how you test and release features.

### Operator considerations

With a software delivery platform, operations teams need to function more like development teams. Instead of building externally facing features, they're building internal tools and processes that help facilitate the development, deployment, and operation of external-facing applications. Platform tools are used by their own team as well as the development and security teams. Operators should build tools to aid in rolling out new versions of applications and also rolling them back in the case of application errors or deployment failures. Operators should also put more emphasis on building monitoring and alerting systems to [proactively detect failures and alert accordingly](https://docs.cloud.google.com/solutions/devops/devops-measurement-proactive-failure-notification).

### Security team considerations

Security teams should work to make security more of a shared responsibility between themselves and operations and development teams. This pattern is commonly called [_shifting left_](https://docs.cloud.google.com/solutions/devops/devops-tech-shifting-left-on-security) on security, in which information security (InfoSec) is involved early in the development process, developers work with pre-approved tools, and security testing is automated. In addition to those techniques, you can programmatically define and enforce security policy with Policy Controller. The combination of techniques and tools puts security enforcement in a more proactive posture.

## What's next

  * Try [implementing aspects of this modern CI/CD architecture](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/modern-cicd-gke-reference-architecture).

  * Learn more about [best practices for setting up identity federation](https://docs.cloud.google.com/solutions/migrating-consumer-accounts-to-cloud-identity-or-g-suite-best-practices-federation).

  * Read [Kubernetes and the challenges of continuous software delivery](https://docs.cloud.google.com/solutions/addressing-continuous-delivery-challenges-in-a-kubernetes-world).

  * Reading about [hybrid and multi-cloud monitoring and logging patterns](https://docs.cloud.google.com/solutions/hybrid-and-multi-cloud-monitoring-and-logging-patterns). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
