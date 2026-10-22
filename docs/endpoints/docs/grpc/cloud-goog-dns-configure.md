---
url: https://docs.cloud.google.com/endpoints/docs/grpc/cloud-goog-dns-configure/
title: Configuring DNS on the cloud.goog domain \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:10.478408+00:00
---

# Configuring DNS on the cloud.goog domain  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/cloud-goog-dns-configure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Configuring DNS on the cloud.goog domain Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/cloud-goog-dns-configure "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

After your API is deployed, users of your API need to access it through a domain name rather than an IP address. You can either:

  * Configure `.endpoints.PROJECT_ID.cloud.goog` as the domain name (where `PROJECT_ID` is your Google Cloud project ID).
  * Or register your own domain name, such as `example.com`, which entails: 
    * Configuring DNS name servers (or using [ Cloud DNS](https://docs.cloud.google.com/dns/docs)).
    * Updating registry addresses.
    * Creating and maintaining DNS records.

If you already have a DNS infrastructure, or you want to register your own domain name, see [ Serving an API from your domain name](https://docs.cloud.google.com/endpoints/docs/grpc/serving-apis-from-domains) for more information.




This page describes how to configure Cloud Endpoints APIs to use `.endpoints.PROJECT_ID.cloud.goog` as the domain name. The configuration steps on this page are applicable for APIs using gRPC running on Compute Engine, Google Kubernetes Engine, or Kubernetes. 

The `.cloud.goog` domain is managed by Google and shared by Google Cloud customers. Because Google Cloud projects are guaranteed to have a globally unique project ID, a domain name in the format `.endpoints.PROJECT_ID.cloud.goog` is unique and can be used as the domain name for your API. Configuring the `.endpoints.PROJECT_ID.cloud.goog` domain name is optional. If you prefer, you can register your own domain name.

## Prerequisites

As a starting point, this page assumes that you have already created your Cloud Endpoints API and deployed it to Compute Engine, Google Kubernetes Engine, or Kubernetes. If you need an API for testing, you can use one of the [tutorials](https://docs.cloud.google.com/endpoints/docs/grpc/tutorials) that walk you through configuring and deploying a sample API.

## Configuring DNS

The following procedure describes how to configure DNS for Endpoints APIs that use `.endpoints.PROJECT_ID.cloud.goog` as the Endpoints service name. For convenience, the procedure refers to your gRPC service configuration file as `service.yaml`.

To configure DNS:

  1. Open `service.yaml`, and add the `endpoints` field to the file as shown in the following code snippet: 
         
         type: google.api.Service
         name: API_NAME.endpoints.PROJECT_ID.cloud.goog
         endpoints:
         - name: API_NAME.endpoints.PROJECT_ID.cloud.goog
           target: "IP_ADDRESS"
           

Typically, the `name` field and the `endpoints.name` field are the same.

  2. Replace `API_NAME` with the name of your API (for example, `bookstore` or `my-cool-api`).
  3. Replace `IP_ADDRESS` with an IPv4 address. The IP address is a string and must be enclosed in quotation marks. 

For example, if you deploy your Endpoints API service to a Compute Engine virtual machine instance, you can use the external IP address of that virtual machine. Alternatively, if you run your code on a group of virtual machine instances (or GKE pods) behind a load balancer, you can use the IP address of the load balancer.

  4. Deploy your updated gRPC configuration file to Service Management by using the following command: 
         
         gcloud endpoints services deploy service.yaml service.pb
         




For example, if the following is specified in the `service.yaml` file:
    
    
    type: google.api.Service
    name: my-cool-api.endpoints.my-project-id.cloud.goog
    endpoints:
    - name: my-cool-api.endpoints.my-project-id.cloud.goog
      target: "192.0.2.1"
    

When you deploy the `service.yaml` file by using the precediing `gcloud` command, Service Management creates a DNS A-record, `my-cool-api.endpoints.my-project-id.cloud.goog`, which resolves to the target IP address, `192.0.2.1`. You might need to wait a few minutes for the new DNS configuration to propagate.

## What's next

  * [Configuring Endpoints](https://docs.cloud.google.com/endpoints/docs/grpc/configure-endpoints)
  * [Enabling SSL for Endpoints](https://docs.cloud.google.com/endpoints/docs/grpc/enabling-ssl)
  * [Reserving a static external IP address](https://docs.cloud.google.com/compute/docs/configure-ip-addresses)
  * [Serving an API from your domain name](https://docs.cloud.google.com/endpoints/docs/grpc/serving-apis-from-domains)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
