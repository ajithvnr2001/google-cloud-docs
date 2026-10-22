---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/page-editor/
title: Developing portal content using the page editor \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:18.191593+00:00
---

# Developing portal content using the page editor  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/page-editor/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Developing portal content using the page editor Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Using the page editor, you define your portal content using Markdown or HTML.

## Exploring the page editor

Access the page editor by clicking the name of a page when viewing the list of pages, as described in [Managing the pages in your portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-pages).

The page editor opens:

![Click for larger image](https://docs.cloud.google.com/static/apigee/docs/api-platform/publish/images/page-editor-console.png)![](https://docs.cloud.google.com/static/apigee/docs/api-platform/publish/images/page-editor-console.png)

The page editor lets you:

  * Edit portal content and add Angular Material components in the left pane
  * Use the quick edit toolbar to apply formats or insert Markdown tags quickly
  * Edit page details, such as name, path, and description, in the right pane
  * Manage the visibility for a page in the right pane
  * Preview the portal content
  * Publish or unpublish a page (see [Publish your portal content](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-publish))
  * Manage the page in your navigation menus (see [Set up navigation](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-menus))
  * View the amount of time since the page was last published
  * [Delete a page](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-pages#delete-page)



## Editing content in the page editor

Markdown is a simple formatting language that uses plain text markup that is both easy to read and write. Its syntax is specified using punctuation characters. Markdown is converted to HTML before rendering in your browser.

The **quick edit toolbar** at the top of the page editor provides shortcuts for applying formats (such as bold, italic, and so on) or inserting Markdown tags (such as lists, images, links, and so on).

For a quick summary of Markdown syntax, in the quick edit toolbar, click the info_outline **Information** icon.

The [Markdown syntax quick reference](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/markdown-reference) is displayed.

To undo or redo the last edit, press `Command+z` or `Command+Shift+z`, respectively.

**Note** : When adding links, note the following: 

  * When adding links to other pages and images in your portal, it is recommended that you use relative paths rather than absolute paths to avoid broken links if you later decide to [customize your domain](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/custom-domain). 
  * When adding links to sections within the portal, you need to include the page name followed by the anchor in your link definition. For example, [Link to anchor] (pagename#anchorname)



Markdown is recommended if you want to keep your formatting workflow simple. However, it is not intended to replace HTML. There is a wide range of formatting you can do in HTML that you cannot do in Markdown. For example, you can specify a CSS class for an element in HTML; you cannot do this in Markdown:
    
    
       <p class="class1">
    

You can insert HTML anywhere within the content body by simply entering the HTML tags.

**Note:** When using HTML, note the following: 

  * Markdown syntax is not valid within HTML tags. 
  * You must add a line break between an HTML text block and the Markdown text block that follows it in order for the Markdown content to be formatted correctly. 



For information about HTML tags, see the [HTML5 specification](https://www.w3.org/TR/html5/).

## Adding Angular Material components

[Angular Material](https://material.angular.io/) provides a state-of-the-art UI component library. Angular Material components enable you to quickly and easily construct consistent, responsive, and accessible user interfaces utilizing modern design principles.

### Available components

The portal experience is built using Angular Material, and a limited set of Angular Material components may be used in pages, summarized in the following table.

**Note:** The Home page in the [sample portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/build-integrated-portal#sample-portal) demonstrates how some of these components are used and rendered. A subset of the examples in the following table are based on the Home page contents, with some of the styling removed for readability. Component | Example  
---|---  
[Buttons](https://material.angular.io/components/button/overview) | The following code creates a rectangular button with elevation.`
    
    
    <a mat-raised-button
       href="quickstart">
       Quick Start
    </a>

` The following code creates a circular button with a transparent background that includes the warning icon. The color of the button is defined using the [warn color palette](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-themes#color-palette).`
    
    
    <button mat-icon-button
       color="warn">
       <mat-icon aria-label="Example warning">warning</mat-icon>
    </button>

`  
[Card](https://material.angular.io/components/card/overview) | The following code creates a card. The card includes button and icon components, as well as heading and body text. The color of the button is defined using the [primary color palette](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/api-portal-themes#color-palette).
    
    
    <mat-card
       href="apis">
       <mat-card-header
          color="primary">
             <mat-icon>
                class
             </mat-icon>
             <h1>
                APIs
             </h1>
       </mat-card-header>
       <mat-card-content>
          <p class="home-page-card-content-text">
             Learn about and try our APIs.
          </p>
       </mat-card-content>
       <mat-card-actions>
          <button mat-button>
              View APIs
          </button>
       </mat-card-actions>
    </mat-card>  
  
[Icon](https://material.angular.io/components/icon/overview) | The following code creates a checkmark icon. For a complete list of icons that are supported, see [Material Design - Icons](https://material.io/icons/).`
    
    
    <mat-icon>
       check_circle
    </mat-icon>

`  
[Toolbar](https://material.angular.io/components/toolbar/overview) | The following code creates a simple toolbar with text and a shopping cart icon. `
    
    
    <mat-toolbar color="primary">
       <span>My Store</span>
       <span class="space-buffer"></span>
       <mat-icon>add_shopping</mat-icon>
    </mat-toolbar>

`  
  
## Managing the visibility for a page in your portal

Managing the visibility of a page in your portal is described in [Managing the visibility of a page in your portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-pages#visibility).

## Previewing portal content

To preview the portal content:

  1. Access the page editor as described in [Managing the pages in your portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-pages).
  2. Preview the page.

     1. Click **Save**.
     2. Click **Preview**.
**Note:** Apigee recommends that you preview all portal content before you publish it.



## Publishing portal content

Publishing and unpublishing portal content is described in [Publishing your portal content](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-publish).

## Deleting a page

Deleting pages from the portal is described in [Deleting pages from your portal](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-pages#deleting_pages_from_your_portal).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
