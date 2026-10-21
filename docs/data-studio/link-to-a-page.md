---
url: https://docs.cloud.google.com/data-studio/link-to-a-page/
title: Link to a page or component \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T06:54:18.749856+00:00
---

# Link to a page or component  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/link-to-a-page/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Link to a page or component Stay organized with collections  Save and categorize content based on your preferences. 

You can provide links that take viewers to specific pages in a report, or to specific components on a report page.

## Create a text link

To create a link from a text component:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. In the toolbar on the top of the page, click **Text** text_fields.
  3. Enter the text to display, for example, "Page 2."
  4. Select the text you just entered; then, on the right, click **Insert link**.
  5. Click **Paste a link or select a page**.
  6. Select a page in this report, choose a dynamic link, or paste a link to a component that you've copied to your clipboard. See Link to pages in this report, Dynamic page links, and Link to a component for more information.



You can also [create a link button](https://docs.cloud.google.com/data-studio/add-buttons) for users to access on the report.

## Link to pages in this report

Select the specific page name to which you want to link. If you reorder the pages in the report, the link continues to point to the selected page.

## Dynamic page links

Dynamic links navigate to pages in the report based on their position:

  * **First** : goes to the first page in the report.
  * **Previous** : goes to the page before the current page, if any.
  * **Next** : goes to the page after the current page, if any.
  * **Last** : navigates to the last page in the report.



If you reorder the pages in the report, dynamic links adjust so as to point to the new pages occupying the first, last, next, and previous positions.

## Link to a component

You can link to a specific component, like a chart or control, in your report. When viewers click the link or access its URL, Data Studio navigates to the report page containing the component and scrolls to that component's position on the page.

To get a link to a component:

  1. [View](https://docs.cloud.google.com/data-studio/ways-to-share-your-reports) or [edit](https://docs.cloud.google.com/data-studio/edit-a-report) your report.
  2. Hover over the component that you want to link to, then do one of the following: 
     * In the component header, click **More** more_vert, then select **Link to component**.
     * Right-click on the component, then select **Link to this component**.
  3. A dialog opens with the link to the component.
  4. Optional: The checkbox "Link to current report view" is checked by default. Clear this checkbox if you don't want the link to include the filter settings that you have applied.



### Notes on modifying linked components

Note the following considerations when using components with links:

  * If you copy a component with a link and paste it, the link will still direct to the original component.
  * If you cut a component with a link and paste it, the link will no longer direct to any component.



## Copy page links

When copying reports and page link components, keep in mind the following:

When [making a copy of an entire report](https://docs.cloud.google.com/data-studio/copy-a-report), page links are adjusted to point to the correct pages in the copy.

If you copy and paste a text component with a page link, the link will work as expected as long as it points to a valid target. For example, if you copy a dynamic link to the next page and paste it into a report's last page, the link won't do anything, since there is no next page to go to. Similarly, if you copy a link to a page called "Sales Performance" and paste it into a report with no such page, you'll need to select a new valid target for the link.

## Links to hidden or non-existent pages

Links to hidden pages or to pages that no longer exist don't go anywhere. If you link to a component that is later deleted, the link will navigate to the top of the page that contained the component.

**Important:** If you remove a page that is the target of a page link, and then add a page with the same name, you'll need to reset the link target to the new page. This is because internally page links use the page's unique identifier, rather than the page name, as the link target.

## Link to a page from another report or site

To link to a specific page in one report from another report, navigate to the target page, then copy the URL in your browser's location field. You can then use that URL as the destination in the **Insert link** dialog. You can also email the link, or use it in a website to direct viewers to that page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
