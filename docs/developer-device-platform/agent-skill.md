---
url: https://docs.cloud.google.com/developer-device-platform/agent-skill/
title: Developer Device Platform Agent Skill \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:44:46.635555+00:00
---

# Developer Device Platform Agent Skill  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/developer-device-platform/agent-skill/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Developer Device Platform ](https://docs.cloud.google.com/developer-device-platform)
  * [ Guides ](https://docs.cloud.google.com/developer-device-platform/overview)



Send feedback 

#  Developer Device Platform Agent Skill Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Use the DDP [Agent Skill](https://github.com/google/skills/blob/main/skills/cloud/developer-device-platform-basics/SKILL.md) in GitHub to to reserve and manage Developer Device Platform devices and sessions with intuitive natural language prompts.

The Developer Device Platform agent skill enables agentic coding using remote devices in Developer Device Platform through the [Device Streaming](https://docs.cloud.google.com/device-streaming/docs) API.

## Before you begin

These steps assume that you have already created a Google Cloud project, completed the setup steps in the Developer Device Platform [Quickstart](https://docs.cloud.google.com/developer-device-platform/quickstart) guide, and authenticated with `gcloud` in the terminal.

**Tip:** Append `--help` to any `gcloud` command to see detailed usage information.

## Prerequisites

In addition to establishing the Google Cloud environment described in the Quickstart, install these packages for the Developer Device Platform agent skill:

  * [ADB](https://developer.android.com/tools/adb) for running commands on the remote Android device

  * a [Python environment](https://docs.cloud.google.com/python/docs/setup) to [enable ADB forwarding](https://github.com/google/skills/blob/main/skills/cloud/developer-device-platform-basics/references/start_adb_forwarder.md)

  * [Antigravity](https://antigravity.google/download) or any other AI coding agent that supports agent skills

  * [Node Version Manager](https://github.com/nvm-sh/nvm) for installing Node.js

  * [Node.js](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm) for installing the agent skill using `npx`




## Set up the DDP agent skill

  1. Confirm you are authenticated with Google Cloud CLI and configure active [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials):
         
         gcloud auth application-default login
         

  2. Establish a Python environment with:
         
         python3 -m venv .venv
         source .venv/bin/activate
         

  3. Install the Developer Device Platform agent skill with:
         
         npx skills add https://github.com/google/skills --skill developer-device-platform-basics
         




## Use the DDP agent

The `developer-device-platform-basics` skill allows agentic coding tools to reserve and manage device session through the Device Streaming API. Here are some sample prompts:

  1. List the available devices in DDP
  2. Get a Pixel 10 from DDP
  3. Display and provide control of the device
  4. List the active device sessions on DDP
  5. Extend the current device session by 30 minutes
  6. Stop the device session



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
