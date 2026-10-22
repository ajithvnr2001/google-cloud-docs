---
url: https://docs.cloud.google.com/deploy/docs/securing/secrets/
title: Manage application secrets \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:06.129961+00:00
---

# Manage application secrets  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/securing/secrets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Guides ](https://docs.cloud.google.com/deploy/docs/overview)



Send feedback 

#  Manage application secrets Stay organized with collections  Save and categorize content based on your preferences. 

This page describes some best practices for managing secrets for applications you deploy to Google Kubernetes Engine or GKE attached clusters using Cloud Deploy.

Because injecting application secrets into deployment artifacts introduces security risks, avoid managing secrets from within Cloud Deploy pipelines.

Secrets consumed in this way should be generated, managed, and rotated outside of the scope of Cloud Deploy.

Secrets, in this context, refer to sensitive data such as database credentials, API keys, certificates, or passwords.

## Kubernetes secrets

Kubernetes Secrets are secure objects that store sensitive data, such as passwords, OAuth tokens, and SSH keys in your clusters, separate from Pods. Secrets are similar to ConfigMaps, but are intended to hold confidential data.

Because Kubernetes Secrets are not secure by default, without encryption, the approaches described in this document don't use them.

## Managing secrets for use with Cloud Deploy

This section describes how to manage secrets for applications that you deploy using Cloud Deploy.

The following are two approaches to secrets management with GKE or GKE attached clusters:

  * [Google Secret Manager](https://docs.cloud.google.com/secret-manager)

  * [Hashicorp Vault](https://www.vaultproject.io/)




### Google Secret Manager

Secret Manager is a fully managed, multi-region Google Cloud service that securely stores API keys, passwords, and other sensitive data.

Secrets from Secret Manager can be accessed from the cluster using the [client library](https://docs.cloud.google.com/secret-manager/docs/reference/libraries) and [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) authentication, or using the [Secrets Store CSI driver](https://github.com/kubernetes-sigs/secrets-store-csi-driver). 

To use Secret Manager for your application:

  1. [Create a secret using Secret Manager](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets#create).

  2. Reference the secret from your application code [using the SDK](https://docs.cloud.google.com/secret-manager/docs/accessing-the-api).




You can specify additional metadata for the secret using environment variables, for example secret version, or application environment (such as dev, staging, prod).

If the deployment process for a specific feature includes provisioning of infrastructure, then create or update the secret using Secret Manager as part of the provisioning process, before deploying the application.

For more information on managing Kubernetes secrets with Secret Manager, see [Using Secret Manager with other products ](https://docs.cloud.google.com/secret-manager/docs/using-other-products).

### Hashicorp Vault

[Hashicorp Vault](https://www.vaultproject.io/) is a popular and widely used open source tool for managing secrets. Google Cloud has extensive integrations and support for Vault, along with other Hashicorp tools such as Terraform.

You can configure Vault within your Kubernetes cluster as follows:

  1. Access Vault secrets through the [API](https://vaultproject.io/api) and authenticate using [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).

  2. Inject Secrets into your Kubernetes Pods using [Vault Agent](https://learn.hashicorp.com/tutorials/vault/agent-kubernetes) containers.

  3. Use the [Vault CSI Provider](https://vaultproject.io/docs/platform/k8s/csi) to consume those secrets.


**Note:** when you implement Vault, you're responsible for securing and updating the Vault cluster, and for configuring backups and high availability.

## What's next

  * Find out more about Secret Manager [best practices](https://docs.cloud.google.com/secret-manager/docs/best-practices).

  * Read a [blog post](https://jryancanty.medium.com/hashicorp-vault-and-terraform-on-google-cloud-security-best-practices-3d94de86a3e9) about security best practices using HashiCorp Vault and Terraform on Google Cloud.

  * [Read more about secrets management in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview).

  * [Learn about configuring Vault on Google Cloud](https://www.vaultproject.io/docs/secrets/gcp).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
