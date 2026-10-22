---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-files/
title: Managing your assets \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:00:15.354051+00:00
---

# Managing your assets  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Managing your assets Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Manage the assets, such as images or other files, that you would like to use in your portal, as described in the following sections.

## Supported file types

The following file types are supported: GIF, JPG, PNG, SVG, and PDF. Apigee recommends that your files not exceed 1 MB.

## Exploring the Assets page

To access the Assets page:

  1. In the Apigee in Cloud console, go to the **Distribution > Portals** page.

[Go to Portals](https://console.cloud.google.com/apigee/portals)

  2. Click the row of the portal for which you want to manage assets.

  3. Click **Assets** in the side navigation.




The assets manager lets you:

  * View file details
  * Upload a file
  * Preview a file
  * Delete a file



## About the default image images

The following default image files are used in the sample portal.

When customizing the default images described in the following table, you may need to "force refresh" your browser to bypass the cache and load the new image. Image file | Where used?  
---|---  
`home-background.jpg` | Backdrop image on the sample portal home page. Customize the image by replacing the `home-background.jpg` image in assets manager by uploading your own version using the same name and relative file size (3000 pixels by 1996 pixels). Alternatively, you can use a different filename and update the SCSS styles, as described in [ Customizing your background image](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-themes#background-image).  
`idp-logo.png` | Logo placeholder image used on the Sign In page. To change the Acme logo to your company's logo, upload your logo using the same name and relative file size: `logo.png` (280 pixels by 125 pixels). See also [ Customizing the logo on the Sign In page](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-themes#sign-in-logo) for relevant style customizations.  
  
## Uploading a file

Upload files to your portal of the types described in Supported file types.

You can upload a maximum of 500 files or 100 MB. Each file can be no larger than 10 MB.

To upload a file:

  1. Access the Assets page.
  2. Click **\+ File**.
  3. Upload the file. 
     1. Click **Browse**.
     2. Click a file.
     3. Click **Open**.
     4. Click **Upload**.

**Warning:** These files are public and can be accessed by anyone on the Internet. Only upload files that are safe to be visible to the Internet as a whole.

## Previewing a file

To preview a file:

  1. Access the Assets page.
  2. Click the name of the file that you want to preview. The file displays in a new browser window.
  3. Close the browser tab when you are done previewing the file.



## Deleting a file

**Note:** Before deleting a file, manually remove any links to it from the pages in your portal. Otherwise, there will be broken links in your content.

To delete a file:

  1. Access the Assets page.
  2. On the row of the asset you want to remove, click delete **Delete**.
  3. Click **Delete** to confirm the delete operation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
