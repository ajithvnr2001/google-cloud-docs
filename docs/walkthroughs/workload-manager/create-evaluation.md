---
url: https://docs.cloud.google.com/walkthroughs/workload-manager/create-evaluation/
title: Create and run an evaluation \u00a0|\u00a0 Workload Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:03:29.245418+00:00
---

# Create and run an evaluation  |  Workload Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/walkthroughs/workload-manager/create-evaluation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Workload Manager ](https://docs.cloud.google.com/workload-manager/docs)



Send feedback 

#  Create and run an evaluation Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to create an evaluation for your workload in Workload Manager.

### Create a workload evaluation

To create a workload evaluation, follow these steps:

  1. Select a Google Cloud project.
  2. If prompted, to enable the required API for Workload Manager, click **Enable**.
  3. Click **New evaluation**.
  4. In the **Name & rules** pane, do the following: 
     1. For **Evaluation name** , enter a name for the workload evaluation.
     2. For **Description** , enter a description for the workload evaluation.
     3. In the **Workload type** field, select the type of workload evaluation.
     4. From the **Rules table** , select the best practices to include in the workload evaluation.
  5. Click **Continue**.
  6. In the **Scope & filters** pane, do the following: 
     1. In the **Evaluation scope** section, click **Browse projects** to add the projects that contain the resources that you want to evaluate.
     2. In the **Apply filters to resources** section, click **Add filter** , and then use the following types of filters to select specific resources from the selected projects: 
        * Service agent
        * Label
        * Name

Multiple filters in a filter type use `OR` logic. Across filter types, `AND` logic is used.

  7. Click **Continue**.
  8. In the **Frequency & notification** pane, do the following: 
     1. In the **Scheduling** section, choose how frequently you want the evaluation to run.
     2. Optional: In the **Notification** section, select the events that you want to receive alerts for.
  9. Click **Continue**.
  10. In the **Review** pane, review the workload evaluation. To make any final changes on any page, click the page name on the left pane.
  11. Click **Create**.



### Run a workload evaluation

To run a workload evaluation, follow these steps:

  1. Click the **Evaluation name**.
  2. On the **Evaluation information** page, click **Run**. 

A workload evaluation takes a few minutes to complete. There might be evaluations that aren't completely real-time due to the time it takes for an evaluation to complete.




### Set alerts for evaluations

To set alerts for existing evaluations, do the following:

  1. click the name of the evaluation for which you want to enable notifications.
  2. Click **Edit**.
  3. Select the **Notification** section. 
  4. Select the events for which you want to receive alerts, and then select [notification channels](https://docs.cloud.google.com/monitoring/support/notification-options#creating_channels).
  5. Click **Save**. 



### Next step

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
