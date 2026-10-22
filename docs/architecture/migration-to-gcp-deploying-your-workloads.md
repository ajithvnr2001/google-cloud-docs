---
url: https://docs.cloud.google.com/architecture/migration-to-gcp-deploying-your-workloads/
title: Migrate to Google Cloud: Deploy your workloads \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:35.346141+00:00
---

# Migrate to Google Cloud: Deploy your workloads  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/migration-to-gcp-deploying-your-workloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Migrate to Google Cloud: Deploy your workloads Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-08 UTC

This document can help you plan and design the deployment phase of your migration to Google Cloud. After you've assessed your current environment, planned the migration to Google Cloud, and built your Google Cloud foundation, you can deploy your workloads.

This document is part of the following multi-part series about migrating to Google Cloud:

  * [Migrate to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started)
  * [Migrate to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads)
  * [Migrate to Google Cloud: Plan and build your foundation](https://docs.cloud.google.com/architecture/migration-to-google-cloud-building-your-foundation)
  * [Migrate to Google Cloud: Transfer your large datasets](https://docs.cloud.google.com/architecture/migration-to-google-cloud-transferring-your-large-datasets)
  * Migrate to Google Cloud: Deploy your workloads (this document)
  * [Migrate to Google Cloud: Migrate from manual deployments to automated, containerized deployments](https://docs.cloud.google.com/architecture/migration-to-google-cloud-automated-containerized-deployments)
  * [Migrate to Google Cloud: Optimize your environment](https://docs.cloud.google.com/architecture/migration-to-google-cloud-optimizing-your-environment)
  * [Migrate to Google Cloud: Best practices for validating a migration plan](https://docs.cloud.google.com/architecture/migration-to-google-cloud-best-practices)
  * [Migrate to Google Cloud: Minimize costs](https://docs.cloud.google.com/architecture/migration-to-google-cloud-minimize-costs)



The following diagram illustrates the path of your migration journey.

![Migration path with four phases.](https://docs.cloud.google.com/static/architecture/images/migration-to-gcp-getting-started-migration-path.svg)

The deployment phase is the third phase in your migration to Google Cloud where you design a deployment process for your workloads.

This document is useful if you're planning a migration from an on-premises environment, from a private-hosting environment, from another cloud provider to Google Cloud, or if you're evaluating the opportunity to migrate and want to explore what it might look like.

In this document, you review the different deployment process types, in order of flexibility, automation, and complexity, along with criteria on how to pick an approach that's right for you:

  1. Deploy manually.
  2. Deploy with configuration management (CM) tools.
  3. Deploy by using container orchestration tools.
  4. Deploy automatically.



Before you deploy your workloads, plan and design your deployment phase. First, you should evaluate the different deployment process types that you implement for your workloads. When you evaluate deployment process types, you can decide to start with a targeted process and move to a more complex one in the future. This approach can lead to quicker results, but can also introduce friction when you move to a more advanced process, because you have to absorb the technical debt you accumulated while using the targeted process. For example, if you move from fully manual deployments to an automated solution, you might have to manage upgrades to your deployment pipeline and apps.

While it's possible to implement different types of deployment processes according to your workloads' needs, this approach can also increase the complexity of this phase. If you implement different types of deployment processes, you can benefit from the added flexibility, but you might need expertise, tooling, and resources tailored to each process, which translates to more effort on your side.

## Deploy manually

A fully manual deployment is backed by a provisioning, configuration, and deployment process that is completely non-automated. While there might be specifications and checklists for each step of the process, there is no automated check or enforcement of those specifications. A manual process is prone to human error, not repeatable, and its performance is limited by the human factor.

Fully manual deployment processes can be useful, for example, when you need to quickly instrument an experiment in a sandboxed environment. Setting up a structured, automated process for an experiment that lasts minutes can unnecessarily slow down your pace, especially in the early stages of your migration, when you might lack the necessary expertise in the tools and practices that let you build an automated process.

While this limitation isn't the case with Google Cloud, fully manual deployments might be your only option when dealing with bare metal environments that lack the necessary management APIs. In this case, you cannot implement an automated process due to the lack of the necessary interfaces. If you have a legacy virtualized infrastructure that doesn't support any automation, you might be forced to implement a fully manual process

We recommend that you avoid a fully manual deployment unless you have no other option.

You can implement a fully manual provisioning, configuration, and deployment process by using tools, such as [Google Cloud console](https://console.cloud.google.com/), [Cloud Shell](https://docs.cloud.google.com/shell), [Cloud APIs](https://docs.cloud.google.com/apis), and [Google Cloud CLI](https://docs.cloud.google.com/sdk).

## Deploy with configuration management tools

CM tools let you configure an environment in a repeatable and controlled way. These tools include a set of plugins and modules that already implement common configuration operations. These tools let you focus on the end state that you want to achieve for your environment, rather than implementing the logic to reach that end state. If the included operations set isn't enough, CM tools often feature an extension system that you can use to develop your own modules. While these extensions are possible, try to use the predefined modules and plugins where applicable, to avoid extra development and maintenance burden.

You use CM tools when you need to configure environments. You can also use them to provision your infrastructure and to implement a deployment process for your workloads. CM tools are a better process compared to a fully manual provisioning, configuration, and deployment process because it's repeatable, controlled, and auditable. However, there are several downsides, because CM tools aren't designed for provisioning or deployment tasks. They usually lack built-in features to implement elaborate provisioning logic, such as detecting and managing differences between the real-world state of your infrastructure and the wanted state, or rich deployment processes, such as deployments with no downtime or [blue-green deployments](https://martinfowler.com/bliki/BlueGreenDeployment.html). You can implement the missing features using the previously mentioned extension points. These extensions can result in extra effort and can increase the overall complexity of the deployment process, because you need the necessary expertise to design, develop, and maintain a customized deployment solution.

You can implement this type of provisioning, configuration, and deployment process by using tools such as [Ansible](https://www.ansible.com/), [Chef](https://www.chef.io/), [Puppet](https://puppet.com/), and [SaltStack](https://www.saltstack.com/).

A basic deployment process that uses CM tools can prepare runtime environments and deploy workloads in those environments. For example, your process might create a Compute Engine instance, install the required software, and deploy your workloads. It takes time to configure a runtime environment that supports your workloads. To reduce the amount of time needed to configure a runtime environment, you can implement a process that runs CM tools to produce a template, such as an operating system (OS) image. You can use this template to create instances of your runtime environment that are ready for your workloads. For example, you can use [Cloud Build to build Compute Engine images](https://docs.cloud.google.com/build/docs/building/build-vm-images-with-packer). These images are often called _golden images_ or _silver images_ , both of which are immutable templates, such as OS images, that you create for your runtime environments. The difference between the two depends on the amount of work a deployment process must complete before the images can run a workload:

  * **Golden image** : A template that you create for your runtime environments or prepare from a base template. Golden images include all data and configuration information that your runtime environments need to accomplish their assigned tasks. You can prepare several types of golden images to accomplish different tasks. Synonyms for golden image types include _flavors_ , _spins_ , and _archetypes_.
  * **Silver image** : A template that you create for your runtime environments by applying minimal changes to a golden image or a base template. Runtime environments running a silver image complete their provisioning and configuration upon the first boot, according to the needs of the use cases that those runtime environments must support.



## Deploy by using container orchestration tools

If you already invested, or plan to invest in the containerization of your workloads, you can use a container orchestration tool to deploy your workloads.

A container orchestration tool takes care of managing the infrastructure underpinning your environment, and supports a wide range of deployment operations and building blocks to implement your deployment logic that you can use when the built-in ones aren't enough. By using these tools, you can focus on composing the actual deployment logic using the provided mechanisms, instead of having to implement them.

Container orchestration tools also provide abstractions that you can use to generalize your deployment processes to different underlying environments, so you don't have to design and implement multiple processes for each of your environments. For example, these tools usually include the logic for scaling and upgrading your deployments, so you don't have to implement them by yourself. You can even start leveraging these tools to implement your deployment processes in your current environment, and you can then port them to the target environment, because the implementation is largely the same, by design. By adopting these tools early, you gain the experience in administering containerized environments, and this experience is useful for your migration to Google Cloud.

You use a container orchestration tool if your workloads are already containerized or if you can containerize them in the future and you plan to invest in this effort. In the latter case, you should run a thorough analysis of each workload to determine the following:

  * Ensure that a containerization of the workload is possible.
  * Assess the potential benefits that you could gain by containerizing the workload.



If the potential pitfalls outweigh the benefits of containerization, you should only use a container orchestration tool if your teams are already committed to using them and if you don't want to manage heterogeneous environments.

For example, data warehouse solutions aren't typically deployed using container orchestration tools, because they aren't designed to run in ephemeral containers.

You can implement this deployment process using [Google Kubernetes Engine (GKE)](https://docs.cloud.google.com/kubernetes-engine) on Google Cloud. If you're interested in a serverless environment, you can use tools, such as [Cloud Run](https://docs.cloud.google.com/run).

## Deploy automatically

Regardless of the provisioning, configuration, deployment, and orchestration tools you use in your environment, you can implement fully automated deployment processes to minimize human errors and to consolidate, streamline, and standardize the processes across your organization. You can also insert manual approval steps in the deployment process if needed, but every step is automated.

The steps of a typical end-to-end deployment pipeline are as follows:

  1. Code review.
  2. Continuous integration (CI).
  3. Artifact production.
  4. Continuous deployment (CD), with eventual manual approvals.



You can automate each of those steps independently from the others, so you can gradually migrate your current deployment processes towards an automated solution, or you can implement a new process directly in the target environment. For this process to be effective, you need testing and validation procedures in each step of the pipeline, not just during the code review step or the CI step.

For each change in your codebase, you should perform a thorough review to assess the quality of the change. Most source code management tools have a top-level support for code reviews. They also often support the automatic creation and initialization of reviews by looking at the source code area that was modified, provided that you configured the teams responsible for each area of your codebase. In each review you can also run automated checks on the source code, such as [linters](https://en.wikipedia.org/wiki/Lint_\(software\)) and [static analyzers](https://en.wikipedia.org/wiki/Static_program_analysis) to enforce consistency and quality standards across the codebase.

After you review and integrate a change in the codebase, the CI tool can automatically run tests, evaluate the results, and then notify you about any issues with the current build. You can add value to this step by following a [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development) process for a complete test coverage of the features of each workload.

For each successful build, you can automate the creation of deployment artifacts. Such artifacts represent a ready-to-deploy version of your workloads, with the latest changes. As part of the artifact creation step, you can also perform an automated validation of the artifact itself. For example, you run a vulnerability scan against known issues and approve the artifact for deployment only if no vulnerabilities are found. For example, you can use [Artifact Registry to scan your artifacts for known vulnerabilities](https://docs.cloud.google.com/artifact-registry/docs/analysis).

Finally, you can automate the deployment of each approved artifact in the target environment. If you have multiple runtime environments, you can also implement unique deployment logic for each one, even adding manual approval steps, if needed. For example, you can automatically deploy new versions of your workloads in your development, quality assurance, and pre-production environments, while still requiring a manual review and approval from your production control team to deploy in your production environment.

While a fully automated end-to-end process is one of your best options if you need an automated, structured, streamlined, and auditable process, implementing this process isn't a trivial task. Before choosing this kind of process, you should have a clear view on the expected benefits, the costs involved, and if your current level of team knowledge and expertise is sufficient to implement a fully automated deployment process.

You can implement fully automated deployment processes with [Cloud Deploy](https://docs.cloud.google.com/deploy).

## What's next

  * Learn how to [migrate your deployment processes](https://docs.cloud.google.com/architecture/migration-to-google-cloud-automated-containerized-deployments).
  * Learn where to [find help for your migrations](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#finding_help).
  * Take the [Google Skills training course on migrating to Google Cloud](https://www.skills.google/course_templates/1561).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-08 UTC."],[],[]] 
