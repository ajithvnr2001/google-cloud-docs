---
url: https://docs.cloud.google.com/architecture/blueprints/serverless-functions-blueprint/
title: Deploy a secured serverless architecture using Cloud Run functions \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:08.236976+00:00
---

# Deploy a secured serverless architecture using Cloud Run functions  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/serverless-functions-blueprint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Deploy a secured serverless architecture using Cloud Run functions Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2023-08-06 UTC

Serverless architectures let you develop software and services without provisioning or maintaining servers. You can use serverless architectures to build applications for a wide range of services.

This document provides opinionated guidance for DevOps engineers, security architects, and application developers on how to help protect serverless applications that use [Cloud Run functions (2nd gen)](https://docs.cloud.google.com/functions/docs/concepts/version-comparison). The document is part of a security blueprint that consists of the following:

  * A [GitHub repository](https://github.com/GoogleCloudPlatform/terraform-google-cloud-functions) that contains a set of Terraform configurations and scripts.
  * A guide to the architecture, design, and security controls that you implement with the blueprint (this document).



Though you can deploy this blueprint without deploying the [Google Cloud enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations) first, this document assumes that you've already configured a foundational set of security controls as described in the Google Cloud enterprise foundations blueprint. The architecture that's described in this document helps you to layer additional controls onto your foundation to help protect your serverless applications.

To help define key security controls that are related to serverless applications, the [Cloud Security Alliance (CSA)](https://cloudsecurityalliance.org/) published [Top 12 Critical Risks for Serverless Applications](https://cloudsecurityalliance.org/blog/2019/02/11/critical-risks-serverless-applications/). The security controls used in this blueprint are designed to address the risks that are relevant to the various use cases described in this document.

## Serverless use cases

The blueprint supports the following use cases:

  * Deploying a serverless architecture using Cloud Run functions (this document)
  * [Deploying a serverless architecture using Cloud Run](https://docs.cloud.google.com/architecture/blueprints/serverless-blueprint)



Differences between Cloud Run functions and Cloud Run include the following:

  * Cloud Run functions is triggered by events, such as changes to data in a database or the receipt of a message from a messaging system such as Pub/Sub. Cloud Run is triggered by requests, such as HTTP requests.
  * Cloud Run functions is limited to a [set of supported runtimes](https://docs.cloud.google.com/functions/docs/concepts/execution-environment#runtimes). You can use Cloud Run with any programming language.
  * Cloud Run functions manages containers and the infrastructure that controls the web server or language runtime so that you can focus on your code. Cloud Run provides the flexibility for you to run these services yourself, so that you have control of the container configuration.



For more information about differences between Cloud Run and Cloud Run functions, see [Choosing a Google Cloud compute option](https://cloud.google.com/blog/topics/developers-practitioners/where-should-i-run-my-stuff-choosing-google-cloud-compute-option).

## Architecture

This blueprint uses a [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) architecture, in which Cloud Run functions is deployed in a service project and can access resources that are located in other VPC networks.

The following diagram shows a high-level architecture, which is further described in the example architectures that follow it.

![The architecture for the serverless blueprint using Cloud Run functions.](https://docs.cloud.google.com/static/architecture/blueprints/images/serverless-blueprint/serverless-functions-architecture.svg)

The architecture that's shown in the preceding diagram uses a combination of the following Google Cloud services and features:

  * [Cloud Run functions](https://docs.cloud.google.com/functions) lets you run functions as a service and manages the infrastructure on your behalf. By default, this architecture deploys Cloud Run functions with an internal IP address only and without access to the public internet.
  * The triggering event is the event that triggers Cloud Run functions. As further described in the example architectures, this can be a Cloud Storage event, a scheduled interval, or a change in BigQuery.
  * [Artifact Registry](https://docs.cloud.google.com/artifact-registry/docs/overview) stores the source containers for your Cloud Run functions application.
  * [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc) lets you connect a Serverless VPC Access connector in your service project to the host project. You deploy a separate Shared VPC network for each environment (production, non-production, and development). This [networking design](https://docs.cloud.google.com/architecture/landing-zones/decide-network-design#option-1) provides network isolation between the different environments. A Shared VPC network lets you centrally manage network resources in a common network while delegating administrative responsibilities for the service project.
  * The Serverless VPC Access connector connects your serverless application to your VPC network using [Serverless VPC Access](https://docs.cloud.google.com/vpc/docs/serverless-vpc-access). Serverless VPC Access helps to ensure that requests from your serverless application to the VPC network aren't exposed to the internet. Serverless VPC Access lets Cloud Run functions communicate with other services, storage systems, and resources that [support VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products).

You can configure Serverless VPC Access in the Shared VPC host project or a service project. By default, this blueprint deploys Serverless VPC access in the Shared VPC host project to align with the Shared VPC model of centralizing network configuration resources. For more information, see [Comparison of configuration methods](https://docs.cloud.google.com/functions/docs/networking/connecting-shared-vpc#comparison_of_configuration_methods).

  * [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls) creates a security perimeter that isolates your Cloud Run functions services and resources by setting up authorization, access controls, and [secure data exchange](https://docs.cloud.google.com/vpc-service-controls/docs/secure-data-exchange). This perimeter is designed to isolate your application and managed services by setting up additional access controls and monitoring, and to separate your governance of Google Cloud from the application. Your governance includes key management and logging.

  * The consumer service is the application that is acted on by Cloud Run functions. The consumer service can be an internal server or another Google Cloud service such as Cloud SQL. Depending on your use case, this service might be behind Cloud Next Generation Firewall, in another subnet, in the same service project as Cloud Run functions, or in another service project.

  * [Secure Web Proxy](https://docs.cloud.google.com/secure-web-proxy/docs/overview) is designed to secure the egress web traffic, if required. It enables flexible and granular policies based on cloud identities and web applications. This blueprint uses Secure Web Proxy for granular access policies to egress web traffic during the build phase of Cloud Run functions. The blueprint adds an allowed list of URLs to the [Gateway Security Policy Rule](https://docs.cloud.google.com/secure-web-proxy/docs/reference/network-security/rest/v1/projects.locations.gatewaySecurityPolicies.rules).

  * [Cloud NAT](https://docs.cloud.google.com/nat/docs/overview) provides outbound connection to the internet, if required. Cloud NAT supports source network address translation (SNAT) for compute resources without public IP addresses. Inbound response packets use destination network address translation (DNAT). You can disable Cloud NAT if Cloud Run functions doesn't require access to the internet. Cloud NAT implements the egress network policy that is attached to Secure Web Proxy.

  * [Cloud Key Management Service (Cloud KMS)](https://docs.cloud.google.com/kms) stores the [customer-managed encryption keys (CMEKs)](https://docs.cloud.google.com/kms/docs/cmek) that are used by the services in this blueprint, including your serverless application, Artifact Registry, and Cloud Run functions.

  * [Secret Manager](https://docs.cloud.google.com/secret-manager) stores the Cloud Run functions secrets. The blueprint mounts [secrets](https://docs.cloud.google.com/functions/docs/configuring/secrets) as a volume to provide a higher level of security than passing secrets as environment variables.

  * [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam) and [Resource Manager](https://docs.cloud.google.com/resource-manager) help to restrict access and isolate resources. The access controls and resource hierarchy follow the principle of least privilege.

  * [Cloud Logging](https://docs.cloud.google.com/logging/docs) collects all the logs from Google Cloud services for storage and retrieval by your analysis and investigation tools.

  * [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) collects and stores performance information and metrics about Google Cloud services.




### Example architecture with a serverless application using Cloud Storage

The following diagram shows how you can run a serverless application that accesses an internal server when a particular event occurs in Cloud Storage.

![Example serverless architecture with Cloud Storage.](https://docs.cloud.google.com/static/architecture/blueprints/images/serverless-blueprint/serverless-functions-example1.svg)

In addition to the services described in Architecture, this example architecture uses a combination of the following Google Cloud services and features:

  * [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction) emits an event when any cloud resource, application, or user creates a web object on a bucket.
  * [Eventarc](https://docs.cloud.google.com/eventarc/docs/overview) routes events from different resources. Eventarc encrypts events in transit and at rest.
  * [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) queues events that are used as the input and a trigger for Cloud Run functions.
  * [Virtual Private Cloud (VPC) firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) control the flow of data into the subnet that hosts your resources, such as an internal server.
  * The internal server runs on Compute Engine or Google Kubernetes Engine and hosts your internal application. If you deploy the [Secure Cloud Run functions with Internal Server Example](https://github.com/GoogleCloudPlatform/terraform-google-cloud-functions/tree/main/examples/secure_cloud_function_internal_server), you deploy an Apache server with a _Hello World_ HTML page. This example simulates access to an internal application that runs VMs or containers.



### Example architecture with Cloud SQL

The following diagram shows how you can run a serverless application that accesses a Cloud SQL hosted service at a regular interval that is defined in Cloud Scheduler. You can use this architecture when you must gather logs, aggregate data, and so on.

![Example serverless architecture with Cloud SQL.](https://docs.cloud.google.com/static/architecture/blueprints/images/serverless-blueprint/serverless-functions-example2.png)

In addition to the services described in Architecture, this example architecture uses a combination of the following Google Cloud services and features:

  * [Cloud Scheduler](https://docs.cloud.google.com/scheduler/docs/overview) emits events on a regular basis.
  * [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview) queues events that are used as the input and a trigger for Cloud Run functions.
  * [Virtual Private Cloud (VPC) firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) control the flow of data into the subnet that hosts your resources, such as company data stored in Cloud SQL.
  * [Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy) controls access to Cloud SQL.
  * [Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction) hosts a service that is peered to the VPC network and that the serverless application can access. If you deploy the [Secure Cloud Run functions with Cloud SQL example](https://github.com/GoogleCloudPlatform/terraform-google-cloud-functions/tree/main/examples/secure_cloud_function_with_sql), you deploy a MySQL database with a sample database.



### Example architecture with BigQuery data warehouse

The following diagram shows how you can run a serverless application that is triggered when an event occurs in BigQuery (for example, data is added or a table is created).

![Example serverless architecture with BigQuery.](https://docs.cloud.google.com/static/architecture/blueprints/images/serverless-blueprint/serverless-functions-example3.svg)

In addition to the services described in Architecture, this example architecture uses a combination of the following Google Cloud services and features:

  * [BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction) hosts a data warehouse. If you deploy the [Secure Cloud Run functions triggered by BigQuery example](https://github.com/GoogleCloudPlatform/terraform-google-cloud-functions/tree/main/examples/secure_cloud_function_bigquery_trigger), you deploy a sample BigQuery dataset and table.
  * Eventarc triggers Cloud Run functions when a particular event occurs in BigQuery.



## Organization structure

Resource Manager lets you logically group resources by project, folder, and organization.

The following diagram shows a resource hierarchy with folders that represent different environments such as bootstrap, common, production, non-production (or testing), and development. This resource hierarchy is based on the hierarchy that's described in the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations/organization-structure). You deploy the projects that the blueprint specifies into the following folders: `Common`, `Production`, `Non-production`, and `Dev`.

![The organization structure for the serverless blueprint.](https://docs.cloud.google.com/static/architecture/blueprints/images/serverless-blueprint/serverless-functions-structure.svg)

The following sections describe this diagram in more detail.

### Folders

You use folders to isolate your production environment and governance services from your non-production and testing environments. The following table describes the folders from the enterprise foundations blueprint that are used by this blueprint.

Folder | Description  
---|---  
` Bootstrap ` | Contains resources required to deploy the enterprise foundations blueprint.  
` Common ` | Contains centralized services for the organization, such as the security project.  
` Production ` | Contains projects that have cloud resources that have been tested and are ready to be used by customers. In this blueprint, the `Production` folder contains the service project and host project.  
` Non-production ` | Contains projects that have cloud resources that are currently being tested and staged for release. In this blueprint, the `Non-production` folder contains the service project and host project.  
` Development ` | Contains projects that have cloud resources that are currently being developed. In this blueprint, the `Development` folder contains the service project and host project.  
  
You can change the names of these folders to align with your organization's folder structure, but we recommend that you maintain a similar structure. For more information, see [Organization structure](https://docs.cloud.google.com/architecture/blueprints/security-foundations/organization-structure). For other folder structures, see [Decide a resource hierarchy for your Google Cloud landing zone](https://docs.cloud.google.com/architecture/landing-zones/decide-resource-hierarchy).

### Projects

You isolate resources in your environment using [projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). The following table describes the projects that are needed within the organization. You can change the names of these projects, but we recommend that you maintain a similar project structure.

Project | Description  
---|---  
Shared VPC host project | This project includes the firewall ingress rules and any resources that have internal IP addresses (as described in [Connect to a VPC network](https://docs.cloud.google.com/functions/docs/networking/connecting-vpc)). When you use Shared VPC, you designate a project as a host project and attach one or more other service projects to it. When you apply the Terraform code, you specify the name of this project, and the blueprint deploys Serverless VPC Access connector, Cloud NAT, and Cloud Secure Web Proxy.  
Shared VPC service project | This project includes your serverless application, Cloud Run functions, and the Serverless VPC Access connector. You [attach](https://docs.cloud.google.com/vpc/docs/provisioning-shared-vpc#create-shared) the service project to the host project so that the service project can participate in the Shared VPC network. When you apply the Terraform code, you specify the name of this project. The blueprint deploys Cloud Run functions and services needed for your use case, such as Cloud SQL, Cloud Scheduler, Cloud Storage, or BigQuery. When you apply the Terraform code, you specify the name of this project, and the blueprint deploys Cloud KMS. If you use the [Secure Serverless Harness](https://github.com/GoogleCloudPlatform/terraform-google-cloud-run/tree/main/modules/secure-serverless-harness) module in the serverless blueprint for Cloud Run functions, Artifact Registry is also deployed.  
Security project | This project includes your security-specific services, such as Cloud KMS and Secret Manager. The default name of the security project is `prj-bu1-p-sec`. If you deploy this blueprint after you deploy the security foundations blueprint, the security project project is created in addition to the enterprise foundation blueprint's secrets project (`prj-bu1-p-env-secrets`). For more information about the enterprise foundations blueprint projects, see [Projects](https://docs.cloud.google.com/architecture/blueprints/security-foundations/organization-structure#projects). If you deploy multiple instances of this blueprint without the enterprise foundations blueprint, each instance has its own security project.  
  
## Mapping roles and groups to projects

You must give different user groups in your organization access to the projects that make up the serverless architecture. The following table describes the blueprint recommendations for user groups and role assignments in the projects that you create. You can customize the groups to match your organization's existing structure, but we recommend that you maintain a similar segregation of duties and role assignment.

Group | Project | Roles  
---|---|---  
Serverless administrator  
grp-gcp-serverless-admin@example.com | Service project | 

  * [Cloud Run functions Admin (`roles/cloudfunctions.admin`)](https://docs.cloud.google.com/functions/docs/reference/iam/roles#cloudfunctions.admin)
  * [Compute Network User (`roles/compute.networkUser`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser)
  * [Compute Network Viewer (`roles/compute.networkViewer`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkViewer)
  * [Cloud Run Admin (`roles/run.admin`)](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.admin)

  
Serverless security administrator  
grp-gcp-serverless-security-admin@example.com | Security project | 

  * [Artifact Registry Reader (`roles/artifactregistry.reader`)](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.reader)
  * Cloud Run functions Admin (`roles/cloudfunctions.admin`)
  * [Cloud KMS Viewer (`roles/cloudkms.viewer`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.viewer)
  * [Cloud Run Viewer (`roles/run.viewer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.viewer)

  
Cloud Run functions developer  
grp-gcp-secure-cloud-run-developer@example.com | Security project | 

  * [Artifact Registry Writer (roles/artifactregistry.writer)](https://docs.cloud.google.com/iam/docs/roles-permissions/artifactregistry#artifactregistry.writer)
  * [Cloud Run functions Developer (`roles/cloudfunctions.developer`)](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.developer)
  * [Cloud KMS CryptoKey Encrypter (`roles/cloudkms.cryptoKeyEncrypter`)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyEncrypter)

  
Cloud Run functions user  
grp-gcp-secure-cloud-run-user@example.com | Shared VPC service project | 

  * [Cloud Run functions Invoker (`roles/cloudfunctions.invoker`)](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudfunctions#cloudfunctions.invoker)

  
  
## Security controls

This section discusses the security controls in Google Cloud that you use to help secure your serverless architecture. The key security principles to consider are as follows:

  * Secure access according to the principle of least privilege, giving principals only the privileges required to perform tasks.
  * Secure network connections through trust boundary design, which includes network segmentation, organization policies, and firewall policies.
  * Secure configuration for each of the services.
  * Identify any compliance or regulatory requirements for the infrastructure that hosts serverless workloads and assign a risk level.
  * Configure sufficient monitoring and logging to support audit trails for security operations and incident management.



### Build system controls

When you deploy your serverless application, you use Artifact Registry to store the container images and binaries. Artifact Registry supports CMEK so that you can encrypt the repository using your own encryption keys.

### Network and firewall rules

[Virtual Private Cloud (VPC) firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls) control the flow of data into the perimeters. You create firewall rules that deny all egress, except for specific TCP port 443 connections from restricted.googleapis.com special domain names. Using the restricted.googleapis.com domain has the following benefits:

  * It helps to reduce your network attack surface by using Private Google Access when workloads communicate with Google APIs and services.
  * It ensures that you use only services that support VPC Service Controls.



In addition, you create a DNS record to resolve [*.googleapis.com to restricted.googleapis.com](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity#configuring-dns).

For more information, see [Configuring Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

### Perimeter controls

As shown in the Architecture section, you place the resources for the serverless application in a separate VPC Service Controls security perimeter. This perimeter helps reduce the broad impact from a compromise of systems or services. However, this security perimeter doesn't apply to the [Cloud Run functions build process](https://docs.cloud.google.com/functions/docs/building) when Cloud Build automatically builds your code into a container image and pushes that image to Artifact Registry. In this scenario, create an [ingress rule](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules) for the Cloud Build service account in the service perimeter.

### Access policy

To help ensure that only specific principals (users or services) can access resources and data, you enable IAM groups and roles.

To help ensure that only specific resources can access your projects, you enable an [access policy](https://docs.cloud.google.com/access-context-manager/docs/overview) for your Google organization. For more information, see [Access level attributes](https://docs.cloud.google.com/access-context-manager/docs/access-level-attributes).

### Service accounts and access controls

Service accounts are accounts for applications or compute workloads instead of for individual end users. To implement the principle of least privilege and the principle of separation of duties, you create service accounts with granular permissions and limited access to resources. The service accounts are as follows:

  * A Cloud Run functions service account (`cloudfunction_sa`) that has the following roles:

    * Compute Network Viewer (`roles/compute.networkViewer`)
    * [Eventarc Event Receiver (`roles/eventarc.eventReceiver`)](https://docs.cloud.google.com/iam/docs/roles-permissions/eventarc#eventarc.eventReceiver)
    * [Cloud Run Invoker (`roles/run.invoker`)](https://docs.cloud.google.com/iam/docs/roles-permissions/run#run.invoker)
    * [Secret Manager Secret Assessor (`roles/secretmanager.secretAccessor`)](https://docs.cloud.google.com/secret-manager/docs/access-control#secretmanager.secretAccessor)

For more information, see [Allow Cloud Run functions to access a secret](https://docs.cloud.google.com/functions/docs/configuring/secrets).

Cloud Run functions uses this service account to grant permission to specific Pub/Sub topics only and to restrict the Eventarc event system from Cloud Run functions compute resources in Example architecture with a serverless application using Cloud Storage and Example architecture with BigQuery data warehouse.

  * A Serverless VPC Access connector account (`gcp_sa_vpcaccess`) that has the [Compute Network User (`roles/compute.networkUser`)](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkUser) role.

  * A second Serverless VPC Access connector account (`cloud_services`) that has the Compute Network User (`roles/compute.networkUser`) role.

These service accounts for the Serverless VPC Access connector are required so that the connector can create the firewall ingress and egress rules in the host project. For more information, see [Grant permissions to service accounts in your service projects](https://docs.cloud.google.com/functions/docs/networking/shared-vpc-service-projects#grant-permissions).

  * A service identity to run Cloud Run functions (`cloudfunction_sa`) that has the [Serverless VPC Access User (`roles/vpcaccess.user)](/iam/docs/roles-permissions/vpcaccess#vpcaccess.user)` and the [Service Account User (`roles/iam.serviceAccountUser`)](https://docs.cloud.google.com/compute/docs/access/iam#iam.serviceAccountUser) roles.

  * A [service account for the Google APIs](https://docs.cloud.google.com/iam/docs/service-account-types#google-managed) (`cloud_services_sa`) that has the Compute Network User (`roles/compute.networkUser`) role to run internal Google processes on your behalf.

  * A [service identity](https://docs.cloud.google.com/run/docs/securing/service-identity) for Cloud Run functions (`cloud_serverless_sa`) that has the Artifact Registry Reader (`roles/artifactregistry.reader`) role. This service account provides access to Artifact Registry and CMEKs.

  * A service identity for Eventarc (`eventarc_sa`) that has the [Cloud KMS CryptoKey Decrypter (roles/cloudkms.cryptoKeyDecrypter)](https://docs.cloud.google.com/kms/docs/reference/permissions-and-roles#cloudkms.cryptoKeyDecrypter) and the Cloud KMS CryptoKey Encrypter (`roles/cloudkms.cryptoKeyEncrypter`) roles.

  * A service identity for Artifact Registry (`artifact_sa`) with the CryptoKey Decrypter (`roles/cloudkms.cryptoKeyDecrypter`) and the Cloud KMS CryptoKey Encrypter (`roles/cloudkms.cryptoKeyEncrypter`) roles.




### Key management

To validate integrity and help protect your data at rest, you use [CMEKs](https://docs.cloud.google.com/kms/docs/cmek) with Artifact Registry, Cloud Run functions, Cloud Storage, and Eventarc. CMEKs provides you with greater control over your encryption key. The following CMEKs are used:

  * A software key for Artifact Registry that attests the code for your serverless application.
  * An [encryption key](https://docs.cloud.google.com/functions/docs/securing/cmek) to encrypt the container images that Cloud Run functions deploys.
  * An [encryption key](https://docs.cloud.google.com/eventarc/docs/use-cmek) for Eventarc events that encrypts the messaging channel at rest.
  * An [encryption key](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys) to help protect data in Cloud Storage.



When you apply the Terraform configuration, you specify the [CMEK location](https://docs.cloud.google.com/kms/docs/locations), which determines the geographical location where the keys are stored. You must ensure that your CMEKs are in the same [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones) as your resources. By default, CMEKs are rotated every 30 days.

### Secret management

Cloud Run functions supports [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to store the secrets that your serverless application might require. These secrets can include API keys and database usernames and passwords. To expose the secret as a mounted volume, use the `service_configs` object variables in the [main module](https://github.com/GoogleCloudPlatform/terraform-google-cloud-functions).

When you deploy this blueprint with the enterprise foundations blueprint, you must add your secrets to the secrets project before you apply the Terraform code. The blueprint will grant the Secret Manager Secret Assessor (`roles/secretmanager.secretAccessor`) role to the Cloud Run functions service account. For more information, see [Using secrets](https://docs.cloud.google.com/functions/docs/configuring/secrets).

### Organization policies

This blueprint adds constraints to the [organization policy constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints) that the enterprise foundations blueprint uses. For more information about the constraints that the enterprise foundations blueprint uses, see [Organization policy constraints](https://docs.cloud.google.com/architecture/blueprints/security-foundations/preventative-controls#organization-policy).

The following table describes the additional organization policy constraints that are defined in the [Secure Cloud Run functions Security](https://github.com/GoogleCloudPlatform/terraform-google-cloud-functions/tree/main/modules/secure-cloud-function-security) module of this blueprint.

Policy constraint | Description | Recommended value  
---|---|---  
[Allowed ingress settings (Cloud Run functions) `constraints/cloudfunctions.allowedIngressSettings`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#:~:text=cloudfunctions.allowedIngressSettings) | Allow ingress traffic only from internal services or the external HTTP(S) load balancer. The default is `ALLOW_ALL`. | ` ALLOW_INTERNAL_ONLY `  
[Require VPC Connector (Cloud Run functions) `constraints/cloudfunctions.requireVPCConnector`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#:~:text=cloudfunctions.requireVPCConnector) | Require specifying a Serverless VPC Access connector when deploying a function. When this constraint is enforced, functions must specify a Serverless VPC Access connector. The default is `false`. | `true `  
[Allowed VPC Connector egress settings (Cloud Run functions) `cloudfunctions.allowedVpcConnectorEgressSettings`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/org-policy-constraints#:~:text=cloudfunctions.allowedVpcConnectorEgressSettings) | Require all egress traffic for Cloud Run functions to use a Serverless VPC Access connector. The default is `PRIVATE_RANGES_ONLY`. | ` ALL_TRAFFIC `  
  
## Operational controls

You can enable logging and [Security Command Center Premium tier features](https://cloud.google.com/security-command-center/pricing#premium-tier) such as security health analytics and threat detection. These controls help you to do the following:

  * Monitor data access.
  * Ensure that proper auditing is in place.
  * Support security operations and incident management capabilities of your organization.



#### Logging

To help you meet auditing requirements and get insight into your projects, you configure the [Google Cloud Observability](https://cloud.google.com/products/operations) with data logs for the services that you want to track. Deploy [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) in the projects before you apply the Terraform code to ensure that the blueprint can configure logging for the firewall, load balancer, and VPC network.

After you deploy the blueprint, we recommend that you configure the following:

  * [Create an aggregated log sink](https://docs.cloud.google.com/logging/docs/export/aggregated_sinks) across all projects.
  * Add CMEKs to your logging sink.



For all services within the projects, ensure that your logs include information about data writes and administrative access. For more information about logging best practices, see [Detective controls](https://docs.cloud.google.com/architecture/blueprints/security-foundations/detective-controls).

#### Monitoring and alerts

After you deploy the blueprint, you can set up alerts to notify your security operations center (SOC) that a security event has occurred. For example, you can use alerts to let your security analysts know when a permission was changed on an IAM role. For more information about configuring Security Command Center alerts, see [Setting up finding notifications](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications).

The [Cloud Run functions Monitoring dashboard](https://github.com/GoogleCloudPlatform/monitoring-dashboard-samples/tree/master/dashboards/google-cloud-functions) helps you to monitor the performance and health of your Cloud Run functions. It provides a variety of metrics and logs, which you can use to identify and troubleshoot problems. The dashboard also includes a number of features that can help you to improve the performance of your functions, such as the ability to set alerts and quotas.

For more information, see [Monitoring Cloud Run functions](https://docs.cloud.google.com/functions/docs/monitoring).

To export alerts, see the following documents:

  * [Introduction to alerting](https://docs.cloud.google.com/monitoring/alerts)
  * [Cloud Monitoring metric export](https://docs.cloud.google.com/architecture/monitoring-metric-export)



#### Debugging and troubleshooting

You can run [Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/concepts/overview) to help you debug network configuration issues between Cloud Run functions and the resources within your subnet. Connectivity Tests simulates the expected path of a packet and provides details about the connectivity, including resource-to-resource connectivity analysis.

Connectivity Tests isn't enabled by the Terraform code; you must set it up separately. For more information, see [Create and run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/connectivity-tests/how-to/running-connectivity-tests).

## Terraform deployment modes

The following table describes the ways that you can deploy this blueprint, and which Terraform modules apply for each deployment mode.

Deployment mode | Terraform modules  
---|---  
Deploy this blueprint after deploying the enterprise foundations blueprint (recommended). This option deploys the resources for this blueprint in the same VPC Service Controls perimeter that is used by the enterprise foundations blueprint. For more information, see [How to customize Foundation v3.0.0 for Secure Cloud Run functions deployment](https://github.com/GoogleCloudPlatform/terraform-google-cloud-functions/blob/main/docs/secure-cloud-function-on-foundation-3-0-0.md). This option also uses the secrets project that you created when you deployed the enterprise foundations blueprint. |  Use these Terraform modules: 

  * [`secure-cloud-function-core`](https://github.com/GoogleCloudPlatform/terraform-google-cloud-functions/tree/main/modules/secure-cloud-function-core)
  * [`secure-serverless-net`](https://github.com/GoogleCloudPlatform/terraform-google-cloud-run/tree/main/modules/secure-serverless-net)
  * [`secure-web-proxy`](https://github.com/GoogleCloudPlatform/terraform-google-cloud-functions/tree/main/modules/secure-web-proxy)

  
Install this blueprint without installing the security foundations blueprint. This option requires that you create a VPC Service Controls perimeter. | Use these Terraform modules: 

  * `secure-cloud-function-core`
  * [`secure-serverless-harness`](https://github.com/GoogleCloudPlatform/terraform-google-cloud-run/tree/main/modules/secure-serverless-harness)
  * `secure-serverless-net`
  * [`secure-cloud-function-security`](https://github.com/GoogleCloudPlatform/terraform-google-cloud-functions/tree/main/modules/secure-cloud-function-security)
  * `secure-web-proxy`
  * [`secure-cloud-function`](https://github.com/GoogleCloudPlatform/terraform-google-cloud-functions/tree/main/modules/secure-cloud-function)

  
  
## Bringing it all together

To implement the architecture described in this document, do the following:

  1. Review the [README](https://github.com/GoogleCloudPlatform/terraform-google-cloud-functions) for the blueprint to ensure that you meet all the prerequisites.
  2. In your testing environment, to see the blueprint in action, deploy one of the [examples](https://github.com/GoogleCloudPlatform/terraform-google-cloud-functions/tree/main/examples/). These examples match the architecture examples described in Architecture. As part of your testing process, consider doing the following: 
     1. Use Security Command Center to scan the projects against common [compliance requirements](https://docs.cloud.google.com/security-command-center/docs/concepts-vulnerabilities-findings).
     2. Replace the sample application with a real application (for example 1) and run through a typical deployment scenario.
     3. Work with the application engineering and operations teams in your enterprise to test their access to the projects and to verify whether they can interact with the solution in the way that they would expect.
  3. Deploy the blueprint into your environment.



## What's next

  * Review the [Google Cloud enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations) for a baseline secure environment.
  * To see the details of the blueprint, read the [Terraform configuration README](https://github.com/GoogleCloudPlatform/terraform-google-cloud-functions).
  * To deploy a serverless application using Cloud Run, see [Deploy a secured serverless architecture using Cloud Run](https://docs.cloud.google.com/architecture/blueprints/serverless-blueprint).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2023-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2023-08-06 UTC."],[],[]] 
