---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/developer-settings/
title: Developer Settings \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:05.989741+00:00
---

# Developer Settings  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/developer-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Developer Settings Stay organized with collections  Save and categorize content based on your preferences. 

Developer settings provide access to configuration specifically for accessing additional services including API.

## API Credential Management

**Warning:** **Deprecation Notice:** for API Company Key and Secret Value

The Company Key and Secret Value is being deprecated as of September 30, 2022.

A new **Credential Management** interface is available at **Settings > Developer Settings > API**.

**Note:** The **token** replaces the password value on the API requests. _This was previously the Company Secret._

Use your **subdomain** (without the https://) as the username. For example, if the URL you visit is _https://__foobar_ _.domain.co_ then the subdomain value for your username is **foobar**. _This was previously the Company Key._

**Create as many API credentials as you need for internal use.**

Be aware that some third-party integrations require the creation of API credentials.

As a result, depending on the integrations you have, you may already see API credentials configured for Advanced Reporting, or others.

**If you lose or forget your token, you canregenerate the token. Be sure to store this in a secure location. **

The API Credential Management Settings allow you to:

  * add new API credentials

  * disable / enable credentials

  * regenerate the secret token

  * or edit the name of an existing credential




## Add an API credential

  1. Go to **Settings > Developer Settings > API Credential management**.

  2. Click the **\+ Add API Credential** button. An **Add API Credential** message will open.

  3. Enter a **Name** for the credentials.

  4. Click **Create**.




## Edit the name of an API credential

  1. Go to **Settings > Developer Settings > API Credential management**.

  2. Click the Edit icon ![Edit the name](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/16331bc4769d53.png) to update the name.




## Generate a new token

**Note:** When creating a new credential or regenerating a token, the secret token will only be displayed once. **Please be sure to store this in a secure location.**

  1. Click the Refresh icon ![Refresh token](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/16331bc476c7e1.jpg) to generate a new token.

A warning message appears.




**Warning** : Regenerating a new token will immediately invalidate the previous token.

Anything using the previous token will generate authentication errors. Are you sure?

  * **Cancel:** there is no new token generated.

  * **Regenerate:** a new token is regenerated. **Copy the new token and store in a secure place.**




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
