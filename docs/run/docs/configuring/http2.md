---
url: https://docs.cloud.google.com/run/docs/configuring/http2/
title: Use HTTP/2 for services \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:35.866347+00:00
---

# Use HTTP/2 for services  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/configuring/http2/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Use HTTP/2 for services Stay organized with collections  Save and categorize content based on your preferences. 

When a container instance receives requests, Cloud Run downgrades those requests from HTTP/2 to HTTP/1 with the exception of native gRPC traffic, which requires HTTP/2 to function correctly. This page shows you how to configure your service to use end-to-end HTTP/2, which prevents Cloud Run from downgrading requests to HTTP1.

For more information about invoking services using HTTP, see [Invoking with an HTTPS Request](https://docs.cloud.google.com/run/docs/triggering/https-request).

## Before you configure

Your Cloud Run service must handle requests in [HTTP/2 cleartext](https://http2.github.io/faq/#can-i-implement-http2-without-implementing-http11) (`h2c`) format. Google's frontend-serving infrastructure terminates TLS and then forwards the `h2c` traffic to Cloud Run and to your container through an encrypted channel.

To confirm that your service supports `h2c` requests, [test the service locally](https://docs.cloud.google.com/run/docs/testing/local) using this curl command:
    
    
    curl -i --http2-prior-knowledge http://localhost:PORT

### Required roles

To get the permissions that you need to configure and deploy Cloud Run services, ask your administrator to grant you the following IAM roles: 

  * [Cloud Run Developer ](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.developer) (`roles/run.developer`) on the Cloud Run service
  * [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) on the service identity



If you are deploying a [service](https://docs.cloud.google.com/run/docs/deploying-source-code#required_roles) or [function](https://docs.cloud.google.com/run/docs/deploy-functions#required-roles) from source code, you must also have additional roles granted to you on your project and Cloud Build service account.

For a list of IAM roles and permissions that are associated with Cloud Run, see [Cloud Run IAM roles](https://docs.cloud.google.com/run/docs/reference/iam/roles) and [Cloud Run IAM permissions](https://docs.cloud.google.com/run/docs/reference/iam/permissions). If your Cloud Run service interfaces with Google Cloud APIs, such as Cloud Client Libraries, see the [service identity configuration guide](https://docs.cloud.google.com/run/docs/configuring/services/service-identity). For more information about granting roles, see [deployment permissions](https://docs.cloud.google.com/run/docs/reference/iam/roles#additional-configuration) and [manage access](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Supported HTTP/2 services

HTTP/2 is ideal for a variety of applications. Some common use cases include the following:

  * **gRPC services** : build high-performance, low-latency microservices that communicate using [gRPC](https://docs.cloud.google.com/load-balancing/docs/https#grpc-support).
  * **APIs with high throughput** : reduce overhead for applications that require efficient handling of numerous small requests or need to push data to clients.



## Set and update HTTP/2 end-to-end

Any configuration change leads to the creation of a new revision. Subsequent revisions will also automatically get this configuration setting unless you make explicit updates to change it.

You can specify the use of HTTP/2 end-to-end by using the Google Cloud console, Google Cloud CLI, or YAML when you [create a new service](https://docs.cloud.google.com/run/docs/deploying#service) or [deploy a new revision](https://docs.cloud.google.com/run/docs/deploying#revision):

### Console

  1. In the Google Cloud console, go to Cloud Run:

[Go to Cloud Run](https://console.cloud.google.com/run)

  2. Select **Services** from the Cloud Run navigation menu:

     1. If you are configuring a new service, click **Deploy container** and fill out the initial service settings page. Then click **Containers, Networking, Security** to expand the service configuration page.

     2. If you are configuring an existing service, click the service.

  3. Click the **Networking** tab.

  4. Select the checkbox next to **Use HTTP/2 end-to-end**. Make sure your custom container image supports HTTP/2 requests.

  5. Click **Create** for a new service. Click **View diff & redeploy**, then **Deploy changes** for an existing service.




###  gcloud 

You can [update](https://docs.cloud.google.com/sdk/gcloud/reference/run/services/update) a given service to use HTTP/2 by using the following command:
    
    
    gcloud run services update SERVICE --use-http2

Replace `SERVICE` with the name of your service.

You can also set your service to use HTTP/2 during [deployment](https://docs.cloud.google.com/sdk/gcloud/reference/run/deploy) using the command:
    
    
    gcloud run deploy --image IMAGE_URL --use-http2

Replace IMAGE_URL with a reference to your custom container image that supports HTTP/2 requests.

### YAML

  1. If you are creating a new service, skip this step. If you are updating an existing service, download its [YAML configuration](https://docs.cloud.google.com/run/docs/reference/yaml/v1):
         
         gcloud run services describe SERVICE --format export > service.yaml

  2. Update `ports` with the name`h2c` and `containerPort` with the port of your choice, as shown in the following example:
         
         apiVersion: serving.knative.dev/v1
         kind: Service
         metadata:
           name: SERVICE
         spec:
           template:
             metadata:
               name: REVISION
             spec:
               containers:
               - image: IMAGE_URL
                 ports:
                 - name: h2c
                   containerPort: 8080

Replace the following:

     * SERVICE: the name of your Cloud Run service
     * IMAGE_URL: a reference to your custom container image that supports HTTP/2 requests
     * `REVISION`: a new revision name or delete it (if present). If you supply a new revision name, it **must** meet the following criteria:
       * Starts with `SERVICE-`
       * Contains only lowercase letters, numbers and `-`
       * Does not end with a `-`
       * Does not exceed 63 characters
  3. Create or update the service using the following command:
         
         gcloud run services replace service.yaml

The `gcloud run services replace` command defaults to using `service.yaml` file if present.




### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands).

Add the following to a [`google_cloud_run_v2_service`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/cloud_run_v2_service) resource in your Terraform configuration:  

    
    
      resource "google_cloud_run_v2_service" "default" {
        name     = "cloudrun-service-h2c"
        location = "us-central1"
    
        deletion_protection = false # set to "true" in production
    
        template {
          containers {
            image = IMAGE_URL
            # Enable HTTP/2
            ports {
              name           = "h2c"
              container_port = 8080
            }
          }
        }
      }
    

Replace IMAGE_URL with a reference to your custom container image that supports HTTP/2 requests.

If your container listens for HTTP requests on a port other than `8080`, replace `8080` with that port number.

## View HTTP/2 settings

To view the current HTTP/2 settings for your Cloud Run service:

### Console

  1. In the Google Cloud console, go to the Cloud Run **Services** page:

[Go to Cloud Run](https://console.cloud.google.com/run/services)

  2. Click the service you are interested in to open the **Service details** page.

  3. Click the **Networking** tab to view the settings.




###  gcloud 

  1. Use the following command:
         
         gcloud run services describe SERVICE

  2. Locate the HTTP/2 setting in the returned configuration.




## Use HTTP/2 behind a load balancer

When configured to listen for HTTP/2, Cloud Run automatically handles the HTTP/2 or gRPC traffic arriving from the Application Load Balancer. No specific configuration is needed on the load balancer's backend service.

To configure Cloud Run to use HTTP/2 or gRPC, use one of the following methods:

  * Set and update HTTP/2 end-to-end
  * Configure an [external Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) with your Cloud Run service as the backend.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
