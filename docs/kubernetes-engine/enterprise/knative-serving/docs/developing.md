---
url: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/developing/
title: Developing your service \u00a0|\u00a0 Knative serving \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:08:41.631443+00:00
---

# Developing your service  |  Knative serving  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/developing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Knative serving ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/architecture-overview)



Send feedback 

#  Developing your service Stay organized with collections  Save and categorize content based on your preferences. 

This page describes a few things you need to know to get started in developing a service for Knative serving.

## Code requirements

You must meet the following requirements when you develop a service:

  * The service must listen for requests. You can [configure the port](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/configuring/containers#configure-port) on which requests are sent. Inside Knative serving container instances, the value of the `PORT` environment variable always reflects the port to which requests are sent. Your code should check for the existence of this `PORT` environment variable and if it is present, should listen on it to maximize portability.
  * The service must be _stateless_. It cannot rely on a persistent **local** state.
  * The service must not perform background activities outside the scope of request handling.



You can find more details about these constraints in the [Container Runtime Contract](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/reference/container-contract).

## Programming language support

Knative serving allows you to write code in the programming language of your choice.

## Using a web server

You can use a web server to listen on the required port, and to process and route incoming requests. For example, Node.js developers can use [Express.js](https://expressjs.com/), Python developers can use [Flask](http://flask.pocoo.org/), Ruby developers can use [Sinatra](http://sinatrarb.com/), and so forth.

## Containerizing your code

To deploy to Knative serving, you need to provide a _container image_. A container image is a packaging format that includes your code, its packages, any needed binary dependencies, the operating system to use, and anything else needed to run your service.

A file named [Dockerfile](https://docs.docker.com/engine/reference/builder/) is commonly used to declare how to build the container image.

Dockerfiles very often start from a base image (e.g. `FROM golang:1.11`). You can find base images maintained by OS and language authors on [Docker Hub](https://hub.docker.com/). Cloud Build checks for [cached images](https://docs.cloud.google.com/container-registry/docs/pulling-cached-images) before pulling from Docker Hub. If you use a third-party build tool, you can configure your Docker daemon to check for images in the same cache. You can also find base images managed by Google in the [Google Cloud Marketplace](https://console.cloud.google.com/marketplace/browse?filter=solution-type:container&filter=category:os).

**Note:** As of November 1, 2020, Docker Hub [ rate limits](https://www.docker.com/blog/scaling-docker-to-serve-millions-more-developers-network-egress/) apply to unauthenticated or authenticated pull requests on the Docker Free plan. To avoid disruptions and have greater control over your software supply chain, you can migrate your dependencies to [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/docker/migrate-external-containers).

If you bring your own binaries, make sure they are compiled for Linux ABI x86_64.

These resources provide further information on Dockerfiles:

  * Learn Dockerfile syntax through the [Dockerfile reference](https://docs.docker.com/engine/reference/builder).
  * Learn how Dockerfiles fit together through the tips in [Best practices for writing Dockerfiles](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/).



## What's next

  * Once you have your service code and Dockerfile, you should [build a container image](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/building/containers) then continue iterating in [local testing](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/testing/local).
  * If you are migrating an existing web application, see [Migrating Your Service to Knative serving](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/migrating).
  * For best practices for designing, implementing, testing, and deploying a service in Knative serving, see the [Development tips](https://docs.cloud.google.com/kubernetes-engine/enterprise/knative-serving/docs/tips/general).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
