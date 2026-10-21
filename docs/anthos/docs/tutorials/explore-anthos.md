---
url: https://docs.cloud.google.com/anthos/docs/tutorials/explore-anthos/
title: Learning Path: Scalable applications - Overview \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T18:37:42.380275+00:00
---

# Learning Path: Scalable applications - Overview  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/docs/tutorials/explore-anthos/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Learning Path: Scalable applications - Overview Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This set of tutorials is for IT administrators and Operators who want to learn how to deploy, run, and manage modern application environments that run on Google Kubernetes Engine (GKE).

In this set of tutorials, you learn by doing. You start by deploying a sample microservices-based application named Cymbal Bank to a GKE cluster. Cymbal Bank uses Python and Java to run the various services, and includes a PostgreSQL backend. You don't need experience with these languages or database platform to complete the series of tutorials, as Cymbal Bank is just an example application to show how GKE can support the needs of your business. Each tutorial then builds on this sample application to show how a real production environment might look as you use different Google Cloud products and services to fit your business needs and goals.

As you progress through this set of tutorials, you explore the following key learning areas:

  * **Modern application foundations** : Deploy a single Google Kubernetes Engine cluster that runs a microservices-based application.
  * **Monitoring** : Use Prometheus to monitor the performance and health of your applications.
  * **Autoscale and load balance** : Scale your cluster to meet application demand with GKE Autopilot, and use horizontal Pod autoscaling.
  * **Simulate and test failovers** : Verify that your highly available and geographically distributed deployment can failover to maintain access for customers.
  * **Centralize change management** : Minimize configuration drift and apply consistent changes with Config Sync.



The tutorials are designed for you to complete in order. Each tutorial builds on the previous tutorial as you create a sample application infrastructure that you can monitor and autoscale. As you progress through the set of tutorials, you learn new skills and use additional Google Cloud products and services. The goal is that you learn all of the core components that are needed to feel more comfortable running scalable applications in your own environment.

## Your journey

For this set of tutorials, you play the role of the platform lead at Cymbal Bank. Cymbal Bank started as a small business for payment processing on two servers almost ten years ago. Since then, it has grown into a successful commercial bank with thousands of employees and a growing engineering organization. Cymbal Bank now wants to expand its business further.

Throughout this period, you and your team have found yourself spending more time and money on maintaining infrastructure than on creating new business value. You have decades of cumulative experience invested in your existing stack; however, you know it's not the right technology to meet the scale of global deployment that the bank needs as it expands.

You've adopted GKE to modernize your application and migrate successfully to Google Cloud to achieve your expansion goals.

## Costs

Enabling GKE and deploying the Cymbal Bank sample application for this series of tutorials means that you incur per-cluster charges for GKE on Google Cloud as listed on our [Pricing page](https://cloud.google.com/kubernetes-engine/pricing) until you disable GKE or delete the project.

You are also responsible for other Google Cloud costs incurred while running the Cymbal Bank sample application, such as charges for Compute Engine VMs and load balancers.

## Before you begin

You don't need to be familiar with Google Kubernetes Engine or Terraform to follow these tutorials, but ensure that you're familiar with [basic Kubernetes concepts](https://kubernetes.io/docs/tutorials/kubernetes-basics/), such as clusters.

Each tutorial outlines specific prerequisites, such as needing a Google Cloud billing account and project or IAM roles.

## Planning considerations

When you plan a production GKE environment, there are a number of planning considerations to keep in mind. These considerations include available networking options, your cluster management mode, and cluster availability.

In this set of tutorials, some of these considerations are simplified so that you can focus on learning about key GKE features and services. Because of this, these tutorials don't provide a complete production-ready environment, but rather give you the building blocks you need to learn how to deploy and run your own workloads. After you complete this set of tutorials, we recommend you review [Scalable apps - Production considerations](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-considerations).

## What's next

Get started by completing the [first tutorial to a deploy a single GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps-basic-deployment) that runs a microservices-based application.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
