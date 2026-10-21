---
url: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/deploy-blueprint/
title: Deploy the blueprint \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:37.399380+00:00
---

# Deploy the blueprint  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/deploy-blueprint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Deploy the blueprint Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-13 UTC

This section describes the process that you can use to deploy the blueprint, its naming conventions, and alternatives to blueprint recommendations.

## Bringing it all together

To implement the architecture described in this document, complete the steps in this section.

### Deploy the blueprint in a new organization

To deploy the blueprint in a new Google Cloud organization, complete the following:

  1. Create your foundational infrastructure using the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations). Complete the following:

     1. Create an organization structure, including folders for separation of environments.
     2. Configure foundational IAM permissions to grant access to developer platform administrators.
     3. Create the VPC network.
     4. Deploy the foundation infrastructure pipeline.

If you don't use the enterprise foundations blueprint, see Deploy the blueprint without the enterprise foundations blueprint.

  2. Deploy the [enterprise application blueprint](https://github.com/GoogleCloudPlatform/terraform-google-enterprise-application) as follows:

     1. The developer platform administrator uses the foundation infrastructure pipeline to create the multi-tenant infrastructure pipeline, application factory, and fleet-scope pipeline.
     2. The developer platform administrator uses the multi-tenant infrastructure pipeline to deploy GKE clusters and shared infrastructure.
     3. Application operators use the application factory to onboard new applications. Operators add one or more entries in the application factory repository, which triggers the creation of application-specific resources.
     4. Application developers use the application CI/CD pipeline within their application-specific infrastructure to deploy applications to the multi-tenant infrastructure.



### Deploy the blueprint without the enterprise foundations blueprint

If you don't deploy the enterprise application blueprint on the enterprise foundations blueprint, complete the following steps:

  1. Create the following resources: 
     * An organization hierarchy with `development`, `nonproduction`, and `production` folders
     * A Shared VPC network in each folder
     * An IP address scheme that takes into account the required IP ranges for your GKE clusters
     * A DNS mechanism for your GKE clusters
     * Firewall policies that are aligned with your security posture
     * A mechanism to access Google Cloud APIs through private IP addresses
     * A connectivity mechanism with your on-premises environment
     * Centralized logging for security and audit
     * Security Command Center for threat monitoring
     * Organizational policies that are aligned with your security posture
     * A pipeline that can be used to deploy the application factory, the multi-tenant infrastructure pipeline, and the fleet-scope pipeline
  2. After you deploy the resources, continue with step 2 in Deploy the blueprint in a new organization.



### Incorporate the blueprint into your existing GKE deployment

This blueprint requires you to deploy the developer platform first, and then deploy applications onto the developer platform. The following table describes how you can use the blueprint if you already have containerized applications running on Google Cloud.

Existing usage | Migration strategy  
---|---  
Already have a CI/CD pipeline. | You can use the blueprint's fleet and cluster architecture even when different products are used for application build and deployment. At a minimum, we recommend that you mirror images to two [regions](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones).  
Have an existing organization structure that doesn't match the enterprise foundations blueprint. | Having at least two environments is recommended for safer sequential deployments. You don't have to deploy environments in separate Shared VPCs or folders. However, don't deploy workloads that belong to different environments into the same cluster.  
Don't use IaC. | If your current application deployment process doesn't use IaC, you can assess your readiness with the [Terraform on Google Cloud maturity model](https://docs.cloud.google.com/docs/terraform/maturity). [Import existing resources](https://docs.cloud.google.com/docs/terraform/resource-management/import) into a different Terraform project which is organized similarly to this blueprint, with the separation of multi-tenant and per-tenant pipelines. To create new clusters, you can use [Terraform modules for Google Cloud](https://github.com/terraform-google-modules).  
Clusters are spread across multiple projects within the same environment. | You can group clusters from multiple projects into a fleet. Verify that your namespaces have unique meanings within the same fleet. Before adding clusters to a fleet, ask teams to move their applications to a namespace with a unique name (for example, not `default`).You can then group namespaces into scopes.  
Clusters are in a single region. | You don't need to use multiple regions in production and non-production to adopt the blueprint.  
Different sets of environments exist. | You can modify the blueprint to support more or less than three environments.  
Creation of clusters is delegated to application developer or application operator teams. | For the most secure and consistent developer platform, you can try to move ownership of clusters from the application teams to the developer platform team. If you can't, you can still adopt many of the blueprint practices. For example, you can add the clusters owned by different application teams to a fleet. However, when combining clusters with independent ownership, don't use Workload Identity Federation for GKE or Cloud Service Mesh, because they don't provide enough control of who can assert what workload identities. Instead, use a [custom organization policy](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/custom-org-policies) to prevent teams from enabling these features on GKE clusters.When clusters are grouped into a fleet, you can still audit and enforce policies. You can use a custom organization policy to require clusters to be created within a fleet that corresponds to the environment folder that the cluster's project is under. You can use [fleet default configuration](https://docs.cloud.google.com/anthos/fleet-management/docs/manage-features) to require that new clusters use policy control.  
  
## Alternatives to default recommendations

This section describes alternatives to the default recommendations that are included in this guide.

Decision area | Possible alternatives  
---|---  
All applications run in the same set of five clusters. | The blueprint uses a set of five clusters (two in production, two in non-production, and one in development). You can modify the blueprint to make additional sets of five clusters.Assign applications to sets of five clusters. Don't bind an application's scopes or fleet namespaces to clusters in the other sets. You may want to segregate applications into different cluster sets to complete activities such as the following:

  * Group together a few applications with special regulatory concerns (for example, PCI-DSS).
  * Isolate applications that require special handling during cluster upgrades (for example, stateful applications that use persistent volumes).
  * Isolate applications with risky security profiles (for example, processing user-provided content in a memory-unsafe language).
  * Isolate applications that require GPUs, cost sensitivity, and performance sensitivity.
  * If you are nearing the [GKE cluster limit](https://docs.cloud.google.com/kubernetes-engine/quotas#limits_per_cluster) on the number of nodes (65,000 nodes), you can create a new set of clusters.
  * Use a different Shared VPC for applications that need to run within a VPC Service Controls perimeter. Create one cluster set in the perimeter and one cluster set outside of the perimeter.

Avoid creating new clusters sets for every application or tenant, because this practice might result in one of the following circumstances:

  * Applications that don't make good use of the minimum cluster size (3 VMs x 2 regions) even with the smallest available instance types.
  * Missed potential for cost reduction from bin-packing different applications.
  * Tedious and uncertain capacity growth planning because planning is applied to each application individually. Predictions of capacity are more accurate when done in aggregate for a broad set of applications.
  * Delays in creating new clusters for new tenants or applications, reducing tenant satisfaction with the platform. For example, in some organizations, the required IP address allocations may take time and require extra approvals.
  * Reaching the [private cluster limit](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#req_res_lim) in a VPC network.

  
Production and non-production environments have clusters in two regions. | For lower latency to end users in multiple regions, you can deploy the production and non-production workloads across more than two regions (for example, three regions for production, three regions for non-production, and one region for development). This deployment strategy increases the cost and overhead of maintaining resources in additional regions.  
If all applications have lower availability requirements, you can deploy production and non-production workloads to only one region (one production environment, one non-production environment, and one development environment). This strategy helps reduce cost, but doesn't protect the same level of availability as a dual-regional or multi-regional architecture.  
If applications have different availability requirements, you can create different cluster sets for different applications (for example, `cluster-set-1` with two production environments, two non-production environments, and one development environment and `cluster-set-2` with one production environment, one non-production environment, and one development environment).  
Hub-and-spoke topology matches your requirements better than Shared VPC. | You can deploy the blueprint in a hub-and-spoke configuration, where each environment (development, production, and non-production) is hosted in its own spoke. Hub-and-spoke topology can increase segregation of the environments. For more information, see [Hub-and-spoke network topology](https://docs.cloud.google.com/architecture/blueprints/security-foundations/networking#hub-spoke-network-topology).  
Each application has a separate Git repository. | Some organizations use a single Git repository (a _monorepo_) for all source code instead of multiple repositories. If you use a monorepo, you can modify the [ application factory](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/deployment-methodology#application-factory) component of the blueprint to support your repository. Complete the following:

  * Instead of creating a new repository for each new application, create a sub-directory in the existing repository.
  * Instead of giving owner permissions on the new repository to the application developer group, give write permission on the existing repository and make the application developer group a required reviewer for changes to the new sub-directory. Use the [ `CODEOWNERS`](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners) feature and branch protection. 

  
  
## What's next

  * Learn more about the [enterprise foundations blueprint](https://docs.cloud.google.com/architecture/blueprints/security-foundations).
  * Learn more about software delivery on Google Cloud from the following: 
    * [Best practices for continuous integration and delivery to GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/best-practices-continuous-integration-delivery-kubernetes#checklist)
    * [Software delivery framework](https://docs.cloud.google.com/anthos-config-management/docs/tutorials/modern-cicd-gke-user-guide)
    * [Secure CI/CD pipeline](https://github.com/GoogleCloudPlatform/terraform-google-secure-cicd) repository
  * Learn more about running applications on GKE from the following: 
    * [Best practices for GKE networking](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/networking)
    * [Best practices for GKE enterprise multi-tenancy](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/enterprise-multitenancy)
    * [Best practices for running cost-optimized Kubernetes applications on GKE](https://docs.cloud.google.com/architecture/best-practices-for-running-cost-effective-kubernetes-applications-on-gke)
    * [GKE safer cluster](https://github.com/terraform-google-modules/terraform-google-kubernetes-engine/tree/master/modules/safer-cluster) repository
    * [Harden your cluster's security](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/hardening-your-cluster)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-13 UTC."],[],[]] 
