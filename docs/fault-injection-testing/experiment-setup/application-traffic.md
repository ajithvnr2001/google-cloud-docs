---
url: https://docs.cloud.google.com/fault-injection-testing/experiment-setup/application-traffic/
title: Set up an experiment for Degrade Application Traffic \u00a0|\u00a0 Fault Injection Testing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:52:42.072858+00:00
---

# Set up an experiment for Degrade Application Traffic  |  Fault Injection Testing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/fault-injection-testing/experiment-setup/application-traffic/

To request access to Fault Injection Testing during Preview, contact your Google Cloud account manager. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Fault Injection Testing ](https://docs.cloud.google.com/fault-injection-testing)
  * [ Guides ](https://docs.cloud.google.com/fault-injection-testing/overview)



Send feedback 

#  Set up an experiment for Degrade Application Traffic Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page explains how to set up a new experiment template for Degrade Application Traffic fault.

This fault lets you selectively degrade L7 traffic through a specified [application load balancer](https://docs.cloud.google.com/load-balancing/docs/application-load-balancer).

Before proceeding, you must have the following:

  * Permission to view Load Balancer Forwarding rules and Backend Services in the project – `compute.viewer, compute.networkViewer` or `viewer` role.
  * The `roles/faulttesting.operator` role.



To create a new experiment template, do the following:

  1. Open the [Google Cloud console](https://console.cloud.google.com/).
  2. Navigate to the Fault Injection Testing **Overview** page.
  3. Select **Create experiment template**. 
     * Alternatively, from the Fault Injection Testing **Overview** page, click **Experiment templates** on the left navigation bar, and click **Create Template**.
  4. In the **Fault Type** section, select the **Degrade application traffic** option.
  5. In the **Target** section, use the filters and select either **XLB (External Load Balancer)** or **ILB (Internal Load Balancer)**. 
     * (Mandatory) Select the **Load balancer frontend service** that is part of the [forwarding rule](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts) you want to target.
  6. In the **Fault Parameters** section, set the following: 
     * Type of load balancer fault - choose from the following: 
       * **HTTP delay injection** \- insert a delay into the selected forwarding rule.
       * **Delay percentage** \- percentage of traffic to impact with a delay. The remaining traffic will pass as normal.
       * **Latency duration** \- how much latency to add to this delayed traffic.
     * **HTTP error injection** \- send HTTP error responses for the selected forwarding rule. Specify the following parameters: 
       * **Error code** \- the error response code you expect to see from your load balancer, ideally a 5xx response code.
       * **Error percentage** \- percentage of traffic that will send the specified error response code. The remaining traffic will receive normal response codes.
     * **Experiment duration** \- determines how long the fault condition should last.
  7. In the **Template name** section, provide a clear and descriptive name for the template. Optionally provide details in the description.
  8. In the **Verify** section: 
     1. See a recap of the settings you selected.
     2. Wait for the automated dry run to finish.
     3. After the dry run is complete, the list of resources that will receive the fault injection appears. If there are errors with the targeted resources, they will also appear here.
  9. **Create** the experiment template. A confirmation message indicating that the template has been created appears, and the new template shows up in the list of templates.



## What's next

[Run an experiment](https://docs.cloud.google.com/fault-injection-testing/run-experiment) using the experiment template you created.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
