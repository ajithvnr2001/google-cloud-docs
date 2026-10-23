---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-terraform/
title: Create a data store using Terraform \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:19.046047+00:00
---

# Create a data store using Terraform  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-terraform/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Create a data store using Terraform Stay organized with collections  Save and categorize content based on your preferences. 

You can use Terraform to create a generic Gemini Enterprise data store or to set up data connectors for Atlassian Confluence, Atlassian Jira, BigQuery, Microsoft SharePoint, or Salesforce.

**Tip:** To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

## Before you begin

Before using Terraform to create a data store, do the following:

  * [Check whether billing is enabled on your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  * Ensure that you have the Project IAM Admin (`roles/resourcemanager.projectIamAdmin`) role for your Google Cloud project, as well as the Gemini Enterprise Admin (`roles/discoveryengine.agentspaceAdmin`) role.

  * Optional: If you are connecting a third-party data source like Microsoft SharePoint to Gemini Enterprise, obtain access credentials (such as API keys or database authentication) for the data source.

  * Ensure that you are using version 7.7.0 or later of the [hashicorp/google](https://registry.terraform.io/providers/hashicorp/google) Terraform provider:
        
        terraform {
          required_providers {
            google = {
              source  = "hashicorp/google"
              version = "7.7.0"
            }
          }
        }
        




## Create a generic data store

To use Terraform to create an empty data store, use the [`google_discovery_engine_data_store`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/discovery_engine_data_store) Terraform resource.

  1. Create the Terraform configuration:
         
         terraform {
           required_providers {
             google = {
               source  = "hashicorp/google"
               version = "7.7.0"
             }
           }
         }
         
         provider "google" {
           project                 = "PROJECT_ID"
           user_project_override   = true
           billing_project         = "BILLING_PROJECT_ID"
         }
         
         resource "google_discovery_engine_data_store" "gemini_search_store" {
           location                    = "LOCATION"
           data_store_id               = "DATA_STORE_ID"
           display_name                = "DATA_STORE_NAME"
           industry_vertical           = "GENERIC"
           content_config              = "NO_CONTENT"
           solution_types              = ["SOLUTION_TYPE_SEARCH"]
           create_advanced_site_search = false
         }
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID

     * `BILLING_PROJECT_ID`: your Google Cloud billing project ID

     * `LOCATION`: the location for the data store, such as `us` or `global` (for more information, see [Gemini Enterprise Standard and Plus Editions data residency and ML regional processing commitments](https://docs.cloud.google.com/gemini/enterprise/docs/locations))

     * `DATA_STORE_ID`: the data store ID

     * `DATA_STORE_NAME`: the data store name

  2. Initialize Terraform:
         
         terraform init -upgrade
         

  3. Preview your configuration:
         
         terraform plan
         

  4. Apply the configuration:
         
         terraform apply
         




After creating the empty data store, you can ingest data into the data store using the Google Cloud console or API commands.

## Create a data connector

To use Terraform to create a data connector for a supported service, use the [`google_discovery_engine_data_connector`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/discovery_engine_data_connector) Terraform resource. Include credentials for the service, as well as search filter configuration, in `json_params`.

  1. Create the Terraform configuration:
         
         terraform {
           required_providers {
             google = {
               source  = "hashicorp/google"
               version = "7.7.0"
             }
           }
         }
         
         provider "google" {
           project                 = "PROJECT_ID"
           user_project_override   = true
           billing_project         = "BILLING_PROJECT_ID"
         }
         
         resource "google_discovery_engine_data_connector" "LOCAL_NAME" {
           provider = google
         
           project                 = "PROJECT_ID"
           location                = "LOCATION"
           collection_id           = "COLLECTION_ID"
           collection_display_name = "COLLECTION_DISPLAY_NAME"
         
           data_source = "DATA_SOURCE"
         
           json_params = jsonencode({
             "client_id"                = "CLIENT_ID"
             "client_secret"            = "CLIENT_SECRET"
             "instance_uri"             = "INSTANCE_URI"
             "tenant_id"                = "TENANT_ID"
             "structured_search_filter" = { "FILTER_KEY" = ["FILTER_VALUE"] }
           })
         
           refresh_interval = "7200s"
         
           connector_modes = [CONNECTOR_MODES]
         
           entities {
             entity_name = "ENTITY_NAME"
           }
         }
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID

     * `BILLING_PROJECT_ID`: your Google Cloud billing project ID

     * `LOCAL_NAME`: the local name of the Terraform resource

     * `LOCATION`: the location for the data store, such as `us` or `global` (for more information, see [Gemini Enterprise Standard and Plus Editions data residency and ML regional processing commitments](https://docs.cloud.google.com/gemini/enterprise/docs/locations))

     * `COLLECTION_ID`: the collection ID

     * `COLLECTION_DISPLAY_NAME`: the collection display name

     * `DATA_SOURCE`: the data source type. The following values are supported:

       * `bigquery`

       * `confluence`

       * `jira`

       * `salesforce`

       * `sharepoint_federated_search`

     * `CLIENT_ID`: the client ID for the service

     * `CLIENT_SECRET`: the client secret for the service

     * `INSTANCE_URI`: the URI of your instance (for example, `https://your-tenant.sharepoint.com`)

     * `TENANT_ID`: the tenant ID

     * `FILTER_KEY`: a filter key (for example, `Path`)

     * `FILTER_VALUE`: a filter value (for example, `"https://example.sharepoint.com/*"`)

     * `ENTITY_NAME`: the name of an entity for the connector to search (see the [resource documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/discovery_engine_data_connector#argument-reference))

     * `CONNECTOR_MODES`: the modes to enable for the connector (for example, `"FEDERATED"`)

  2. Initialize Terraform:
         
         terraform init -upgrade
         

  3. Preview your configuration:
         
         terraform plan
         

  4. Apply the configuration:
         
         terraform apply
         

When prompted, confirm your changes.




After applying the configuration, you can see the data connector in the list of data stores and can connect it to a Gemini Enterprise app. For more information, see [Connect a data store to app and authorize Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-existing-data-store).

## Update a data connector

To use Terraform to update settings for an existing data connector, provide the new settings in `json_params`, and provide any unchanged arguments with their current values so that Terraform doesn't replace the resource. Add any required arguments that don't need to be updated to `ignore_changes` in the `lifecycle` block.

**Tip:** For the list of required arguments, see the [`google_discovery_engine_data_connector` resource documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/discovery_engine_data_connector#argument-reference).

  1. Create the Terraform configuration. This example updates the `structured_search_filter` setting with a new filter value, but lists other required fields such as `refresh_interval`, `entities`, and `connector_modes` with their current values.
         
         terraform {
           required_providers {
             google = {
               source  = "hashicorp/google"
               version = "7.7.0"
             }
           }
         }
         
         provider "google" {
           project               = "PROJECT_ID"
           user_project_override = true
           billing_project       = "BILLING_PROJECT_ID"
         }
         
         resource "google_discovery_engine_data_connector" "LOCAL_NAME" {
           provider = google
         
           project                 = "PROJECT_ID"
           location                = "LOCATION"
           collection_id           = "COLLECTION_ID"
           collection_display_name = "COLLECTION_DISPLAY_NAME"
         
           data_source = "DATA_SOURCE"
         
           json_params = jsonencode({
             "structured_search_filter" = { "FILTER_KEY" = ["UPDATED_FILTER_VALUE"] }
           })
           refresh_interval = "REFRESH_INTERVAL"
         
           entities {
             entity_name           = "ENTITY_NAME"
             key_property_mappings = {}
           }
           static_ip_enabled = false
           connector_modes   = [CONNECTOR_MODES]
         
           lifecycle {
             ignore_changes = [
               collection_display_name,
               entities,
               refresh_interval
             ]
           }
         }
         

Replace the following:

     * `PROJECT_ID`: your Google Cloud project ID

     * `BILLING_PROJECT_ID`: your Google Cloud billing project ID

     * `LOCAL_NAME`: the local name of the Terraform resource

     * `LOCATION`: the location for the data store, such as `us` or `global` (for more information, see [Gemini Enterprise Standard and Plus Editions data residency and ML regional processing commitments](https://docs.cloud.google.com/gemini/enterprise/docs/locations))

     * `COLLECTION_ID`: the collection ID

     * `COLLECTION_DISPLAY_NAME`: the collection display name

     * `DATA_SOURCE`: the data source type. The following values are supported:

       * `bigquery`

       * `confluence`

       * `jira`

       * `salesforce`

       * `sharepoint_federated_search`

     * `FILTER_KEY`: a filter key for which you want to update the value (for example, `Path`)

     * `UPDATED_FILTER_VALUE`: the new filter value (for example, `https://other.sharepoint.com/*`)

     * `REFRESH_INTERVAL`: the refresh interval

     * `ENTITY_NAME`: the name of an entity for the connector to search (see the [resource documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/discovery_engine_data_connector#argument-reference))

     * `CONNECTOR_MODES`: the modes to enable for the connector (for example, `"FEDERATED"`)

  2. Run `terraform import` to indicate that this is an update operation:
         
         terraform import \
         google_discovery_engine_data_connector.LOCAL_NAME \
         projects/PROJECT_ID/locations/LOCATION/collections/COLLECTION_ID/dataConnector
         

**Note:** The local name of the resource in the `terraform import` command must match the local name of the resource in the Terraform configuration.
  3. Preview your configuration:
         
         terraform plan
         

The output should be similar to the following:
         
         Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
           ~ update in-place
         
         Terraform will perform the following actions:
         
           google_discovery_engine_data_connector.update-sharepoint-connector will be updated in-place
           ~ resource "google_discovery_engine_data_connector" "update-sharepoint-connector" {
                 id                              = "projects/my-project-123/locations/global/collections/default_collection/dataConnector"
               ~ json_params                     = jsonencode(
                   ~ {
                       ~ structured_search_filter = {
                           ~ "Path" = [
                               ~ "https://other.sharepoint.com/*" - "https://example.sharepoint.com/*",
                                 (1 unchanged element hidden)
                             ]
                         }
                     }
                 )
                 name                            = "projects/my-project-123/locations/global/collections/default_collection/dataConnector"
                 (21 unchanged attributes hidden)
         
                 (2 unchanged blocks hidden)
             }
         
         Plan: 0 to add, 1 to change, 0 to destroy.
         

Ensure that the final line of output specifies `0 to add, 1 to change, 0 to destroy`.

  4. Apply the configuration:
         
         terraform apply
         

When prompted, confirm your changes.

The output should be similar to the following:
         
         Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
         




## What's next

  * To provide a user interface for querying your data, [create an app](https://docs.cloud.google.com/gemini/enterprise/docs/create-app) in Gemini Enterprise and [connect it to your data store](https://docs.cloud.google.com/gemini/enterprise/docs/connect-existing-data-store).

  * To manage the list of actions for a data connector, see [Manage actions](https://docs.cloud.google.com/gemini/enterprise/docs/manage-actions).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
