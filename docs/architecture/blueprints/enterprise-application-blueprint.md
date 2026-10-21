---
url: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/
title: Deploy an enterprise developer platform on Google Cloud \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:36.548971+00:00
---

# Deploy an enterprise developer platform on Google Cloud  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Deploy an enterprise developer platform on Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-13 UTC

As enterprises shift to container-based application development and deployment, they must learn how to manage distributed teams with separate engineering workflows. To help large enterprises complete the shift to container-based applications, we created the _enterprise application blueprint_. This blueprint deploys an [internal developer platform](https://internaldeveloperplatform.org/) that enables cloud platform teams to provide a managed platform for software development and delivery that their organization's application development groups can use.

The enterprise application blueprint includes the following:

  * A [GitHub repository](https://github.com/GoogleCloudPlatform/terraform-google-enterprise-application) that contains a set of Terraform configurations and scripts. The Terraform configuration sets up a developer platform in Google Cloud that supports multiple development teams.
  * A guide to the architecture, design, security controls, and operational processes that you use this blueprint to implement (this document).



The enterprise application blueprint is designed to be compatible with the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations). The enterprise foundations blueprint provides a number of base-level services that the enterprise application blueprint relies on, such as Cloud Identity. You can deploy the enterprise application blueprint without deploying the enterprise foundations blueprint if your Google Cloud environment provides the [necessary functionality to support the enterprise application blueprint](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/deploy-blueprint#deploy-without-efb).

This document is intended for cloud architects and assumes that you're using the enterprise application blueprint to deploy new enterprise applications on Google Cloud. However, if you already have existing containerized enterprise applications on Google Cloud, you can [incrementally adopt this reference architecture](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/deploy-blueprint#incorporate-the-blueprint-into-your-existing-gke-deployment).

This document also assumes that you understand Kubernetes components, including services, namespaces and clusters. For background information on Kubernetes and its implementation in Google Cloud, see the [Google Kubernetes Engine technical overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview).

### Enterprise application blueprint overview

In most enterprises, a developer platform manages the shared infrastructure that is used by all developers. The developer platform creates build pipelines, deployment pipelines, and runtime environments for each application component on demand. Developer teams and application operators have access to only those application components for which they are responsible. The platform is designed to support the deployment of highly available and secure applications.

This blueprint deploys a developer platform on top of the enterprise foundations blueprint (or its equivalent). The developer platform includes resources such as Google Kubernetes Engine (GKE) clusters, GKE fleet, the application factory, infrastructure pipelines, platform monitoring, and platform logging. In addition, the developer platform sets up the users (developer platform administrators and application developers) who manage the solution.

This blueprint enables organizations to provide different application development teams (called _tenants_) access to the platform. A tenant is a group of users with common ownership over a set of resources. A tenant owns one or more _applications_ that run on the platform as a container-based service. An application on the developer platform is a bundle of source code and configuration. Each application is built and deployed by a dedicated CI/CD pipeline. Tenants and applications are isolated from one another at run time and in the CI/CD pipelines. Portions of the blueprint provide automation are used by all tenants, and are referred to as _multi-tenant_.

To illustrate how the developer platform is used, the blueprint includes a sample application, called _Cymbal Bank_. Cymbal Bank is a microservices application that is designed to run on GKE. The application is intended to simulate a highly-available application that is deployed in an active-active configuration to enable disaster recovery. Cymbal Bank assumes that the application is developed and operated by several independent developer teams.

## What's next

  * Read about [architecture](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/architecture) (next document in this series).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-13 UTC."],[],[]] 
