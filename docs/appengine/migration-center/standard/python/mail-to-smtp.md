---
url: https://docs.cloud.google.com/appengine/migration-center/standard/python/mail-to-smtp/
title: Migrate from the App Engine Mail service to an SMTP-based service \u00a0|\u00a0 App Engine migration center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:38:15.385736+00:00
---

# Migrate from the App Engine Mail service to an SMTP-based service  |  App Engine migration center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/migration-center/standard/python/mail-to-smtp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Migration center ](https://docs.cloud.google.com/appengine/migration-center)
  * [ Guides ](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services)



Send feedback 

#  Migrate from the App Engine Mail service to an SMTP-based service Stay organized with collections  Save and categorize content based on your preferences. 

To improve email security and ensure reliable, high-volume email delivery, migrate from the [legacy Mail service](https://docs.cloud.google.com/appengine/docs/standard/services/mail) to a standard third-party email provider service that uses the Simple Mail Transfer Protocol (SMTP), such as [SendGrid](https://sendgrid.com/), [Mailgun](https://www.mailgun.com/), or [Mailjet](https://www.mailjet.com/).

This guide describes the process for migrating outbound email services from the App Engine Mail service to an SMTP-based email service. You can apply these instructions to migrate to any SMTP-based third-party email provider, or use another [supported runtime](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule). This guide doesn't provide steps for migrating inbound messaging that uses a third-party alternative.

The SMTP standard offers the following benefits over the legacy App Engine Mail service:

  * SMTP-based services provide improved email delivery by reducing the likelihood of emails being marked as spam.

  * With SMTP-based services, you can access detailed analytics reports on email opens, clicks, and bounces. These reports provide useful information about how users interact with your emails.

  * You have complete control over your sender reputation and email authentication.

  * Increased daily send limits compared to the legacy Mail service with access to advanced features like A/B testing, segmentation, and templating.




## Overview of the migration process

The migration process includes the following steps:

  1. Set up the SMTP-based email service to get your SMTP credentials.
  2. Verify your sender identity to authenticate with your domain or email address.
  3. Configure your source files with your SMTP credentials and sending method, and then deploy your application.
  4. Test your application to check your email functionality.



## Set up the SMTP-based email service

Set up an account with a standard third-party email provider that uses SMTP, such as SendGrid, Mailgun, or Mailjet and retrieve the following information from your chosen provider:

  * **SMTP Host** : The SMTP server address used for sending mail. For example, `smtp.sendgrid.net` or `example.mailjet.com`.

  * **Port** : The port number for the connection. For example `587` for TLS encryption.

  * **Username** : Your account's SMTP login username.

  * **Password or API Key** : Your account's password or an API key, which acts as the password for the SMTP connection. For some providers like SendGrid, the username is a fixed value like `apikey`, and the API key is used as the password.




## Verify your sender identity

To prevent spam, all email services require you to verify that you are the owner of the email address or domain you are sending emails from. This step often involves adding specific DNS details, such as `CNAME` records to your domain host's DNS management page.

Follow your provider's instructions to verify your sender identity before proceeding with the application configuration.

To add DNS records to your domain host, follow these steps:

  1. Sign in to your DNS provider service.
  2. Navigate to the DNS management page for your domain.
  3. Add the CNAME records exactly as provided by your email service provider. For each record, do the following:

     * In the **Name** or **Host** field, enter the host details.
     * In the **Points** or **Value** field, enter the value.



DNS changes might take a few hours to become active. If your verification fails, wait for some time, and try again.

## Configure your source files

To include the SMTP functionality, follow these steps:

  1. Add the following Python SDK version to your `requirements.txt` file:
         
         appengine-python-standard==2.0.0
         

  2. Add the following code in your `app.yaml` file to switch to the SMTP service:
         
         runtime: RUNTIME  # a supported python version
         
         env_variables:
           # Enable the SMTP service.
           APPENGINE_USE_SMTP_MAIL_SERVICE: "true"
         
           # --- SMTP Server Configuration ---
           # The server address from your mail provider
           APPENGINE_SMTP_HOST: "SMTP_HOST"
         
           # The recommended port for TLS connections
           APPENGINE_SMTP_PORT: "587"
         
           # The username for your SMTP login
           APPENGINE_SMTP_USER: "SMTP_USER"
         
           # The API key or password
           APPENGINE_SMTP_PASSWORD: "SMTP_PASSWORD"
         
           # Use TLS for a secure connection
           APPENGINE_SMTP_USE_TLS: "true"
         
           # --- For sending emails to Admins ---
           # A comma-separated list of admin email addresses.
           # This is required if you use the send_mail_to_admins() function.
           APPENGINE_ADMIN_EMAIL_RECIPIENTS: "admin@example.com,another-admin@example.com"
         

Replace the following:

     * RUNTIME: a [supported](https://docs.cloud.google.com/appengine/docs/standard/lifecycle/support-schedule#python) Python runtime version.
     * SMTP_HOST: the SMTP host address. For example, `smtp.sendgrid.net` or `example.mailjet.com`.
     * SMTP_USER: your account's SMTP login username. For example, `apiKey`.
     * SMTP_PASSWORD: the password or API key you obtained from your third-party email provider. For improved security, we recommend that you use the [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) to store your API key instead of placing it in the `app.yaml` file.
     * If you don't use the `send_mail_to_admins()` function, omit the `APPENGINE_ADMIN_EMAIL_RECIPIENTS` setting.
  3. Run the following command to deploy your application:
         
         gcloud app deploy
         




## Test your application

Migration is successful if you are able to [deploy your app](https://docs.cloud.google.com/appengine/docs/standard/testing-and-deploying-your-app#deploying_your_application) without errors. To verify that your mail service is working, follow these steps:

  1. Trigger the part of your application that sends an email.
  2. [Check the Logs Explorer](https://docs.cloud.google.com/appengine/docs/standard/writing-application-logs?tab=python#view_logs) to make sure there are no errors related to the API calls or the SMTP connection attempt.
  3. Sign in to your third-party email provider's account (e.g., Mailgun, Mailjet, SendGrid) and check their Activity Feed, Logs, or Delivery Dashboard. Your test email should appear in the feed with a delivery status marked as `Processed`, `Delivered`, or similar.



## What's next

  * [Create and access a secret using Secret Manager](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart).
  * [Migrate off of legacy bundled services](https://docs.cloud.google.com/appengine/migration-center/standard/services/migrating-services).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
