---
url: https://docs.cloud.google.com/compute/vm-manager/docs/vm-manager-org-terraform/
title: Set up VM Manager across an organization by using Terraform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:34:56.856681+00:00
---

# Set up VM Manager across an organization by using Terraform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/vm-manager/docs/vm-manager-org-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ VM Manager ](https://docs.cloud.google.com/compute/vm-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/vm-manager/docs/overview)



Send feedback 

#  Set up VM Manager across an organization by using Terraform Stay organized with collections  Save and categorize content based on your preferences. 

To enforce consistent operating system configurations and automate compliance across the Google Cloud resource hierarchy, use Terraform to configure [VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs) at the organization level.

This document explains how to use Terraform to automatically enable VM Manager (OS Config API), set common instance metadata, and assign OS policies across all target projects in your resource hierarchy.

For an overview of Terraform resources available for VM Manager, see [Provision VM Manager resources by using Terraform](https://docs.cloud.google.com/compute/vm-manager/docs/terraform).

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

To use the Terraform samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  * If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  * If you're using a local shell, then create local authentication credentials for your user account: 
        
        gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up authentication for a local development environment](https://docs.cloud.google.com/compute/docs/authentication#local-development). 




## Before you begin

  * Review [Setup overview](https://docs.cloud.google.com/compute/vm-manager/docs/setup#overview) for VM Manager.
  * Review [OS Config quotas](https://docs.cloud.google.com/compute/vm-manager/docs/os-config-quotas).
  * Prepare your [Terraform environment](https://docs.cloud.google.com/docs/terraform/install-configure-terraform).



## Required IAM permissions

To automatically enable VM Manager and assign OS policies across multiple projects, the principal or service account that runs Terraform requires specific Identity and Access Management (IAM) permissions.

### Target project permissions

To get the permissions that you need to activate the VM Manager service and set project metadata, ask your administrator to grant you the following IAM roles on each target project: 

  * [Service Usage Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageAdmin) (`roles/serviceusage.serviceUsageAdmin`)
  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to activate the VM Manager service and set project metadata. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to activate the VM Manager service and set project metadata:

  * `serviceusage.services.enable`
  * `compute.projects.setCommonInstanceMetadata`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** Don't grant the `serviceusage.services.disable` permission. Granting disable permissions poses operational risks if required services are accidentally disabled. 

### Service account and custom role setup

Google recommends that you create a dedicated [service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts) to run your centralized Terraform automation.

To grant the required permissions to this service account across multiple projects, create an [IAM custom role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#iam-custom-roles-create-gcloud) at the organization level:

  1. Create an organization-level custom role that includes `serviceusage.services.enable` and `compute.projects.setCommonInstanceMetadata`.
  2. [Grant the custom role to your service account](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) at the lowest applicable scope, such as the organization or folder level. For example, if your target projects are all contained within a specific folder, grant the role at the folder level.



## Enable VM Manager by using Terraform

To enable VM Manager and assign OS policies across multiple projects, use one of the following automated approaches: golden project blueprints or centralized project management.

### Use golden project blueprints

If your organization uses a standardized Terraform project module (a golden blueprint) or a centrally enforced mechanism to provision projects, add the following resource definitions to your project blueprint:

  * [`google_project_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_service)
  * [`google_project_service_identity`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/project_service_identity)
  * [`google_project_iam_member`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/google_project_iam#google_project_iam_member)
  * [`google_compute_project_metadata_item`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_project_metadata_item)



To enable VM Manager, include the following service and metadata resources:
    
    
    # Enable the OS Config API
    resource "google_project_service" "osconfig" {
      service            = "osconfig.googleapis.com"
      disable_on_destroy = false
    }
    
    # Explicitly provision the OS Config Service Agent
    resource "google_project_service_identity" "osconfig_identity" {
      provider = google-beta
      project  = google_project_service.osconfig.project
      service  = "osconfig.googleapis.com"
    }
    
    # Grant the required role to the explicitly provisioned Service Agent
    resource "google_project_iam_member" "osconfig_service_agent_binding" {
      project = google_project_service.osconfig.project
      role    = "roles/osconfig.serviceAgent"
      member  = "serviceAccount:${google_project_service_identity.osconfig_identity.email}"
    }
    
    # Set project metadata to enable VM Manager
    resource "google_compute_project_metadata_item" "enable_osconfig" {
      key   = "enable-osconfig"
      value = "TRUE"
    }
    

To deploy OS policy assignments across all VMs provisioned by the blueprint, append the following policy assignment resource:
    
    
    resource "google_os_config_os_policy_assignment" "base_security_policy" {
      name        = "base-security-ospolicy"
      description = "Ensure baseline security agent is installed and operational"
      location    = var.zone
    
      os_policies {
        id   = "no-op-policy"
        mode = "ENFORCEMENT"
    
        resource_groups {
          resources {
            id = "sample"
            exec {
              validate {
                interpreter = "SHELL"
                script      = "exit 100"
              }
              enforce {
                interpreter = "SHELL"
                script      = "exit 100"
              }
            }
          }
        }
      }
    
      os_policies {
        id   = "install-security-agent"
        mode = "ENFORCEMENT"
    
        resource_groups {
          resources {
            id = "install-agent"
            pkg {
              desired_state = "INSTALLED"
              apt {
                name = "security-agent"
              }
              yum {
                name = "security-agent"
              }
            }
          }
        }
      }
    
      instance_filter {
        all = true
      }
    
      rollout {
        disruption_budget {
          percent = 10
        }
        min_wait_duration = "3.5s"
      }
    }
    

### Centrally manage all projects

If modifying a golden project blueprint is not applicable, then you can centrally manage VM Manager enablement and OS policy assignments across multiple existing projects by using the Terraform `for_each` argument.

To enable VM Manager across target projects, use the `for_each` argument to iterate over your project map:
    
    
    resource "google_project_service" "osconfig" {
      for_each           = var.target_projects
      project            = each.key
      service            = "osconfig.googleapis.com"
      disable_on_destroy = false
    }
    
    resource "google_project_service_identity" "osconfig_identity" {
      provider = google-beta
      for_each = var.target_projects
      project  = google_project_service.osconfig[each.key].project
      service  = "osconfig.googleapis.com"
    }
    
    resource "google_project_iam_member" "osconfig_service_agent_binding" {
      for_each = var.target_projects
      project  = google_project_service.osconfig[each.key].project
      role     = "roles/osconfig.serviceAgent"
      member   = "serviceAccount:${google_project_service_identity.osconfig_identity[each.key].email}"
    }
    
    resource "google_compute_project_metadata_item" "enable_osconfig" {
      for_each = var.target_projects
      project  = each.key
      key      = "enable-osconfig"
      value    = "TRUE"
    }
    

To assign an OS policy across target projects, define the policy assignment resource with the `for_each` argument:
    
    
    resource "google_os_config_os_policy_assignment" "observability_agent_policy" {
      for_each    = var.target_projects
      project     = each.key
      name        = "observability-agent-ospolicy"
      description = "Install Google Cloud Observability agent on CentOS VMs across target projects"
      location    = var.zone
    
      os_policies {
        id   = "setup-repo-and-install-package-policy"
        mode = "ENFORCEMENT"
    
        resource_groups {
          inventory_filters {
            os_short_name = "centos"
            os_version    = "8"
          }
    
          resources {
            id = "setup-repo"
            repository {
              yum {
                id           = "google-cloud-ops-agent"
                display_name = "Google Cloud Ops Agent Repository"
                base_url     = "https://packages.cloud.google.com/yum/repos/google-cloud-ops-agent-el8-x86_64-all"
                gpg_keys = [
                  "https://packages.cloud.google.com/yum/doc/yum-key.gpg",
                  "https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg",
                ]
              }
            }
          }
    
          resources {
            id = "install-pkg"
            pkg {
              desired_state = "INSTALLED"
              yum {
                name = "google-cloud-ops-agent"
              }
            }
          }
        }
      }
    
      instance_filter {
        all = true
      }
    
      rollout {
        disruption_budget {
          percent = 10
        }
        min_wait_duration = "3.5s"
      }
    }
    

#### Define target projects

You can provide the `var.target_projects` map to your Terraform configuration by using either fixed scoping or dynamic scoping:

  * **Fixed scoping.** Maintain an explicit list of project IDs in a local variable or external data file. Fixed scoping requires you to update the list whenever you create or delete projects.
  * **Dynamic scoping.** Discover target projects based on resource hierarchy rules (for example, all projects within an organization or folder). You can query projects using the `google_projects` data source:
        
        data "google_projects" "in_folder" {
         filter = "parent.id:${local.folder_id}"
         }
        

To handle exceptions, filter out projects that contain specific exclusion labels. You can also execute external scripts using `local_exec` that run Google Cloud CLI commands (such as `gcloud asset search-all-resources`) to generate dynamic target lists.




#### Establish a stateless automated workflow

When you use dynamic scoping, your target project list changes constantly. Using a standard persistent Terraform state file requires manual effort to import new resources and remove deleted projects from state.

To manage dynamic scoping efficiently, implement a stateless automated workflow using Cloud Build:

  1. **Initialize Terraform.** Run `terraform init` by using a temporary, non-persistent local backend.
  2. **Discover target projects.** Generate the current list of target projects based on your dynamic scoping criteria.
  3. **Import existing resources.** Execute `terraform import` to pull existing `google_project_service`, `google_project_service_identity`, `google_project_iam_member`, `google_compute_project_metadata_item`, and `google_os_config_os_policy_assignment` resources into the local state.
  4. **Apply configuration.** Run standard Terraform commands (`terraform plan` and `terraform apply`), passing the discovered project list to your declarations.
  5. **Store run artifacts.** Optionally save plan outputs, state snapshots, and copy summaries to a Cloud Storage bucket for auditing.



Schedule your Cloud Build pipeline to run periodically (for example, daily or weekly) to automatically detect configuration drift and enforce compliance across your organization.

## View organization-level VM Manager status

After you set up VM Manager across your organization, you can view enablement and operating system status reports across all projects in your hierarchy. By exporting Cloud Asset Inventory data to BigQuery, you can run SQL queries to check whether VM Manager is enabled, check OS Config agent versions, and inspect operating system details across all projects in your organization.

To learn how to export data and run status report queries, see [View VM Manager status for your organization by using Cloud Asset Inventory and BigQuery](https://docs.cloud.google.com/compute/vm-manager/docs/view-org-status).

## What's next

  * [View VM Manager status for your organization by using Cloud Asset Inventory and BigQuery](https://docs.cloud.google.com/compute/vm-manager/docs/view-org-status).
  * [Create an OS policy assignment](https://docs.cloud.google.com/compute/vm-manager/docs/os-policies/create-os-policy-assignment).
  * [Create patch jobs](https://docs.cloud.google.com/compute/vm-manager/docs/patch/create-patch-job).
  * [Troubleshoot VM Manager](https://docs.cloud.google.com/compute/vm-manager/docs/troubleshooting/troubleshoot-vm-manager).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
