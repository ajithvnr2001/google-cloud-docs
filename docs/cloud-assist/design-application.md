---
url: https://docs.cloud.google.com/cloud-assist/design-application/
title: Design an application with Gemini assistance \u00a0|\u00a0 Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:14:01.908993+00:00
---

# Design an application with Gemini assistance  |  Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/design-application/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Guides ](https://docs.cloud.google.com/cloud-assist/overview)



Send feedback 

#  Design an application with Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Use of this Preview offering of Gemini Cloud Assist is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/service-terms), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview).

This document shows you how to design an application by using [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview) along with Application Design Center, an application design and deployment service in Google Cloud.

When you use natural language assistance in [Gemini Cloud Assist chat](https://docs.cloud.google.com/cloud-assist/chat-panel) along with Application Design Center, you can accelerate your application development time. This combination lets you translate your application requirements and goals into Terraform infrastructure as code (IaC), which you can then deploy in a built-in or personal deployment pipeline. In this way, Application Design Center offers an end-to-end assisted solution that lets you author, customize, export, and deploy applications.

At a high level, using Gemini Cloud Assist for design assistance generally involves the following steps:

  1. Access the **Cloud Assist** chat panel.
  2. Enter a prompt.
  3. Review the Gemini Cloud Assist response.
  4. Create a new application template.
  5. Iterate and refine the application design.
  6. Deploy your application infrastructure.

**Note:** Gemini Cloud Assist doesn't support applications created in a [ host project or a single-project boundary](https://docs.cloud.google.com/app-hub/docs/set-up-app-hub#compare-models).

## Before you begin

  * [Ensure that Gemini Cloud Assist is set up for your Google Cloud user account and project](https://docs.cloud.google.com/cloud-assist/set-up-gemini).
  * [Ensure that you have set up Application Design Center](https://docs.cloud.google.com/application-design-center/docs/setup).



## Access Gemini Cloud Assist chat

If Gemini Cloud Assist is set up for your project, you can access its chat capabilities from any page in the Google Cloud console.

  1. In the Google Cloud console, go to any page—for example, the **Dashboard**.

[Go to Dashboard](https://console.cloud.google.com/home/dashboard)

  2. In the Google Cloud console toolbar, click spark **Open or close Gemini Cloud Assist chat**.

The **Cloud Assist** panel opens.




If you're familiar with application templates, you can navigate to the [Application Design Center in the Google Cloud console](https://console.cloud.google.com/products/design-center/applications), create a template, and then open [Gemini Cloud Assist chat](https://docs.cloud.google.com/gemini/docs/codeassist/use-gemini-code-assist-chat).

## Enter a prompt

In Gemini Cloud Assist chat, you can get assistance by using natural language _prompts_ (questions or statements) such as the following:

  * Product-oriented prompts—for example, "Help me set up Cloud Run, Cloud SQL, and a Load Balancer together in region eu-west-2."
  * Business outcome-oriented prompts—for example, "I need a data pipeline solution to process async events."



If you're exploring Gemini Cloud Assist design capabilities or are at an early phase of design, you can use basic design-related prompts such as the following:

  * "I need to process short-lived, event-based actions triggered from other systems for data pipeline automation."
  * "Set up a batch pipeline."
  * "Help me set up jobs that periodically run on datasets."
  * "Help me implement a high availability web application with a Java backend and a MySQL database. Traffic will be bursty so make sure it scales up and down fast."



In these examples, Gemini Cloud Assist responds with a suggested application architecture that adheres to Google Cloud best practices and applies to [supported resource types](https://docs.cloud.google.com/application-design-center/docs/supported-resources). It also provides the purpose of each resource in the stack.

## Review the Gemini Cloud Assist response

The way you review a Gemini Cloud Assist response depends on whether you prompted Gemini while an Application Design Center template was open or not.

If you started from the **Cloud Assist** panel and have an application template open in the Application Design Center, then the response provides an explanation describing the purpose of each product in the stack based on your prompt. Any suggested updates or modifications are directly applied to the application design visible on the Application Design Center canvas.

If you started from the **Cloud Assist** panel but are outside of an Application Design Center template, the response includes an initial architecture diagram and an explanation detailing the purpose of each component in the suggested stack.

Click **Edit App Design** to navigate to the Application Design Center, where you need to create a new application template. After the template is created, your generated application design is loaded onto the Application Design Center canvas so you can further iterate and refine the application design.

If you don't have access to the Application Design Center, then when you click **Edit App Design** , the Application Design Center launches your design in _preview mode_. In preview mode, you can visualize the Gemini- generated application design and refine it by using natural language interactions in the **Cloud Assist** panel. When you're satisfied with the application design, click **Get Code** to download the Terraform configuration. You can then use this Terraform code with your deployment tools to provision the infrastructure.

### Iterate in the Application Design Center canvas

Within the canvas environment, Gemini Cloud Assist retains the context of your design. This means that if you manually make changes to the architecture, Gemini is aware of these modifications, letting you continue iterating and refining your application with its assistance.

## Create a new application template

  1. In Gemini Cloud Assist chat, click **Edit App Design**.

  2. On the **Create a new template** page, [specify the template details](https://docs.cloud.google.com/application-design-center/docs/design-application-templates#specify_template_details), and then click **Create template**.

The application design is imported as a template, which you can then further iterate and edit in the canvas.




After you have the template that you like, you can iterate and refine your application design, or deploy your application infrastructure.

## Iterate and refine your application design

The more detailed initial information that you give Gemini Cloud Assist, the more likely it is to produce an initial application template that's well aligned to your design goals. You can iteratively build the design by defining each sub-system and its requirements across multiple prompts and turns of the conversation. For example, you might enter the following in Gemini Cloud Assist chat:
    
    
    Help me create an application with 3 microservices called search, order, and
    inventory in europe-west1 region.
    

Then, in subsequent prompts, you can add more detail, such as defining frontend requirements:
    
    
    I also want a frontend microservice which is exposed via an external load
    balancer. The frontend layer invokes the three microservices. Order and
    inventory microservices need to have a database with the same name as the
    microservice.
    

Then, refine the microservice even more, such as defining log requirements:
    
    
    For the inventory microservice, capture the changelog events and publish
    them to a Pub/Sub topic.
    

Then, refine your microservice even more, such as defining backend requirements:
    
    
    The search microservice should use a distributed search and analytics backend. I
    also want the inventory microservice to publish the changelog events to the
    distributed search backend.
    

After you select an application design, you can deploy your application infrastructure.

## Deploy your application infrastructure

  1. [Create an application instance](https://docs.cloud.google.com/application-design-center/docs/manage-application-instances) from an application template.

  2. Deploy the application using one of the following methods:

     * [Deploy from the Google Cloud console](https://docs.cloud.google.com/application-design-center/docs/deploy-from-console). The Google Cloud console lets you track changes and apply template revisions.

     * [Download and deploy Terraform](https://docs.cloud.google.com/application-design-center/docs/download-and-deploy). This approach lets you use your own deployment tools and workflows.




## What's next

  * Learn more about [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview).
  * Learn more about [Application Design Center](https://docs.cloud.google.com/application-design-center/docs/overview).
  * Learn how to [write better prompts for Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/discover/write-prompts). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
