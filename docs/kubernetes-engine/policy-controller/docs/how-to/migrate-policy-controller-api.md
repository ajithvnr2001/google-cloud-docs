---
url: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/migrate-policy-controller-api/
title: Migrate from the ConfigManagement API to the PolicyController API \u00a0|\u00a0 Policy Controller \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:10:56.157652+00:00
---

# Migrate from the ConfigManagement API to the PolicyController API  |  Policy Controller  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/migrate-policy-controller-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Policy Controller ](https://docs.cloud.google.com/kubernetes-engine/policy-controller)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)



Send feedback 

#  Migrate from the ConfigManagement API to the PolicyController API Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to migrate from the `ConfigManagement` API to the `PolicyController` API for managing Policy Controller. The `PolicyController` API offers the same capabilities for installing and managing Policy Controller.

Starting in April, 2025, the `configManagement` API version 1.21 and later no longer supports Policy Controller installation or updates. Attempting to upgrade or install Policy Controller with this method will fail with an error. Follow the instructions on this page to migrate so that you can continue using Policy Controller.

The steps to fully migrate differ depending on which installation method you used to install Policy Controller.

If you use gcloud CLI `PolicyController` commands that start with `gcloud container fleet policycontroller`, you are already using the `PolicyController` API. No action is needed. Otherwise, review the instructions for the method that you used to install Policy Controller:

### `config management`

If you use gcloud CLI commands that start with `gcloud alpha container fleet config-management`, switch to using gcloud CLI Policy Controller commands that start with `gcloud container fleet policycontroller`. Review the [gcloud CLI documentation](https://docs.cloud.google.com/sdk/gcloud/reference/container/fleet/policycontroller) for a list of commands. No other action is required.

If your [Google Cloud CLI `apply spec` file](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/reference/gcloud-apply-fields#policy_controller) has the `policyController` block, remove it to ensure compatibility with Config Sync.

### Terraform

If you use a Terraform resource that configures Policy Controller with the [feature name `"configmanagement"`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_feature_membership), you should switch to a Terraform resource with the feature name `"policycontroller"` by completing the following steps:

  1. Copy your existing Terraform file to a new file, or update your Terraform file, and add the following:
         
         resource "google_gke_hub_feature" "feature" {
           name = "policycontroller"
           location = "global"
         }
         
         resource "google_gke_hub_feature_membership" "feature_member" {
           feature = google_gke_hub_feature.feature.name # "policycontroller"
           location = "global"
           membership = MEMBERSHIP_NAME
           project = PROJECT_ID
            policycontroller {
               policy_controller_hub_config {
                 install_spec = "INSTALL_SPEC_ENABLED"
             }
           }
         }
         

Replace the following:

     * `MEMBERSHIP`: the membership name of the registered cluster that has Policy Controller installed.
     * `PROJECT_ID`: your project ID.
  2. Remove the `"policy_controller"` block from your existing Terraform resource. You can find the block under the `"configmanagement"` block. If you're using the resource to _only_ manage Policy Controller, you can remove the entire `configmanagement` block. If you're using the resource to manage Config Sync, ensure you remove only the Policy Controller block. For example, your `configmanagement` block might resemble the following:
         
         resource "google_gke_hub_feature_membership" "feature_member" {
            provider   = google-beta
            location   = "global"
            feature    = "configmanagement"
            membership = google_gke_hub_membership.membership.membership_id
            configmanagement {
               version = "1.8.0"
               config_sync {
                  source_format = "unstructured"
                  git {
                  }
               }
               # if you're still using the config_sync block, delete only the policy_controller block
               policy_controller {
                  enabled                    = true
                  template_library_installed = true
                  referential_rules_enabled  = true
               }
            }
         }
         

  3. [Import the Policy Controller membership feature settings](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_feature#import) by completing one of the following steps:

     1. Run the following command:
            
            terraform import "google_gke_hub_feature.feature" "projects/PROJECT_ID/locations/global/features/policycontroller"
            terraform import "google_gke_hub_feature_membership.feature_member" "projects/PROJECT_ID/locations/global/features/policycontroller/membershipId/MEMBERSHIP_NAME"
            

     2. Add an [import block](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_feature_membership#import) to your Terraform resource:
            
            import {
               to = google_gke_hub_feature_membership.feature_member
               id = "projects/PROJECT_ID/locations/global/features/policycontroller/membershipId/MEMBERSHIP_NAME"
            }
            import {
               to = google_gke_hub_feature.feature
               id = "projects/PROJECT_ID/locations/global/features/policycontroller"
            }
            

  4. Apply the Policy Controller settings:
         
         terraform apply
         

  5. Optional: After the import is complete, you can remove the import block from your Terraform resource. Alternatively, it is safe to leave the import block in your configuration as a record of the resource's origin.




###  Config Connector 

To stop using the `configmanagement.policyController` spec, complete the following steps:

  1. Create a new [`GKEHubFeatureMembership` spec](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/gkehub/gkehubfeaturemembership) with the required `policycontroller` fields. Ensure that you set the `resourceID` field to `policyController`.

  2. If you have an existing `GKEHubFeatureMembership` that uses the `spec.configmanagement.policyController` field, remove any `policycontroller` fields from the `configmanagement` spec.




### kubectl

If you use `kubectl` commands to manage Policy Controller with a `ConfigManagement` object, switch to using gcloud CLI Policy Controller commands that start with `gcloud container fleet policycontroller`. No other action is required.

If your [`ConfigManagement` object](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/configmanagement-fields#integrations) has the `policyController` block, remove it for compatibility with Config Sync.

You might want to review the following resources to learn more about the Policy Controller API:

  * [Install Policy Controller with `gcloud container fleet policycontroller` commands](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/how-to/installing-policy-controller#gcloud-policycontroller)
  * Review the [Config Connector `GKEHubFeature` reference documentation](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/gkehub/gkehubfeature)
  * Review the [Terraform `google_gke_hub_feature` reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_featureP)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
