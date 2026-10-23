---
url: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/configure-networking/
title: Configure networking for a basic production cluster \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:09.456216+00:00
---

# Configure networking for a basic production cluster  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/tutorials/configure-networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  Configure networking for a basic production cluster Stay organized with collections  Save and categorize content based on your preferences. 

Autopilot  Standard 

This tutorial is intended for cloud architects and operations administrators interested in deploying a web application to a Google Kubernetes Engine (GKE) cluster and exposing it with an HTTPS load balancer.

## Objectives

In this tutorial, you will learn how to:

  * Create a GKE cluster.
  * Create a global IP address and Cloud DNS zone with Terraform.
  * Configure HTTPS load balancing.
  * Deploy a sample web application.



## Costs

In this document, you use the following billable components of Google Cloud: 

  * [GKE](https://cloud.google.com/kubernetes-engine/pricing)
  * [Cloud Load Balancing](https://cloud.google.com/load-balancing/pricing)
  * [External IP address](https://docs.cloud.google.com/vpc/network-pricing#ipaddress)



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://docs.cloud.google.com/products/calculator). 

New Google Cloud users might be eligible for a [free trial](https://docs.cloud.google.com/free). 

When you finish the tasks that are described in this document, you can avoid continued billing by deleting the resources that you created. For more information, see Clean up.

## Before you begin

### Set up your project

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, click **Create project** to begin creating a new Google Cloud project.

**Roles required to create a project**

To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. Enable the Google Kubernetes Engine, Cloud DNS APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,dns.googleapis.com)

  5. In the Google Cloud console, on the project selector page, click **Create project** to begin creating a new Google Cloud project.

**Roles required to create a project**

To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  7. Enable the Google Kubernetes Engine, Cloud DNS APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com,dns.googleapis.com)



  * You must own a domain name. The domain name must be no longer than 63 characters. You can use [Google Domains](https://domains.google.com/) or another registrar. 



### Set up your environment

In this tutorial, you use [Cloud Shell](https://docs.cloud.google.com/shell) to manage resources hosted on Google Cloud. Cloud Shell is preinstalled with the software you need for this tutorial, including [Terraform](https://docs.cloud.google.com/docs/terraform/get-started-with-terraform), [`kubectl`](https://kubernetes.io/docs/reference/kubectl/) and the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

  1. Set environment variables:
         
         PROJECT_ID=$(gcloud config get-value project)
         gcloud config set project $PROJECT_ID
         gcloud config set compute/region us-central1
         

  2. Clone the code repository:
         
         git clone https://github.com/GoogleCloudPlatform/kubernetes-engine-samples.git
         

  3. Change to the working directory:
         
         cd kubernetes-engine-samples/autopilot/networking-tutorial
         




## Create a GKE cluster

The following Terraform file creates a GKE cluster:
    
    
    terraform {
      required_version = "~> 1.3"
    }
    
    provider "google" {}
    
    variable "region" {
      type        = string
      description = "Region where the cluster will be created."
      default     = "us-central1"
    }
    
    variable "cluster_name" {
      type        = string
      description = "Name of the cluster"
      default     = "networking-cluster"
    }
    
    resource "google_container_cluster" "default" {
      name             = var.cluster_name
      description      = "Cluster for sample web application"
      location         = var.region
      enable_autopilot = true
    
      ip_allocation_policy {}
    }
    
    output "region" {
      value       = var.region
      description = "Compute region"
    }
    
    output "cluster_name" {
      value       = google_container_cluster.default.name
      description = "Cluster name"
    }
    

The following Terraform file creates a global IP address and Cloud DNS zone:
    
    
    terraform {
      required_version = "~> 1.3"
    }
    
    variable "base_domain" {
      type        = string
      description = "Your base domain"
    }
    
    variable "name" {
      type        = string
      description = "Name of resources"
      default     = "networking-tutorial"
    }
    
    data "google_client_config" "current" {}
    
    resource "google_compute_global_address" "default" {
      name = var.name
    }
    
    resource "google_dns_managed_zone" "default" {
      name        = var.name
      dns_name    = "${var.name}.${var.base_domain}."
      description = "DNS Zone for web application"
    }
    
    resource "google_dns_record_set" "a" {
      name         = google_dns_managed_zone.default.dns_name
      type         = "A"
      ttl          = 300
      managed_zone = google_dns_managed_zone.default.name
    
      rrdatas = [google_compute_global_address.default.address]
    }
    
    resource "google_dns_record_set" "cname" {
      name         = join(".", compact(["www", google_dns_record_set.a.name]))
      type         = "CNAME"
      ttl          = 300
      managed_zone = google_dns_managed_zone.default.name
    
      rrdatas = [google_dns_record_set.a.name]
    }
    
    output "dns_zone_name_servers" {
      value       = google_dns_managed_zone.default.name_servers
      description = "Write these virtual name servers in your base domain."
    }
    
    output "domain" {
      value = trim(google_dns_record_set.a.name, ".")
    }
    

  1. Initialize Terraform:
         
         terraform init
         

  2. View the infrastructure changes:
         
         terraform plan
         

When prompted, enter your domain, such as `my-domain.net`.

  3. Apply the Terraform configuration:
         
         terraform apply --auto-approve
         

When prompted, enter your domain, such as `my-domain.net`.

The output is similar to the following:
         
         Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
         
         Outputs:
         
         cluster_name = "networking-cluster"
         region = "us-central1"
         




## Create an external Application Load Balancer

  1. The following manifest describes a ManagedCertificate, FrontendConfig, Deployment, Service, and Ingress:
         
         ---
         apiVersion: networking.gke.io/v1
         kind: ManagedCertificate
         metadata:
           name: networking-managed-cert
         spec:
           domains:
             - DOMAIN_NAME
             - www.DOMAIN_NAME
         ---
         apiVersion: networking.gke.io/v1beta1
         kind: FrontendConfig
         metadata:
           name: networking-fc
         spec:
           redirectToHttps:
             enabled: true
             responseCodeName: MOVED_PERMANENTLY_DEFAULT
         ---
         apiVersion: apps/v1
         kind: Deployment
         metadata:
           name: frontend
         spec:
           selector:
             matchLabels:
               app: frontend
           replicas: 2
           template:
             metadata:
               labels:
                 app: frontend
             spec:
               containers:
               - name: echo-amd64
                 image: us-docker.pkg.dev/google-samples/containers/gke/hello-app-cdn:1.0
         ---
         apiVersion: v1
         kind: Service
         metadata:
           name: frontend
         spec:
           type: LoadBalancer
           selector:
             app: frontend
           ports:
           - name: http
             port: 80
             targetPort: 8080
         ---
         apiVersion: networking.k8s.io/v1
         kind: Ingress
         metadata:
           name: frontend
           annotations:
             networking.gke.io/managed-certificates: networking-managed-cert
             networking.gke.io/v1beta1.FrontendConfig: networking-fc
             kubernetes.io/ingress.global-static-ip-name: networking-tutorial
             kubernetes.io/ingress.class: gce
           labels:
             app: frontend
         spec:
           defaultBackend:
             service:
               name: frontend
               port:
                 number: 80

Replace `DOMAIN_NAME` with your domain name, such as `my-domain.net`.

This manifest has the following properties:

     * `networking.gke.io/managed-certificates`: the name of the ManagedCertificate. This resource provisions a Google-managed SSL certificate (Classic).
     * `networking.gke.io/v1beta1.FrontendConfig`: the name of the FrontendConfig resource.
     * `kubernetes.io/ingress.global-static-ip-name`: the name of the IP address.
     * `kubernetes.io/ingress.class`: instructs the GKE Ingress controller to create an external Application Load Balancer.
  2. Apply the manifest to your cluster:
         
         kubectl apply -f kubernetes-manifests.yaml
         

  3. Verify the Ingress was created:
         
         kubectl describe ingress frontend
         

The output is similar to the following:
         
         ...
           Events:
             Type    Reason  Age   From                     Message
             ----    ------  ----  ----                     -------
             Normal  ADD     2m    loadbalancer-controller  default/frontend
             Normal  CREATE  1m    loadbalancer-controller  ip: 203.0.113.2
         ...
         

It might take several minutes for the Ingress to provision.




## Test application

  1. Check the status of the SSL certificate:
         
         kubectl get managedcertificates.networking.gke.io networking-managed-cert
         

The SSL certificate might take up to 30 minutes to provision. The following output indicates the SSL certificate is ready:
         
         NAME                      AGE   STATUS
         networking-managed-cert   28m   Active
         

  2. Run a `curl` command:
         
         curl -Lv https://DOMAIN_NAME
         

The output is similar to the following:
         
         *   Trying 34.160.115.33:443...
         * Connected to DOMAIN_NAME (34.160.115.33) port 443 (#0)
         ...
         * TLSv1.3 (IN), TLS handshake, Certificate (11):
         ...
         * Server certificate:
         *  subject: CN=DOMAIN_NAME
         ...
         > Host: DOMAIN_NAME
         




## Clean up

To avoid incurring charges to your Google Cloud account for the resources used in this tutorial, either delete the project that contains the resources, or keep the project and delete the individual resources. 

### Delete the project

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

Delete a Google Cloud project:
    
    gcloud projects delete PROJECT_ID




### Delete individual resources

  1. Delete the kubernetes resources:
         
         kubectl delete -f kubernetes-manifests.yaml
         

  2. Delete the Terraform resources:
         
         terraform destroy --auto-approve
         

When prompted, enter your domain, such as `my-domain.net`.




## What's next

  * Learn more about [GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
