---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/prerequisites/
title: Prerequisites \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:46:21.896079+00:00
---

# Prerequisites  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/prerequisites/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Prerequisites Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.9 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.9 (unsupported)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/prerequisites.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/prerequisites.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/prerequisites.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/prerequisites.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/prerequisites.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/prerequisites.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/prerequisites.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/prerequisites.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/prerequisites.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/prerequisites.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/prerequisites.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/prerequisites.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/prerequisites.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/prerequisites.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/prerequisites.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/prerequisites.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/prerequisites.html)



Before you can install Apigee hybrid, you must meet the following prerequisites:

Done? | Prerequisite | Description  
---|---|---  
| **Google Cloud billing account** | You must have a Google Cloud account with active billing. For more information, see [Create a new billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account#create_a_new_billing_account).  
| **Google Cloud project** |  Create a new Google Cloud project for the Apigee hybrid installation. For more information, see [Creating a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project). If you'd prefer to use Cloud Identity to manage your organizational identity with Apigee, see [Cloud Identity Help](https://support.google.com/cloudidentity#topic=7516500). Although not needed for Apigee hybrid, Cloud Identity might be useful if you plan to use other Google Cloud services or have multiple members of your organization access the product.   
| **Clock synchronization** | Apigee hybrid uses the Cassandra database, and Cassandra relies on Network Time Protocol (NTP) synchronization to maintain data consistency. Before you begin your hybrid installation, we recommend you use Network Time Protocol (NTP) to synchronize the clocks on all nodes and application servers. If you plan to install hybrid into multiple regions, be sure they are synchronized with NTP across all regions.   
| **Software** | Install the following software on your administrative machine:

  * [gcloud CLI](https://docs.cloud.google.com/sdk/docs/install) (required for command line provisioning steps). 
    * After the gcloud CLI is installed, run `gcloud components update` to get the latest gcloud components.
  * [`curl`](https://curl.haxx.se/) (recommended)
  * If you are installing Apigee hybrid on EKS and you are using Kubernetes 1.24 or newer, install the [Kubernetes CSI driver for Amazon EBS](https://github.com/kubernetes-sigs/aws-ebs-csi-driver). 

  
| **Hardware** | Review the following information before installing hybrid:

  * [Configure Cassandra for production](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-production)
  * [Configuring TLS for Cassandra](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cassandra-tls)
  * [Minimum cluster configurations](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/cluster-overview)
  * [Secure ports usage](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/ports)

  
**Note:** If you plan to enable Google Cloud [ Virtual Private Cloud (VPC) Service Controls](https://cloud.google.com/vpc-service-controls) with your Apigee hybrid installation, see [Using VPC Service Controls with Apigee and Apigee hybrid](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc) for instructions before you proceed.

##  Next step 

Each of these steps is described in the sections that follow.

[Let's Go!](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/precog-overview)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
