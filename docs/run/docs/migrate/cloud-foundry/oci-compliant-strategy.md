---
url: https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/oci-compliant-strategy/
title: Choose an OCI-compliant strategy \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:17.307655+00:00
---

# Choose an OCI-compliant strategy  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/oci-compliant-strategy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Choose an OCI-compliant strategy Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the Cloud Foundry build process you need to migrate from, and provides a description of the various ways you can migrate from that to a process that builds OCI-compliant containers.

## Cloud Foundry build process overview

When an application is pushed to Cloud Foundry, it goes through a build stage where the source code is compiled by the [Cloud Foundry v2 buildpacks](https://docs.cloudfoundry.org/buildpacks/).

The output of a Cloud Foundry build process creates a runnable archive known as a [droplet](https://docs.cloudfoundry.org/concepts/glossary.html). Droplets are not directly compatible with the Open Container Initiative (OCI) specification for running containers on Cloud Run.

When migrating applications from Cloud Foundry to Cloud Run you must change the application build process to generate industry standard OCI images (sometimes referred to as Docker images).

![Diagram describing how Cloud Foundry Droplets are created](https://docs.cloud.google.com/static/run/docs/images/cf-cr-droplet.svg)

## Strategies to achieve OCI-compliant images

There are three migration strategies you can choose from to build OCI-compliant containers:

  * Modify the existing Cloud Foundry application (sometimes referred to as "lift and shift")
  * Use Cloud Native buildpacks
  * Use self-managed Dockerfiles



### Modifying a Cloud Foundry application (lift and shift)

The core components of the Cloud Foundry ecosystem (v2 Buildpacks, Stemcells, etc.) are open source. This means you can re-create the application containerization process by following our guide to "Dockerize" the core build components to create a new OCI-compliant image.

**Pros:**

  * It requires the least amount of application refactoring and customization.
  * The process is repeatable for all application instances.



**Cons:**

  * The pipeline for building application containers is self-managed.
  * Older Cloud Foundry components have diminished maintenance and support.
  * There are ongoing security maintenance costs, including: 
    * Routinely re-building the build components to ensure you get security patches.
    * Routinely re-building the "dockerized" applications to take on the security updates from the rebuilt build components.



### Using Cloud Native Buildpacks

The [Cloud Native Buildpacks](https://buildpacks.io/) (CNB) specification was created to modernize and unify the buildpacks ecosystem. Builders compatible with the CNB specification follow open standards and create OCI-compliant images. Three common CNB providers are:

  * [Google Cloud's buildpacks](https://docs.cloud.google.com/docs/buildpacks/overview)
  * [VMware's Paketo buildpacks](https://paketo.io/)
  * [Heroku's buildpacks](https://devcenter.heroku.com/articles/buildpacks)



**Pros:**

  * Buildpack maintainers and platform providers are responsible for maintenance of the buildpack.
  * Buildpacks support rebasing containers on new images for fast security updates without rebuilding application containers.
  * Buildpacks generate portable OCI images.
  * The CNB project is [incubating under the Cloud Native Computing Foundation (CNCF)](https://www.cncf.io/projects/buildpacks/) and has an active community of maintainers and contributors.



**Cons:**

  * Functionality and configuration gaps between v2 and v3 buildpacks.
  * Frameworks and integrations installed on your behalf in the [Java v2 buildpacks](https://github.com/cloudfoundry/java-buildpack) may not be available in the Java CNB buildpack.



### Using self-managed Dockerfiles

You can author completely new Dockerfiles to containerize your application. Refer to [building containers](https://docs.cloud.google.com/run/docs/building/containers) to learn about container images accepted by Cloud Run.

**Pros:**

  * Gives you the most flexibility in designing your applications.
  * Leverage your company's existing container tooling & build strategies.



**Cons:**

  * Dockerization and custom configuration must be performed for each application, leading to potentially time consuming debugging and rewrites.
  * Difficult to standardize implementations across multiple teams.
  * Patching images requires a full rebuild and redeploy.



### Recommendations

Teams that are resource-constrained and looking to move as many applications as possible should first consider the **Lift and Shift** strategy to modify Cloud Foundry. Once the applications are modernized to towards being OCI-compliant images, we recommend that you consider using Cloud Native Buildpacks or self-managed Dockerfiles.

Teams that are ready to migrate immediately should try Cloud Native Buildpacks and then move to self managed Dockerfiles if they need a high level of control over their environment.

## What's Next

  * Follow the [sample Spring Music migration](https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/spring-music-migration-example) which uses the lift and shift strategy.
  * [Migrate to OCI containers](https://docs.cloud.google.com/run/docs/migrate/cloud-foundry/migrate-to-oci-containers)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
