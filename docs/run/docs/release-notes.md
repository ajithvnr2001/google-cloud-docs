---
url: https://docs.cloud.google.com/run/docs/release-notes/
title: Cloud Run release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:51:05.012769+00:00
---

# Cloud Run release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Resources ](https://docs.cloud.google.com/run/docs/resources)



Send feedback 

#  Cloud Run release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Cloud Run. You can periodically check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/run-release-notes.xml) directly. 

## October 22, 2026

Feature

You can configure [Direct VPC ingress for Cloud Run instances](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#direct-vpc-instance) ([Preview](https://cloud.google.com/products#product-launch-stages)). Direct VPC ingress lets Cloud Run instances on a VPC network use their own ephemeral private IP address to communicate with each other and with other resources on the VPC network.

Security

All supported versions of [PHP 8.2](https://docs.cloud.google.com/run/docs/runtime-support#php) and later are patched. Take immediate protective action by redeploying your resources with updated dependencies.

See [Responding to core PHP vulnerabilities](https://cloud.google.com/blog/products/identity-security/responding-to-core-php-vulnerabilities-cve-2026-109618-cve-2026-109619) for more information.

## October 21, 2026

Security

This note is incorrect; follow guidance in the entry for October 22, 2026.

Patch updates to [supported PHP runtimes](https://docs.cloud.google.com/run/docs/runtime-support#php) are available for Cloud Run resources [deployed from source code](https://docs.cloud.google.com/run/docs/deploying-source-code): `8.5.12`, `8.4.27`, `8.3.36`, and `8.2.35`. Take immediate action to protect your workloads by redeploying your Cloud Run resources with updated dependencies. Cloud Run resources with [automatic base image updates](https://docs.cloud.google.com/run/docs/configuring/services/automatic-base-image-updates) enabled have already been patched. See [Responding to core PHP vulnerabilities](https://cloud.google.com/blog/products/identity-security/responding-to-core-php-vulnerabilities-cve-2026-109618-cve-2026-109619) for more information.

## October 12, 2026

Feature

Support for [Budget spend caps](https://docs.cloud.google.com/run/docs/configuring/billing-settings#spend-caps) to pause your Cloud Run workloads is in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

## October 07, 2026

Feature

[SSH for Cloud Run services and instances](https://docs.cloud.google.com/run/docs/troubleshooting/ssh) is in [Preview](https://cloud.google.com/products#product-launch-stages). Use this feature to establish a secure, interactive shell connection to your running instances.

## September 29, 2026

Feature

Support for specifying custom target CPU or concurrency utilization using [scaling controls](https://docs.cloud.google.com/run/docs/configuring/scaling-controls) is in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

## September 28, 2026

Feature

Create [custom URLs](https://docs.cloud.google.com/run/docs/custom-urls), like `example.cloud.run`, that are easy to remember and globally available for your Cloud Run services. No DNS configuration, load balancers, or extra costs required ([Preview](https://cloud.google.com/products#product-launch-stages)).

## September 08, 2026

Feature

To take advantage of [reduced pricing](https://cloud.google.com/run/pricing#delayed-jobs) for Cloud Run jobs, you can [delay job execution](https://docs.cloud.google.com/run/docs/delayed-jobs) to defer non-urgent tasks for up to 12 hours ([Preview](https://cloud.google.com/products#product-launch-stages)).

## September 01, 2026

Feature

Configure [Agent Platform features](https://docs.cloud.google.com/run/docs/ai/agent-platform-features) on your Cloud Run services and jobs to securely authenticate AI agents and MCP servers using system-managed Agent Identities. This support also includes automatic registration in the Agent Registry ([Preview](https://cloud.google.com/products#product-launch-stages)).

Feature

Support for the [Go 1.27 runtime](https://docs.cloud.google.com/run/docs/runtime-support#go) is in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

## August 25, 2026

Feature

[Cloud Run instances](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run#cloud-run-instances) are available in [Preview](https://cloud.google.com/products#product-launch-stages). Instances are specifically designed for running long-lived and individually addressable workloads. To learn more, see the [product overview](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run), [resource comparison](https://docs.cloud.google.com/run/docs/resource-model#resource-comparison), and [instance lifecycle](https://docs.cloud.google.com/run/docs/instances/instance-lifecycle) pages.

## August 19, 2026

Feature

Support for the [Go 1.27 runtime](https://docs.cloud.google.com/run/docs/runtime-support#go) is in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

Starting from Go runtime version 1.26 and later, the lifecycle support dates align more closely with the [Go community release cycle](https://go.dev/wiki/Go-Release-Cycle). For more information, see [Runtime support schedule](https://docs.cloud.google.com/run/docs/runtime-support#go).

## August 11, 2026

Feature

Cloud Run NVIDIA L4 GPU driver version 580.x.x is available for [services](https://docs.cloud.google.com/run/docs/configuring/services/gpu), [jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/gpu), and [worker pools](https://docs.cloud.google.com/run/docs/configuring/workerpools/gpu).

## August 05, 2026

Feature

Cloud Run supports [sandboxes](https://docs.cloud.google.com/run/docs/code-execution) for all resources, including [jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/sandboxes) and [worker pools](https://docs.cloud.google.com/run/docs/configuring/workerpools/sandboxes) ([Preview](https://cloud.google.com/products#product-launch-stages)).

## July 27, 2026

Feature

Support for the [Node.js 26 runtime](https://docs.cloud.google.com/static/run/docs/runtime-support#node.js) is in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

Support for [Budget spend caps](https://docs.cloud.google.com/run/docs/configuring/billing-settings#spend-caps) to pause your Cloud Run workloads is in [Preview](https://cloud.google.com/products#product-launch-stages).

## July 14, 2026

Feature

Cloud Run support for [importing public container images from GitHub Container Registry](https://docs.cloud.google.com/run/docs/deploying#images) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## July 08, 2026

Feature

Cloud Run sandboxes provide a fast and secure isolated environment to execute untrusted code, such as code generated by AI agents. For more information, see [Configure sandboxes for services](https://docs.cloud.google.com/run/docs/configuring/services/sandboxes) and [Code execution in Cloud Run](https://docs.cloud.google.com/run/docs/code-execution) ([Preview](https://cloud.google.com/products#product-launch-stages)).

## June 29, 2026

Feature

Deploy a highly available, multi-region Cloud Run service with automated failover and failback for internal and external traffic using [Cloud Run service health](https://docs.cloud.google.com/run/docs/configuring/configure-service-health) in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

Feature

[Configure HTTP and gRPC readiness probes](https://docs.cloud.google.com/run/docs/configuring/configure-service-health) for your Cloud Run services is in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

## April 20, 2026

Feature

Cloud Run ephemeral disk, which allows you to mount a volume that persists only for the duration of your [service](https://docs.cloud.google.com/run/docs/configuring/services/ephemeral-disk), [job](https://docs.cloud.google.com/run/docs/configuring/jobs/ephemeral-disk), or [worker pool](https://docs.cloud.google.com/run/docs/configuring/workerpools/ephemeral-disk) instance, is in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 16, 2026

Feature

Support for specifying custom CPU or concurrency targets using [scaling controls](https://docs.cloud.google.com/run/docs/configuring/scaling-controls) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 15, 2026

Feature

The [Cloud Run remote MCP server](https://docs.cloud.google.com/run/docs/use-cloud-run-mcp), which lets agents and AI applications deploy with Cloud Run, is in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

## April 14, 2026

Feature

Support for [worker pools](https://docs.cloud.google.com/run/docs/deploy-worker-pools) is in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

## April 13, 2026

Feature

Support for NVIDIA RTX PRO 6000 Blackwell GPU is in [General Availability](https://cloud.google.com/products#product-launch-stages). For more information, see GPU support for [services](https://docs.cloud.google.com/run/docs/configuring/services/gpu), [jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/gpu), and [worker pools](https://docs.cloud.google.com/run/docs/configuring/workerpools/gpu).

## March 25, 2026

Feature

[Deploying services using a Compose file](https://docs.cloud.google.com/run/docs/deploy-run-compose) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## March 17, 2026

Feature

Support for [Ruby 4.0 runtime](https://docs.cloud.google.com/run/docs/runtime-support#ruby) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## March 13, 2026

Feature

[Configuring Identity-Aware Proxy (IAP) directly on Cloud Run](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run) to secure your services without the need for load balancers is in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

## March 12, 2026

Feature

Support for [Go 1.26 runtime](https://docs.cloud.google.com/run/docs/runtime-support#go) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## March 03, 2026

Feature

Support for [Ruby 4.0 runtime](https://docs.cloud.google.com/run/docs/runtime-support#ruby) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 27, 2026

Feature

Support for [PHP 8.5 runtime](https://docs.cloud.google.com/run/docs/runtime-support#php) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## February 24, 2026

Feature

Deploy a highly available, multi-region Cloud Run service with automated failover and failback for [external traffic using Cloud Run service health](https://docs.cloud.google.com/run/docs/multiple-regions#service-health) (Preview).

Feature

You can use the [Cloud Run remote MCP server](https://docs.cloud.google.com/run/docs/reference/mcp) to let agents and AI applications deploy with Cloud Run ([Preview](https://cloud.google.com/products#product-launch-stages)).

## February 19, 2026

Feature

Support for [Go 1.26 runtime](https://docs.cloud.google.com/run/docs/runtime-support#go) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## February 18, 2026

Feature

Support for [.NET 10 runtime](https://docs.cloud.google.com/run/docs/runtime-support#.net) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## February 17, 2026

Feature

Cloud Run [source deployment](https://docs.cloud.google.com/run/docs/deploying-source-code) supports Ubuntu 24 LTS base images in [General Availability](https://cloud.google.com/products#product-launch-stages). This builder is available under `gcr.io/buildpacks/builder:google-24`. For more information, see [Builders](https://docs.cloud.google.com/docs/buildpacks/builders).

## February 11, 2026

Feature

Support for [osonly24 runtime](https://docs.cloud.google.com/run/docs/runtime-support#osonly) is in [General Availability](https://cloud.google.com/products#product-launch-stages). The OS only runtime lets you deploy binaries such as Dart and Go. For more information, see [Configure the OS only runtime](https://docs.cloud.google.com/docs/buildpacks/osonly).

## February 06, 2026

Feature

Expanded coverage for compute flexible committed use discounts (CUDs) is available to all Cloud Billing accounts. Your Cloud Billing accounts have been automatically migrated to the [new spend-based CUD model](https://docs.cloud.google.com/docs/cuds-multiprice) and you no longer need to opt-in to benefit from the expanded coverage. For the full list of eligible SKUs across Compute Engine, GKE, and Cloud Run, see [SKU Groups - Compute Flexible CUD Eligible SKUs](https://cloud.google.com/skus/sku-groups/compute-flexible-cud-eligible-skus).

To learn more about compute flexible CUDs for Cloud Run and how they apply to your usage, see the [compute flexible CUDs documentation](https://docs.cloud.google.com/run/cud).

## February 05, 2026

Feature

You can configure [Direct VPC ingress for Cloud Run worker pools](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#direct-vpc-workerpool). When you configure Direct VPC ingress, each worker instance receives a private IP address on your configured network and subnet. To access private IP addresses between instances in your VPC network for secure internal communication, see [Retrieve the private IP addresses using the metadata server (MDS)](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#mds-support). 

## February 02, 2026

Feature

Support for NVIDIA RTX PRO 6000 Blackwell GPU is in [Preview](https://cloud.google.com/products#product-launch-stages). For more information, see GPU support for [services](https://docs.cloud.google.com/run/docs/configuring/services/gpu), [jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/gpu), and [worker pools](https://docs.cloud.google.com/run/docs/configuring/workerpools/gpu).

Feature

Support for [PHP 8.5 runtime](https://docs.cloud.google.com/run/docs/runtime-support#php) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## January 27, 2026

Feature

Support for [.NET 10 runtime](https://docs.cloud.google.com/run/docs/runtime-support#.net) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## January 22, 2026

Feature

The Python buildpack supports default entrypoint detection for the [Agent Development Kit (ADK) framework](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-adk-service) in [General Availability](https://cloud.google.com/products#product-launch-stages). For more information, see [Build a Python application](https://docs.cloud.google.com/docs/buildpacks/python#entrypoint).

## January 20, 2026

Feature

The following new region is now available: `asia-southeast3`.

## January 13, 2026

Feature

Cloud Run and Cloud Run functions source deployments support the `pyproject.toml` file for managing dependencies. This feature is in [General Availability](https://cloud.google.com/products#product-launch-stages) for all [supported Python versions](https://docs.cloud.google.com/run/docs/runtime-support#python). For more information, see [Deploy Python applications with a `pyproject.toml` file](https://docs.cloud.google.com/docs/buildpacks/python#deploy-with-toml).

## December 22, 2025

Feature

Support for [Java 25 runtime](https://docs.cloud.google.com/run/docs/runtime-support#java) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## December 19, 2025

Feature

Support for [Python 3.14 runtime](https://docs.cloud.google.com/run/docs/runtime-support#python) is in [General Availability](https://cloud.google.com/products#product-launch-stages). Starting from Python version 3.14 and later, the Python buildpack uses the uv package manager as the default installer for the dependencies you specify in your `requirements.txt` file. You can also use pip as the default installer for these versions by setting the `GOOGLE_PYTHON_PACKAGE_MANAGER` environment variable to `pip`. For more information, see [Specify dependencies in Python](https://docs.cloud.google.com/run/docs/runtimes/python-dependencies#dependencies).

Feature

Cloud Run and Cloud Run functions source deployments support `pyproject.toml` file for managing dependencies. This feature is in General Availability for Python version 3.13 and later, and is in Preview for Python version 3.12 and earlier. For more information, see [Deploy Python applications with a `pyproject.toml` file](https://docs.cloud.google.com/docs/buildpacks/python#deploy-with-toml).

Feature

The Python buildpack supports default entrypoint detection for the [Agent Development Kit (ADK) framework](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-adk-service) (Preview). For more information, see [Build a Python application](https://docs.cloud.google.com/docs/buildpacks/python#entrypoint).

## December 18, 2025

Feature

Support for [osonly24 runtime](https://docs.cloud.google.com/run/docs/runtime-support#osonly) is in [Preview](https://cloud.google.com/products#product-launch-stages). The OS only runtime lets you deploy Go applications from source, and binaries such as Dart and Go. For more information, see [Configure the OS only runtime](https://docs.cloud.google.com/docs/buildpacks/osonly).

## December 01, 2025

Feature

You can use [Developer Connect in the Cloud Run console](https://docs.cloud.google.com/run/docs/continuous-deployment) to set up continuous deployments from GitHub, GitLab, and Bitbucket repositories (Preview).

## November 21, 2025

Feature

Deploy a highly available, multi-region Cloud Run service with automated failover and failback for internal traffic using [Cloud Run service health](https://docs.cloud.google.com/run/docs/multiple-regions#service-health) (Preview).

Feature

[Configure HTTP and gRPC readiness probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks#readiness-probes) for your Cloud Run services (Preview).

## November 20, 2025

Feature

Support for [Node.js 24 runtime](https://docs.cloud.google.com/static/run/docs/runtime-support#node.js) is in [General Availability](https://cloud.google.com/products#product-launch-stages).

## November 19, 2025

Feature

You can [deploy source artifacts directly to Cloud Run](https://docs.cloud.google.com/run/docs/deploying-source-code#deploy_from_source_without_build), bypassing the Cloud Build step. (Preview)

## November 17, 2025

Feature

Cloud Run and Cloud Run functions source deployments support `pyproject.toml` file for managing dependencies. If you use a `pyproject.toml` file, source deployments use one of the following to find and install dependencies:

  * `pip`
  * `uv`
  * `poetry`



For more information, see [Deploy Python applications with a `pyproject.toml` file](https://docs.cloud.google.com/docs/buildpacks/python#deploy-with-toml) (Preview).

Feature

The time it takes for initial deployments to Cloud Run in a new project has been reduced. This change results in reduced latency and a faster getting started experience.

## November 13, 2025

Feature

You can deploy services to Cloud Run [using a Compose file](https://docs.cloud.google.com/run/docs/deploy-run-compose) (Preview).

## November 12, 2025

Feature

Support for [Python 3.14 runtime](https://docs.cloud.google.com/run/docs/runtime-support#python) is in [Preview](https://cloud.google.com/products#product-launch-stages). Starting from Python version 3.14 and later, the Python buildpack uses the uv package manager as the default installer for the dependencies you specify in your `requirements.txt` file. You can also use pip as the default installer for these versions by setting the `GOOGLE_PYTHON_PACKAGE_MANAGER` environment variable to `pip`. For more information, see [Specify dependencies in Python](https://docs.cloud.google.com/run/docs/runtimes/python-dependencies#dependencies).

Feature

Cloud Run [source deployment](https://docs.cloud.google.com/run/docs/deploying-source-code) supports Ubuntu 24 LTS base images (Preview). This builder is available under `gcr.io/buildpacks/builder:google-24`. For more information, see [Builders](https://docs.cloud.google.com/docs/buildpacks/builders).

## November 11, 2025

Feature

You can set a [task timeout](https://docs.cloud.google.com/run/docs/configuring/task-timeout) up to 168 hours (7 days) for Cloud Run jobs. (GA)

## November 06, 2025

Feature

Use [dual-stack subnets with IPv6](https://docs.cloud.google.com/run/docs/configuring/vpc-dual-stack-subnet) to let your Cloud Run resources send IPv4 and internal IPv6 traffic to a VPC network with Direct VPC egress, and send external IPv6 traffic to the public internet. (GA)

## October 31, 2025

Feature

Support for [Java 25 runtime](https://docs.cloud.google.com/run/docs/runtime-support#java) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## October 30, 2025

Feature

For Cloud Run source deployed services and functions with [GPU enabled](https://docs.cloud.google.com/run/docs/configuring/services/gpu), Cloud Run defaults to using Cloud Build's `e2-highcpu-8 machine` type for the build process when using the gcloud CLI or the Google Cloud console. This change allows for higher CPU support and faster build times, and also leads to a moderate increase in the overall cost of your service (GA).

## October 21, 2025

Feature

Support for [configuring GPU](https://docs.cloud.google.com/run/docs/configuring/jobs/gpu) for your Cloud Run job is in General Availability (GA).

Feature

[Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) now supports [Private NAT](https://docs.cloud.google.com/nat/docs/private-nat) (GA).

## October 20, 2025

Feature

Direct VPC egress now supports [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records) (Preview).

## October 06, 2025

Feature

Support for [applying maximum instance configuration](https://docs.cloud.google.com/run/docs/configuring/max-instances#service-vs-revision-level) at the service level is in General Availability (GA).

## September 24, 2025

Feature

Support for setting multiple environment variables using the `.env` file is in General Availability (GA). For more information, see [Configure environment variables for services](https://docs.cloud.google.com/run/docs/configuring/services/environment-variables#set_multiple_environment_variables), [jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/environment-variables#set_multiple_environment_variables), and [worker pools](https://docs.cloud.google.com/run/docs/configuring/workerpools/environment-variables#set_multiple_environment_variables).

## September 23, 2025

Feature

You can specify mount options when you configure Cloud Storage volume mounts for Cloud Run [services](https://docs.cloud.google.com/run/docs/configuring/services/cloud-storage-volume-mounts), [jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/cloud-storage-volume-mounts), and [worker pools](https://docs.cloud.google.com/run/docs/configuring/workerpools/cloud-storage-volume-mounts). (GA)

## September 10, 2025

Feature

You can deploy and configure a [multi-region service](https://docs.cloud.google.com/run/docs/multiple-regions#deploy) from a single gcloud CLI command or by using a YAML or Terraform file (GA).

Feature

[Cloud Run Threat Detection](https://docs.cloud.google.com/run/docs/securing/cloud-run-threat-detection) is available in [General Availability](https://cloud.google.com/products#product-launch-stages).

## September 03, 2025

Feature

You can [configure GPU](https://docs.cloud.google.com/run/docs/configuring/workerpools/gpu) in your Cloud Run worker pool (Preview).

## August 21, 2025

Feature

Support for [Go 1.25 runtime](https://docs.cloud.google.com/run/docs/runtime-support#go) is in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

## August 20, 2025

Feature

For Cloud Run source deployed services and functions with [GPU enabled](https://docs.cloud.google.com/run/docs/configuring/services/gpu), Cloud Run defaults to using Cloud Build's `e2-highcpu-8` machine type for the build process when you use the `gcloud beta run` command (Preview). This change allows for higher CPU support and faster build times, and also leads to a moderate increase in the overall cost of your service.

## August 14, 2025

Feature

The Python buildpack supports Cloud Run source deployments for modern web frameworks such as [FastAPI](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-fastapi-service), [Gradio](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-gradio-service), and [Streamlit](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-streamlit-service).

For Python version 3.13 and later, the Python buildpack sets the default entrypoint for [Cloud Run source deployments](https://docs.cloud.google.com/run/docs/deploying-source-code) based on the web server or framework configuration in your `requirements.txt` file. For more information, see [Build a Python application](https://docs.cloud.google.com/docs/buildpacks/python#entrypoint).

## August 13, 2025

Feature

You can set multiple environment variables using the `.env` file (Preview). For more information, see [Configure environment variables for services](https://docs.cloud.google.com/run/docs/configuring/services/environment-variables#set_multiple_environment_variables), [jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/environment-variables#set_multiple_environment_variables), and [worker pools](https://docs.cloud.google.com/run/docs/configuring/workerpools/environment-variables#set_multiple_environment_variables).

## August 05, 2025

Feature

Support for [manually scaling your Cloud Run service](https://docs.cloud.google.com/run/docs/configuring/services/manual-scaling) is now at General Availability (GA).

## July 30, 2025

Feature

Support for [Go 1.25 runtime](https://docs.cloud.google.com/run/docs/runtime-support#go) is in [Preview](https://cloud.google.com/products#product-launch-stages). This runtime is available for early testers using existing [release candidates](https://go.dev/dl/#unstable).

Feature

Support for [Node.js 24 runtime](https://docs.cloud.google.com/static/run/docs/runtime-support#node.js) is in [Preview](https://cloud.google.com/products#product-launch-stages). Node.js 24 is in the Current release state and enters long-term support (LTS) in October 2025\. For more information, see [Node.js v24.0.0 (Current) ](https://nodejs.org/en/blog/release/v24.0.0) in the Node.js website.

Feature

Support for [Go 1.24 runtime](https://docs.cloud.google.com/run/docs/runtime-support#go) is in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

## July 16, 2025

Feature

You can [disable the built-in `run.app` URL](https://docs.cloud.google.com/run/docs/securing/ingress) of a Cloud Run service to ensure that traffic can only ingress through paths that you've explicitly configured ([GA](https://cloud.google.com/products#product-launch-stages)).

## July 15, 2025

Feature

Compute flexible committed use discounts (CUDs) have expanded to also cover your Cloud Billing account's spend across Cloud Run services with request-based billing and Cloud Run functions.

The [improved spend-based CUD experience](https://docs.cloud.google.com/docs/cuds-multiprice) is available without requiring an opt-in for new users or users who don't have an active spend-based CUD.

To learn more about how opting into the new model affects your flexible CUDs, see [Committed use discounts](https://docs.cloud.google.com/run/cud).

Feature

Support for the [Go 1.24 runtime](https://docs.cloud.google.com/run/docs/runtime-support#go) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## June 30, 2025

Feature

You can [apply maximum instance configuration](https://docs.cloud.google.com/run/docs/configuring/max-instances#service-vs-revision-level) at the service level (in Preview).

## June 25, 2025

Feature

Cloud Run [worker pools](https://docs.cloud.google.com/run/docs/deploy-worker-pools) are now available (Preview). Worker pools are specifically designed for non-request workloads.

## June 24, 2025

Feature

A new region is now available for [Cloud Run GPUs](https://docs.cloud.google.com/run/docs/configuring/services/gpu#supported-regions): `us-east4`.

## June 17, 2025

Feature

Support for the [PHP 8.4 runtime](https://docs.cloud.google.com/run/docs/runtime-support#php) is in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

Feature

Support for the [Ruby 3.4 runtime](https://docs.cloud.google.com/run/docs/runtime-support#ruby) is in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

## June 16, 2025

Feature

You can [configure GPU](https://docs.cloud.google.com/run/docs/configuring/jobs/gpu) in your Cloud Run job (Preview).

## June 09, 2025

Feature

You can [use request host and request path in IAM Conditions](https://docs.cloud.google.com/run/docs/securing/managing-access#conditions) when defining access control for invoking Cloud Run services.

## May 30, 2025

Feature

For Java Cloud Run functions that use `functions-framework` version 1.4.0 or later, you can now use the logging class `java.util.logging.Logger` to add a [unique execution ID](https://docs.cloud.google.com/run/docs/runtimes/java#execution_id) to log outputs.

## May 28, 2025

Feature

Multiple regions now benefit from enhanced responsiveness for latency-sensitive applications for [Cloud Run service URLs](https://docs.cloud.google.com/run/docs/triggering/https-request#url).

## May 15, 2025

Change

The region selector when creating a service or a job from the Google Cloud console now defaults to `europe-west1`.

## May 13, 2025

Feature

Labels you previously set for your Cloud Run functions using either `gcloud functions` commands or the Cloud Functions v2 API propagate to Cloud Run when you [deploy your functions in Cloud Run](https://docs.cloud.google.com/run/docs/deploy-functions). For more information on creating labels in Cloud Run, see [Configure labels for services](https://docs.cloud.google.com/run/docs/configuring/services/labels#set-labels).

## May 06, 2025

Feature

[Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) supports [Private NAT](https://docs.cloud.google.com/nat/docs/private-nat) ([Preview](https://cloud.google.com/products#product-launch-stages)).

Change

The Cloud Monitoring [memory usage metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-run) now show lower memory utilization for most services using the second generation execution environment. These metrics previously included memory used by the operating system page cache.

## May 05, 2025

Feature

Support for the [Python 3.13 runtime](https://docs.cloud.google.com/run/docs/runtime-support#python) is in [General Availability (GA)](https://cloud.google.com/products#product-launch-stages).

Feature

Support for the [PHP 8.4 runtime](https://docs.cloud.google.com/run/docs/runtime-support#php) is in [Preview](https://cloud.google.com/products#product-launch-stages).

Feature

Support for the [Ruby 3.4 runtime](https://docs.cloud.google.com/run/docs/runtime-support#ruby) is in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 22, 2025

Feature

[Cloud KMS with Autokey](https://docs.cloud.google.com/run/docs/securing/using-cmek#use-autokey) is now in General Availability (GA) for Cloud Run.

## April 21, 2025

Feature

Support for the [Python 3.13 runtime](https://docs.cloud.google.com/run/docs/runtime-support#python) is now in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 09, 2025

Feature

Gemini Cloud Assist in Cloud Run is supported in [Preview](https://cloud.google.com/products#product-launch-stages). You can use the chat panel to [design](https://docs.cloud.google.com/run/docs/developing#design-with-gemini-cloud-assist), [optimize](https://docs.cloud.google.com/run/docs/recommender#optimize-with-gemini-cloud-assist), and [troubleshoot](https://docs.cloud.google.com/run/docs/troubleshooting/overview#troubleshoot-with-gemini-cloud-assist) your Cloud Run apps with Gemini assistance.

## April 07, 2025

Feature

Direct VPC egress support for [Cloud Run jobs](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#direct-vpc-job) is now generally available (GA).

Feature

You can now [configure Identity-Aware Proxy (IAP) for Cloud Run](https://docs.cloud.google.com/run/docs/securing/identity-aware-proxy-cloud-run) to secure your services with a single click from all ingress paths (in Preview).

Feature

[Configuring GPU](https://docs.cloud.google.com/run/docs/configuring/services/gpu) in your Cloud Run service is now generally available (GA).

Feature

[Cloud Run Threat Detection](https://docs.cloud.google.com/run/docs/securing/cloud-run-threat-detection) is available in [Preview](https://cloud.google.com/products#product-launch-stages).

## April 02, 2025

Feature

Deploying [multiple containers (sidecars)](https://docs.cloud.google.com/run/docs/create-jobs#sidecars) to a Cloud Run job is now generally available. (GA)

## March 28, 2025

Feature

The ability to [disable the Invoker IAM check](https://docs.cloud.google.com/run/docs/securing/managing-access#invoker_check) for Cloud Run services is now at general availability (GA).

## March 26, 2025

Change

Cloud Run services configured with Direct VPC egress now use only [2 times (2X) as many IP addresses as the number of instances](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#ip-consumption-services) for the duration of the instance plus up to 20 minutes, reduced from 4X as many IP addresses.

## March 25, 2025

Feature

New services using GPUs by default will have zonal redundancy turned on. However, you can now [specify GPUs with zonal redundancy or without zonal redundancy](https://docs.cloud.google.com/run/docs/configuring/services/gpu-zonal-redundancy), and request quota for either of these configurations. (In Preview)

## March 11, 2025

Feature

A new region is now available for [Cloud Run GPUs](https://docs.cloud.google.com/run/docs/configuring/services/gpu#supported-regions): `europe-west1`.

## March 06, 2025

Feature

The following new region is now available: `europe-north2`.

## March 04, 2025

Feature

The following new region is now available: `northamerica-south1`.

## March 03, 2025

Feature

Support for the [Go 1.23 runtime](https://docs.cloud.google.com/run/docs/runtime-support#go) is now in general availability (GA).

## February 19, 2025

Feature

Support for [deploying functions](https://docs.cloud.google.com/run/docs/deploy-functions) in Cloud Run is now in general availability (GA). Note that you must use Google Cloud SDK 511.0.0 version or later if using the gcloud CLI. Review the [use cases](https://docs.cloud.google.com/run/docs/functions-with-run) guide for deploying new functions.

Feature

Support for configuring [automatic base image updates](https://docs.cloud.google.com/run/docs/configuring/services/automatic-base-image-updates) for Cloud Run source deployed services and functions is now in general availability (GA). Note that you must use Google Cloud SDK 511.0.0 version or later if using the gcloud CLI.

## February 18, 2025

Feature

You can now [scale your Cloud Run service manually](https://docs.cloud.google.com/run/docs/configuring/services/manual-scaling), in place of the [built-in Cloud Run autoscaling feature](https://docs.cloud.google.com/run/docs/about-instance-autoscaling). (Preview)

## February 07, 2025

Change

Cloud Run integrations are discontinued from the Google Cloud console and Google Cloud CLI. No action is required; your deployed services that use these integrations will continue to work. We recommend transitioning to use the individual product experiences for each integration you have deployed. For more information about configuring resources for your services to connect to other Google Cloud products, see [Connect to Google Cloud services](https://docs.cloud.google.com/run/docs/integrate/using-gcp-services).

## February 04, 2025

Feature

When deploying a function in Cloud Run, you can now [specify an Artifact Registry image repository](https://docs.cloud.google.com/run/docs/deploy-functions#specify-image-repository) to store the container (Preview).

## January 24, 2025

Feature

You can now use [dual-stack subnets with internal IPv6](https://docs.cloud.google.com/run/docs/configuring/vpc-dual-stack-subnet) to let your Cloud Run services and jobs send IPv4 and internal IPv6 traffic to a VPC network with Direct VPC egress. (Preview)

## January 22, 2025

Feature

The [Cloud Run Builder](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.builder) (`roles/run.builder`) IAM role is now available in preview. When deploying a service or function from [source](https://docs.cloud.google.com/run/docs/resource-model#source), grant this role to the Compute Engine default service account that builds your Cloud Run resource.

## January 14, 2025

Feature

You can now deploy [multiple containers (sidecars)](https://docs.cloud.google.com/run/docs/create-jobs#sidecars) to a Cloud Run job. (In Preview)

## January 13, 2025

Breaking

The principal (user or service account) creating or updating a Cloud Run resource now needs explicit permission to access the container image(s). When using Artifact Registry, [ensure the principal has the Artifact Registry Reader (`roles/artifactregistry.reader`) IAM role](https://docs.cloud.google.com/artifact-registry/docs/access-control#grant) on the project or repository containing the container image(s) to deploy.

## December 17, 2024

Feature

New finer-grained [predefined IAM roles are available for Cloud Run](https://docs.cloud.google.com/run/docs/reference/iam/roles): Cloud Run Service Invoker, Cloud Run Jobs Executor, Cloud Run Jobs Executor With Overrides. These roles make it easier to grant least privilege access to production accounts accessing Cloud Run resources.

## December 16, 2024

Change

[Service-level minimum instances](https://docs.cloud.google.com/run/docs/configuring/min-instances#setting) are now set using the `--min` command line flag, `--service-min-instances` remains available as an alias to `--min`.

## December 13, 2024

Change

The _CPU allocation_ setting has been renamed to _Billing_ in the Google Cloud console for Cloud Run services. 

The two billing settings are:

  * Request-based billing (default), previously called _CPU is only allocated during request processing_ , only charges your Cloud Run instances during request processing, container startup, and container shutdown. 
  * Instance-based billing, previously called _CPU always allocated_ , charges your Cloud Run instances for the entire lifecycle of instances, even when there are no incoming requests.



For more details, see the [Billing settings](https://docs.cloud.google.com/run/docs/configuring/billing-settings) guide.

## December 09, 2024

Feature

You can now create [custom organization policies](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access#custom-constraints) for Serverless VPC Access connectors and apply them to projects, folders, or organizations (GA).

## November 25, 2024

Feature

You can now set a [task timeout](https://docs.cloud.google.com/run/docs/configuring/task-timeout) up to 168 hours (7 days) for Cloud Run jobs. (Preview)

## November 19, 2024

Feature

Support for the [Go 1.23 runtime](https://docs.cloud.google.com/run/docs/runtime-support#go) is now in Preview.

## November 18, 2024

Feature

Support for the [Node.js 22 runtime](https://docs.cloud.google.com/static/run/docs/runtime-support#node.js) is now in general availability (GA).

## November 15, 2024

Feature

Cloud Run is now in scope for [International Traffic in Arms Regulations (ITAR)](https://cloud.google.com/security/compliance/itar).

Change

`asia-south1` (Mumbai, India) is now subject to [Tier 1 pricing](https://cloud.google.com/run/pricing#tables).

## November 12, 2024

Feature

The _in-memory_ volume type is now generally available (GA) for Cloud Run [services](https://docs.cloud.google.com/run/docs/configuring/services/in-memory-volume-mounts) and [jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/in-memory-volume-mounts).

## November 07, 2024

Feature

You can now specify mount options when you configure Cloud Storage volume mounts for both Cloud Run [services](https://docs.cloud.google.com/run/docs/configuring/services/cloud-storage-volume-mounts#specify-mount-options) and [jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/cloud-storage-volume-mounts#specify-mount-options). (In Preview)

## October 23, 2024

Feature

[GPU support (Preview)](https://docs.cloud.google.com/run/docs/configuring/services/gpu) is now available in the following region: `europe-west4`.

## October 21, 2024

Feature

You can now create [custom organization policies](https://docs.cloud.google.com/run/docs/securing/custom-constraints) and apply them to projects, folders, or organizations (GA).

Announcement

Cloud Run integrations are discontinued from the Google Cloud console and Google Cloud CLI for new users. If you are an existing user, you will continue to have access until January 2025. No action is required, your deployed services that use these integrations will continue to work. We recommend transitioning to use the individual product experiences for each integration you have deployed. For more information about configuring resources for your services to connect to other Google Cloud products, see [Connect to Google Cloud services](https://docs.cloud.google.com/run/docs/integrate/using-gcp-services).

## October 10, 2024

Feature

You can now deploy and configure a [multi-region service](https://docs.cloud.google.com/run/docs/multiple-regions) from a single gcloud CLI command (in Preview).

## October 01, 2024

Feature

[Service-level minimum instances](https://docs.cloud.google.com/run/docs/configuring/min-instances#service-vs-revision-level) are now generally available (GA).

## September 24, 2024

Feature

[GPU support (Preview)](https://docs.cloud.google.com/run/docs/configuring/services/gpu) is now available in the following region: `asia-southeast1`.

## September 23, 2024

Change

The [runtime support schedule for some PHP runtimes](https://docs.cloud.google.com/run/docs/runtime-support#php) has been extended to match [PHP's public support schedule](https://www.php.net/supported-versions.php).

## September 17, 2024

Feature

The [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) feature of Cloud Run now supports [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview).

## September 16, 2024

Feature

You can now [apply custom constraints for projects](https://docs.cloud.google.com/run/docs/securing/custom-constraints) that get enforced by organization policies on your Cloud Run services and jobs (in Preview).

## September 03, 2024

Feature

[Deterministic URLs](https://docs.cloud.google.com/run/docs/triggering/https-request#deterministic), which let you predict a Cloud Run service URL before the service is created, is now in general availability (GA).

## August 27, 2024

Feature

The following Cloud Run volume types are now generally available (GA):

  * Mounting an NFS file share as a volume for Cloud Run [services](https://docs.cloud.google.com/run/docs/configuring/services/nfs-volume-mounts) and [jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/nfs-volume-mounts) .
  * Mounting a Cloud Storage bucket as a storage volume for Cloud Run [services](https://docs.cloud.google.com/run/docs/configuring/services/cloud-storage-volume-mounts) and [jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/cloud-storage-volume-mounts).



## August 26, 2024

Feature

You can now configure traffic routing between Cloud Run and Cloud Run, Google Kubernetes Engine, and Google Compute Engine services using [Cloud Service Mesh service routing APIs](https://docs.cloud.google.com/service-mesh/docs/configure-cloud-service-mesh-for-cloud-run). Cloud Run also automatically authenticates calls to destination services using service account credentials (In Preview).

## August 22, 2024

Feature

Cloud Run is now supported by [Sovereign Controls by Partners](https://docs.cloud.google.com/sovereign-controls-by-partners/docs/overview). The set of packages and features provided by Sovereign Controls by Partners lets you use Cloud Run while meeting digital sovereignty requirements and managing your workloads with data sovereignty guarantees.

## August 21, 2024

Feature

Cloud Run now provides security updates for services that are deployed from source when you specify the [runtime base image](https://docs.cloud.google.com/run/docs/configuring/services/runtime-base-images) (Preview). Automatic security updates are enabled by default for functions. For details, see [Configure automatic base image updates](https://docs.cloud.google.com/run/docs/configuring/services/automatic-base-image-updates).

Feature

You can now [configure GPU](https://docs.cloud.google.com/run/docs/configuring/services/gpu) in your Cloud Run service (Preview).

Feature

You can now [deploy functions](https://docs.cloud.google.com/run/docs/deploy-functions) in Cloud Run (Preview). Functions that were created using the [Cloud Functions v2 API](https://docs.cloud.google.com/functions/docs/apis) can now be directly updated in Cloud Run. Note that you must use Google Cloud SDK 489.0.0 version or later if using the gcloud CLI.

Learn more about the different [use cases](https://docs.cloud.google.com/run/docs/functions-with-run) for deploying functions.

## July 18, 2024

Feature

You can now [disable the default `run.app` URL](https://docs.cloud.google.com/run/docs/securing/ingress#disable-url) for your Cloud Run services (Preview).

## July 15, 2024

Feature

Compute flexible committed use discounts are now available for Cloud Run services with [CPU always allocated](https://docs.cloud.google.com/run/docs/configuring/cpu-allocation#choosing), and Cloud Run jobs. A single flexible commitment covers eligible spend across Compute Engine, GKE, and Cloud Run. For more information, see [Committed use discounts](https://docs.cloud.google.com/run/cud).

## July 11, 2024

Announcement

Starting July 2024, Cloud Build changed the default behavior for how Cloud Build uses service accounts in new projects. This change is detailed in [Cloud Build Service Account Change](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates) documentation. As a result of this change, new projects [deploying to Cloud Run from source code](https://docs.cloud.google.com/run/docs/deploying-source-code) for the first time may be using a default Cloud Build service account with [insufficient permissions](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-service-accounts#disable_service_account_default_grants) for deploying from source.

If you are impacted by this change, you can do one of the following:

  * Review the Cloud Build guidance on changes to the default service account and [opt out of these changes](https://docs.cloud.google.com/build/docs/cloud-build-service-account-updates#what_do_you_need_to_do).
  * Grant the [Cloud Build Service Account](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudbuild#cloudbuild.builds.builder) (`roles/cloudbuild.builds.builder`) role to the Compute Engine default service account.



## June 27, 2024

Feature

The following IAM roles are now available in preview:

  * [Cloud Run Source Developer (`roles/run.sourceDeveloper`)](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.sourceDeveloper) for deploying a Cloud Run service or job from source.
  * [Cloud Run Source Viewer (`roles/run.sourceViewer`)](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.sourceViewer) viewing a Cloud Run service or job that is deployed from source.



## May 20, 2024

Feature

[Uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks) can now be configured and viewed directly within the Cloud Run "metrics" page.

## May 17, 2024

Feature

Cloud Run is now covered by [FedRAMP High](https://cloud.google.com/security/compliance/fedramp).

## May 15, 2024

Feature

Cloud Run has been added to [Google Cloud's Pricing Calculator](https://cloud.google.com/products/calculator).

## April 24, 2024

Feature

Support for [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc), which lets you send traffic directly to a VPC network with no Serverless VPC Access connector required, is now at general availability (GA).

## April 15, 2024

Feature

The [Direct VPC egress feature](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) of Cloud Run is now supported in all [regions](https://docs.cloud.google.com/run/docs/locations).

## March 28, 2024

Change

All jobs are now subject to [maintenance events](https://docs.cloud.google.com/run/docs/configuring/task-timeout#observing_and_handling_maintenance_events), not just jobs longer than one hour, which increases reliability for jobs under 1 hour. These maintenance events are transparent and don't require any changes to your container.

## March 22, 2024

Feature

Direct VPC egress (Preview) is now available in the following additional [regions](https://docs.cloud.google.com/run/docs/locations#direct):

  * `africa-south1`
  * `asia-south1`
  * `asia-southeast2`
  * `australia-southeast2`
  * `europe-central2`
  * `europe-west2`
  * `europe-west6`
  * `europe-west8`
  * `europe-west9`
  * `europe-west10`
  * `me-central1`
  * `me-central2`
  * `southamerica-west1`
  * `us-east5`
  * `us-west2`
  * `us-west3`
  * `us-west8`



Feature

Cloud Run services can now [connect to Vertex AI to access generative AI models](https://docs.cloud.google.com/run/docs/integrate/vertex-ai) using integrations (Preview).

Feature

Cloud Run services can now [connect to a Firestore database](https://docs.cloud.google.com/run/docs/integrate/firestore) using integrations (Preview).

## March 19, 2024

Feature

You can now mount an NFS file share as a volume for Cloud Run [services](https://docs.cloud.google.com/run/docs/configuring/services/nfs-volume-mounts) and [jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/nfs-volume-mounts). (In Preview)

## March 14, 2024

Feature

[Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) now supports Cloud NAT with [Public NAT](https://docs.cloud.google.com/nat/docs/public-nat) IP addresses (in Preview).

## March 07, 2024

Feature

Charts on the [metrics dashboard of Cloud Run services](https://docs.cloud.google.com/run/docs/monitoring#service-metrics) now display deployment events.

## March 05, 2024

Feature

You can now [apply minimum instance configuration](https://docs.cloud.google.com/run/docs/configuring/min-instances#service-vs-revision-level) at the service level (in Preview).

## February 13, 2024

Feature

You can now set and override the [deployment service account for Cloud Run integrations](https://docs.cloud.google.com/run/docs/integrate#service_accounts) when creating, updating, or deleting integrations using the Google Cloud CLI.

## January 31, 2024

Feature

The following new region is now available: `africa-south1`.

## January 23, 2024

Feature

The option to [update a Serverless VPC Access connector](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#update-connector) is now available at general availability (GA). This feature allows you to edit the machine (instance) type, as well as the minimum and maximum number of instances.

## January 19, 2024

Feature

You can now [mount a Cloud Storage bucket as a storage volume](https://docs.cloud.google.com/run/docs/configuring/services/cloud-storage-volume-mounts) for services, and also for [Cloud Run jobs](https://docs.cloud.google.com/run/docs/configuring/jobs/cloud-storage-volume-mounts).

## January 18, 2024

Feature

Direct VPC egress (Preview) is now available in the following additional [regions](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc#regions): 

  * `asia-east1`
  * `asia-east2`
  * `asia-northeast2`
  * `asia-south2`
  * `australia-southeast1`
  * `europe-north1`
  * `europe-southwest1`
  * `europe-west12`
  * `europe-west4`
  * `me-west1`
  * `northamerica-northeast1`
  * `northamerica-northeast2`
  * `southamerica-east1`
  * `us-east4`
  * `us-south1`
  * `us-west1`
  * `us-west4`



## January 10, 2024

Change

[Tags](https://docs.cloud.google.com/run/docs/configuring/tags) configured on Cloud Run services are now available when [exporting Cloud Billing data to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).

## December 18, 2023

Feature

For revisions that have CPU allocation set to CPU always on, instance autoscaling now occurs for CPU activity even outside of incoming requests.

## December 15, 2023

Feature

You can now collect [Prometheus metrics](https://prometheus.io/docs/introduction/overview) from Cloud Run services by using the [Managed Service for Prometheus sidecar for Cloud Run](https://docs.cloud.google.com/run/docs/monitoring-managed-prometheus-sidecar).

## November 17, 2023

Feature

For services with cold start times exceeding 10 seconds, requests are now queued for at least the cold start time before timing out while waiting for instances to start.

## November 14, 2023

Feature

[Cancelling a currently running job execution](https://docs.cloud.google.com/run/docs/execute/jobs#cancel-job-execution) is now at general availability (GA).

## November 13, 2023

Feature

[Deploying sidecar containers](https://docs.cloud.google.com/run/docs/deploying#sidecars) to your Cloud Run service is now at general availability (GA). Console UI and CLI are also now available for this feature.

## November 08, 2023

Feature

[Setting custom audiences](https://docs.cloud.google.com/run/docs/configuring/custom-audiences) on your Cloud Run services is now at general availability (GA).

## October 31, 2023

Feature

Job [overrides](https://docs.cloud.google.com/run/docs/execute/jobs#override-job-configuration) are now at general availability (GA). This feature lets you override the arguments, environment variables, number of tasks, and task timeouts already configured for a job when you execute a job.

## October 11, 2023

Feature

[Shared VPC ingress](https://docs.cloud.google.com/run/docs/securing/private-networking#shared-vpc) is now at general availability (GA). Shared VPC traffic is now considered "internal" for Cloud Run services that are connected to the Shared VPC network.

## September 27, 2023

Feature

[Long running jobs](https://docs.cloud.google.com/run/docs/configuring/task-timeout#long-task-timeout) greater than 1 hour are at general availability (GA).

## September 21, 2023

Feature

Cloud Run [integrations](https://docs.cloud.google.com/run/docs/integrate/using-gcp-services#integrations) (Preview) are now available in the following [regions](https://docs.cloud.google.com/run/docs/locations#integrations): 

  * `asia-northeast1`
  * `asia-northeast2`
  * `asia-south1`
  * `asia-southeast2`
  * `australia-southeast1`
  * `europe-central2`
  * `europe-north1`
  * `europe-west2`
  * `europe-west3`
  * `northamerica-northeast1`
  * `southamerica-east1`
  * `us-east4`
  * `us-west2`
  * `us-west3`



## September 19, 2023

Feature

The following new region is now available: `me-central2`.

## September 18, 2023

Feature

[Cloud Run Operators](https://airflow.apache.org/docs/apache-airflow-providers-google/stable/operators/cloud/cloud_run.html) are available in [Cloud Composer](https://cloud.google.com/products/managed-service-for-apache-airflow).

## August 25, 2023

Feature

You can now [cancel a currently running job execution](https://docs.cloud.google.com/run/docs/execute/jobs#cancel-job-execution). (In Preview.)

## August 22, 2023

Feature

The following new region is now available: `europe-west10`.

## August 14, 2023

Feature

You can now [send traffic directly](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) to a VPC network with no Serverless VPC Access connector required (Preview).

## August 08, 2023

Feature

You can now [override](https://docs.cloud.google.com/run/docs/execute/jobs#override-job-configuration) the arguments, environment variables, number of tasks, and task timeout already configured for a job when you execute a job. (In Preview)

## August 03, 2023

Change

Accessing a service that's prohibited by the **Internal** or **Internal and Cloud Load Balancing** [ingress setting](https://docs.cloud.google.com/run/docs/securing/ingress#settings) now results in a `404` rather than `403` error code.

## July 05, 2023

Feature

[Long running jobs](https://docs.cloud.google.com/run/docs/configuring/task-timeout#long-task-timeout) greater than 1 hour are now supported (in Preview).

## June 09, 2023

Feature

You can now create and then [configure a Serverless VPC Access connector](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc#configuring) for your service or job directly from the _Create_ form in the Google Cloud console. (Preview)

## May 17, 2023

Feature

[Allocating up to 32 GiB of memory](https://docs.cloud.google.com/run/docs/configuring/memory-limits#max) and [up to 8 CPU](https://docs.cloud.google.com/run/docs/configuring/cpu#setting) to your Cloud Run services is now at general availability (GA).

## May 12, 2023

Feature

You can now [deploy sidecar containers](https://docs.cloud.google.com/run/docs/deploying#sidecars) to your Cloud Run service. (In Preview.)

Feature

You can now configure [in-memory volumes](https://docs.cloud.google.com/run/docs/configuring/in-memory-volumes) for your Cloud Run containers. (In Preview.)

## May 10, 2023

Feature

Cloud Run [integrations](https://docs.cloud.google.com/run/docs/integrate/using-gcp-services#integrations) (Preview) are now available in `asia-east1`, `europe-west4`, `us-east1`, and `us-west1`.

## May 09, 2023

Feature

Cloud Run services can now [connect to Firebase Hosting for custom domains and CDN capabilities](https://docs.cloud.google.com/run/docs/integrate/firebase-hosting), using [Integrations](https://docs.cloud.google.com/run/docs/integrate/using-gcp-services#integrations) (Preview).

Change

Cloud Run now [logs container health check failures](https://docs.cloud.google.com/run/docs/configuring/healthchecks), including default TCP startup probe failures.

## May 03, 2023

Feature

[CPU allocation recommender](https://docs.cloud.google.com/run/docs/recommender#optimize_cost) now automatically recommends CPU allocation changes based on traffic received by your Cloud Run service over the past month. (In Preview)

## April 26, 2023

Announcement

Cloud Run [source deployment](https://docs.cloud.google.com/run/docs/deploying-source-code) now supports Ubuntu 22 LTS base images. This is a new builder that is available under `gcr.io/buildpacks/builder:google-22` and addresses multiple security issues. You can read more about the `google-22` builder in our [announcement on GitHub](https://docs.cloud.google.com/docs/buildpacks/github/buildpacks/discussions/271).

The default builder for Cloud Run source deployments will be switched to `google-22` at a future date. To preview the `google-22` builder, see [Deploy from source with Cloud Run](https://docs.cloud.google.com/docs/buildpacks/use-a-specific-builder#deploy_from_source_with_cloud_run).

## April 20, 2023

Feature

Cloud Run [integrations](https://docs.cloud.google.com/run/docs/integrate/using-gcp-services#integrations) (Preview) are now available in `europe-west1`.

## April 18, 2023

Feature

[Session affinity](https://docs.cloud.google.com/run/docs/configuring/session-affinity) for Cloud Run service revisions is now at general availability (GA).

Feature

A Cloud Run service revision will now [accept requests from the Shared VPC network](https://docs.cloud.google.com/run/docs/securing/private-networking#shared-vpc) that it is [connected to](https://docs.cloud.google.com/run/docs/configuring/connecting-shared-vpc), including when [Ingress](https://docs.cloud.google.com/run/docs/securing/ingress#settings) is configured as "Internal" or "Internal and Cloud Load Balancing." (Preview)

## April 13, 2023

Feature

[Startup CPU boost](https://docs.cloud.google.com/run/docs/configuring/cpu#startup-boost) for Cloud Run services is now at general availability (GA).

## April 11, 2023

Breaking

Source code deployments that use Node.js now automatically run the `npm run build` command by default when any `build` script is defined in the `package.json` file. 

For details about how to configure the `package.json` file, including the option to set environment variables or prevent the default script from running, see the [Node.js buildpack configuration](https://docs.cloud.google.com/docs/buildpacks/nodejs#executing_custom_build_steps_during_deployment) in the Google Cloud's buildpacks documentation.

## April 10, 2023

Change

When [deploying a new revision](https://docs.cloud.google.com/run/docs/deploying#revision), Cloud Run now starts enough instances of the new revision before directing traffic to it. This reduces the impact of new revision deployments on request latencies, notably when serving high levels of traffic.

## April 07, 2023

Feature

Support for [Identity-aware Proxy (IAP) with Cloud Run](https://docs.cloud.google.com/iap/docs/enabling-cloud-run) to use identity and context to guard access to your applications is now at general availability (GA).

## April 06, 2023

Feature

Regional external and regional internal HTTP(S) load balancers now support using Cloud Run services as backends for the load balancer. This is configured using a serverless network endpoint group (NEG).

For details, see:

  * [Serverless NEG concepts](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts)
  * [Setting up a regional external HTTP(S) load balancer with a Cloud Run backend](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-reg-ext-https-serverless)
  * [Setting up an internal HTTP(S) load balancer with a Cloud Run backend](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless)



This feature is available in **General availability**.

## March 30, 2023

Feature

The following new region is now available: `me-central1`.

## March 29, 2023

Feature

[Cloud Run jobs](https://docs.cloud.google.com/run/docs/create-jobs) are now at general availability (GA).

## March 23, 2023

Feature

The following new region is now available: `europe-west12`.

## March 11, 2023

Feature

Cloud Run [healthcheck probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks) now support container port configuration.

## March 07, 2023

Feature

You can now authenticate to a Cloud Run service by including a Google-signed OpenID Connect ID token in the [`X-Serverless-Authorization` header](https://docs.cloud.google.com/run/docs/authenticating/service-to-service#acquire-token) if your application already uses the `Authorization` header for custom authorization.

## February 27, 2023

Change

When [session affinity](https://docs.cloud.google.com/run/docs/configuring/session-affinity) is enabled on a Cloud Run service that is splitting traffic between multiple revisions, requests from the same clients are now [routed to the same revision](https://docs.cloud.google.com/run/docs/configuring/session-affinity#affinity-and-traffic-splitting). When updating the traffic splitting configuration, Cloud Run minimizes the number of clients that are redirected to a new revision.

## February 16, 2023

Feature

You can now deploy public container images from Docker Hub to Cloud Run.

## February 03, 2023

Feature

You can now [deploy multi-architecture container images](https://docs.cloud.google.com/run/docs/container-contract#languages) to Cloud Run if their manifest list includes `amd64/linux`.

## January 12, 2023

Change

Terraform resources for [Cloud Run Services](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) and [Cloud Run Jobs](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_job) based on the [Cloud Run Admin API v2](https://docs.cloud.google.com/run/docs/reference/rest) are now generally available (GA).

## December 21, 2022

Feature

The option to [update a Serverless VPC Access connector](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc#update-connector) is now available in preview. This feature allows you to edit the machine (instance) type, as well as the minimum and maximum number of instances.

## December 09, 2022

Feature

[Healthcheck probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks) are now at general availability (GA).

## December 06, 2022

Feature

Cloud Run support for a new [second generation execution environment](https://docs.cloud.google.com/run/docs/about-execution-environments) is now at generally availability (GA).

Feature

Cloud Run support for network file systems such as [NFS, NDB, 9P, CIFS/Samba, and Ceph](https://docs.cloud.google.com/run/docs/configuring/jobs/nfs-volume-mounts), as well as [Cloud Filestore](https://docs.cloud.google.com/run/docs/configuring/services/nfs-volume-mounts) and [Cloud Storage FUSE](https://docs.cloud.google.com/run/docs/configuring/services/cloud-storage-volume-mounts), is now at general availability (GA.)

## November 17, 2022

Feature

Logs from Cloud Run services can now be [tailed or viewed in a command-line friendly format](https://docs.cloud.google.com/run/docs/logging#viewing-logs-gcloud) using `gcloud beta run services logs tail` and `gcloud beta run services logs read`

## October 07, 2022

Feature

Cloud Run services can now [use the Global External HTTP(S) Load Balancer to map Custom Domains](https://docs.cloud.google.com/run/docs/integrate/custom-domain-load-balancer) using [integrations](https://docs.cloud.google.com/run/docs/integrate/using-gcp-services#integrations) (Preview).

Feature

Cloud Run services can now [connect to Memorystore for Redis instances](https://docs.cloud.google.com/run/docs/integrate/redis-memorystore) using [integrations](https://docs.cloud.google.com/run/docs/integrate/using-gcp-services#integrations) (Preview).

## October 04, 2022

Feature

New [security recommendations](https://docs.cloud.google.com/run/docs/recommender) are created for Cloud Run services, which recommends securing environment variables that might contain passwords, API keys and Google application credentials.

## September 30, 2022

Change

The [Cloud Run Admin API v2](https://docs.cloud.google.com/run/docs/reference/rest) is now at general availability (GA).

Feature

The Cloud Run first generation execution environment now has faster filesystem performance.

## September 23, 2022

Feature

You can now configure an [HTTP liveness healthcheck probe](https://docs.cloud.google.com/run/docs/configuring/healthchecks#liveness-probes).

## September 20, 2022

Feature

Cloud Run now supports [workforce identity federation](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services)

## September 14, 2022

Feature

[Startup CPU boost](https://docs.cloud.google.com/run/docs/configuring/cpu#startup-boost) for revisions is now available to provide additional CPU during container instance startup time.

## September 13, 2022

Feature

You can now [deploy Cloud Run services from Cloud Deploy](https://docs.cloud.google.com/deploy/docs/run-targets) (Preview).

Feature

[Startup healthcheck probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks) are now available (Preview).

Feature

The following new region is now available: `me-west1`.

## September 05, 2022

Change

Cloud Run now allows up to 4,000 serving revisions and 2,000 [tagged revisions](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#tags) per region and project.

## September 01, 2022

Change

Terraform samples are now available in many of the Cloud Run tutorials and guides, such as:

  * [Static outbound IP address](https://docs.cloud.google.com/run/docs/configuring/static-outbound-ip#terraform),
  * [Pub/Sub with Cloud Run](https://docs.cloud.google.com/run/docs/tutorials/pubsub)
  * [Authenticating service to service](https://docs.cloud.google.com/run/docs/authenticating/service-to-service#terraform)
  * [Rollbacks & Rollouts](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#terraform)
  * [Request Timeouts](https://docs.cloud.google.com/run/docs/configuring/request-timeout#terraform)



and many other pages. You can also find a [full list of Terraform samples](https://github.com/terraform-google-modules/terraform-docs-samples) in GitHub.

## July 18, 2022

Feature

Cloud Run now supports container images in the [Open Container Initiative (OCI)](https://github.com/opencontainers/image-spec) image format.

## July 11, 2022

Feature

Cloud Run now writes [Access Transparency logs](https://docs.cloud.google.com/cloud-provider-access-management/access-transparency/docs/overview), see [Enabling Access Transparency](https://docs.cloud.google.com/cloud-provider-access-management/access-transparency/docs/enable#enabling).

## June 08, 2022

Feature

[Session affinity](https://docs.cloud.google.com/run/docs/configuring/session-affinity) is now available for Cloud Run service revisions.

## June 07, 2022

Feature

The following new region is now available: `us-south1`.

## June 06, 2022

Feature

You can now [create and edit Cloud Run jobs](https://docs.cloud.google.com/run/docs/create-jobs) using the Cloud console.

## May 24, 2022

Feature

The following new region is now available: `us-east5`.

## May 16, 2022

Feature

You can now [tag services](https://docs.cloud.google.com/run/docs/configuring/tags) using Resource Manager tags for fine-grained access control.

## May 11, 2022

Feature

[Cloud Run jobs](https://docs.cloud.google.com/run/docs/create-jobs) are now available in Preview.

## May 09, 2022

Feature

The following new region is now available: `europe-southwest1`.

## May 05, 2022

Feature

You can now define service-level objectives (SLOs) for your Cloud Run services using [SLO monitoring](https://docs.cloud.google.com/stackdriver/docs/solutions/slo-monitoring) in Cloud Monitoring or the Cloud Run service page.

## May 03, 2022

Feature

The following new region is now available: `europe-west9`.

## April 22, 2022

Feature

You can now [allocate up to 32 GiB of memory](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits) and [up to 8 CPU](https://docs.cloud.google.com/run/docs/configuring/services/cpu) to your Cloud Run services.

## April 19, 2022

Feature

The following new region is now available: `europe-west8`.

## March 28, 2022

Feature

Cloud Run reports a new Cloud Monitoring metric: Container Startup Latency, measuring the [startup time](https://docs.cloud.google.com/run/docs/container-contract#startup) of container instances.

## March 24, 2022

Feature

Support for Serverless VPC Access connectors in Shared VPC host projects is now at general availability (GA). Learn about the [advantages](https://docs.cloud.google.com/run/docs/configuring/connecting-shared-vpc#host-project) of this method and how to [configure connectors in host projects](https://docs.cloud.google.com/run/docs/configuring/shared-vpc-host-project).

## February 25, 2022

Feature

Cloud Run now supports using less than one CPU. Refer to [ CPU limits](https://docs.cloud.google.com/run/docs/configuring/services/cpu) for details. (Available in public preview.)

## February 16, 2022

Feature

[BigQuery remote functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/remote-functions) allow you to implement custom BigQuery SQL functions leveraging Cloud Run HTTP services (Preview)

## February 09, 2022

Fixed

The [configured container arguments](https://docs.cloud.google.com/run/docs/configuring/containers#configure-entrypoint) are now correctly overriding arguments defined inside the container image. This change applies to new services only.

## December 16, 2021

Change

For consistency with latency reported in request logs, the `request_latencies` monitoring metric now excludes container startup latency.

## December 14, 2021

Feature

The ability to [configure](https://docs.cloud.google.com/run/docs/configuring/cpu-allocation) Cloud Run services to have CPU allocated for the entire lifetime of container instances is now at general availability (GA).

## December 02, 2021

Feature

[Internal ingress from Workflows](https://docs.cloud.google.com/workflows/docs/calling-run-functions#internal_ingress) to Cloud Run is now at general availability (GA).

## November 16, 2021

Feature

The following new region is now available: `southamerica-west1`.

## November 09, 2021

Feature

Cloud Run support for referencing Secret Manager [Secrets](https://docs.cloud.google.com/run/docs/configuring/services/secrets) is now at general availability (GA).

## November 01, 2021

Feature

You can now allocate up to 16GiB of [memory](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits) to your Cloud Run services.

Feature

[Committed use discount recommender](https://docs.cloud.google.com/docs/cuds-recommender) now automatically generates recommendations to purchase Cloud Run [committed use discounts](https://docs.cloud.google.com/run/cud) based on historical usage.

## October 27, 2021

Feature

Cloud Run now supports network file systems such as [NFS, NDB, 9P, CIFS/Samba, and Ceph](https://docs.cloud.google.com/run/docs/configuring/jobs/nfs-volume-mounts), as well as [Cloud Filestore](https://docs.cloud.google.com/run/docs/configuring/services/nfs-volume-mounts) and [Cloud Storage FUSE](https://docs.cloud.google.com/run/docs/configuring/services/cloud-storage-volume-mounts). (Available in public preview.)

Feature

Cloud Run now supports a new [second generation execution environment](https://docs.cloud.google.com/run/docs/configuring/execution-environments) that provides full Linux compatibility rather than system call emulation. This execution environment provides better performance and the ability to use network file systems. (Available in public preview.)

## September 28, 2021

Feature

[Customer managed encryption keys](https://docs.cloud.google.com/run/docs/securing/using-cmek) are now at general availability (GA).

Feature

[Binary Authorization for Cloud Run](https://docs.cloud.google.com/binary-authorization/docs/run/overview) is now at generally availability (GA).

## September 13, 2021

Feature

You can now [configure](https://docs.cloud.google.com/run/docs/configuring/billing-settings) Cloud Run services to have CPU allocated for the entire lifetime of container instances. [Pricing](https://cloud.google.com/run/pricing) depends on the CPU allocation configuration. (Available in public preview.)

## August 24, 2021

Feature

[Deploying to Cloud Run from source code](https://docs.cloud.google.com/run/docs/deploying-source-code) is now at General Availability (GA).

## August 03, 2021

Feature

The following new region is now available: `northamerica-northeast2`.

## July 27, 2021

Feature

Cloud Run [VPC Service Controls](https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls) are now at General Availability (GA).

Feature

[Committed use discounts](https://docs.cloud.google.com/run/cud) are now at General Availability (GA).

Feature

The following [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) are now at General Availability (GA): Cloud Run **Allowed ingress settings** and **Allowed VPC egress settings**.

## July 26, 2021

Feature

Cloud Run container instances can now process up to 1,000 [concurrent requests](https://docs.cloud.google.com/run/docs/about-concurrency), see [Setting maximum concurrency](https://docs.cloud.google.com/run/docs/configuring/concurrency). The default is still 80.

## July 20, 2021

Feature

Cloud Run is now covered by [FedRAMP Moderate](https://cloud.google.com/security/compliance/fedramp)

## June 30, 2021

Feature

Cloud Run is now available in the following region:

  * asia-south2 (Delhi, India)



## June 25, 2021

Feature

Cloud Run is now available in the following region:

  * `australia-southeast2` (Melbourne)



## June 22, 2021

Feature

Cloud Run support for [WebSockets](https://docs.cloud.google.com/run/docs/triggering/websockets), [HTTP/2](https://docs.cloud.google.com/run/docs/configuring/http2), and [gRPC streaming](https://docs.cloud.google.com/run/docs/triggering/grpc) are now at general availability (GA).

## June 03, 2021

Feature

[Request timeouts up to 60 minutes](https://docs.cloud.google.com/run/docs/configuring/request-timeout) are now at general availability (GA).

## May 14, 2021

Feature

[User labels now appear in logs](https://docs.cloud.google.com/run/docs/logging#log-resource).

## May 12, 2021

Feature

You can now use [Binary authorization](https://docs.cloud.google.com/binary-authorization/docs/run/enabling-binauthz-cloud-run) with Cloud Run to enforce policy-based deployment of Cloud Run services. (Available in public preview.)

Feature

[Committed use discounts](https://cloud.google.com/run/cud) are now available for Cloud Run . (Available in public preview.)

Feature

Cloud Run now provides UI, command line, and YAML support for referencing Secret Manager [Secrets](https://docs.cloud.google.com/run/docs/configuring/services/secrets). (Available in public preview.)

Feature

[Customer managed encryption keys](https://docs.cloud.google.com/run/docs/securing/using-cmek) are now available for use with Cloud Run. (Available in public preview.)

Feature

[Recommender](https://docs.cloud.google.com/run/docs/recommender) now provides recommendations for securing Cloud Run services by creating dedicated service accounts. (Available in public preview.)

## May 03, 2021

Feature

You can now use [Identity-aware Proxy](https://docs.cloud.google.com/iap/docs/concepts-overview) with Cloud Run to use identity and context to guard access to your applications. (Available in public preview.)

Change

By default, the memory allocated to each container instance of a new service is 512MiB. The new default applies to new services. Existing services retain their allocated memory.

## April 14, 2021

Feature

Cloud Run is now available in `europe-central2` (Warsaw)

## April 01, 2021

Feature

[Restricting ingress on Cloud Run](https://docs.cloud.google.com/run/docs/securing/ingress) is now at general availability (GA).

## March 31, 2021

Feature

"Memory limit exceeded" and "No instances available" errors are now captured and aggregated in [Cloud Error Reporting](https://docs.cloud.google.com/error-reporting/docs/service-errors)

## March 18, 2021

Feature

[Shared VPC on Cloud Run](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc#shared-vpc) is now at general availability (GA).

## March 08, 2021

Feature

The ability to specify a [minimum number of container instances](https://docs.cloud.google.com/run/docs/configuring/min-instances) to be kept warm and ready to serve requests is now at general availability (GA).

## March 05, 2021

Feature

You can now use [VPC Service Controls](https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls) with Cloud Run to set up a secure perimeter to guard against data exfiltration. (Available in public preview.)

## March 03, 2021

Feature

Cloud Run reports a new Cloud Monitoring metric: [Instance count](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-run), which counts the number of container instances that exist, broken down by state (active or idle).

## March 01, 2021

Feature

Cloud Run is now available in the following regions:

  * `us-west2` (Los Angeles)
  * `us-west3` (Salt Lake city)
  * `us-west4` (Las Vegas)



## January 20, 2021

Feature

Cloud Run now supports [WebSockets](https://docs.cloud.google.com/run/docs/triggering/websockets), [HTTP/2](https://docs.cloud.google.com/run/docs/configuring/http2) and [gRPC streaming](https://docs.cloud.google.com/run/docs/triggering/grpc).

## December 18, 2020

Feature

Cloud Run now allows you to [restrict ingress](https://docs.cloud.google.com/run/docs/securing/ingress) of your Cloud Run services.

Feature

You can now [allocate up to 8GiB of memory](https://docs.cloud.google.com/run/docs/configuring/memory-limits) to your Cloud Run services.

## December 16, 2020

Feature

You can now build and deploy source code to Cloud Run using a single command: [`gcloud beta run deploy --source .` ](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run/deploy#--source)

## December 14, 2020

Feature

Cloud Run container instances can now process up to 250 [concurrent requests](https://docs.cloud.google.com/run/docs/about-concurrency), see [Configuring maximum concurrency](https://docs.cloud.google.com/run/docs/configuring/concurrency). The default is still 80.

## October 23, 2020

Feature

Cloud Run services can now be triggered using [Eventarc](https://docs.cloud.google.com/run/docs/quickstarts/events) (available in public preview)

## October 19, 2020

Feature

Cloud Run is now available in the following regions:

  * `asia-east2` (Hong Kong)
  * `asia-northeast3` (Seoul, South Korea)
  * `asia-southeast2 ` (Jakarta)
  * `asia-south1` (Mumbai, India)
  * `europe-west2` (London, UK)
  * `europe-west3` (Frankfurt, Germany)
  * `europe-west6` (Zurich, Switzerland)
  * `southamerica-east1` (Sao Paulo, Brazil)



Feature

You can now [purchase a custom domain via Cloud Domains](https://docs.cloud.google.com/run/docs/mapping-custom-domains) using the Cloud Run user interface.

## October 15, 2020

Feature

You can now specify a [minimum number of container instances](https://docs.cloud.google.com/run/docs/configuring/min-instances) to be kept warm and ready to serve requests, for services requiring reduced latency and fewer cold starts.

## October 13, 2020

Feature

You can now [control egress traffic from a service](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc#egress) and route all outbound requests to your VPC network. This allows you to configure [a static outbound IP address by leveraging Cloud NAT](https://docs.cloud.google.com/run/docs/configuring/static-outbound-ip).

## October 12, 2020

Feature

You can now [allocate 4 vCPUs](https://docs.cloud.google.com/run/docs/configuring/cpu) to container instances of Cloud Run services.

Feature

Traces of requests to Cloud Run services are now automatically captured in [Cloud Trace](https://docs.cloud.google.com/trace)

## October 11, 2020

Feature

When a container instance needs to be shut down, it now receives a `SIGTERM` signal. If handled, CPU is allocated for up to [10 seconds before the container is shut down](https://docs.cloud.google.com/run/docs/reference/container-contract#lifecycle).

## October 06, 2020

Feature

Cloud Run now supports [request timeouts up to 60 minutes](https://docs.cloud.google.com/run/docs/configuring/request-timeout). However, timeouts greater than 15 minutes are a beta feature.

## September 29, 2020

Feature

Cloud Run now supports server-side HTTP and gRPC streaming.

## August 19, 2020

Feature

Cloud Code IDE extensions now allow you to develop and debug Cloud Run services locally. See [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/developing-a-cloud-run-app) and [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/developing-a-cloud-run-app)

## August 18, 2020

Feature

You can now [allocate up to 4GiB of memory](https://docs.cloud.google.com/run/docs/configuring/memory-limits) to your Cloud Run (fully managed) services.

## August 03, 2020

Feature

When [setting up Continuous Deployment](https://docs.cloud.google.com/run/docs/continuous-deployment-with-cloud-build) in the Cloud Run user interface, you can now select a repository that contains Go, Node.js, Python Java or .NET Core code. It will be built using [Google Cloud Buildpacks](https://github.com/GoogleCloudPlatform/buildpacks) without needing a Dockerfile.

## July 30, 2020

Feature

You can now tag Cloud Run revisions. Tagged revisions get a dedicated URL allowing developers to reach these specific revisions without needing to allocate traffic to it.

## July 27, 2020

Feature

Cloud Run is now available in `asia-southeast1` (Singapore)

## July 23, 2020

Feature

[Serverless VPC Access support for Shared VPC](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc#shared-vpc) is now available in Beta.

## July 21, 2020

Feature

Cloud Run resources are now available in [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview)

## July 13, 2020

Feature

The Cloud Run user interface now allows you to easily [set up Continuous Deployment from Git using Cloud Build](https://docs.cloud.google.com/run/docs/continuous-deployment-with-cloud-build)

## July 07, 2020

Feature

External HTTP(S) Load Balancing is now supported for Cloud Run services via [Serverless network endpoint groups](https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-serverless-negs).  
Notably, this feature allows you to use [Cloud CDN](https://cloud.google.com/cdn) and multi-region load balancing. This feature is available in Beta.

## June 30, 2020

Feature

Cloud Run (fully managed) support for [connecting to a VPC network](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc) with [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access) is now at general availability (GA).

## June 29, 2020

Feature

Cloud Run is now available in the following regions:

  * `asia-northeast2` (Osaka)
  * `australia-southeast1` (Sydney)
  * `northamerica-northeast1` (Montréal)



## June 16, 2020

Feature

The Cloud Run user interface now allows you to copy a Cloud Run service.

## June 09, 2020

Feature

Export a Cloud Run service to a YAML file with `gcloud run services describe SERVICE --format export`

## June 03, 2020

Feature

The Cloud Run user interface now allows you to edit the service YAML.

## May 20, 2020

Feature

The Cloud Run [container instance metadata server](https://docs.cloud.google.com/run/docs/reference/container-contract#metadata-server) now exposes the unique identifier of the container instance and the region of the Cloud Run service

## May 13, 2020

Feature

Cloud Run (fully managed) now supports [connecting to a VPC network](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc) with [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access), in beta.

## May 08, 2020

Feature

Cloud Code IDE extensions support Cloud Run. See [Cloud Code for VS Code](https://docs.cloud.google.com/code/docs/vscode/deploying-a-cloud-run-app) and [Cloud Code for IntelliJ](https://docs.cloud.google.com/code/docs/intellij/deploying-a-cloud-run-app)

## March 30, 2020

Feature

The Cloud Run revision details panel now surfaces build information if the [Container Analysis API](https://docs.cloud.google.com/container-registry/docs/container-analysis) has been enabled and the container has been built with [Cloud Build](https://cloud.google.com/build), as well as source repository information if the container has been built by a [Cloud Build Trigger](https://docs.cloud.google.com/build/docs/running-builds/create-manage-triggers).

## March 23, 2020

Fixed

You can now restrict which regions are available to deploy Cloud Run (fully managed) services using an organization policy with a [resource locations constraint](https://docs.cloud.google.com/organization-policy/restrict-locations).

## March 16, 2020

Feature

Cloud Run (fully managed) now supports deploying container images from [Cloud Artifact Registry](https://docs.cloud.google.com/artifacts/docs/overview)

## February 12, 2020

Feature

Cloud Run (fully managed) now supports [rollbacks, gradual rollouts (blue/green deployments), and other traffic migration manipulations](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration) between revisions.

## January 30, 2020

Feature

Cloud Run is now available in the following regions:

  * asia-east1 (Taiwan) 
  * europe-north1 (Finland) 
  * europe-west4 (Netherlands) 
  * us-east4 (Northern Virginia)
  * us-west1 (Oregon)



## January 27, 2020

Deprecated

The Cloud Run v1alpha1 API is deprecated and will be turned down. It is replaced by the [Cloud Run v1 API](https://docs.cloud.google.com/run/docs/reference/rest)

## January 24, 2020

Feature

You can now [allocate 2 vCPUs](https://docs.cloud.google.com/run/docs/configuring/cpu) to Cloud Run (fully managed) services.

## January 07, 2020

Feature

Deploy Cloud Run services from a local configuration file with `gcloud beta run services replace service.yaml`.

Feature

You can now [customize the container port](https://docs.cloud.google.com/run/docs/configuring/containers#configure-port) on which requests are sent. We still recommend listening on `$PORT` for better container portability.

Feature

[Specify custom command and arguments](https://docs.cloud.google.com/run/docs/configuring/containers#configure-entrypoint) for your deployed containers.

Feature

Use custom revision names with the `--revision-suffix` command line flag.

## December 23, 2019

Change

Cloud Run (fully managed) [Service Level Agreement (SLA)](https://cloud.google.com/run/sla) has been updated to a Monthly Uptime Percentage of at least 99.95%

## November 14, 2019

Announcement

Cloud Run (fully managed) is now Generally Available (GA).

## October 25, 2019

Breaking

Legacy versions of the [container instance metadata server](https://docs.cloud.google.com/run/docs/reference/container-contract#metadata-server) have been removed.

## October 22, 2019

Change

Cloud Run (fully managed) free tier is now applied as a spending based discount.

## October 21, 2019

Feature

Cloud Run is now covered by [HIPAA Compliance](https://docs.cloud.google.com/docs/security/compliance/hipaa).

## October 01, 2019

Feature

The [max instances setting](https://docs.cloud.google.com/run/docs/configuring/max-instances) feature allows you to set a limit to the total number of container instances that are started up to handle traffic.

## September 26, 2019

Feature

The "Metrics" tab on the [service detail page](https://docs.cloud.google.com/run/docs/managing/services#details) now includes an ["Error Reporting"](https://docs.cloud.google.com/run/docs/error-reporting) table that displays the top application errors for this service.

Feature

The "Metrics" tab on the [service detail page](https://docs.cloud.google.com/run/docs/managing/services#details) now includes a "[Billable container instance time](https://docs.cloud.google.com/monitoring/api/metrics_gcp#gcp-run)" chart, allowing you to better understand how many instances are actively serving traffic for this service.

## September 25, 2019

Feature

Cloud Run (fully managed) now supports [unary gRPC](https://grpc.io/docs/guides/concepts/).

## September 19, 2019

Feature

[Cloud Run (fully managed) v1 API](https://docs.cloud.google.com/run/docs/reference/rest) is now available.

## September 10, 2019

Feature

You can set [labels](https://docs.cloud.google.com/run/docs/configuring/labels) on Cloud Run services and revisions.

## August 19, 2019

Change

Cloud Run (fully managed) services are now only accessible via HTTPS. Any HTTP requests to Cloud Run services now receives a 302 "Moved Temporarily" status code that redirects to the HTTPS location. Web browsers follow this redirection.

## July 10, 2019

Feature

The following new regions are now available: `asia-northeast1`, `europe-west1`, and `us-east1`.

## July 08, 2019

Feature

New YAML tab on the service details page.

## June 18, 2019

Change

New `--platform` flag added to [Cloud Run gcloud command line](https://docs.cloud.google.com/sdk/gcloud/reference/beta/run). This argument is optional but will be required in a future release of the tool.

## June 07, 2019

Feature

[Per-service identity](https://docs.cloud.google.com/run/docs/securing/service-identity#per-service-identity).

## May 20, 2019

Feature

New "Metrics" tab in the Cloud Run service detail view, displaying a list of curated [monitoring metrics](https://docs.cloud.google.com/run/docs/monitoring).

## May 17, 2019

Feature

Cloud Run (fully managed) has been added to the [Google Cloud Platform Pricing Calculator](https://cloud.google.com/products/calculator).

## May 07, 2019

Feature

[Cloud SQL is now supported](https://docs.cloud.google.com/run/docs/configuring/connect-cloudsql).

## April 09, 2019

Feature

Cloud Run (fully managed) Beta release.

## August 15, 2018

Feature

Cloud Run (fully managed) Alpha release.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
