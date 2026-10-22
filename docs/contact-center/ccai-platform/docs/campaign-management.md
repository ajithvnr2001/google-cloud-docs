---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-management/
title: Campaign management \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:10:32.751741+00:00
---

# Campaign management  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Campaign management Stay organized with collections  Save and categorize content based on your preferences. 

Contact Center AI Platform (CCAI Platform) provides the ability to perform outbound calling campaigns. A campaign includes a list of customers that should be contacted and are managed through the CCAI Platform campaign manager.

The default CCAI Platform roles don't include the `Campaigns Manager` permission. Therefore, to get started with campaigns, you need to create a custom role with the `Campaigns Manager` permission and then add it to the user. For more information, see [User roles and permissions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/user-roles-permissions).

## Campaign manager

Users with administrator role can set up the outbound dialer using campaign manager.

The campaign manager allows for the manual control of campaigns (start and pause buttons in the **Action** column).

Creates campaigns in the campaign manager by:

  * Uploading a contact list.

  * Setting the dialing mode.

  * Selecting the target queue.




When a campaign starts, it reserves available agents in the selected target queue and sends them contacts from the campaign contact list, following the flow defined for the selected dialing mode.

**Note:** Prior to uploading a contact list, it must be checked against any and all applicable Do Not Call (DNC) lists.

To access the campaign manager, go to **Campaigns** in the CCAI Platform portal.

The campaign manager includes the following columns:

  * Campaign name

  * Assigned queue

**Note:** When you assign a campaign to a queue, the campaign is not limited to the queue's hours of operation.
  * **Mode:** the type of campaign:

    * **Preview:** a preview campaign has the agent manually dial the contact.

    * **Predictive:** a predictive campaign predicts how many contacts need to be dialed.

    * **Progressive:** a progressive campaign uses reserved agents.

  * **Status:** the current status of the campaign:

    * **Ready:** the campaign is ready to be started

    * **Running:** the campaign is being executed

    * **Paused:** the campaign has been paused, and execution is halted

    * **Completed:** the campaign has completed execution

  * **Action:** change the status of the campaign:

    * **Play:** pause the execution of the campaign

    * **Pause:** temporarily halt the execution of the campaign

  * Total Volume

  * Progress




### Start a campaign

