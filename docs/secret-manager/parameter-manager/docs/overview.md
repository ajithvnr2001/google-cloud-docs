---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview/
title: Parameter Manager overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:09:37.301376+00:00
---

# Parameter Manager overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Parameter Manager overview Stay organized with collections  Save and categorize content based on your preferences. 

Parameter Manager is an extension to the [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) service and provides a centralized storage for all configuration parameters related to your workload deployments.

Parameters are variables, often in the form of key-value pairs, which customize how an application functions. Parameters can include a wide range of settings such as the following:

  * **Configuration settings** : Database connection strings, API keys, and user interface preferences
  * **Environment-specific settings** : Tailored configurations for production, development, or testing environments
  * **Secrets** : Sensitive data such as credentials and secure connection strings



Using Parameter Manager, you can do the following:

  * Store all your workload parameters in a centralized system. Having all your configuration data in one place simplifies management, improves consistency, and reduces errors.
  * Ensure consistent deployments across all environments by using the same parameter values.
  * Track changes to your parameters for compliance and security purposes.
  * Control access to parameters with fine-grained Identity and Access Management IAM permissions, ensuring that only authorized users and services can access sensitive data.



### Key features

Following are the key features of Parameter Manager:

  * **Data encryption** : Parameters are encrypted using the Advanced Encryption Standard (AES) algorithm (AES-256).
  * **Versioning** : Each parameter can have multiple versions, allowing you to track changes over time and roll back to previous values if needed.
  * **Flexible format support** : you can store your configuration data using structured formats such as YAML and JSON. You can also use unformatted configurations such as plain text or custom formats for maximum flexibility.
  * **Reference[Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) secrets**: You can reference secrets stored in Secret Manager from Parameter Manager parameters. This lets you manage all your application configuration data, including secrets, from Parameter Manager while also leveraging Secret Manager features such as automatic rotation and auditing.
  * **Regional parameters** : Parameter Manager supports regional endpoints, letting you create and manage parameters specific to each location in which your cloud environment operates. For a list of locations that support regional endpoints, see [Parameter Manager regional endpoint locations](https://docs.cloud.google.com/secret-manager/docs/locations#parameter_manager_locations).



## Parameter Manager resources

There are two main resources in Parameter Manager:

  * [**Parameter**](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/create-parameter): A parent object that holds all the information about the parameter. It includes metadata such as the parameter's name, the type of data it stores (for example, YAML, JSON, or unstructured), and any associated labels. A parameter also holds all the parameter versions.
  * [**Parameter version**](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/add-parameter-version): A parameter version stores the actual value of the parameter. Each version can contain structured data (like YAML or JSON) or unstructured data (plain text).



## Differences between Secret Manager and Parameter Manager

Both Secret Manager and Parameter Manager store and manage sensitive data, but they differ in the type of data they handle and their use cases within a workload.

Feature | Secret Manager | Parameter Manager  
---|---|---  
Primary purpose | Stores and manages sensitive data, such as API keys, passwords, OAuth tokens, and TLS/SSL certificates. It's the ideal choice when the data is a secret. You can use Secret Manager to securely inject credentials into CI/CD pipelines and workloads like Cloud Run and GKE. | Stores and manages workload configuration data. It's used for environment-specific settings, feature flags, and other configurations. You can use Parameter Manager for applications that dynamically fetch configuration at runtime, without requiring restarts or redeployments.  
Data types | Stores secrets as binary blobs or text strings. Focuses on individual, sensitive credentials. | Supports structured formats like JSON and YAML, as well as unformatted plaintext. Suitable for diverse configuration file types.  
Data size limit | Each secret version can store up to 64 KiB of data. | Each parameter version can store up to 1 MiB of data.  
Versioning | Automatically versions secrets with auto-incrementing numbers and allows pinning specific versions to aliases (for example, `previous`). | Users can provide names for versions.  
Lifecycle management | Supports automatic rotation of secrets. | Doesn't support rotation.  
  
Use Secret Manager to _securely store and audit sensitive data_ that requires strict access control and rotation. Use Parameter Manager to _manage and deliver diverse configuration data_ —both sensitive and non-sensitive—for your applications at scale.

## What's next

  * [Prepare environment for Parameter Manager](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/prepare-environment)
  * [Create a parameter](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/create-parameter)
  * [Add a parameter version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/add-parameter-version)
  * [Reference secrets in parameters](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference-secrets-in-parameter)
  * [Render secrets referenced within a parameter version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/render-parameter-version)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
