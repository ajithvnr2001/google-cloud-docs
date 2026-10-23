---
url: https://docs.cloud.google.com/looker/docs/best-practices/migrate-teams-webhook-to-workflows/
title: Migrate your Teams webhook to Workflows \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:33.640856+00:00
---

# Migrate your Teams webhook to Workflows  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/migrate-teams-webhook-to-workflows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Migrate your Teams webhook to Workflows Stay organized with collections  Save and categorize content based on your preferences. 

Microsoft is [retiring](https://mc.merill.net/message/MC1181996) the legacy **Office 365 Connectors** in favor of **Power Automate Workflows**.

Connectors will stop working by the end of April 2026.

To ensure that your Looker alerts continue to deliver to Teams, you must replace your current webhook URL with a new "Workflow" URL.

## Phase 1: Create the new webhook in Microsoft Teams

  1. Open Microsoft Teams and navigate to the channel where you want to receive alerts.
  2. Click the **three dots (...)** menu in the channel and select **Workflows**.
  3. In the search bar, type "webhook" and select the template titled "Post to a channel when a webhook request is received".
  4. Follow the setup prompts:

     * **Name:** Give the workflow a descriptive name (for example, "Looker Alerts - Sales").
     * **Connections:** Ensure that you're signed in to the Microsoft Teams connector.
     * **Details:** Confirm that the team and channel are correct.
  5. Click **Add Workflow**.

  6. Once created, a URL will be displayed. **Copy this URL immediately.** This is your new webhook endpoint.




## Phase 2: Update the URL in Looker

  1. Go to your Looker instance and navigate to the **Admin > Actions** panel or to the specific Looker schedule where the webhook is configured.
  2. Locate the **Microsoft Teams** action.
  3. Delete the old URL (which likely starts with `outlook.office.com`) and paste the new URL (which likely starts with `prod-XX.region.logic.azure.com`).
  4. Test the connection by sending a test payload from Looker to ensure that the message appears in your Teams channel.



## Why is this migration necessary?

  * **Infrastructure change:** Microsoft is moving the backend of webhooks from the old "Connectors" service to "Power Automate."
  * **URL expiry:** The old URLs will eventually stop accepting data, resulting in `404` or `Expired` errors in your Looker logs.
  * **Backward compatibility:** Even though you are using a new "Workflow" URL, the existing Looker message format (**MessageCard**) is still supported.



## Troubleshooting note

  * **Permissions:** If you don't see the **Workflows** option in your Teams channel, your IT administrator may have restricted the **Workflows (Power Automate)** app. You will need to ask your admin to enable the app for your account.
  * **Rate Limits:** The new Workflows service has different rate limits than the old connectors. If you send hundreds of alerts per minute, you may encounter `429 Too Many Requests` errors.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
