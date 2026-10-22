---
url: https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform/
title: Terraform and Infrastructure Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:26:43.144558+00:00
---

# Terraform and Infrastructure Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/infrastructure-manager/docs/infra-manager-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Infrastructure Manager ](https://docs.cloud.google.com/infrastructure-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/infrastructure-manager/docs/overview)



Send feedback 

#  Terraform and Infrastructure Manager Stay organized with collections  Save and categorize content based on your preferences. 

To work with Infrastructure Manager (Infra Manager), you should be familiar with Terraform. To learn more about Terraform, start with [What is Terraform?](https://developer.hashicorp.com/terraform/intro).

Infra Manager deploys infrastructure resources and configurations that are defined in a Terraform configuration. These configurations can consist of multiple files and directories, but their entrypoint must be a [Terraform root module](https://developer.hashicorp.com/terraform/language/modules).

Infra Manager uses the term _blueprint_ to refer to a Terraform configuration.

To learn more about Terraform with Google Cloud, see [Terraform on Google Cloud](https://docs.cloud.google.com/docs/terraform).

## Terraform modules for Google Cloud

For a set of modules to provision Google Cloud resources, see [Terraform blueprints and modules for Google Cloud](https://docs.cloud.google.com/docs/terraform/blueprints/terraform-blueprints).

You can also create your own Terraform modules for Google Cloud. For more details, see [Creating Modules](https://developer.hashicorp.com/terraform/language/modules/develop).

## Supported Terraform versions

Infra Manager supports the following Terraform versions:

Terraform version | Date available | Deprecation date | End of support date | Auto-migrate to version  
---|---|---|---|---  
`1.2.3` | 8/21/2023 | 1/8/2026 | 2/8/2026 | `1.5.7`  
`1.3.10` | 3/14/2024 | TBD | TBD | TBD  
`1.4.7` | 3/14/2024 | TBD | TBD | TBD  
`1.5.7` | 3/14/2024 | TBD | TBD | TBD  
  
You can use the flag `--tf-version-constraint` to specify the version of Terraform that Infra Manager uses to [create a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources).

Before you use Infrastructure Manager to deploy a Terraform configuration, ensure that the configuration has the following constraints:

If you don't specify a version of Terraform, the latest supported version is used by default.

When updating a deployment, you can upgrade to a later Terraform version, but you cannot downgrade to an earlier supported version. For information about Terraform version deprecation, see the [Terraform version management policy](https://docs.cloud.google.com/infrastructure-manager/docs/terraform-version-deprecation) documentation.

To view the version of Terraform that was used to create a specific deployment or revision, see [View details of a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments#deployment-details) and [View details of a revision](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments#revision-details).

## Constraints on Terraform configurations

To use Infrastructure Manager to deploy a Terraform configuration, the configuration has the following constraints:

  * Don't include personally identifiable or sensitive information in Terraform configuration values. For more information, see Terraform configuration values and sensitive data.
  * A valid [Terraform root module](https://developer.hashicorp.com/terraform/language/modules#the-root-module) must be provided. Templating or generation of Terraform is not supported.
  * The configuration should be actuatable by a supported version of Terraform.
  * [Backend blocks](https://developer.hashicorp.com/terraform/language/backend) shouldn't be defined.
  * We don't recommend using [provisioners](https://developer.hashicorp.com/terraform/language/resources/provisioners/syntax). When possible, use a different solution. For more information about this recommendation, see [Provisioners are a Last Resort](https://developer.hashicorp.com/terraform/language/resources/provisioners/syntax#provisioners-are-a-last-resort). If you are using provisioners, note that the [Infra Manager runtime environment](https://docs.cloud.google.com/infrastructure-manager/docs/overview#runtime_environment) can change at any time.



## Terraform configuration values and sensitive data

Don't include personally identifiable or sensitive information in Terraform configuration values.

The [documentation for the Google Cloud provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs) indicates configuration values that can potentially include sensitive information.

For example, the resource `google_storage_bucket_object` allows creation of a Cloud Storage object using the `content` argument. This argument is labeled as sensitive on the [`google_storage_bucket_object` page of the Google Cloud Provider documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket_object#content).

You can use these labels to help guide you as you create Terraform configurations or as you review an existing Terraform configuration before use.

See the [Google Cloud Privacy Notice](https://cloud.google.com/terms/cloud-privacy-notice) for information on how Google Cloud processes personal information it collects or generates during the provision and administration of the Cloud Services.

## Use the Terraform provider for Google Cloud

Optionally, you can use gcloud CLI to configure deployments and previews to use Infra Manager maintained Terraform providers for Google Cloud.

Infra Manager supports Terraform providers for Google Cloud:

  * `google`
  * `google-beta`



Omit this field to use the [HashiCorp-maintained Terraform provider for Google Cloud](https://registry.terraform.io/providers/hashicorp/google/latest/docs).

To learn how to specify the use of a Infra Manager maintained Terraform provider, see [Deploy infrastructure using Infrastructure Manager](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources#storage-bucket), [Update a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment#storage-bucket), or [Preview a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/preview-deployment#storage-bucket).

### Check supported versions of the provider

To check the versions of a Terraform provider for Google Cloud that Infra Manager supports, view the `manifest.json` in the Infra Manager maintained Cloud Storage bucket _associated with the region of your deployment_ in the format:
    
    
    https://storage.googleapis.com/LOCATION-im-providers/hashicorp/PROVIDER_VERSION/manifest.json
    

You can find a complete list of supported versions within the `versions` field of the `manifest.json` file.

For example, if your deployment is located in the `africa-south1` region and you are using the `google-beta` provider, navigate to <https://storage.googleapis.com/africa-south1-im-providers/hashicorp/google-beta/manifest.json> to view available regions.

## What's next

  * Learn more about [Infrastructure Manager](https://docs.cloud.google.com/infrastructure-manager/docs/overview).
  * [Create a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/deploy-resources).
  * [Update a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/update-deployment).
  * [View the state of a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/view-deployments).
  * [Delete a deployment](https://docs.cloud.google.com/infrastructure-manager/docs/delete-deployments).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
