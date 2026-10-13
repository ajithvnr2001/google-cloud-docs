---
url: https://docs.cloud.google.com/run/docs/multiple-regions/
title: Serve traffic from multiple regions \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:56:45.418795+00:00
---

# Serve traffic from multiple regions  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/multiple-regions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Serve traffic from multiple regions Stay organized with collections  Save and categorize content based on your preferences. 

You return faster responses to your users around the world by deploying services in multiple regions and routing your users to the nearest region. Deploying across multiple regions delivers low latency and higher availability in case of regional outages.

Because Cloud Run services deploy into individual regions, you must deploy your service to multiple regions and then configure global load balancing for the service.

You can automate cross-regional failover using [Cloud Run service health](https://docs.cloud.google.com/run/docs/multiple-regions#service-health).

### Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  6. [Set up your Cloud Run development environment](https://docs.cloud.google.com/run/docs/setup) in your Google Cloud project.
  7. [Install and initialize the gcloud CLI](https://docs.cloud.google.com/sdk/docs/install).
  8. Ensure your account has the following IAM roles: 
     * [Cloud Run Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin) (`roles/run.admin`)
     * [Project IAM Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
     * [Service Usage Consumer](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`)

#### Grant the roles

#### Console

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)
     2. Select the project. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the Google Account email address used to deploy the Cloud Run service.

     5. In the **Select a role** list, select a role. 
     6. To grant additional roles, click add **Add another role** and select each additional role. 
     7. Click **Save**. 

#### gcloud

To grant the required IAM roles to your account on your project:
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
                --member=PRINCIPAL \
                --role=ROLE
            

Replace:

     * PROJECT_NUMBER with your Google Cloud project number.
     * PROJECT_ID with your Google Cloud project ID.
     * PRINCIPAL with the account you are adding the binding for. This is typically the Google Account email address that is used to deploy the Cloud Run service.
     * ROLE with the role you are adding to the deployer account.

  9. Review the [Cloud Run pricing](https://docs.cloud.google.com/run/pricing) page. To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).
  10. Enable the Artifact Registry, Cloud Build, Cloud Run Admin API, Compute Engine, and Network Services API APIs by running the following command:
    
    gcloud services enable artifactregistry.googleapis.com \
        cloudbuild.googleapis.com \
        run.googleapis.com \
        compute.googleapis.com \
        networkservices.googleapis.com
      




## Deploy the service to multiple regions

Scaling parameters that you configure apply across multiple regions. In a multi-region deployment, for example, the minimum instances value applies for each of the multiple regions.

You deploy the same service to multiple regions using one of the following methods:

  * Repeat the steps to [deploy to a single region](https://docs.cloud.google.com/run/docs/deploying).
  * Deploy a multi-region service.



### Deploy a multi-region service

This section shows you how to deploy and configure a multi-region service from a single gcloud CLI command or using a YAML or Terraform file.

###  gcloud 

  * To create and deploy a multi-region service, run the `gcloud run deploy` command using the `--regions` flag:
        
        gcloud run deploy SERVICE_NAME \
          --image=IMAGE_URL \
          --regions=REGIONS

Replace the following:

    * `SERVICE_NAME`: The name of the multi-region service that you want to deploy.
    * `IMAGE_URL`: A reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`.
    * `REGIONS`: The list of multiple regions that you want to deploy to. For example, `europe-west1,asia-east1`.



### YAML

  1. Create the [YAML file](https://docs.cloud.google.com/run/docs/reference/yaml/v1) for your service, using the `run.googleapis.com/regions` attribute to set the multiple regions that you want to deploy your service to:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE_NAME
           annotations:
             run.googleapis.com/regions: REGIONS
         spec:
           template:
             spec:
               containers:
               - image: IMAGE_URL

Replace the following:

     * `SERVICE_NAME`: The name of the multi-region service that you want to deploy to.
     * `REGIONS`: The list of multiple regions that you want to update. For example, `europe-west1,asia-east1`.
     * `IMAGE_URL`: A reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`.
  2. Create the service using the following command:
         
         gcloud run multi-region-services replace service.yaml




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration.
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "cloudrun-service-multi-region"
      location = "global"
    
      multi_region_settings {
        regions = [
          "REGION_1",
          "REGION_2",
        ]
      }
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
      }
    }
    

Replace "REGION_1" and "REGION_2" with each of the needed Google Cloud regions. For example, `europe-west1` and `us-central1`.

### Update a multi-region service

**Note:** You cannot modify individual regional services after deployment. They are read-only resources.

This section shows you how to add or remove regions from a multi-region service from a single gcloud CLI command or a YAML file.

###  gcloud 

To add or remove regions from a multi-region service, run the `gcloud run multi-region-services update` command.

  * To add the multi-region service to an additional region or regions, use the `--add-regions` flag:
        
        gcloud run multi-region-services update SERVICE_NAME \
          --add-regions=REGIONS

  * To remove the multi-region service from a region or regions, use the `--remove-regions` flag:
        
        gcloud run multi-region-services update SERVICE_NAME \
          --remove-regions=REGIONS

Replace the following:

    * `SERVICE_NAME`: The name of the multi-region service that you want to update.
    * `REGIONS`: The region or regions that you want to add your service to or remove your service from. For example, `us-central1,asia-east1`.



### YAML

  1. To update an existing multi-region service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run multi-region-services describe SERVICE_NAME --format export > service.yaml

  2. Update the `run.googleapis.com/regions` attribute to add or remove the list of regions that you want the service to deploy to:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE_NAME
           annotations:
             run.googleapis.com/regions: REGIONS

Replace the following:

     * `SERVICE_NAME`: The name of the multi-region service that you want to deploy to.
     * `REGIONS`: The new list of multiple regions that you want the service revision to deploy to.
  3. Update the service using the following command:
         
         gcloud run multi-region-services replace service.yaml




### Delete a multi-region service

**Note:** You cannot modify individual regional services after deployment. They are read-only resources.

  * To delete a multi-region service, run the `gcloud run multi-region-services delete` command:
        
        gcloud run multi-region-services delete SERVICE_NAME

Replace `SERVICE_NAME` with the name of the multi-region service that you want to delete.




## Configure a global external Application Load Balancer

This section shows you how to configure a [global external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) with a domain secured with a managed TLS certificate pointing to a global anycast IP address, which routes users to the nearest Google data center that deploys your service.

The architecture described in the following sections does not automatically route requests to a different region when a regional Cloud Run service becomes unresponsive or returns errors.

To increase the availability of your multi-regional service:

  * Automate cross-region failover with Cloud Run service health
  * [Configure outlier detection](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-global-traffic-mgmt#configure_outlier_detection) to identify unhealthy Cloud Run services based on their HTTP error rate and diverge some requests to another region.



### Configure regional network endpoint groups

For each region you deployed to in the previous step, you must create [serverless network endpoint groups (NEGs)](https://docs.cloud.google.com/load-balancing/docs/negs/setting-up-serverless-negs) using the following instructions:

### gcloud CLI

  1. Create a network endpoint group for the Cloud Run service in `REGION`:
         
         gcloud compute network-endpoint-groups create NEG_NAME \
           --region=REGION \
           --network-endpoint-type=serverless \
           --cloud-run-service=SERVICE_NAME

Replace the following:

     * NEG_NAME with the name of the network endpoint group resource, for example, `myservice-neg-uscentral1`. 
     * REGION with the region your service is deployed in. 
     * SERVICE_NAME with the name of your service. 
  2. Repeat the preceding step for each region




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

  1. Configure a network endpoint group with name `myservice-neg` for the Cloud Run service for each region specified in `run_regions` variable: 
         
         resource "google_compute_region_network_endpoint_group" "lb_default" {
           provider              = google-beta
           count                 = length(local.run_regions)
           name                  = "myservice-neg"
           network_endpoint_type = "SERVERLESS"
           region                = local.run_regions[count.index]
           cloud_run {
             service = google_cloud_run_v2_service.run_default[count.index].name
           }
         }




### Create a global external Application Load Balancer

Creating a global external Application Load Balancer involves creating [various networking resources](https://docs.cloud.google.com/load-balancing/docs/https/ext-https-lb-simple) and connecting them together: 

### gcloud

  1. Reserve a static IP address so you don't have to update your DNS records when you recreate your load balancer. 
         
         gcloud compute addresses create --global SERVICE_IP

In the command above, replace SERVICE_IP with a name for the IP address resource (e.g. `myservice-ip`). 

This IP address is a global anycast IPv4 address that routes to the Google datacenter or point of presence closest to your visitors. 

  2. Create a backend service. 
         
         gcloud compute backend-services create \
           --global BACKEND_NAME \
           --load-balancing-scheme=EXTERNAL_MANAGED

Replace BACKEND_NAME with a name you want to give to the backend service. For example, `myservice-backend`. 

  3. Add the network endpoint group to the backend service:
         
         gcloud compute backend-services add-backend --global BACKEND_NAME   
           --network-endpoint-group-region=REGION   
           --network-endpoint-group=NEG_NAME

Specify the NEG_NAME you created in the previous step for the region.

  4. Create a URL map. 
         
         gcloud compute url-maps create URLMAP_NAME --default-service=BACKEND_NAME

Replace URLMAP_NAME with a name you want to give to the URL map (e.g. `myservice-urlmap`). 

  5. Create a managed TLS certificate for your domain to serve HTTPS traffic. (Replace example.com with your domain name.) 
         
         gcloud compute ssl-certificates create CERT_NAME \
           --domains=example.com

Replace CERT_NAME with the name you want the managed SSL certificate to have (e.g. `myservice-cert`). 

  6. Create a target HTTPS proxy. 
         
         gcloud compute target-https-proxies create HTTPS_PROXY_NAME \
           --ssl-certificates=CERT_NAME \
           --url-map=URLMAP_NAME

Replace HTTPS_PROXY_NAME with the name you want to give to the target HTTPS proxy (e.g. `myservice-https`). 

  7. Create a forwarding rule connecting the networking resources you created to the IP address. 
         
         gcloud compute forwarding-rules create --global FORWARDING_RULE_NAME \
           --target-https-proxy=HTTPS_PROXY_NAME \
           --address=SERVICE_IP \
           --ports=443 \
           --load-balancing-scheme=EXTERNAL_MANAGED 

Replace FORWARDING_RULE_NAME with the name of the forwarding rule resource you want to create. For example, `myservice-lb`. 




### Terraform

Alternatively to the steps described in this section, you can use the [Global HTTP Load Balancer Terraform Module](https://github.com/terraform-google-modules/terraform-google-lb-http/blob/master/modules/serverless_negs/README.md).

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

  1. Configure the IP address:
         
         resource "google_compute_global_address" "lb_default" {
           provider = google-beta
           name     = "myservice-service-ip"
         
           # Use an explicit depends_on clause to wait until API is enabled
           depends_on = [
             google_project_service.compute_api
           ]
         }
         output "load_balancer_ip_addr" {
           value = google_compute_global_address.lb_default.address
         }

Configures your IP address resource name to be `myservice-service-ip`. You can change this to your own value. This IP address is a global anycast IPv4 address that routes to the Google data center or point of presence closest to your visitors. 

  2. Create and configure the backend service:
         
         resource "google_compute_backend_service" "lb_default" {
           provider              = google-beta
           name                  = "myservice-backend"
           load_balancing_scheme = "EXTERNAL_MANAGED"
         
           backend {
             group = google_compute_region_network_endpoint_group.lb_default[0].id
           }
         
           backend {
             group = google_compute_region_network_endpoint_group.lb_default[1].id
           }
         
           # Use an explicit depends_on clause to wait until API is enabled
           depends_on = [
             google_project_service.compute_api,
           ]
         }

This resource configures the backend service to be named `myservice-backend`. You can change this to your own value. 

  3. Configure the URL map:
         
         resource "google_compute_url_map" "lb_default" {
           provider        = google-beta
           name            = "myservice-lb-urlmap"
           default_service = google_compute_backend_service.lb_default.id
         
           path_matcher {
             name            = "allpaths"
             default_service = google_compute_backend_service.lb_default.id
             route_rules {
               priority = 1
               url_redirect {
                 https_redirect         = true
                 redirect_response_code = "MOVED_PERMANENTLY_DEFAULT"
               }
             }
           }
         }

Connects the backend service resource (`myservice-backend`) to the new URL map resource (`myservice-lb-urlmap`). You can change these to your own values. 

  4. Create a managed TLS certificate for your domain to serve HTTPS traffic. Replace `example.com` with your domain name in the `google_compute_managed_ssl_certificate` resource:
         
         resource "google_compute_managed_ssl_certificate" "lb_default" {
           provider = google-beta
           name     = "myservice-ssl-cert"
         
           managed {
             domains = ["example.com"]
           }
         }

  5. Configure the HTTPS proxy:
         
         resource "google_compute_target_https_proxy" "lb_default" {
           provider = google-beta
           name     = "myservice-https-proxy"
           url_map  = google_compute_url_map.lb_default.id
           ssl_certificates = [
             google_compute_managed_ssl_certificate.lb_default.name
           ]
           depends_on = [
             google_compute_managed_ssl_certificate.lb_default
           ]
         }

Creates `google_compute_target_https_proxy` resource with target name `myservice-https-proxy` and connects previously created TLS certificate (`myservice-ssl-cert`) and URL mapping resources (`myservice-lb-urlmap`). You can change these to your own values. 

  6. Configure the forwarding rule:
         
         resource "google_compute_global_forwarding_rule" "lb_default" {
           provider              = google-beta
           name                  = "myservice-lb-fr"
           load_balancing_scheme = "EXTERNAL_MANAGED"
           target                = google_compute_target_https_proxy.lb_default.id
           ip_address            = google_compute_global_address.lb_default.id
           port_range            = "443"
           depends_on            = [google_compute_target_https_proxy.lb_default]
         }

Creates `google_compute_global_forwarding_rule` resource with target name `myservice-https-proxy` and connects previously created HTTPS proxy target (`myservice-https-proxy`) and IP address resource (`myservice-service-ip`). You can change these to your own values. 

  7. Apply this config:

To apply your Terraform configuration in a Google Cloud project, complete the steps in the following sections.

## Prepare Cloud Shell

     1. Launch [Cloud Shell](https://shell.cloud.google.com/).
     2. Set the default Google Cloud project where you want to apply your Terraform configurations. 

You only need to run this command once per project, and you can run it in any directory.
            
            export GOOGLE_CLOUD_PROJECT=PROJECT_ID

Environment variables are overridden if you set explicit values in the Terraform configuration file.

## Prepare the directory

Each Terraform configuration file must have its own directory (also called a _root module_).

     1. In [Cloud Shell](https://shell.cloud.google.com/), create a directory and a new file within that directory. The filename must have the `.tf` extension—for example `main.tf`. In this tutorial, the file is referred to as `main.tf`. 
            
            mkdir DIRECTORY && cd DIRECTORY && touch main.tf

     2. If you are following a tutorial, you can copy the sample code in each section or step.

Copy the sample code into the newly created `main.tf`.

Optionally, copy the code from GitHub. This is recommended when the Terraform snippet is part of an end-to-end solution. 

     3. Review and modify the sample parameters to apply to your environment.
     4. Save your changes.
     5. Initialize Terraform. You only need to do this once per directory. 
            
            terraform init

Optionally, to use the latest Google provider version, include the `-upgrade` option: 
            
            terraform init -upgrade

## Apply the changes

     1. Review the configuration and verify that the resources that Terraform is going to create or update match your expectations: 
            
            terraform plan

Make corrections to the configuration as necessary.

     2. Apply the Terraform configuration by running the following command and entering `yes` at the prompt: 
            
            terraform apply

Wait until Terraform displays the "Apply complete!" message.

     3. [Open your Google Cloud project](https://console.cloud.google.com/) to view the results. In the Google Cloud console, navigate to your resources in the UI to make sure that Terraform has created or updated them. 
**Note:** Terraform samples typically assume that the required APIs are enabled in your Google Cloud project. 



### Configure regional network endpoint groups

For each region you deployed to in the previous step, you must create [serverless network endpoint groups (NEGs)](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) and add them to the backend service using the following instructions:

### gcloud CLI

  1. Create a network endpoint group for the Cloud Run service in `REGION`:
         
         gcloud compute network-endpoint-groups create NEG_NAME \
           --region=REGION \
           --network-endpoint-type=serverless \
           --cloud-run-service=SERVICE_NAME

Replace the following:

     * NEG_NAME with the name of the network endpoint group resource. (for example, `myservice-neg-uscentral1`) 
     * REGION with the region your service is deployed in. 
     * SERVICE_NAME with the name of your service. 
  2. Add the network endpoint group to the backend service:
         
         gcloud compute backend-services add-backend --global BACKEND_NAME \
           --network-endpoint-group-region=REGION \
           --network-endpoint-group=NEG_NAME

Specify the NEG_NAME you created in the previous step for the region.

  3. Repeat the preceding steps for each region.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

  1. Configure a network endpoint group with name `myservice-neg` for the Cloud Run service for each region specified in `run_regions` variable: 
         
         resource "google_compute_region_network_endpoint_group" "lb_default" {
           provider              = google-beta
           count                 = length(local.run_regions)
           name                  = "myservice-neg"
           network_endpoint_type = "SERVERLESS"
           region                = local.run_regions[count.index]
           cloud_run {
             service = google_cloud_run_v2_service.run_default[count.index].name
           }
         }

  2. Configure a backend service to attach the network endpoint group (`myservice-neg`):
         
         resource "google_compute_backend_service" "lb_default" {
           provider              = google-beta
           name                  = "myservice-backend"
           load_balancing_scheme = "EXTERNAL_MANAGED"
         
           backend {
             group = google_compute_region_network_endpoint_group.lb_default[0].id
           }
         
           backend {
             group = google_compute_region_network_endpoint_group.lb_default[1].id
           }
         
           # Use an explicit depends_on clause to wait until API is enabled
           depends_on = [
             google_project_service.compute_api,
           ]
         }




### Configure DNS records on your domain

To point your domain name to the forwarding rule you created, update its DNS records with the IP address that you created.

  1. Find the reserved IP address of the load balancer by running the following command:
         
         gcloud compute addresses describe SERVICE_IP \
           --global \
           --format='value(address)'

Replace SERVICE_IP with the name of the IP address you created previously. This command prints the IP address to the output.

  2. Update your domain's DNS records by adding an `A` record with this IP address.




#### Configure custom audience if using authenticated services

Authenticated services are [protected by IAM](https://docs.cloud.google.com/run/docs/securing/managing-access). Such Cloud Run services require client authentication that declares the intended recipient of a request at credential generation time (the _audience_).

Audience is usually the full URL of the target service, which by default for Cloud Run services is a generated URL ending in `run.app`. However, in a multi-region deployment, a client cannot know in advance which regional service a request will be routed to. So, for a multi-region deployment, configure your service to use [custom audiences](https://docs.cloud.google.com/run/docs/configuring/custom-audiences).

### Wait for load balancer to provision

After configuring the domain with the load balancer IP address, wait for DNS records to propagate. Similarly, wait for the managed TLS certificate to be issued for your domain and to be ready to start serving HTTPS traffic globally.

It might take up to 30 minutes for your load balancer to start serving traffic.

After it is ready, visit your website's URL with `https://` prefix to try it out.

### Verify status

  1. To check the status of your DNS record propagation, use the `dig` command-line utility:
         
         dig A +short example.com

The output shows the IP address that you configured in your DNS records.

  2. Check the status of your managed certificate issuance by running the following command:
         
         gcloud compute ssl-certificates describe CERT_NAME

Replace CERT_NAME with the name you previously chose for the SSL certificate resource.

The output shows a line containing `status: ACTIVE`.




### Set up HTTP-to-HTTPS redirect

**Note:** Creating additional forwarding rules are subject to charges. See [load balancer pricing](https://docs.cloud.google.com/vpc/network-pricing#lb-pricing).

By default, a forwarding rule only handles a single protocol and therefore requests to your `http://` endpoints respond with "404 Not Found". If you need requests to your `http://` URLs to redirect to the `https://` protocol, create an additional URL map and a forwarding rule using the following instructions:

### gcloud CLI

  1. Create a URL map with a redirect rule.
         
         gcloud compute url-maps import HTTP_URLMAP_NAME \
           --global \
           --source /dev/stdin <<EOF
                 name: HTTP_URLMAP_NAME
                 defaultUrlRedirect:
                   redirectResponseCode: MOVED_PERMANENTLY_DEFAULT
                   httpsRedirect: True
                 EOF

Replace the HTTP_URLMAP_NAME with the name of the URL map resource you will create (for example, `myservice-httpredirect`).

  2. Create a target HTTP proxy with the URL map.
         
         gcloud compute target-http-proxies create HTTP_PROXY_NAME \
           --url-map=HTTP_URLMAP_NAME

Replace HTTP_PROXY_NAME with the name of the target HTTP proxy you will create (for example, `myservice-http`).

  3. Create a forwarding rule on port `80` with the same reserved IP address.
         
         gcloud compute forwarding-rules create --global HTTP_FORWARDING_RULE_NAME \
           --target-http-proxy=HTTP_PROXY_NAME \
           --address=SERVICE_IP \
           --ports=80
                 

Replace HTTP_FORWARDING_RULE_NAME with the name of the new forwarding rule you will create (for example, `myservice-httplb`).




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

  1. Create a URL map resource with a redirect rule:
         
         resource "google_compute_url_map" "https_default" {
           provider = google-beta
           name     = "myservice-https-urlmap"
         
           default_url_redirect {
             redirect_response_code = "MOVED_PERMANENTLY_DEFAULT"
             https_redirect         = true
             strip_query            = false
           }
         }

  2. Create a target HTTP proxy with the newly created URL map resource (`myservice-https-urlmap`):
         
         resource "google_compute_target_http_proxy" "https_default" {
           provider = google-beta
           name     = "myservice-http-proxy"
           url_map  = google_compute_url_map.https_default.id
         
           depends_on = [
             google_compute_url_map.https_default
           ]
         }

  3. Create a forwarding rule on port `80` with the same reserved IP address resource (`myservice-http-proxy`):
         
         resource "google_compute_global_forwarding_rule" "https_default" {
           provider   = google-beta
           name       = "myservice-https-fr"
           target     = google_compute_target_http_proxy.https_default.id
           ip_address = google_compute_global_address.lb_default.id
           port_range = "80"
           depends_on = [google_compute_target_http_proxy.https_default]
         }




**Note:** Similar to the HTTPS forwarding rule to be created, creating the additional forwarding rule might take some time. After it is ready, your application is accessible over `http://` and redirects to `https://` URL with a "301 Moved Permanently" status code.

For additional configuration options, see [Set up a global external Application Load Balancer with Cloud Run](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-serverless#additional_configuration_options).

## Automate cross-regional failover with Cloud Run service health

To set up a multi-region, high availability Cloud Run service with automated failover and failback capabilities for internal or external traffic, see the [Service health guide](https://docs.cloud.google.com/run/docs/configuring/configure-service-health).

## Use authenticated Pub/Sub push subscriptions with multi-region deployment

A Pub/Sub service by default delivers messages to push endpoints in the same Google Cloud region where the Pub/Sub service stores the messages. For a workaround to this behavior, refer to [Using an authenticated Pub/Sub push subscription with a multi-region Cloud Run deployment](https://docs.cloud.google.com/load-balancing/docs/https/setting-up-https-serverless#pubsub).

## Configure a manual failover

To manually configure traffic to fail over to a healthy region, modify the global external Application Load Balancer URL map.

  1. To update the global external Application Load Balancer URL map, remove the NEG from the backend service, using the `--global` flag:
         
         gcloud compute backend-services remove-backend BACKEND_NAME \
         --network-endpoint-group=NEG_NAME \
         --network-endpoint-group-region=REGION \
         --global
         

Replace the following:

     * `BACKEND_NAME`: The name of the backend service.
     * `NEG_NAME`: The name of the network endpoint group resource, for example, `myservice-neg-uscentral1`.
     * `REGION`: The region where the NEG was created and where you want to remove your service from. For example, `us-central1,asia-east1`.
  2. To confirm that a healthy region is now serving traffic, navigate to https://`<domain-name>`.




## What's next

  * Learn how to [configure health checks for Cloud Run services](https://docs.cloud.google.com/run/docs/configuring/healthchecks), including [readiness probes](https://docs.cloud.google.com/run/docs/configuring/healthchecks#readiness-probes).



  * Check out a Cloud Run readiness probe and service health [code sample written in Go](https://github.com/GoogleCloudPlatform/golang-samples/tree/main/run/service-health).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
