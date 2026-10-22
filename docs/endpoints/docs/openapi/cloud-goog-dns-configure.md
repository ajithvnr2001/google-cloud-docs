---
url: https://docs.cloud.google.com/endpoints/docs/openapi/cloud-goog-dns-configure/
title: Configuring DNS on the cloud.goog domain \u00a0|\u00a0 Cloud Endpoints with OpenAPI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:53:13.367720+00:00
---

# Configuring DNS on the cloud.goog domain  |  Cloud Endpoints with OpenAPI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/openapi/cloud-goog-dns-configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ OpenAPI ](https://docs.cloud.google.com/endpoints/docs/openapi)



Send feedback 

#  Configuring DNS on the cloud.goog domain Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI | [gRPC](https://docs.cloud.google.com/endpoints/docs/grpc/cloud-goog-dns-configure "View this page for the Cloud Endpoints gRPC docs")

After your API is deployed, users of your API need to access it through a domain name rather than an IP address. You can either:

  * Configure `.endpoints.PROJECT_ID.cloud.goog` as the domain name (where `PROJECT_ID` is your Google Cloud project ID).
  * Or register your own domain name, such as `example.com`, which entails: 
    * Configuring DNS name servers (or using [ Cloud DNS](https://docs.cloud.google.com/dns/docs)).
    * Updating registry addresses.
    * Creating and maintaining DNS records.

If you already have a DNS infrastructure, or you want to register your own domain name, see [ Serving an API from your domain name](https://docs.cloud.google.com/endpoints/docs/grpc/serving-apis-from-domains) for more information.




This page describes how to configure Cloud Endpoints APIs to use `.endpoints.PROJECT_ID.cloud.goog` as the domain name. The configuration steps on this page are applicable for APIs using OpenAPI running on Compute Engine, Google Kubernetes Engine, or Kubernetes. The `.endpoints.PROJECT_ID.cloud.goog` domain name isn't supported for APIs running on App Engine. For APIs on App Engine, we recommend that you use `PROJECT_ID.appspot.com` as the Endpoints service name. When you deploy the API to App Engine, a DNS entry with a name in the format `PROJECT_ID.appspot.com` is created automatically. 

The `.cloud.goog` domain is managed by Google and shared by Google Cloud customers. Because Google Cloud projects are guaranteed to have a globally unique project ID, a domain name in the format `.endpoints.PROJECT_ID.cloud.goog` is unique and can be used as the domain name for your API. Configuring the `.endpoints.PROJECT_ID.cloud.goog` domain name is optional. If you prefer, you can register your own domain name.

## Prerequisites

As a starting point, this page assumes that you have already created your Cloud Endpoints API and deployed it to Compute Engine, Google Kubernetes Engine, or Kubernetes. If you need an API for testing, you can use one of the [tutorials](https://docs.cloud.google.com/endpoints/docs/openapi/tutorials) that walk you through configuring and deploying a sample API.

## Configuring DNS

The following procedure describes how to configure DNS for Cloud Endpoints APIs that use `.endpoints.[PROJECT_ID].cloud.goog` as the Endpoints service name where `[PROJECT_ID]` represents your Google Cloud project ID. For convenience, the procedure refers to your OpenAPI configuration file as `openapi.yaml`.

To configure DNS:

  1. Open `openapi.yaml`, and add the `x-google-endpoints` field to the file as shown in the following snippet: 
         
         swagger: "2.0"
             host: "[API_NAME].endpoints.[PROJECT_ID].cloud.goog"
             x-google-endpoints:
             - name: "[API_NAME].endpoints.[PROJECT_ID].cloud.goog"
               target: "[IP_ADDRESS]"

Typically, you configure the `host` field and the `x-google-endpoints.name` field to be the same. When you deploy your OpenAPI specification, the text specified in the `host` field is used as the name of your Endpoints service.

  2. Replace `[API_NAME]` with the name of your API (for example, `bookstore` or `my-cool-api`).
  3. Replace `[PROJECT_ID]` with your Google Cloud project ID.
  4. Replace `[IP_ADDRESS]` with an IPv4 address. 

For example, if you deploy your Endpoints API service to a Compute Engine virtual machine instance, you can use the external IP of that virtual machine. Alternatively, if you run your code on a group of virtual machine instances (or GKE pods) behind a load balancer, you can use the IP address of the load balancer.

  5. Deploy your new OpenAPI specification to Service Management using the following command: 
         
         gcloud endpoints services deploy openapi.yaml




For example, if the following is specified in an `openapi.yaml` file: 
    
    
        swagger: "2.0"
        host: "my-cool-api.endpoints.my-project-id.cloud.goog"
        x-google-endpoints:
        - name: "my-cool-api.endpoints.my-project-id.cloud.goog"
          target: "192.0.2.1"

When you deploy the `openapi.yaml` using the previous `gcloud` command, Service Management creates a DNS A-record, `my-cool-api.endpoints.my-project-id.cloud.goog`, which resolves to the target IP address, `192.0.2.1`. You might need to wait a few minutes for the new DNS configuration to propagate.

## What's next

  * [Enabling SSL for Endpoints](https://docs.cloud.google.com/endpoints/docs/openapi/enabling-ssl)
  * [Configuring IP addresses](https://docs.cloud.google.com/compute/docs/configure-ip-addresses)
  * [Naming your API service](https://docs.cloud.google.com/endpoints/docs/openapi/naming-your-api-service)
  * [Serving an API from your domain name](https://docs.cloud.google.com/endpoints/docs/openapi/serving-apis-from-domains)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
