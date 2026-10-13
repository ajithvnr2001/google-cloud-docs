---
url: https://docs.cloud.google.com/run/docs/resource-model/
title: Deployment options and resource model \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:46.392724+00:00
---

# Deployment options and resource model  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/resource-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Deployment options and resource model Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how Cloud Run handles deployments, broken down into three areas:

  * **Deployment types** : _What_ you bring to Cloud Run, such as source code or container images.
  * **Cloud Run resources** : _What_ your deployment runs as within Cloud Run (service, job, worker pool, or instance).
  * **Deployment methods** : _How_ you execute the deployment, for example, using the Google Cloud console, gcloud CLI, YAML, or Terraform.



## Deployment types

Cloud Run offers multiple deployment options. After deployment, all deployments, executions, or creations run as sandboxed container instances on Cloud Run's fully managed and highly scalable infrastructure. The following table shows the supported deployment options for each resource type:

Deployment option | Services | Jobs | Worker pools | Instances  
---|---|---|---|---  
Deploy container images | Supported | Supported | Supported | Supported  
Deploy from source code | Supported | Supported | Supported | —  
Deploy functions1 | Supported | — | — | —  
Continuous deployment from git | Supported | — | — | —  
  
1 Functions are a specialized version of source deployment for single-purpose, event-driven code.

### Deploy container images

You can deploy any container image that adheres to Cloud Run's [container runtime contract](https://docs.cloud.google.com/run/docs/container-contract) to a Cloud Run service, [job](https://docs.cloud.google.com/run/docs/resource-model#jobs), [worker pool](https://docs.cloud.google.com/run/docs/resource-model#workerpools), or [instance](https://docs.cloud.google.com/run/docs/resource-model#instances).

### Deploy from source code

