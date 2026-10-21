---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-byb/
title: Agent Assist for Salesforce required resources \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:44:25.561900+00:00
---

# Agent Assist for Salesforce required resources  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/aaforsalesforce-byb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Agent Assist for Salesforce required resources Stay organized with collections  Save and categorize content based on your preferences. 

To integrate Agent Assist UI modules with Salesforce, you need access to the following resources:

  * [Node.js](https://nodejs.org/en/download/package-manager)

Follow the recommended installation instructions for your operating system.

  * [Salesforce CLI](https://developer.salesforce.com/docs/atlas.en-us.sfdx_setup.meta/sfdx_setup/sfdx_setup_install_cli.htm)

Follow the recommended installation instructions for your operating system.

  * [Google Cloud CLI](https://docs.cloud.google.com/sdk/docs/install-sdk)

Install the gcloud CLI command as instructed and authenticate using gcloud CLI auth login.

  * Salesforce

Sign in at your instance URL or the [Salesforce sign in page](https://login.salesforce.com/) and note the following:

    * Your Salesforce My Domain URL. Follow these steps to find the My Domain URL:

      1. Navigate to the menu bar > **Setup** menu.
      2. Click **Setup**.
      3. In the Quick Find box, enter **My Domain**. The domain name is in the following format: `MY-DOMAIN-NAME.develop.my.salesforce.com`.
    * Your Salesforce organization ID. Follow these steps to find the organization ID.

      1. Navigate to the menu bar > **Setup** menu.
      2. Click Setup.
      3. In the Quick Find box, enter **Company Information**.
  * [Agent Assist integration backend](https://github.com/GoogleCloudPlatform/agent-assist-integrations/tree/HEAD/aa-integration-backend)

    1. Follow [the instructions](https://github.com/GoogleCloudPlatform/agent-assist-integrations/tree/HEAD/aa-integration-backend#how-to-deploy-and-run) to set up the integration.
    2. Before running the deploy script, configure the following environment variables with deploy.sh or in an .env file at the project root:

       * `AUTH_OPTION`: Set this to `SalesforceLWC`.
       * `SALESFORCE_DOMAIN`: A domain name similar to `YOUR_SUBDOMAIN.develop.lightning.force.com`. You noted this value in the Salesforce prerequisite. Exclude https://.
       * `SALESFORCE_ORGANIZATION_ID`: You noted this value in the Salesforce prerequisite.
       * `APP_AUTH_OPTION`: Set this to Twilio. Only applies to Twilio users.
       * `TWILIO_ACCOUNT_SID`: Set this to your Twilio Account SID. Only applies to Twilio users.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
