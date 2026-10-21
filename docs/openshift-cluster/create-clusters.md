---
url: https://docs.cloud.google.com/openshift-cluster/create-clusters/
title: Create an OpenShift cluster \u00a0|\u00a0 Cluster Services for OpenShift \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:07:51.546144+00:00
---

# Create an OpenShift cluster  |  Cluster Services for OpenShift  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/openshift-cluster/create-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Services for OpenShift ](https://docs.cloud.google.com/openshift-cluster)
  * [ Guides ](https://docs.cloud.google.com/openshift-cluster/overview)



Send feedback 

#  Create an OpenShift cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to create a managed or self-managed Red Hat OpenShift cluster on Google Cloud.

In partnership with Red Hat, Google Cloud helps you run robust OpenShift clusters reliably, securely, and cost-effectively. For more information about the features and benefits of running OpenShift clusters on Google Cloud, see [Overview of OpenShift on Google Cloud](https://docs.cloud.google.com/openshift-cluster/openshift-overview).

This document is intended for administrators who set up OpenShift clusters for organizations on Google Cloud.

## Before you begin

Before you create an OpenShift cluster on Google Cloud, you must meet the following prerequisites:

  * You must have a Google Account and an existing Google Cloud project. For information about how to create a Google Cloud project, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).



## Create a self-managed OpenShift cluster

To create a self-managed OpenShift cluster on Google Cloud, complete the following steps:

  1. In the Google Cloud console, go to the **Red Hat OpenShift on Google Cloud** page.

[Go to Red Hat OpenShift on Google Cloud](https://console.cloud.google.com/redhat-openshift/landing)

  2. Click **Create an OpenShift cluster**.

  3. In the dialog that appears, select **Self-managed (OpenShift Container Platform)** and then click **Continue**.

  4. Review and follow the instructions that are displayed.

For information from Red Hat about how to create a self-managed cluster, see [Preparing to install on Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/installing_on_google_cloud/index).




## Create a managed OpenShift cluster

To create a managed OpenShift cluster on Google Cloud, complete the following steps:

  1. In the Google Cloud console, go to the **Red Hat OpenShift on Google Cloud** page.

[Go to Red Hat OpenShift on Google Cloud](https://console.cloud.google.com/redhat-openshift/landing)

  2. Click **Create an OpenShift cluster**.

  3. In the dialog that appears, select **Managed (OpenShift Dedicated)** and then click **Continue**.

  4. In the **OpenShift Dedicated prerequisite check** page, complete the following steps:

     1. In the **Google Cloud Marketplace terms and agreements** section, review the terms and agreements, select the checkbox, and then click **Accept**.

     2. In the **IAM permissions** section, review and grant any missing IAM permissions. If you already have the required IAM permissions, then you see a **Passed** status.

     3. In the **API and services** section, review and enable any missing APIs.

        * To enable the missing APIs, you can click **Enable**.
        * If all the required APIs are already enabled, then see a **Passed** status.
     4. In the **Cloud quotas** section, select the region where you want to create the managed cluster, and then verify that sufficient quotas are available.

     5. As instructed in the **Organization policies** section, review the information and configure the required organization policies.

     6. In the **VPC network and subnetworks configuration** section, review the provided information and configure a VPC network for your cluster.

For information about how to create a VPC network, see [Create and manage VPC networks](https://docs.cloud.google.com/vpc/docs/create-modify-vpc-networks).

     7. In the **Billing** section, review the provided information.

     8. Click **Continue to Red Hat**. You're taken to the Red Hat OpenShift Cluster Manager, where you complete the remaining steps.

For information from Red Hat about how to create a managed cluster, see [OpenShift Dedicated clusters on Google Cloud](https://docs.redhat.com/en/documentation/openshift_dedicated/4/html/openshift_dedicated_clusters_on_google_cloud/index).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
