---
url: https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/create-cluster-using-terraform/
title: Quickstart: Create a GKE cluster and deploy a workload using Terraform \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:13.192706+00:00
---

# Quickstart: Create a GKE cluster and deploy a workload using Terraform  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/create-cluster-using-terraform/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Create a cluster and deploy a workload using Terraform

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

A Kubernetes _cluster_ provides compute, storage, networking, and other services for applications, similar to a virtual data center. Apps and their associated services that run in Kubernetes are called _workloads_.

This tutorial lets you quickly see a running Google Kubernetes Engine cluster and sample workload, all set up using Terraform. You can then explore the workload in the Google Cloud console before going on to our [more in-depth learning path](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps), or to start planning and creating your own production-ready cluster. This tutorial assumes that you are already familiar with Terraform.

If you'd prefer to set up your sample cluster and workload in the Google Cloud console, see [Create a cluster in the Google Cloud console](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/create-cluster).

**What is Terraform?** Infrastructure as Code (IaC) is a practice of managing and provisioning software infrastructure resources using code. Terraform is a popular open source IaC tool created by HashiCorp that supports a wide range of Cloud services, including GKE. As a GKE platform administrator, you can use Terraform to standardize configuration of your Kubernetes clusters in production and streamline your DevOps workflows. To learn more, see [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke). 

## Before you begin

Take the following steps to enable the Kubernetes Engine API:

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

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the GKE API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

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

  12. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  13. Enable the GKE API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable container.googleapis.com

  14. Grant roles to your user account. Run the following command once for each of the following IAM roles: `roles/container.admin, roles/compute.networkAdmin, roles/iam.serviceAccountUser`
         
         gcloud projects add-iam-policy-binding PROJECT_ID --member="user:USER_IDENTIFIER" --role=ROLE

Replace the following:

     * `PROJECT_ID`: Your project ID.
     * `USER_IDENTIFIER`: The identifier for your user account. For example, `myemail@example.com`. 
     * `ROLE`: The IAM role that you grant to your user account.



## Prepare the environment

