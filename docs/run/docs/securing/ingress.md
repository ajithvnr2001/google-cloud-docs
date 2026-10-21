---
url: https://docs.cloud.google.com/run/docs/securing/ingress/
title: Restrict network endpoint ingress for Cloud Run services and instances \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:01:54.196951+00:00
---

# Restrict network endpoint ingress for Cloud Run services and instances  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/securing/ingress/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Restrict network endpoint ingress for Cloud Run services and instances Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to use ingress settings to restrict network access to your Cloud Run services and instances.

At a network level, a Cloud Run service's or instance's endpoint is reachable from the following network ingress paths:

  * Default `run.app` URLs, which you can [disable](https://docs.cloud.google.com/run/docs/securing/ingress#disable-url)
  * Any configured [domain mapping](https://docs.cloud.google.com/run/docs/mapping-custom-domains)
  * Any configured External Application Load Balancer or Internal Application Load Balancer



All network ingress paths are subject to the resource's ingress setting. The default ingress paths and ingress setting allow any resource on the internet to reach your Cloud Run resource. You can [use a custom constraint](https://docs.cloud.google.com/run/docs/securing/custom-constraints#restrict-ingress) to restrict ingress settings for your organization or for a set of projects. [IAM authentication](https://docs.cloud.google.com/run/docs/securing/managing-access) still applies to requests reaching the service or instance endpoints from any of the preceding network ingress paths. For a layered approach to managing access, use both network ingress settings and [IAM](https://docs.cloud.google.com/run/docs/securing/managing-access) authentication.

Use network tags to [restrict connector VM access to VPC resources](https://docs.cloud.google.com/run/docs/configuring/vpc-connectors#connector-to-resource).

## Available network ingress settings

The following settings are available:

Setting | Description  
---|---  
Internal |  Most restrictive. Allows requests from the following sources:  


  * Internal Application Load Balancer, including requests from Shared VPC networks when routed through the internal Application Load Balancer.
  * Resources allowed by any [ VPC Service Controls](https://docs.cloud.google.com/run/docs/securing/using-vpc-service-controls) perimeter that contains your Cloud Run service or instance. Cloud Run must be configured as a restricted service.
  * VPC networks that are in the same project as your Cloud Run service or instance.
  * Shared VPC ingress: the Shared VPC network that your service revision or Cloud Run instance is configured to send traffic to. For information about when Shared VPC traffic is recognized as "internal", see [Special considerations for Shared VPC](https://docs.cloud.google.com/run/docs/securing/private-networking#shared-vpc).
  * The following Google Cloud products, if they're in the same project or VPC Service Controls perimeter as your Cloud Run service or instance, and if they're using the default `run.app` URL and not a custom URL or custom domain:
    * Cloud Scheduler
    * Cloud Tasks
    * [Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#internal-only-traffic)
    * Eventarc
    * Gemini Enterprise
    * Pub/Sub subscriptions
    * [Synthetic monitors (including uptime checks)](https://docs.cloud.google.com/monitoring/uptime-checks/introduction)
    * Workflows
    * [BigQuery](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/remote-functions)

Requests from these sources stay within the Google network, even if they access your service or instance at the `run.app` URL. Requests from other sources, including the internet, cannot reach your service or instance at the `run.app` URL, custom URL, or custom domain.  
  
  
Internal and Cloud Load Balancers | This setting allows requests from the following resources:  


  * Resources allowed by the more restrictive "internal" setting
  * External Application Load Balancer

Use this setting to do the following: 
  * Accept requests from the internet through the external Application Load Balancer. Direct requests to the `run.app` URL from the internet are not allowed.
  * Ensure that requests from the internet are subject to external Application Load Balancer features, such as [Identity-Aware Proxy](https://docs.cloud.google.com/iap), [Google Cloud Armor](https://cloud.google.com/security/products/armor), and [Cloud CDN](https://docs.cloud.google.com/cdn/docs/setting-up-cdn-with-serverless).

  
Note: To enable this setting in the gcloud CLI, use `internal-and-cloud-load-balancing`. To enable this setting in the Google Cloud console, select **Internal > Allow traffic from external Application Load Balancers**.   
All |  Least restrictive. Allows all requests, including requests directly from the internet to the `run.app` URL.   
  
## Access internal services

The following additional considerations apply:

  * When accessing internal services, call them as you would normally do using their URL, either the default `run.app` URL, a [custom URL](https://docs.cloud.google.com/run/docs/custom-urls), or a [custom domain](https://docs.cloud.google.com/run/docs/mapping-custom-domains) set up in Cloud Run.

  * For requests from Compute Engine VM instances, no further setup is required for machines that have external IP addresses or that use Cloud NAT. Otherwise, see [Receive requests from VPC networks](https://docs.cloud.google.com/run/docs/securing/private-networking#from-vpc).

  * When calling from Cloud Run or App Engine to a Cloud Run service that's set to "Internal" or "Internal and Cloud Load Balancers", traffic must route through a VPC network that's considered internal. See [Receive requests from other Cloud Run services or App Engine](https://docs.cloud.google.com/run/docs/securing/private-networking#from-other-services).

  * Requests from resources within VPC networks in the same project are "internal" even if the resource that they originate from has an external IP address.

  * Requests from on-premises resources connected to the VPC network using Cloud VPN and Cloud Interconnect are "internal."




## Set ingress

The following sections show how to set ingress for Cloud Run services and instances.

### Set ingress for Cloud Run services

You can set ingress for a Cloud Run service by using the Google Cloud console, Google Cloud CLI, YAML, or Terraform.

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. If you are configuring a new service, click **Deploy container** to display the **Create service** form. Fill out the initial service settings page.

  3. If you are configuring an existing service, click the service, and then click the **Networking** tab.

  4. Select the ingress traffic you want to allow.

  5. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

  1. If you are deploying a new service, deploy your service with the `--ingress` flag:
         
         gcloud run deploy SERVICE \
             --image IMAGE_URL \
             --ingress INGRESS

Replace the following:

     * `SERVICE`: your service name.
     * `IMAGE_URL`: a reference to the container image, for example, `us-docker.pkg.dev/cloudrun/container/hello:latest`. If you use Artifact Registry, the [repository](https://docs.cloud.google.com/artifact-registry/docs/repositories/create-repos#docker) REPO_NAME must already be created. The URL follows the format of `LOCATION-docker.pkg.dev/PROJECT_ID/REPO_NAME/PATH:TAG` .
     * `INGRESS`: one of the available ingress settings: 
       * `all`
       * `internal`
       * `internal-and-cloud-load-balancing`
  2. If you are changing an existing service ingress:
         
         gcloud run services update SERVICE \
             --ingress INGRESS

Replace the following:

     * `SERVICE`: your service name
     * `INGRESS`: one of the available ingress settings: 
       * `all`
       * `internal`
       * `internal-and-cloud-load-balancing`



### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update the `run.googleapis.com/ingress:` annotation:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
           annotations:
             run.googleapis.com/ingress: INGRESS
         spec:
           template:
             metadata:
               name: REVISION

Replace the following:

     * `SERVICE`: the name of your Cloud Run service.
     * `INGRESS`: one of the available ingress settings: 
       * `all`
       * `internal`
       * `internal-and-cloud-load-balancing`
     * `REVISION`: a new revision name or delete it (if present). If you supply a new revision name, it **must** meet the following criteria:
       * Starts with `SERVICE-`
       * Contains only lowercase letters, numbers and `-`
       * Does not end with a `-`
       * Does not exceed 63 characters
  3. Replace the service with its new configuration using the following command:
         
         gcloud run services replace service.yaml




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
    resource "google_cloud_run_v2_service" "default" {
      provider = google-beta
      name     = "ingress-service"
      location = "us-central1"
    
      deletion_protection = false # set to "true" in production
    
      # For valid annotation values and descriptions, see
      # https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service#ingress
      ingress = "INGRESS_TRAFFIC_INTERNAL_ONLY"
    
      template {
        containers {
          image = "us-docker.pkg.dev/cloudrun/container/hello" #public image for your service
        }
      }
    }

### Set ingress for Cloud Run instances

You can set ingress for a Cloud Run instance by using the Google Cloud CLI or YAML:

###  gcloud 

  1. If you are creating a new instance, deploy your instance with the `--ingress` flag:
         
         gcloud beta run instances deploy INSTANCE \
             --image IMAGE_URL \
             --ingress INGRESS

Replace the following:

     * `INSTANCE`: your instance name.
     * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`..
     * `INGRESS`: one of the available ingress settings: 
       * `all`
       * `internal`
       * `internal-and-cloud-load-balancing`
  2. If you are changing an existing instance ingress:
         
         gcloud beta run instances update INSTANCE \
             --ingress INGRESS

Replace the following:

     * `INSTANCE`: your instance name.
     * `INGRESS`: one of the available ingress settings: 
       * `all`
       * `internal`
       * `internal-and-cloud-load-balancing`



### YAML

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. Update the `run.googleapis.com/ingress:` annotation:
         
         apiVersion: run.googleapis.com/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/ingress: INGRESS
             run.googleapis.com/launch-stage: BETA
         spec:
           containers:
           - name: CONTAINER_NAME
             image: IMAGE_URL

Replace the following:

     * `INSTANCE`: the name of your Cloud Run instance.
     * `INGRESS`: one of the [available ingress settings](https://docs.cloud.google.com/run/docs/securing/ingress#settings): 
       * `all`
       * `internal`
       * `internal-and-cloud-load-balancing`
     * `CONTAINER_NAME`: the name of the container.
     * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`..
  3. Create or update the instance using the following command:
         
         gcloud beta run instances replace instance.yaml




**Note:** Administrators can restrict the ingress settings that developers can select by setting the [`run.allowedIngress`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#available_constraints) organization policy.

## Disable the default URL

Before you disable the default URL, be aware that the following Google Cloud services or instance use the default `run.app` URL to invoke Cloud Run. Disabling the default `run.app` URL prevents these services or instance from working as expected:

  * The [`cloudfunctions.net` URL](https://docs.cloud.google.com/functions/docs/calling/http#url) of Cloud Functions v2 API based on the Cloud Run service.
  * [Cloud Scheduler](https://docs.cloud.google.com/run/docs/triggering/using-scheduler#create_job)
  * [Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview)
  * [Cloud Tasks](https://docs.cloud.google.com/run/docs/triggering/using-tasks#creating_http_tasks_with_authentication_tokens)
  * [Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/webhook#internal-only-traffic)
  * [Eventarc](https://docs.cloud.google.com/eventarc/docs/run/route-trigger-cloud-audit-logs#create-trigger)
  * [Firebase App Hosting](https://firebase.google.com/docs/app-hosting)
  * [Firebase Hosting](https://firebase.google.com/docs/hosting)
  * [Pub/Sub](https://docs.cloud.google.com/run/docs/tutorials/pubsub#integrating-pubsub)
  * [Synthetic monitors](https://docs.cloud.google.com/monitoring/uptime-checks/introduction) and [uptime checks](https://docs.cloud.google.com/monitoring/uptime-checks)
  * [Workflows](https://docs.cloud.google.com/workflows/docs/tutorials/run/cloud-run#connect-rest-api)

**Note:** [Custom URLs](https://docs.cloud.google.com/run/docs/custom-urls) are fully independent. If you choose to disable the default `.run.app` URL for a service, your custom URL mapping remains fully active and accessible.

To use custom domain mappings, [map the custom domain before you disable the `run.app` URL](https://docs.cloud.google.com/run/docs/known-issues#custom-domain-mappings).

See the following sections to learn how to disable the default URL for Cloud Run services and instances.

### Disable the default URL for Cloud Run services

Disable the default `run.app` URL of a Cloud Run service or instance to only allow traffic from the service's other ingress paths: Cloud Load Balancing and any configured [domain mapping](https://docs.cloud.google.com/run/docs/mapping-custom-domains).

To disable the default URL, perform the following steps by using the Google Cloud console, Google Cloud CLI, YAML, or Terraform.

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click an existing service.

  3. Select the **Networking** tab.

  4. In the **Endpoints** card, clear **Enable** under **Default HTTPS endpoint URL**.

  5. Click **View diff & redeploy**, then **Deploy changes**.




To restore the default URL, select **Enable**.

###  gcloud 

  * For an existing service, run the `gcloud run services update` command with the `--no-default-url` flag, for example:
        
        gcloud run services update SERVICE_NAME --no-default-url

  * For a new service, run the `gcloud run deploy` command with the `--no-default-url` flag, for example:
        
        gcloud run deploy SERVICE_NAME --no-default-url

Replace `SERVICE_NAME` with the name of your Cloud Run service.

In the output, the URL displays as `None`.




To restore the default URL, use the `--default-url` flag.

### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. To disable the `run.app` URL, use the `run.googleapis.com/default-url-disabled` annotation:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           annotations:
             run.googleapis.com/default-url-disabled: true
           name: SERVICE
         spec:
           template:
             metadata:
               name: REVISION

Replace the following:

     * `SERVICE`: the name of your Cloud Run service.
     * `REVISION`: a new revision name or delete it (if present). If you supply a new revision name, it **must** meet the following criteria:
       * Starts with `SERVICE-`
       * Contains only lowercase letters, numbers and `-`
       * Does not end with a `-`
       * Does not exceed 63 characters
  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




To restore the default URL, remove the `run.googleapis.com/default-url-disabled` annotation.

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
      resource "google_cloud_run_v2_service" "disable_default_url_service" {
        name     = "cloudrun-service"
        location = "europe-west1"
        default_uri_disabled = true
    
        template {
          containers {
            image = "us-docker.pkg.dev/cloudrun/container/hello"
          }
          annotations = {
            "run.googleapis.com/ingress" = "all"   # "all" or "internal-only"
          }
    
        }
      }
    

Verify that the `launch_stage` and `default_uri_disabled` lines are in your `main.tf` file. The preceding `google_cloud_run_v2_service` resource specifies a Cloud Run service with the default URL disabled in Preview.

To restore the default URL, remove the `default_uri_disabled` and `launch_stage` arguments.

### Disable the default URL for Cloud Run instances

Disable the default `run.app` URL of a Cloud Run instance to only allow traffic from the instance's other ingress paths: Cloud Load Balancing and any configured [domain mapping](https://docs.cloud.google.com/run/docs/mapping-custom-domains).

###  gcloud 

  * For an existing instance, run the `gcloud beta run instances update` command with the `--no-default-url` flag, for example:
        
        gcloud beta run instances update INSTANCE --no-default-url

  * For a new instance, run the `gcloud beta run instances deploy` command with the `--no-default-url` flag, for example:
        
        gcloud beta run instances deploy INSTANCE \
            --image IMAGE_URL \
            --no-default-url

Replace `INSTANCE` with the name of your Cloud Run instance.

In the output, the URL displays as `None`.




To restore the default URL, use the `--default-url` flag.

### YAML

  1. If you are creating a new instance, skip this step. If you are updating an existing instance, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud beta run instances describe INSTANCE --format export > instance.yaml

  2. To disable the default URL, set the `run.googleapis.com/default-url-disabled` annotation to `'true'`:
         
         apiVersion: run.googleapis.com/v1
         kind: Instance
         metadata:
           name: INSTANCE
           annotations:
             run.googleapis.com/default-url-disabled: 'true'
             run.googleapis.com/launch-stage: BETA
         spec:
           containers:
           - name: CONTAINER_NAME
             image: IMAGE_URL

Replace the following:

     * `INSTANCE`: the name of your Cloud Run instance.
     * `CONTAINER_NAME`: the name of the container.
     * `IMAGE_URL`: a reference to the container image, such as `us-docker.pkg.dev/cloudrun/container/hello:latest`.
  3. Create or update the instance using the following command:
         
         gcloud beta run instances replace instance.yaml




To restore the default URL, set the `run.googleapis.com/default-url-disabled` annotation to `false` or remove it.

## What's next

  * Learn about [egress](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc) settings.
  * Set up an [internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless) for Cloud Run. 
  * Set up an [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https/setup-global-ext-https-serverless) with Cloud Run. 
  * Configure [IAM](https://docs.cloud.google.com/run/docs/securing/managing-access) authentication methods for accessing services or instances.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
