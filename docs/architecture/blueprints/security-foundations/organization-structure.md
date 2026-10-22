---
url: https://docs.cloud.google.com/architecture/blueprints/security-foundations/organization-structure/
title: Organization structure \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:27:26.440232+00:00
---

# Organization structure  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/security-foundations/organization-structure/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Organization structure Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-05-15 UTC

The root node for managing resources in Google Cloud is the [organization](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations). The Google Cloud organization provides a [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) that provides an ownership structure for resources and attachment points for [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) and access controls. The resource hierarchy consists of folders, projects, and resources, and it defines the structure and use of Google Cloud services within an organization.

Resources lower in the hierarchy inherit policies such as IAM allow policies and organization policies. All access permissions are denied by default, until you apply allow policies directly to a resource or the resource inherits the allow policies from a higher level in the resource hierarchy.

The following diagram shows the folders and projects that are deployed by the blueprint.

![The example.com organization structure.](https://docs.cloud.google.com/static/architecture/blueprints/security-foundations/images/example-org-structure.svg)

The following sections describe the folders and projects in the diagram.

## Folders

The blueprint uses [folders](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#folders) to group projects based on their environment. This logical grouping is used to apply configurations like allow policies and organization policies at the folder level and then all resources within the folder inherit the policies. The following table describes the folders that are part of the blueprint.

Folder | Description  
---|---  
`bootstrap` | Contains the projects that are used to deploy foundation components.  
`common` | Contains projects with resources that are shared by all environments.  
`production` | Contains projects with production resources.  
`nonproduction` | Contains a copy of the production environment to let you test workloads before you promote them to production.  
`development` | Contains the cloud resources that are used for development.   
`networking` | Contains the networking resources that are shared by all environments.   
  
## Projects

The blueprint uses [projects](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#projects) to group individual resources based on their functionality and intended boundaries for access control. This following table describes the projects that are included in the blueprint.

Folder | Project | Description  
---|---|---  
`bootstrap` | `prj-b-cicd` | Contains the deployment pipeline that's used to build out the foundation components of the organization. For more information, see [deployment methodology](https://docs.cloud.google.com/architecture/blueprints/security-foundations/deployment-methodology).  
`prj-b-seed` | Contains the Terraform state of your infrastructure and the Terraform service account that is required to run the pipeline. For more information, see [deployment methodology](https://docs.cloud.google.com/architecture/blueprints/security-foundations/deployment-methodology).  
`common` | `prj-c-secrets` | Contains organization-level secrets. For more information, see [store application credentials with Secret Manager](https://docs.cloud.google.com/architecture/blueprints/security-foundations/operation-best-practices#store-and).  
`prj-c-logging` | Contains the aggregated log sources for audit logs. For more information, see [centralized logging for security and audit](https://docs.cloud.google.com/architecture/blueprints/security-foundations/detective-controls#centralized-logging).  
`prj-c-scc` | Contains resources to help configure Security Command Center alerting and other custom security monitoring. For more information, see [threat monitoring with Security Command Center](https://docs.cloud.google.com/architecture/blueprints/security-foundations/detective-controls#threat-monitoring).  
`prj-c-billing-export` | Contains a BigQuery dataset with the organization's [billing exports](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery). For more information, see [allocate costs between internal cost centers](https://docs.cloud.google.com/architecture/blueprints/security-foundations/operation-best-practices#allocate-costs).  
`prj-c-infra-pipeline` | Contains an infrastructure pipeline for deploying resources like VMs and databases to be used by workloads. For more information, see [pipeline layers](https://docs.cloud.google.com/architecture/blueprints/security-foundations/deployment-methodology#pipeline-layers).  
`prj-c-kms` | Contains encryption keys for encrypting shared services within the common folder. For more information, see [manage encryption keys](https://docs.cloud.google.com/architecture/blueprints/security-foundations/operation-best-practices#manage-encryption).  
`networking` | `prj-net-{env}-svpc` | Contains the host project for a Shared VPC network. For more information, see [network topology](https://docs.cloud.google.com/architecture/blueprints/security-foundations/networking#network_topology).  
`prj-net-hub` | Contains the Shared VPC network used as a hub between the on-premises environment and Google Cloud spokes. This project is created in the hub-and-spoke topology only. For more information, see [network topology](https://docs.cloud.google.com/architecture/blueprints/security-foundations/networking#network_topology).  
`prj-net-interconnect` | Contains the Cloud Interconnect connections that provide connectivity between your on-premises environment and Google Cloud. For more information, see [hybrid connectivity](https://docs.cloud.google.com/architecture/blueprints/security-foundations/networking#hybrid-connectivity).  
environments:   
` - development (d)   
- non-production (n)   
- production (p)` | `prj-{env}-{workload_name_or_id}` | Contains various workload projects in which you create resources for applications. For more information, see [project deployment patterns](https://docs.cloud.google.com/architecture/blueprints/security-foundations/networking#project-deployment) and [pipeline layers](https://docs.cloud.google.com/architecture/blueprints/security-foundations/deployment-methodology#pipeline-layers).  
`prj-{env}-secrets` | Contains folder-level secrets. For more information, see [store and audit application credentials with Secret Manager](https://docs.cloud.google.com/architecture/blueprints/security-foundations/operation-best-practices#store-and).  
`prj-{env}-kms` | Contains encryption keys for encrypting services within each environment folder. For more information, see [manage encryption keys](https://docs.cloud.google.com/architecture/blueprints/security-foundations/operation-best-practices#manage-encryption).  
  
## Governance for resource ownership

We recommend that you apply labels consistently to your projects to assist with governance and cost allocation. The following table describes the project labels that are added to each project for governance in the blueprint.

Label | Description  
---|---  
`application` | The human-readable name of the application or workload that is associated with the project.  
`businesscode` | A short code that describes which business unit owns the project. The code `shared` is used for common projects that are not explicitly tied to a business unit.  
`billingcode` | A code that's used to provide chargeback information.  
`primarycontact` | The username of the primary contact that is responsible for the project. Because project labels can't include special characters such as the ampersand (@), it is set to the username without the @example.com suffix.  
`secondarycontact` | The username of the secondary secondary contact that is responsible for the project. Because project labels can't include special characters such as @, set only the username without the @example.com suffix.  
`environment` | A value that identifies the type of environment, such as `bootstrap`, `common`, `production`, `non-production,development`, or `network.`  
`envcode` | A value that identifies the type of environment, shortened to `b`, `c`, `p`, `n`, `d`, or `net`.  
`vpc` | The ID of the VPC network that this project is expected to use.  
  
Google might occasionally send important notifications such as account suspensions or updates to product terms. The blueprint uses [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) to send those notifications to the groups that you configure during deployment. Essential Contacts is configured at the organization node and inherited by all projects in the organization. We recommend that you review these groups and ensure that emails are monitored reliably.

Essential Contacts is used for a different purpose than the `primarycontact` and `secondarycontact` fields that are configured in project labels. The contacts in project labels are intended for internal governance. For example, if you identify non-compliant resources in a workload project and need to contact the owners, you could use the `primarycontact` field to find the person or team responsible for that workload.

## What's next

  * Read about [networking](https://docs.cloud.google.com/architecture/blueprints/security-foundations/networking) (next document in this series).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-15 UTC."],[],[]] 
