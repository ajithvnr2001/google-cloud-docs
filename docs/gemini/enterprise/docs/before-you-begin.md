---
url: https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin/
title: Set up Gemini Enterprise as an administrator \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T23:41:33.183284+00:00
---

# Set up Gemini Enterprise as an administrator  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Set up Gemini Enterprise as an administrator Stay organized with collections  Save and categorize content based on your preferences. 

The guides in this section help administrators and IT operators set up and manage Gemini Enterprise. It describes the start-up tasks and prerequisites required to configure Cloud projects, manage user licensing, set up identity authentication, and deploy enterprise security controls.

### Project and licensing setup

Set up your Google Cloud project, enable billing, and manage user subscriptions:

###  Create a Google Cloud project 

Create or select a Google Cloud project to host your enterprise apps, data stores, and third-party data connectors.

[Create project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects)

###  Enable or verify Cloud billing 

Verify billing is active on your Cloud project to enable subscription tiers and pay-as-you-go platform capabilities.

[Verify billing](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled)

###  Purchase a product subscription 

Subscribe to Gemini Enterprise edition licenses through the Google Cloud console.

[View licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses)

### Access control and permissions

Assign platform licenses and configure Identity and Access Management (IAM) roles:

###  Assign licenses to platform users 

Distribute and assign licenses to employees manually by email or configure automatic seat assignment upon initial sign-in.

[Assign licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#license-assignment)

###  Grant administrator IAM access 

Grant the Gemini Enterprise Admin role to administrators managing platform settings, security policies, and data stores.

[Grant Admin role](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#grant-permissions-to-admins)

###  Grant end-user IAM access 

Grant the Gemini Enterprise User role to licensed employees accessing search, chat, and custom AI assistant features.

[Grant User role](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#grant-role)

### Identity and data security

Configure single sign-on, authentication, and enterprise data source access controls:

###  Configure your identity provider 

Connect your identity provider to manage user authentication, sync group memberships, and enforce permissions-aware search access.

[Configure identity provider](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider)

###  Connect enterprise data sources 

Create Google data stores and third-party data stores, such as Jira, Microsoft SharePoint, and many more.

[Create Google data stores](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/create-data-store) [Connect third-party data](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-third-party-data-source)

###  Enable Model Armor safety controls 

Configure Model Armor templates to sanitize prompt inputs, redact sensitive data, and enforce enterprise safety policies.

[Enable Model Armor](https://docs.cloud.google.com/gemini/enterprise/docs/enable-model-armor)

### Mobile app deployment

Configure access controls, device policies, and mobile app onboarding:

###  Set up and configure the mobile app 

Enable and configure the mobile app for iOS and Android devices, including single sign-on authentication and mobile enterprise access.

[Configure the mobile app](https://docs.cloud.google.com/gemini/enterprise/docs/configure-mobile-app)

### AI developer tools configuration

Enable developer tools, configure enterprise gateway routing, and govern developer access: 

###  Configure AI developer tools settings 

Enable AI developer tools in your Cloud project, manage organizational settings, and enforce code suggestion governance policies across your developer fleet.

[Configure tools](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-settings)

###  Set up Enterprise Gateway 

Route Antigravity app, Antigravity CLI, and Antigravity for IDEs model inference requests through your enterprise gateway to control network paths and centralize billing attribution.

[Deploy Gateway](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools/deploy-enterprise-gateway)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