To get a campaign to progress, be sure that the following requirements are met.

  * **Queue:** One queue must be built. See [IVR: Add and edit queues menus](https://docs.cloud.google.com/contact-center/ccai-platform/docs/Queue_and_Menu_Setup).

**Note:** If a queue also is reachable using the IVR menu, the assigned agents will be receiving regular inbound calls as well. This way, you can have blended campaign calls and regular calls. However, you make the queue unreachable, then only campaign calls will be served.
  * **Agent:** One agent must be in Available status. See [Agent statuses](https://docs.cloud.google.com/contact-center/ccai-platform/docs/agent-statuses).




### Action column

The **Action** column is used to start, pause, or restart campaigns. The action buttons available are based on the current execution status of the campaign.

  * For a new campaign, click **Play** to begin the campaign. The status for this campaign will be updated to Running and the refresh cycle for the progress bar will begin.

  * If the campaign execution needs to be placed on hold, click **Pause** in the **action** column. The execution status is set to **paused** and the progress bar will stop refreshing.

  * To resume the execution of a paused campaign, click **Play** again to restart execution of the campaign. The execution status will return to Running and the refresh cycle for the progress bar will be reset.


**Note:** If the campaign is running, **Pause** is displayed in the **Action** column. If the campaign execution has not started or is paused, **Play** is displayed.

Once a campaign has completed, no buttons will be displayed in the **Action** column for that campaign.

### Progress column

The **progress** column indicates the list position of the next contact to be called.

When the green progress bar is full, the campaign has reached the end of the list and the campaign execution status is updated to **Completed**. If the campaign execution is manually paused, the progress bar will also be paused until the campaign is restarted.

Campaign data is processed in real-time and automatically updates the progress bar, the campaign metrics, campaign status, and the action buttons as calls are made.

You can also click the **Refresh** icon to see new campaigns that have been added since your last refresh.

## Outbound dialer campaign call status window

The call status window shows the number of calls from the campaign that fall into each of the various statuses. These metrics provide real-time feedback that allows managers to quickly adjust their strategies for upcoming campaigns and ensure agent productivity. These metrics also provide insight into any data quality issues in their campaign file.

To access the call status window, click the campaign for which you want to view statistics and click the **External link** icon adjacent to the **progress** bar.

### Call status window

In the call status window you can see call volumes by status for various metrics. The metrics available in this window will vary by campaign type.

![Call status window](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ce48e0a5fb.png)

**Reached**

  * **Finished** : Agent connected to end-user.

  * **Call transferred** : Agent connected to end-user, then transferred the end-user to another agent.




**Not Yet Reached**

  * **Queued** : Calls in a queue waiting to be called.

  * **Dialing** : Contacts that are being dialed.

  * **Connected** : Connected calls.

  * **Upcoming** : Number has not yet been called.

  * **Skipped** : The agent clicked **Skip** , which keeps the contact in the campaign (Preview campaigns only).




**Not Reached**

  * **Carrier Error** : Dialer experienced a call error, such as prolonged ringing with no pickup.

  * **General Error** : Any error that does not fall into another error category.

  * **Invalid Number or Name** : Number from the CSV file is in an unsupported format, isn't the right number of digits, is a duplicate within the campaign, or is missing a name.

  * **Not Picked Up** : Calls that were not answered by the end-user.

  * **Skip & Close:** Agent clicked **Skip & close** to take the contact out of the campaign (preview campaigns only).

  * **Abandon by Contact** : The end-user answered, but hung up (for example, a short abandon).

  * **Voicemail Hung Up** : The dialer encountered a voicemail and the agent hung up without leaving a message.




Click  Close  to close the call status window.

## Outbound number

Outbound number is a feature of the outbound dialer that provides the ability to specify which outbound number to use when dialing out for each contact. With this feature, you can rotate outbound phone numbers for more control over the outbound phone numbers you use to make your outbound calls.

You can specify which outbound number to use when dialing out for each contact by adding a new column named **outbound number** to your [campaign management CSV](https://docs.cloud.google.com/contact-center/ccai-platform/docs/campaign-management#add_a_unique_id_for_campaign_reporting). If the outbound number column is missing or the value is not committed, the default outbound phone number will be used.

The dialer will use this number when dialing out if it has been validated on the CCAI Platform. If the outbound number is not validated, the contact will fail and log an error. The outbound number is displayed in the CCAI Platform agent adapter.

## Outbound dialer campaign mode global settings

To enable Campaign Mode at the global settings:

  1. In the CCAI Platform portal, go to **Settings > Campaign**.

  2. On the panel, turn **on** the campaign by clicking the switch next to the campaign you would like to enable.

  3. Click **Save**.




## Add a Unique ID for campaign reporting

The following instructions outline how to add a Unique ID column to a campaign management CSV file for reporting purposes.

The process includes adding a Unique ID column to a CSV file using spreadsheet software, uploading the file to a campaign, running the campaign to populate the data, and viewing the Unique ID in the reporting data.

The Unique ID column in the CSV file has no restrictions on formatting. It accepts both alphanumeric and special characters, with no maximum length enforced. You can use Unique ID to represent any relevant identifier such as a customer ID in another CRM, a SKU, or any other identifier.

### Add a Unique ID column and upload the CSV file to a campaign

  1. Open the campaign CSV file that you want to upload and add a column called `Unique ID`. Save the changes to the CSV file.

  2. In the CCAI Platform portal, go to the **campaign manager**.

  3. Click **+Add campaign**. A campaign settings dialogue will display.

  4. Click **choose file** and select the file with the Unique ID column added.

  5. Click **open** to upload the file.

  6. Select the queue.

  7. Click **Save**.




### Populate data through the campaign for reporting purposes

  1. After the CSV file has been uploaded, the campaign execution status will progress to **Ready**.

  2. Click *_Start_ to start the execution of the campaign.

  3. Wait for the status of the file to change to **Ready**.

  4. Click **Start** to begin the execution of the campaign. Allow the campaign to run for a while.




### View the Unique ID results in detailed campaign reporting

  1. Go to **Reports > Campaigns**.

  2. Under **Step 1: Select Campaign Mode** , choose which type of campaign you want to generate reports on.

  3. Under **Step 2: Select Campaigns** , choose the campaign associated with the CSV file containing a Unique ID.

  4. In **Step 3: Select Reports Desired** , choose the reports you would like to download by checking the box next to the report (options appear based on campaign type selected in Step 1). Be sure to select a **detailed** report.

  5. In **Step 4: Choose Filters** , configure the filter the reports by timeframe or time zone.

  6. Click **Download**.

  7. After the file is downloaded, open it to view the Unique ID column.




### Enable the DNC list

  1. Go to **Settings > Campaigns > Company Do Not Call (DNC) List** and toggle the switch to **ON**. When toggle is set to ON, additional menu options will appear.

  2. (Optional) Check the box to apply the DNC list check to direct, manual outbound calls made by agents in addition to outbound and scheduled calls created by the Apps API.

  3. (Optional) Enable the **Do Not Call Again** disposition code to use this code to add end-users to the DNC list. Both the disposition code and the DNC list itself must be enabled in order for the DNC list to work in conjunction with the disposition code.




After both the DNC feature and Do Not Call Again disposition code are enabled, the DNC list will be continually updated with new contacts tagged with the disposition code. The DNC list contains contact entries with the following fields:

  * `Note`: A string of up to 200 characters.

  * `Phone number`: A phone number to not call.

  * `Timestamp`: The time when the contact was added to the list.

  * `Expires at`: A date and time when the number can be removed from the DNC list.




Contacts are removed from the DNC list within an hour of the expiration time. If this parameter is not set, the number remains on the list indefinitely.

### View the DNC and blocked numbers in Reporting

**Note:** You won't be able to see or download the full DNC list, because the list contains PII.

  * Attempted calls to a blocked number are included in the real-time metrics display.

  * Attempted calls that were blocked by the DNC are included as `dnc_abandoned` with the reason: Company DNC.

  * Numbers on the DNC list are reported in the campaign summary report.




### API commands for the company DNC list

The Company DNC API endpoints allow you to:

  * Add multiple phone numbers to the DNC list simultaneously.

  * Remove phone numbers from the DNC list.

  * Check whether a phone number is on the DNC list.




See the [Apps API documentation](https://docs.cloud.google.com/contact-center/ccai-platform/docs/apps-api-dnc) for complete details.

## Edit a campaign

To edit a campaign that has already been created, follow these steps:

  1. In the CCAI Platform portal, go to **Campaigns**.

  2. Click the campaign you want to update and select the **Edit** icon.

  3. In the **Edit campaign** window, make any necessary changes to the current settings.

  4. Click **Set**.




## Delete a campaign

To delete a campaign, follow these steps: 

  1. Select **Campaigns** in the CCAI Platform portal. 

  2. Select the campaign you want to delete.

  3. Click **Delete** in the far right column.




The selected campaign is removed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
