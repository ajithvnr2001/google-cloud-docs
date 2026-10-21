---
url: https://docs.cloud.google.com/service-catalog/docs/marketplace-solutions/
title: Adding a solution from Cloud Marketplace \u00a0|\u00a0 Service Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:54.306242+00:00
---

# Adding a solution from Cloud Marketplace  |  Service Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-catalog/docs/marketplace-solutions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Catalog ](https://docs.cloud.google.com/service-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/service-catalog/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Adding a solution from Cloud Marketplace

In this guide, you learn how to add [Google Cloud Marketplace](https://console.cloud.google.com/marketplace) solutions for Service Catalog.

Adding solutions in Service Catalog lets you approve and share a curated list of Google Cloud solutions with users in your organization. After creating the solution from Google Cloud Marketplace, you can assign it to a [catalog](https://docs.cloud.google.com/service-catalog/docs/create-catalog) so that your users can view and deploy the solution.

This guide explains how to add two types of Google Cloud Marketplace solutions for your Service Catalog users: virtual machines (VMs) and software as a service (SaaS) solutions.

## Before you begin

  * You must have the [Catalog Admin](https://docs.cloud.google.com/service-catalog/docs/access-control#instance_admin_role) (`roles/cloudprivatecatalogproducer.admin`) _OR_ [Catalog Manager](https://docs.cloud.google.com/service-catalog/docs/access-control#catalog_manager_role) (`roles/cloudprivatecatalogproducer.manager`) role for the Google Cloud organization associated with the Google Cloud project which has Service Catalog enabled. If you don't have this role, contact your Organization Administrator to request access.

  * If you're adding a SaaS solution, go to the solution's description page in Cloud Marketplace and subscribe to the solution.




## Adding VMs

To add a VM solution in Service Catalog:

  1. Go to [Cloud Marketplace](https://console.cloud.google.com/marketplace/browse?filter=solution-type:vm) and filter by **Virtual machines**.

[View VM solutions in Cloud Marketplace](https://console.cloud.google.com/marketplace/browse?filter=solution-type:vm)

  2. Find the VM solution you want to add, and click it to go to the solution description page.

  3. In the **Add to Service Catalog** section of the side navigation, click **Deployment ZIP file** to download a zip file containing the Deployment Manager configuration files for the solution.

You might not see the **Add to Service Catalog** link if:

     * You have not accepted the Google Cloud Marketplace Terms of Service.
     * If Private Marketplace is enabled for your project, the product must be permitted in the Private Marketplace inventory.
  4. Using the zip file, follow the steps to [create a Deployment Manager-based solution](https://docs.cloud.google.com/service-catalog/docs/dm-based-solution) to your catalog.




## Adding SaaS solutions

To add a SaaS solution in Service Catalog:

  1. Go to [Cloud Marketplace](https://console.cloud.google.com/marketplace/browse?filter=solution-type:service) and filter by **APIs & services**.

[View APIs & services in Cloud Marketplace](https://console.cloud.google.com/marketplace/browse?filter=solution-type:service)

  2. Click the SaaS solution you want to add.

  3. On the solution description page, click **Add to Service Catalog**.

You might not see the **Add to Service Catalog** link if:

     * Your organization is not onboarded to Service Catalog.
     * You don't have the required IAM permissions to create a product.
     * Your organization does not have an active subscription or entitlement for the product.
  4. In the **Add to Service Catalog** pane, select a Google Cloud project for the solution.

  5. Verify the details that appear to users when they view the solution in Service Catalog. Click **Next**.

  6. Optionally, add links for getting support and documentation.

  7. Optionally, [assign the solution](https://docs.cloud.google.com/service-catalog/docs/assign-solutions) to one or more catalogs.

  8. Click **Add**.




## Next steps

  * [Assign the solution](https://docs.cloud.google.com/service-catalog/docs/assign-solutions) to a catalog, so that users in your organization can access and launch the solution.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
