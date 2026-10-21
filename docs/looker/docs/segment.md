---
url: https://docs.cloud.google.com/looker/docs/segment/
title: Sharing data to Segment \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:10:52.326937+00:00
---

# Sharing data to Segment  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/segment/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Sharing data to Segment Stay organized with collections  Save and categorize content based on your preferences. 

With the [Segment integration](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions#list_of_integrated_services), available in the [Looker Action Hub](https://docs.cloud.google.com/looker/docs/action-hub#the_looker_action_hub), you can send Looks and Explores to a variety of integrations managed by Segment, including third-party applications like Marketo, Hubspot, and [others](https://segment.com/docs/connections/sources/catalog/cloud-apps/looker/).

To start using Segment in Looker:

  1. A Looker admin sets up a Segment integration. This step is only required once.
  2. A Looker developer sets up Segment tags. This step is only required once.
  3. A Looker user selects Segment as the destination of a delivery.



## Setting up a Segment integration

**Note:** You must be a Looker admin to set up a Segment integration.

To set up a Segment integration:

  1. In your Segment workspace, search the **Catalog** for the Looker source and select it.

  2. In **Source setup** , give your source a name (typically `Looker`), and select **Add Source**.

  3. Segment will display a write key for your source. Copy this write key.

  4. In your Looker instance, navigate to the **Actions** page in the **Platform** section of the **Admin** panel.

  5. Select **Enable** next to the Segment action you want to enable.

  6. Paste the Segment write key from step 3 into the **Segment Write Key** field.

  7. Select **Save**.




To finish setting up your Segment integration, add Segment tags to your LookML model.

## Adding Segment tags to your LookML model

To send or schedule Looks and Explores with Segment attributes, first add [LookML tags](https://docs.cloud.google.com/looker/docs/reference/param-field-tags) to the appropriate fields in your Looker model. For a complete list of allowed tags for each action, see the [tags (for fields)](https://docs.cloud.google.com/looker/docs/reference/param-field-tags) documentation page.

Most actions require at least the `email` and `user_id` tags. Add these tags to the fields in your LookML model that correspond to Segment user email addresses and user IDs, respectively. For example:
    
    
    dimension: email {
      sql: ${TABLE}.email ;;
      tags: ["email"]
    }
    
    dimension: user_id {
      sql: ${TABLE}.user_id ;;
      tags: ["user_id"]
    }
    

**Note:** Without the correct user ID, your data will not be delivered to your supported integrations. You can see the required IDs for each supported Segment integration in the [Segment documentation](https://segment.com/docs/sources/cloud-apps/looker/).

## Sending a Look or an Explore to Segment

Once you have set up the Segment integration and defined LookML tags, you can send Looks and Explores to Segment.

  1. [Create a Look](https://docs.cloud.google.com/looker/docs/saving-and-editing-looks) or [build an Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores) using one or more fields with a Segment LookML tag.

  2. Select the gear icon. For Looks, select either **Send** or **Schedule**. For Explores, select either **Send** or **Save and schedule**.

  3. Select your Segment destination.

  4. Configure [other delivery settings](https://docs.cloud.google.com/looker/docs/delivering-looks-explores#creating_a_delivery) as desired and select **Send** or **Save**.

**Note:** Your payload will be delivered in JSON format.
  5. Confirm that Segment is receiving your Segment attributes using the [Segment debugger](https://segment.com/docs/connections/sources/debugger/).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
