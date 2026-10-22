---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/using-dynamic-variables-in-email-html-templates/
title: Add variables to email templates \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:23:45.788657+00:00
---

# Add variables to email templates  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/configuration/using-dynamic-variables-in-email-html-templates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Add variables to email templates

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to use dynamic variables in email HTML templates to create reusable and customizable email content within Google Security Operations.

## Create the email HTML template

You can create the email HTML template with a fixed subject header and title. The `{Text}` placeholder lets playbook builders manually insert content when they create a new playbook.

To do this, follow these steps:

  1. Go to **Settings > Environments > Email HTML templates**.
  2. Add a new template and give it a name. For example, `Testing Text Option`.
  3. In the template body, make sure you include the `{Text}` placeholder. This placeholder will be replaced with the custom content provided in the playbook.
  4. Click **Add**.



### Add the template to a playbook

  1. In your playbook, drag in a **Send Email** action.
  2. Choose the specific template: click the list and select **Testing Text Option**. 
  3. In the **Content** field, enter the body of your email. This content will replace the `{Text}` placeholder when the playbook runs.
  4. Click **Save**.
  5. When an alert is ingested into the Google SecOps platform, the playbook runs and triggers an email. The system renders the email template, inserting the content from the **Content** field into the `{Text}` placeholder before sending the email to the recipient.



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
