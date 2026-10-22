---
url: https://docs.cloud.google.com/cloud-assist/release-notes/
title: Gemini Cloud Assist release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:24:49.706306+00:00
---

# Gemini Cloud Assist release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ Resources ](https://docs.cloud.google.com/cloud-assist/resources)



Send feedback 

#  Gemini Cloud Assist release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Gemini Cloud Assist. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/gemini-cloud-assist-release-notes.xml) directly. 

## August 04, 2026

Feature

Gemini Cloud Assist is now supported within VPC Service Controls perimeters. For more information, see [VPC Service Controls supported services](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products#table_cloud_assist).

## April 22, 2026

Feature

### Model Context Protocol support

MCP support is available in Private Preview. To request access, contact your Google Cloud account team. You can interact with Gemini Cloud Assist agents from various surfaces, including third-party client agents and IDEs, using the Model Context Protocol (MCP). For more information, see [Integrating with MCP](https://docs.cloud.google.com/cloud-assist/configure-mcp).

Feature

### Proactive agents for issue investigation

Proactive agents are available in Private Preview to Premium Support customers. Enable Gemini Cloud Assist to autonomously investigate issues triggered by Cloud Alerting policies or cost anomalies in the background. These investigations don't modify or make any changes to your environment. Results and insights, such as root cause analysis for alerts or cost spike drivers, are delivered via Eventarc. You can view these results in the Google Cloud console. This feature requires administrator enablement and configuration of an agent identity. For more information, see [Configure proactive agents](https://docs.cloud.google.com/cloud-assist/proactive-agents-setup).

Feature

### Page context awareness

Page context awareness is available in Public Preview. Gemini Cloud Assist automatically uses the context of the content currently visible on your Google Cloud console page to provide more relevant and accurate responses to your prompts. For more information, see [Manage page context sharing](https://docs.cloud.google.com/cloud-assist/chat-panel#page-context-sharing).

Feature

### Enhanced agent administration controls

[Enhanced agent administration controls](https://docs.cloud.google.com/cloud-assist/admin-settings) are available in Public Preview. Administrators have the following options in the Cloud Assist settings panel:

  * **Web grounding settings:** Choose how Gemini Cloud Assist uses Google Search to ground its responses, with options for either the most comprehensive results or stricter data residency compliance. For more information, see [Configure web grounding](https://docs.cloud.google.com/cloud-assist/configure-grounding).
  * **Custom instructions:** Define persistent system instructions to customize the agent's persona, response formatting, and awareness of organizational standards or business context for all users within the project. For more information, see [Set custom instructions](https://docs.cloud.google.com/cloud-assist/custom-instructions).



## April 16, 2026

Announcement

### geminicloudassist API automatically enabled for Gemini Cloud Assist chat users

As of April 16th, 2026, the `geminicloudassist.googleapis.com` API has been automatically enabled on projects that meet **all** of the following criteria:

  * Had used [Gemini Cloud Assist chat](https://docs.cloud.google.com/cloud-assist/chat-panel) in the prior 60 days.
  * Had the `cloudaicompanion.googleapis.com` API enabled on April 16, 2026.
  * Did not have the `geminicloudassist.googleapis.com` API enabled on April 16, 2026.



The Gemini Cloud Assist chat functionality that was previously served by `cloudaicompanion.googleapis.com` is now served by `geminicloudassist.googleapis.com`, and both APIs are dependencies to use Gemini Cloud Assist. This automatic API enablement ensures that users have access to the same functionality without any loss of service.

## April 10, 2026

Breaking

### Update for Gemini Cloud Assist investigations

From April 10, 2026, creating, running, and editing Gemini Cloud Assist [investigations](https://docs.cloud.google.com/cloud-assist/investigations) will only be available to users with a Premium Support contract or who have requested access through their account team. If you ran an investigation prior to April 10, 2026, the results of the investigation continue to be available to you in the Google Cloud console.

## April 09, 2026

Deprecated

### VPC Service Controls support for Gemini Cloud Assist investigations deprecation

Starting April 13, 2026, Gemini Cloud Assist investigations will no longer be supported within VPC Service Controls perimeters. You do not need to remove the Gemini Cloud Assist API (`geminicloudassist.googleapis.com`) from your Restricted Service configurations, but if you keep it there, access to it will still be blocked within the perimeter. To continue using this feature, you must make requests to the service from outside any VPC Service Controls perimeter. For more information, see the [Deprecated VPC Service Controls support for Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/deprecations/vpcsc-support) page.

## April 08, 2026

Breaking

### Custom IAM roles permission update for Gemini Cloud Assist

Gemini Cloud Assist has replaced the `cloudaicompanion.instances.completeTask` IAM permission with `geminicloudassist.agents.invoke`. If you have access to Gemini Cloud Assist through a custom IAM role, you must update the role to continue having access. For more information, see the [deprecated IAM permissions](https://docs.cloud.google.com/cloud-assist/deprecations/permissions) document.

## April 06, 2026

Deprecated

### Custom IAM roles permission update for Gemini Cloud Assist

On April 8, 2026, Gemini Cloud Assist is replacing the `cloudaicompanion.instances.completeTask` IAM permission with `geminicloudassist.agents.invoke`. Updates to standard IAM roles will be done automatically, but if you have access to Gemini Cloud Assist through a custom IAM role, you must update the role before April 8, 2026 to ensure continued access. For more information, see the [deprecated IAM permissions](https://docs.cloud.google.com/cloud-assist/deprecations/permissions) document.

## January 01, 2026

Announcement

### Gemini Cloud Assist documentation migration

Gemini Cloud Assist release notes are now published here. If you are looking for Gemini Cloud Assist release notes prior to January 2026, see the [Gemini for Google Cloud release notes](https://docs.cloud.google.com/gemini/docs/release-notes).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
