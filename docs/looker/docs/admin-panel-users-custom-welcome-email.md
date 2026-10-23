---
url: https://docs.cloud.google.com/looker/docs/admin-panel-users-custom-welcome-email/
title: Admin settings - Custom welcome email \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:13.408697+00:00
---

# Admin settings - Custom welcome email  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-users-custom-welcome-email/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - Custom welcome email Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances do not include this page.

## Overview

On the **Custom Welcome Email** page in the **Users** section of the **Admin** menu, you can customize the body of the welcome email that is sent to new users inviting them to activate their accounts. Using HTML, you can specify custom formatting, links, and images. This can be useful, for example, when you want to provide new users with helpful information and resources to help them get started with Looker.

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

## Enabling custom welcome emails

To create custom body content for welcome emails, navigate to **Custom Welcome Email** in the **Users** section of the **Admin** panel.

Switch on the **Use custom HTML for welcome email body** toggle on the **Customize Your Welcome Email Copy** page.

If the switch is turned off, Looker will display the default welcome email.

## Creating a custom welcome email

When custom welcome emails are enabled, Looker displays a box with the content of the welcome email. Using HTML, you can edit the body of the welcome email by adding formatting, links, and images.

The subject line "Welcome to Looker," the heading "You've been invited to join Looker!" at the top of the welcome email, and the **Activate Your Account** button cannot be customized and will appear in all welcome emails. Clicking on the **Activate Your Account** button in the email opens the page for users to create a new account.

For a list of HTML and CSS that Looker supports, see the [HTML sanitization](https://docs.cloud.google.com/looker/docs/html-sanitization) documentation page.

## Testing custom welcome emails

To test your new welcome email, save your changes by selecting **Save Changes** , then click the **Send Test Email** button at the bottom of the **Custom Welcome Email** page. This sends an example of your custom welcome email to the email address that is associated with your Looker account.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
