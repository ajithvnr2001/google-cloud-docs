---
url: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-tenancy/
title: Manage team resources across your fleet \u00a0|\u00a0 Config Sync \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:12.878551+00:00
---

# Manage team resources across your fleet  |  Config Sync  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/fleet-tenancy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Config Sync ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)



Send feedback 

#  Manage team resources across your fleet Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to use Config Sync and Terraform to dynamically create team-scoped resources across a fleet of clusters. Config Sync extends the capabilities of fleet team management to create and manage infrastructure and cluster configurations across your fleets.

This guide assumes that you are already familiar with fleet team management concepts like team scopes and fleet namespaces. For more information, see the [fleet team management overview](https://docs.cloud.google.com/anthos/fleet-management/docs/team-management).

For an end-to-end tutorial with sample configurations, see the [fleet tenancy tutorial](https://github.com/GoogleCloudPlatform/anthos-config-management-samples/tree/main/fleet-tenancy) in the sample repository.

For a list of fields supported for Config Sync in Terraform, see the [Terraform reference documentation for GKE fleet features](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_feature#config_sync).

## Example workflow

You're a platform administrator who wants to dynamically create resources across a fleet of clusters where different teams have different needs. For example, you might want to apply a `NetworkPolicy` to your Backend team's namespaces, but not your Frontend team's namespaces. In this scenario, the procedure for creating team-scoped resources across a namespace is as follows:

  1. Choose or create the fleet where you want to manage resources for teams.
  2. Set up your source of truth. The source of truth contains the `NamespaceSelector` objects that you use to to select fleet-level namespaces in your team scopes, and any resources (like a `NetworkPolicy`) that you want to sync across these namespaces.

**Key Term:** A `NamespaceSelector` is a special type of config used by Config Sync to limit which namespaces another config affects. For more information, see [Limit which namespaces a config affects](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/namespace-scoped-objects#namespaceselectors).
  3. Create the fleet-level default configuration for Config Sync. Config Sync uses these default settings when syncing from the source of truth created in the previous step. These Config Sync settings apply to any [new clusters created in the fleet](https://docs.cloud.google.com/anthos/fleet-management/docs/register/gke#register_a_new_cluster).

**Important:** You must create the fleet-level default configuration before creating new clusters. These settings are only automatically applied to new clusters created in the fleet. If you want to apply these settings to existing clusters, see [Configuring fleet-level defaults](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#configure-fleet) in the Config Sync installation guide.
  4. Create clusters in your fleet.

  5. Create your Frontend and Backend team scopes and namespaces so that Config Sync can detect and reconcile resources in your namespaces.




After you complete these steps, Config Sync creates and applies the `NetworkPolicy` based on the `NamespaceSelector` to the Backend team's namespaces. If you change or add any resources, Config Sync continuously detects and applies any changes to your configuration files, team scopes, fleet namespaces, and fleet members.

## Pricing

Config Sync and fleet team management features are available as part of GKE. For more information about pricing, see the [GKE Pricing page](https://cloud.google.com/kubernetes-engine/pricing).

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  7. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  8. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  9. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  10. Create, or have access to, a source of truth (either a Git repository or an OCI image) where you can store your configuration files. The examples in this guide use a Git repository. 



### Required roles

To get the permissions that you need to create team resources for your fleet, ask your administrator to grant you the following IAM roles on your project: 

  * Managing fleet resources: [Fleet Admin (formerly GKE Hub Admin) ](https://docs.cloud.google.com/iam/docs/roles-permissions/gkehub#gkehub.admin) (`roles/gkehub.admin`) 
  * Creating GKE clusters: [Kubernetes Engine Cluster Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/container#container.clusterAdmin) (`roles/container.clusterAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Acquire user credentials

To run the Terraform commands in this guide in your local environment, run the following command to [acquire new user credentials](https://docs.cloud.google.com/sdk/gcloud/reference/auth/application-default/login):
    
    
    gcloud auth application-default login
    

## Set up your fleet

In this section, you create your fleet and enable the required services.

To set up your fleet, complete the following steps:

  1. Create a directory for the fleet configuration Terraform files. To that directory, add a `main.tf` file and a `variables.tf` file.

  2. In the `variables.tf` file, add the following variables: 
         
         variable "project" {
           type = string
           description = "GCP project ID"
         }

  3. In the `main.tf` file, add the following resources:

**Note:** If you're using an existing fleet, omit the section that declares a fleet in the project.
         
         terraform {
           required_providers {
             google = {
               source = "hashicorp/google"
               version = ">= 5.16.0"
             }
           }
         }
         
         provider "google" {
           # project variable must be provided at runtime
           project = var.project
         }
         
         # Enable API services
         resource "google_project_service" "services" {
           for_each = toset([
             "gkehub.googleapis.com",
             "container.googleapis.com",
             "connectgateway.googleapis.com",
             "cloudresourcemanager.googleapis.com",
             "iam.googleapis.com",
             "anthos.googleapis.com",
             "anthosconfigmanagement.googleapis.com",
           ])
           service = each.value
           disable_on_destroy = false
         }
         
         # Declare a fleet in the project
         resource "google_gke_hub_fleet" "default" {
           display_name = "demo"
         
           depends_on = [google_project_service.services]
         }

  4. Export the PROJECT_ID variable:
         
         export TF_VAR_project=PROJECT_ID
         

Replace `PROJECT_ID` with the project ID where you want to create your fleet.

  5. Initialize Terraform in the directory that you created:
         
         terraform init
         

  6. Check that the changes you propose with Terraform match the expected plan:
         
         terraform plan
         

  7. Create the fleet, enable the APIs, and create the service account:
         
         terraform apply
         

It can sometimes take a few minutes to enable all of the services.




## Set up your source of truth

In this section, you add configuration files to a source of truth. You need a [`NamespaceSelector` object](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/namespace-scoped-objects#namespaceselectors) for each team scope that you want to use. For example, if you have Frontend and Backend teams, you must create a `NamespaceSelector` object for each team. The `NamespaceSelector` object selects all or some of the namespaces within a team scope. You can add additional team resources to your source of truth, like a `NetworkPolicy`. When you create these resources, you reference the `NamespaceSelector` so that Config Sync can deploy and sync those resources dynamically across namespaces.

To set up your source of truth, complete the following steps:

  1. In your source of truth, create a directory for the configuration files that you want Config Sync to sync from.

  2. For each team, create a `NamespaceSelector` object in your configuration directory:

**Important:** the `NamespaceSelector` must have the mode set to `dynamic`. The dynamic mode allows the selection of namespaces both statically declared in the source of truth and any namespaces dynamically present on the cluster.
         
         apiVersion: configmanagement.gke.io/v1
         kind: NamespaceSelector
         metadata:
            name: NAMESPACE_SELECTOR_NAME
         spec:
           mode: dynamic
           selector:
             matchLabels:
               fleet.gke.io/fleet-scope: SCOPE_NAME
         

Replace the following:

     * `NAMESPACE_SELECTOR_NAME`: the name for the `NamespaceSelector` object, for example `backend-scope`.
     * `SCOPE_NAME`: the name of your team scope, for example `backend`.

Any namespaces that are part of a fleet namespace automatically have the label `fleet.gke.io/fleet-scope: SCOPE_NAME`. The `NamespaceSelector` selects all fleet namespaces of a team scope using that label. For more examples about how to include or exclude namespaces, see [`NamespaceSelector` examples](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/namespace-scoped-objects#namespaceselectors).

  3. Create any objects that you want to sync across namespaces.

To sync an object only to a particular team, set the following annotation in that object's metadata:
         
         annotations:
           configmanagement.gke.io/namespace-selector: NAMESPACE_SELECTOR_NAME
         

For example, a `NetworkPolicy` for the Backend team might resemble the following:
         
         apiVersion: networking.k8s.io/v1
         kind: NetworkPolicy
         metadata:
           name: be-deny-all
           annotations:
             configmanagement.gke.io/namespace-selector: backend-scope # Actuate this resource in the namespaces with labels matched by the namespace selector
         spec:
           ingress:
           - from:
             - podSelector: {}
           podSelector:
             matchLabels: null




## Create fleet-level defaults for Config Sync

In this section, you create fleet-level defaults for Config Sync, which applies the same Config Sync configuration to all clusters created in your fleet.

**Note:** if you previously installed Config Sync and [set up fleet defaults](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#configure-fleet), including the `git` or `oci` configuration, by using Terraform or gcloud CLI, you can skip this section. If you used the Google Cloud console to set fleet defaults, you might need to import your existing feature settings using [`terraform import`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_feature#import) before running `terraform plan` and `terraform apply`.

To create a fleet-level default configuration for Config Sync, complete the following steps:

  1. Create a directory for the fleet-default configuration Terraform files. To that directory, add a `main.tf` file and a `variables.tf` file.

  2. In the `variables.tf` file, add the following variables: 
         
         variable "project" {
           type = string
           description = "GCP project ID"
         }

  3. In the `main.tf` file, add the following resource to configure Config Sync's settings:

### git
         
         terraform {
           required_providers {
             google = {
               source = "hashicorp/google"
               version = ">=5.16.0"
              }
            }
          }
         
         provider "google" {
           project = var.project
         }
         
         resource "google_gke_hub_feature" "feature" {
           name = "configmanagement"
           location = "global"
           provider = google
           fleet_default_member_config {
             configmanagement {
             version = "VERSION"
          config_sync {
            source_format = "unstructured"
            git {
              sync_repo = "REPO"
              sync_branch = "BRANCH"
              policy_dir = "DIRECTORY"
              secret_type = "SECRET"
                 }
               }
             }
           }
         }
         

Replace the following:

     * `VERSION`: (optional) the Config Sync version number. If left blank, the default is the latest version.
     * `REPO`: the URL to the repository containing your configuration files.
     * `BRANCH`: the repository branch, for example `main`.
     * `DIRECTORY`: the path within the Git repository that represents the top level of the repository you want to sync.
     * `SECRET`: the secret authentication type.

For a full list of settings supported in the Config Sync `git` block, see the [Terraform reference documentation for GKE hub features](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_feature#git).

### OCI
    
    terraform {
      required_providers {
        google = {
          source = "hashicorp/google"
          version = ">=5.16.0"
         }
       }
     }
    
    provider "google" {
      project = var.project
    }
    
    resource "google_gke_hub_feature" "feature" {
      name = "configmanagement"
      location = "global"
      provider = google
      fleet_default_member_config {
        configmanagement {
        version = "VERSION"
        config_sync {
        source_format = "unstructured"
        oci {
         sync_repo = "REPO"
         policy_dir = "DIRECTORY"
         secret_type = "SECRET"
         }
        }
        }
      }
    }
    

Replace the following:

     * `VERSION`: the Config Sync version number. If left blank, the default is the latest version.
     * `REPO`: the URL to the OCI image repository containing configuration files.
     * `DIRECTORY`: the absolute path of the directory containing the resources you want to sync. Leave blank to use the root directory.
     * `SECRET`: the secret auth type.

For a full list of settings supported in the Config Sync `oci` block, see the [Terraform reference documentation for GKE hub features](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/gke_hub_feature#oci).

As an example, the following `main.tf` file configures Config Sync to sync from a Git repository and syncs all of the objects present in the `config` directory:
    
    terraform {
      required_providers {
        google = {
          source = "hashicorp/google"
          version = ">= 5.16.0"
        }
      }
    }
    
    provider "google" {
      project = var.project
    }
    
    resource "google_gke_hub_feature" "feature" {
      name = "configmanagement"
      location = "global"
      provider = google
      fleet_default_member_config {
        configmanagement {
          # version = "1.17.0" # Use the default latest version; if specifying a version, it must be at or after 1.17.0
          config_sync {
            source_format = "unstructured"
            git {
              sync_repo = "https://github.com/GoogleCloudPlatform/anthos-config-management-samples"
              sync_branch = "main"
              policy_dir = "fleet-tenancy/config"
              secret_type = "none"
            }
          }
        }
      }
    }

  4. Initialize Terraform in the directory that you created:
         
         terraform init
         

  5. Check that the changes you propose with Terraform match the expected plan:
         
         terraform plan
         

  6. Create the default fleet member configurations:
         
         terraform apply
         




## Create clusters in your fleet

In this section, you create a shared cluster configuration and then create clusters in your fleet.

To create and register new clusters to your fleet, complete the following steps:

  1. Create a directory for the cluster configuration Terraform files. To that directory, add a `main.tf` file and a `variables.tf` file.

  2. In the `variables.tf` file, add the following variables: 
         
         variable "project" {
           type = string
           description = "GCP project ID"
         }

  3. Create a `cluster.tf` file that contains default values used across all your clusters, such as your project and fleet IDs:
         
         variable "location" {
           type = string
         }
         
         variable "cluster_name" {
           type = string
         }
         
         data "google_project" "project" {
           provider = google
         }
         
         resource "google_container_cluster" "cluster" {
          provider = google
          name               = var.cluster_name
          location           = var.location
          initial_node_count = 3
          project = data.google_project.project.project_id
          fleet {
            project = data.google_project.project.project_id
          }
          workload_identity_config {
            workload_pool = "${data.google_project.project.project_id}.svc.id.goog"
          }
          deletion_protection = false
         }
         

  4. In the `main.tf` file, add the following resources:
         
         terraform {
           required_providers {
             google = {
             source = "hashicorp/google"
             version = ">=5.16.0"
             }
           }
         }
         
         provider "google" {
           project = var.project
         }
         
         module "MODULE_NAME" {
           source = "CLUSTER_CONFIGURATION_FILEPATH"
           cluster_name = "CLUSTER_NAME"
           location="CLUSTER_LOCATION"
         }
         

Replace the following:

     * `MODULE_NAME`: the name that you want to give the cluster module. MODULE_NAME and CLUSTER_NAME can be the same value, for example `us-east-cluster`.
     * `CLUSTER_CONFIGURATION_FILEPATH`: the relative path to the `cluster.tf` file that you created.
     * `CLUSTER_NAME`: the name of your cluster. MODULE_NAME and CLUSTER_NAME can be the same value, for example `us-east-cluster`.
     * `CLUSTER_LOCATION`: the location of your cluster, for example `us-east1`.

You can create as many clusters as you want. As an example, the following `main.tf` file creates 3 clusters in different regions:
    
    terraform {
      required_providers {
        google = {
          source = "hashicorp/google"
          version = ">= 5.16.0"
        }
      }
    }
    
    provider "google" {
      project = var.project
    }
    
    module "us-west-cluster" {
      source = "./cluster"
      cluster_name = "us-west-cluster"
      location="us-west1-a"
    }
    
    module "us-east-cluster" {
      source = "./cluster"
      cluster_name = "us-east-cluster"
      location="us-east1-b"
    }
    
    module "us-central-cluster" {
      source = "./cluster"
      cluster_name = "us-central-cluster"
      location="us-central1-c"
    }

  5. Initialize Terraform in the directory that you created:
         
         terraform init
         

  6. Check that the changes you propose with Terraform match the expected plan:
         
         terraform plan
         

  7. Create the clusters:
         
         terraform apply
         




## Configure team scopes and fleet namespaces

In this section, you create your team scopes and associate your clusters with those scopes. Then you create the fleet namespaces that you require, for example one for each team, in each scope, and Config Sync creates the resources across your namespaces.

To configure team scopes and namespaces, complete the following steps:

  1. Create a directory for the team scope and namespace configuration Terraform files. To that directory, add a `main.tf` file and a `variables.tf` file.

  2. In the `variables.tf` file, add the following variables: 
         
         variable "project" {
           type = string
           description = "GCP project ID"
         }
         

  3. In the `main.tf` file, add the following resources:

     1. Add the provider information:
            
            terraform {
              required_providers {
                google = {
                  source = "hashicorp/google"
                  version = ">=5.16.0"
                 }
               }
             }
            
            provider "google" {
              project = var.project
            }
            

     2. Add the team scope resource:
            
            resource "google_gke_hub_scope" "scope" {
              provider = google
              for_each = toset([
                "SCOPE_NAME",
                "SCOPE_NAME_2",
              ])
              scope_id = each.value
            }
            

Replace the following:

        * `SCOPE_NAME`: the name of your team scope, for example `backend`.
        * `SCOPE_NAME_2`: an additional team scope if you created one.

You can add as many team scopes as you need. When a fleet namespace is created in the cluster, the namespace is automatically labelled with `fleet.gke.io/fleet-scope: SCOPE_NAME`, allowing Config Sync to select namespaces based on the `NamespaceSelector` labels present when syncing Kubernetes resources.

As an example, a team scope Terraform resource that includes a scope for both the Frontend and Backend team might resemble the following:
    
    resource "google_gke_hub_scope" "scope" {
      provider = google
      for_each = toset([
        "backend",
        "frontend",
      ])
      scope_id = each.value
    }

     3. Add a fleet membership binding for each cluster that you want to apply to a team scope:
            
            resource "google_gke_hub_membership_binding" "membership-binding" {
              provider = google
              for_each = {
                MEMBERSHIP_BINDING_NAME = {
                  membership_binding_id = "MEMBERSHIP_BINDING_ID"
                  scope = google_gke_hub_scope.scope["SCOPE_NAME"].name
                  membership_id = "CLUSTER_NAME"
                  location = "CLUSTER_LOCATION"
                }
                MEMBERSHIP_BINDING_NAME_2 = {
                  membership_binding_id = "MEMBERSHIP_BINDING_ID_2"
                  scope = google_gke_hub_scope.scope["SCOPE_NAME_2"].name
                  membership_id = "CLUSTER_NAME_2"
                  location = "CLUSTER_LOCATION_2"
                }
              }
              membership_binding_id = each.value.membership_binding_id
              scope = each.value.scope
              membership_id = each.value.membership_id
              location = each.value.location
            
              depends_on = [google_gke_hub_scope.scope]
            }
            

Replace the following:

        * `MEMBERSHIP_BINDING_NAME`: the membership binding name, for example `us-east-backend`.
        * `MEMBERSIP_BINDING_ID`: the membership binding ID. This can be the same as the MEMBERSHIP_BINDING_NAME.
        * `SCOPE_NAME`: the label selector that you gave your team scope when you created a `NamespaceSelector`, for example `backend`.
        * `CLUSTER_NAME`: the name of the cluster that you created when you created clusters, for example `us-east-cluster`.
        * `CLUSTER_LOCATION`: the cluster location, for example `us-east1`.

You need to define a fleet membership binding for each cluster. If you don't define a team scope for a cluster, then that cluster is not created for that namespace. For example, if you have three clusters in regions `us-east1`, `us-west1`, and `us-central1`, but the `us-central1` cluster is only for the Frontend team, your membership binding resource would resemble the following:
    
    resource "google_gke_hub_membership_binding" "membership-binding" {
      provider = google
      for_each = {
        us-east-backend = {
          membership_binding_id = "us-east-backend"
          scope = google_gke_hub_scope.scope["backend"].name
          membership_id = "us-east-cluster"
          location = "us-east1"
        }
        us-west-backend = {
          membership_binding_id = "us-west-backend"
          scope = google_gke_hub_scope.scope["backend"].name
          membership_id = "us-west-cluster"
          location = "us-west1"
        }
        us-east-frontend = {
          membership_binding_id = "us-east-frontend"
          scope = google_gke_hub_scope.scope["frontend"].name
          membership_id = "us-east-cluster"
          location = "us-east1"
        }
        us-west-frontend = {
          membership_binding_id = "us-west-frontend"
          scope = google_gke_hub_scope.scope["frontend"].name
          membership_id = "us-west-cluster"
          location = "us-west1"
        }
        us-central-frontend = {
          membership_binding_id = "us-central-frontend"
          scope = google_gke_hub_scope.scope["frontend"].name
          membership_id = "us-central-cluster"
          location = "us-central1"
        }
      }
    
      membership_binding_id = each.value.membership_binding_id
      scope = each.value.scope
      membership_id = each.value.membership_id
      location = each.value.location
    
      depends_on = [google_gke_hub_scope.scope]
    }

     4. Add any namespaces that you want to define for your teams:
            
            resource "google_gke_hub_namespace" "fleet_namespace" {
              provider = google
            
              for_each = {
                FLEET_NAMESPACE = {
                  scope_id = "SCOPE_NAME"
                  scope_namespace_id = "FLEET_NAMESPACE_ID"
                  scope = google_gke_hub_scope.scope["SCOPE_NAME"].name
                }
                FLEET_NAMESPACE_2 = {
                  scope_id = "SCOPE_NAME"
                  scope_namespace_id = "FLEET_NAMESPACE_ID_2"
                  scope = google_gke_hub_scope.scope["SCOPE_NAME"].name
                }
            
            }
            
              scope_namespace_id = each.value.scope_namespace_id
              scope_id = each.value.scope_id
              scope = each.value.scope
            
              depends_on = [google_gke_hub_scope.scope]
            }
            

Replace the following:

        * `FLEET_NAMESPACE`: that name that you want to give the namespace, for example `backend-a`.
        * `SCOPE_NAME`: the label selector that you gave your team scope when you created a `NamespaceSelector`, for example `backend`.
        * `FLEET_NAMESPACE_ID`: the namespace ID. This can be the same value as FLEET_NAMESPACE.

For example, if you wanted both the Frontend and Backend team to have two namespaces each, your fleet namespace resource might resemble the following:
    
    resource "google_gke_hub_namespace" "fleet_namespace" {
      provider = google
    
      for_each = {
        bookstore = {
          scope_id = "backend"
          scope_namespace_id = "bookstore"
          scope = google_gke_hub_scope.scope["backend"].name
        }
        shoestore = {
          scope_id = "backend"
          scope_namespace_id = "shoestore"
          scope = google_gke_hub_scope.scope["backend"].name
        }
        frontend_a = {
          scope_id = "frontend"
          scope_namespace_id = "frontend-a"
          scope = google_gke_hub_scope.scope["frontend"].name
        }
        frontend_b = {
          scope_id = "frontend"
          scope_namespace_id = "frontend-b"
          scope = google_gke_hub_scope.scope["frontend"].name
        }
      }
    
      scope_namespace_id = each.value.scope_namespace_id
      scope_id = each.value.scope_id
      scope = each.value.scope
    
      depends_on = [google_gke_hub_scope.scope]
    }

  4. Initialize Terraform in the directory that you created:
         
         terraform init
         

  5. Check that the changes you propose with Terraform match the expected plan:
         
         terraform plan
         

  6. Create the fleet scopes and namespaces:
         
         terraform apply
         




After you create fleet scopes and namespaces, Config Sync detects those new namespaces and their scopes, selects resources in the fleet namespaces, and reconciles them with your configuration files.

You can check that your resources are applied to the correct cluster by using [`nomos status`](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/nomos-command#status-install) or by visiting the Config Sync **Packages** tab in the Google Cloud console and changing the **View by** radio button to **Cluster**.

[Go to Packages](https://console.cloud.google.com/kubernetes/config_management/packages)

Config Sync syncs your resources across namespaces based on your team scopes according to the configuration stored in your source of truth. Whenever you add a new resource, as long as you include the correct `NamespaceSelector` annotation, Config Sync automatically reconciles that resource across your team namespaces.

If you want to apply Config Sync settings to your existing clusters, see the instructions for [Configuring fleet-level defaults](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/how-to/installing-config-sync#configure-fleet) in the Config Sync installation guide.

## What's next

  * Learn more about [setting up teams for your fleet](https://docs.cloud.google.com/anthos/fleet-management/docs/setup-teams#team_setup_overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
