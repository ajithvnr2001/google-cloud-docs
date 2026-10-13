---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-pages/
title: Managing the pages in your portal \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:57:26.935464+00:00
---

# Managing the pages in your portal  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-pages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Managing the pages in your portal Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

For information about editing, previewing, and publishing portal pages, and managing the audience for the pages in your portal, see [Developing portal content using the page editor](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/page-editor).

Manage the pages in your portal, as described in the following sections.

## About the reserved URL paths

The following URL paths are reserved for use by the developer portal and cannot be specified as the page path when creating pages:

  * `a`
  * `accounts/create`
  * `apis`
  * `create`
  * `docs`
  * `login`
  * `logout`
  * `my-apps`
  * `sites`
  * `teams`



The reserved path `/create` can be used as the target URL of a `MenuItem` or be linked to from a Page.

The `/create` reserved path will redirect to the [accounts creation page](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-register-sign-in).

## Exploring the Pages page

To access the Pages page:

  1. In the Apigee in Cloud console, go to the **Distribution > Portals** page.

[Go to Portals](https://console.cloud.google.com/apigee/portals)

The list of pages in your portal is displayed.

**Note:** For a list of the default pages provided with the sample portal, see [ About the sample portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/build-integrated-portal#sample-portal).

![Click for larger image](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/pages-list-cloud.png)

![list of pages in the portal](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/pages-list-cloud.png)




The Pages page lets you:

  * Create a page
  * View page details, including name, relative path, status, visibility, and amount of time since the page was last modified
  * Edit page content and details
  * Manage the visibility of a page in your portal
  * Delete pages in your portal
  * Sort the list of pages by column (the arrow indicates the active column and direction of the sorted content)



## Creating a page

**Note** : You can create a **maximum of 1000 pages** in your portal.

To create a new page:

  1. Access the Pages page.
  2. Click **+Page**.
  3. In the Create a Page dialog, enter the following details:

Field | Description | Required?  
---|---|---  
Name | Name of the page. The page name must be unique within the portal. The name is used in the portal page header and browser tab. | Yes  
Path | User-friendly relative URL to use for the page. For best practices, see [Implement search engine optimization (SEO)](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-best-practices#seo). Use alphanumeric characters and dashes only. Spaces and special characters are not allowed. Defaults to the page name with spaces converted to dashes.   
**Note** : Avoid specifying a reserved URL path when creating a portal. For a list of reserved URL paths, see About the reserved URL paths. | Yes  
  4. Save the page. Click **Save**.




## Editing the contents of a page

To edit the contents of a page:

  1. Access the Pages page.
  2. Click the name of the page that you want to edit.
  3. Edit the contents of the page. See [Developing portal content using the page editor](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/page-editor).



## Editing the page details

To edit the details for a page, including the name, description, and relative path:

  1. Access the Pages page.
  2. Open the editor. On the row for the page you want to edit, click more_vert **More** , edit **Edit**.

  3. Edit the page details.

  4. Save the page. Click **Save**.




## Managing the visibility of a page in your portal

**Note:** To use all of the features described in this section, you must have [ enrolled in the Preview release of the audience management feature](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-audience#enroll).

To manage the visibility of a page in your portal:

  1. Access the Pages page.

  2. Open the visibility editor:

     1. On the row for the page you want to modify, click more_vert **More** , edit **Edit**.
     2. In the **Visibility** area, click **Edit**.
  3. Select one of the following options:

     * **Public (visible to anyone)** to allow all users to view the page.
     * **Authenticated users** to allow only registered users to view the page.
     * **Selected audiences** to select the specific audiences that you want to be able to view the page. For information about managing the audiences defined for your portal, see [ Managing the audiences for your portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-audience). 
**Note:** If you set the visibility to **Authenticated users** or **Selected audiences** , the page will not be indexed by search engines.
  4. Save the visibility settings.

Click **Apply**.




## Deleting pages from your portal

**Notes** : 

  * You cannot delete the Home page. The `index` URL path serves as the default landing page for your portal.
  * To avoid having an orphaned navigation menu or menu item with a broken link to a page that has been removed, it is recommended that you delete any relevant navigation menus or menu items items first, then delete the page.



To delete a page from your portal:

  1. Access the Pages page.

  2. Delete the page.

     1. Click more_vert **More** , delete **Delete**.
     2. Type **Delete** and then click **Delete page** to confirm.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
