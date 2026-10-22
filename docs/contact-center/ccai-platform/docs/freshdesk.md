---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/freshdesk/
title: Freshdesk \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:26.410000+00:00
---

# Freshdesk  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/freshdesk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Freshdesk Stay organized with collections  Save and categorize content based on your preferences. 

The Contact Center AI Platform (CCAI Platform) is able to integrate with Freshdesk CRM Customer Engagement Center.

  * Automatic CRM record updates through seamless real-time data exchange, which significantly reduces handle times and post-call work for agents.

  * Call records, chat transcripts, consumer uploaded media files, and any pass through custom data.

  * CCAI Platform agent call and chat adapters are available when signed in to the CCAI Platform portal. This includes support of the smart actions feature for IVR and mobile calls, and features user authentication, screenshots, parallel SMS messaging, and real-time multimedia sharing.




## Feature availability

|   
---|---  
**Feature** | **Availability**  
SmartActions | Supported  
Custom Field Mapping | Future feature  
CSAT by IVR | Supported  
Custom Callback Number | Supported  
User Segment DAP | Supported  
API DAP (Basic Auth) | Supported  
API Batching | Not planned  
Custom contact field matching | Not supported yet  
Click to Call | Unable to support due to CRM restriction  
Default Admin User | Supported  
Flexible Outbound Calling | Supported  
Secondary account lookup | Unable to support due to CRM restriction  
IVR API lookup | Not supported yet  
Chat transcription attachment | Supported  
  
## Retrieve your Freshdesk API Key

In this section, we will guide you to set up an initial connection between CCAI Platform and Freshdesk by finding the required subdomain information and adding it into the CCAI Platform portal developer settings.

### Prerequisites

  * Account with Administrator access in Freshdesk


  1. Log into Freshdesk using an account with Administrator permissions.

  2. Click your profile picture in the upper right and select **Profile Settings** from the drop-down.

  3. The **Your API Key** field is displayed near the **Profile Settings** screen.

  4. Copy the API Key.




## CCAI Platform configuration of Freshdesk

This section provides guidance on the configuration of Freshdesk with CCAI Platform.

### Prerequisites

  * Your API Key from Freshdesk

  * User with Admin role assigned in the CCAI Platform portal to access Developer Settings




### Configuration steps

  1. Sign in to the CCAI Platform portal, go to **Settings** > **Developer Settings**

> **CRM**.

  2. Select **Freshdesk** as the **Agent Platform**.

  3. In the Freshdesk subdomain field, enter the subdomain for your Freshdesk CRM (i.e., subdomain.freshdesk.com).

  4. Paste the API key from Freshdesk in the **API Key field**.

  5. Use the **Phone Number Format** drop-down to select the format used for phone number lookups and how the phone number is formatted in the Freshdesk record. Available options are:

Automatic: Create: +1 222 333 4444, Search: *222*333*4444

E.164: +12223334444

US Local: 2223334444

US local standard: (111) 222-3333

International: +1 222 333 4444

  6. Select the **Attach session metadata files to CRM records option** to include the session metadata file as part of the record in Freshdesk.

  7. The session metadata file includes detailed information about a session and is sent approximately 15 minutes after the session is ended as a JSON file.

  8. For more information, refer to [Session Metadata File](https://docs.cloud.google.com/contact-center/ccai-platform/docs/crm-session-metadata).

  9. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
