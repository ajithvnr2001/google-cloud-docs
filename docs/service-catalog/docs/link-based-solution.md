---
url: https://docs.cloud.google.com/service-catalog/docs/link-based-solution/
title: Creating a link-based solution \u00a0|\u00a0 Service Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:38:23.374928+00:00
---

# Creating a link-based solution  |  Service Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-catalog/docs/link-based-solution/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Service Catalog ](https://docs.cloud.google.com/service-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/service-catalog/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Creating a link-based solution

When creating Service Catalog solutions for users in your organization, you can create a link-based solution, which is a reference link to a solution that your users download and launch. After you create the solution, you can share it with your users by assigning it to [catalogs](https://docs.cloud.google.com/service-catalog/docs/create-catalog).

## Before you begin

  * You must have the [Catalog Admin](https://docs.cloud.google.com/service-catalog/docs/access-control#instance_admin_role) (`roles/cloudprivatecatalogproducer.admin`) _OR_ [Catalog Manager](https://docs.cloud.google.com/service-catalog/docs/access-control#catalog_manager_role) (`roles/cloudprivatecatalogproducer.manager`) role for the Google Cloud organization associated with the Google Cloud project which has Service Catalog enabled. If you don't have this role, contact your Organization Administrator to request access.



## Creating the solution in Service Catalog

To create a link-based solution in Service Catalog:

  1. Go to the Service Catalog Admin [**Solutions** page](https://console.cloud.google.com/catalog/admin/solutions) in the Google Cloud console.   
[Go to the Solutions page](https://console.cloud.google.com/catalog/admin/solutions)
  2. Click **Select** to choose the Google Cloud project.
  3. Click **CREATE SOLUTION**. In the drop-down list, select **Create a Link solution**.
  4. Enter a name, URL, description, and tagline for your solution. The tagline is a short description of a solution that users see as they browse Service Catalog.
  5. Optionally, upload an icon for the solution. The recommended dimensions for an icon are 80 by 80 pixels.
  6. Optionally, add a link for getting support.
  7. Optionally, add a link to documentation for the solution.
  8. Click **CREATE**.



The following screenshot illustrates creating a link-based solution:

![Form to create a link-based solution](https://docs.cloud.google.com/static/service-catalog/images/screen-privatecatalog-create-link.png)

## Next steps

  * [Assign the solution](https://docs.cloud.google.com/service-catalog/docs/assign-solutions) to a catalog, so that users in your organization can access and launch the solution.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
