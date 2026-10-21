---
url: https://docs.cloud.google.com/secret-manager/docs/using-other-products/
title: Use Secret Manager with other products \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:41:04.043604+00:00
---

# Use Secret Manager with other products  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/using-other-products/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/secret-manager/docs/overview)



Send feedback 

#  Use Secret Manager with other products Stay organized with collections  Save and categorize content based on your preferences. 

This topic provides resources for using Secret Manager with other Google Cloud services.

## Cloud Build

Access Secret Manager secrets using environment variables in build steps on Cloud Build. See [using Secret Manager secrets with Cloud Build](https://docs.cloud.google.com/build/docs/securing-builds/use-encrypted-secrets-credentials) for more information.

## Cloud Code

Create, view, update, and use secrets within [VS Code](https://docs.cloud.google.com/code/docs/vscode/secret-manager), [IntelliJ](https://docs.cloud.google.com/code/docs/intellij/secret-manager), or [Cloud Shell](https://docs.cloud.google.com/code/docs/shell/secret-manager) with Cloud Code's Secret Manager integration.

## Cloud Run functions

Access Secret Manager secrets and expose them as environment variables or using the file system from Cloud Run functions. See [using Secret Manager secrets with Cloud Run functions](https://docs.cloud.google.com/functions/docs/configuring/secrets) for more information.

You can also use Secret Manager with Cloud Run functions by using a [Secret Manager client library](https://docs.cloud.google.com/secret-manager/docs/reference/libraries) or by [accessing the Secret Manager API directly](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api).

## Cloud Run

Access Secret Manager secrets and expose them as environment variables or using the file system from Cloud Run services. See [using Secret Manager secrets with Cloud Run](https://docs.cloud.google.com/run/docs/configuring/secrets) for more information.

You can also use Secret Manager with Cloud Run services by using a [Secret Manager client library](https://docs.cloud.google.com/secret-manager/docs/reference/libraries) or by [accessing the Secret Manager API directly](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api).

## Compute Engine

**Important:** To use Secret Manager with workloads running on Compute Engine or Google Kubernetes Engine, the underlying instance or node must have the `cloud-platform` OAuth scope. See [accessing the Secret Manager API](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes) for more information. 

Use Secret Manager with workloads running on Compute Engine by using a [Secret Manager client library](https://docs.cloud.google.com/secret-manager/docs/reference/libraries) or by [accessing the Secret Manager API directly](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api).

## Google Kubernetes Engine

**Important:** To use Secret Manager with workloads running on Compute Engine or Google Kubernetes Engine, the underlying instance or node must have the `cloud-platform` OAuth scope. See [accessing the Secret Manager API](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api#oauth-scopes) for more information. 

Use Secret Manager with workloads running on Google Kubernetes Engine (GKE) using one of the following options:

  * Client libraries: The recommended way to access Secret Manager secrets from workloads running on Google Kubernetes Engine is to use a [Secret Manager client library](https://docs.cloud.google.com/secret-manager/docs/reference/libraries) authenticated using [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/workload-identity-secrets). For more information, see [Secret Manager best practices](https://docs.cloud.google.com/secret-manager/docs/best-practices).

  * Secret Manager add-on: You can use the Secret Manager add-on to access Secret Manager secrets as volumes mounted in Kubernetes Pods. For information, see [Use Secret Manager add-on with Google Kubernetes Engine](https://docs.cloud.google.com/secret-manager/docs/secret-manager-managed-csi-component).




## Config Connector

Create and manage Secret Manager secrets with Config Connector using a declarative syntax. See the [Secret Manager Config Connector resource documentation](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/secretmanager/secretmanagersecret) for more information.

## Key Access Justifications

In Secret Manager, you can use Cloud External Key Manager (Cloud EKM) keys to encrypt and decrypt secrets. Key Access Justifications works by adding an additional field to the Cloud EKM requests that lets you view the reason for every request to access the externally managed keys. It lets you approve or deny the access request based on that justification. With select external key management partners, you can automatically approve or deny these requests, based on the justification. See the [Key Access Justifications documentation](https://docs.cloud.google.com/assured-workloads/key-access-justifications/docs/overview) for more information.

## Managed Service for Apache Airflow

To improve the security of your Managed Service for Apache Airflow environments, use Secret Manager to store sensitive data such as Airflow variables and connections. Managed Service for Apache Airflow integrates with Secret Manager, letting you configure Secret Manager as an Airflow secrets backend. When configured, Airflow tasks fetch secrets directly from the Secret Manager API at runtime. For more information, see [Configure Secret Manager for your Managed Service for Apache Airflow environment](https://docs.cloud.google.com/composer/docs/composer-2/configure-secret-manager).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
