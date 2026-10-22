---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-do-not-call/
title: Do Not Call for HubSpot \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:10:43.928098+00:00
---

# Do Not Call for HubSpot  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-do-not-call/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Do Not Call for HubSpot Stay organized with collections  Save and categorize content based on your preferences. 

You can configure your HubSpot integration so the HubSpot call adapter warns agents when they're about to call a Do Not Call phone number for a company or contact. You can configure whether a number triggers the Do Not Call warning based on the phone number type: phone or mobile phone. As a result, one phone number associated with a contact or company can trigger a Do Not Call warning, while another phone number on the same record won't.

Do Not Call is for manual and click-to-call HubSpot outbound calls. It doesn't work for campaign calls.

## Before you begin

Before you begin, do the following:

  * Integrate HubSpot with your Contact Center AI Platform (CCAI Platform) instance. For more information, see [HubSpot](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot).

  * Configure [HubSpot account lookup](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-lookups) for the contact or company lookup objects that you want CCAI Platform to check for Do Not Call information.

  * In HubSpot, configure one or more contact or company properties as opted out of sales or marketing calls.




## Configure Do Not Call for HubSpot

To configure Do Not Call for HubSpot, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **CRM** pane, click the **Do-not-call Configuration** toggle to the on position.

  3. To create a Do Not Call configuration, do the following:

     1. Click **Add**. The **Add configuration** dialog appears.

     2. In the **Object Type** field, select the object type that you want to configure Do Not Call for. Only the object types that you configured as a [primary lookup object](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-lookups#configure-primary-lookup) or a [secondary lookup object](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-lookups#configure-secondary-lookup) appear.

     3. In the **Phone Number Field** field, select the phone number type.

     4. In the **Do-Not-Call CRM Field** field, select the object's field that indicates that this is a Do Not Call phone number.

     5. In the **Opt-out Value** field, enter one or more of the values that specifies that the phone number is Do Not Call.

     6. Click **Add configuration**. The configuration appears in the configuration list.

  4. To create additional Do Not Call configurations, repeat the previous step.

  5. Click **Save**.




## Example Do Not Call configurations

The following table shows example Do Not Call configurations:

Object Type | Phone Number Field | Do-Not-Call CRM Field | Opt-out Value  
---|---|---|---  
Contact | Phone Number (phone) | TPS Status | Opted out  
Contact | Mobile Phone Number (mobilephone) | Do not call | true  
Contact | Mobile Phone Number (mobilephone) | Phone Consent | No  
Company | Phone Number (phone) | Marketing Preference | DNC  
  
With these configurations:

  * The contact's phone number and mobile phone number are checked for Do Not Call independently of one another.

  * The contact's mobile phone number is checked using two different Do Not Call CRM fields: `Do not call` and `Phone Consent`.

  * The contact's phone number is checked using a single Do Not Call CRM field: `TPS Status`.

  * The company's phone number is checked using a single Do Not Call CRM field: `Marketing Preference`.




The **Phone Number Field** values in the tables are standard HubSpot properties that you can't change. The other values in the table are examples that depend on how you configure HubSpot.

## The Do Not Call workflow

This section describes the workflow that takes place when an agent places a call with a HubSpot integration that you've configured for Do Not Call.

Here's the workflow:

  1. An agent initiates a call using the HubSpot call adapter.

  2. CCAI Platform performs a [HubSpot account lookup](https://docs.cloud.google.com/contact-center/ccai-platform/docs/hubspot-lookups) for a contact object, a company object, or both, depending on how you've configured account lookups.

  3. For each returned HubSpot record, the system checks each Do Not Call configuration that you created in Configure Do Not Call for HubSpot, looking for the following matches (matching isn't case-sensitive):

     * The **Object Type** value in the configuration matches the object type of the returned record.

     * The **Phone Number Field** value in the configuration matches the phone number type that the agent called (phone or mobile phone number).

     * The **Do-Not-Call CRM Field** value in the configuration matches a Do Not Call field name in the returned record.

     * One or more of the **Opt-out Value** values in the configuration matches the value of the Do Not Call field in the returned record.

  4. If all of the matches are found for a returned record, the call is considered "Do Not Call" and the HubSpot call adapter displays the following Do Not Call warning:

`This number is on the Do Not Call list`

  5. Depending on your company policy and the current use case, the agent can do either of the following:

     * Stop and don't place the call.

     * If needed, place the call. The system sends the following message to HubSpot:

`The contact is in TPS, the agent chose to proceed with the call.`


**Note:** If the account lookup is unsuccessful, the system doesn't display the Do Not Call warning and the call proceeds normally.

## Turn off Do Not Call for HubSpot

To turn off Do Not Call for HubSpot, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click menu **Menu**.

  2. In the **CRM** pane, click the **Do-not-call Configuration** toggle to the off position.

  3. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
