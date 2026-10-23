---
url: https://docs.cloud.google.com/unified-maintenance/docs/turn-off-logs-storage/
title: Turn off logs storage \u00a0|\u00a0 Unified Maintenance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:56.836778+00:00
---

# Turn off logs storage  |  Unified Maintenance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/unified-maintenance/docs/turn-off-logs-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Unified Maintenance ](https://docs.cloud.google.com/unified-maintenance/docs)
  * [ Guides ](https://docs.cloud.google.com/unified-maintenance/docs/overview)



Send feedback 

#  Turn off logs storage Stay organized with collections  Save and categorize content based on your preferences. 

You cannot deactivate Unified Maintenance, but you can opt out of storing these logs. You can either [disable the Default sink](https://docs.cloud.google.com/logging/docs/routing/overview#buckets) in the Log Router, or you can configure an [exclusion filter](https://docs.cloud.google.com/logging/docs/routing/overview#exclusions) specific to Unified Maintenance logs.

## Exclusion filters

Exclusion filters let you exclude log entries that match the inclusion filter from being routed to the sink's destination or from being stored in a log bucket.

### Enforce exclusion filter

To enforce an exclusion filter for Unified Maintenance logs:

  1. In the Google Cloud console, go to the **Log Router** page. If you use the search bar to find this page, select the result whose subheading is **Logging**. 

[Go to Logs Router](https://console.cloud.google.com/logs/router)

  2. Select the Google Cloud project from which the log entries that are being routed originate.
  3. Click **Create sink**.
  4. Provide a **Sink name** and **Sink description** and then click **Next**.
  5. In the **Select sink service** list, select a sink service and then select a destination.
  6. Select **Choose logs to filter out of sink**.
  7. Click **Add exclusion**.
  8. Provide an **Exclusion filter name** and an **exclusion filter**. To exclude all maintenance event logs, enter: 
         
         LOG_ID("maintenance.googleapis.com/maintenance_events") 

  9. Click **Create sink**.



You should see a message indicating that your log sink was successfully created.

### Remove exclusion filter

To remove an exclusion filter for Unified Maintenance logs:

  1. In the Google Cloud console, go to the **Log Router** page. If you use the search bar to find this page, select the result whose subheading is **Logging**.

[Go to Logs Router](https://console.cloud.google.com/logs/router)

  2. Select the Google Cloud project from which the log entries that are being routed originate.

  3. Select the sink that controls your exclusion filter.

  4. Click more_vert **More actions** and select one of the following:

     1. **Edit sink—** lets you remove the exclusion query; delete the exclusion query and then click **Update sink**.
     2. **Disable sink—** stops all logs from being exported by the sink. Note that any logs that arrive after the sink is disabled are not sent to this sink's destination and will be lost if they are not captured by another sink.



## What's next

  * Product [overview](https://docs.cloud.google.com/unified-maintenance/docs/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
