---
url: https://docs.cloud.google.com/looker/docs/admin-panel-platform-api/
title: Admin settings - API \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:44:18.187964+00:00
---

# Admin settings - API  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-platform-api/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - API Stay organized with collections  Save and categorize content based on your preferences. 

The **API** page in the **Platform** section of the **Admin** menu lets you manage access to the Looker API server endpoint. The page also provides a link to the [API Explorer](https://docs.cloud.google.com/looker/docs/api-explorer) documentation.

## Accessing the API page

To access the API page:

  1. Click the Looker **Main menu** icon menu.
  2. Click **Admin** to open the **Admin** menu.
  3. Select **API**.
  4. View the **API Host URL**.

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

## API Host URL

The **API Host URL** is the user-facing domain name (and port) that users need to reach the Looker API server endpoint. To specify a URL, enter your API path in the **API Host URL** field in the following format:
    
    
    https://<instance_name>.cloud.looker.com
    

For Looker installations behind a load balancer (for example, a [cluster](https://docs.cloud.google.com/looker/docs/clustering-looker) configuration) or other proxy, the user-facing domain name may be different from the actual Looker server machine name. If this is the case, the **API Host URL** must indicate the user-facing API host name and port.

If the **API Host URL** field is empty, Looker uses the default API path. For Looker instances hosted on Google Cloud, Microsoft Azure, and instances hosted on Amazon Web Service (AWS) that were created on or after 07/07/2020, the default Looker API path uses port `443`. For Looker instances hosted on AWS that were created before 07/07/2020, the default Looker API path uses port `19999`. The default API URL is in the following format:
    
    
    https://<instance_name>.cloud.looker.com:<port>
    

## API Documentation

If you have installed the [API Explorer extension](https://docs.cloud.google.com/looker/docs/api-explorer) from the [Looker Marketplace](https://docs.cloud.google.com/looker/docs/marketplace), you can click **Use API Explorer** to open the API Explorer and view current API documentation.

If you have not installed the API Explorer extension, you can click **Install API Explorer from the Marketplace** to install the API Explorer on your Looker instance.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
