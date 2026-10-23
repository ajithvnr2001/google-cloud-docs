---
url: https://docs.cloud.google.com/appengine/docs/standard/payment-instrument/
title: Payment method required for all App Engine runtimes \u00a0|\u00a0 App Engine standard environment \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:16:42.333268+00:00
---

# Payment method required for all App Engine runtimes  |  App Engine standard environment  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/appengine/docs/standard/payment-instrument/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Engine ](https://docs.cloud.google.com/appengine/docs)
  * [ Standard environment ](https://docs.cloud.google.com/appengine/docs/standard)
  * [ Resources ](https://docs.cloud.google.com/appengine/docs/standard/resources)



Send feedback 

#  Payment method required for all App Engine runtimes Stay organized with collections  Save and categorize content based on your preferences. 

As of November 30, 2019, you can only deploy new versions of your App Engine apps if your account provides a [payment method](https://docs.cloud.google.com/billing/docs/how-to/payment-methods#available_payment_methods), such as a credit card. As of August 9, 2021, all App Engine apps require a payment method to continue running. This requirement applies to apps in all App Engine runtimes, including Java 8, Python 2.7, PHP 5, and Go 1.11 apps in the App Engine standard environment.

**As of August 9, 2021, if a running application does not have a payment method, it will be shut down.**

While you must provide a payment method for your accounts, the **App Engine free tier has not changed and is not going away**.

## Why we made this change

Requiring a payment method for all runtimes prevents fraud and abuse, and brings App Engine in line with the rest of Google Cloud. This allows us to spend more time on delivering new features and supporting you as you grow on App Engine.

In addition, all App Engine runtimes now use Cloud Build to build apps into a container during the deployment process. Cloud Build requires a payment method, and therefore if a payment method is not present, **deployments to App Engine will fail**. As of August 9, 2021, if a running application does not have a payment method, it **will be shut down**. You can reinstate your application by adding a payment method.

Other than providing a payment method, you don't need to make any other changes to your project. The change to Cloud Build is entirely in the background and has no effect on deployment commands or administration APIs.

## What remains the same

**The[free tier](https://docs.cloud.google.com/appengine/quotas) on App Engine is unchanged.**

## What you will see

If you do not have a valid payment method on the project, you will see:

  * `HTTP 500` errors returned when requests are sent to your app

  * App log entries in your App Engine logs that read "Billing disabled. Shutting down instance."




## What you need to do

You will need to add a payment method to your project if you have App Engine apps using the Java 8, Python 2.7, PHP 5, and Go 1.11 runtimes in the App Engine standard environment.

To add a payment method to your project:

  1. [Create a billing account](https://console.cloud.google.com/billing/) if you do not already have one.

  2. Add your credit card or other payment method as a payment method.

  3. Link your project to the billing account.




Learn more about [adding, removing or updating a payment method](https://docs.cloud.google.com/billing/docs/how-to/payment-methods).

## Why we are making this change

This change is driven by the following goals:

  * Reducing fraud on App Engine

  * Increasing the integration of App Engine with other Google Cloud services




### Reduce fraud on App Engine

Fraud hurts all legitimate users of App Engine and Google. Our engineering and support teams invest significant amounts of time in preventing, monitoring, and diagnosing fraudulent usage. This limits the resources we have available to legitimate customers. In addition, fraud costs Google money, which raises costs for everyone as it must be accounted for in our pricing of App Engine.

We have direct evidence from our experience with the newer runtimes that requiring a payment method reduces fraud.

### Integrate App Engine with other Google Cloud services

App Engine launched in 2008, predating Google Cloud, and was built in a completely custom and proprietary architecture, since there was no broader platform to integrate with. Now that Google Cloud is a large and sophisticated platform, our customers are asking for App Engine to integrate seamlessly with the services available in Google Cloud.

Integration with other Google Cloud services is possible through Serverless VPC Access, which allows App Engine to sit within the same VPC as Compute Engine VMs and Google Kubernetes Engine clusters. As part of the integration, we are moving App Engine builds to Cloud Build, which has the following benefits:

  * Detailed build output including verbose warnings and errors

  * The ability to view build history in the Cloud Build section of the Cloud console

  * (Coming soon) The ability to include any library in your code in addition to the predefined set that is available in the App Engine runtimes




Almost all Google Cloud services require a payment method, so this additional integration means that App Engine must also require a payment method.

## Costs of using Cloud Build

Cloud Build has a free tier that includes 120 build minutes per billing account, per day. For example, if your build took 5 minutes to complete, you would be able to deploy 24 times a day without incurring any charges. For more information on pricing beyond the free tier, see [Cloud Build pricing](https://cloud.google.com/build/pricing).

## Limit your costs

You can use the following mechanisms to limit your App Engine costs:

  * Set the [`max_instances`](https://docs.cloud.google.com/appengine/docs/standard/reference/app-yaml#scaling_elements) setting in your `app.yaml` configuration file to `1` to restrict your instance usage to the free tier.

  * [Set a budget and alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets) to monitor your resource consumption across all Google Cloud services.

  * [Manually disable your app](https://docs.cloud.google.com/appengine/docs/standard/managing-projects-apps-billing#disabling_an_application) once it goes above a preset usage level.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
