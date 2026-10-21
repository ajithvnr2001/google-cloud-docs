---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/big-picture/
title: The big picture \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:24:28.243063+00:00
---

# The big picture  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/big-picture/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  The big picture Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.10 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.10 keyboard_arrow_down

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



Using Apigee hybrid is a two-part process:

See a video walkthrough of installing Apigee hybrid on GKE

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
  
[1: Configure it](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/precog-overview)  
| 

### Part 2:  
INSTALL THE RUNTIME  
  
---  
Install the runtime in your cluster with this quickstart. **Prerequisites:**

  * Complete [Part 1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/precog-overview)
  * Verify [Prerequisites](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/prerequisites)
  * 
**When you're done:**

  * Created a Kubernetes cluster
  * Installed `apigeectl` and set up your local Apigee directory structure
  * Created the required service accounts and assigned roles to them 
  * Customized your Apigee instance
  * Checked cluster readiness
  * Set up Synchronizer access
  * Installed the Apigee runtime
  * Exposed the Apigee ingress gateway, and tested proxy traffic through it
  * 
  
[2: Install it](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-before-begin)  
**Note:** The procedures in this guide contain code samples you can copy and modify. Many code samples include variables in red text that you can edit before copying. 

Most samples are written for the Linux/UNIX/Mac command shell. If you are using Windows, substitute the correct Windows command line syntax. When there are significant differences between the Linux/UNIX/Mac and the Windows syntax, the examples are followed by specific Windows examples. 

##  Video Walkthrough: Setup Apigee hybrid in GKE 

The following example walks through installation of Apigee hybrid v1.8.0 on GKE. This is an example of a hybrid installation, and not a tutorial. 

**Note:** This video was filmed installing Apigee hybrid v1.8.0 on GKE. See the instructions in this documentation for installation on other platforms. Apigee hybrid may have changed in subsequent releases. The main points of installation will have remained the same or similar. 

For a discussion of this video in the Google Cloud Community, see [Walkthrough: Setup Apigee hybrid 1.8 in GKE](https://www.googlecloudcommunity.com/gc/Apigee/Walkthrough-Setup-Apigee-hybrid-1-8-in-GKE/m-p/469708). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
