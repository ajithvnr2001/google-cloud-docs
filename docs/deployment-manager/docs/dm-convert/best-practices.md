---
url: https://docs.cloud.google.com/deployment-manager/docs/dm-convert/best-practices/
title: Best practices for using DM Convert \u00a0|\u00a0 Cloud Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:46:59.494627+00:00
---

# Best practices for using DM Convert  |  Cloud Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/dm-convert/best-practices/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Best practices for using DM Convert Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Best practices for converting to Terraform

### State

The [state file](https://developer.hashicorp.com/terraform/language/state) stores information about the resources Terraform manages. By default, Terraform stores [state](https://developer.hashicorp.com/terraform/language/state) locally on disk. If you store state remotely, you can allow for distributed collaboration, protect sensitive information, and run Terraform in continuous integration (CI).

After you convert your Deployment Manager template to Terraform and optionally import resources, we recommend that you follow the steps to [store state remotely in Cloud Storage](https://docs.cloud.google.com/docs/terraform/resource-management/store-state#change_the_backend_configuration).

### Modules

If you want to reduce complexity, enforce consistency, and promote reusability of your configuration, you can use [Terraform modules](https://developer.hashicorp.com/terraform/tutorials/modules/module) to encapsulate collections of resources.

To use modules, you can do either of the following:

  * Create a custom module from the resources exported by DM Convert. This gives you the most flexibility.

  * Use a published module from Google Cloud's collection of [official modules](https://docs.cloud.google.com/docs/terraform/blueprints/terraform-blueprints) or the [Terraform registry](https://registry.terraform.io/).




For most use cases, we recommend that you use a published module.

#### Create a custom module

  1. After you've [converted your configuration](https://docs.cloud.google.com/deployment-manager/docs/dm-convert/docs/dm-convert/convert#view_the_conversions) ,identify which resources you want to move into a module.

  2. Move the configurations of those resources into a module directory, and convert required variables into parameters.

The following example shows how to move `google_bigquery_dataset` and `google_bigquery_table` into a module:
         
         # bq-module/main.tf
         resource "google_bigquery_dataset" "bigquerydataset" {
           provider = google-beta
         
           default_table_expiration_ms = 36000000
           location = "us-west1"
           dataset_id = var.dataset_id
           project = var.project_id
         }
         
         resource "google_bigquery_table" "bigquerytable" {
           provider = google-beta
         
           labels = {
             data-source = "external"
             schema-type = "auto-junk"
           }
           dataset_id = var.dataset_id
           project = var.project_id
           table_id = var.table_id
         
           depends_on = [
             google_bigquery_dataset.bigquerydataset
           ]
         }
         
         
         # bq-module/variables.tf
         variable "project_id" {
           description = "Project ID"
           type = string
         }
         
         variable "dataset_id" {
           description = "Dataset ID"
           type = string
         }
         
         variable "table_id" {
           description = "Table ID"
           type = string
         }
         

  3. In the exported `main.tf` file, replace the original configuration with the module you created.

The following example shows this replacement using the module created in the example from the previous step.
         
         # main.tf
         module "bq" {
           source = "./bq-module"
         
           project_id = "PROJECT_ID"
           dataset_id = "bigquerydataset"
           table_id   = "bigquerytable"
         }
         

  4. To initialize the local module, run the following command:
         
         terraform init
         

  5. [Move](https://developer.hashicorp.com/terraform/cli/commands/state/mv) the Terraform state associated with the resources into the module instance.

To move the module from the example in the previous step, run the following command:
         
         terraform state mv google_bigquery_dataset.bigquerydataset module.bq.google_bigquery_dataset.bigquerydataset
         terraform state mv google_bigquery_table.bigquerytable module.bq.google_bigquery_table.bigquerytable
         

For this example, the output from the move is:
         
         Move "google_bigquery_dataset.bigquerydataset" to "module.bq.google_bigquery_dataset.bigquerydataset"
         Successfully moved 1 object(s).
         Move "google_bigquery_table.bigquerytable" to "module.bq.google_bigquery_table.bigquerytable"
         Successfully moved 1 object(s).
         

  6. Validate that no resources have changed, by running the following command:
         
         terraform plan
         

The following is an example of the output you receive after you run the command:
         
         No changes. Your infrastructure matches the configuration.
         




#### Use a published module

  1. After you've [converted your configuration](https://docs.cloud.google.com/deployment-manager/docs/dm-convert/docs/dm-convert/convert#view_the_conversions), identify a [published module](https://docs.cloud.google.com/docs/terraform/blueprints/terraform-blueprints) and the resources that you want to move into it.

  2. Identify configuration options for the module by reading the module's documentation.

  3. Create an instance of the module configured to your current resource configuration.

For example, if you want to move `google_bigquery_dataset` and `google_bigquery_table` into the official [BigQuery module](https://github.com/terraform-google-modules/terraform-google-bigquery) , the following example shows what your module might look like:
         
         module "bq" {
           source  = "terraform-google-modules/bigquery/google"
           version = "~> 5.0"
         
           project_id          = "PROJECT_ID"
           dataset_id          = "bigquerydataset"
           location            = "us-west1"
           deletion_protection = true
         
           tables = [
             {
               table_id           = "bigquerytable",
               friendly_name      = "bigquerytable"
               time_partitioning  = null,
               range_partitioning = null,
               expiration_time    = null,
               clustering         = [],
               schema             = null,
               labels = {
                 data-source = "external"
                 schema-type = "auto-junk"
               },
             }
           ]
         }
         

  4. To initialize the local module, run the following command:
         
         terraform init
         

  5. Read the [module source code](https://github.com/terraform-google-modules/terraform-google-bigquery/blob/v5.4.1/main.tf) to identify resource addresses within the upstream module and construct the [move](https://developer.hashicorp.com/terraform/cli/commands/state/mv) commands.
         
         terraform state mv google_bigquery_dataset.bigquerydataset  module.bq.google_bigquery_dataset.main
         terraform state mv google_bigquery_table.bigquerytable 'module.bq.google_bigquery_table.main["bigquerytable"]'
         

  6. To view any changes to the configuration, run the following command:
         
         terraform plan
         




If the published module you selected has different default settings or is configured differently than your configuration, you might see differences highlighted in the output from running the command.

### Actuation

We recommend that you use a continuous integration (CI) system, such as Cloud Build, Jenkins, or GitHub Actions, to automate running Terraform at scale. For more information, visit [Managing infrastructure as code with Terraform, Cloud Build, and GitOps](https://docs.cloud.google.com/deployment-manager/docs/dm-convert/architecture/managing-infrastructure-as-code).

If you want to bootstrap creation of triggers and simplify authentication, you can choose to use the [Cloud Build Workspace](https://github.com/terraform-google-modules/terraform-google-bootstrap/tree/master/modules/tf_cloudbuild_workspace) blueprint.

### Structure

Each converted configuration from DM Convert is a [single root configuration](https://developer.hashicorp.com/terraform/language/modules#the-root-module) mapped to a single state file. We don't recommend setting up a single state file to hold a large number of resources. After you've converted your configuration, we recommend that you ensure that your new configuration follows the [best practices for root modules](https://docs.cloud.google.com/docs/terraform/best-practices-for-terraform#root-modules).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
