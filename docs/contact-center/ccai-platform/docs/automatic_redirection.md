---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/automatic_redirection/
title: Automatic redirection \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:09.034931+00:00
---

# Automatic redirection  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/automatic_redirection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Automatic redirection Stay organized with collections  Save and categorize content based on your preferences. 

You can set up automatic redirects of incoming contacts to redirection groups. You can specify the redirection destination for each group, as well as the percentage of incoming traffic that is allocated to each group.

This guide will walk you through the steps to configure and manage the redirection allocation. Note that any existing queues with a single redirect have been ported over to this new configuration and automatically had their percent allocations set at 100%.

### Permissions

To configure automatic deflections, ensure you've granted the **All other features** permission within the **User & Teams settings: Roles and Permissions**.

You can enable **All other features** within the **Settings - Queue** section on the **Roles and Permissions** page.

### Enable automatic redirection

To enable automatic redirections, follow these steps:

  1. Go to **Settings > Queue > IVR > [all queue levels]** to access the **Automatic Redirection** percent allocation configuration. On the **Settings for Queue** page, locate the **Automatic Redirection** section.

![The IVR menu settings with the Settings for Queue options is shown.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/ivr-menu-settings-for-queue.png)

  2. Toggle the switch to enable automatic redirection at the queue level if it's not already enabled. Select **Configure**.

  3. Set the percent allocation for automatic redirection. Ensure that the total allocation does not exceed 100%. You can add up to 100 redirects.

![The automatic redirection options are shown, along with the allocation groups.](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/automatic-redirection-options.png)




### Create redirection groups

  1. Go to the *_Settings for Queue_ page **Automatic Redirection** section (navigation above).

  2. Click the **Add Group** button to create a new redirection group. The default redirection percentage will be 0 for any new group.

  3. Assign a label to the redirection group for identification.

  4. Configure the percentage allocation for the group. The total allocation across all groups must not exceed 100%.

  5. Select the redirection destination for the group (for example: messages, queues, phone numbers, voicemail, outbound SIP transfers).

  6. Configure after hours deflection settings if needed.




### Manage redirection groups

  1. **Edit Group** : click the **Configure** button to edit the settings for a specific group.

  2. **Delete Group** : use the **Disable** button to delete a redirection group if necessary.

  3. **Adjust Allocation** : update the percentage allocation for each group as needed. The first group will automatically adjust based on changes to other groups.




### After hours deflections

  1. If after hours deflection is required, enable the **After Hours** toggle switch for the redirection group.

  2. Configure custom after hours deflections such as voicemail, alternative queues, or message playback.

  3. Ensure correct percentage levels for after hours deflections based on your business needs.




### Saving and back options

After making changes, click the **Save** button to save your settings.

Use the **Back to Settings** button to return to queue configurations after saving.

### Logging

The `percentage_redirection` parameter indicates whether a call is routed through percentage redirection or not.

#### Example

This JSON snippet represents a scenario where `call id 200` was redirected to `Redirection Group 2`, which triggered outbound SIP redirection during after hours.
    
    
    {
      "id": 200,
      ....
      "automation_redirection": {
        "percent_redirection": true,
        "redirection_group_settings": [
          {
            "group_label": "Redirection Group 2",
            "destination": null,
            "after_hours": true,
            "ah_destination": {
                "type": "SIP",
                "sip_address" : "sip:1-999-123-4567@voip-provider.example.net"
               }
          }
    

#### Redirection Types

The redirection type and destination recorded when applicable:

**Message**
    
    
    "type": "Message"
    

**Phone**
    
    
    "type": "Phone Number","phone_number" : "+12016441484"
    

**Queue**
    
    
    "type": "Queue",
    "queue_id" : 2938,
    "queue_lang" : "en"
    

**Voicemail**
    
    
    "type": "Voicemail"
    

**SIP**
    
    
    "type": "SIP",
    "sip_address" : "sip:1-999-123-4567@voip-provider.example.net"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
