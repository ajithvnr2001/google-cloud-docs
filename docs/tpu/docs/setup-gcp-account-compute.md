---
url: https://docs.cloud.google.com/tpu/docs/setup-gcp-account-compute/
title: Set up a Google Cloud project for TPUs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:54:01.268287+00:00
---

# Set up a Google Cloud project for TPUs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/setup-gcp-account-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up a Google Cloud project for TPUs

This document describes how to set up your Google Cloud project to use Cloud TPU VMs:

  * Create a Google Cloud project
  * Configure your Google Cloud project for Cloud TPU



## Create a Google Cloud project

  1. In the Google Cloud console, [sign in](https://accounts.google.com/Login) to your Google Account or [sign up for a new account](https://accounts.google.com/SignUp).

  2. Create a Google Cloud project. For more information, see [Create a project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#creating_a_project).

  3. [Enable billing for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled). For more information, see the [Cloud Billing documentation](https://docs.cloud.google.com/billing/docs/concepts).

Billing for all Cloud TPU versions uses the standard regional pricing on the [Cloud TPU pricing page](https://cloud.google.com/tpu/pricing).




## Configure your Google Cloud project for Cloud TPU

You can configure your Google Cloud project using the Cloud Shell, a Compute Engine VM, or your local machine. The [Cloud Shell](https://docs.cloud.google.com/shell/docs) lets you interact with TPU VMs without installing any software. The Cloud Shell disconnects after a period of inactivity. If you run long-running commands, you should install the Google Cloud CLI on your local machine. For more information about the Google Cloud CLI, see the [`gcloud` Reference](https://docs.cloud.google.com/sdk/gcloud/reference).

  1. If you use a local machine or a Compute Engine VM, [install the Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install). The Google Cloud CLI includes the `gcloud` command, which you use to work with Google Cloud resources and services.

**Note:** If you need a specific release of gcloud CLI components, install these components to ensure that relevant commands and flags are supported. For example, for alpha components, run `gcloud components install alpha`.**Note:** If you installed the gcloud CLI previously, ensure you have the latest version by running `gcloud components update`.
  2. Configure the `gcloud` command to use your project.
         
         export PROJECT_ID=your-project-id
         gcloud config set project $PROJECT_ID

  3. Activate the Compute Engine API using `gcloud` or the Google Cloud console:

### gcloud
         
         gcloud services enable compute.googleapis.com
         

### Console

     1. In the Google Cloud console, go to the **Compute Engine API** page.

[Go to Compute Engine API](https://console.cloud.google.com/apis/library/compute.googleapis.com)

     2. Click **Enable**.

  4. Ensure your Google Cloud account has the following roles in your project:

     * [**Compute Instance Admin (v1)**](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1): This role lets you create and manage Compute Engine instances.
     * [**Service Account User**](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser): This role lets you run operations as a service account.
     * [**Service Account Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin): This role lets you create a service account.
     * [**Project IAM Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin): This role lets you grant a role in a project.

To view your current roles, see [View current access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#iam-view-access-console).

To add any missing roles, see [Grant a single IAM role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role) or ask your administrator to grant these roles for you.

  5. Create a TPU service account:

Service accounts provide credentials for your TPU VMs to access other Google Cloud resources. To improve security, create a user-managed service account that has only the permissions your TPU VM requires. To use it, specify the service account with the `--service-account` flag when you create the TPU VM.

     1. Follow the instructions in [Create service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-create) to create a user-managed service account.

     2. Grant your service account the following roles so your TPU VM can access common Google Cloud services:

        * [**Storage Admin**](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin): This role provides access to Cloud Storage.
        * [**Logs Writer**](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.logWriter): This role lets you write logs with the Cloud Logging API.
        * [**Monitoring Metric Writer**](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.metricWriter): This role lets you write metrics to Cloud Monitoring.
**Note:** If you don't specify a custom service account, your Cloud TPU uses the [default Compute Engine service account](https://docs.cloud.google.com/compute/docs/access/service-accounts#default_service_account%7D).



## What's next

  * Learn how to [plan your Cloud TPU resources](https://docs.cloud.google.com/tpu/docs/plan-tpus)
  * Learn how to [create TPUs](https://docs.cloud.google.com/tpu/docs/create-tpu-vm)
  * Learn how to [manage TPUs](https://docs.cloud.google.com/tpu/docs/managing-tpus-tpu-vm)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
