---
url: https://docs.cloud.google.com/migrate/kf/docs/2.11/concepts/cloud-sb-overview/
title: Kf Cloud Service Broker \u00a0|\u00a0 Kf 2.11 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:36:59.701176+00:00
---

# Kf Cloud Service Broker  |  Kf 2.11  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.11/concepts/cloud-sb-overview/

Version 2.11 - Latest version

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.11 ](https://docs.cloud.google.com/migrate/kf/docs/2.11)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.11/getting-started)



Send feedback 

#  Kf Cloud Service Broker Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Kf Cloud Service Broker for Google Cloud is a supported component of Kf.

Kf Cloud Service Broker is a Service Broker bundle that includes the open source [Cloud Service Broker](https://github.com/cloudfoundry-incubator/cloud-service-broker) and [Google Cloud Brokerpak](https://github.com/cloudfoundry-incubator/csb-brokerpak-gcp). It is made available as a public Docker image and ready to deploy as a Kubernetes service in Kf clusters. Once the Kf Cloud Service Broker service is deployed in a cluster, developers can provision Google Cloud backing services through the Kf Cloud Service Broker service, and bind the backing services to Kf Apps.

**Note:** Kf Cloud Service Broker is not currently customizable, and the default Google Cloud Brokerpak is included. If you would like to use an unsupported custom Brokerpak, you can follow the steps in the [open source Cloud Service Broker Google Cloud installation guide](https://github.com/cloudfoundry/csb-brokerpak-gcp/blob/main/docs/installation.md).

## Requirements

  * Kf Cloud Service Broker requires a [Cloud SQL for MySQL](https://docs.cloud.google.com/sql) instance and a service account for accessing the Cloud SQL for MySQL instance and Google Cloud backing services to be provisioned. Connection from the Kf Cloud Service Broker to the Cloud SQL for MySQL instance goes through the [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy).
  * Requests to access Google Cloud services (for example: [Cloud SQL for MySQL](https://docs.cloud.google.com/sql) or [Memorystore](https://docs.cloud.google.com/memorystore)) are authenticated via [Workload Identity](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity).



## Override Brokerpak defaults

Brokerpaks are essentially a Terraform plan and related dependencies in a tar file. You can inspect the Terraform plans to see what the defaults are, and then you can tell Kf Cloud Service Broker to override them when creating new services.

For example, the [Terraform configuration for Cloud SQL for MySQL](https://github.com/cloudfoundry/csb-brokerpak-gcp/blob/main/terraform/cloudsql/mysql/provision/data.tf) includes a variable called `authorized_network`. If not overridden, the `default` VPC will be used. If you'd like to override the default, you can pass that during service creation. Here are some examples:

  1. Override the compute region `config`.
         
         kf create-service csb-google-postgres small spring-music-postgres-db -c '{"config":"YOUR_COMPUTE_REGION"}'

  2. Override the `authorized_network` and compute region `config`.
         
         kf create-service csb-google-postgres small spring-music-postgres-db -c '{"config":"YOUR_COMPUTE_REGION","authorized_network":"YOUR_CUSTOM_VPC_NAME"}'




## Architecture

The following Kf Cloud Service Broker architecture shows how instances are created.

[ ![Kf Kf Cloud Service Broker architecture](https://docs.cloud.google.com/migrate/kf/docs/2.11/images/kf-csb-architecture.svg)](https://docs.cloud.google.com/static/migrate/kf/docs/images/kf-csb-architecture.svg)

  * The Kf Cloud Service Broker (CSB) is installed in its own namespace.
  * On installation, a Cloud SQL for MySQL instance must be provided to persist business logic used by Kf Cloud Service Broker. Requests are sent securely from the Kf Cloud Service Broker pod to the Cloud SQL for MySQL instance via the Cloud SQL for MySQL Auth Proxy.
  * On service provisioning, a Kf Service custom resource is created. The reconciler of the Kf Service provisions Google Cloud backing services using the Open Service Broker API.
  * When a request to provision/deprovision backing resources is received, Kf Cloud Service Broker sends resource creation/deletion requests to the corresponding Google Cloud service, and these requests are authenticated with Workload Identity. It also persists the business logics (e.g. mapping of Kf services to backing services, service bindings) to the Cloud SQL for MySQL instance.
  * On backing service creation success, the backing service is bound to an App via [VCAP_SERVICES](https://docs.cloud.google.com/migrate/kf/docs/2.11/how-to/app-runtime#vcapservices).



## What's next?

  * [Deploy Kf Cloud Service Broker](https://docs.cloud.google.com/migrate/kf/docs/2.11/how-to/deploying-cloud-sb).
  * [Learn how to list and provision services](https://docs.cloud.google.com/migrate/kf/docs/2.11/how-to/managed-services).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
