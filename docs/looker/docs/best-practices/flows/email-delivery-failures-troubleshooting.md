---
url: https://docs.cloud.google.com/looker/docs/best-practices/flows/email-delivery-failures-troubleshooting/
title: Troubleshooting email delivery failures \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:57.978385+00:00
---

# Troubleshooting email delivery failures  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/flows/email-delivery-failures-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Troubleshooting email delivery failures Stay organized with collections  Save and categorize content based on your preferences. 

Scheduling and sending emails from Looker lets you automatically distribute data and insights to keep your team informed. If these emails fail to arrive, this guide helps you troubleshoot the delivery process and resolve the issues.

## Lifecycle of a scheduled email

Understanding the stages of the email delivery process can help you identify where a failure occurred:

  1. **Schedule configuration:** A user creates and saves a schedule for a Look or dashboard, choosing email as the delivery method.
  2. **Job creation:** The Looker instance creates a scheduled job.
  3. **Query execution and rendering:** At the scheduled time, the Looker instance runs the queries for the content and renders the visualizations as specified in the schedule options.
  4. **Handoff to SMTP:** The Looker instance sends the email to the designated SMTP server (either the default Looker email service or a [custom SMTP server](https://docs.cloud.google.com/looker/docs/admin-panel-platform-smtp#custom_mail_settings)).
  5. **SMTP delivery:** The SMTP server receives the email and delivers it to the recipient's email server.
  6. **Gateway filtering:** Security software (such as Proofpoint) at the recipient's organization may filter out the email as spam or malicious before it reaches the user.
  7. **Inbox routing:** The recipient's email client receives the email, where local spam filters or inbox rules may organize, archive, or delete it.



## Debugging tree

Use the following decision tree to begin troubleshooting email delivery failures:

The following sections describe the scenarios in the tree in further detail.

## Check the scheduler plans

If a scheduled email was not received, first verify that the schedule exists and is active.

### Verify that the schedule was created

Navigate to the [Schedules](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-schedule) page in the **Admin** panel to check if the schedule is listed. You can also use System Activity if it is enabled on your instance.

If the schedule doesn't appear, investigate the following:

  * Verify that the user successfully saved the schedule.
  * Check whether the schedule was deleted or paused.



If the schedule appears, the Looker instance planned to send the email. Continue to the next section.

## Check the scheduler history

If the schedule exists, check its execution status.

### Check the job status

Navigate to the [Scheduler History](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-schedule-history) page in the **Admin** panel and look for the job corresponding to the failed delivery.

  * If the job status is **Complete** , Looker successfully sent the email to the SMTP server. Proceed to the next step.
  * If the job status is NOT **Complete** (for example, if it is **Failed**), investigate the following: 
    * Click the **Details** tab for the job to view error messages.
    * Try running the content (Look or dashboard) manually to see if it renders successfully or returns an error. Common issues include database connection errors or query timeouts.



## Custom SMTP troubleshooting

If the job status is **Complete** and you're using Custom SMTP, the issue likely lies with your SMTP server or DNS configuration.

### Check SMTP server logs

If you have [Custom SMTP](https://docs.cloud.google.com/looker/docs/admin-panel-platform-smtp#custom_mail_settings) enabled, investigate the following:

  * Check your SMTP server logs to verify that the server received the job from Looker and to check if the server attempted delivery.
  * Common issues include authentication failures, incorrect port settings, or rate limiting on your SMTP server.



### Verify SPF records

If your SMTP server is sending emails but they're being marked as spam or rejected by recipients, check your Sender Policy Framework (SPF) records. Incorrect SPF records can cause receiving mail servers to reject emails sent from your domain.

To test SPF records, you can use the `dig` command-line tool:

  1. Run the following command to check the SPF record for your domain (replace DOMAIN_NAME with your domain): `bash dig +short txt <var>DOMAIN_NAME</var> | grep spf`
  2. Verify that the output includes the IP address or hostname of your Custom SMTP server.



## Default SMTP troubleshooting

If you're using Looker's default SMTP service, you don't have direct access to the mail server logs. Check for delivery blocks.

### Check for delivery blocks: security software and spam filters

Before contacting Support, check if the email is being blocked by your organization's security systems or email client settings.

Security software (like Proofpoint) or email client filters can block emails from `lookermail.com` (the default sender domain for Looker).

  * Check your organization's email gateway logs (for example, Proofpoint or Mimecast) for blocked emails from `lookermail.com` or `looker@lookermail.com`.
  * Check the recipient's **Spam** or **Junk** folders.
  * Check whether there are any inbox rules that might be archiving or deleting the emails.
  * **Resolution:** Work with your email administrator to allowlist `lookermail.com` and the IP addresses associated with Looker's default email service.



## Contact Support

If you have verified all the previous steps, and the email is still not received:

  * If you're using default SMTP, [contact Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details) to check the default SMTP logs for your job. Provide the Job ID and recipient email address. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
