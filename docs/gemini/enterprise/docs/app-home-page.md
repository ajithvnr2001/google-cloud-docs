---
url: https://docs.cloud.google.com/gemini/enterprise/docs/app-home-page/
title: Configure the app home page \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:41.276167+00:00
---

# Configure the app home page  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/app-home-page/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure the app home page Stay organized with collections  Save and categorize content based on your preferences. 

The home page serves as the central hub for accessing key features and information within your app. It provides navigation to important areas of the app and enhances user productivity by offering quick access to commonly used resources. The key items on the home page include personalized announcements, shortcuts, and other customizable elements designed to streamline the user experience. These tools allow users to efficiently interact with essential internal resources, stay updated on the latest announcements, and manage their day-to-day tasks with ease.

  * Create and manage announcements
  * Show new team member announcements
  * Create and manage shortcuts



## Create and manage announcements

Announcements are used to display important updates, news, and notifications for all end users. These announcements appear prominently on the home page, so that key messages reach the entire organization. The primary purpose is to broadcast company-wide information, such as top news, policy changes, and upcoming events.

An administrator configures the items that appear on the home page. End users can see only these configured items.

Announcements can be viewed only in the app. They can't be targeted to specific groups.

### Before you begin

Before creating announcements, verify you have already set up an app with connected data stores.

### Create announcements

Set up announcements to share important news with your organization. Configure details such as title, description, images, links, and scheduling so that the announcement reaches users at the right time.

To create announcements:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Go to the **Data Stores** page and click add **Create Data Store**.

  3. Select **Announcements**.

  4. In the **Configure your data store** pane, enter a name for your data store and click **Create** to create your announcement data store.

  5. Go to your announcement data store, and, in the **Announcements** pane, click **+New** to create an announcement.

  6. In the **New announcement** pane, fill in the following fields:

     * **Title** : Name of the announcement.
     * **Description** : Describe your announcement.
     * **Image URL** : The URL for an image that represents the announcement. **Note** : The **Image URL** must be accessible to all users within the organization.
     * **Link URL** : The URL for a link that represents the announcement.
     * **Start date** : Enter the start date of your announcement.
     * **End date** : Enter the end date of your announcement.
  7. Click **Publish** to create a new announcement.

  8. To see the announcements for a data store, go to the **Data Stores** page and click the name of the announcements data store.




The app displays the announcement only if the current date falls within the specified start and end times. It sorts announcements in descending order by start time.

### Manage announcements

Announcements are managed similarly to how regular data stores are, but offer a custom UI for creating and updating individual rows of announcements.

## Show new team member announcements

New team member announcements welcome people who recently joined. These cards are shown in the announcements area of the home page. Each user sees only recent joiners from their own part of the organization, not every new hire in the company.

### Limitations

  * People data from Google Workspace isn't supported.



### Enable new team member announcements

To enable new team member announcements, do the following:

  1. Make sure that your people data includes each person's hire date and management chain. These appear in a person's record as the `hireDate` and `managers` fields:
         
         {"id":"jdoe","structData":{"personId":"jdoe","hireDate":"2025-06-02T00:00:00Z","managers":[{"personId":"asmith"},{"personId":"bwong"}]}}
         

  2. Create an announcements data store and connect it to your app. For more information, see Create and manage announcements.

  3. Connect a people data store to the same app. Supported people data sources include [Microsoft Entra ID](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/entra-id/connect-entra-id) and [People via Custom Connector](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-people-custom) (Preview).




## Create and manage shortcuts

Shortcuts in the app provide users with quick access to commonly accessed links, such as internal document sites, knowledge bases, or frequently used tools. These shortcuts appear on the app's home page, letting your users navigate to important resources without searching through menus. Although shortcuts are optional, they offer a way to boost productivity by reducing the time spent looking for frequently used resources.

The administrator configures items on the home page. Up to six shortcuts can appear on the home page.

### Before you begin

Verify an app is set up before creating shortcuts.

### Create shortcuts

To create shortcuts, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that you want to edit.

  3. In the navigation menu, click **Configurations**.

  4. Click the **Search UI** tab.

  5. Under **Pinned Links / Shortcuts** , click **Add shortcut**.

  6. Fill in the following fields:

     * **Title** : Name of the shortcut.
     * **Icon URL** : Optional: The URL for the icon that represents the shortcut.
     * **Shortcut URL** : The direct link to the resource you provide.
  7. In the **Preview** pane, verify that the shortcut appears correctly.

  8. Click **Save and Publish**.




### Manage shortcuts

Organize shortcuts by reordering and removing them as needed to keep the home page streamlined and up-to-date with the most relevant links.

To rearrange or delete shortcuts, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise** page.

[Gemini Enterprise](https://console.cloud.google.com/gemini-enterprise/)

  2. Click the name of the app that you want to edit.

  3. In the navigation menu, click **Configurations**.

  4. Click the **Search UI** tab.

  5. Under **General configurations** > **Pinned Links / Shortcuts** , click the up arrow or down arrow icons to rearrange the shortcuts.

  6. To delete a shortcut, click delete the delete icon.

  7. Click **Save and Publish**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
