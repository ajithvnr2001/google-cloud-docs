---
url: https://docs.cloud.google.com/run/docs/configuring/static-outbound-ip/
title: Static outbound IP address \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:17.234058+00:00
---

# Static outbound IP address  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/static-outbound-ip/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Static outbound IP address Stay organized with collections  Save and categorize content based on your preferences. 

By default, a Cloud Run service connects to external endpoints on the internet using a dynamic IP address pool. If the Cloud Run service connects to an external endpoint that requires a static IP address such as a database or API using an IP address-based firewall, you must configure your Cloud Run service to route requests using a static IP address.

This page describes how to enable a Cloud Run service to send requests using a static IP address.

We recommend configuring Cloud Run to send traffic to a VPC network using [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc). However, you have the option to [Create a connector](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#create-connector). 

## Task overview

To enable a Cloud Run service to route requests using a static IP address, configure the Cloud Run service's [VPC egress](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc) to route all outbound traffic through a [VPC network](https://docs.cloud.google.com/vpc/docs) that has a [Cloud NAT](https://docs.cloud.google.com/nat/docs) gateway configured with the static IP address.

In this tutorial, you configure Cloud NAT in manual mode and assign a single static IP address to it. If your Cloud Run workloads scale up to large numbers, you might need to assign multiple static IP addresses to Cloud NAT. Learn more about how Cloud NAT gateways use [IP addresses and ports](https://docs.cloud.google.com/nat/docs/ports-and-addresses).

Routing your traffic through [Cloud NAT](https://docs.cloud.google.com/nat/docs) does not cause an additional hop in your networking stack since the Cloud NAT gateway and the Cloud Router provide only a control plane and the packets don't pass through the NAT gateway or the Cloud Router.

## Configure network address translation (NAT)

If you use Direct VPC egress or a Serverless VPC Access connector, requests from your Cloud Run service arrive at your VPC network. If you want to route outbound requests to external endpoints using a static IP, configure a [Cloud NAT](https://docs.cloud.google.com/nat/docs) gateway.

###  gcloud 

  1. Create a new Cloud Router to program a Cloud NAT gateway:
         
         gcloud compute routers create ROUTER_NAME \
           --network=NETWORK_NAME \
           --region=REGION

Replace the following:

     * `ROUTER_NAME`: a name for the Cloud Router resource that you want to create.
     * `NETWORK_NAME`: the name of the VPC network that you found earlier.
     * `REGION`: the region that you want to create a Cloud NAT gateway in.
  2. Reserve a static IP address. A reserved IP address resource retains the underlying IP address when the resource it is associated with is deleted and re-created:
         
         gcloud compute addresses create ORIGIN_IP_NAME --region=REGION

Replace the following:

     * `ORIGIN_IP_NAME`: the name that you want to assign to the IP address resource.
     * `REGION`: the [region](https://docs.cloud.google.com/run/docs/locations) that will run the Cloud NAT router. Use the same region as your Cloud Run service to minimize latency and network costs.
  3. Create a Cloud NAT gateway configuration on this router to route the traffic originating from the VPC network using the static IP address that you created:
         
         gcloud compute routers nats create NAT_NAME \
           --router=ROUTER_NAME \
           --region=REGION \
           --nat-custom-subnet-ip-ranges=SUBNET_NAME \
           --nat-external-ip-pool=ORIGIN_IP_NAME

Replace the following:

     * `NAT_NAME`: a name for the Cloud NAT gateway resource that you want to create.
     * `ROUTER_NAME`: the name of your Cloud Router.
     * `REGION`: the region that you want to create a Cloud NAT gateway in.
     * `SUBNET_NAME`: the name of your subnet.
     * `ORIGIN_IP_NAME`: the name of the reserved IP address resource that you created in the previous step.



### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

  1. Create a new Cloud Router to program a Cloud NAT gateway:
         
         resource "google_compute_router" "default" {
           name    = "cr-static-ip-router"
           network = google_compute_network.default.name
           region  = google_compute_subnetwork.default.region
         }

Replace `cr-static-ip-router` with your subnet name.

  2. Reserve a static IP address. A reserved IP address resource retains the underlying IP address when the resource it is associated with is deleted and recreated:
         
         resource "google_compute_address" "default" {
           name   = "cr-static-ip-addr"
           region = google_compute_subnetwork.default.region
         }

Replace `cr-static-ip-addr` with your subnet name.

  3. Create a Cloud NAT gateway configuration on this router to route the traffic originating from the VPC network using the static IP address that you created:
         
         resource "google_compute_router_nat" "default" {
           name   = "cr-static-nat"
           router = google_compute_router.default.name
           region = google_compute_subnetwork.default.region
         
           nat_ip_allocate_option = "MANUAL_ONLY"
           nat_ips                = [google_compute_address.default.self_link]
         
           source_subnetwork_ip_ranges_to_nat = "LIST_OF_SUBNETWORKS"
           subnetwork {
             name                    = google_compute_subnetwork.default.id
             source_ip_ranges_to_nat = ["ALL_IP_RANGES"]
           }
         }

Replace `cr-static-nat` with your Cloud NAT gateway name.




## Route Cloud Run traffic through the VPC network

After Cloud NAT is configured, deploy or update your Cloud Run service with [Direct VPC egress](https://docs.cloud.google.com/run/docs/configuring/vpc-direct-vpc) or the [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/configure-serverless-vpc-access) connector, and set the VPC egress to [route all traffic through the VPC network](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc):

###  gcloud 

**Direct VPC egress**

To deploy or update your Cloud Run service to use Direct VPC egress and route all egress traffic through it, run the following command:
    
    
    gcloud run deploy SERVICE_NAME \
    --image=IMAGE_URL \
    --network=NETWORK \
    --subnet=SUBNET \
    --region=REGION \
    --vpc-egress=all-traffic

Replace the following:

  * SERVICE_NAME: the name of the Cloud Run service that you want to deploy.
  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
  * NETWORK: the name of your VPC network.
  * SUBNET: the name of your subnet.
  * REGION: a region for your service.



**Serverless VPC Access connector**

To deploy or update your Cloud Run service to use a Serverless VPC Access connector and route all egress traffic through it, run the following command:
    
    
    gcloud run deploy SERVICE_NAME \
    --image=IMAGE_URL \
    --vpc-connector=CONNECTOR_NAME \
    --region=REGION \
    --vpc-egress=all-traffic

Replace the following:

  * SERVICE_NAME: the name of the Cloud Run service that you want to deploy.
  * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
  * CONNECTOR_NAME: the name of your Serverless VPC Access connector.
  * REGION: a region for your service.



### YAML

**Direct VPC egress**

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update as needed. 
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/network-interfaces: '[{"network":"NETWORK","subnetwork":"SUBNET"}]'
                 run.googleapis.com/vpc-access-egress: all-traffic
             spec:
               containers:
               - image: IMAGE_URL

Replace the following:

     * SERVICE: the name of the Cloud Run service.
     * NETWORK: the name of your VPC network.
     * SUBNET: the name of your subnet.
     * IMAGE_URL: the URL of your service container image.
  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




**Serverless VPC Access connector**

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update as needed. 
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             metadata:
               annotations:
                 run.googleapis.com/vpc-access-connector: CONNECTOR_NAME
             spec:
               containers:
               - image: IMAGE_URL

Replace the following:

     * SERVICE: the name of the Cloud Run service.
     * CONNECTOR_NAME: the name of your Serverless VPC Access network.
     * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

**Direct VPC egress**

This Cloud Run service uses Direct VPC egress and routes all egress traffic through it:
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "cloudrun-service"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
        vpc_access {
          network_interfaces {
            network    = "default"
            subnetwork = "default"
            tags       = ["tag1", "tag2", "tag3"]
          }
        }
      }
    }

**Serverless VPC Access connector**

This Cloud Run service uses a VPC connector and routes all egress traffic through it:
    
    
    resource "google_cloud_run_v2_service" "default" {
      name     = "cr-static-ip-service"
      location = google_compute_subnetwork.default.region
    
      deletion_protection = false # set to "true" in production
    
      template {
        containers {
          # Replace with the URL of your container
          #   gcr.io/<YOUR_GCP_PROJECT_ID>/<YOUR_CONTAINER_NAME>
          image = "us-docker.pkg.dev/cloudrun/container/hello"
        }
        scaling {
          max_instance_count = 5
        }
        vpc_access {
          connector = google_vpc_access_connector.default.id
          egress    = "ALL_TRAFFIC"
        }
      }
      ingress = "INGRESS_TRAFFIC_ALL"
    
    }

Replace `us-docker.pkg.dev/cloudrun/container/hello` with a reference to your container image.

## Verify the static external IP address

After completing the previous steps, you have set up Cloud NAT on your VPC network with a predefined static IP address, and you have routed all of your Cloud Run service's outbound traffic into your VPC network. Requests from your Cloud Run service travel through your VPC network and reach external endpoints using the static IP address.

To verify this behavior and confirm the origin IP address that your service uses, you can make a request to an API or a website such as [curlmyip.org](https://curlmyip.org) that shows the originating IP address.

## Deleting the static external IP address

If you no longer need a static external IP address, see [Release a static external IP address](https://docs.cloud.google.com/vpc/docs/reserve-static-external-ip-address#release_ip).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
