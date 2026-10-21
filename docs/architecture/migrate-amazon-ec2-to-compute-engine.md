---
url: https://docs.cloud.google.com/architecture/migrate-amazon-ec2-to-compute-engine/
title: Migrate from AWS to Google Cloud: Migrate from Amazon EC2 to Compute Engine \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:08.284143+00:00
---

# Migrate from AWS to Google Cloud: Migrate from Amazon EC2 to Compute Engine  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/migrate-amazon-ec2-to-compute-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Migrate from AWS to Google Cloud: Migrate from Amazon EC2 to Compute Engine Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2026-01-05 UTC

Google Cloud provides tools, products, guidance, and professional services to migrate virtual machines (VMs) along with their data from Amazon Elastic Compute Cloud (Amazon EC2) to [Compute Engine](https://docs.cloud.google.com/compute). This document discusses how to design, implement, and validate a plan to migrate from Amazon EC2 to Compute Engine.

The discussion in this document is intended for cloud administrators who want details about how to plan and implement a migration process. It's also intended for decision-makers who are evaluating the opportunity to migrate and who want to explore what migration might look like.

This document is part of a multi-part series about migrating from AWS to Google Cloud that includes the following documents:

  * [Get started](https://docs.cloud.google.com/architecture/migration-from-aws-get-started)
  * Migrate from Amazon EC2 to Compute Engine (this document)
  * [Migrate from Amazon S3 to Cloud Storage](https://docs.cloud.google.com/architecture/migrate-amazon-s3-to-cloud-storage)
  * [Migrate from Amazon EKS to Google Kubernetes Engine](https://docs.cloud.google.com/architecture/migrate-amazon-eks-to-gke)
  * [Migrate from Amazon RDS and Amazon Aurora for MySQL to Cloud SQL for MySQL](https://docs.cloud.google.com/architecture/migrate-aws-rds-to-sql-mysql)
  * [Migrate from Amazon RDS and Amazon Aurora for PostgreSQL to Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL](https://docs.cloud.google.com/architecture/migrate-aws-rds-aurora-to-postgresql)
  * [Migrate from Amazon RDS for SQL Server to Cloud SQL for SQL Server](https://docs.cloud.google.com/architecture/migrate-aws-rds-to-cloudsql-for-sqlserver)
  * [Migrate from AWS Lambda to Cloud Run](https://docs.cloud.google.com/architecture/migrate-aws-lambda-to-cloudrun)



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

## Assess the source environment

In the assessment phase, you determine the requirements and dependencies to migrate your source environment to Google Cloud.

The assessment phase is crucial for the success of your migration. You need to gain deep knowledge about the workloads you want to migrate, their requirements, their dependencies, and about your current environment. You need to understand your starting point to successfully plan and execute a Google Cloud migration.

The assessment phase consists of the following tasks:

  1. Build a comprehensive inventory of your workloads.
  2. Catalog your workloads according to their properties and dependencies.
  3. Train and educate your teams on Google Cloud.
  4. Build experiments and proofs of concept on Google Cloud.
  5. Calculate the total cost of ownership (TCO) of the target environment.
  6. Choose the migration strategy for your workloads.
  7. Choose your migration tools.
  8. Define the migration plan and timeline.
  9. Validate your migration plan.



For more information about the assessment phase and these tasks, see [Migrate to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-assessing-and-discovering-your-workloads). The following sections are based on information in that document.

### Build an inventory of your Amazon EC2 instances

To scope your migration, you create an inventory of your Amazon EC2 instances. You can then use the inventory to assess your deployment and operational processes for deploying workloads on those instances.

To build the inventory of your Amazon EC2 instances, we recommend that you use [Migration Center](https://docs.cloud.google.com/migration-center/docs/migration-center-overview), Google Cloud's unified platform that helps you accelerate your end-to-end cloud journey from your current environment to Google Cloud. Migration Center lets you [run an inventory discovery on AWS](https://docs.cloud.google.com/migration-center/docs/run-inventory-discovery).

The data that Migration Center and the Migration Center discovery client CLI provide might not fully capture the dimensions that you're interested in. In that case, you can integrate that data with the results from other data-collection mechanisms that you create that are based on AWS APIs, AWS developer tools, and the AWS command-line interface.

In addition to the data that you get from Migration Center and the Migration Center discovery client CLI, consider the following data points for each Amazon EC2 instance that you want to migrate:

  * Deployment region and zone.
  * Instance type and size.
  * The Amazon Machine Image (AMI) that the instance is launching from.
  * The instance hostname, and how other instances and workloads use this hostname to communicate with the instance.
  * The instance tags as well as metadata and user data.
  * The instance virtualization type.
  * The instance purchase option, such as on-demand purchase or spot purchase.
  * How the instance stores data, such as using instance stores and Amazon EBS volumes.
  * The instance tenancy configuration.
  * Whether the instance is in a specific placement group.
  * Whether the instance is in a specific autoscaling group.
  * The security groups that the instance belongs to.
  * Any AWS Network Firewall configuration that involves the instance.
  * Whether the workloads that run on the instance are protected by AWS Shield and AWS WAF.
  * Whether you're controlling the processor state of your instance, and how the workloads that run on the instance depend on the processor state.
  * The configuration of the instance I/O scheduler.
  * How you're exposing workloads that run on the instance to clients that run in your AWS environment (such as other workloads) and to external clients.



For more information about collecting these data points, see [Create an inventory of your EC2 instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-data-inventory.html).

To accelerate your assessment, you can use [Gemini CLI](https://geminicli.com/) to assess your inventory. For example, you can add the inventory files that list the Amazon EC2 instances to the Gemini CLI context and then prompt Gemini to help you assess those instances. For more information, see [Gemini-powered migrations to Google Cloud](https://googlecloudplatform.github.io/cloud-solutions/gemini-powered-migrations-to-google-cloud/).

### Assess your deployment and operational processes

It's important to have a clear understanding of how your deployment and operational processes work. These processes are a fundamental part of the practices that prepare and maintain your production environment and the workloads that run there.

Your deployment and operational processes might build the artifacts that your workloads need to function. Therefore, you should gather information about each artifact type. For example, an artifact can be an operating system package, an application deployment package, an operating system image, a container image, or something else.

In addition to the artifact type, consider how you complete the following tasks:

  * **Develop your workloads**. Assess the processes that development teams have in place to build your workloads. For example, how are your development teams designing, coding, and testing your workloads?
  * **Generate the artifacts that you deploy in your source environment**. To deploy your workloads in your source environment, you might be generating deployable artifacts, such as container images or operating system images, or you might be customizing existing artifacts, such as third-party operating system images by installing and configuring software. Gathering information about how you're generating these artifacts helps you to ensure that the generated artifacts are suitable for deployment in Google Cloud.
  * **Store the artifacts**. If you produce artifacts that you store in an artifact registry in your source environment, you need to make the artifacts available in your Google Cloud environment. You can do so by employing strategies like the following:

    * **Establish a communication channel between the environments** : Make the artifacts in your source environment reachable from the target Google Cloud environment.
    * **Refactor the artifact build process** : Complete a minor refactor of your source environment so that you can store artifacts in both the source environment and the target environment. This approach supports your migration by building infrastructure like an artifact repository before you have to implement artifact build processes in the target Google Cloud environment. You can implement this approach directly, or you can build on the previous approach of establishing a communication channel first.

Having artifacts available in both the source and target environments lets you focus on the migration without having to implement artifact build processes in the target Google Cloud environment as part of the migration.

  * **Scan and sign code**. As part of your artifact build processes, you might be using code scanning to help you guard against common vulnerabilities and unintended network exposure, and code signing to help you ensure that only trusted code runs in your environments.

  * **Deploy artifacts in your source environment**. After you generate deployable artifacts, you might be deploying them in your source environment. We recommend that you assess each deployment process. The assessment helps ensure that your deployment processes are compatible with Google Cloud. It also helps you to understand the effort that will be necessary to eventually refactor the processes. For example, if your deployment processes work with your source environment only, you might need to refactor them to target your Google Cloud environment.

  * **Inject runtime configuration**. You might be injecting runtime configuration for specific clusters, runtime environments, or workload deployments. The configuration might initialize environment variables and other configuration values such as secrets, credentials, and keys. To help ensure that your runtime configuration injection processes work on Google Cloud, we recommend that you assess how you're configuring the workloads that run in your source environment.

  * **Logging, monitoring, and profiling**. Assess the logging, monitoring, and profiling processes that you have in place to monitor the health of your source environment, the metrics of interest, and how you're consuming data provided by these processes.

  * **Authentication**. Assess how you're authenticating against your source environment.

  * **Provision and configure your resources**. To prepare your source environment, you might have designed and implemented processes that provision and configure resources. For example, you might be using [Terraform](https://www.terraform.io/) along with configuration management tools to provision and configure resources in your source environment. If you're using Terraform, you can build your foundations and landing zone on Google Cloud by using the following tools, depending on your preferred starting point:

    * [Resources in the Google Cloud Terraform Provider](https://docs.cloud.google.com/docs/terraform/create-vm-instance): Start from scratch using base building blocks.
    * [Terraform blueprints and modules for Google Cloud](https://docs.cloud.google.com/docs/terraform/blueprints/terraform-blueprints): Start from a baseline of opinionated Terraform modules. This approach builds on top of resources in the Google Cloud Terraform Provider.
    * [Enterprise Foundations Blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations): Start from an opinionated foundation and landing zones. This approach builds on top of Terraform blueprints and modules for Google Cloud.
    * [Cloud Foundation Fabric](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric): Start from an opinionated foundation and landing zones. Cloud Foundation Fabric is a standalone implementation that uses its own Terraform modules. This approach builds on top of resources in the Google Cloud Terraform Provider.



## Plan and build your foundation

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

## Migrate your workloads

To migrate your workloads from Amazon EC2 to Compute Engine, you do the following:

  1. Migrate VMs from Amazon EC2 to Compute Engine.
  2. Migrate your VM disks to Persistent Disk.
  3. Expose workloads that run on Compute Engine to clients.
  4. Refactor deployment and operational processes to target Google Cloud instead of targeting Amazon EC2.



The following sections provide details about each of these tasks.

### Migrate your VMs to Compute Engine

To migrate VMs from Amazon EC2 to Compute Engine, we recommend that you use [Migrate to Virtual Machines](https://docs.cloud.google.com/migrate/virtual-machines/docs), which is a fully managed service. For more information, see [Migration journey with Migrate to VMs](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/discover/migrating-vms-migrate-for-compute-engine-getting-started).

As part of the migration, Migrate for VMs migrates Amazon EC2 instances in their current state, apart from [required configuration changes](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/resources/vm-adaptations). If your Amazon EC2 instances run customized Amazon EC2 AMIs, Migrate for VMs migrates these customizations to Compute Engine instances. However, if you want to make your infrastructure reproducible, you might need to apply equivalent customizations by building [Compute Engine operating system images](https://docs.cloud.google.com/compute/docs/images) as part of your deployment and operational processes, as explained later in this document.

### Migrate your VM disks to Persistent Disk

You can also use Migrate to VMs to migrate disks from your source Amazon EC2 VMs to Persistent Disk, with minimal interruptions to the workloads that are running on the Amazon EC2 VMs. For more information, see [Migrate VM disks and attach them to a new VM](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/migrate/migrating-disks).

For example, you can migrate a data disk attached to an Amazon EC2 VM to Persistent Disk, and attach it to a new Compute Engine VM.

### Expose workloads that run on Compute Engine

After you migrate your Amazon EC2 instances to Compute Engine instances, you might need to provision and configure your Google Cloud environment to expose the workloads to clients.

Google Cloud offers secure and reliable services and products for exposing your workloads to clients. For workloads that run on your Compute Engine instances, you configure resources for the following categories:

  * Firewalls
  * Traffic load balancing
  * DNS names, zones, and records
  * [DDoS](https://en.wikipedia.org/wiki/Denial-of-service_attack#Distributed_DoS) protection and web application firewalls



For each of these categories, you can start by implementing a baseline configuration that's similar to how you configured AWS services and resources in the equivalent category. You can then iterate on the configuration and use additional features that are provided by Google Cloud services.

The following sections explain how to provision and configure Google Cloud resources in these categories, and how they map to AWS resources in similar categories.

#### Firewalls

If you configured AWS security groups and AWS Network Firewall policies and rules, you can configure [Cloud Next Generation Firewall policies and rules](https://docs.cloud.google.com/vpc/docs/about-firewalls). You can also provision [VPC Service Controls rules](https://docs.cloud.google.com/vpc-service-controls/docs/overview) to regulate network traffic inside your VPC. You can use VPC Service Controls to control outgoing traffic from your Compute Engine instances, and to help mitigate the risk of data exfiltration.

For example, if you use AWS security groups to allow or deny connections to your Amazon EC2 instances, you can configure similar [Virtual Private Cloud (VPC) firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) that apply to your Compute Engine instances.

If you use remote access protocols like SSH or RDP to connect to your Amazon EC2 VMs, you can remove the VM's public IP address and connect to the VM remotely with [Identity-Aware Proxy (IAP)](https://docs.cloud.google.com/iap/docs/concepts-overview). IAP TCP forwarding lets you establish an encrypted tunnel. You can use the tunnel to forward SSH, RDP, and other internet traffic to VMs without assigning your VMs public IP addresses. Because connections from the IAP service originate from a reserved public IP address range, you need to create matching VPC firewall rules. If you have Windows-based VMs and you turned on Windows Firewall, verify that the Windows Firewall isn't configured to block RDP connections from IAP. For more information, see [Troubleshooting RDP](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-rdp).

#### Traffic load balancing

If you've configured Elastic Load Balancing (ELB) in your AWS environment, you can configure [Cloud Load Balancing](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview) to distribute network traffic to help improve the scalability of your workloads in Google Cloud. Cloud Load Balancing supports several global and regional [load balancing products](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview#summary-of-google-cloud-load-balancers) that work at different layers of the [OSI model](https://en.wikipedia.org/wiki/OSI_model), such as at the transport layer and at the application layer. You can [choose a load balancing product](https://docs.cloud.google.com/load-balancing/docs/choosing-load-balancer) that's suitable for the requirements of your workloads.

Cloud Load Balancing also supports [configuring Transport Layer Security (TLS) to encrypt network traffic](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates). When you configure TLS for Cloud Load Balancing, you can use [self-managed or Google-managed TLS certificates](https://docs.cloud.google.com/load-balancing/docs/ssl-certificates#certificate-types), depending on your requirements.

#### DNS names, zones, and records

If you use Amazon Route 53 in your AWS environment, you can use the following in Google Cloud:

  * [Cloud Domains](https://docs.cloud.google.com/domains/docs/overview) to register your DNS domains.
  * [Cloud DNS](https://docs.cloud.google.com/dns/docs/overview) to manage your [public and private DNS zones](https://docs.cloud.google.com/dns/docs/zones/zones-overview) and your [DNS records](https://docs.cloud.google.com/dns/docs/records-overview).



For example, if you registered a domain by using Amazon Route 53, you can [transfer the domain registration to Cloud Domains](https://docs.cloud.google.com/domains/docs/transfer-domain-from-another-registrar). Similarly, if you configured public and private DNS zones using Amazon Route 53, you can [migrate that configuration to Cloud DNS](https://docs.cloud.google.com/dns/docs/migrating).

#### DDoS protection and web application firewalls

If you configured AWS Shield and AWS WAF in your AWS environment, you can use [Google Cloud Armor](https://docs.cloud.google.com/armor/docs/cloud-armor-overview) to help protect your Google Cloud workloads from DDoS attacks and from common exploits.

### Refactor deployment and operational processes

After you refactor your workloads, you refactor your deployment and operational processes to do the following:

  * Provision and configure resources in your Google Cloud environment instead of provisioning resources in your source environment.
  * Build and configure workloads, and deploy them in your Google Cloud instead of deploying them in your source environment.



You gathered information about these processes during the assessment phase earlier in this process.

The type of refactoring that you need to consider for these processes depends on how you designed and implemented them. The refactoring also depends on what you want the end state to be for each process. For example, consider the following:

  * You might have implemented these processes in your source environment and you intend to design and implement similar processes in Google Cloud. For example, you can refactor these processes to use [Cloud Build](https://docs.cloud.google.com/build/docs/overview), [Cloud Deploy](https://docs.cloud.google.com/deploy/docs/overview), and [Infrastructure Manager](https://docs.cloud.google.com/infrastructure-manager/docs/overview).
  * You might have implemented these processes in another third-party environment outside your source environment. In this case, you need to refactor these processes to target your Google Cloud environment instead of your source environment.
  * A combination of the previous approaches.



Refactoring deployment and operational processes can be complex and can require significant effort. If you try to perform these tasks as part of your workload migration, the workload migration can become more complex, and it can expose you to risks. After you assess your deployment and operational processes, you likely have an understanding of their design and complexity. If you estimate that you require substantial effort to refactor your deployment and operational processes, we recommend that you consider refactoring these processes as part of a separate, dedicated project.

For more information about how to design and implement deployment processes on Google Cloud, see:

  * [Migrate to Google Cloud: Deploy your workloads](https://docs.cloud.google.com/architecture/migration-to-gcp-deploying-your-workloads)
  * [Migrate to Google Cloud: Migrate from manual deployments to automated, containerized deployments](https://docs.cloud.google.com/architecture/migration-to-google-cloud-automated-containerized-deployments)



This document focuses on the deployment processes that produce the artifacts to deploy, and deploy them in the target runtime environment. The refactoring strategy highly depends on the complexity of these processes. The following list outlines a possible, general, refactoring strategy:

  1. Provision artifact repositories on Google Cloud. For example, you can use Artifact Registry to store artifacts and build dependencies.
  2. Refactor your build processes to store artifacts both in your source environment and in Artifact Registry.
  3. Refactor your deployment processes to deploy your workloads in your target Google Cloud environment. For example, you can start by deploying a small subset of your workloads in Google Cloud, using artifacts stored in Artifact Registry. Then, you gradually increase the number of workloads deployed in Google Cloud, until all the workloads to migrate run on Google Cloud.
  4. Refactor your build processes to store artifacts in Artifact Registry only.
  5. If necessary, migrate earlier versions of the artifacts to deploy from the repositories in your source environment to Artifact Registry. For example, to migrate container images to Artifact Registry, you can use tools like [gcrane](https://github.com/google/go-containerregistry/blob/main/cmd/gcrane/README.md) or [Rackware SWIFT](https://www.rackwareinc.com/post/rackware-swift-container-replication-backup-and-dr).
  6. Decommission the repositories in your source environment when you no longer require them.



To facilitate eventual rollbacks due to unanticipated issues during the migration, you can store container images both in your current artifact repositories in Google Cloud while the migration to Google Cloud is in progress. Finally, as part of the decommissioning of your source environment, you can refactor your container image building processes to store artifacts in Google Cloud only.

Although it might not be crucial for the success of a migration, you might need to migrate your earlier versions of your artifacts from your source environment to your artifact repositories on Google Cloud. For example, to support rolling back your workloads to arbitrary points in time, you might need to migrate earlier versions of your artifacts to Artifact Registry. For more information, see [Migrate images from a third-party registry](https://docs.cloud.google.com/artifact-registry/docs/docker/migrate-external-containers).

If you're using Artifact Registry to store your artifacts, we recommend that you configure controls to help you secure your artifact repositories, such as access control, data exfiltration prevention, vulnerability scanning, and Binary Authorization. For more information, see [Control access and protect artifacts](https://docs.cloud.google.com/artifact-registry/docs/protect-artifacts).

## Optimize your Google Cloud environment

Optimization is the last phase of your migration. In this phase, you iterate on optimization tasks until your target environment meets your optimization requirements. The steps of each iteration are as follows:

  1. Assess your current environment, teams, and optimization loop.
  2. Establish your optimization requirements and goals.
  3. Optimize your environment and your teams.
  4. Tune the optimization loop.



You repeat this sequence until you've achieved your optimization goals.

For more information about optimizing your Google Cloud environment, see [Migrate to Google Cloud: Optimize your environment](https://docs.cloud.google.com/architecture/migration-to-google-cloud-optimizing-your-environment) and [Google Cloud Well-Architected Framework: Performance optimization](https://docs.cloud.google.com/architecture/framework/performance-optimization).

## What's next

  * Read about [other AWS to Google Cloud migration journeys](https://docs.cloud.google.com/architecture/migration-from-aws-get-started).
  * Learn how to [compare AWS and Azure services to Google Cloud](https://docs.cloud.google.com/free/docs/aws-azure-gcp-service-comparison).
  * Learn where to [find help for your migrations](https://docs.cloud.google.com/architecture/migration-to-gcp-getting-started#finding_help).
  * Take the [Google Skills training course on migrating to Google Cloud](https://www.skills.google/course_templates/1561).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-05 UTC."],[],[]] 
