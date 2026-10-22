---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot/
title: HubSpot \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:48.532773+00:00
---

# HubSpot  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  HubSpot Stay organized with collections  Save and categorize content based on your preferences. 

The steps below will establish the initial connection between Contact Center AI Platform (CCAI Platform) and HubSpot by locating and providing the relevant domain information to the CCAI Platform portal.

## Prerequisites

The Admin must locate the following two parameters in order to set up Hubspot integration:

  * HubSpot Domain ID

  * API Key




## Supported features

**Note:** The HubSpot integration does not currently support the storage of media files, such as content sent via blended SMS or MMS messages.

  * SmartActions

  * CSAT over IVR v1

  * Custom Callback number

  * API DAP (Basic Auth)

  * Flexible inbound call

  * Chat transcription attachment

  * Force use provided ticket ID




## Configure HubSpot

  1. Log in to HubSpot using an account with Administrator credentials.

  2. In the URL address locate the customer's Hubspot URL and write down the **Domain ID** number.

  3. Create a private app in HubSpot and generate an access token, which is a Private App Auth Token, within the app. For more information, see [Developer platform](https://developers.hubspot.com/docs/apps/developer-platform/build-apps/overview) in the HubSpot documentation.

  4. Save the token.

  5. In the **Active API Key** field, click the **Copy** link.

  6. Sign in to the CCAI Platform portal with Admin permissions.

  7. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  8. For **Agent Platform** , select **HubSpot**.

  9. In the **HubSpot Domain ID** field, enter the domain ID from step 2.

  10. In the **Private App Auth Token** field, enter the Active API key from step 5.

  11. For **CRM Record Type** , select a CRM record type. This determines which object type (tickets or deals) is used for CRM record lookup. If you select **Service > Tickets**, then **CRM Ticket View** appears.

  12. If **CRM Ticket View** appears, select a CRM ticket view:

     * **Standard view** : the standard HubSpot ticket view

     * **Help desk view** : the HubSpot helpdesk view, which provides real-time updates

  13. Optional: For **Calls** , select the **Attach call data directly to the Call object** checkbox to push call data directly to the call object.

This data includes call data such as status, length of call, call started and finished, call recording, and associations to tickets, deals or users.

  14. If **Sales > Deals** was selected as the CRM Record Type, the Pipeline and Stage dropdowns will display and are used when creating a new deal. Use these fields to indicate the status of the deal (CRM record).

**Note:** The Pipeline and Stage fields are required.
  15. Use the **Phone Number Format** menu to select the format used for phone number lookups and how the phone number is formatted in the HubSpot record. Select **Automatic** as the format type unless your phone numbers are stored in a specific format in the CRM.

The available format options are:

Automatic: Create: +1 222 333 4444, Search: *222*333*4444

E.164: +12223334444

US Local: 2223334444

US Local Standard: (111) 222-3333

National: (111) 222-3333

International: +1 222 333 4444

  16. Select the **Attach session metadata files to CRM records** option to include the session metadata file as part of the record in HubSpot.

The session metadata file includes detailed information about a session and is sent approximately 15 minutes after the session is ended as a JSON file. For more information, please see the Session Metadata File

  17. Use the **Custom** fields for records section to automatically create custom fields for CRM records via API and push session data to those fields.

**Important:** Creating fields in the CRM is a one-way process and cannot be undone from the CCAI Platform portal.
  18. Click **Save**.




## Data passed to the CRM

**Note:** This integration currently does not save SMS media files in the CRM.

Once HubSpot has been integrated, the Admin Portal can pass **call data** to the CRM automatically.

This data is attached to the Call object in HubSpot _by default_ and includes:

  * the call duration

  * a copy of the call recording (in .wav format)




The Call object also includes a description of the call at the top of the screen to describe what has been done, such as _IVR call Completed_.

You can select the outcome of the call such as _Connected_ , _No answer_ , or _Left voicemail_ , using the **Select an outcome** dropdown at the top of the window.

The Call information is associated with the Contact record in HubSpot as well as either the **Ticket** or **Deal** object, depending on the configuration in the Admin Portal.

To see where else this information has been shared, click **Associations**.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
