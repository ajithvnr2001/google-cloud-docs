---
url: https://docs.cloud.google.com/endpoints/docs/grpc/architecture-overview/
title: Architectural overview of Cloud Endpoints \u00a0|\u00a0 Cloud Endpoints with gRPC \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:01:26.481960+00:00
---

# Architectural overview of Cloud Endpoints  |  Cloud Endpoints with gRPC  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/endpoints/docs/grpc/architecture-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Endpoints ](https://docs.cloud.google.com/endpoints/docs)
  * [ gRPC ](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

#  Architectural overview of Cloud Endpoints Stay organized with collections  Save and categorize content based on your preferences. 

[OpenAPI](https://docs.cloud.google.com/endpoints/docs/openapi/architecture-overview "View this page for the Cloud Endpoints OpenAPI docs") | gRPC

Endpoints is a distributed API management system comprising services, runtimes, and tools. Endpoints provides management, monitoring, and authentication.

The components that make up Endpoints are:

  * Extensible Service Proxy (ESP) or Extensible Service Proxy V2 (ESPv2) - for injecting Endpoints functionality.

  * Service Control - for applying API management rules.

  * Service Management - for configuring API management rules.

  * Google Cloud CLI - for deploying and management.

  * Google Cloud console - for logging, monitoring and sharing.




## Endpoints architecture

![Endpoints architecture](https://docs.cloud.google.com/static/endpoints/docs/images/endpoints_arch.png)

## Endpoints components

### ESP

ESP is a NGINX-based proxy that runs in front of the backend and injects Endpoints functionality such as authentication, monitoring, and logging. ESP retrieves a service configuration from Service Management and uses it to validate incoming requests.

ESP is designed for you to deploy it in a containerized environment and validate JWTs and Google ID tokens. It employs a variety of techniques, such as heavy caching and asynchronous calls to remain lightweight and highly performant.

ESP support is available for the following platforms:

  * [Compute Engine](https://docs.cloud.google.com/endpoints/docs/grpc/get-started-compute-engine-docker-espv2)
  * [Google Kubernetes Engine](https://docs.cloud.google.com/endpoints/docs/grpc/get-started-kubernetes-engine-espv2)
  * [Kubernetes](https://docs.cloud.google.com/endpoints/docs/grpcs/get-started-kubernetes-espv2)



### ESPv2

ESPv2 is an [Envoy](https://www.envoyproxy.io/docs/envoy/latest/)-based high-performance, scalable proxy that runs in front of an OpenAPI or gRPC API backend. Endpoints on ESPv2 supports version 2 of the [OpenAPI Specification](https://github.com/OAI/OpenAPI-Specification/blob/master/versions/2.0.md) and gRPC specifications.

ESPv2 integrates with Google Service Infrastructure to enable API management features at scale, including authentication, telemetry reports, metrics, and security.

[ESPv2](https://docs.cloud.google.com/endpoints/docs/openapi/glossary#extensible_service_proxy_v2) support is available for the following platforms: 

  * [Cloud Run](https://docs.cloud.google.com/endpoints/docs/grpc/set-up-cloud-run-anthos-espv2)
  * [Knative serving](https://docs.cloud.google.com/endpoints/docs/grpc/set-up-cloud-run-anthos-espv2)
  * [Compute Engine](https://docs.cloud.google.com/endpoints/docs/grpc/get-started-compute-engine-docker-espv2)
  * [Google Kubernetes Engine](https://docs.cloud.google.com/endpoints/docs/grpc/get-started-kubernetes-engine-espv2)
  * [Kubernetes](https://docs.cloud.google.com/endpoints/docs/grpcs/get-started-kubernetes-espv2)



### Service Control

[Service Control](https://docs.cloud.google.com/service-control) applies API management rules at runtime, such as key authentication, monitoring, and logging. Service Control provides the following methods:

  * Check - verifies authentication and API keys, and indicates whether a call should be permitted

  * Report - notifies the systems of record for logging and monitoring




### Service Management

You describe the behavior of your gRPC service in a YAML file referred to as the Endpoints configuration. You deploy the Endpoints configuration and your compiled `.proto` files to Service Management by using the gcloud CLI, which configures the API management rules. Other configuration related tasks also happen here, such as sharing your API with other developers, enabling or disabling the API in different projects, and generating API keys. 

### The gcloud CLI

[The gcloud CLI](https://docs.cloud.google.com/sdk) provides the Google Cloud CLI that you can use to make calls to various Google Cloud services. You use the Google Cloud CLI to deploy your Endpoints configuration to Service Management.

### Google Cloud console

[Google Cloud console](https://docs.cloud.google.com/cloud-console) is the graphical user interface for Google Cloud. Endpoints uses the Google Cloud console to expose monitoring and logging data that are sent from ESP or ESPv2 and recorded by Service Control and share APIs with other developers, and for them to generate API keys to call the API.

## Deployment scenarios

Options for deployment vary depending upon the use of ESP or ESPv2 as the Endpoints proxy. ESPv2 can be deployed as a remote proxy and both ESPv2 and ESP can be deployed in sidecar mode, as explained in the following sections.

### Remote proxy mode

If using ESPv2, Endpoints can be deployed as a remote proxy. This mode is used to support applications running on serverless platforms such as Cloud Run, Cloud Run functions, and App Engine for standard environments.

In this mode, ESPv2 is deployed as a Cloud Run application. The application is configured to use ESPv2 as a remote backend using the `x-google-backend` field in the OpenAPI service config. When functioning as a remote proxy in this deployment mode, a single ESPv2 can support multiple remote backends.

See [Configuring Endpoints](https://docs.cloud.google.com/endpoints/docs/grpc/get-started-cloud-run#endpoints_configure) for more details. 

### Sidecar mode

Both ESP and ESPv2 support deployment in a container alongside each instance of your backend. This server-local topology is ideal for both web-facing APIs as well as microservices. It avoids the network hop typically associated with centralized proxies and allows API management that is highly performant as well as scalable.

Typically, load balancing is applied before traffic hits ESP or ESPv2. On Compute Engine, it is accomplished by Cloud Load Balancing. For Kubernetes deployments, you can use an ingress proxy for load balancing. In Google Kubernetes Engine, you can use either Cloud Load Balancing or an ingress proxy for load balancing.

Upon startup, ESP or ESPv2 obtains its service configuration from Service Management. The service configuration is generated from the OpenAPI specification or from [gRPC](http://www.grpc.io/), the service configuration YAML file. It tells ESP or ESPv2 both the surface of the API to be managed along with the policies, such as which methods require authentication, and which require API keys.

## Request routing

When a request is received, ESP or ESPv2 creates a trace token for Cloud Trace.

Next, ESP or ESPv2 matches the path of the incoming requests with the surface of the API. After finding a matching route, ESP or ESPv2 performs any authentication steps for the specified method.

If JWT validation is necessary, ESP or ESPv2 validates the authentication using the appropriate public key for the signer, and validates the audience field in the JWT. If an API key is required, ESP or ESPv2 calls the Service Control API to validate the key.

Service Control looks up the key to validate it, and ensures that the project associated with the key has enabled the API. If the key isn't valid or the project hasn't enabled the API, the call is rejected and it is logged via the Service Control API.

If Service Control successfully validates the key, the request along with all original headers, plus a JWT validation header, if appropriate, is forwarded to the backend.

When a response is received from the backend, ESP or ESPv2 returns the response to the caller and sends the final timing information to Trace. The call points are logged by the Service Control API, which writes metrics and logs to their appropriate destinations.

## ESP or ESPv2 on Kubernetes

The following diagram shows the overall architecture where ESP runs as a side-car container in front of the API service application container, with `my-api` API hosted at `my-api.com` and backed by a [Kubernetes service](http://kubernetes.io/docs/user-guide/services/). The architecture would be the same for a sidecar deployment with ESPv2.

![Endpoints on Kubernetes overview](https://docs.cloud.google.com/static/endpoints/docs/images/endpoints_kube.png)

## What's next

  * [About Endpoints](https://docs.cloud.google.com/endpoints/docs/grpc/about-cloud-endpoints)
  * [gRPC documentation](https://grpc.io/docs/)
  * [Cloud Endpoints for gRPC APIs](https://docs.cloud.google.com/endpoints/docs/grpc/about-grpc)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
