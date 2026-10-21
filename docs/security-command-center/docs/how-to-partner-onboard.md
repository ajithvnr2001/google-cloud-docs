---
url: https://docs.cloud.google.com/security-command-center/docs/how-to-partner-onboard/
title: Onboarding as a Security Command Center partner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:50.048892+00:00
---

# Onboarding as a Security Command Center partner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/how-to-partner-onboard/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Resources ](https://docs.cloud.google.com/security-command-center/docs/resources)



Send feedback 

#  Onboarding as a Security Command Center partner Stay organized with collections  Save and categorize content based on your preferences. 

Complete Security Command Center partner onboarding by creating a Google Cloud Marketplace solution and completing pre-setup steps. The guide covers the following use cases:

  * Onboarding using a customer's service account: your customer owns the service account and you write data for your customer.
  * Onboarding for self-service customers: your customer owns the service account and writes their own data using an app you provide.



## Before you begin

Before you create a Cloud Marketplace solution, you need to sign up for the technology partner program:

  * If you aren't already signed up as a partner, sign up to [list your products on Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners), and complete the corresponding business and service agreements.
  * If you're already signed up as a partner, use the [Partner Support Desk](https://g.co/cloud/psd-partner) to get started with a Security Command Center listing, and include the word "Marketplace" in your description. For more information about Partner Support Desk, including steps to resolve any issues with accessing Partner Support Desk, visit [Request assistance with Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/partners/get-support). Your project is added to the access control list that lets you create a Managed Listing - Billed by Partner (also known as Standalone SaaS).



## Onboarding using a customer's service account

This section describes how to complete onboarding in the following scenario:

  * You want to write Security Command Center data on behalf of your customer;
  * You're using a service account key from the customer.



To set up the Cloud Marketplace product using the customer's service account, follow these steps:

  1. In the Google Cloud console, go to the **Producer Portal Overview** page and select a project where the Cloud Commerce Producer API is enabled.

[Go to Overview](https://console.cloud.google.com/projectselector2/producer-portal?supportedpurview=project)

  2. To create a new product, click **Add Product**.

  3. On the **Add product** page, complete the following steps:

     1. Select **Standalone Listing**.
     2. For **Product name** , enter the name of the product. The product name can't have more than 64 characters.

Take note of the product ID.

     3. Click **Create**.

  4. To view the product details, click **Product details**.

  5. In the **Product info** pane, add signup instructions for your customer:

     1. For **Signup URL** , enter the signup URL in the following format:
            
            https://console.cloud.google.com/security/command-center/source-registration;partnerId=PARTNER_ID;solutionId=SOLUTION_ID
            

Replace the following:

        * PARTNER_ID: the ID assigned to you when you enrolled as a Cloud Marketplace partner.
        * SOLUTION_ID: the ID assigned to the solution you created in the previous steps.
     2. For **Product overview** , add details about tasks that your customer must complete after they register. This section supports hyperlinks to external websites. Include the following information:

        * How to generate a service account key for the service account by using the guide to [creating and managing service account keys](https://docs.cloud.google.com/iam/docs/creating-managing-service-account-keys).
        * How to sign in to your website and provide you with the sourceId and service account key.
     3. In the **Category ID** drop-down list, select **Security Command Center Services**.

  6. Select the **Product metadata** tab.

  7. For **Search metadata** , enter "Security Command Center".

  8. After you finish setting up your solution, click **Submit**.

  9. Contact [cloud-partners@google.com](mailto:cloud-partners@google.com) to request approval of your solution.

  10. Use the [Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/reference/rest) to write data to Security Command Center.




After your customer uses the signup URL to provide their `sourceId` and service account key, you can use them to write Security Command Center data. When your customer adds your security tool as a new [security source](https://docs.cloud.google.com/security-command-center/docs/how-to-security-sources), your security findings will be displayed on the Security Command Center console.

## Onboarding for self-service customers

This solution describes how to complete onboarding in the following scenario:

  * You don't want to write Security Command Center data on behalf of a customer;
  * You want your customer to write Security Command Center data on their own, using an app you provide;
  * Your customer will use their own service account.



To set up the Cloud Marketplace product for a self-service customer, follow these steps:

  1. In the Google Cloud console, go to the **Producer Portal Overview** page and select a project where the Cloud Commerce Producer API is enabled.

[Go to Overview](https://console.cloud.google.com/projectselector2/producer-portal?supportedpurview=project)

  2. To create a new solution, click **Add Product**.

  3. In the **Add product** window that appears, complete the following:

     1. Select **Standalone Listing**.
     2. Add a **Product name** and make note of the **Product ID**. The product name cannot be more than 64 characters.
     3. Click **Create**.
  4. To view the product details, click **Product details** on the left menu.

  5. In the **Product info** panel that appears, add signup instructions for your customer:

     1. Under **Signup URL** , enter the signup URL in the following format:
            
            https://console.cloud.google.com/security/command-center/source-registration;partnerId=[PARTNER_ID];solutionId=[SOLUTION_ID]
            

Where the variables correspond to the following:

        * `[PARTNER_ID]` is the ID assigned to you when you enrolled as a Cloud Marketplace partner.
        * `[SOLUTION_ID]` is the ID assigned to the solution you created in the previous steps.
     2. In the **Product overview** box, add details about tasks that your customer should complete after they register. This section supports hyperlinks to external websites. You should include the following information:

        * Where to download your app to write Security Command Center data.
        * How to set up, sign in and authenticate, and run your app.
        * Where to paste the sourceId.
        * How to use the Security Command Center service account credentials in your app. For example, you might have the customer start a VM as the service account and run the app inside the VM.
     3. On the **Category ID** drop-down list, select **Security Command Center Services**

  6. Select the **Product metadata** tab. Under **Search metadata** , enter "Security Command Center".

  7. After you've finished setting up your solution, click **Submit** and contact [cloud-partners@google.com](mailto:cloud-partners@google.com) to approve the solution.

  8. Use the [Security Command Center API](https://docs.cloud.google.com/security-command-center/docs/reference/rest) to enable your customers to write data to Security Command Center using your app.




After your customer sets up the app, they'll be able to use your app to write their Security Command Center data.

## What's next

  * Learn how to [access Security Command Center with client libraries](https://docs.cloud.google.com/security-command-center/docs/reference/libraries).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
