---
url: https://docs.cloud.google.com/run/docs/integrate/using-gcp-services/
title: Connect to Google Cloud services \u00a0|\u00a0 Cloud Run \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:01:38.239250+00:00
---

# Connect to Google Cloud services  |  Cloud Run  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/run/docs/integrate/using-gcp-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Cloud Run ](https://docs.cloud.google.com/run/docs)
  * [ Guides ](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run)



Send feedback 

#  Connect to Google Cloud services Stay organized with collections  Save and categorize content based on your preferences. 

Integrating Cloud Run with other Google Cloud services lets you extend your containerized applications to persist data, manage secrets, and handle asynchronous workloads. This document identifies the Google Cloud services recommended for use with Cloud Run and highlights services that are not yet supported.

## Connect to Google Cloud services in code

You can connect your Cloud Run service to Google Cloud services by using the client libraries they provide. For code samples showing how to connect with a particular Google Cloud service, refer to the documentation provided for that Google Cloud service.

To call Google Cloud APIs from your code, the [Cloud Run service identity](https://docs.cloud.google.com/run/docs/securing/service-identity) must have the minimal set of permissions to your Cloud Run services. For example, if your Cloud Run service is only reading data from Firestore, we recommend assigning it a service account that only has the _Firestore User_ IAM role.

The Google Cloud environment uses Application Default Credentials (ADC) to automatically detect whether the Cloud Run service identity is authenticated to use the Google Cloud client libraries and perform the API operation.

## Services and tools recommended for use

The following table lists services recommended for Cloud Run.

### Tools

Service | Description  
---|---  
[Cloud Build](https://cloud.google.com/build) | Build container images and continuous integration.  
[Artifact Registry](https://docs.cloud.google.com/artifact-registry) | Store container images.  
[Cloud Deploy](https://docs.cloud.google.com/deploy) | Continuous delivery.  
[Google Cloud Observability](https://cloud.google.com/products/observability) | [Monitoring](https://docs.cloud.google.com/run/docs/monitoring) and [logging](https://docs.cloud.google.com/run/docs/logging) of Cloud Run services.  
  
### Data storage

Service | Description  
---|---  
[Firestore](https://cloud.google.com/products/firestore) | Fully managed NoSQL database, with [MongoDB compatibility](https://docs.cloud.google.com/firestore/mongodb-compatibility/docs/overview).  
[Spanner](https://cloud.google.com/spanner) | Fully managed, scalable, relational database.  
[Cloud SQL](https://cloud.google.com/sql) | Fully managed relational database. Refer to [Connecting to Cloud SQL instances](https://docs.cloud.google.com/run/docs/configuring/connect-cloudsql).  
[Cloud Storage](https://cloud.google.com/storage) | Object storage. Store objects and serve static content. Use [Cloud Storage client libraries](https://docs.cloud.google.com/storage/docs/reference/libraries) or [mount Cloud Storage volumes](https://docs.cloud.google.com/run/docs/configuring/services/cloud-storage-volume-mounts)  
[Memorystore](https://cloud.google.com/memorystore) | Fully managed in-memory datastore service. Connect to your VPC network to access Memorystore instances. Refer to [Connecting to a Redis instance from a Cloud Run service](https://docs.cloud.google.com/memorystore/docs/redis/connect-redis-instance-cloud-run).  
[BigQuery](https://cloud.google.com/bigquery) | Fully managed cloud data warehouse for analytics. Cloud Run services can be used to implement custom [BigQuery remote functions](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/remote-functions).  
[Secret Manager](https://docs.cloud.google.com/secret-manager) | Create and access secrets or any other configuration.  
[Filestore](https://cloud.google.com/filestore) | [Fully managed NFS file servers on Google Cloud](https://docs.cloud.google.com/run/docs/tutorials/network-filesystems-filestore)  
[Parameter Manager](https://docs.cloud.google.com/secret-manager/parameter-manager/docs) | Create and access configuration files or parameters.  
  
### Orchestration

Service | Description  
---|---  
[Pub/Sub](https://cloud.google.com/pubsub) | Push events to Cloud Run services. Refer to the [Using Pub/Sub with Cloud Run Tutorial](https://docs.cloud.google.com/run/docs/tutorials/pubsub).  
[Cloud Scheduler](https://docs.cloud.google.com/scheduler) | Trigger Cloud Run services on a schedule.  
[Cloud Tasks](https://docs.cloud.google.com/tasks) | Execute asynchronous tasks on Cloud Run. Refer to [HTTP Target tasks with authentication tokens](https://docs.cloud.google.com/tasks/docs/creating-http-target-tasks#http_target_tasks_with_authentication_tokens).  
[Workflows](https://cloud.google.com/workflows) | Orchestrate and automate Cloud Run services.  
  
### Web-apps

Service | Description  
---|---  
[Identity Platform](https://docs.cloud.google.com/identity-cp) | Login your users.  
[Firebase App Hosting](https://firebase.google.com/docs/app-hosting/product-comparison) | Fully managed hosting service for dynamic content with cost-effective CDN caching. Suitable for hosting full-stack web applications built with modern, server-rendered frameworks like Angular and Next.js.  
[Firebase Hosting](https://firebase.google.com/docs/hosting/) | Managed service that hosts static content, dynamic content, and microservices using a global content delivery network (CDN) for fast, reliable delivery. Suitable for hosting static websites or single-page applications.  
  
### Networking

Service | Description  
---|---  
[Virtual Private Cloud](https://cloud.google.com/vpc) | Managed networking functionality for your Google Cloud resources. Refer to [Connecting to a VPC network](https://docs.cloud.google.com/run/docs/configuring/connecting-vpc).  
[External Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/https) | Use [serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) to configure a Cloud Run backend for an external Application Load Balancer.  
[Internal Application Load Balancer](https://docs.cloud.google.com/load-balancing/docs/l7-internal/setting-up-l7-internal-serverless) | Use [serverless NEGs](https://docs.cloud.google.com/load-balancing/docs/negs/serverless-neg-concepts) to run your Cloud Run services behind an internal IP address.  
[Google Cloud Armor](https://cloud.google.com/security/products/armor) | Helps protect your applications and websites against denial of service and web attacks.  
[Cloud CDN](https://cloud.google.com/cdn) | [Cloud CDN is supported with external Application Load Balancers](https://docs.cloud.google.com/cdn/docs/overview).  
  
### Security

Service | Description  
---|---  
[Identity-Aware Proxy](https://docs.cloud.google.com/iap) | Use [identity and context to guard access to your services](https://docs.cloud.google.com/iap/docs/enabling-cloud-run).  
[Binary Authorization](https://docs.cloud.google.com/binary-authorization) | Deploy only container images that you trust.  
[Cloud Run Threat Detection](https://docs.cloud.google.com/security-command-center/docs/use-cloud-run-threat-detection) | Detects threats in running containers.  
  
## Services not yet supported

The following table lists services that are not yet supported by Cloud Run.

Service | Notes  
---|---  
[Web Security Scanner](https://docs.cloud.google.com/security-command-center/docs/concepts-web-security-scanner-overview) |   
  
## Simplify use of Google Cloud services and resources using App Hub

Optionally, you can use App Hub to build, operate, and manage applications that include multiple resources from one or more Google Cloud projects.

You can use App Hub to organize your Cloud Run resources in an application-centric way based on your changing business needs. To track and organize your Cloud Run resources, add your resources as services and workloads to App Hub applications. App Hub is fully managed by Google Cloud and doesn't require you to install any additional infrastructure. For more information on: 

  * Resources that App Hub supports, see [Supported resources](https://docs.cloud.google.com/app-hub/docs/supported-resources).
  * How to set up App Hub on your project and register your resources with an App Hub application, see [Set up App Hub](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
