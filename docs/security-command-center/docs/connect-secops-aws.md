---
url: https://docs.cloud.google.com/security-command-center/docs/connect-secops-aws/
title: Connect to AWS for log data collection \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:13:47.241849+00:00
---

# Connect to AWS for log data collection  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/connect-secops-aws/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Connect to AWS for log data collection Stay organized with collections  Save and categorize content based on your preferences. 

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

The Security Command Center curated detections, threat investigation, and Cloud Infrastructure Entitlement Management (CIEM) capabilities for Amazon Web Services (AWS) require the ingestion of AWS logs using the Google SecOps ingestion pipeline. The AWS log types required for ingestion differ based on what you are configuring:

  * CIEM requires data from the AWS CloudTrail log type.
  * Curated detections require data from multiple AWS log types.



To learn more about the different AWS log types, see [Supported devices and log types](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#aws-log-types).

## Configure AWS log ingestion for CIEM

To generate findings for your AWS environment, the Cloud Infrastructure Entitlement Management (CIEM) capabilities require data from AWS CloudTrail logs.

To use CIEM, do the following when configuring AWS log ingestion.

  1. When setting up your AWS CloudTrail, complete the following configuration steps:

     1. Create one of the following:

        * An organization-level trail that pulls log data from across all AWS accounts.
        * An account-level trail that pulls log data from select AWS accounts.

**Note:** For an account-level trail, Security Command Center won't be able to detect all lateral movement risks.
     2. Set the Amazon S3 bucket or Amazon SQS queue you choose for CIEM to log **management events** from _all regions_.

  2. When setting up a feed to ingest AWS logs using the Security Operations console **Feeds** page, complete the following configuration steps:

     1. Create a feed that ingests all account logs from the Amazon S3 bucket or Amazon SQS queue for _all regions_.
     2. Set the feed **Ingestion labels** key-value pair based on the feed source type, using one of the following options:

        * If the **Source type** is **Amazon S3** , configure one of the following:

          * To extract data every 15 minutes, set the **Label** to `CIEM` and the **Value** to `TRUE`. You can reuse this feed for other Security Command Center services where a 15-minute data latency is acceptable.
          * To extract data every 12 hours, set the **Label** to `CIEM_EXCLUSIVE` and the **Value** to `TRUE`. This option works for CIEM and other potential Security Command Center services where a 24-hour data latency is acceptable.
        * If the **Source type** is **Amazon SQS** , set the **Label** to `CIEM` and the **Value** to `TRUE`.




If you don't configure log ingestion correctly, the CIEM detection service might display incorrect findings. In addition, if there are issues with your CloudTrail configuration, Security Command Center displays the [`CIEM AWS CloudTrail configuration error`](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-scc-errors#ciem-cloudtrail-troubleshoot).

To configure log ingestion, see [Ingest AWS logs into Google Security Operations](https://docs.cloud.google.com/chronicle/docs/ingestion/ingest-aws-logs-into-chronicle) in the Google SecOps documentation.

For full instructions on enabling CIEM, see [Enable the CIEM detection service for AWS](https://docs.cloud.google.com/security-command-center/docs/ciem-enable-service). For more information about CIEM features, see [Overview of Cloud Infrastructure Entitlement Management](https://docs.cloud.google.com/security-command-center/docs/ciem-overview).

## Configure AWS log ingestion for curated detections

Curated detections available with Security Command Center Enterprise help identify threats in AWS environments using both event and context data.

Each [AWS rule set](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#aws-rule-sets) requires certain data to function as designed, including one or more of the following sources:

  * AWS CloudTrail
  * AWS GuardDuty
  * AWS context data about hosts, services, and VPCs.
  * AWS Identity and Access Management



To use these curated detections, you must ingest AWS log data to the Google SecOps tenant, and then enable the curated detection rules.

For more information, see the following in the Google SecOps documentation:

  * [Supported devices and log types for AWS](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#aws-log-types): information about data required by the AWS rule sets.

  * [Ingest AWS logs into Google Security Operations](https://docs.cloud.google.com/chronicle/docs/ingestion/ingest-aws-logs-into-chronicle): steps to collect AWS CloudTrail logs.

  * [Curated detections for AWS data](https://docs.cloud.google.com/chronicle/docs/detection/cloud-threats-category#aws-rule-sets): summary of the AWS rule sets in the Cloud Threats curated detections.

  * [Use curated detections to identify threats](https://docs.cloud.google.com/chronicle/docs/detection/use-curated-detections): how to use curated detections in Google SecOps.




See [Google SecOps log data collection](https://docs.cloud.google.com/security-command-center/docs/secops-limits#aws-logs) for information about the type of log data that customers with Security Command Center Enterprise can ingest to the Google SecOps tenant.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
