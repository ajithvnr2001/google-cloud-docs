---
url: https://docs.cloud.google.com/looker/docs/making-announcements-to-your-users/
title: Making announcements to your users \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T21:06:28.454975+00:00
---

# Making announcements to your users  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/making-announcements-to-your-users/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Making announcements to your users Stay organized with collections  Save and categorize content based on your preferences. 

If your company uses the [Looker pre-built homepage](https://docs.cloud.google.com/looker/docs/finding-content#viewing_content_on_your_homepage), admins or users who have the [`manage_homepage` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_homepage) can share text, links, and images with all Looker users in the right-hand announcement sidebar:

![](https://docs.cloud.google.com/static/looker/docs/images/admin-curated-sidebar-2412.png)

If the announcement sidebar has been closed, it can be re-opened by selecting **Welcome Guide** from the **Help** menu in the Looker header.

Admins and users who have the [`manage_homepage` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_homepage) can add or edit the sidebar. Before content is added to the sidebar, non-admin users will see the pre-built homepage without the sidebar. Admins and users who have the [`manage_homepage` permission](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_homepage) will see prompts to add content to the sidebar.

**Note:** For Looker (Google Cloud core) instances, the [**Discover** sidebar](https://docs.cloud.google.com/looker/docs/finding-content#viewing_content_on_your_homepage) appears instead of the announcement sidebar until the user closes the **Discover** sidebar by clicking the **Close** close icon. Once the **Discover** sidebar is closed, the announcement sidebar appears.

## Adding a card

  1. At the top of the sidebar, click **\+ Add New Card**.
  2. Under **Title** , enter a title for the card. The title appears as header text that is always visible on the card. Titles that are more than 25 characters long may not display properly — the end may be cut off.
  3. Optionally, enter the following: 
     * **Description** : Text that appears after the title on the card. The **Description** field has a 250-character limit.
     * **Link** : URL that opens in a new browser tab when a user clicks on the card. Enter the full URL, including the `https://` or `http://`. The URL path does not appear to the user, but the card title and text will appear blue if the card is a link or will appear black if the card is not a link. You can also use the **Description** field to add a text description of the link target, such as its title.
     * **Upload Image** : Click the **Upload Image** button to upload an image that appears in the card.
  4. When your new card is finished, click **Create**.



## Editing a card

  1. Click the three-dot **Content Card Menu** icon on the card you would like to edit, and select **Edit**.
  2. Optionally, edit the following: 
     * **Title** : Bold text that is always visible on the card
     * **Description** : Text that appears after the title on the card
     * **Link** : URL that opens in a new browser tab when a user clicks on the card
  3. Optionally, click the trash bin icon to delete the card's image. If you want to upload a new image, click **Upload Image** to navigate to and upload a new image for the card.
  4. Select **Save** to save the card.



## Changing a sidebar title or description

  1. Hover over the sidebar title or description to reveal the **Edit** pencil icon. Click the **Edit** pencil icon.
  2. Select the existing title or description and replace it with a new sidebar title or description.
  3. To save changes, click the **Done** checkmark icon.



## Rearranging cards

Click and drag the six-dot **Drag handle** icon in the bottom left of a card to move the card's order in the sidebar.

## Deleting a card

  1. Click the three-dot **Content Card Menu** icon on the card that you would like to edit, and select **Delete**.
  2. To confirm the deletion, click **Confirm**.



## Linking to Markdown documents

You can write documentation, announcements, or information for [Looker projects](https://docs.cloud.google.com/looker/docs/how-project-works) using [GitHub-flavored Markdown](https://guides.github.com/features/mastering-markdown/) and link to the [documentation files](https://docs.cloud.google.com/looker/docs/other-project-files#document_files) in the sidebar.

Users with develop privileges can navigate to and obtain the URL for a Markdown document by following these steps:

  1. [Navigate to the project](https://docs.cloud.google.com/looker/docs/accessing-project-files).
  2. Select the name of the document (or [create a new document](https://docs.cloud.google.com/looker/docs/other-project-files#creating_documentation_files)).
  3. From the document menu, select **View Document**.
  4. From the new browser window, copy the URL for the document.
  5. Paste the Markdown file URL into the **Link** field of a sidebar card.



Now, users can click that sidebar card and Looker will open the document in a new browser tab.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
