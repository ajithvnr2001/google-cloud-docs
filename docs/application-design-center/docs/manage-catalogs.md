---
url: https://docs.cloud.google.com/application-design-center/docs/manage-catalogs/
title: Manage, publish, and share catalogs \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:43.748734+00:00
---

# Manage, publish, and share catalogs  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/manage-catalogs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Guides ](https://docs.cloud.google.com/application-design-center/docs/overview)



Send feedback 

#  Manage, publish, and share catalogs Stay organized with collections  Save and categorize content based on your preferences. 

When you create [application templates](https://docs.cloud.google.com/application-design-center/docs/design-application-templates) and [import component templates](https://docs.cloud.google.com/application-design-center/docs/import-components) in a space, your templates can be accessed by other space members. This document helps you share templates outside of your space by publishing templates to a catalog, and sharing that catalog with appropriate spaces.

Each space contains a single catalog where you can add templates and control sharing. You can share a catalog from the space that you created in your initial [application management boundary](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-mgmt-boundary) to spaces in other application management boundaries.

## Before you begin

To perform the tasks in this document, ask your administrator to grant you the necessary roles on the [app-enabled folder](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-enabled-folder) or [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project), as listed in the following table:

Task | Required roles  
---|---  
Publish application templates to a space catalog | Application Design Center Admin (`roles/designcenter.admin`)  
Share a catalog with destination spaces | Application Design Center Admin (`roles/designcenter.admin`)  
  
For more information about roles, see [Access control with IAM](https://docs.cloud.google.com/application-design-center/docs/access-control).

Do the following before you manage catalogs:

  * Complete the App Design Center [_initial setup_](https://docs.cloud.google.com/application-design-center/docs/setup).
  * To create spaces in addition to your _initial space_ , see [Manage spaces](https://docs.cloud.google.com/application-design-center/docs/manage-spaces).



## Publish an application template to a catalog

Before you can share a template with other spaces, publish the template to your catalog.

### Design canvas

  1. From the navigation menu, click **Catalogs**.

[Go to Catalogs](https://console.cloud.google.com/products/design-center/catalog)

  2. Click **Add templates**.

  3. In the **Add templates to Default Catalog** area, do the following:

     1. To find a specific template, type the template name in the **Filter** field.
     2. To add a template to this catalog, in the **Actions** column, click **Add to catalog**.
  4. Click **Done**. The spaces that have access to the catalog have access to the selected templates.

  5. To share the catalog, see Share a catalog with a space.




###  gcloud CLI 

  1. Identify the catalog ID for the catalog where you want to add your template.
         
         gcloud design-center spaces catalogs list \
         --project=PROJECT \
         --location=LOCATION \
         --space=SPACE
         

Replace the following:

     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The catalog region.
     * `SPACE`: Your space ID.

For more information, see [gcloud design-center spaces catalogs list](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/catalogs/list).

  2. Identify the template ID for the template that you want to add to your catalog. For example, the following command lists application templates.
         
         gcloud design-center spaces application-templates list \
         --project=PROJECT \
         --location=LOCATION \
         --space=SPACE \
         --filter=FILTER
         

Replace the following:

     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The catalog region.
     * `SPACE`: Your space ID.
     * `FILTER`: A filter to help you narrow the search results. For example, `"displayName:my-app-template*"`

For more information, see [gcloud design-center spaces application-templates list](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/list).

  3. Commit the application template.
         
         gcloud design-center spaces application-templates commit TEMPLATE \
          --project=PROJECT \
          --location=LOCATION \
          --space=SPACE
         

Replace the following:

     * `TEMPLATE`: The template ID for the template to commit.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The application template region.
     * `SPACE`: Your space ID.

For more information, see [gcloud design-center spaces application-templates commit](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/application-templates/commit).

  4. Copy the `name` output from the commit command. You'll specify this name as the `application-template-revision-source` value when you create your catalog template revision.

  5. Make sure that the application template is not already in the catalog.
         
         gcloud design-center spaces catalogs templates list \
         --catalog=CATALOG \
         --project=PROJECT \
         --location=LOCATION \
         --space=SPACE
         

Replace the following:

     * `CATALOG`: Your catalog ID. For example, `default-catalog`.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The catalog region.
     * `SPACE`: Your space ID.

For more information, see [gcloud design-center spaces catalogs templates list](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/catalogs/templates/list).

  6. If the application template isn't in the catalog, create the catalog template.
         
         gcloud design-center spaces catalogs templates create CATALOG_TEMPLATE \
         --project=PROJECT \
         --location=LOCATION \
         --space=SPACE \
         --catalog=CATALOG \
         --template-category=TEMPLATE_CATEGORY
         

Replace the following:

     * `CATALOG_TEMPLATE`: The catalog template ID for the catalog template that you want to create.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The catalog region.
     * `SPACE`: Your space ID.
     * `CATALOG`: Your catalog ID.
     * `TEMPLATE_CATEGORY`: The template category. For example, `application-template`.

For more information, see [gcloud design-center spaces catalogs templates create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/catalogs/templates/create).

  7. Create a catalog template revision. This creates the first revision, which developers use as a source for an application.
         
         gcloud design-center spaces catalogs templates revisions create REVISION \
         --project=PROJECT \
         --location=LOCATION \
         --space=SPACE \
         --catalog=CATALOG \
         --template=CATALOG_TEMPLATE \
         --application-template-revision-source=APPLICATION_TEMPLATE_REVISION_SOURCE
         

Replace the following:

     * `REVISION`: The revision ID for the revision that you want to create. For example, `r1`.
     * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
     * `LOCATION`: The catalog region.
     * `SPACE`: Your space ID.
     * `CATALOG`: Your catalog ID.
     * `CATALOG_TEMPLATE`: The template ID.
     * `APPLICATION_TEMPLATE_REVISION_SOURCE`: The application template revision source. You copied this value when you committed your application template. For example, `projects/my-project/locations/us-central1/spaces/my-space/applicationTemplates/my-app-template/revisions/r1`.

For more information, see [gcloud design-center spaces catalogs templates revisions create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/catalogs/templates/revisions/create).




### Share revised templates

If you make changes to a template, those changes are not automatically published to the catalog. To share the latest revision, publish the template to the catalog again.

### Remove templates from a catalog

If you no longer want to share a specific template with a space, remove it from the catalog.

### Design canvas

  1. From the navigation menu, click **Catalogs**.

[Go to Catalogs](https://console.cloud.google.com/products/design-center/catalog)

  2. To manage the templates in this catalog, click **Templates in catalog**.

  3. To remove a template, click more_vert **Actions** and select **Remove from catalog**.

     1. In the field, enter the name of the template.
     2. Click **Remove**.



###  gcloud CLI 

Remove a template from your catalog.
    
    
    gcloud design-center spaces catalogs templates delete CATALOG_TEMPLATE \
    --catalog=CATALOG \
    --project=PROJECT \
    --location=LOCATION \
    --space=SPACE
    

Replace the following:

  * `CATALOG_TEMPLATE`: The catalog template ID for the template that you want to remove from the catalog.
  * `CATALOG`: Your catalog ID.
  * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
  * `LOCATION`: The catalog region.
  * `SPACE`: Your space ID.



For more information, see [gcloud design-center spaces catalogs templates delete](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/catalogs/templates/delete).

## Share a catalog with a space

You can only share a catalog with a destination space that is in the same region as the source space, but located in a different [application management boundary](https://docs.cloud.google.com/application-design-center/docs/key-concepts#app-mgmt-boundary).

To share your catalog with a space, do the following:

### Design canvas

  1. From the navigation menu, click **Catalogs**.

[Go to Catalogs](https://console.cloud.google.com/products/design-center/catalog)

  2. Click **Share catalog**.

  3. From the **Share with** field, select whether the destination space is in one of the following:

     * **Folder** : a folder-level application management boundary.
     * **Project** : a project-level application management boundary.
  4. In the **Project/Folder ID** field, enter the project or folder ID for the application management boundary where the destination space resides.

The space in the same region as your origination space automatically populates in the **Space name** field.

  5. Click **Share**.

Developers can view the templates from a shared catalog by opening their space in App Design Center and clicking **Shared templates** from the navigation menu.




###  gcloud CLI 

Share a catalog with a space.
    
    
    gcloud design-center spaces catalogs shares create SHARE \
    --project=PROJECT \
    --space=SPACE \
    --location=LOCATION \
    --catalog=CATALOG \
    --destination-space=DESTINATION_SPACE
    

Replace the following:

  * `SHARE`: The share ID for the share that you want to delete.
  * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
  * `SPACE`: Your space ID.
  * `LOCATION`: The catalog region.
  * `CATALOG`: The catalog ID for the catalog that you're sharing.
  * `DESTINATION_SPACE`: The fully qualified space name for the space that you're sharing to. For example, `projects/my-project/locations/us-central1/spaces/my-space`.



For more information, see [gcloud design-center spaces catalogs shares create](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/catalogs/shares/create).

### Stop sharing a catalog with a space

If you no longer want to share a catalog with a space, stop sharing the catalog by doing the following:

### Design canvas

  1. From the navigation menu, click **Catalogs**.

[Go to Catalogs](https://console.cloud.google.com/products/design-center/catalog)

  2. Click **Spaces shared with**.

  3. To stop sharing this catalog with a space, click more_vert

**Actions** and select **Stop sharing**.

     1. In the field, enter the space name.
     2. Click **Stop sharing**.



###  gcloud CLI 

Stop sharing a catalog with a space.
    
    
    gcloud design-center spaces catalogs shares delete SHARE \
    --project=PROJECT \
    --location=LOCATION \
    --space=SPACE \
    --catalog=CATALOG
    

Replace the following:

  * `SHARE`: The share ID for the share that you want to delete.
  * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
  * `LOCATION`: The catalog region.
  * `SPACE`: Your space ID.
  * `CATALOG`: The catalog ID for the catalog that you're sharing.



For more information, see [gcloud design-center spaces catalogs shares delete](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/catalogs/shares/delete).

## Edit catalog metadata

To manage your catalog, you can give it a descriptive name and description by doing the following:

### Design canvas

  1. From the navigation menu, click **Catalogs**.

[Go to Catalogs](https://console.cloud.google.com/products/design-center/catalog)

  2. Examine the catalog details.

  3. To modify the **Display name** , do the following:

     1. Click edit **Edit Display name**.
     2. In the **Display name** field, enter the new name.
     3. Click **Save**.
  4. To modify the **Description** , do the following:

     1. Click edit **Edit Description**.
     2. In the **Description** field, enter the new description.
     3. Click **Save**.



###  gcloud CLI 
    
    
    gcloud design-center spaces catalogs update CATALOG \
    --project=PROJECT \
    --location=LOCATION \
    --space=SPACE \
    --description=DESCRIPTION \
    --display-name=DISPLAY_NAME
    

Replace the following:

  * `CATALOG`: Your catalog ID.
  * `PROJECT`: Your [management project](https://docs.cloud.google.com/application-design-center/docs/key-concepts#mgmt-project) ID.
  * `LOCATION`: The catalog region.
  * `SPACE`: Your space ID.
  * `DESCRIPTION`: The catalog description.
  * `DISPLAY_NAME`: The catalog display name.



For more information, see [gcloud design-center spaces catalogs update](https://docs.cloud.google.com/sdk/gcloud/reference/design-center/spaces/catalogs/update).

## What's next

  * Define your own configurations by [designing application templates](https://docs.cloud.google.com/application-design-center/docs/design-application-templates).
  * Learn how to update, scale, and delete your resources by [managing applications](https://docs.cloud.google.com/application-design-center/docs/manage-applications).
  * Use your own Terraform modules in your template designs by [importing components](https://docs.cloud.google.com/application-design-center/docs/import-components).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