In this tutorial you use [Cloud Shell](https://docs.cloud.google.com/shell) to manage resources hosted on Google Cloud. Cloud Shell is preinstalled with the software you need for this tutorial, including [Terraform](https://docs.cloud.google.com/docs/terraform), [`kubectl`](https://kubernetes.io/docs/reference/kubectl/), and the the [Google Cloud CLI](https://docs.cloud.google.com/sdk/gcloud).

  1. Launch a Cloud Shell session from the Google Cloud console, by clicking the Cloud Shell activation icon **Activate Cloud Shell** ![Activate Shell Button](https://docs.cloud.google.com/static/kubernetes-engine/images/cloud-shell.png). This launches a session in the bottom pane of the Google Cloud console.

The service credentials associated with this virtual machine are automatic, so you don't have to set up or download a service account key.

  2. Before you run commands, set your default project in the gcloud CLI using the following command:
         
         gcloud config set project PROJECT_ID
         

Replace `PROJECT_ID` with your [project ID](https://support.google.com/cloud/answer/6158840).

  3. Clone the GitHub repository:
         
         git clone https://github.com/terraform-google-modules/terraform-docs-samples.git --single-branch
         

  4. Change to the working directory:
         
         cd terraform-docs-samples/gke/quickstart/autopilot
         




## Review the Terraform files

The [Google Cloud provider](https://registry.terraform.io/providers/hashicorp/google/latest/docs) is a plugin that lets you manage and provision Google Cloud resources using Terraform. It serves as a bridge between Terraform configurations and Google Cloud APIs, letting you declaratively define infrastructure resources, such as virtual machines and networks.

The cluster and sample app for this tutorial are specified in two Terraform files that use the Google Cloud and Kubernetes providers.

  1. Review the `cluster.tf` file:
         
         cat cluster.tf
         

The output is similar to the following
         
         resource "google_compute_network" "default" {
           name = "example-network"
         
           auto_create_subnetworks  = false
           enable_ula_internal_ipv6 = true
         }
         
         resource "google_compute_subnetwork" "default" {
           name = "example-subnetwork"
         
           ip_cidr_range = "10.0.0.0/16"
           region        = "us-central1"
         
           stack_type       = "IPV4_IPV6"
           ipv6_access_type = "INTERNAL" # Change to "EXTERNAL" if creating an external loadbalancer
         
           network = google_compute_network.default.id
           secondary_ip_range {
             range_name    = "services-range"
             ip_cidr_range = "192.168.0.0/24"
           }
         
           secondary_ip_range {
             range_name    = "pod-ranges"
             ip_cidr_range = "192.168.1.0/24"
           }
         }
         
         resource "google_container_cluster" "default" {
           name = "example-autopilot-cluster"
         
           location                 = "us-central1"
           enable_autopilot         = true
           enable_l4_ilb_subsetting = true
         
           network    = google_compute_network.default.id
           subnetwork = google_compute_subnetwork.default.id
         
           ip_allocation_policy {
             stack_type                    = "IPV4_IPV6"
             services_secondary_range_name = google_compute_subnetwork.default.secondary_ip_range[0].range_name
             cluster_secondary_range_name  = google_compute_subnetwork.default.secondary_ip_range[1].range_name
           }
         
           # Set `deletion_protection` to `true` will ensure that one cannot
           # accidentally delete this instance by use of Terraform.
           deletion_protection = false
         }

This file describes the following resources:

     * `google_compute_network`: a VPC network with internal IPv6 enabled.
     * `google_compute_subnetwork`: a [dual-stack subnetwork](https://docs.cloud.google.com/vpc/docs/subnets#subnet-types).
     * `google_container_cluster`: a [dual-stack Autopilot mode cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alias-ips#dual_stack_network) located in `us-central1`. The `deletion_protection` setting controls whether you can use Terraform to delete this cluster. If you set the value in the `deletion_protection` field to `false`, Terraform can delete the cluster. For details, see the [`google_container_cluster` reference](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/container_cluster).
  2. Review the `app.tf` file:
         
         cat app.tf
         

The output is similar to the following:
         
         data "google_client_config" "default" {}
         
         provider "kubernetes" {
           host                   = "https://${google_container_cluster.default.endpoint}"
           token                  = data.google_client_config.default.access_token
           cluster_ca_certificate = base64decode(google_container_cluster.default.master_auth[0].cluster_ca_certificate)
         
           ignore_annotations = [
             "^autopilot\\.gke\\.io\\/.*",
             "^cloud\\.google\\.com\\/.*"
           ]
         }
         
         resource "kubernetes_deployment_v1" "default" {
           metadata {
             name = "example-hello-app-deployment"
           }
         
           spec {
             selector {
               match_labels = {
                 app = "hello-app"
               }
             }
         
             template {
               metadata {
                 labels = {
                   app = "hello-app"
                 }
               }
         
               spec {
                 container {
                   image = "us-docker.pkg.dev/google-samples/containers/gke/hello-app:2.0"
                   name  = "hello-app-container"
         
                   port {
                     container_port = 8080
                     name           = "hello-app-svc"
                   }
         
                   security_context {
                     allow_privilege_escalation = false
                     privileged                 = false
                     read_only_root_filesystem  = false
         
                     capabilities {
                       add  = []
                       drop = ["NET_RAW"]
                     }
                   }
         
                   liveness_probe {
                     http_get {
                       path = "/"
                       port = "hello-app-svc"
         
                       http_header {
                         name  = "X-Custom-Header"
                         value = "Awesome"
                       }
                     }
         
                     initial_delay_seconds = 3
                     period_seconds        = 3
                   }
                 }
         
                 security_context {
                   run_as_non_root = true
         
                   seccomp_profile {
                     type = "RuntimeDefault"
                   }
                 }
         
                 # Toleration is currently required to prevent perpetual diff:
                 # https://github.com/hashicorp/terraform-provider-kubernetes/pull/2380
                 toleration {
                   effect   = "NoSchedule"
                   key      = "kubernetes.io/arch"
                   operator = "Equal"
                   value    = "amd64"
                 }
               }
             }
           }
         }
         
         resource "kubernetes_service_v1" "default" {
           metadata {
             name = "example-hello-app-loadbalancer"
             annotations = {
               "networking.gke.io/load-balancer-type" = "Internal" # Remove to create an external loadbalancer
             }
           }
         
           spec {
             selector = {
               app = kubernetes_deployment_v1.default.spec[0].selector[0].match_labels.app
             }
         
             ip_family_policy = "RequireDualStack"
         
             port {
               port        = 80
               target_port = kubernetes_deployment_v1.default.spec[0].template[0].spec[0].container[0].port[0].name
             }
         
             type = "LoadBalancer"
           }
         
           depends_on = [time_sleep.wait_service_cleanup]
         }
         
         # Provide time for Service cleanup
         resource "time_sleep" "wait_service_cleanup" {
           depends_on = [google_container_cluster.default]
         
           destroy_duration = "180s"
         }

This file describes the following resources:

     * A [Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) with a sample container image.
     * A [Service of type LoadBalancer](https://kubernetes.io/docs/concepts/services-networking/service/#loadbalancer). The Service exposes the Deployment on port 80.



### (Optional) Expose the application to the internet

The Terraform files for the example describe an application **with an internal IP address** , which can only be accessed from the same Virtual Private Cloud (VPC) as the sample app. If you want to access the running demo app's web interface from the internet (for example, from your laptop), modify the Terraform files to create a public IP address instead before you create the cluster. You can do this using a text editor directly in Cloud Shell or by using the Cloud Shell Editor.

To expose the demo application to the internet:

  1. In `cluster.tf`, change `ipv6_access_type` from `INTERNAL` to `EXTERNAL`.
         
         ipv6_access_type = "EXTERNAL"
         

  2. In `app.tf`, configure an external load balancer by removing the `networking.gke.io/load-balancer-type` annotation.
         
         annotations = {
            "networking.gke.io/load-balancer-type" = "Internal" # Remove this line
          }
         




## Create a cluster and deploy an application

  1. In Cloud Shell, run this command to verify that Terraform is available:
         
         terraform
         

The output should be similar to the following:
         
         Usage: terraform [global options] <subcommand> [args]
         
         The available commands for execution are listed below.
         The primary workflow commands are given first, followed by
         less common or more advanced commands.
         
         Main commands:
           init          Prepare your working directory for other commands
           validate      Check whether the configuration is valid
           plan          Show changes required by the current configuration
           apply         Create or update infrastructure
           destroy       Destroy previously-created infrastructure
         

  2. Initialize Terraform:
         
         terraform init
         

  3. Plan the Terraform configuration:
         
         terraform plan
         

  4. Apply the Terraform configuration
         
         terraform apply
         

When prompted, enter `yes` to confirm actions. This command might take several minutes to complete. The output is similar to the following:
         
         Apply complete! Resources: 6 added, 0 changed, 0 destroyed.
         




## Verify the cluster is working

Do the following to confirm your cluster is running correctly:

  1. Go to the **Workloads** page in the Google Cloud console:

[Go to Workloads](https://console.cloud.google.com/kubernetes/workload)

  2. Click the `example-hello-app-deployment` workload. The Pod details page displays. This page shows information about the Pod, such as annotations, containers running on the Pod, Services exposing the Pod, and metrics including CPU, Memory, and Disk usage.

  3. Go to the **Services & Ingress** page in the Google Cloud console:

[Go to Services & Ingress](https://console.cloud.google.com/kubernetes/discovery)

  4. Click the `example-hello-app-loadbalancer` LoadBalancer Service. The Service details page displays. This page shows information about the Service, such as the Pods associated with the Service, and the Ports the Services uses.

  5. In the **External endpoints** section, click the **IPv4 link** or the **IPv6 link** to view your Service in the browser. The output is similar to the following:
         
         Hello, world!
         Version: 2.0.0
         Hostname: example-hello-app-deployment-5df979c4fb-kdwgr
         


**Success:** You've successfully created a cluster and deployed a workload to GKE using Terraform.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, delete the Google Cloud project with the resources. 

If you plan to take additional tutorials or to [explore your sample further](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/tour-cluster), wait until you're finished to perform this cleanup step.

  * In Cloud Shell, run the following command to delete the Terraform resources:
        
        terraform destroy --auto-approve
        




### Troubleshoot cleanup errors

If you see an error message similar to `The network resource 'projects/PROJECT_ID/global/networks/example-network' is already being used by 'projects/PROJECT_ID/global/firewalls/example-network-yqjlfql57iydmsuzd4ot6n5v'`, do the following:

  1. Delete the firewall rules:
         
         gcloud compute firewall-rules list --filter="NETWORK:example-network" --format="table[no-heading](name)" | xargs gcloud --quiet compute firewall-rules delete
         

  2. Re-run the Terraform command:
         
         terraform destroy --auto-approve
         




## What's next

  * [Explore your cluster and workload](https://docs.cloud.google.com/kubernetes-engine/docs/quickstarts/tour-cluster) in the Google Cloud console to learn about the some of the key workload settings and resources that you deployed.

  * Learn more about setting up and using Terraform with GKE in [Terraform support for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/resources/use-terraform-gke).

  * Try our more in-depth [Learning path: Scalable apps](https://docs.cloud.google.com/kubernetes-engine/docs/learn/scalable-apps).

  * Learn how to get started with real life cluster administration in our [Cluster administration overview](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-admin-overview).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
