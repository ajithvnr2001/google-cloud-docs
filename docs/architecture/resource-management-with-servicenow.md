---
url: https://docs.cloud.google.com/architecture/resource-management-with-servicenow/
title: Reference architecture: Resource management with ServiceNow \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:38:01.495787+00:00
---

# Reference architecture: Resource management with ServiceNow  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/resource-management-with-servicenow/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Reference architecture: Resource management with ServiceNow Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-05-08 UTC

This document discusses architecture patterns for how to find and collect information about assets in Google Cloud, in other cloud platforms, and on-premises by using ServiceNow cloud discovery. The document is intended for architecture teams or cloud operations teams that are familiar with IT operations management (ITOM); Information technology infrastructure library (ITIL); Google Cloud services such as Compute Engine, Google Kubernetes Engine (GKE), and Cloud Asset Inventory; and ServiceNow Cloud Discovery.

## Overview

Many large enterprises use a hybrid IT infrastructure deployment that combines Google Cloud, other cloud platforms, and on-premises infrastructure. Such a hybrid deployment is typically the initial iteration in a cloud migration strategy. IT departments in these enterprises are required to discover and keep track of all the assets in their technical ecosystem, which can potentially number in the millions. The IT departments must construct a configuration management system that ties these assets together with the technical services that the assets provide. This system must also monitor the assets and services in a way that supports IT operations management (ITOM) and IT service management (ITSM) best practices.

