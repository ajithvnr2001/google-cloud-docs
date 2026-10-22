---
url: https://docs.cloud.google.com/architecture/migration-to-google-cloud-automated-containerized-deployments/
title: Migrate to Google Cloud: Migrate from manual deployments to automated, containerized deployments \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:34.539082+00:00
---

# Migrate to Google Cloud: Migrate from manual deployments to automated, containerized deployments  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/migration-to-google-cloud-automated-containerized-deployments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Migrate to Google Cloud: Migrate from manual deployments to automated, containerized deployments Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-08 UTC

This document helps you plan and design a migration path from manual deployments to automated, containerized deployments in Google Cloud using cloud-native tools and Google Cloud managed services.

This document is part of the following multi-part series about migrating to Google Cloud:

  * [Migrate to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started)
  * [Migrate to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads)
  * [Migrate to Google Cloud: Plan and build your foundation](https://docs.cloud.google.com/architecture/migration-to-google-cloud-building-your-foundation)
  * [Migrate to Google Cloud: Transfer your large datasets](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets)
  * [Migrate to Google Cloud: Deploy your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-deploying-your-workloads)
  * Migrate to Google Cloud: Migrate from manual deployments to automated, containerized deployments (this document)
  * [Migrate to Google Cloud: Optimize your environment](https://docs.cloud.google.com/architecture/migration-to-google-cloud-optimizing-your-environment)
  * [Migrate to Google Cloud: Best practices for validating a migration plan](https://docs.cloud.google.com/architecture/migration-to-google-cloud-best-practices)
  * [Migrate to Google Cloud: Minimize costs](https://docs.cloud.google.com/architecture/migration-to-google-cloud-minimize-costs)



This document is useful if you're planning to modernize your deployment processes, if you're migrating from manual and legacy deployment processes to automated and containerized deployments, or if you're evaluating the opportunity to migrate and want to explore what it might look like.

Before starting this migration, you should evaluate the scope of the migration and the status of your current deployment processes, and set your expectations and goals. You choose the starting point according to how you're [currently deploying your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-deploying-your-workloads):

  * You're deploying your workloads manually.
  * You're deploying your workloads with configuration management (CM) tools.



It's hard to move from manual deployments directly to fully automated and containerized deployments. Instead, we recommend the following migration steps:

  1. [Deploy by using container orchestration tools](https://docs.cloud.google.com/architecture/migration-to-gcp-deploying-your-workloads#deploy_by_using_container_orchestration_tools).
  2. [Deploy automatically](https://docs.cloud.google.com/architecture/migration-to-gcp-deploying-your-workloads#deploy_automatically).



This migration path is an ideal one, but you can stop earlier in the migration process if the benefits of moving to the next step outweigh the costs for your particular case. For example, if you don't plan to automatically deploy your workloads, you can stop after you deploy by using container orchestration tools. You can revisit this document in the future, when you're ready to continue on the journey.

When you move from one step of the migration to another, there is a transition phase where you might be using different deployment processes at the same time. In fact, you don't need to choose only one deployment option for all of your workloads. For example, you might have a hybrid environment where you deploy certain workloads using CM tools, while deploying other workloads with container orchestration tools.

For this migration to Google Cloud, we recommend that you follow the migration framework described in [Migrate to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#the_migration_path).

The following diagram illustrates the path of your migration journey.

![Migration path with four phases.](https://docs.cloud.google.com/static/architecture/images/migration-to-gcp-getting-started-migration-path.svg)

You might migrate from your source environment to Google Cloud in a series of iterations—for example, you might migrate some workloads first and others later. For each separate migration iteration, you follow the phases of the general migration framework:

  1. Assess and discover your workloads and data.
  2. Plan and build a foundation on Google Cloud.
  3. Migrate your workloads and data to Google Cloud.
  4. Optimize your Google Cloud environment.



For more information about the phases of this framework, see [Migrate to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started).

To design an effective migration plan, we recommend that you validate each step of the plan, and ensure that you have a rollback strategy. To help you validate your migration plan, see [Migrate to Google Cloud: Best practices for validating a migration plan](https://docs.cloud.google.com/architecture/migration-to-google-cloud-best-practices).

## Migrate to container orchestration tools

One of your first steps to move away from manual deployments is to deploy your workloads with container orchestration tools. In this step, you design and implement a deployment process to handle containerized workloads by using container orchestration tools, such as [Kubernetes](https://kubernetes.io/).

If your workloads aren't already [containerized](https://wikipedia.org/wiki/OS-level_virtualization), you're going to spend a significant effort containerizing them. Not all workloads are suitable for containerization. If you're deploying a workload that isn't cloud-ready or ready for containerization, it might not be worth containerizing the workloads. Some workloads can't even support containerization for technical or licensing reasons.

### Assess and discover your workloads

To scope your migration, you first need an inventory of the artifacts that you're producing and deploying along with their dependencies on other systems and artifacts. To build this inventory, you need to use the expertise of the teams that designed and implemented your current artifact production and deployment processes. The [Migrate to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads) document discusses how to assess your environment during a migration and how to [build an inventory of apps](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads#building_an_inventory_of_your_apps).

For each artifact, you need to evaluate its test coverage. You should have proper test coverage for all your artifacts before moving on to the next step. If you have to manually test and validate each artifact, you don't benefit from the automation. Adopt a methodology that highlights the importance of testing, like [test-driven development](https://wikipedia.org/wiki/Test-driven_development).

When you evaluate your processes, consider how many different versions of your artifacts you might have in production. For example, if the latest version of an artifact is several versions ahead of instances that you must support, you have to design a model that supports both versions.

Also consider the branching strategy that you use to manage your codebase. A branching strategy is only part of a collaboration model that you need to evaluate, and you need to assess the broader collaboration processes inside and outside your teams. For example, if you adopt a flexible branching strategy but don't adapt it to the communication process, the efficiency of those teams might be reduced.

In this assessment phase, you also determine how you can make the artifacts you're producing more efficient and suitable for containerization than your current deployment processes. One way to improve efficiency is to assess the following:

  * Common parts: Assess what your artifacts have in common. For example, if you have common libraries and other runtime dependencies, consider consolidating them in one runtime environment.
  * Runtime environment requirements: Assess whether you can streamline the runtime environments to reduce their variance. For example, if you're using different runtime environments to run all your workloads, consider starting from a common base to reduce the maintenance burden.
  * Unnecessary components: Assess whether your artifacts contain unnecessary parts. For example, you might have utility tools, such as debugging and troubleshooting tools, that are not strictly needed.
  * Configuration and secret injection: Assess how you're configuring your artifacts according to the requirements of your runtime environment. For example, your current configuration injection system might not support a containerized environment.
  * Security requirements: Assess whether your container security model meets your requirements. For example, the security model of a containerized environment might clash with the requirement of a workload to have super user privileges, direct access to system resources, or sole tenancy.
  * Deployment logic requirements: Assess whether you need to implement advanced deployment processes. For example, if you need to implement a [canary deployment process](https://docs.cloud.google.com/deploy/docs/deployment-strategies/canary), you could determine whether the container orchestration tool supports that.



### Plan and build a foundation

In the plan and build phase, you provision and configure the infrastructure to do the following:

  * Support your workloads in your Google Cloud environment.
  * Connect your source environment and your Google Cloud environment to complete the migration.



The plan and build phase is composed of the following tasks:

  1. Build a resource hierarchy.
  2. Configure Google Cloud's Identity and Access Management (IAM).
  3. Set up billing.
  4. Set up network connectivity.
  5. Harden your security.
  6. Set up logging, monitoring, and alerting.



For more information about each of these tasks, see the [Migrate to Google Cloud: Plan and build your foundation](https://docs.cloud.google.com/architecture/migration-to-google-cloud-building-your-foundation).

To achieve the necessary flexibility to manage your Google Cloud resources, we recommend that you design a [Google Cloud resource hierarchy](https://docs.cloud.google.com/architecture/migration-to-google-cloud-building-your-foundation#resource_hierarchy) that supports multiple environments such as for development, testing, and production workloads.

When you're establishing user and service identities, for the best isolation you need at least a service account for each deployment process step. For example, if your process executes steps to produce the artifact and to manage the storage of that artifact in a repository, you need at least two service accounts. If you want to provision and configure development and testing environments for your deployment processes, you might need to create more service accounts. If you have a distinct set of service accounts per environment, you make the environments independent from each other. Although this configuration increases the complexity of your infrastructure and puts more burden on your operations team, it gives you the flexibility to independently test and validate each change to the deployment processes.

You also need to provision and configure the services and infrastructure to support your containerized workloads:

  * Set up a registry to store your container images, like [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) and to isolate this registry and the related maintenance tasks, you set it up in a dedicated Google Cloud project.
  * Provision and configure the Kubernetes clusters you need to support your workloads. Depending on your current environment and your goals, you can use services like [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine/docs).
  * Provision and configure persistent storage for your [stateful workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps). For more information, see [Google Kubernetes Engine storage overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/storage-overview).



By using container orchestration tools, you don't have to worry about provisioning your infrastructure when you deploy new workloads. For example, you can use [Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) to automatically manage your GKE cluster configuration.

### Deploy your artifacts with container orchestration tools

Based on the requirements you gathered in the assessment phase and the foundation phase of this step, you do the following:

  * Containerize your workloads.
  * Implement deployment processes to handle your containerized workloads.



Containerizing your workloads is a nontrivial task. What follows is a generalized list of activities you need to adapt and extend to containerize your workloads. Your goal is to cover your own needs, such as networking and traffic management, persistent storage, secret and configuration injection, and fault tolerance requirements. This document covers two activities: building a set of container images to use as a base, and building a set of container images for your workloads.

First, you automate the artifact production, so you don't have to manually produce a new image for each new deployment. The artifact building process should be automatically triggered each time the source code is modified so that you have immediate feedback about each change.

You execute the following steps to produce each image:

  1. Build the image.
  2. Run the test suite.
  3. Store the image in a registry.



For example, you can use [Cloud Build](https://docs.cloud.google.com/build) to build your artifacts, run the test suites against them, and, if the tests are successful, store the results in Artifact Registry.

You also need to establish rules and conventions for identifying your artifacts. When producing your images, label each one to make each execution of your processes repeatable. For example, a popular convention is to identify releases by using [semantic versioning](https://semver.org/) where you tag your container images when producing a release. When you produce images that still need work before release, you can use an identifier that ties them to the point in the codebase from which your process produced them. For example, if you're using [Git](https://git-scm.com/) repositories, you can use the [commit hash](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects) as an identifier for the corresponding container image that you produced when you pushed a commit to the main branch of your repository.

During the assessment phase of this step, you gathered information about your artifacts, their common parts, and their runtime requirements. With this information, you can design and build a set of base container images and another set of images for your workloads. You use the base images as a starting point to build the images for your workloads. The set of base images should be tightly controlled and supported to avoid proliferating unsupported runtime environments.

When producing container images from base images, remember to extend your test suites to cover the images, not only the workloads inside each image. You can use tools like [InSpec](https://www.inspec.io/) to run compliance test suites against your runtime environments.

When you finish containerizing your workloads and implementing processes to automatically produce such container images, you implement the deployment processes to use container orchestration tools. In the assessment phase, you use the information about the deployment logic requirements that you gathered to design rich deployment processes. By using container orchestration tools, you can focus on composing the deployment logic using the provided mechanisms, instead of having to manually implement them. For example, you can use [Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview) to implement your deployment processes.

When designing and implementing your deployment processes, consider how to inject configuration files and secrets in your workloads, and how to manage data for stateful workloads. Configuration files and secret injection are instrumental to produce immutable artifacts. By deploying immutable artifacts, you can do the following:

  * For example, you can deploy your artifacts in your development environment. Then, after testing and validating them, you move them to your quality assurance environment. Finally, you move them to the production environment.
  * You lower the chances of issues in your production environments because the same artifact went through multiple testing and validation activities.



If your workloads are stateful, we suggest you provision and configure the necessary persistent storage for your data. On Google Cloud, you have different options:

  * [Persistent disks managed with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/stateful-apps)
  * Fully managed database services like [Cloud SQL](https://docs.cloud.google.com/sql), [Firestore](https://docs.cloud.google.com/firestore) and [Spanner](https://docs.cloud.google.com/spanner)
  * File storage services like [Filestore](https://docs.cloud.google.com/filestore)
  * Object store services like [Cloud Storage](https://docs.cloud.google.com/storage)



### Optimize your environment

After implementing your deployment process, you can use container orchestration tools to start optimizing the deployment processes. For more information, see [Migrate to Google Cloud: Optimize your environment](https://docs.cloud.google.com/architecture/migration-to-google-cloud-optimizing-your-environment).

The requirements of this optimization iteration are the following:

  * Extend your monitoring system as needed.
  * Extend the test coverage.
  * Increase the security of your environment.



You extend your monitoring system to cover your new artifact production, your deployment processes, and all of your new runtime environments.

If you want to effectively monitor, automate, and codify your processes as much as possible, we recommend that you increase the coverage of your tests. In the assessment phase, you ensured that you had at least minimum end-to-end test coverage. During the optimization phase, you can expand your test suites to cover more use cases.

Finally, if you want to increase the security of your environments, you can configure [binary authorization](https://docs.cloud.google.com/binary-authorization) to allow only a set of signed images to be deployed in your clusters. You can also enable [Artifact Analysis](https://docs.cloud.google.com/artifact-registry/docs/analysis) to scan container images stored in Artifact Registry for vulnerabilities.

## Migrate to deployment automation

After migrating to container orchestration tools, you can move to full deployment automation, and you can extend the artifact production and deployment processes to automatically deploy your workloads.

### Assess and discover your workloads

Building on the previous evaluation, you can now focus on the requirements of your deployment processes:

  * Manual approval steps: Assess whether you need to support any manual steps in your deployment processes.
  * Deployment-per-time units: Assess how many deployments-per-time units you need to support.
  * Factors that cause a new deployment: Assess which external systems interact with your deployment processes.



If you need to support manual deployment steps, it doesn't mean that your process cannot be automated. In this case, you automate each step of the process, and place the manual approval gates where appropriate.

Supporting multiple deployments per day or per hour is more complex than supporting a few deployments per month or per year. However, if you don't deploy often, your agility and your ability to react to issues and to ship new features in your workloads might be reduced. For this reason, before designing and implementing a fully automated deployment process, it's a good idea to set your expectations and goals.

Also evaluate which factors trigger a new deployment in your runtime environments. For example, you might deploy each new release in your development environment, but deploy the release in your quality assurance environment only if it meets certain quality criteria.

### Plan and build a foundation

To extend the foundation that you built in the previous step, you provision and configure services to support your automated deployment processes.

For each of your runtime environments, set up the necessary infrastructure to support your deployment processes. For example, if you provision and configure your deployment processes in your development, quality assurance, pre-production, and production environments, you have the freedom and flexibility to test changes to your processes. However, if you use a single infrastructure to deploy your runtime environments, your environments are simpler to manage, but less flexible when you need to change your processes.

When provisioning the service accounts and roles, consider isolating your environments and your workloads from each other by creating dedicated service accounts that don't share responsibilities. For example, don't reuse the same service accounts for your different runtime environments.

### Deploy your artifacts with fully automated processes

In this phase, you configure your deployment processes to deploy your artifacts with no manual interventions, other than approval steps.

You can use tools like [Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview) to implement your automated deployment processes, according to the requirements you gathered in the assessment phase of this migration step.

For any given artifact, each deployment process should execute the following tasks:

  1. Deploy the artifact in the target runtime environment.
  2. Inject the configuration files and secrets in the deployed artifact.
  3. Run the compliance test suite against the newly deployed artifact.
  4. Promote the artifact to the production environment.



Make sure that your deployment processes provide interfaces to trigger new deployments according to your requirements.

Code review is a necessary step when implementing automated deployment processes, because of the short feedback loop that's part of these processes by design. For example, if you deploy changes to your production environment without any review, you impact the stability and reliability of your production environment. An unreviewed, malformed, or malicious change might cause a service outage.

### Optimize your environment

After automating your deployment processes, you can run another optimization iteration. The requirements of this iteration are the following:

  * Extend your monitoring system to cover the infrastructure supporting your automated deployment processes.
  * Implement more advanced deployment patterns.
  * Implement a [_break glass_ process](https://en.wikipedia.org/wiki/Computer_access_control#Break-Glass_Access_Control_Models).



An effective monitoring system lets you plan further optimizations for your environment. When you measure the behavior of your environment, you can find any bottlenecks that are hindering your performance or other issues, like unauthorized or accidental accesses and exploits. For example, you configure your environment so that you receive alerts when the consumption of certain resources reaches a threshold.

When you're able to efficiently orchestrate containers, you can implement advanced deployment patterns depending on your needs. For example, you can implement [blue/green deployments](https://martinfowler.com/bliki/BlueGreenDeployment.html) to increase the reliability of your environment and reduce the impact of any issue for your users.

## What's next

  * [Optimize your environment](https://docs.cloud.google.com/architecture/migration-to-google-cloud-optimizing-your-environment).
  * Learn where to [find help for your migrations](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#finding_help).
  * Take the [Google Skills training course on migrating to Google Cloud](https://www.skills.google/course_templates/1561).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-08 UTC."],[],[]] 
