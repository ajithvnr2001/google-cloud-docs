---
url: https://docs.cloud.google.com/cloud-assist/custom-instructions/
title: Configure custom instructions for Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:28.616550+00:00
---

# Configure custom instructions for Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/custom-instructions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Guides ](https://docs.cloud.google.com/cloud-assist/overview)



Send feedback 

#  Configure custom instructions for Gemini Cloud Assist Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Use of this Preview offering of Gemini Cloud Assist is subject to the Google Cloud Agreement, including the Pre-GA Offering Terms of the [Google Cloud Specific Service Terms](https://cloud.google.com/terms/service-terms), as supplemented by the terms for the [Gemini for Google Cloud Trusted Tester Program](https://cloud.google.com/trusted-tester/gemini-for-google-cloud-preview).

To define persistent guidelines that shape the persona, reasoning, and responses of Gemini Cloud Assist, you can configure custom instructions. The following sections show you how to set these instructions for a project by using the Google Cloud console.

## About custom instructions

Administrators can set custom instructions to define guidelines that shape Gemini Cloud Assist's persona, reasoning, responses, and output formatting. These instructions can be free-form or structured, contain up to 3,000 characters, and apply to all users interacting with Gemini Cloud Assist in the Google Cloud project.

Setting custom instructions reduces the need to repeat directions in every prompt. For example, you can instruct Gemini Cloud Assist to act as a senior security architect that mandates [Customer-Managed Encryption Keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) for all infrastructure. You can also enforce internal naming conventions or procedures.

If a custom instruction doesn't interact with Gemini Cloud Assist in the way you expect, you can edit or delete the instruction and try again.

## Before you begin

  1. [Verify that Gemini Cloud Assist is set up for your Google Cloud project](https://docs.cloud.google.com/cloud-assist/set-up-gemini).



### Required roles

To get the permissions that you need to configure custom instructions, ask your administrator to grant you the [Gemini Settings Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudaicompanion#cloudaicompanion.settingsAdmin) (`roles/cloudaicompanion.settingsAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure custom instructions

To set custom instructions, follow these steps:

  1. Open the Google Cloud console.

[Go to Google Cloud console](https://console.cloud.google.com/)

  2. In any page of the Google Cloud console, click spark **Open or close Gemini Cloud Assist chat**.

The **Cloud Assist** panel opens.

  3. Click **More actions** (more_vert), and then click **Cloud Assist Settings** from the drop-down menu.

The **Manage Gemini Cloud Assist** settings panel opens.

  4. In the **Custom instructions** section, enter your instructions in the text field.

  5. Click **Save**.




## Examples

These examples show how to configure custom instructions for different scenarios.

### Act as a site reliability engineer

To direct Gemini Cloud Assist to act as a site reliability engineer (SRE), investigate logs and resources, and use a professional and direct tone, use the following instructions:
    
    
    You are a skilled Site Reliability Engineer (SRE). You leverage trusted runbooks
    and logs to quickly identify hypotheses for any reported issues. Your tone is
    professional and direct.
    

### Apply organization's standards

To direct Gemini Cloud Assist to apply your organization's standards to its responses, use the following instructions:
    
    
    Act as the Onboarding & Standards Lead for our Cloud Platform team. Your goal is
    to explain internal deployment workflows and enforce organizational standards
    for new engineers.
    
    Standardization Guidelines:
    
    - Naming Conventions: When explaining environment setup, always refer to the
       'Organizational Naming Standard' (for example, [Env]-[Region]-[Service]-[Index]).
    - Correct any user suggestions that deviate from this format.
    - Resource Labeling: Mandate the inclusion of cost-center, owner, and
       environment tags in every resource description or Terraform snippet.
    - Training Environments: For 'Data Science Training' requests, always recommend
       Vertex AI Workbenches with restricted VPC-SC perimeters, as
       defined in our internal security playbook.
    
    Knowledge Delivery:
    
    - When asked 'How-To' questions, provide a step-by-step 'Internal Checklist'
       followed by the corresponding gcloud commands.
    - If a user's request violates a standard, explain the why behind the policy
      (such as, 'This ensures billing transparency across projects').
    

## What's next

  * Learn more about [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview).
  * Learn how to [set up Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/set-up-gemini).
  * Learn how to [configure prompt and response sharing](https://docs.cloud.google.com/cloud-assist/configure-prompt-response-sharing).
  * Learn how to [use the **Cloud Assist** panel in the Google Cloud console](https://docs.cloud.google.com/cloud-assist/chat-panel).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
