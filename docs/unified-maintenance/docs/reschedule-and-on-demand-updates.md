---
url: https://docs.cloud.google.com/unified-maintenance/docs/reschedule-and-on-demand-updates/
title: Control maintenance \u00a0|\u00a0 Unified Maintenance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:32.371464+00:00
---

# Control maintenance  |  Unified Maintenance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/unified-maintenance/docs/reschedule-and-on-demand-updates/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Unified Maintenance ](https://docs.cloud.google.com/unified-maintenance/docs)
  * [ Guides ](https://docs.cloud.google.com/unified-maintenance/docs/overview)



Send feedback 

#  Control maintenance Stay organized with collections  Save and categorize content based on your preferences. 

Depending on the service used, you might have the ability to reschedule or perform on-demand updates. See the type of controls supported by various products in the [Supported services](https://docs.cloud.google.com/unified-maintenance/docs/supported-services).

### Reschedule maintenance

For products that support rescheduling a scheduled maintenance, you might find a link to reschedule the maintenance in the description field of the log.

For example, the description might look similar to the following:
    
    
    Your instance is scheduled to undergo routine
    maintenance.  As a managed service, Cloud SQL automatically updates instances to
    ensure that the underlying hardware, operating system, and database engine are
    reliable, performant, secure, and up-to-date. Most of these updates are performed
    while your Cloud SQL instance is up and running. However, certain system updates
    require a brief service interruption and are referred to as maintenance which
    typically happens once every few months. Learn more: https://cloud.google.com/sql/docs/mysql/maintenance
      
      
    
    For rescheduling the maintenance see - https://cloud.google.com/sql/docs/mysql/maintenance#reschedule-maintenance

### Perform on-demand updates

Some Google Cloud products allow the user to apply maintenance on-demand. For these products, you can find more information on how to perform updates within the description of the event.

The description might look similar to the following:
    
    
    Description: A Google Cloud Compute Engine instance
    undergoes planned maintenance to update important hardware and/or software
    components. During planned maintenance, the host maintenance policy configured
    for the instance will be used to perform the update. https://cloud.google.com/compute/docs/instances/setting-vm-host-options#viewoptions
      
      
    
    You can perform on-demand maintenance ahead of this schedule with this instance.
    https://cloud.google.com/compute/docs/instances/trigger-host-maintenance-event

## What's next

  * Configure [alerts and notifications](https://docs.cloud.google.com/unified-maintenance/docs/configure-alerts-and-notifications)
  * Implement [common alert policies](https://docs.cloud.google.com/unified-maintenance/docs/implement-common-alert-policies)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
