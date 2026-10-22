---
url: https://docs.cloud.google.com/datastream/docs/use-secret-manager/
title: Use Secret Manager to store sensitive data \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:01.330971+00:00
---

# Use Secret Manager to store sensitive data  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/use-secret-manager/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Use Secret Manager to store sensitive data Stay organized with collections  Save and categorize content based on your preferences. 

Datastream integrates with [Secret Manager](https://docs.cloud.google.com/security/products/secret-manager) to let you securely store authentication resources, such as source database passwords. Rather than use a plain text password when creating a connection profile, create and use a secret.

## What are secrets

**Secrets** are global resources that contain metadata, such as labels, annotations, and permissions.

Secrets also have **secret versions**. Secret versions store the actual data for the secret resource, such as API keys, passwords, or certificates. Each version has a unique identifier or a timestamp.

## How are secrets different from encryption keys

Managing secrets is equally important as managing encryption keys, however it focuses on a different area of data security. You might use one or the other, depending on your use cases and types of sensitive information that you store.

You would typically select secrets to securely store and manage your sensitive data as binary blobs or text strings. Secrets store the actual data, but to access it, you need specific permissions which are defined in the secrets metadata.

On the other hand, encryption keys are a better choice if you need to encrypt or decrypt data. You can't view or extract the actual cryptographic data that is used for encryption. Key management systems such as Cloud Key Management Service are typically used to manage more demending scenarios, for example encrypting rows in a database, or images and files.

If you need an additional layer of protection for your data, you can enable customer-managed encryption keys (CMEK), and use your own encryption keys stored in Cloud Key Management Service to secure secrets in Secret Manager. For more information about how to use CMEK with Datastream, see [Use customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/datastream/docs/use-cmek).

## Use Secret Manager with Datastream

To store your sensitive data for use with Datastream, you need to create a secret using Secret Manager. For more information, see [Create a secret](https://docs.cloud.google.com/secret-manager/docs/creating-and-accessing-secrets).

You can also create a secret when you define connection details for your connection profile. For detailed information, see [Create connection profiles](https://docs.cloud.google.com/datastream/docs/create-connection-profiles).

**Note:** You can store your newly created secret in any Google Cloud project, it doesn't have to be the project where you created your stream.

### Required roles

To get the permissions that you need to use Secret Manager with Datastream, ask your administrator to grant you the [Secret Manager Secret Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/secretmanager#secretmanager.secretAccessor) (`roles/secretmanager.secretAccessor`) IAM role on the Datastream service account. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
