---
url: https://docs.cloud.google.com/marketplace/docs/governance/private-marketplace/
title: Private Marketplace \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:46:16.681351+00:00
---

# Private Marketplace  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/governance/private-marketplace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/overview)



Send feedback 

#  Private Marketplace Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud Private Marketplace contains curated lists of products, called _collections_ , that have met your organization's requirements for use and that are available to either specified projects and folders or to your entire organization.

**Note:** When you turn on and turn off Google Cloud Private Marketplace, you turn it on and off at the organization level.

When you turn Private Marketplace on for your organization, your users can only access the products in the collections that you've shared with them, and they can't deploy products that you haven't shared with them. Private Marketplace uses a fail open governance model, with an estimated 99.994% reliability.

**Note:** Starting March 26, 2025, Google Cloud Private Marketplace can block new API deployments of third-party Cloud Marketplace products that aren't in a shared collection. After March 26, 2025, if you turn on Private Marketplace for the first time, it blocks these deployments by default. However, if you've previously turned on Private Marketplace at any point, you must upgrade Private Marketplace to ensure that it properly blocks API deployments of unapproved products. For more information, see [Upgrade Google Cloud Private Marketplace's enforcement capabilities](https://docs.cloud.google.com/marketplace/docs/migrations/private-marketplace-api-enforcement).

We recommend that you turn on [Product Requests](https://docs.cloud.google.com/marketplace/docs/governance/procurement-requests) to allow your users to request access to specific Google Cloud Marketplace products.

## Required IAM roles

To manage your private marketplace as an administrator, you must have the following roles for your Google Cloud organization:

**Action** | **Roles** | **Level at which role is assigned**  
---|---|---  
Turn on Private Marketplace |  Commerce Organization Governance Admin (`roles/commerceorggovernance.admin`) AND Organization Viewer (`roles/resourcemanager.organizationViewer`) roles  | Organization level  
Manage collections |  Commerce Organization Governance Admin (`roles/commerceorggovernance.admin`) AND Organization Viewer (`roles/resourcemanager.organizationViewer`) roles  | Organization level  
  
## Supported products

Private Marketplace supports third-party Cloud Marketplace product listings that are sold by independent software vendors (ISVs) and governed by the [Google Cloud Marketplace Terms of Service](https://cloud.google.com/terms/marketplace/launcher).

For the following types of products, if they aren't approved for your users, Private Marketplace blocks your users from using the API to deploy them:

  * Kubernetes apps and container images deployed onto Google Kubernetes Engine (GKE) clusters that are version 1.32.1-gke.1376000 or later
  * Container images deployed to Cloud Run
  * Virtual image disk creations
  * Procurable Vertex AI models
  * Procurable BigQuery datasets

**Note:** After you've approved a procurable Vertex AI model through Private Marketplace, you can't revoke that approval. If you use Private Marketplace to attempt to revoke approval for a procurable Vertex AI model, the model no longer appears as approved to your users in Private Marketplace, but they're still able to procure it.

For VMs deployed to Compute Engine, Private Marketplace identifies VMs by their product service name. For container images, Private Marketplace identifies images as follows:

  * For images referenced directly in Cloud Marketplace listings, Private Marketplace identifies the container images by the URL that links to them.
  * For images that match images available through Cloud Marketplace, Private Marketplace identifies the container images by their Secure Hash Algorithm (SHA) value.
  * For images deployed to Cloud Run, Private Marketplace identifies images by checking their metadata for Cloud Marketplace annotations.

**Note:** Private Marketplace doesn't block Google Kubernetes Engine images that are deployed to non-Cloud Marketplace repositories and referenced by tag. To block these images, use [Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/overview).

### Unsupported products

Private Marketplace doesn't support the following types of products:

  * Google-provided [public OS images](https://docs.cloud.google.com/compute/docs/images#os-compute-support)
  * Google-provided [public datasets](https://console.cloud.google.com/marketplace/browse?filter=partner:BigQuery%20Public%20Data)
  * Products owned and managed by Google, such as Maps, Firebase, Mandiant, or Kubeflow
  * Products listed as offered by: 
    * Google
    * Google Enterprise API
    * Google Cloud Platform
  * Third-party and open source datasets and AI models that require you to have BigQuery or Vertex AI Identity and Access Management (IAM) permissions to access them
  * [The API Library](https://console.cloud.google.com/apis/library)



## Get started with Google Cloud Private Marketplace

To set up your organization with Private Marketplace, complete the following steps:

  1. [Create and publish a default collection](https://docs.cloud.google.com/marketplace/docs/governance/create-default-collection) for your organization.

  2. Optionally, to share additional Cloud Marketplace products with specific folders or projects, you can [create additional collections](https://docs.cloud.google.com/marketplace/docs/governance/curate-collection) and [share them](https://docs.cloud.google.com/marketplace/docs/governance/share-collection).

  3. Optionally, [turn on Product Requests](https://docs.cloud.google.com/marketplace/docs/governance/procurement-requests).

  4. [Turn on Google Cloud Private Marketplace](https://docs.cloud.google.com/marketplace/docs/governance/enable-private-marketplace).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
