---
url: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/test-agents/
title: Test the Remote Agent connection flow \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:09.126539+00:00
---

# Test the Remote Agent connection flow  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/working-with-remote-agents/test-agents/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Test the Remote Agent connection flow

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** Before you begin, you must configure the Siemplify integration in the Content Hub. 

This document outlines how to perform a basic, end-to-end test of the Remote Agent deployment by installing an agent locally and verifying its connection to an integrated security tool. The goal is to confirm the full communication path from the Google Security Operations platform, through the agent, and back.

  1. Create and deploy an agent:

     1. Create a new agent and send the download link to an email address you can access.
     2. Click the link in the email and download the agent installation package.
     3. Deploy the agent locally.
  2. Verify the agent status is live in the Google SecOps platform.

Confirm the agent can successfully communicate with another product (for example, Active Directory or ServiceNow). This test confirms the flow from Google SecOps to the agent and back.

  3. Set up the relevant integration to run remotely and test the specific actions.




Both integrations and connectors provide testing features and display the status of the assigned Remote Agents directly within the platform. This same flow can be repeated for agents deployed on remote sites.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
