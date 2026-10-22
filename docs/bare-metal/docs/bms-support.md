---
url: https://docs.cloud.google.com/bare-metal/docs/bms-support/
title: Get support \u00a0|\u00a0 Bare Metal Solution \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:26:44.103780+00:00
---

# Get support  |  Bare Metal Solution  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bare-metal/docs/bms-support/

The availability of Bare Metal Solution is transitioning to a specialized, allowlist-only model. If you are an existing customer, please contact your Google account team to explore the value of migrating to new [Oracle and Google Cloud strategic partnership offerings](https://docs.cloud.google.com/bare-metal/docs/explore-oracle-partnership-offerings). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Bare Metal ](https://docs.cloud.google.com/bare-metal/docs)
  * [ Resources ](https://docs.cloud.google.com/bare-metal/docs/resource)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Get support

## Get a Google support package

Google Cloud offers different support packages to meet different needs, such as 24/7 coverage, phone support, and access to a technical support manager. For more information, see [Cloud Customer Care](https://docs.cloud.google.com/support).

### Recommendations for efficient support

When you contact technical support, we recommend that you have the following information ready:

  * Name of your server
  * Troubleshooting that you have performed
  * Screenshot of the error, if applicable
  * Specific date and time if you would like to reimage the server
  * Alternative contact information to supplement the primary contacts you set in **Essential contacts - Technical**
  * SOS report: We might request you for an SOS report to troubleshoot the issue. See Generate and share SOS report.
  * Logs: We might request specific logs based on your issue.



## Respond to the support team

If there is an issue with your Bare Metal Solution environment that requires attention, Cloud Customer Care needs to contact you right away. The following information explains how to set up your Google Cloud project to receive notifications from Cloud Customer Care, the importance of keeping your contact information up to date, and the need for you to respond promptly when we do contact you.

### Set up contact information in your Google Cloud project

When you set up your Google Cloud project during the provisioning process, there are two key items you need to configure:

  * Essential contacts - Technical
  * Project Owner(s)



The Cloud Customer Care team uses the _Essential contacts - Technical_ entry as the primary way to contact you, with the _Project Owner_(s) as a backup contact.

To set up the **Essential contacts - Technical** entry in your Google Cloud project, see [Managing contacts for notifications](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts). We recommend that you use a group email address as your first entry for **Essential contacts - Technical** so that [Cloud Customer Care](https://cloud.google.com/support-hub) can reach your entire on-call team responsible for critical incident response.

You are responsible for managing and updating these contacts. Because of the critical nature of this type of communication, you must review your contacts on a regular basis and keep the contact information up to date.

### When Cloud Customer Care contacts you

Cloud Customer Care contacts you proactively if there is a maintenance or operational event that might impact your Bare Metal Solution environment, such as:

  * When we need to confirm a maintenance window, and discuss the associated downtime or actions that you need to take.
  * If we find an issue with your Bare Metal Solution infrastructure that needs attention, such as an outage or hardware failure.
  * If there is an unresponsive server and we need your help to troubleshoot the issue.
  * If we need to restore an application or database to full operation.



We also might send you maintenance notices to correct potentially impactful hardware errors in a timely manner. If you delay in responding to us, this inaction might expose you to additional risk of hardware failure.

For these many reasons, respond to Cloud Customer Care with urgency when we contact you. The messages we send you alert you to either a current, production-impacting event or a planned maintenance event. When we contact you, be sure to call us back or reply to the email.

To learn about Bare Metal Solution maintenance process and how to prepare for the maintenance events, see [Prepare for Bare Metal Solution maintenance events](https://docs.cloud.google.com/bare-metal/docs/bms-maintenance-process).

## Contact support

If you already have a support package, you can contact [Cloud Customer Care](https://cloud.google.com/support-hub).

For Bare Metal Solution, file a support case for a problem or a service request such as rebooting or reimaging a server, changing the network configuration, or requesting hardware changes in your environment.

To get help with a problem, specify the category that is most relevant to your issue when you open a case.

Field | Specification  
---|---  
Product | **Bare Metal Solution**  
Category | Select a category as appropriate.  
  
## Generate and share SOS report

**Applicable only to Oracle Linux and Red Hat Enterprise Linux (RHEL) users.**

An SOS report contains configuration details, system information, and diagnostic information of your system. We might request you for an SOS report to perform a root cause analysis and troubleshoot your issue.

We recommend that you generate SOS reports at the following times:

  1. Before changing the OS configuration of your server.
  2. Immediately after changing the OS configuration but prior to rebooting the server.
  3. Immediately after the reboot following the change in the OS configuration.

**Caution:** Running the `sosreport` utility with `ethtool -d` can cause a buffer overflow and kernel panic. Before using the `sosreport` utility, read about this issue and how to prevent it . See [Buffer overflow when using ethtool with debug flag](https://docs.cloud.google.com/bare-metal/docs/known-issues#buffer-overflow-with-ethtool). 

To generate and share an SOS report, follow these steps:

  1. Run the following command to see if the `sosreport` package is installed on your server.
         
         rpm -qa | grep sos
         

If the `sosreport` package is installed, you'll see the version of the `sosreport` package. For example:
         
         sos-3.2-35.el7_2.3.noarch

If the package is not installed, the output is blank.

  2. If the package is not installed, as the root user, run the following command to install the `sosreport` package:
         
         sudo yum install sos

  3. To generate the SOS report, as the root user, run the following command:
         
         sudo sosreport

When prompted, press the **Enter** or **Return** key to continue.

  4. (If running Oracle Linux) When prompted, accept the default name for the file by pressing the **Enter** or **Return** key.

  5. When prompted, enter the case ID if you have one.

  6. Locate the report. When the command finishes executing, you'll see the location of the SOS report in its output, as shown in the following example:
         
         Your sosreport has been generated and saved in:
         /var/tmp/sosreport-breakboot2-2021-03-30-lyrkotf.tar.xz
         Size   8.76MiB
         Owner  root
         md5    afda594259aade437dd00c44f92d66db
         Please send this file to your support representative.
         

  7. By default, the system generates the report in `tar` format. Convert it to `zip` format.

  8. Upload the report to the support case.




If you're unable to upload the report to the case, follow these steps:

  1. Upload the report to a Google Drive folder.

  2. Right-click the file, and click **Share**.

  3. In the **Add people and groups** field, enter the following email address:

`gcp-ps-oracle-team-global@google.com`.

  4. Select the **Editor** role.

  5. Click **Copy link**.

  6. Click **Done**.

  7. Add the copied link into your support case.




## Scope of support for Bare Metal Solution

Cloud Customer Care covers the following areas in Bare Metal Solution environments:

  * The bare-metal servers and attached storage
  * The network and interconnect
  * Physical and network security
  * The facilities



Service level agreements define initial response times for Cloud Customer Care according to the [Google Cloud technical support services guidelines](https://cloud.google.com/terms/tssg/).

Google Cloud does not provide support for the operating system or your application software and databases that run in a Bare Metal Solution environment.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
