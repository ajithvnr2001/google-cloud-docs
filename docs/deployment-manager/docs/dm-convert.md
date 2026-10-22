---
url: https://docs.cloud.google.com/deployment-manager/docs/dm-convert/
title: Using DM Convert to transition to Terraform or Kubernetes Resource Model (KRM) \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:43:08.872680+00:00
---

# Using DM Convert to transition to Terraform or Kubernetes Resource Model (KRM)  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/dm-convert/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Using DM Convert to transition to Terraform or Kubernetes Resource Model (KRM) Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Deployment Manager Convert (DM Convert) is a tool you can use to convert your Deployment Manager [configurations](https://docs.cloud.google.com/deployment-manager/docs/configuration) and [templates](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template) to other declarative configuration formats that Google supports. Google currently supports [Terraform](https://docs.cloud.google.com/docs/terraform) and [Kubernetes Resource Model (KRM)](https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/resource-management.md).

## Why convert to Terraform or KRM?

Terraform and KRM are popular options for managing Google Cloud services and infrastructure. They offer actively-updated ecosystems, with support for modern features such as Secrets management and continuous reconciliation (for KRM).

Google works with [HashiCorp](https://www.hashicorp.com/) to develop the [Terraform provider for Google Cloud](https://registry.terraform.io/providers/hashicorp/google/latest/docs). In 2020, Google also launched [Config Connector](https://docs.cloud.google.com/config-connector/docs/overview) to help customers use Kubernetes to manage Google Cloud [resource types](https://docs.cloud.google.com/config-connector/docs/reference/overview).

### Terraform

[Terraform](https://www.terraform.io/) is an open-source tool for provisioning infrastructure. You can use Terraform to write declarative configurations to manage your Google Cloud services and resources using the [Terraform provider for Google Cloud](https://registry.terraform.io/providers/hashicorp/google/latest/docs). For more information, refer to [Terraform on Google Cloud](https://docs.cloud.google.com/docs/terraform).

### Kubernetes Resource Model (KRM)

[KRM](https://github.com/kubernetes/design-proposals-archive/blob/main/architecture/resource-management.md) is a paradigm for building APIs and resource definitions for declarative configuration management. It represents Google Cloud resources as [Custom Resource Definitions (CRDs)](https://docs.cloud.google.com/config-connector/docs/reference/overview) and can be actuated using [Config Controller](https://docs.cloud.google.com/anthos-config-management/docs/concepts/config-controller-overview).

## Supported types and type providers

DM Convert converts Deployment Manager configuration YAML files and Jinja or Python template files to KRM or Terraform configuration files.

To check the current status of DM Convert's support for type providers and resource types, you can use the `--list-supported-types` flag.

## Understanding how DM Convert translates concepts across formats

The following table shows how DM Convert translates concepts from Deployment Manager into KRM and Terraform:

Deployment Manager concept | KRM/Config Connector conversion | Terraform conversion  
---|---|---  
[References](https://docs.cloud.google.com/deployment-manager/docs/step-by-step-guide/using-references) | [Resource references](https://docs.cloud.google.com/config-connector/docs/how-to/creating-resource-references), if the KRM schema defines the field as a reference. If the KRM schema doesn't define the field as a reference, the Deployment Manager reference is replaced with its resolved value. | [Terraform references](https://www.terraform.io/docs/language/expressions/references.html) look and behave similarly to Deployment Manager references.  
[Explicit dependencies](https://docs.cloud.google.com/deployment-manager/docs/configuration/create-explicit-dependencies) (`depends_on`) | No support for explicit dependency ordering. Resources actuate in an eventually-consistent manner. | [`depends_on`](https://www.terraform.io/docs/language/meta-arguments/depends_on.html)  
Identity and Access Management (IAM) Bindings (authoritative [`accessControl`](https://docs.cloud.google.com/deployment-manager/docs/configuration/set-access-control-resources) blocks) | [`IAMPolicy`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/iam/iampolicy) | `<resource_type>_iam_policy` types (for example, [`google_pubsub_topic_iam_policy`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/pubsub_topic_iam))  
IAM Bindings (nonauthoritative `iamMemberBinding` types) | [`IAMPolicyMember`](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/iam/iampolicymember) | `<resource_type>_iam_member` (for example, [`google_project_iam_member`](http://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_iam#google_project_iam_member))  
[Composite types](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-composite-types) | [Composite types are deprecated](https://docs.cloud.google.com/deployment-manager/docs/deprecations). DM Convert doesn't convert them. | [Composite types are deprecated](https://docs.cloud.google.com/deployment-manager/docs/deprecations). DM Convert doesn't convert them.  
[Actions](https://docs.cloud.google.com/deployment-manager/docs/migrations/actions), [custom type providers](https://docs.cloud.google.com/deployment-manager/docs/configuration/type-providers/creating-type-provider), and [outputs](https://docs.cloud.google.com/deployment-manager/docs/configuration/expose-information-outputs) | Not supported. | Actions that have declarative equivalents in Terraform are converted. For more details, refer to Support for Actions.  
  
## Support for Actions in DM Convert (for Terraform)

Actions is a Preview feature for Deployment Manager that extends the set of available API methods. [Actions is unsupported](https://docs.cloud.google.com/deployment-manager/docs/migrations/actions), and DM Convert doesn't convert Actions that don't have declarative equivalents in Terraform, such as:

  * Patch, delete, and list APIs

  * APIs defined in custom type providers

  * Custom APIs, such as `sqladmin-v1beta4:sql.instances.restart`




DM Convert does support conversion to Terraform equivalents for Actions in the following cases:

  * It replaces Action calls to APIs that insert a resource with equivalent Terraform resources. For example, `action: gcp-types/storage-v1:storage.buckets.insert` converts to [`google_storage_bucket`](http://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket).

  * It converts Action calls to APIs that get a resource to Terraform `data` types whenever possible. For example, `actions: gcp-types/compute-v1:compute.subnetworks.get` converts to [`google_compute_subnetwork`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/data-sources/compute_subnetwork).

  * It converts `setIamPolicy` commands to either `*_iam_policy` (authoritative) or `*_iam_member` (non-authoritative) resources, depending on whether or not they're used with `getIamPolicy`.




For information on migrating usage of Actions to declarative alternatives within Deployment Manager, visit [Replacing usage of Actions](https://docs.cloud.google.com/deployment-manager/docs/migrations/actions).

## Workflow for converting to Terraform

To use DM Convert to convert your Deployment Manager configurations to Terraform:

  1. Identify the Deployment Manager configuration you want to convert to Terraform.
  2. To make sure your resources are up-to-date, reconcile any active deployments of the configuration.
  3. To convert your configuration to Terraform, [run the DM Convert tool](https://docs.cloud.google.com/deployment-manager/docs/dm-convert/convert) locally.
  4. Verify that the generated Terraform configuration reflects the current state of your resources.
  5. Delete the Deployment Manager deployment. To preserve your resources when you delete the deployment, set `delete-policy` to `abandon`.



We recommend that you follow [Terraform best practices](https://docs.cloud.google.com/docs/terraform/best-practices-for-terraform#root-modules), such as:

  * Storing your [Terraform state in a Cloud Storage bucket](https://docs.cloud.google.com/docs/terraform/resource-management/store-state)
  * [Using Cloud Build to manage actuation](https://docs.cloud.google.com/architecture/managing-infrastructure-as-code).



For a detailed walkthrough of this workflow, refer to [Converting your Deployment Manager configurations with DM Convert](https://docs.cloud.google.com/deployment-manager/docs/dm-convert/convert).

## Data collection in DM Convert

### What we collect, by default

By default, the DM Convert tool sends anonymous usage data to Google to help us maintain and improve the tool. When the DM Convert tool executes, data about the requested operation, the success of the operation, and the timing of the conversion is collected. This data is anonymous, and excludes any personally identifiable information, sensitive data, or customer content.

The usage data might contain:

  * **Conversion command input parameters:** We record the parameter values of your conversion command when running the tool, including the output format (KRM or Terraform) and boolean representations of whether other flags are specified (we don't collect the specific values of those flags).

  * **Conversion result:** We record the results of the conversion, including the conversion status (`SUCCESS` or `FAILURE`) as well as the error code and error message, if an issue occurs.

  * **Conversion time:** We record the start and end times of the conversion.




### How we use this data

Google collects and processes the usage data to:

  * Understand how the tool is used, including which features and settings are most popular.

  * Diagnose unsuccessful usage of the tool, and provide guidance to users seeking technical assistance.

  * Improve the tool by resolving issues and potentially increasing feature coverage.




### Opting out of data collection

Google collects usage data by default when you execute a conversion, but this data collection can be disabled.

To disable the data collection for a specific conversion, you can specify the flag `--opt_out_data_collection=true` in your conversion command. To continue to opt out of this data collection going forward, you must specify the flag every time that you run a conversion.

To enable the data collection for a specific conversion, you can specify the flag `--opt_out_data_collection=false` in your conversion command, or omit the flag from your command.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
