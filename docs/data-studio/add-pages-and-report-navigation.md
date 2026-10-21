---
url: https://docs.cloud.google.com/data-studio/add-pages-and-report-navigation/
title: Add pages and report navigation \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:25:15.427105+00:00
---

# Add pages and report navigation  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/add-pages-and-report-navigation/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)



Send feedback 

#  Add pages and report navigation Stay organized with collections  Save and categorize content based on your preferences. 

The ability to add pages and navigation options to reports lets you organize related data, improve report performance, and minimize the overall complexity of reports. 

## Add pages and navigation items to a report

To add a page to your report, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. In the report header navigation, select the **New Page** option from the **Page** drop-down menu.



If your report has more than one page, you can also add a new page by following these steps:

  1. Open the **Properties** panel, and click **Page __ of __** in the toolbar to open the **Report Pages** panel. Alternatively, select the **Manage pages** option from the **Page** drop-down menu in the report header navigation.

![A user hovers their cursor over text that reads Page 3 of 4 on report navigation.](https://docs.cloud.google.com/static/data-studio/images/manage-pages-2022-01-25.png)

  2. Click the ![The Create icon.](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Add a page** button to add a page to your report.




You can also click the ![The Create icon.](https://docs.cloud.google.com/static/data-studio/images/rainbow-plus-2019-06-26.png)**Add a page** button in the **Report Pages** panel to add sections, dividers, and headers.

![](https://docs.cloud.google.com/static/data-studio/images/manage-pages-pane-2021-09-06.png)

#### Limits

You can add only three levels of page sections on a single report page.

**Example**

  1. Page (level 1)
  2. Section (level 1) 
     1. Page (level 2)
     2. Section (level 2) 
        1. Page (level 3)



## Navigate between pages and sections

**Report viewers** can navigate between pages and sections in several ways:

  * Use the navigation panel to click a specific page, section, or header name.
  * Use a keyboard: 
    * Left and right arrows, or page up and page down to navigate to the next page or the previous page.
    * Home and end keys to navigate to the first page or the last page.



Report viewers can expand and collapse the navigation panel by clicking the ![Chevron left icon.](https://docs.cloud.google.com/static/data-studio/images/gmchevronleftgmgrey50048dp-2021-10-07.png)**Expand/collapse navigation drawer** button. When the navigation panel is collapsed, page numbers or icons will display in lieu of section or page names.

**Report editors** can navigate between pages and sections in several ways:

  * Click the left and right arrows on either side of the **Page _ of _** button in the toolbar.
  * Use the **Report Pages** panel to click a specific page, section, or header name.
  * Use a keyboard: 
    * Left and right arrows, or page up and page down navigate to the next page or the previous page.
    * Home and end keys navigate to the first page or the last page.
  * Use the **Search** box in the **Report Pages** panel to find a page, section, or header by name.

Note that this doesn't search for text in the report itself.




If you would like the navigation panel to display for report editors, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Select the **Show navigation in edit mode** option from the **View** drop-down menu in the report header navigation.



## Make changes to a page or navigation item

Once you have added navigation items to a report, you can customize and manage them on the **Report Pages** panel.

You can choose from several options:

  * **Rename** : This option lets you rename a page, section, or header
  * **Duplicate** : This option lets you make a copy of a page.
  * **Delete** : This option lets you delete a page or navigation item.
  * **Control visibility** : This option lets you hide sections and pages from report viewers.
  * **Select icon :** This option lets you add an icon to section and page names.
  * **Move :** This option lets you reorder pages, sections, and headers.



### Rename

New pages and sections have the default names **Untitled Page** and **Untitled Section**.

New headers have the default name **Header**.

To rename a new page or a new header, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Open the **Properties** panel, and then click **Page __ of __** in the toolbar to open the **Report Pages** panel. Alternatively, select the **Manage pages** option from the **Page** drop-down menu in the report header navigation.
  3. Hover over a specific item.
  4. Click the ![More options.](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png) three-dot menu icon.
  5. Click the **Rename** option.
  6. Enter a new page or header name in the name text field.
  7. Click outside of the text field, or select **Enter** (PC) or **Return** (Mac) on a keyboard to save your changes.



### Duplicate

Duplicating a page creates a copy of that page in the current report. You can only duplicate individual pages. You cannot duplicate a section or a header of a page.

**Tip:** To copy a page from one report to another report, select all the components on the original page, and then paste them into a page of the target report. This adds any data sources that are used in the original report to the target report. Page style or theme settings won't be copied from the original page. Learn more about [copying reports](https://docs.cloud.google.com/data-studio/copy-a-report).

### Delete

Deleting a page, section, or navigation item removes it from the report.

**Tip:** If you remove a page or section by mistake, you can undo the action by selecting **Undo** from the **Edit** drop-down menu in the report header navigation. You can also use the keyboard shortcuts Ctrl + Z (PC) or Command + Z (Mac). If **Undo** doesn't work (if you've reloaded the report or signed out and back in to Data Studio), you can use [version history](https://docs.cloud.google.com/data-studio/see-whats-changed-in-reports-and-data-sources) to restore a previous version of the report that contains the deleted items.**Important:** Deleting a section will delete all of the pages that are organized in that section.

### Control visibility

The **Control visibility** option lets you hide a page or section so that some or no viewers can see it. You might want to hide a page or section if it contains information that you want only other report editors to see.

#### Hide for all viewers

To hide a page or section for all viewers on a report, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Open the **Properties** panel and then click **Page __ of __** in the toolbar to open the **Report Pages** panel. Alternatively, select the **Manage pages** option from the **Page** drop-down menu in the report header navigation.
  3. Hover over a specific page or section name.
  4. Click the ![More options.](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png) three-dot menu icon.
  5. Click the **Control Visibility** option.
  6. Select **Always hide the page for all viewers in the view mode**.
  7. Click **Confirm**.



When a page or section is hidden on a report, the following things are true:

  * **Report viewers** can't navigate to that page or section.
  * **Report editors** can still see and edit that page or section.
  * That page or section won't appear in PDF downloads.
  * If you copy the report, that page or section will also be copied but will remain hidden.



#### Conditionally hide the page for some viewers

To hide a page or section for a subset of viewers on a report, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Open the **Properties** panel and then click **Page __ of __** in the toolbar to open the **Report Pages** panel. Alternatively, select the **Manage pages** option from the **Page** drop-down menu in the report header navigation.
  3. Hover the cursor over a specific page or section name.
  4. Click the ![More options.](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png) three-dot menu icon.
  5. Click the **Control Visibility** option.
  6. Select **Control page visibility with parameter (variable)**.
  7. Select an existing group membership variable, or click **Create new group membership variable**. 
     * A group membership variable includes the email addresses of the individual users or Google Groups who can view the page.
  8. Click **Confirm**.



#### Unhide a page for all viewers

To unhide a page or section, follow these steps:

  1. Hover over a specific page or section name on the **Report Pages** panel.
  2. Click the ![More options.](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png) three-dot menu icon.
  3. Click the **Control Visibility** option.
  4. Select **Always show the page for all viewers in the view mode**.
  5. Click **Confirm**.



### Select icon

The **Select icon** option lets you search for an icon to add to a page or section name in your report. The icon will appear next to the page or section name in the navigation panel and in the **Report Pages** panel.

To add or replace an icon, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Open the **Properties** panel, and then click **Page __ of __** in the toolbar to open the **Report Pages** panel. Alternatively, select the **Manage pages** option from the **Page** drop-down menu in the report header navigation.
  3. Hover over a specific item.
  4. Click the ![More options.](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png) three-dot menu icon next to a page or section name.
  5. Click **Select icon**.
  6. Use the search option or select a **Category** to find an icon.
  7. Click **Apply**.



If you've added icons, you'll see those icons instead of page numbers when the navigation panel is collapsed with the ![Chevron left icon.](https://docs.cloud.google.com/static/data-studio/images/gmchevronleftgmgrey50048dp-2021-10-07.png)**Expand/collapse navigation drawer** button.

#### Limits

  * Icons can be applied only to the top level of content. Pages within a section, for example, can't have an icon.
  * If you apply an icon, all top-level content will have an icon. If no icon is selected, a default icon will appear for pages and sections.



### Move

Using the **Move** option lets you reorder pages, headers, and sections on your report.

To move a page, header, or section, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Open the **Properties** panel, and then click **Page __ of __** in the toolbar to open the **Report Pages** panel. Alternatively, select the **Manage pages** option from the **Page** drop-down menu in the report header navigation.
  3. Hover over a specific item.
  4. Click the ![More options.](https://docs.cloud.google.com/static/data-studio/images/icmorevertgrey2xweb24dp-2016-03-14-.png) three-dot menu icon next to a page or section name.
  5. Choose one of the following **Move** options: 
     * Move to top
     * Move to bottom
     * Move up
     * Move down



## Reorder pages, sections, and navigation items

As an alternative to the **Move** option, you can quickly change the order of items in the **Report pages** panel by using your mouse to drag and drop items into a new position.

![A user selects and moves a page called Untiled Page to reorder the pages on the Report Pages panel.](https://docs.cloud.google.com/static/data-studio/images/drag-and-drop-2021-09-06.png)

To reorder a page, section, or navigation item, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. Open the **Properties** panel, and then click **Page __ of __** in the toolbar to open the **Report pages** panel. Alternatively, select the **Manage pages** option from the **Page** drop-down menu in the report header navigation.
  3. Hover over a specific item that you wish to move.
  4. Click the move option on the left of the item to drag it up or down to its new position.



## Change report navigation for report viewers

**Left** navigation is the default navigation option for report viewers.

To change the appearance of the page navigation for report viewers, follow these steps:

  1. [Edit your report](https://docs.cloud.google.com/data-studio/edit-a-report).
  2. In the toolbar, click **Theme and Layout**.
  3. Select the **Layout** tab.
  4. Under **View Mode** , select the **Navigation type.**



Page navigation options include the following:

  * **Left** : Pages appear in a collapsible drawer in the left margin of your report. This is the default navigation option for report viewers.
  * **Tab** : Pages appear as tabbed links at the top of the report.
  * **Top Left** : Pages appear in a drop-down menu in the upper left of the report.
  * **Hidden:** No page navigation is displayed.



## Related resources

  * Use [report theme](https://docs.cloud.google.com/data-studio/themes) and [layout](https://docs.cloud.google.com/data-studio/report-and-page-layout) settings to adjust the appearance of the page navigation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
