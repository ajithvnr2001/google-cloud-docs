---
url: https://docs.cloud.google.com/appengine/docs/standard/sending-messages/
title: Sending messages with third-party services \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:14:07.819217+00:00
---

# Sending messages with third-party services  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/sending-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Guides ](https://docs.cloud.google.com/appengine/docs/an-overview-of-app-engine)



Send feedback 

#  Sending messages with third-party services Stay organized with collections  Save and categorize content based on your preferences. 

App Engine apps can use third-party companies to send email, SMS messages, or make and receive phone calls. For example, you might send email to confirm business transactions, confirm the creation of user accounts, or send marketing communications.

This page lists some examples of companies that provide communication services and client libraries for App Engine apps.

**Note:** The services offered by these third-party companies are not covered by the [App Engine Service Level Agreement](https://cloud.google.com/appengine/sla).

## Mailgun

[Mailgun](https://www.mailgun.com/) provides both RESTful APIs and client libraries for sending email, along with a free quota for all users. See the monthly pricing calculator on [the sign up page](http://www.mailgun.com/google) for pricing on additional messages and volume discounts.

Learn more about Mailgun:

  * [Mailgun developer documentation](https://documentation.mailgun.com)
  * [Mailgun client libraries](https://documentation.mailgun.com/en/latest/libraries.html#libraries)



## Mailjet

[Mailjet](https://www.mailjet.com/google/?p=google) is a global email service that offers a free quota for App Engine users. To take advantage of this offer, click the following link to [Create a Mailjet account](https://www.mailjet.com/google/?p=google).

Learn more about Mailjet:

  * [Mailjet developer documentation](https://dev.mailjet.com/email/guides/getting-started/)
  * [Mailjet client libraries](https://dev.mailjet.com/email/guides/libraries/)



## SendGrid

You can use [SendGrid](https://sendgrid.com/) to power your emails on App Engine. SendGrid can improve your deliverability and provide transparency into what actually happens to those emails your app sends. You can see statistics on opens, clicks, unsubscribes, spam reports and more with the SendGrid interface or its API.

App Engine customers can take advantage of a free quota by signing up for the [SendGrid Email API plan](https://console.cloud.google.com/marketplace/product/sendgrid-app/sendgrid-email) through the Google Cloud console. Note that Google is compensated for customers who sign up for a paid account.

Learn more about SendGrid:

  * [SendGrid developer documentation](https://sendgrid.com/docs/for-developers/)
  * [SendGrid client libraries](https://sendgrid.com/docs/Integrate/libraries.html)



## SMS and Voice Services via Twilio

You can use Twilio to embed voice, VoIP, and messaging into applications. The Twilio platform consists of the [Twilio Markup Language (TwiML)](http://www.twilio.com/docs/api/twiml), a [RESTful API](http://www.twilio.com/docs/api/rest), and VoIP SDKs for web browsers, Android, and iOS.

Learn more about Twilio:

  * [Twilio developer documentation](https://www.twilio.com/docs/)
  * [Twilio client libraries](http://www.twilio.com/docs/libraries)



## Adding client libraries and third-party API keys to your app

To make client libraries available in your App Engine development and deployment environments, specify the library as a dependency. For example, to specify dependencies for the Node.js runtime, see [here](https://docs.cloud.google.com/appengine/docs/standard/nodejs/specifying-dependencies).

Most third party services use API keys to authenticate your app. You generate the keys on the third-party's site. To use the third-party API keys in your app:

  1. Store the API keys in the [Secret Manager](https://docs.cloud.google.com/secret-manager/docs/overview) and [fetch the key securely](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart) at instance start time.

  2. Encrypt the key with [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service), store the encrypted key in an environment variable, and [decrypt it programmatically](https://docs.cloud.google.com/kms/docs/encrypt-decrypt) at instance start time.

  3. For non-production environments, you can store the key itself in an environment variable. Note that anyone with access to your `app.yaml` file can also access your key.




To learn about the advantages of each approach, see [Choosing a secret management solution](https://docs.cloud.google.com/kms/docs/secret-management#choosing_a_secret_management_solution)

To store the key, or encrypted key value in an environment variable:

  1. Add the key or encrypted key value to the environment variables section in your app's `app.yaml` file.

For example:
         
         env_variables:
              EMAIL_API_KEY: key-from-third-party OR encrypted-key
         

If you are using the Node.js runtime, add the key to the configuration variables in your app's environment variables section in your app's `app.standard.yaml` file. 

  2. In your app's code, retrieve the key or encrypted key from your environment variables.

For example, if you are using the Python runtime:
         
         EMAIL_API_KEY = os.environ['EMAIL_API_KEY']
         

  3. Pass the key as required by the third party's API. Ensure you [decrypt the key](https://docs.cloud.google.com/kms/docs/encrypt-decrypt) if you encrypted it previously.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
