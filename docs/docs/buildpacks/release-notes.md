---
url: https://docs.cloud.google.com/docs/buildpacks/release-notes/
title: Buildpacks release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:10:59.499957+00:00
---

# Buildpacks release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/buildpacks/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Buildpacks ](https://docs.cloud.google.com/docs/buildpacks)
  * [ Resources ](https://docs.cloud.google.com/docs/buildpacks/release-notes)



Send feedback 

#  Buildpacks release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Buildpacks. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/cloudbuildpacks-release-notes.xml) directly. 

## October 21, 2026

Feature

Patch updates to [PHP runtimes](https://docs.cloud.google.com/appengine/docs/flexible/lifecycle/support-schedule#php) are available on `google-22` and `google-24` tags: `8.5.12`, `8.4.27`, `8.3.36`, and `8.2.35`. Take immediate action to protect your PHP workloads by rebuilding your workloads with updated dependencies. See [Responding to core PHP vulnerabilities](https://cloud.google.com/blog/products/identity-security/responding-to-core-php-vulnerabilities-cve-2026-109618-cve-2026-109619) for more information.

## August 19, 2026

Feature

Starting from Go runtime version 1.26 and later, the lifecycle support dates align more closely with the [Go community release cycle](https://go.dev/wiki/Go-Release-Cycle). For more information, see [Runtime support schedule](https://docs.cloud.google.com/docs/buildpacks/runtime-support#go).

## May 12, 2026

Feature

The `latest` tag of [generic builder](https://docs.cloud.google.com/docs/buildpacks/builders#generic_builder) uses the `google-24` stack.

## April 03, 2026

Feature

The Node.js buildpack supports the Bun package manager in [General Availability](https://cloud.google.com/products#product-launch-stages). For more information, see [Building a Node.js application](https://docs.cloud.google.com/docs/buildpacks/nodejs#bun_package_manager).

## March 13, 2026

Feature

The Node.js buildpack supports the Bun package manager in [Preview](https://cloud.google.com/products?e=48754805#product-launch-stages). For more information, see [Building a Node.js application](https://docs.cloud.google.com/docs/buildpacks/nodejs#bun_package_manager).

## February 17, 2026

Feature

Cloud Run [source deployment](https://docs.cloud.google.com/run/docs/deploying-source-code) supports Ubuntu 24 LTS base images in [General Availability](https://cloud.google.com/products?e=48754805#product-launch-stages). This builder is available under `gcr.io/buildpacks/builder:google-24`. For more information, see [Builders](https://docs.cloud.google.com/docs/buildpacks/builders).

## February 11, 2026

Feature

Support for [osonly24 runtime](https://docs.cloud.google.com/docs/buildpacks/runtime-support#osonly) is in [General Availability](https://cloud.google.com/products?e=48754805#product-launch-stages). The OS only runtime lets you deploy binaries such as Dart and Go. For more information, see [Configure the OS only runtime](https://docs.cloud.google.com/docs/buildpacks/osonly).

## January 22, 2026

Feature

The Python buildpack supports default entrypoint detection for the [Agent Development Kit (ADK) framework](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-adk-service) in [General Availability](https://cloud.google.com/products#product-launch-stages). For more information, see [Build a Python application](https://docs.cloud.google.com/docs/buildpacks/python#entrypoint).

## January 13, 2026

Feature

Cloud Run and Cloud Run functions source deployments support the `pyproject.toml` file for managing dependencies. This feature is in [General Availability](https://cloud.google.com/products#product-launch-stages) for all [supported Python versions](https://docs.cloud.google.com/docs/buildpacks/runtime-support#python). For more information, see [Deploy Python applications with a `pyproject.toml` file](https://docs.cloud.google.com/docs/buildpacks/python#deploy-with-toml).

## December 19, 2025

Feature

The Python buildpack supports default entrypoint detection for the [Agent Development Kit (ADK) framework](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-adk-service) (Preview). For more information, see [Build a Python application](https://docs.cloud.google.com/docs/buildpacks/python#entrypoint).

Feature

Cloud Run and Cloud Run functions source deployments support `pyproject.toml` file for managing dependencies. This feature is in General Availability for Python version 3.13 and later, and is in Preview for Python version 3.12 and earlier. For more information, see [Deploy Python applications with a `pyproject.toml` file](https://docs.cloud.google.com/docs/buildpacks/python#deploy-with-toml).

## December 18, 2025

Feature

Support for [osonly24 runtime](https://docs.cloud.google.com/buildpacks/docs/runtime-support#osonly) is in [Preview](https://cloud.google.com/products?e=48754805#product-launch-stages). The OS only runtime lets you deploy Go applications from source, and binaries such as Dart and Go. For more information, see [Configure the OS only runtime](https://docs.cloud.google.com/docs/buildpacks/osonly).

## November 14, 2025

Feature

Cloud Run and Cloud Run functions source deployments support `pyproject.toml` file for managing dependencies. If you use a `pyproject.toml` file, source deployments use one of the following to find and install dependencies:

  * `pip`
  * `uv`
  * `poetry`



For more information, see [Deploy Python applications with a `pyproject.toml` file](https://docs.cloud.google.com/docs/buildpacks/python#deploy-with-toml) (Preview).

## September 18, 2025

Feature

Ubuntu 24 builder with the `google-24` stack is available for Google Cloud's Buildpacks. For more information, see [Builders](https://docs.cloud.google.com/docs/buildpacks/builders) and [Use a specific builder](https://docs.cloud.google.com/docs/buildpacks/use-a-specific-builder).

## August 14, 2025

Feature

The Python buildpack supports Cloud Run source deployments for modern web frameworks such as [FastAPI](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-fastapi-service), [Gradio](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-gradio-service), and [Streamlit](https://docs.cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-streamlit-service).

For Python version 3.13 and later, the Python buildpack sets the default entrypoint for [Cloud Run source deployments](https://docs.cloud.google.com/run/docs/deploying-source-code) based on the web server or framework configuration in your `requirements.txt` file. For more information, see [Build a Python application](https://docs.cloud.google.com/docs/buildpacks/python#entrypoint).

## September 23, 2024

Change

The [runtime support schedule for some PHP runtimes](https://docs.cloud.google.com/docs/buildpacks/runtime-support#php) has been extended to match [PHP's public support schedule](https://www.php.net/supported-versions.php).

## February 26, 2024

Feature

Starting in Go version 1.22 and later, you can no longer use `GOPATH` for installing dependencies. To manage dependencies, you use a [`go.mod`](https://cs.opensource.google/go/go/+/refs/tags/go1.22.0:src/go.mod) file. For more information about Go versions, and managing dependencies for vendor directories, see [GOPATH and Modules](https://pkg.go.dev/cmd/go#hdr-GOPATH_and_Modules) in Go documentation.

## August 28, 2023

Announcement

The support policy and schedule for Google Cloud's buildpacks is now available at [https://cloud.google.com/docs/buildpacks/support-policy](https://docs.cloud.google.com/docs/buildpacks/support-policy).

## July 19, 2023

Change

The Python buildpack now uses `gunicorn --bind :8080 main:app` as the default entrypoint for all web applications. If you currently use a `Procfile`, it will continue to work but you are no longer required to configure a `Procfile` for your projects. Learn more about [Python application entrypoints](https://docs.cloud.google.com/docs/buildpacks/python#application_entrypoint).

## June 27, 2023

Change

The default generic builder now uses the Ubuntu 22 LTS base image. When you specify the `latest` location, the builds now uses the `google-22` builder by default. For example, you can specify either of the following to use `google-22`:

  * `gcr.io/buildpacks/builder:latest`
  * `gcr.io/buildpacks/builder:google-22`



If you need to pin your build to the previous Ubuntu 18 builder, see the [instructions about how to configure the builder version](https://docs.cloud.google.com/docs/buildpacks/use-a-specific-builder), including:

  * `pack` commands for local builds.
  * `gcloud` commands for remote builds.
  * How to configure the `project.toml` for Cloud Run.



## June 22, 2023

Feature

The Java runtime now supports using [Maven wrappers](https://docs.cloud.google.com/docs/buildpacks/java#configure_maven) for managing your project's dependency on Maven.

## June 01, 2023

Feature

You can use the [Pnpm](https://pnpm.io/installation) package manager to configure dependencies for Node.js runtimes. [Learn how to configure your application](https://docs.cloud.google.com/docs/buildpacks/nodejs#installing_dependencies).

## April 26, 2023

Announcement

Starting June 5, 2023, the default generic builder will begin using the Ubuntu 22 LTS base image. This means that builds using `gcr.io/buildpacks/builder:latest` will get the `google-22` builder which addresses multiple security issues. You can read more about the `google-22` builder in our [announcement on GitHub](https://docs.cloud.google.com/docs/buildpacks/github/buildpacks/discussions/271).

You can preview the new builder by adding `--builder=gcr.io/buildpacks/builder:google-22` to the `gcloud builds submit --pack` command when you build your application with a [specific builder](https://docs.cloud.google.com/docs/buildpacks/use-a-specific-builder).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
