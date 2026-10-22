---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules/
title: Deployment schedules \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:22:07.227796+00:00
---

# Deployment schedules  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/deployment-schedules/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Deployment schedules Stay organized with collections  Save and categorize content based on your preferences. 

Google Cloud manages your Contact Center AI Platform (CCAI Platform) instances to ensure that they receive security updates, new features, and performance improvements. You can control the timing of those updates by choosing a deployment schedule for your instance.

There are three deployment schedules:

  * **Rapid**. Get updates as early as possible. Google recommends the rapid deployment schedule for instances that are in pre-production environments, such as development or testing instances.

  * **Regular**. Get updates at least two days after updates are available with rapid deployment. These updates are performed in parallel with critical updates.

  * **Critical**. Get updates outside of your peak business hours, starting at least two days after updates are available with rapid deployment. We update instances set for the critical deployment schedule generally within one week after all rapid deployment schedule instances are updated, although delays beyond one week can occur. We recommend the critical deployment schedule for instances that are in production environments.


**Important:** Google immediately applies security patches to CCAI Platform instances with regular and critical deployment. These are not delayed for two days after rapid deployment.

CCAI Platform instances that were created before deployment schedules were available are set for rapid deployment.

You can select a deployment schedule when you [create a CCAI Platform instance](https://docs.cloud.google.com/docs/get-started#create-ccaip-instance). You can also change the deployment schedule for an existing instance.

Deployment schedules are intended to ensure that upgrades are not done during peak hours. They are not intended to block upgrades for weeks at a time. Google Cloud operates its own maintenance freezes during large national events such as elections, holidays, and peak scale events. If you want to block upgrades of your instance during your own special event, you can open a Google Cloud support request to ask us to block upgrades for your instance.

We don't block instance upgrades for more than one release. Because releases occur approximately every three weeks, this means that we won't block instance upgrades for more than six weeks.

To check the deployment schedule for an instance, do the following:

  1. In the Google Cloud console, go to the project selector dashboard and select the Google Cloud project that contains your instance.

[Project selector dashboard](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. In the navigation menu, click **CCAI Platform**.

[CCAI Platform instances](https://console.cloud.google.com/contact-center-ai-platform)

The **CCAI Platform instances** page displays. The deployment schedule is in the **Schedule** column for your instance.




To change the deployment schedule for an instance, do the following:

  1. In the Google Cloud console, go to the project selector dashboard and select the Google Cloud project that contains your instance.

[Project selector dashboard](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. In the navigation menu, click **CCAI Platform**.

[CCAI Platform instances](https://console.cloud.google.com/contact-center-ai-platform)

The **CCAI Platform instances** page displays.

  3. For the instance that you want to edit, click more_vert **More options** , and then click edit **Edit**.

  4. Click **Configure deployments**.

  5. In the **Deployment schedule** field, select the deployment schedule that you want. If you select **Critical** , you must define your peak business hours by creating at least one schedule. To create a schedule, do the following:

     1. Click the **Days** field, select the days to include in this schedule, and then click **OK**.

     2. In the **Start time** field, enter the start time, including AM or PM. Times are in UTC.

     3. In the **End time** field, enter the end time, including AM or PM. Times are in UTC.

A summary of your schedule appears in local time.

     4. Optional: Click keyboard_arrow_up **Arrow up** or keyboard_arrow_down **Arrow down** to move schedules up or down.

     5. Optional: Click delete **Delete** to delete a schedule.

     6. If you need additional schedules, click **Add schedule** and repeat these steps.

  6. Click **Save**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
