---
url: https://docs.cloud.google.com/looker/docs/admin-panel-platform-smtp/
title: Admin settings - SMTP \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:07.696452+00:00
---

# Admin settings - SMTP  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/admin-panel-platform-smtp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Admin settings - SMTP Stay organized with collections  Save and categorize content based on your preferences. 

The **SMTP** page (SMTP stands for _Simple Mail Transfer Protocol_) in the **Platform** section of the **Admin** menu lets you configure your email settings. Looker instances send emails in many situations, including new user notifications, password resets, and administrative notifications, as well as when users [deliver](https://docs.cloud.google.com/looker/docs/scheduling) content such as [dashboards](https://docs.cloud.google.com/looker/docs/scheduling-and-sending-dashboards) and [Looks](https://docs.cloud.google.com/looker/docs/delivering-looks-explores).

**Note:** If you have a permission that provides access to only select pages in the Admin panel, such as [`manage_schedules`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_schedules), [`manage_themes`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#manage_themes), or [`see_admin`](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#see_admin), but you don't have the [Admin role](https://docs.cloud.google.com/looker/docs/admin-panel-users-roles#default_roles), the page or pages that are described here may not be visible to you in the Admin panel.

## Mail settings

**Deprecated:** For customer-hosted Looker instances, the default Looker email service is not available and the SMTP Options won't be visible. You must configure a different email service for all new customer-hosted instances.

In Looker's **Admin** panel, choose **SMTP** to see and change your instance's SMTP settings. You can use the default mail settings to take advantage of Looker's email service, without the need for additional configuration.

To use a different email service, select **Use custom mail settings**. Looker supports two authentication methods for custom SMTP: **Basic Authentication** (username and password) and **OAuth 2.0**.

Custom mail settings can be configured for SMTP servers that support the [`PLAIN` and `LOGIN` authentication protocols](https://en.wikipedia.org/wiki/SMTP_Authentication#Details) or OAuth 2.0.

### Custom mail settings

Enter the appropriate values for your email service's SMTP settings:

  * **Mail Server** : The URL of your SMTP server. Any changes to this setting require the Looker admin to also change the SMTP server password.
  * **From** : The name to display as the sender of your Looker emails (see Testing Custom Email Settings for an example). You can enter a name string and an email address encased in angle brackets (for example, **Display Name <email@address.com>**) or an email address without angle brackets (for example, **email@address.com**). Special characters, other than the `@` symbol in an email address and the surrounding angle brackets, if applicable, are not supported.
  * **User Name** : The username that's needed to gain access to your SMTP server.
  * **Password** : The password that's needed to gain access to your SMTP server.
  * **Port** : The port to use for your SMTP server. Any changes to this setting require the Looker admin to also change the SMTP server password.

**Note:** Looker instances that are hosted on Google Cloud cannot use port 25 for SMTP. Google Cloud blocks all traffic on port 25. For more information, see the [Sending email from an instance](https://docs.cloud.google.com/compute/docs/tutorials/sending-mail) page in the Google Cloud documentation. Using port 25 for SMTP on Looker instances that are hosted on Microsoft Azure is not recommended and may result in errors. For more information, see the [Troubleshooting outbound SMTP connectivity](https://docs.microsoft.com/en-us/azure/virtual-network/troubleshoot-outbound-smtp-connectivity) page in the Azure documentation.
  * **TLS/SSL** : If your SMTP server uses the TLS or SSL protocols for more secure email, select this option. Looker displays a drop-down menu of supported TLS and SSL versions. Select your protocol version. For TLS, TLS 1.2 is recommended.

  * **Authentication type** : Select **Basic Auth** to configure a username and password to authenticate to your SMTP server, or select **OAuth** to configure OAuth 2.0 authentication.

**Note:** You can switch between authentication types without interrupting email service.



#### Basic authentication

Enter the **Username** and **Password** required to authenticate to your SMTP server.

#### OAuth 2.0 authentication

Select this option if your SMTP provider uses OAuth 2.0 to authenticate. This method is required for services like Microsoft Office 365, which is deprecating basic authentication.

Enter the following information from your email provider:

  * **Client ID** : The client ID of the application that you created in your email provider's admin console.
  * **Client Secret** : The client secret for the application.
  * **Token URL** : The URL where Looker will exchange credentials for an access token.
  * **Scopes** : The URLs of the [scopes](https://oauth.net/2/scope/) that your email provider requires. For example, to assign the Microsoft identity platform `.default` scope, enter `https://outlook.office365.com/.default`.



**Generating OAuth credentials**

You'll need to create an application within your email provider's platform to generate the client ID, client secret, and token URL. For more information about creating an application, see the following pages:

  * [Using OAuth 2.0 to Access Google APIs](https://docs.cloud.google.com/developers.google.com/identity/protocols/oauth2#1.-obtain-oauth-2.0-credentials-from-the-dynamic_data.setvar.console_name.)
  * [Application types for the Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/v2-app-types)



## Saving SMTP settings

Once you have entered your SMTP settings, click the **Save** button to save your configuration. You can also test your settings, or refresh the page to see if your configuration has any errors.

**Note:** If you are using custom mail settings for SMTP, add [Looker's IP addresses](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access#option_1:_ip_address_allowlist) to your SMTP server's IP allowlist so that your SMTP server will allow inbound traffic from Looker.

Looker restricts how often Looker admins can save or test the SMTP settings to prevent using this feature to scan for open ports.

## Testing custom email settings

To test your custom email setup, use the **Send Test Email** button. This test works for both **Basic Authentication** and **OAuth 2.0** settings. Looker will attempt to send a test email to the user who pressed the button. The test email has the following attributes:

  * The sender is `admin@looker.com`.
  * The subject is `Looker Mail Test`.
  * The email body text is `Looker mail is working!`



To prevent malicious agents from scanning for open ports, Looker restricts how frequently Looker admins can test the SMTP settings.

## SMTP error messages

If there are any problems with your SMTP configuration, Looker alerts all admins in the following locations:

  * A warning message on the **SMTP** page
  * A warning icon next to the **SMTP** listing in the **Admin** sidebar



These errors are visible to all admins on your Looker instance. You can check for errors immediately by refreshing the page after saving custom mail settings.

Errors related to custom email settings tests appear below the **Save** and **Send Test Email** buttons at the bottom of the **SMTP** page.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
