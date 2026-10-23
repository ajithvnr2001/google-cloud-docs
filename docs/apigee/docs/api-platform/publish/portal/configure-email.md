---
url: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-email/
title: Configuring email \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:22.903167+00:00
---

# Configuring email  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-email/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Configuring email Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

By default, the developer portal sends emails in response to certain events. For example, when a new app developer registers on the portal, the portal automatically sends an account verification email to the provided email address.

Configure the following email settings for all email notifications originating from the portal:

  * Configure the SMTP server for all email notifications, as described in Configuring an SMTP server

  * Configure the contents of the email notifications, as described in Configuring email notifications.




## Configure an SMTP server

When a portal is first provisioned, email notifications are sent to portal users from a generic sender address, `noreply-apigee-portals@google.com`. This approach is suitable for evaluation, but you should configure your own SMTP server before launching your portal to users. When you configure the SMTP server, you can also configure the sender address, for example, `no-reply@mycompany.com`.

**Note:** We are not able to document a fixed range of outbound IP addresses that requests from the integrated portal to your SMTP server may be sent from.

To configure the SMTP server:

  1. In the Apigee in Cloud console, go to the **Distribution > Portals** page.

[Go to Portals](https://console.cloud.google.com/apigee/portals)

  2. Click your portal name.

  3. Click **Settings**.

  4. Click the **SMTP** tab.

  5. Configure the SMTP server settings:

Setting | Description  
---|---  
Server URL | Host URL of the SMTP server.  
From Email | Email address used as the sender.  
SMTP Username | User name for the SMTP account.  
SMTP Password | Password for the SMTP account.  
Use Secure Connection? | Select to use a secure connection to the SMTP server.  
Auth Type | Authorization type. Valid values include: SSL, TLS, or STARTTLS. Leave this field blank for no authorization.  
Port | Port number for the SMTP server. The following ports are supported:
     * 465 (SSL)
     * 587 (TLS)
     * 25 (open, no authorization)  
**Note:** At any time, you can reset the default Apigee settings by clicking **Restore Defaults**.
  6. Click **Save**.




## Configure email notifications

Configure email notifications, as described in the following sections:

  * [Configuring email notifications](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/portal-identity-provider#configuring_email_notifications) as part of configuring the identity provider

  * [Configuring notifications for new user account registration](https://docs.cloud.google.com/apigee/docs/api-platform/publish/portal/configure-register-sign-in#notifications) as part of configuring the sign-in experience for user accounts




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
