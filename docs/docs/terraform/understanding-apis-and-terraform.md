---
url: https://docs.cloud.google.com/docs/terraform/understanding-apis-and-terraform/
title: Understanding Google Cloud APIs and Terraform \u00a0|\u00a0 Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:06:23.884710+00:00
---

# Understanding Google Cloud APIs and Terraform  |  Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/docs/terraform/understanding-apis-and-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)



Send feedback 

#  Understanding Google Cloud APIs and Terraform Stay organized with collections  Save and categorize content based on your preferences. 

This guide aims to clarify how Terraform interacts with Google Cloud APIs (while differentiating between public and private APIs), and explain key concepts like API enablement and resource import. This understanding is crucial for effectively managing your Google Cloud resources with Terraform and avoiding common pitfalls.

## Public versus private Google Cloud APIs

Google Cloud services expose various APIs that allow applications and tools (like Terraform) to interact with and manage resources. These APIs broadly fall into two categories:

### Public APIs

**Purpose:** These are the primary interfaces for customers and tools to create, configure, and manage Google Cloud resources (e.g., Compute Engine instances, Cloud Storage buckets, BigQuery datasets).

**Exposure:** Public APIs are well-documented, have defined REST endpoints, and are intended for external consumption. They are the APIs that the `google` Terraform provider is built to interact with.

**Examples:** `compute.googleapis.com`, `storage.googleapis.com`, `bigquery.googleapis.com`.

### Private (internal) APIs

**Purpose:** These APIs are internal to Google Cloud services, used by Google itself for the internal operation, orchestration, and provisioning of its managed services. They expose functionalities that are not meant for direct customer interaction or management.

**Exposure:** Private APIs are generally not publicly documented, don't have stable external endpoints, and are not designed for direct access by third-party tools like Terraform. They are an implementation detail of the service.

**Example:** `dataproc-control.googleapis.com` is an internal API that Managed Service for Apache Spark uses for its operational control plane. Customers don't directly interact with or manage this API.

## API Enablement versus Resource Import in Terraform

Understanding the distinction between "enabling an API" and "importing a resource" is fundamental to using Terraform effectively with Google Cloud.

### Enabling an API

  * **What it means:** When you "enable an API" in Google Cloud, you are activating a specific Google Cloud service for your project. This grants your project the necessary permissions and access to use the functionalities of that service and create resources managed by it.



**Terraform context:** In Terraform, this is typically done using the `google_project_service` resource. This resource verifies that a specified public API (e.g., `compute.googleapis.com`) is enabled for your Google Cloud project.

**Purpose:** Enabling an API is a **prerequisite** for creating or managing resources that belong to that service. For example, you must enable `compute.googleapis.com` before you can create `google_compute_instance` resources.

**Example (Terraform):**
    
    
    ```hcl
    resource "google_project_service" "compute_api" {
      project            = "your-gcp-project-id"
      service            = "compute.googleapis.com"
      disable_on_destroy = false
    }
    ```
    

**Important Note:** The `google_project_service` resource is designed exclusively for managing the enablement state of **publicly accessible Google Cloud APIs**. It is not intended for, and won't work with, internal or private APIs. Attempting to use it for private APIs will result in errors, as those APIs are not exposed through the public API surface for such management.

### Importing a Resource

**What it means:** In Terraform, "importing" refers to bringing an **existing cloud resource** (one that was created manually or by another process outside of Terraform) under Terraform's management. When you import a resource, Terraform generates a state entry for it, allowing you to manage its lifecycle (updates, deletion) using your Terraform configuration.

**Terraform context:** This is achieved using the `terraform import` command, or by utilizing `import` blocks introduced in Terraform 1.5+.

**Purpose:** To gain control over resources that were not initially provisioned by Terraform.

**Example (Terraform CLI):**
    
    
    ```bash
    terraform import google_compute_instance.my_instance projects/your-gcp-project-id/zones/us-central1-a/instances/my-vm
    ```
    

**Note:** You "import" _resources_ (like a `google_compute_instance`, `google_storage_bucket`, `google_sql_database_instance`), not generally "APIs" themselves. While an API's enablement is a state managed by `google_project_service`, the API itself is not a resource that can be separately "imported" in the same manner as a VM or a bucket. If a public API is enabled for your project, its enablement state can be managed by the `google_project_service` resource and brought into state by importing the `google_project_service` resource (e.g., `terraform import google_project_service.my_api projects/your-gcp-project-id/services/compute.googleapis.com`), but this is distinct from importing a product-specific resource.

## Addressing Concerns about Private APIs (e.g., `dataproc-control.googleapis.com`)

Customers sometimes encounter references to private APIs (like `dataproc-control.googleapis.com` for Managed Service for Apache Spark) in logs or documentation and wonder if they need to enable or import them with Terraform.

**No Customer Action Required:** If an API is identified as a private or internal Google Cloud API, you **don't** need to explicitly enable it using `google_project_service` or attempt to import it with Terraform.

**Internal Management:** These APIs are crucial for the internal operation of Google Cloud services. They are automatically managed by Google and are not designed for direct customer interaction or management through public tools.

**No Impact on Service Usage:** Your inability to "import" or explicitly manage such a private API using Terraform will **not** impact your ability to use the associated Google Cloud service (e.g., Managed Service for Apache Spark will function correctly without you managing `dataproc-control.googleapis.com`). The necessary internal API interactions are handled by Google.

**Focus on Public APIs:** When managing Google Cloud resources with Terraform, your focus should solely be on enabling and configuring the **public APIs** that correspond to the services and resources you intend to provision.

## Conclusion

By understanding the clear distinction between public and private Google Cloud APIs, and the specific roles of "enabling" APIs versus "importing" resources in Terraform, you can effectively manage your Google Cloud infrastructure. don't attempt to explicitly manage or import private Google Cloud APIs; they are internal components handled by Google. Focus your Terraform configurations on the publicly exposed APIs and their corresponding resources. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
