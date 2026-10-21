---
url: https://docs.cloud.google.com/spanner/docs/configure-virtual-machine-instance/
title: Using Spanner in a virtual machine instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:14.209131+00:00
---

# Using Spanner in a virtual machine instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/configure-virtual-machine-instance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Using Spanner in a virtual machine instance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to grant your Compute Engine [virtual machine instance](https://docs.cloud.google.com/compute/docs/instances) permission to access a Spanner database.

Your instance can access the Cloud Spanner API from Compute Engine by using a service account to act on your behalf. The service account provides [application default credentials](https://developers.google.com/identity/protocols/application-default-credentials) for your applications so that you don't need to configure each Compute Engine instance to use your personal user credentials.

Configure the service account on your instance with one of the following options:

  * For easy development and testing, configure your instance to use the default service account with full access to all Cloud APIs.
  * For production environments, create a service account with read and write access to your Spanner databases and apply it to your instance.



## Configure an instance with access to all Cloud APIs

To quickly allow your instance to access the Cloud Spanner API, create a new instance to use the default service account and a scope with full access to all Cloud APIs.

  1. Go to the Compute Engine VM instances page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Select your project and click **Continue**.

  3. Click **Create Instance** to start creating a new instance.

  4. In the **Identity and API access** section, click **Allow full access to all Cloud APIs**.

  5. Configure other instance settings as needed, then click **Create**.




Now that the service account on your Compute Engine instance has access to the Cloud Spanner API, [use a client library](https://docs.cloud.google.com/spanner/docs/tutorials) to read and write data in your Spanner database. The instance uses the credentials from the default service account to authenticate with the Cloud Spanner API.

## Configure an instance with a service account

To restrict instance access to specific APIs and roles, create a service account with permission only to access your Spanner databases. Then, apply the service account to your instance.

  1. Select a service account that will act on your behalf to access Spanner. Use one of the following options:

     * [Create a new service account](https://docs.cloud.google.com/iam/docs/service-accounts-create).
     * [Identify an existing service account](https://docs.cloud.google.com/iam/docs/service-accounts-list-edit#listing) that you can use for your instance.
  2. [Grant a role to the service account](https://docs.cloud.google.com/iam/docs/granting-roles-to-service-accounts#granting_access_to_a_service_account_for_a_resource) so that it has the necessary permissions to access Spanner. For a list of roles that apply to Spanner, see [Access Control for Spanner](https://docs.cloud.google.com/spanner/docs/iam#roles).

  3. Go to the Compute Engine VM instances page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  4. Select your project and click **Continue**.

  5. Click **Create Instance** to start creating a new instance.

  6. In the **Identity and API access** section, select the service account from the list under **Service account**.

  7. Configure other instance settings as needed, then click **Create**.




Now that the service account on your Compute Engine instance has access to the Cloud Spanner API, [use a client library](https://docs.cloud.google.com/spanner/docs/tutorials) to read and write data in your Spanner database. The instance uses the service account credentials to authenticate with the Cloud Spanner API.

## What's next

  * [Connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) and follow a [client library tutorial](https://docs.cloud.google.com/spanner/docs/tutorials) to learn how to read and write data to Spanner from your instance.
  * Learn more about [service accounts on Compute Engine](https://docs.cloud.google.com/compute/docs/access/service-accounts) and how you can use them to grant Identity and Access Management (IAM) roles and API access scopes to the applications that run on your instances.
  * Learn how to [change service accounts on existing instances](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes).
  * Learn more about [creating and starting an Compute Engine instances](https://docs.cloud.google.com/compute/docs/instances/create-start-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
