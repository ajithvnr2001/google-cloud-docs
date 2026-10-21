---
url: https://docs.cloud.google.com/compute/docs/containers/cluster-services-for-openshift-overview/
title: Overview of Cluster Services for OpenShift \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:09:07.786187+00:00
---

# Overview of Cluster Services for OpenShift  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/containers/cluster-services-for-openshift-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Services for OpenShift ](https://docs.cloud.google.com/openshift-cluster)
  * [ Guides ](https://docs.cloud.google.com/openshift-cluster/overview)



Send feedback 

#  Overview of Cluster Services for OpenShift Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of Cluster Services for OpenShift. 

Cluster Services for OpenShift is a Google Cloud service that provides built-in OpenShift integrations with Google services for self-managed OpenShift clusters that run on Google Cloud.

These integrations make it easier for you to perform core operations for your OpenShift clusters, such as identity management, authentication, compute management, storage management, networking, and monitoring.

This document is intended for cloud architects, platform administrators, and developers who develop, deploy, or manage enterprise grade applications on OpenShift clusters that run on Google Cloud.

## Get joint support from Google Cloud and Red Hat

Cluster Services for OpenShift is jointly engineered and supported by Google Cloud and Red Hat.

## Use Google services through OpenShift mechanisms

OpenShift environments use standardized APIs and middleware to integrate with services and create solutions for requirements such as compute, networking, storage, and monitoring. These standardized mechanisms help you preserve platform cohesiveness across the hybrid cloud.

Creating solutions for your self-managed OpenShift clusters by using Cluster Services for OpenShift includes the following benefits:

  * You can benefit from the customizations that Cluster Services for OpenShift provides for Google services. These customizations are engineered so that these Google services work best for OpenShift use cases.
  * These customizations include adaptations in the underlying Google Cloud services themselves, as well as in the integration layers.



For information about the Google services that Cluster Services for OpenShift lets you use with OpenShift clusters on Google Cloud, and the supported service-specific customizations, see [Supported integrations](https://docs.cloud.google.com/openshift-cluster/supported-integrations).

## Automatic configuration validation tooling

Automatic configuration validation tooling ([Preview](https://cloud.google.com/products#product-launch-stages)) is a rule-based validation service that uses Google Cloud's Workload Manager to evaluate your OpenShift clusters that run on Google Cloud. The automatic configuration validation tooling scans your OpenShift clusters and their integration with Google Cloud managed services. The tooling detects deviations from standards, rules, and best practices and helps you improve system quality, reliability, and performance.

For more information, see [Automate cluster configuration validation](https://docs.cloud.google.com/openshift-cluster/automate-cluster-config-validation).

## Benefits in migration or hybrid-cloud scenarios

Cluster Services for OpenShift is particularly useful when you're migrating self-managed OpenShift clusters from on-premises environments to Google Cloud.

Self-managed OpenShift clusters that run in on-premises environments typically rely on self-managed solutions for core operations such as storage, networking, monitoring, secret management, certificate authorities. When you migrate such clusters to the cloud, you'd typically have to make a hard choice between refactoring your cluster into a fully-managed platform such as Google Kubernetes Engine or lift-and-shift your cluster with the existing self-managed solutions.

Refactoring your cluster and its components into a managed platform such as Google Kubernetes Engine can demand significant efforts from you, notably when there are pre-existing platform, application, or corporate policy dependencies on the solutions that you're using in your clusters for purposes like storage, networking, and monitoring.

The lift-and-shift choice, which minimizes the refactoring cost and associated risks, leaves you with an operating model that doesn't fully take advantage of the features that a cloud platform typically offers.

Cluster Services for OpenShift is designed to provide you the flexibility to optimize your OpenShift architecture with the right balance between refactoring your cluster and continuing to use self-managed solutions. This flexibility is provided through the following capabilities of Cluster Services for OpenShift:

  * **Support for OpenShift clusters with self-managed control planes:** Cluster Services for OpenShift lets you run OpenShift clusters, that have self-managed control planes, on Google Cloud. This capability lets you use a cloud based operating model with self-managed solutions in your OpenShift clusters.
  * **Support for selective adoption of cloud services:** Cluster Services for OpenShift lets you opt into using any of the supported Google services to create solutions for the applications that run on your clusters. This capability lets you take advantage of a cloud based operating model.



To help you find the right balance between adopting managed services and retaining your existing self-managed solutions, Google Cloud recommends that you request an OpenShift migration assessment. For more information, see [Migrate OpenShift clusters to Google Cloud](https://docs.cloud.google.com/openshift-cluster/plan-deployment#migrate-openshift-to-gc).

## What's next

  * Learn about the [supported integrations](https://docs.cloud.google.com/openshift-cluster/supported-integrations) for OpenShift clusters that run on Google Cloud



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