For convenience, Cloud Run lets you build and deploy source code from a single command. See [deploying services from source code](https://docs.cloud.google.com/run/docs/deploying-source-code), [executing jobs from source code](https://docs.cloud.google.com/run/docs/quickstarts/jobs/build-create-go) and [deploying worker pools from source code](https://docs.cloud.google.com/run/docs/workerpools/deploy-source-code) for details.

When you deploy from source code, Cloud Build transforms the code into a container image stored in Artifact Registry. You can deploy source code that includes a `Dockerfile` or that uses one of [the supported language runtimes](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images).

### Functions

You can [deploy single-purpose functions](https://docs.cloud.google.com/run/docs/deploy-functions) that respond to events emitted from your cloud infrastructure and services. Cloud Run triggers your function when a watched event fires.

A functions deployment is a special type of [source code deployment](https://docs.cloud.google.com/run/docs/resource-model#source), where you only have to provide the function code. You can write Cloud Run functions using a number of [supported programming languages](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images).

Deploying a function creates a Cloud Run [service](https://docs.cloud.google.com/run/docs/resource-model#services).

### Continuous source code deployment from git

Cloud Run helps you configure [continuous deployment from Git](https://docs.cloud.google.com/run/docs/continuous-deployment-with-cloud-build). Like [source deployments](https://docs.cloud.google.com/run/docs/resource-model#source), you can deploy source code that include a `Dockerfile` or are written in one of [the supported language runtimes](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images).

Continuous deployment from Git is available for Cloud Run [services](https://docs.cloud.google.com/run/docs/resource-model#services). You can manually configure them in Cloud Build for Cloud Run [jobs](https://docs.cloud.google.com/run/docs/resource-model#jobs).

## Cloud Run resources

The following sections describe Cloud Run resources in more detail.

### Cloud Run resource comparison

Feature | Services | Jobs | Worker Pools | Instances  
---|---|---|---|---  
**Primary Use Case** | Request-driven (Websites, APIs, Microservices) | Task-driven (Scripts, Data processing, Migrations) | Event/Pull-driven (Kafka/PubSub consumers) | Managed singleton (Agentic workloads, specific compute needs)  
**Trigger** | HTTP/gRPC requests, Eventarc | Execution modes - standard (immediate), delayed.  
  
Triggers - Manual execution, using Scheduler, using Workflows | Always-on OR autoscaled using pull-based background work | None  
**Scaling** | Automatic/Manual: scales to zero or based on requests | Automatic: Scales to N independent tasks that run sequentially or in parallel. | Automatic/Manual: Fixed number of instances using manual scaling or built-in autoscaling based on CPU utilization or Pub/Sub message backlog (KEDA based autoscaling using [external autoscaler](https://github.com/GoogleCloudPlatform/cloud-run-external-metrics-autoscaling?tab=readme-ov-file)) | None: No autoscaling; individually manageable  
**Lifecycle** | Ephemeral, scales down when idle | Runs to completion up to 7 days (Short-lived) | Choice between always-on background processes OR ephemeral autoscaled instances. | Long-lived (can run for days/weeks) and restart automatically indefinitely  
**Addressing** | Stable Service URL (load balanced) | No public endpoint.  
  
Internal URL for triggers (e.g. scheduler) | No public endpoint.  
  
Private Direct VPC IP based ingress access | Individual URL per Instance  
**Inbound Traffic** | Public/Internal HTTP/gRPC | None | IP based L4 ingress with Direct VPC | Public/Internal per-instance URL  
**Billing** | Request-based or Instance-based | Per-execution duration | Per-instance duration | Per-instance duration  
  
### Cloud Run services

A service is the primary resource type in Cloud Run, representing a request-driven workload that automatically scales container instances to handle incoming web traffic, HTTP requests, or events. Each service is located in a specific [Google Cloud region](https://docs.cloud.google.com/run/docs/locations). To provide redundancy and failover, Cloud Run automatically replicates services across multiple zones within a region. A given Google Cloud project can run many services in different regions.

Each service exposes a unique endpoint. By default, Cloud Run [automatically scales](https://docs.cloud.google.com/run/docs/about-instance-autoscaling) to handle incoming requests. You can optionally change the scaling behavior to [manual scaling](https://docs.cloud.google.com/run/docs/configuring/services/manual-scaling) if needed. You can deploy a service from a container, repository, or source code.

The following diagram shows the Cloud Run resource model for services:

![Cloud Run services and
revisions](https://docs.cloud.google.com/static/run/docs/images/resource-model.svg)

The diagram shows a Google Cloud project containing three Cloud Run services, Service A, Service B and Service C, each of which has several revisions:

  * Service A is getting multiple requests so Cloud Run has started multiple instances to handle the load. Each of these instances runs just one container (the application's container).
  * Service B has no requests so it is idle and Cloud Run isn't running any instances.
  * Service C has requests and has scaled to handle the load by creating multiple instances. In this case, each of these instances runs a set of multiple containers. In each set, only the ingress container receives the request but the other containers help to fulfill the request.



#### Cloud Run service revisions

Each deployment to a service creates a revision. A revision consists of one or more container images, along with configuration settings such as environment variables, memory limits, or request concurrency value.

You cannot modify a revision after its creation. For example, when you deploy a container image to a new service, Cloud Run creates the first revision. If you then deploy a different container image to that same service, Cloud Run creates a second revision. If you subsequently set an environment variable, Cloud Run creates a third revision. Over time, Cloud Run eventually removes unused revisions.

Cloud Run automatically routes requests as soon as possible to the latest healthy service revision.

#### Cloud Run service instances

Cloud Run automatically scales each service revision receiving requests to the number of instances needed to handle all these requests. Note that instances can receive many requests at the same time. With the [request concurrency setting](https://docs.cloud.google.com/run/docs/configuring/concurrency), you can set the maximum number of requests that can be sent in parallel to each instance of a revision.

### Cloud Run jobs

Each [job](https://docs.cloud.google.com/run/docs/create-jobs) is located in a specific Google Cloud region and consists of one or more job tasks that execute one or more containers to completion. Job tasks are independent and can execute in parallel in a given job execution.

#### Cloud Run job executions

When you [execute a job](https://docs.cloud.google.com/run/docs/execute/jobs), Cloud Run creates a job execution and starts all job tasks. All tasks in a job execution must complete successfully for the job execution to be successful. You can set [timeouts](https://docs.cloud.google.com/run/docs/configuring/task-timeout) on task and specify the number of [retries](https://docs.cloud.google.com/run/docs/configuring/max-retries) in case of task failure.

If any task exceeds its maximum number of retries, Cloud Run marks that task as failed and the job as failed. By default, tasks execute in parallel up to a maximum of 100, but you can specify a lower maximum if any of your backing resources, such as a database, require it.

#### Cloud Run job tasks

Every job execution executes a number of tasks in parallel, with each task running one instance. Cloud Run automatically attempts to run any failed tasks again, depending on the job's configuration for `maxRetries`.

### Cloud Run worker pools

Worker pools are a Cloud Run resource specifically designed for non-request workloads, such as pull queues. Note that worker pools don't have the following features:

  * No endpoint/URL
  * No requirement for the deployed container to listen for requests at a port
  * No automatic scaling



Similar to a Cloud Run service, deploying or updating a worker pool creates a new revision.

You can [manually scale](https://docs.cloud.google.com/run/docs/configuring/workerpools/manual-scaling) worker pool instances as needed to handle the workloads. You can also [autoscale worker pools with external metrics](https://docs.cloud.google.com/run/docs/configuring/workerpools/crema-autoscaling), which handles the scaling for workloads driven by sources such as Pub/Sub subscriptions, Prometheus queries, or Kafka queues.

When [connected to a Virtual Private Cloud (VPC) network](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc), each worker pool instance gets an IP address on the VPC network and is able to send and receive traffic to and from this VPC.

### Cloud Run instances

**Preview — Cloud Run instances**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

A Cloud Run instance represents a standalone, singleton runtime environment. Unlike a service—which scales container instances automatically or manually to handle traffic—a Cloud Run instance is a top-level resource with its own direct URL addressability and lifecycle operations.

Each Cloud Run instance includes the following features:

  * **Dedicated URL endpoint** : Assigns a stable ingress URL by default. You can disable the default URL to only allow traffic from the instance's other ingress paths.
  * **Restart policies** : Supports restart conditions (`always`, `on-failure`, `never`) to automatically recover the container process on crashes.
  * **Shared CPU allocation** : Runs on a shared CPU model where CPU is fully allocated on a burst budget basis and throttled to a 6.25% baseline resource limit outside that budget.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
