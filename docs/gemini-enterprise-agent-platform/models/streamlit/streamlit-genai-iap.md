---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/streamlit-genai-iap/
title: Secure a generative AI app by using IAP \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:09.737080+00:00
---

# Secure a generative AI app by using IAP  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/streamlit-genai-iap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ Models ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)



Send feedback 

#  Secure a generative AI app by using IAP Stay organized with collections  Save and categorize content based on your preferences. 

This tutorial shows you how to deploy a generative AI app to Cloud Run and secure it with Identity-Aware Proxy (IAP). IAP provides a central authorization layer for HTTPS applications deployed to Cloud Run. You can use IAP to adopt application-level or organization-level access control policies instead of using network-level firewalls.

Note that while it's also possible to use manual or third-party authentication to secure an app deployed to Cloud Run, we recommend using IAP for large volumes or multi-region traffic, to avoid disruptions in the app serving.

In this tutorial, you deploy an app that makes calls to the [Gemini API](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.endpoints/generateContent). The app is based on the Streamlit framework.

## Prerequisites

This tutorial assumes that you're able to use the following tools and frameworks:

  * **Streamlit** : [Streamlit](https://streamlit.io/) is an open source app framework that lets you create and deploy data applications. It transforms data scripts into web apps by using Python.

  * **Git** : For this tutorial, you use a Git repository to manage the source code of your app. For more information about using Git, see the [Git documentation](https://git-scm.com/doc).




### Google Cloud services

You must have a basic understanding of the following Google Cloud services:

  * **Generative AI on Agent Platform** : Provides access to Google's LLMs so you can test, tune, and deploy them for use in your applications. [Learn more about Generative AI on Agent Platform.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models)

  * **Cloud Run** : A managed compute platform that lets you deploy and run container images. You create a Cloud Run service to deploy your app. [Learn more about Cloud Run.](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)

  * **Cloud Build** : Executes your builds on Google Cloud. For this tutorial, you set up an automatic [Cloud Build trigger](https://docs.cloud.google.com/build/docs/triggers) to build and deploy your app to Cloud Run whenever you push your commits to the Git repository. [Learn more about Cloud Build.](https://docs.cloud.google.com/build/docs/overview)

  * **Cloud Load Balancing** : Helps distribute traffic across multiple instances of your app to achieve scalability. You create an Application Load Balancer to distribute the traffic to the app backend instances hosted on Cloud Run. Cloud Load Balancing is also a prerequisite for IAP. [Learn more about Cloud Load Balancing.](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)

  * **Identity-Aware Proxy (IAP)** : You use IAP to create a central authorization layer to secure the app. IAP makes authentication and authorization checks that extend to linked Google Cloud services. IAP also supports and seamlessly integrates with Cloud Load Balancing, making it the most efficient security management option for this tutorial.

To learn more about IAP, see [Identity-Aware Proxy overview](https://docs.cloud.google.com/iap/docs/concepts-overview).

To understand how IAP works with Cloud Run, see the [Cloud Run section of How IAP Works](https://docs.cloud.google.com/iap/docs/concepts-overview#how_iap_works).




### Valid domain name

Additionally, you must have a valid domain name for provisioning a certificate, which is required to configure the load balancer.

## Tutorial pages

This tutorial has the following pages:

  1. [Set up your project and source repository.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/setup-environment)

  2. [Create a Cloud Run service.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/create-cloudrun-service)

  3. [Create a load balancer.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/create-loadbalancer)

  4. [Configure Identity-Aware Proxy (IAP).](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/configure-iap)

  5. [Test your IAP-secured app.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/view-app)

  6. [Clean up your project.](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/clean-up)




Each page assumes that you've already completed the instructions from the previous pages of the tutorial.

[ Next Set up your project and source repository  arrow_forward  ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/streamlit/setup-environment)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