For Google Cloud customers, a common architecture uses ServiceNow [cloud resource discovery](https://docs.servicenow.com/bundle/tokyo-it-operations-management/page/product/discovery/reference/cloud-discovery-collected-data.html) to find and collect information about assets in Google Cloud, in other cloud platforms, and on-premises. ServiceNow offers a wide range of tools for automating resource-management IT workflows across multiple cloud providers. Tools such as [Cloud Operations Workspace](https://docs.servicenow.com/bundle/tokyo-it-operations-management/page/product/cloud-operations-workspace/reference/cow-landing-page.html) let IT departments create multi-cloud resource dashboards and manage complex configurations through a unified interface (sometimes called a _single pane of glass_). This document presents a set of architecture patterns for this scenario, an overview of its high-level components, and a discussion of general design considerations.

### ServiceNow components for this architecture

The ServiceNow platform components in these architecture patterns include the following:

  * A ServiceNow instance that contains a [configuration management database (CMDB)](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/resource-center/data-sheet/ds-configuration-management.pdf) of configuration items (CIs). Each CI represents components in your operational environment that are involved in the delivery of digital services. A CI has multiple attributes that contain specific metadata about the component and its [relationships to other CIs](https://docs.servicenow.com/en-US/bundle/tokyo-servicenow-platform/page/product/configuration-management/concept/c_CIRelationships.html).
  * One or more [ServiceNow Management, Instrumentation, and Discovery (MID) Servers](https://docs.servicenow.com/bundle/tokyo-servicenow-platform/page/product/mid-server/concept/mid-server-landing.html), running in your Google Cloud project. MID Servers collect the metadata for CIs and store it in the CMDB.



These architecture patterns define some common practices for importing Google [Cloud Asset Inventory](https://docs.cloud.google.com/asset-inventory/docs/overview) data into ServiceNow's [Google Cloud Platform asset inventory discovery](https://docs.servicenow.com/bundle/tokyo-it-operations-management/page/product/service-mapping/reference/gcp-resource-inventory-discovery.html).

## Architecture patterns for Google Cloud integration

This document discusses the following architecture patterns for integrating Google Cloud into ServiceNow:

  * Google Cloud discovery pattern

  * Google Cloud agentless IP discovery pattern

  * Google Cloud discovery with Agent Client Collector pattern




These example architecture patterns are designed for a hybrid deployment that includes some infrastructure in Google Cloud and some in the ServiceNow cloud. They demonstrate how ServiceNow operates in Google Cloud between Google-managed infrastructure and customer-managed infrastructure. ServiceNow MID Servers query all Google-managed infrastructure by calling Google [Cloud APIs](https://docs.cloud.google.com/apis/docs/overview). For more information about which APIs are called, see [Google Cloud Platform APIs used by ITOM applications](https://docs.servicenow.com/bundle/tokyo-it-operations-management/page/product/it-operations-management/reference/apis-google-cloud.html).

In each of the following patterns, the architecture components work together in the [Google Cloud Platform asset inventory discovery process](https://docs.servicenow.com/bundle/tokyo-it-operations-management/page/product/service-mapping/reference/gcp-resource-inventory-discovery.html) to collect the cloud asset inventory information required by the ServiceNow Discovery application and related tools.

### Google Cloud discovery pattern

The basic ServiceNow cloud discovery architecture pattern uses ServiceNow MID Servers to call Google Cloud Asset Inventory and other Google Cloud APIs to gather data about resources such as the following:

  * VM instances
  * Tags (keys/values)
  * Storage volumes and storage mapping
  * Data center resources, including hardware types
  * Cloud networks, subnets, and gateways
  * Images
  * Cloud load balancers and availability zones
  * Cloud databases and database clusters
  * Containers (GKE)
  * Service mapping based on resource labels



In this pattern, the MID Servers don't need credentials, because they don't log into the VMs to collect data. This limits the ability of the discovery process to gather additional information. But it imposes less operational cost, because it removes the need to manage and rotate MID Server credentials.

The following diagram illustrates this architecture pattern.

![Diagram that shows the Google Cloud discovery architecture pattern.](https://docs.cloud.google.com/static/architecture/images/resource-management-with-servicenow-1.svg)

The Google Cloud portion of this pattern consists of the following:

  * One Google Cloud project (Service Project A in the diagram), which consists of two Google Cloud load balancers, one or more VM instances, a GKE instance, and one or more ServiceNow MID Servers. Each MID Server runs in its own VM.
  * A second Google Cloud project (Service Project B in the diagram), which consists of MID Servers running in their own VMs.
  * A third Google Cloud project (Host Project C in the diagram), which consists of the partner interconnect.
  * Additional managed services, such as Cloud APIs, BigQuery, and Cloud Storage.
  * Network routes that are set up from the MID Servers to the Google Cloud APIs.



The ServiceNow portion consists of the ServiceNow instance, which captures the metadata from the MID Servers and stores it in the CMDB.

### Google Cloud agentless IP-based discovery pattern

This architecture pattern adds [IP-based discovery](https://docs.servicenow.com/en-US/bundle/tokyo-it-operations-management/page/product/discovery/concept/cloud-discovery-wizard.html) to the basic cloud discovery pattern by using a batch job and a Google Cloud [service account](https://docs.cloud.google.com/iam/docs/service-accounts) to log into VMs and gather additional details. This pattern requires more of an operational burden to manage the MID Server than with the basic pattern, because it requires you to manage and rotate the MID Server credentials. However, it expands the discovery process beyond the data provided by Cloud Asset Inventory to include additional data, such as the following:

  * OS credential management and security
  * Enhanced discovery, such as [file-based discovery](https://docs.servicenow.com/en-US/bundle/tokyo-it-operations-management/page/product/discovery/concept/file-based-discovery.html) and discovery of licenses
  * OS details
  * Running processes
  * TCP connections
  * Installed software



In this architecture pattern, one or more ServiceNow MID Servers are located in Google Cloud, while the ServiceNow instance is hosted in the ServiceNow cloud platform. The MID Servers are connected to the ServiceNow instance through the [MID Server External Communication Channel (ECC) Queue](https://docs.servicenow.com/bundle/tokyo-servicenow-platform/page/product/mid-server/concept/ecc-queue-mid-server.html) (not shown). This architecture is shown in the following diagram.

![Diagram that shows the Google Cloud agentless IP-based discovery pattern.](https://docs.cloud.google.com/static/architecture/images/resource-management-with-servicenow-2.svg)

The Google Cloud portion of this pattern consists of the following:

  * Service Project A, which consists of two Google Cloud load balancers, one or more VMs, a GKE instance, and one or more ServiceNow MID Servers. Each MID Server runs in its own VM.
  * Service Project B, which consists of MID Servers that run in their own VMs.
  * Host Project C, which consists of the partner interconnect.
  * Additional managed services, such as Cloud APIs, BigQuery, and Cloud Storage.
  * ServiceNow Kubernetes Discovery deployed on the GKE infrastructure.
  * Network routes that are set up from the MID Servers to the Google Cloud APIs.
  * Service accounts that enable MID Servers to log into any Google Cloud VMs that require serverless IP address discovery.
  * Network routes that are set up from the MID Servers to any Google Cloud VMs that require serverless IP address discovery.



The ServiceNow portion consists of the ServiceNow instance, which captures the metadata from the MID Servers and stores it in the CMDB.

### Google Cloud discovery with Agent Client Collector pattern

This architecture pattern includes the following:

  * The initial cloud discovery.
  * One or more MID Servers.
  * An additional ServiceNow agent, the [Agent Client Collector](https://docs.servicenow.com/en-US/bundle/tokyo-it-operations-management/page/product/agent-client-collector/concept/acc-landing-page.html), which you install on your VMs. These agents connect directly to the MID Servers and relay the following additional information to ServiceNow:

    * Near real-time push-based discovery
    * Software metering
    * Live CI view
    * Workflow automation to servers



The following diagram illustrates this architecture pattern.

![Diagram that shows the Google Cloud discovery with Agent Client Collector pattern.](https://docs.cloud.google.com/static/architecture/images/resource-management-with-servicenow-3.svg)

The Google Cloud portion of this pattern consists of the following:

  * Service Project A, which consists of two Google Cloud load balancers, one or more VM instances, a GKE instance, and one or more ServiceNow MID Servers. Each MID Server runs in its own VM.
  * Service Project B, which consists of MID Servers running in their own VMs.
  * Host Project C, which consists of the partner interconnect.
  * ServiceNow Kubernetes Discovery deployed on the GKE infrastructure.
  * Additional managed services, such as Cloud APIs, BigQuery, and Cloud Storage.
  * Network routes that are set up from the MID Servers to the Google Cloud APIs.
  * Network routes that are set up from the MID Servers to Google Cloud VMs that have ServiceNow Discovery Agents installed.



The ServiceNow portion consists of the following:

  * The ServiceNow instance, which captures the metadata from the MID Servers and stores it in the CMDB.
  * ServiceNow discovery agents that are installed on customer-managed Google Cloud VMs.



## Cloud asset discovery workflow

The following sections discuss the workflow for Google Cloud asset discovery. This workflow applies to all three of the architecture patterns described in this document.

### Install and configure ServiceNow components

  1. Enable the Cloud Asset Inventory APIs.
  2. Install Agent Client Collector on your VMs. For more information, see [Agent Client Collector installation](https://docs.servicenow.com/en-US/bundle/tokyo-it-operations-management/page/product/agent-client-collector/concept/acc-installation.html).
  3. [Allocate resources for computers that host the MID Servers](https://docs.servicenow.com/en-US/bundle/tokyo-servicenow-platform/page/product/mid-server/reference/r_MIDServerSystemRequirements.html).
  4. [Configure firewall rules](https://docs.cloud.google.com/vpc/docs/using-firewalls) to allow connections on port 443 between your VM instance and the computers that host the MID Servers.
  5. [Configure MID Server network connectivity](https://docs.servicenow.com/bundle/tokyo-servicenow-platform/page/product/mid-server/task/t_ConfigMIDSvrConnecPrereq.html).
  6. [Install the MID Servers](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0535145).
  7. Configure the MID Servers to [call the relevant Google Cloud APIs](https://docs.servicenow.com/bundle/tokyo-it-operations-management/page/product/service-mapping/reference/gcp-resource-inventory-discovery.html). Make sure that the MID Servers have a valid network route to call Google Cloud APIs.



### Workflow

  1. Cloud Asset Inventory compiles a database of all [supported asset types](https://docs.cloud.google.com/asset-inventory/docs/supported-asset-types) in the Google Cloud environment. ServiceNow uses Cloud Asset Inventory as the source to retrieve additional information to update the CMDB.
  2. The ServiceNow MID Servers query the Cloud Asset Inventory database for information about all of the assets in the Google Cloud environment.
  3. The MID Servers store the cloud asset information in a Cloud Storage bucket.
  4. Not all required information can be obtained from the Cloud Asset Inventory database. In the agentless pattern, the VM information doesn't include the current OS patch version. For this level of detail, the MID Servers perform a [deep discovery](https://docs.servicenow.com/en-US/bundle/tokyo-release-notes/page/product/discovery/task/select-cloud-provider-vms.html) by doing the following: 
     1. The MID Servers create a batch job based on the IP addresses of the VMs that require a deep discovery.
     2. In the batch job, the MID Servers log into each VM and query the OS for patch versioning and other information.
  5. If Agent Client Collectors are installed, the data that they capture is transmitted to the MID Servers directly, rather than stored in the Cloud Asset Inventory database. For more information, see [Networking Preparation](https://docs.servicenow.com/en-US/bundle/rome-it-operations-management/page/product/mid-server/concept/c_MIDServerConnectionPrerequisites.html) and [MID Server Configuration](https://docs.servicenow.com/en-US/bundle/tokyo-it-operations-management/page/product/mid-server/task/t_ConfigMIDSvrConnecPrereq.html).
  6. After collecting the asset discovery data, the MID Servers store it into the CMDB as follows: 
     1. The MID Servers create CIs in the CMDB to represent the operational capability provided by each asset.
     2. The MID Servers automatically discover labels from Google Cloud and store them in the CMDB. These labels are mapped to the CIs automatically and are useful for creating [service maps](https://docs.servicenow.com/bundle/tokyo-it-operations-management/page/product/service-mapping/concept/tag-based-mapping.html).



The workflow process should be repeated periodically as needed. Depending on the scale and configuration of your deployment, you might choose event-based or schedule-based discovery. For more information, see "Managing the CI lifecycle" in [CMDB Design Guidance](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/resource-center/white-paper/wp-cmdb-design-guidance.pdf).

## Design considerations

The following sections provide design guidance for implementing any of the architecture patterns that are described in this document.

### Location of the ServiceNow instance

For most use cases, we recommend deploying the MID Servers in Google Cloud. That way the instances are close to the cloud assets on which they perform deep discovery.

The architecture patterns in this document assume that your CMDB stores discovery data for all your cloud resources and for all on-premises resources, not just your Google Cloud assets. The CMDB can be located in the ServiceNow cloud, in Google Cloud, or on-premises. The ultimate decision about where to locate the CMDB in your environment depends on your specific requirements.

### Deciding to use MID Server agents

Another design consideration is whether to use MID Server agents and service accounts. If your discovery process needs to collect information beyond the metadata that Cloud Asset Inventory provides, you need to use a MID Server infrastructure with service accounts, or alternatively, a MID Server with [Agent Client Collector](https://docs.servicenow.com/en-US/bundle/tokyo-it-operations-management/page/product/agent-client-collector/concept/acc-landing-page.html). Either approach can affect your operational support cost, which you must consider in your design. The approach that you should use depends on what data you need to capture and how you will use the data. The operational cost of capturing the data might outweigh the value that the data provides.

### Multi-region support for MID Servers

If your company requires multi-region support of the MID Server infrastructure, you should plan to deploy each MID Server in at least two availability zones and replicate it into another [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).

### Cost implications

When you choose where to deploy the ServiceNow components for Google Cloud asset discovery, you need to consider egress cost and compute cost.

#### Egress cost

[Egress charges](https://docs.cloud.google.com/vpc/network-pricing#internet_egress) are incurred whenever data moves out of Google Cloud. For this reason, you should analyze the egress cost for your use case to determine the best option for locating your ServiceNow components. Typically, MID Servers that perform deep discovery incur lower egress costs if they are running in Google Cloud than if they run on another cloud or on-premises.

#### Compute cost

ServiceNow components that run in Google Cloud incur compute costs that you should analyze to determine the best value for your company.

For example, you should consider the number of MID Servers that you deploy in Google Cloud Compute Engine instances. Deploying more MID Servers makes the asset discovery process go faster. But doing so increases compute cost, because each MID Server is deployed in its own VM instance. For more information about whether to deploy one or multiple MID Servers, see [Install multiple MID Servers on a single system](https://docs.servicenow.com/en-US/bundle/tokyo-servicenow-platform/page/product/mid-server/task/t_InstallMultplMIDSvrOnASingleSys.html).

### Operational supportability considerations

Your deployment likely includes network security controls such as firewalls, intrusion protection systems, intrusion detection systems, and packet mirroring infrastructure. If there are extensive network security controls in place between Google Cloud and the environment where the MID Servers are deployed, these controls can create operational supportability issues. To avoid these issues, we recommend that you host the MID Servers in Google Cloud or as close as possible to the Google Cloud infrastructure that a deep discovery will query against.

### Securing MID Servers

We recommend the following security practices for your MID Server instances:

  * Make sure that the MID Servers are [isolated to help ensure that only trusted administrators can connect to them](https://cloud.google.com/blog/products/identity-security/preventing-lateral-movement-in-google-compute-engine).
  * Make sure that the [MID Servers are protected from deletion](https://docs.servicenow.com/bundle/tokyo-platform-security/page/administer/security/reference/mid-server-secure-deployment-guide.html).
  * Make sure that IAM roles are applied to limit the capability for changes to only those changes that are approved through ITIL processes or through a CI/CD pipeline.



### Securing service accounts

We recommend the following security practices for managing service accounts:

  * Make sure that the MID Servers use a service account that has only the IAM roles and permissions that are absolutely necessary for asset discovery. For more information, see [Best practices for working with service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).
  * [ServiceNow authentication](https://docs.servicenow.com/bundle/washingtondc-it-operations-management/page/product/cloud-management-v2-setup/task/gcp-first-cld-and-srvc-accts.html) requires copying the content of a service account key into the ServiceNow user interface. Service account keys are a security risk if not managed correctly. You are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 




### Folder and project structure

Folders and projects are nodes in the Google Cloud resource hierarchy. To support asset discovery, your folder and project structure should reflect the structure of your application and of the environments where the application is deployed. Structuring your resources in this way also makes it possible for ServiceNow to map your assets to the technical services that they provide.

Be mindful of any changes you make to the folder and project structure to support ServiceNow discovery. The primary role of the folder and project structure is to support billing and IAM access. Therefore, any changes you make to support ServiceNow should support and align to your organization's Google Cloud billing structure. For best practices for structuring your Google Cloud organization, folder, and project hierarchy, see [Resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) and [Creating and managing organizations](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization).

The following diagram represents an example Google Cloud resource hierarchy in its complete form. In this example, the [folder structure](https://docs.cloud.google.com/resource-manager/docs/creating-managing-folders) defines the application, and each project defines an environment.

![Diagram that shows an example Google Cloud resource
hierarchy.](https://docs.cloud.google.com/static/resource-manager/img/cloud-hierarchy.svg)

### Labeling

[_Labels_](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) are key-value pairs that you can assign to your cloud resources. (ServiceNow, AWS, and Azure refer to labels as _tags_.)

ServiceNow uses the labels that you assign to your Google Cloud assets to [identify your assets and optionally map them to services](https://docs.servicenow.com/bundle/tokyo-it-operations-management/page/product/service-mapping/concept/tag-based-mapping.html). Choosing a good labeling scheme helps ServiceNow monitor your infrastructure for accurate reporting and ITOM/ITSM compliance.

We recommend that you use labels for any resources that require unique identification that is more specific than what your folder and project structure allows for. For example, you might want to use labels in the following cases:

  * If there are strict compliance requirements for your application, you can label all of the application resources so that your organization can easily identify all the infrastructure that's in scope.
  * In a multi-cloud environment, you can use labels to identify the cloud provider and region for all resources.
  * If you need more fine-grained visibility than what's provided by default by [Google Cloud Billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports) or [Cloud Billing export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery), the data can be [filtered by labels](https://docs.cloud.google.com/billing/docs/how-to/bq-examples#query-with-labels).



Google automatically assigns labels to Google-managed assets that run in your VPC. Google-assigned labels are prefixed with `goog-`. Your MID Servers shouldn't attempt to perform a deep inspection on these assets. For more information about labels for Google-managed resources, see [Tag Based Mapping](https://docs.servicenow.com/bundle/tokyo-it-operations-management/page/product/service-mapping/concept/tag-based-mapping.html) and [Label resources automatically based on Cloud Asset Inventory real-time notifications](https://github.com/GoogleCloudPlatform/community/blob/master/archived/cloud-asset-inventory-auto-label-resources/index.md).

The following table lists labels that Google Cloud services assign to resources that those services manage.

Google Cloud service | **Labels or label prefix**  
---|---  
Google Kubernetes Engine | ` goog-gke- `  
Compute Engine | ` goog-gce- `  
Managed Service for Apache Spark | ` goog-dataproc- `  
Gemini Enterprise Agent Platform Workbench | ` goog-caip-notebook and goog-caip-notebook-volume `  
  
To support resource management effectively, your organization's deployment process must create project and folder structures and assign asset labels consistently across your entire organization. Inconsistencies in infrastructure and labeling can make it difficult to maintain a correct CMDB without manual processes that are likely to be unsupportable and that present scaling challenges in the long term.

The following list suggests best practices for making your deployment process consistent and repeatable:

  * Use infrastructure as code (IaC) or automated provisioning systems such as [Terraform](https://www.terraform.io/), [ServiceNow ITOM](https://www.servicenow.com/products/it-operations-management/what-is-itom.html), or [Cloud provisioning and governance](https://docs.servicenow.com/bundle/tokyo-it-operations-management/page/product/cloud-management-v2-setup/concept/cloud-mgt-gcp-setup-day-1.html) with [Google Cloud Deployment Manager](https://docs.cloud.google.com/deployment-manager/docs).
  * Have a good governance process in place for your labels. For an overview of labeling governance, see [Tag Governance](https://docs.servicenow.com/en-US/bundle/tokyo-it-asset-management/page/product/it-operations-management/concept/tag-governance.html) in the ServiceNow documentation.



### What's next

  * Learn about the [integration connector for ServiceNow](https://docs.cloud.google.com/integration-connectors/docs/connectors/servicenow/configure).
  * For additional best practices for structuring your resources for Cloud Billing, see [Guide to Cloud Billing Resource Organization & Access Management](https://docs.cloud.google.com/billing/docs/onboarding-checklist) and [Cloud Insights setup guide for Google Cloud](https://docs.servicenow.com/en-US/bundle/tokyo-it-asset-management/page/product/cloud-insights/concept/gcp-cloud-insights-setup-guide.html).
  * For best practices for structuring your organization's IAM permissions, see [Best practices for planning accounts and organizations](https://docs.cloud.google.com/architecture/identity/best-practices-for-planning) and [Cloud Provisioning and Governance](https://docs.servicenow.com/bundle/tokyo-it-operations-management/page/product/cloud-management-v2/concept/cloud-management-v2-landing-page.html).
  * For best practices for structuring your VPC firewall policies across your organization, see [Hierarchical firewall policies](https://docs.cloud.google.com/vpc/docs/firewall-policies).
  * Learn how to use labels to support ServiceNow [tag-based discovery](https://docs.servicenow.com/bundle/tokyo-it-operations-management/page/product/service-mapping/concept/tag-based-mapping.html).
  * Learn about [ServiceNow Agent Client Collector](https://docs.servicenow.com/en-US/bundle/tokyo-it-operations-management/page/product/agent-client-collector/concept/acc-landing-page.html), a push mechanism that runs in your Google Cloud project and [sends output data to the ServiceNow instance through the MID Server](https://www.servicenow.com/content/dam/servicenow-assets/public/en-us/doc-type/resource-center/data-sheet/ds-itom-acc.pdf), storing events and metrics in the relevant database.
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-08 UTC."],[],[]] 
