---
url: https://docs.cloud.google.com/billing/docs/how-to/restart-services/
title: Restarting Google Cloud Services \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:20.108632+00:00
---

# Restarting Google Cloud Services  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/restart-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Restarting Google Cloud Services Stay organized with collections  Save and categorize content based on your preferences. 

## Reopen a closed Cloud Billing account

If your Cloud Billing account was closed due to an issue with your account (such as non-payment of your balance), you might need to manually reopen your Cloud Billing account after you resolve the issues.

Learn how to [reopen a closed Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account#reopen_a_closed_billing_account). 

## Restart services that were shut down

If billing is disabled on your projects, all billable Google Cloud services in the affected projects are shut down. Many services can be restarted after you re-enable billing on the projects, though some services might be removed while billing is disabled. [Learn about data deletion on Google Cloud](https://docs.cloud.google.com/security/deletion#deletion_timeline). _Removed resources are not recoverable._

  * If your [Cloud Billing account was closed](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account), _all_ billable services in _all_ projects that use that Cloud Billing account were stopped. While in this state, some resources might be deleted and might not be fully recoverable. After you [reopen your billing account](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account#reopen_a_closed_billing_account), you might need to manually restart some services.
  * If [billing was disabled on a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#disable_billing_for_a_project), all billable services within that project were stopped. While in this state, some resources might be deleted and might not be fully recoverable. To restart services, you must first [re-enable billing on the project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_an_existing_project).
  * If your [project was shut down](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#shutting_down_projects), all resources within that project were stopped and billing was disabled on the project. When you shut down a project, the project enters a 30-day recovery period, during which you can restore the project to active status. While a project is in this state, some resources might be deleted and might not be fully recoverable, even if you restore the project within the 30-day period. If your project is shut down for more than 30 days, your project and resources are marked for deletion and can't be recovered. To restart services in the project, you must first [restore the project](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects#restoring_a_project) and then [re-enable billing on the project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_an_existing_project).



After your account issues are resolved and billing is re-enabled on your projects, many resources are recovered. Some services have delays in restoring and you might need to wait some time for services to be restored.

### Manually restart services

You might need to manually restart some services in your projects. For Google Cloud, this includes Compute Engine virtual machine (VM) instances, [ephemeral IP addresses](https://docs.cloud.google.com/compute/docs/vm-ip-addresses#reservedaddress), and solid-state persistent disks (SSDs). Almost all instances can be stopped and [restarted](https://docs.cloud.google.com/compute/docs/instances/restarting-an-instance#restart_a_stopped_instance), except for virtual machine instances with local SSDs, which can't be restarted.

To restore your Google Cloud services, you must restart your instances on Google Cloud as follows:

  1. Sign in to the Google Cloud console.

[Sign in to Google Cloud console](https://console.cloud.google.com/)

  2. In the menu menu, select **Compute Engine**.

  3. From the Compute Engine menu, select **VM instances**.

  4. If prompted, select a project.

  5. Select the checkboxes next to the instances that you want to start.

  6. To restart the instances, click **start** play_arrow.




Although most instances can be restarted quickly after re-enabling billing, [Google Kubernetes Engine](https://docs.cloud.google.com/kubernetes-engine/docs) clusters can take up to 60 minutes to recover.

**Note:** After you restart the instance, check your external DNS to ensure it's configured correctly.

## Related topics

  * [Resetting or restarting an instance](https://docs.cloud.google.com/compute/docs/instances/restarting-an-instance)
  * [Starting, stopping, and restarting instances](https://docs.cloud.google.com/sql/docs/mysql/start-stop-restart-instance)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
