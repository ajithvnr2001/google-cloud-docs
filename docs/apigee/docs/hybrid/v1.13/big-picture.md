---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/big-picture/
title: The big picture \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:49:03.603444+00:00
---

# The big picture  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/big-picture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  The big picture Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.13 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.13 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/big-picture.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/big-picture.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/big-picture.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/big-picture.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/big-picture.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/big-picture.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/big-picture.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/big-picture.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/big-picture.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/big-picture.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/big-picture.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/big-picture.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/big-picture.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/big-picture.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/big-picture.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/big-picture.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/big-picture.html)



Using Apigee hybrid is a three-part process:

| 

### Part 1:  
CONFIGURE GOOGLE CLOUD AND UI  
  
---  
Get your project and organization set up with Google Cloud and hybrid UI. **Prerequisites:**

  * Created Google Cloud account and project
  * Install gcloud CLI
  * 
**When you're done:**

  * Enabled APIs
  * Created an organization
  * Created an environment and environment group
  * 
  
[1: Configure it](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/precog-overview)  
| 

### Part 2:  
INSTALL THE RUNTIME  
  
---  
Install the runtime in your cluster with this quickstart. **Prerequisites:**

  * Complete [Part 1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/precog-overview)
  * Verify [Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/prerequisites)
  * 
**When you're done:**

  * Created a Kubernetes cluster
  * installed and set up [Helm v3.14.2+](https://helm.sh/docs/intro/install/).  

  * Created the required service accounts and assigned roles to them 
  * Customized your Apigee instance
  * Checked cluster readiness
  * Set up Synchronizer access
  * Installed the Apigee runtime
  * Exposed the Apigee ingress gateway, and tested proxy traffic through it
  * 
  
[2: Install it](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-before-begin)  
| 

### Part 3:  
CREATE A PROXY AND TEST YOUR HYBRID INSTALLATION  
  
---  
Get your project and organization set up with Google Cloud and hybrid UI. **Prerequisites:**

  * Configured your overrides
  * Installed the Apigee hybrid runtime
  * 
**When you're done:**

  * Set up and exposed your ingress gateway
  * Created your first proxy
  * Tested your Hybrid installation
  * 
  
[3: Test it](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-expose-apigee-ingress)  
**Note:** The procedures in this guide contain code samples you can copy and modify. Many code samples include variables in red text that you can edit before copying. 

Most samples are written for the Linux/UNIX/Mac command shell. If you are using Windows, substitute the correct Windows command line syntax. When there are significant differences between the Linux/UNIX/Mac and the Windows syntax, the examples are followed by specific Windows examples. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
