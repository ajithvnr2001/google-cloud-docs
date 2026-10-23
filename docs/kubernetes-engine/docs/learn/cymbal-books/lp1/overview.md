---
url: https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/overview/
title: Learning Path: Transform a monolith into a GKE app - Overview \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:32.574026+00:00
---

# Learning Path: Transform a monolith into a GKE app - Overview  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Learning Path: Transform a monolith into a GKE app - Overview Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This series of tutorials is for Developers who are new to Kubernetes and Google Kubernetes Engine (GKE). In the series, you learn how to transform Cymbal Books, a sample monolithic app, into a modular, containerized app that runs on a GKE cluster.

Before starting this tutorial series, it's helpful if you have some experience with Python programming and web application development. Although all the code is provided and you won't need to write any code yourself, being able to read and understand basic Python code will help you follow along better. You also need to be comfortable using the command line to run commands. If you're new to Google Cloud, containerization, or Kubernetes, don't worry—these concepts are explained in the series.

## Costs

You can complete this tutorial without incurring any charges. However, following the steps in the [final tutorial](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/deploy) of this series incurs charges on your Google Cloud account. Costs begin when you enable GKE and deploy the Cymbal Books app to a GKE cluster. These costs include per-cluster charges for GKE, as outlined on the [Pricing page](https://cloud.google.com/kubernetes-engine/pricing), and charges for running Compute Engine VMs.

To avoid unnecessary charges, ensure that you disable GKE or delete the project once you have completed this tutorial.

## Why containerize an app?

You might be wondering why you'd want to containerize your app. The following list explains some of the advantages of containerized apps:

  * **Isolation** : each component runs independently in its own container. Changes or updates to one component don't disrupt the rest of the app.
  * **Scalability** : you can scale individual components based on demand. If one part of the app experiences high load, you can scale only that part. You don't need to scale the entire app.
  * **Fault isolation** : issues in one component are contained and don't affect other components. This isolation makes it easier to debug and resolve issues without affecting the rest of the system.
  * **Faster development and deployment** : teams can work on different components of the app simultaneously. They can develop, test, and deploy independently, which can speed up development cycles.
  * **Resource efficiency** : containers help optimize resource usage, which can reduce the costs of running your app.
  * **Consistency across environments** : each container runs the same way in different environments, such as development, testing, and production.



## Tutorials in this series

The series consists of the following tutorials:

  1. Overview (this tutorial)
  2. [Understand the monolith](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/monolith)
  3. [Modularize the monolith](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/modular)
  4. [Prepare the modular app for containerization](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/prep-containerization)
  5. [Containerize the modular app](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/containerize)
  6. [Deploy the app to a GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/deploy)



Each tutorial builds on the previous one, and helps you understand key concepts and practices in app modularization, containerization, and deployment. By the end of the series, you'll have an app that's running on GKE and a solid understanding of modularization, containerization, and Kubernetes basics.

To get started, see [Understand the monolith](https://docs.cloud.google.com/kubernetes-engine/docs/learn/cymbal-books/lp1/monolith).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
