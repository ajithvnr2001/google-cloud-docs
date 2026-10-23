---
url: https://docs.cloud.google.com/security-command-center/docs/respond-cloud-run-threats/
title: Respond to Cloud Run threat findings \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:38:03.625031+00:00
---

# Respond to Cloud Run threat findings  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/respond-cloud-run-threats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Respond to Cloud Run threat findings Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

This document offers informal guidance on how you can respond to findings of suspicious activities in your Cloud Run resources. The recommended steps might not be appropriate for all findings and might impact your operations. Before you take any action, you should investigate the findings; assess the information that you gather; and decide how to respond.

**Note:** The techniques that Security Command Center provides aren't guaranteed to be effective against any previous, current, or future threats that you face. For information about why Security Command Center does not provide official remediation guidance for threats, see [Approach to threat finding remediation](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats#remediating_threats).

## Before you begin

  1. [Review the finding](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats#reviewing_findings). Note the affected container and the detected binaries, processes, or libraries.
  2. To learn more about the finding that you're investigating, search for the finding in the [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index).



## General recommendations

  * Contact the owner of the affected resource.
  * [View the logs](https://docs.cloud.google.com/run/docs/logging#viewing-logs) for the potentially compromised Cloud Run service, job, or worker pool.
  * For forensic analysis, collect and back up the logs from the affected Cloud Run resource.
  * For further investigation, consider using incident response services like [Mandiant](https://docs.cloud.google.com/security/consulting/mandiant-incident-response-services).
  * Consider deleting any of the following affected Cloud Run resources:

    * Delete the affected [service](https://docs.cloud.google.com/run/docs/managing/services#delete).
    * [Roll back to a previous service revision](https://docs.cloud.google.com/run/docs/rollouts-rollbacks-traffic-migration#rollback), or deploy a new, more secure revision, and then [delete the affected revision](https://docs.cloud.google.com/run/docs/managing/revisions#delete).
    * Delete the affected [job](https://docs.cloud.google.com/run/docs/managing/jobs#delete).
    * Delete the affected [worker pool](https://docs.cloud.google.com/run/docs/managing/workerpools#delete).
    * [Roll back to a previous worker pool revision](https://docs.cloud.google.com/run/docs/managing/workerpool-instance-splits-rollbacks), or deploy a new, more secure revision, and then [delete the affected revision](https://docs.cloud.google.com/run/docs/managing/workerpool-revisions#delete).



## Malicious script or Python code executed

If the script or Python code was making intended changes to the container, [deploy a revision](https://docs.cloud.google.com/run/docs/deploying#revision) to the service that has all the intended changes. Don't rely on a script to make changes after the container is deployed.

## What's next

  * Learn [how to work with threat findings in Security Command Center](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats).
  * Refer to the [Threat findings index](https://docs.cloud.google.com/security-command-center/docs/threat-findings-index).
  * Learn how to [review a finding](https://docs.cloud.google.com/security-command-center/docs/how-to-investigate-threats#reviewing_findings) through the Google Cloud console.
  * Learn about the [services that generate threat findings](https://docs.cloud.google.com/security-command-center/docs/concepts-security-sources#threats).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
