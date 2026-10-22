---
url: https://docs.cloud.google.com/code/docs/intellij/kubernetes-secrets/
title: Sensitive information storage in Kubernetes using Cloud Code for IntelliJ \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:41:02.442783+00:00
---

# Sensitive information storage in Kubernetes using Cloud Code for IntelliJ  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/code/docs/intellij/kubernetes-secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Code ](https://docs.cloud.google.com/code/docs)
  * [ IntelliJ Cloud Code ](https://docs.cloud.google.com/code/docs/intellij)
  * [ Guides ](https://docs.cloud.google.com/code/docs/intellij/quickstart)



Send feedback 

#  Sensitive information storage in Kubernetes using Cloud Code for IntelliJ Stay organized with collections  Save and categorize content based on your preferences. 

This page provides a quick introduction to what Kubernetes secrets are, and how Cloud Code helps enable the Secret Manager API to create, use, and store them.

## Introduction to Kubernetes secrets

When creating Kubernetes applications, it's often necessary to pass small amounts of sensitive data for passwords, SSH keys, or OAuth tokens. Rather than store this information in a pod specification or container image, Kubernetes secrets can be created to store the sensitive data.

By default, Kubernetes secrets are stored unencrypted in the API server's underlying data store. Anyone with API access can retrieve or modify a secret. The [Kubernetes Secrets documentation](https://kubernetes.io/docs/concepts/configuration/secret/) recommends taking at least the following steps in order to safely use Kubernetes secrets:

  * [Enable Encryption at Rest](https://kubernetes.io/docs/tasks/administer-cluster/encrypt-data/) for Secrets.
  * [Enable or configure RBAC rules](https://kubernetes.io/docs/reference/access-authn-authz/authorization/) with least-privilege access to Secrets.
  * Restrict Secret access to specific containers.
  * [Consider using external Secret store providers](https://secrets-store-csi-driver.sigs.k8s.io/concepts.html#provider-for-the-secrets-store-csi-driver).



## Secret Manager in Cloud Code

Cloud Code helps you use the Secret Manager API to create, version, and store your secrets with [encryption at rest](https://docs.cloud.google.com/secret-manager/docs/encryption) from within your IDE. You can use Secret Manager exclusively in Cloud Code, or in addition to other tools you already use for secret management.

Actions available within your IDE with Cloud Code include:

  * [Enable the Secret Manager API](https://docs.cloud.google.com/code/docs/intellij/secret-manager#enabling).
  * [Create Kubernetes secrets](https://docs.cloud.google.com/code/docs/intellij/secret-manager#creating_secrets) using the Secret Manager view or the editor view.
  * [Version](https://docs.cloud.google.com/code/docs/intellij/secret-manager#creating_new_versions_of_secrets), view, and delete secrets.
  * [Access secrets from your application](https://docs.cloud.google.com/code/docs/intellij/secret-manager#accessing_secrets_from_your_application). 



## Work with Kubernetes secrets in Cloud Code

For step-by-step instructions on creating, versioning, using, and deleting secrets in Cloud Code, see [Manage secrets](https://docs.cloud.google.com/code/docs/intellij/secret-manager).

## What's next

  * Read more about Kubernetes secrets in the [Kubernetes documentation](https://kubernetes.io/docs/concepts/configuration/secret/).
  * Familiarize yourself with [good practices for Kubernetes secrets](https://kubernetes.io/docs/concepts/security/secrets-good-practices/).
  * Consider using a [service account token](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#service-account-tokens) or other [alternatives](https://kubernetes.io/docs/concepts/configuration/secret/#alternatives-to-secrets) to secrets.



## Get support

To submit feedback or report an issue in your IntelliJ IDE, go to **Tools** > **Cloud Code** > **Help / About** > **Submit feedback or report an issue** to report an issue on [GitHub](https://github.com/GoogleCloudPlatform/cloud-code-intellij/issues). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
