---
url: https://docs.cloud.google.com/architecture/migrate-aws-lambda-to-cloudrun/
title: Migrate from AWS to Google Cloud: Migrate from AWS Lambda to Cloud Run \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:36.890782+00:00
---

# Migrate from AWS to Google Cloud: Migrate from AWS Lambda to Cloud Run  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/migrate-aws-lambda-to-cloudrun/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Migrate from AWS to Google Cloud: Migrate from AWS Lambda to Cloud Run Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-12-31 UTC

Google Cloud provides tools, products, guidance, and professional services to assist in migrating serverless workloads from Amazon Web Services (AWS) Lambda to Google Cloud. Although Google Cloud provides several services on which you can develop and deploy serverless applications, this document focuses on migrating to [Cloud Run](https://docs.cloud.google.com/run/docs), a serverless runtime environment. Both AWS Lambda and Cloud Run share similarities such as automatic resource provisioning, scaling by the cloud provider, and a pay-per-use pricing model.

This document helps you to design, implement, and validate a plan to migrate serverless workloads from AWS Lambda to Cloud Run. Additionally, it offers guidance for those evaluating the potential benefits and process of such a migration.

This document is part of a multi-part series about migrating from AWS to Google Cloud that includes the following documents:

  * [Get started](https://docs.cloud.google.com/architecture/migration-from-aws-get-started)
  * [Migrate from Amazon EC2 to Compute Engine](https://docs.cloud.google.com/architecture/migrate-amazon-ec2-to-compute-engine)
  * [Migrate from Amazon S3 to Cloud Storage](https://docs.cloud.google.com/architecture/migrate-amazon-s3-to-cloud-storage)
  * [Migrate from Amazon EKS to Google Kubernetes Engine](https://docs.cloud.google.com/architecture/migrate-amazon-eks-to-gke)
  * [Migrate from Amazon RDS and Amazon Aurora for MySQL to Cloud SQL for MySQL](https://docs.cloud.google.com/architecture/migrate-aws-rds-to-sql-mysql)
  * [Migrate from Amazon RDS and Amazon Aurora for PostgreSQL to Cloud SQL for PostgreSQL and AlloyDB for PostgreSQL](https://docs.cloud.google.com/architecture/migrate-aws-rds-aurora-to-postgresql)
  * [Migrate from Amazon RDS for SQL Server to Cloud SQL for SQL Server](https://docs.cloud.google.com/architecture/migrate-aws-rds-to-cloudsql-for-sqlserver)
  * Migrate from AWS Lambda to Cloud Run (this document)



For more information about picking the right serverless runtime environment for your business logic, see [Select a managed container runtime environment](https://docs.cloud.google.com/architecture/select-managed-container-runtime-environment). For a comprehensive mapping between AWS and Google Cloud services, see [compare AWS and Azure services to Google Cloud services](https://docs.cloud.google.com/free/docs/aws-azure-gcp-service-comparison).

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

Migrating serverless workloads often extends beyond just moving functions from one cloud provider to another. Because cloud-based applications rely on an interconnected web of services, migrating from AWS to Google Cloud might require replacing dependent AWS services with Google Cloud services. For example, consider a scenario in which your Lambda function interacts with Amazon SQS and Amazon SNS. To migrate this function, you will likely need to adopt Pub/Sub and Cloud Tasks to achieve similar functionality.

Migration also presents a valuable chance for you to thoroughly review your serverless application's architecture and design decisions. Through this review, you might discover opportunities to do the following:

  * **Optimize with Google Cloud built-in features** : Explore whether Google Cloud services offer unique advantages or better align with your application's requirements.
  * **Simplify your architecture** : Assess whether streamlining is possible by consolidating functionality or using services differently within Google Cloud.
  * **Improve cost-efficiency** : Evaluate the potential cost differences of running your refactored application on the infrastructure that is provided on Google Cloud.
  * **Improve code efficiency** : Refactor your code alongside the migration process.



Plan your migration strategically. Don't view your migration as a rehost (lift and shift) exercise. Use your migration as a chance to enhance the overall design and code quality of your serverless application.

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

### Build an inventory of your AWS Lambda workloads

To define the scope of your migration, you create an inventory and collect information about your AWS Lambda workloads.

To build the inventory of your AWS Lambda workloads, we recommend that you do the following:

  1. To discover your AWS Lambda assets, use [Migration Center](https://docs.cloud.google.com/migration-center/docs/discover-aws-assets). Migration Center is Google Cloud's unified platform that helps you accelerate your end-to-end cloud journey from your current environment to Google Cloud.
  2. To refine the inventory of your AWS Lambda workloads, use the [AWS command-line interface (CLI)](https://docs.aws.amazon.com/cli/latest/reference/lambda/#cli-aws-lambda). For example, you can use the AWS CLI to get a list of AWS Lambda functions. Then, for each function, get its configuration details and its triggers.

  3. To review recent AWS Lambda invocation logs and durations, concurrent executions, and errors, use [CloudWatch](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html). CloudWatch provides [several types of metrics for AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html). For more information about viewing AWS Lambda metrics, see [Viewing metrics for AWS Lambda functions](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-view.html).

  4. To assess your AWS Lambda workloads inventory, use [Gemini CLI](https://geminicli.com/). For example, you can add the inventory files that list the AWS Lambda workloads to the Gemini CLI context and then prompt Gemini to help you assess those objects. For more information, see [Gemini-powered migrations to Google Cloud](https://googlecloudplatform.github.io/cloud-solutions/gemini-powered-migrations-to-google-cloud/).




After you build your inventory, we recommend that you gather information about each AWS Lambda workload in the inventory. For each workload, focus on aspects that help you anticipate potential friction. Also, analyze that workload to understand how you might need to modify the workload and its dependencies before you migrate to Cloud Run. We recommend that you start by collecting data about the following aspects of each AWS Lambda workload:

  * The use case and design
  * The source code repository
  * The deployment artifacts
  * The invocation, triggers, and outputs
  * The runtime and execution environments
  * The workload configuration
  * The access controls and permissions
  * The compliance and regulatory requirements
  * The deployment and operational processes



#### Use case and design

Gathering information about the use case and design of the workloads helps in identifying a suitable migration strategy. This information also helps you to understand whether you need to modify your workloads and their dependencies before the migration. For each workload, we recommend that you do the following:

  * Gain insights into the specific use case that the workload serves, and identify any dependencies with other systems, resources, or processes.
  * Analyze the workload's design and architecture.
  * Assess the workload's latency requirements.



#### Source code repository

Inventorying the source code of your AWS Lambda functions helps if you need to refactor your AWS Lambda workloads for compatibility with Cloud Run. Creating this inventory involves tracking the codebase, which is typically stored in version control systems like Git or in development platforms such as GitHub or GitLab. The inventory of your source code is essential for your DevOps processes, such as continuous integration and continuous development (CI/CD) pipelines, because these processes will also need to be updated when you migrate to Cloud Run.

#### Deployment artifacts

Knowing what deployment artifacts are needed by the workload is another component in helping you understand whether you might need to refactor your AWS Lambda workloads. To identify what deployment artifacts that the workload needs, gather the following information:

  * The type of deployment package to deploy the workload.
  * Any AWS Lambda layer that contains additional code, such as libraries and other dependencies.
  * Any AWS Lambda extensions that the workload depends on.
  * The qualifiers that you configured to specify versions and aliases.
  * The deployed workload version.



#### Invocation, triggers, and outputs

AWS Lambda supports several invocation mechanisms, such as triggers, and different invocation models, such as synchronous invocation and asynchronous invocation. For each AWS Lambda workload, we recommend that you gather the following information that is related to triggers and invocations:

  * The triggers and event source mappings that invoke the workload.
  * Whether the workload supports synchronous and asynchronous invocations.
  * The workload URLs and HTTP(S) endpoints.



Your AWS Lambda workloads can interact with other resources and systems. You need to know what resources consume the outputs of your AWS Lambda workloads and how those resources consume those outputs. This knowledge helps you to determine whether you need to modify anything that might depend on those outputs, such as other systems or workloads. For each AWS Lambda workload, we recommend that you gather the following information about other resources and systems:

  * The destination resources that the workload might send events to.
  * The destinations that receive information records for asynchronous invocations.
  * The format for the events that the workload processes.
  * How your AWS Lambda workload and its extensions interact with AWS Lambda APIs, or other AWS APIs.



In order to function, your AWS Lambda workloads might store persistent data and interact with other AWS services. For each AWS Lambda workload, we recommend that you gather the following information about data and other services:

  * Whether the workload accesses virtual private clouds (VPCs) or other private networks.
  * How the workload stores persistent data, such as by using ephemeral data storage and Amazon Elastic File System (EFS).



#### Runtime and execution environments

AWS Lambda supports several execution environments for your workloads. To correctly map AWS Lambda execution environments to Cloud Run execution environments, we recommend that you assess the following for each AWS Lambda workload:

  * The execution environment of the workload.
  * The instruction set architecture of the computer processor on which the workload runs.



If your AWS Lambda workloads run in language-specific runtime environments, consider the following for each AWS Lambda workload:

  * The type, version, and unique identifier of the language-specific runtime environment.
  * Any modifications that you applied to the runtime environment.



#### Workload configuration

In order to configure your workloads as you migrate them from AWS Lambda to Cloud Run, we recommend that you assess how you configured each AWS Lambda workload.

For each AWS Lambda workload, gather information about the following concurrency and scalability settings:

  * The concurrency controls.
  * The scalability settings.
  * The configuration of the instances of the workload, in terms of the amount of memory available and the maximum execution time allowed.
  * Whether the workload is using AWS Lambda SnapStart, reserved concurrency, or provisioned concurrency to reduce latency.
  * The environment variables that you configured, as well as the ones that AWS Lambda configures and the workload depends on.
  * The tags and attribute-based access control.
  * The state machine to handle exceptional conditions.
  * The base images and configuration files (such as the Dockerfile) for deployment packages that use container images.



#### Access controls and permissions

As part of your assessment, we recommend that you assess the security requirements of your AWS Lambda workloads and their configuration in terms of access controls and management. This information is critical if you need to implement similar controls in your Google Cloud environment. For each workload, consider the following:

  * The execution role and permissions.
  * The identity and access management configuration that the workload and its layers use to access other resources.
  * The identity and access management configuration that other accounts and services use to access the workload.
  * The Governance controls.



#### Compliance and regulatory requirements

For each AWS Lambda workload, make sure that you understand its compliance and regulatory requirements by doing the following:

  * Assess any compliance and regulatory requirements that the workload needs to meet.
  * Determine whether the workload is meeting these requirements.
  * Determine whether there are any future requirements that will need to be met.



Compliance and regulatory requirements might be independent from the cloud provider that you're using, and these requirements might have an impact on the migration as well. For example, you might need to ensure that data and network traffic stays within the boundaries of certain geographies, such as the European Union (EU).

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



### Complete the assessment

After you build the inventories from your AWS Lambda environment, complete the rest of the activities of the assessment phase as described in [Migrate to Google Cloud: Assess and discover your workloads](https://docs.cloud.google.com/solutions/migration-to-gcp-assessing-and-discovering-your-workloads).

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

## Migrate your AWS Lambda workloads

To migrate your workloads from AWS Lambda to Cloud Run, do the following:

  1. Design, provision, and configure your Cloud Run environment.
  2. If needed, refactor your AWS Lambda workloads to make them compatible with Cloud Run.
  3. Refactor your deployment and operational processes to deploy and observe your workloads on Cloud Run.
  4. Migrate the data that is needed by your AWS Lambda workloads.
  5. Validate the migration results in terms of functionality, performance, and cost.



To help you avoid issues during the migration, and to help estimate the effort that is needed for the migration, we recommend that you evaluate how AWS Lambda features compare to similar Cloud Run features. AWS Lambda and Cloud Run features might look similar when you compare them. However, differences in the design and implementation of the features in the two cloud providers can have significant effects on your migration from AWS Lambda to Cloud Run. These differences can influence both your design and refactoring decisions, as highlighted in the following sections.

### Design, provision, and configure your Cloud Run environment

The first step of the migrate phase is to design your Cloud Run environment so that it can support the workloads that you are migrating from AWS Lambda.

In order to correctly design your Cloud Run environment, use the data that you gathered during the assessment phase about each AWS Lambda workload. This data helps you to do the following:

  1. Choose the right Cloud Run resources to deploy your workload.
  2. Design your Cloud Run resources configuration.
  3. Provision and configure the Cloud Run resources.



#### Choose the right Cloud Run resources

For each AWS Lambda workload to migrate, choose the right Cloud Run resource to deploy your workloads. Cloud Run supports the following main resources:

  * **Cloud Run services** : a resource that hosts a containerized runtime environment, exposes a unique endpoint, and automatically scales the underlying infrastructure according to demand.
  * **Cloud Run jobs** : a resource that executes one or more containers to completion.



The following table summarizes how AWS Lambda resources map to these main Cloud Run resources:

AWS Lambda resource | Cloud Run resource  
---|---  
AWS Lambda function that gets triggered by an event such as those used for websites and web applications, APIs and microservices, streaming data processing, and event-driven architectures. | Cloud Run service that you can invoke with triggers.  
AWS Lambda function that has been scheduled to run such as those for background tasks and batch jobs. | Cloud Run job that runs to completion.  
  
Beyond services and jobs, Cloud Run provides additional resources that extend these main resources. For more information about all of the available Cloud Run resources, see [Cloud Run resource model](https://docs.cloud.google.com/run/docs/resource-model).

#### Design your Cloud Run resources configuration

Before you provision and configue your Cloud Run resources, you design their configuration. Certain AWS Lambda configuration options, such as resource limits and request timeouts, are comparable to similar Cloud Run configuration options. The following sections describe the configuration options that are available in Cloud Run for service triggers and job execution, resource configuration, and security. These sections also highlight AWS Lambda configuration options that are comparable to those in Cloud Run.

##### Cloud Run service triggers and job execution

Service triggers and job execution are the main design decisions that you need to consider when you migrate your AWS Lambda workloads. Cloud Run provides a variety of options to trigger and run the event-based workloads that are used in AWS Lambda. In addition, Cloud Run provides options that you can use for streaming workloads and scheduled jobs.

When you migrate your workloads, it is often useful to first understand what triggers and mechanisms are available in Cloud Run. This information helps with your understanding of how Cloud Run works. Then, you can use this understanding to determine which Cloud Run features are comparable to AWS Lambda features and which Cloud Run features could be used when refactoring those workloads.

To learn more about the service triggers that Cloud Run provides, use the following resources:

  * [HTTPS invocation](https://docs.cloud.google.com/run/docs/triggering/https-request): send HTTPS requests to trigger Cloud Run services.
  * [HTTP/2 invocation](https://docs.cloud.google.com/run/docs/configuring/http2): send HTTP/2 requests to trigger Cloud Run services.
  * [WebSockets](https://docs.cloud.google.com/run/docs/triggering/websockets): connect clients to a WebSockets server running on Cloud Run.
  * [gRPC connections](https://docs.cloud.google.com/run/docs/triggering/grpc): connect to Cloud Run services using gRPC.
  * [Asynchronous invocation](https://docs.cloud.google.com/run/docs/triggering/using-tasks): enqueue tasks using Cloud Tasks to be asynchronously processed by Cloud Run services.
  * [Scheduled invocation](https://docs.cloud.google.com/run/docs/triggering/using-scheduler): use Cloud Scheduler to invoke Cloud Run services on a schedule.
  * [Event-based invocation](https://docs.cloud.google.com/run/docs/triggering/trigger-with-events): create Eventarc triggers to invoke Cloud Run services on specific events in [CloudEvents format](https://docs.cloud.google.com/eventarc/docs/overview#event-format).
  * [Integration with Pub/Sub](https://docs.cloud.google.com/run/docs/tutorials/pubsub): invoke Cloud Run services from Pub/Sub push subscriptions.
  * [Integration with Workflows](https://docs.cloud.google.com/run/docs/triggering/invoke-services-from-workflows): invoke a Cloud Run service from a workflow.



To learn more about the job execution mechanisms that Cloud Run provides, use the following resources:

  * [On-demand execution](https://docs.cloud.google.com/run/docs/execute/jobs): create job executions that run to completion.
  * [Scheduled execution](https://docs.cloud.google.com/run/docs/execute/jobs-on-schedule): execute Cloud Run jobs on a schedule.
  * [Integration with Workflows](https://docs.cloud.google.com/run/docs/triggering/invoke-jobs-with-workflows): execute Cloud Run jobs from a workflow.



To help you understand which Cloud Run invocation or execution mechanisms are comparable to AWS Lambda invocation mechanisms, use the following table. For each Cloud Run resource that you need to provision, make sure to choose the right invocation or execution mechanism.

AWS Lambda feature | Cloud Run feature  
---|---  
HTTPS trigger (function URLs) | HTTPS invocation  
HTTP/2 trigger (partially supported using an external API gateway) | HTTP/2 invocation (supported natively)  
WebSockets (supported using external API gateway) | WebSockets (supported natively)  
N/A (gRPC connections not supported) | gRPC connections  
Asynchronous invocation | Cloud Tasks integration  
Scheduled invocation | Cloud Scheduler integration  
Event-based trigger in a proprietary event format | Event-based invocation in CloudEvents format  
Amazon SQS and Amazon SNS integration | Pub/Sub integration  
AWS Lambda Step Functions | Workflows integration  
**Note:** This document focuses on migrating from AWS Lambda workloads to Cloud Run. If you use AWS Step Functions and you need to migrate them as well, see [Migrate from AWS Step Functions to Workflows](https://docs.cloud.google.com/workflows/docs/migrate-from-step-functions).

##### Cloud Run resource configuration

To supplement the design decisions that you made for triggering and running your migrated workloads, Cloud Run supports several configuration options that let you fine tune several aspects of the runtime environment. These configuration options consist of resource services and jobs.

As mentioned earlier, you can better understand how Cloud Run works by first developing an understanding of all of the configuration options that are available in Cloud Run. This understanding then helps you to compare AWS Lambda features to similar Cloud Run features, and helps you determine how to refactor your workloads.

To learn more about the configurations that Cloud Run services provide, use the following resources:

  * Capacity: [memory limits](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits), [CPU limits](https://docs.cloud.google.com/run/docs/configuring/services/cpu), [CPU allocation](https://docs.cloud.google.com/run/docs/configuring/cpu-allocation), [request timeout](https://docs.cloud.google.com/run/docs/configuring/request-timeout), [maximum concurrent requests](https://docs.cloud.google.com/run/docs/about-concurrency) per instance, [minimum instances](https://docs.cloud.google.com/run/docs/configuring/min-instances), [maximum instances](https://docs.cloud.google.com/run/docs/configuring/max-instances), and [GPU configuration](https://docs.cloud.google.com/run/docs/configuring/services/gpu)
  * Environment: [container port and entrypoint](https://docs.cloud.google.com/run/docs/configuring/services/containers), [environment variables](https://docs.cloud.google.com/run/docs/configuring/services/environment-variables), [Cloud Storage volume mounts](https://docs.cloud.google.com/run/docs/configuring/services/cloud-storage-volume-mounts), [in-memory volume mounts](https://docs.cloud.google.com/run/docs/configuring/services/in-memory-volume-mounts), [execution environment](https://docs.cloud.google.com/run/docs/about-execution-environments), [container health checks](https://docs.cloud.google.com/run/docs/configuring/healthchecks), [secrets](https://docs.cloud.google.com/run/docs/configuring/services/secrets), and [service accounts](https://docs.cloud.google.com/run/docs/configuring/services/service-accounts)
  * [Autoscaling](https://docs.cloud.google.com/run/docs/about-instance-autoscaling)
  * Handling exceptional conditions: [Pub/Sub failure handling](https://docs.cloud.google.com/pubsub/docs/handling-failures), and [Eventarc failure handling](https://docs.cloud.google.com/eventarc/docs/retry-events)
  * Metadata: [description](https://docs.cloud.google.com/run/docs/configuring/description), [labels](https://docs.cloud.google.com/run/docs/configuring/services/labels), and [tags](https://docs.cloud.google.com/run/docs/configuring/tags)
  * Traffic serving: [custom domain mapping](https://docs.cloud.google.com/run/docs/mapping-custom-domains), [auto-assigned URLs](https://docs.cloud.google.com/run/docs/triggering/https-request), [Cloud CDN integration](https://docs.cloud.google.com/run/docs/set-up-cdn), and [session affinity](https://docs.cloud.google.com/run/docs/configuring/session-affinity)



To learn more about the jobs that Cloud Run provides, use the following resources:

  * Capacity: [memory limits](https://docs.cloud.google.com/run/docs/configuring/jobs/memory-limits), [CPU limits](https://docs.cloud.google.com/run/docs/configuring/jobs/cpu), [parallelism](https://docs.cloud.google.com/run/docs/configuring/parallelism), and [task timeout](https://docs.cloud.google.com/run/docs/configuring/task-timeout)
  * Environment: [container entrypoint](https://docs.cloud.google.com/run/docs/configuring/jobs/containers), [environment variables](https://docs.cloud.google.com/run/docs/configuring/jobs/environment-variables), [Cloud Storage volume mounts](https://docs.cloud.google.com/run/docs/configuring/jobs/cloud-storage-volume-mounts), [in-memory volume mounts](https://docs.cloud.google.com/run/docs/configuring/jobs/in-memory-volume-mounts), [secrets](https://docs.cloud.google.com/run/docs/configuring/jobs/secrets), and [service accounts](https://docs.cloud.google.com/run/docs/configuring/jobs/service-accounts)
  * Handling exceptional conditions: [maximum retries](https://docs.cloud.google.com/run/docs/configuring/max-retries)
  * Metadata: [labels](https://docs.cloud.google.com/run/docs/configuring/jobs/labels) and [tags](https://docs.cloud.google.com/run/docs/configuring/jobs/tags)



To help you understand which Cloud Run configuration options are comparable to AWS Lambda configuration options, use the following table. For each Cloud Run resource that you need to provision, make sure to choose the right configuration options.

AWS Lambda feature | Cloud Run feature  
---|---  
Provisioned concurrency | Minimum instances  
Reserved concurrency per instance  
(The concurrency pool is shared across AWS Lambda functions in your AWS account.) | Maximum instances per service  
N/A (not supported, one request maps to one instance) | Concurrent requests per instance  
N/A (depends on memory allocation) | CPU allocation  
Scalability settings | Instance autoscaling for services  
Parallelism for jobs  
Instance configuration (CPU, memory) | CPU and memory limits  
Maximum execution time | Request timeout for services  
Task timeout for jobs  
AWS Lambda SnapStart | Startup CPU boost  
Environment variables | Environment variables  
Ephemeral data storage | In-memory volume mounts  
Amazon Elastic File System connections | NFS volume mounts  
S3 volume mounts are not supported | Cloud Storage volume mounts  
AWS Secrets Manager in AWS Lambda workloads | Secrets  
Workload URLs and HTTP(S) endpoints | Auto-assigned URLs  
[Cloud Run integrations with Google Cloud products](https://docs.cloud.google.com/run/docs/integrate)  
Sticky sessions (using an external load balancer) | Session affinity  
Qualifiers | [Revisions](https://docs.cloud.google.com/run/docs/resource-model#revisions)  
  
In addition to the features that are listed in the previous table, you should also consider the differences between how AWS Lambda and Cloud Run provision instances of the execution environment. AWS Lambda provisions a single instance for each concurrent request. However, Cloud Run lets you [set the number of concurrent requests that an instance can serve](https://docs.cloud.google.com/run/docs/about-concurrency). That is, the provisioning behavior of AWS Lambda is equivalent to setting the maximum number of concurrent requests per instance to 1 in Cloud Run. Setting the maximum number of concurrent requests to more than 1 can significantly save costs because the CPU and memory of the instance is shared by the concurrent requests, but they are only billed once. Most HTTP frameworks are designed to handle requests in parallel.

##### Cloud Run security and access control

When you design your Cloud Run resources, you also need to decide on the security and access controls that you need for your migrated workloads. [Cloud Run supports several configuration options to help you secure your environment](https://docs.cloud.google.com/run/docs/securing/security), and to set roles and permissions for your Cloud Run workloads.

This section highlights the security and access controls that are available in Cloud Run. This information helps you both understand how your migrated workloads will function in Cloud Run and identify those Cloud Run options that you might need if you refactor those workloads.

To learn more about the authentication mechanisms that Cloud Run provides, use the following resources:

  * [Allow public (unauthenticated) access](https://docs.cloud.google.com/run/docs/authenticating/public)
  * [Custom audiences](https://docs.cloud.google.com/run/docs/configuring/custom-audiences)
  * [Developer authentication](https://docs.cloud.google.com/run/docs/authenticating/developers)
  * [Service-to-service authentication](https://docs.cloud.google.com/run/docs/authenticating/service-to-service)
  * [User authentication](https://docs.cloud.google.com/run/docs/authenticating/end-users)



To learn more about the security features that Cloud Run provides, use the following resources:

  * [Access control with Identity and Access Management (IAM)](https://docs.cloud.google.com/run/docs/securing/managing-access)
  * [Per-service identity](https://docs.cloud.google.com/run/docs/securing/service-identity)
  * [Google Cloud Armor integration](https://docs.cloud.google.com/run/docs/securing/cloud-armor)
  * [Binary Authorization](https://docs.cloud.google.com/run/docs/securing/binary-authorization)
  * [Customer managed encryption keys](https://docs.cloud.google.com/run/docs/securing/using-cmek)
  * [Software supply chain security](https://docs.cloud.google.com/run/docs/securing/software-delivery-shield-panel)
  * [Ingress restriction settings](https://docs.cloud.google.com/run/docs/securing/ingress)
  * [VPC Service Controls](https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls)



To help you understand which Cloud Run security and access controls are comparable to those that are available in AWS Lambda, use the following table. For each Cloud Run resource that you need to provision, make sure to choose the right access controls and security features.

AWS Lambda feature | Cloud Run feature  
---|---  
Access control with AWS identity access and management | Access control with Google Cloud's IAM  
Execution role | Google Cloud's [IAM role](https://docs.cloud.google.com/run/docs/reference/iam/roles)  
Permission boundaries | Google Cloud's [IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions) and custom audiences  
Governance controls | [Organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview)  
Code signing | Binary authorization  
Full VPC access | [Granular VPC egress access controls](https://docs.cloud.google.com/run/docs/securing/private-networking)  
  
#### Provision and configure Cloud Run resources

After you choose the Cloud Run resources to deploy your workloads, you provision and configure those resources. For more information about provisioning Cloud Run resources, see the following:

  * [Deploy a Cloud Run Service from source](https://docs.cloud.google.com/run/docs/deploying-source-code)
  * [Deploying container images to Cloud Run](https://docs.cloud.google.com/run/docs/deploying)
  * [Create jobs](https://docs.cloud.google.com/run/docs/create-jobs)
  * [Deploy a Cloud Run function](https://docs.cloud.google.com/functions/docs/deploy)



### Refactor AWS Lambda workloads

To migrate your AWS Lambda workloads to Cloud Run, you might need to refactor them. For example, if an event-based workload accepts triggers that contain Amazon CloudWatch events, you might need to refactor that workload to make it accept events in the [CloudEvents format](https://docs.cloud.google.com/eventarc/docs/overview#event-format).

To help you with the refactoring of your AWS Lambda workloads, we recommend that you use [Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/overview) and [Gemini CLI](https://geminicli.com/). For more information, see [Gemini-powered migrations to Google Cloud](https://googlecloudplatform.github.io/cloud-solutions/gemini-powered-migrations-to-google-cloud/).

There are several factors that may influence the amount of refactoring that you need for each AWS Lambda workload, such as the following:

  * **Architecture**. Consider how the workload is designed in terms of architecture. For example, AWS Lambda workloads that have clearly separated the business logic from the logic to access AWS-specific APIs might require less refactoring as compared to workloads where the two logics are mixed.
  * **Idempotency**. Consider whether the workload is idempotent in regard to its inputs. A workload that is idempotent to inputs might require less refactoring as compared to workloads that need to maintain state about which inputs they've already processed.
  * **State**. Consider whether the workload is stateless. A stateless workload might require less refactoring as compared to workloads that maintain state. For more information about the services that Cloud Run supports to store data, see [Cloud Run storage options](https://docs.cloud.google.com/run/docs/storage-options).
  * **Runtime environment**. Consider whether the workload makes any assumptions about its runtime environment. For these types of workloads, you might need to satisfy the same assumptions in the Cloud Run runtime environment or refactor the workload if you can't assume the same for the Cloud Run runtime environment. For example, if a workload requires certain packages or libraries to be available, you need to install them in the Cloud Run runtime environment that is going to host that workload.
  * **Configuration injection**. Consider whether the workload supports using environment variables and secrets to inject (set) its configuration. A workload that supports this type of injection might require less refactoring as compared to workloads that support other configuration injection mechanisms.
  * **APIs**. Consider whether the workload interacts with AWS Lambda APIs. A workload that interacts with these APIs might need to be refactored to use Cloud APIs and [Cloud Run APIs](https://docs.cloud.google.com/run/docs/apis).
  * **Error reporting**. Consider whether the workload [reports errors using standard output and error streams](https://docs.cloud.google.com/run/docs/error-reporting). A workload that does such error reporting might require less refactoring as compared to workloads that report errors using other mechanisms.



For more information about developing and optimizing Cloud Run workloads, see the following resources:

  * [General development tips](https://docs.cloud.google.com/run/docs/tips/general)
  * [Optimize Java applications for Cloud Run](https://docs.cloud.google.com/run/docs/tips/java)
  * [Optimize Python applications for Cloud Run](https://docs.cloud.google.com/run/docs/tips/python)
  * [Load testing best practices](https://docs.cloud.google.com/run/docs/about-load-testing)
  * [Jobs retries and checkpoints best practices](https://docs.cloud.google.com/run/docs/jobs-retries)
  * [Frontend proxying using Nginx](https://docs.cloud.google.com/run/docs/internet-proxy-nginx-sidecar)
  * [Serve static assets with Cloud CDN and Cloud Run](https://docs.cloud.google.com/run/docs/set-up-cdn)
  * [Understand Cloud Run zonal redundancy](https://docs.cloud.google.com/run/docs/zonal-redundancy)



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

#### Refactor operational processes

As part of your migration to Cloud Run, we recommend that you refactor your operational processes to constantly and effectively monitor your Cloud Run environment.

Cloud Run integrates with the following operational services:

  * [Google Cloud Observability](https://docs.cloud.google.com/run/docs/monitoring) to provide logging, monitoring, and alerting for your workloads. If needed, you can also get [Prometheus-style monitoring](https://docs.cloud.google.com/run/docs/monitoring-managed-prometheus-sidecar) or [OpenTelemetry metrics](https://docs.cloud.google.com/run/docs/tutorials/custom-metrics-opentelemetry-sidecar) for your Cloud Run workloads.
  * [Cloud Audit Logs](https://docs.cloud.google.com/run/docs/audit-logging) to provide audit logs.
  * [Cloud Trace](https://docs.cloud.google.com/run/docs/trace) to provide distributed performance tracing.



### Migrate data

The assessment phase earlier in this process should have helped you determine whether the AWS Lambda workloads that you're migrating either depend on or produce data that resides in your AWS environment. For example, you might have determined that you need to migrate data from AWS S3 to Cloud Storage, or from Amazon RDS and Aurora to Cloud SQL and AlloyDB for PostgreSQL. For more information about migrating data from AWS to Google Cloud, see [Migrate from AWS to Google Cloud: Get started](https://docs.cloud.google.com/architecture/migration-from-aws-get-started).

As with refactoring deployment and operational processes, migrating data from AWS to Google Cloud can be complex and can require significant effort. If you try to perform these data migration tasks as part of the migration of your AWS Lambda workloads, the migration can become complex and can expose you to risks. After you analyze the data to migrate, you'll likely have an understanding of the size and complexity of the data. If you estimate that you require substantial effort to migrate this data, we recommend that you consider migrating data as part of a separate, dedicated project.

### Validate the migration results

Validating your workload migration isn't a one-time event but a continuous process. You need to maintain focus on testing and validation before, during, and after migrating from AWS Lambda to Cloud Run.

To help ensure a successful migration with optimal performance and minimal disruptions, we recommend that you use the following process to validate the workloads that you're migrating from AWS Lambda to Cloud Run:

  * Before you start the migration phase, refactor your existing test cases to take into account the target Google Cloud environment.
  * During the migration, validate test results at each migration milestone and conduct thorough integration tests.
  * After the migrations, do the following testing: 
    * **Baseline testing** : Establish performance benchmarks of the original workload on AWS Lambda, such as execution time, resource usage, and error rates under different loads. Replicate these tests on Cloud Run to identify discrepancies that could point to migration or configuration problems.
    * **Functional testing** : Ensure that the core logic of your workloads remains consistent by creating and executing test cases that cover various input and expected output scenarios in both environments.
    * **Load testing** : Gradually increase traffic to evaluate the performance and scalability of Cloud Run under real-world conditions. To help ensure a seamless migration, address discrepancies such as errors and resource limitations.



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

Authors: 

  * [Marco Ferrari](https://www.linkedin.com/in/ferrarimark) | Cloud Solutions Architect
  * [Xiang Shen](https://www.linkedin.com/in/xiangshen07) | Solutions Architect



Other contributors: 

  * [Steren Giannini](https://www.linkedin.com/in/steren) | Group Product Manager
  * [James Ma](https://www.linkedin.com/in/james-ma-526a6012) | Product Manager
  * [Henry Bell](https://www.linkedin.com/in/henry-bell-uk) | Cloud Solutions Architect
  * [Christoph Stanger](https://www.linkedin.com/in/cstanger) | Strategic Cloud Engineer
  * CC Chen | Customer Solutions Architect
  * [Wietse Venema](https://www.linkedin.com/in/wietse-venema) | Developer Relations Engineer



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-31 UTC."],[],[]] 
