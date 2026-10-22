---
url: https://docs.cloud.google.com/fault-injection-testing/exclusion-windows/
title: Set up an exclusion windows \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:49:51.987899+00:00
---

# Set up an exclusion windows  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/exclusion-windows/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Guides ](https://docs.cloud.google.com/fault-injection-testing/overview)



Send feedback 

#  Set up an exclusion windows Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes exclusion windows in Fault Injection Testing and how to use them to protect your applications and services during critical business operations.

Exclusion windows enhance your control over resilience testing schedules. An exclusion window is a time period you define, during which new fault injection experiments are prevented from starting. This feature helps you protect your applications and services during critical events, such as:

  * Peak traffic hours or high-volume sales events
  * Major system migrations or upgrades
  * Critical maintenance windows



While an exclusion window is active, Fault Injection Testing blocks any attempts to start new experiments within the defined scope. Any experiments that were already running before the exclusion window became active are permitted to continue until they complete.

## How exclusion windows work

### Scope and targeting

When you configure an exclusion window, you select a specific Cloud region. Once activated, the exclusion window prevents new experiments from starting _only_ within that designated region, regardless of the experiment template used.

### Activation and duration

Creating an exclusion window defines its parameters but does not immediately activate it. You must explicitly start the window to make it active.

An active exclusion window stops blocking experiments in one of two ways:

  * **Automatic expiration:** Each exclusion window is configured with a duration. Once activated, the window automatically deactivates after this duration has passed. The system calculates the end time (start time + duration) and stops blocking new experiments once the current time passes this end time.
  * **Manual stop:** You can manually stop an active exclusion window before its scheduled duration expires. This is useful if the critical period ends earlier than expected and you want to resume testing immediately.



## Manage exclusion windows in the Google Cloud console

Before proceeding, you must have the `roles/faulttesting.operator` role.

### Create and configure an exclusion window

  1. In the Google Cloud console, navigate to the Fault Injection Testing **Exclusion windows** page.
  2. Click **Create exclusion window**.
  3. Specify the **Cloud Region** , **Duration** , and an optional **Description**.
  4. Click **Create**.



### Manually control an exclusion window

You can manually trigger **Start** and **Stop** actions for any configured exclusion window directly from the Google Cloud console.

### Automatically activate an exclusion window

You may want, for example, to align with a scheduled maintenance window or recurring event. To automate the activation of an exclusion window:

  1. After creating an exclusion window, copy the **HTTPS URL** for the `StartExclusionWindow` RPC displayed in the UI.
  2. Use a scheduling service like [Cloud Scheduler](https://docs.cloud.google.com/scheduler) to set up a job that sends a request to this URL at your chosen time.



## Manage exclusion windows using the Google Cloud CLI

You can manage exclusion window resources using the `gcloud alpha fault-testing exclusion-windows` commands.

### Create an exclusion window

To create an exclusion window, use the `create` command. Specify the window ID, the target region, and the duration:
    
    
    gcloud alpha fault-testing exclusion-windows create EXCLUSION_WINDOW_ID \
        --location=REGION \
        --duration=DURATION \
        [--description="DESCRIPTION"]
    

Replace the following:

  * `EXCLUSION_WINDOW_ID`: A unique identifier for the window (for example, `black-friday-freeze`).
  * `REGION`: The Google Cloud region where this window applies (for example, `us-central1`).
  * `DURATION`: The active duration, specified in seconds (for example, `86400s` for 24 hours).
  * `DESCRIPTION`: (Optional) A description of the window's purpose.



Example:
    
    
    gcloud alpha fault-testing exclusion-windows create black-friday-freeze \
        --location=us-east1 \
        --duration=259200s \
        --description="Exclusion window for Black Friday to Cyber Monday sales period"
    

### Delete an exclusion window

To delete an exclusion window definition, use the `delete` command:
    
    
    gcloud alpha fault-testing exclusion-windows delete EXCLUSION_WINDOW_ID \
        --location=REGION
    

### Start an exclusion window

To activate a configured exclusion window, use the `start` command:
    
    
    gcloud alpha fault-testing exclusion-windows start EXCLUSION_WINDOW_ID \
        --location=REGION
    

### Stop an exclusion window

To manually deactivate an active exclusion window early, use the `stop` command:
    
    
    gcloud alpha fault-testing exclusion-windows stop EXCLUSION_WINDOW_ID \
        --location=REGION
    

## Best practices

When creating an exclusion window, consider the following:

  * **Plan for experiment overlap**. Start your exclusion windows slightly before your critical business period begins. Because running experiments are allowed to finish, starting the window early ensures all faults are cleared before your critical period starts.
  * **Use descriptive identifiers**. Use clear, meaningful IDs (for example, `black-friday-freeze` or `system-migration-us-east1`) to identify the purpose and scope of the window.
  * **Align duration with event type**. Match the window duration to the expected length of the critical event. For major holiday sales, a multi-day duration (for example, `259200s` for 3 days) is recommended.
  * **Leverage automation**. Use Cloud Scheduler to automate the activation of exclusion windows for recurring events or planned maintenance to reduce manual effort and risk of omission.
  * **Maintain flexibility**. Remember that you can use the `stop` command to end a window early if a critical period finishes sooner than expected, allowing you to resume resiliency testing immediately.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
