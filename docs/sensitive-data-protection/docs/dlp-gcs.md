---
url: https://docs.cloud.google.com/sensitive-data-protection/docs/dlp-gcs/
title: Using Sensitive Data Protection with Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:31:50.638238+00:00
---

# Using Sensitive Data Protection with Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sensitive-data-protection/docs/dlp-gcs/

Cloud Data Loss Prevention (Cloud DLP) is now a part of Sensitive Data Protection. The API name remains the same: Cloud Data Loss Prevention API (DLP API). For information about the services that make up Sensitive Data Protection, see [Sensitive Data Protection overview](https://cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Sensitive Data Protection ](https://docs.cloud.google.com/sensitive-data-protection/docs)
  * [ Guides ](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



Send feedback 

#  Using Sensitive Data Protection with Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This page contains references to pages that provide information on how to use Sensitive Data Protection with [Cloud Storage](https://docs.cloud.google.com/storage).

## Quickstart guides

[Quickstart: Scheduling an inspection scan](https://docs.cloud.google.com/sensitive-data-protection/docs/schedule-inspection-scan)
    Schedule periodic inspection of a Cloud Storage bucket, a BigQuery table, or a Datastore kind. For detailed instructions, see [Creating and scheduling inspection jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers).

## How-to guides

This section provides a categorized list of task-based guides that demonstrate how to use Sensitive Data Protection with Cloud Storage.

### Inspection

[Inspecting storage and databases for sensitive data](https://docs.cloud.google.com/sensitive-data-protection/docs/inspecting-storage)
    Create a one-time job that searches for sensitive data in a Cloud Storage bucket, a BigQuery table, or a Datastore kind.
[Creating and scheduling inspection jobs](https://docs.cloud.google.com/sensitive-data-protection/docs/creating-job-triggers)
    Create and schedule a job trigger that searches for sensitive data in a Cloud Storage bucket, a BigQuery table, or a Datastore kind. A job trigger automates the creation of Sensitive Data Protection jobs on a periodic basis.

### Working with scan results

[Sending Sensitive Data Protection scan results to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/sending-results-to-scc)
    Scan a Cloud Storage bucket, a BigQuery table, or a Datastore kind, and then send the findings to Security Command Center.
[Analyzing and reporting on Sensitive Data Protection findings](https://docs.cloud.google.com/sensitive-data-protection/docs/analyzing-and-reporting)
    Use Cloud Storage to run analytics on Sensitive Data Protection findings.

## Tutorials

[De-identification and re-identification of PII in large-scale datasets using Sensitive Data Protection](https://docs.cloud.google.com/architecture/de-identification-re-identification-pii-using-cloud-dlp)
    Create an automated data transformation pipeline to de-identify sensitive data like personally identifiable information (PII).
[Automating the classification of data uploaded to Cloud Storage](https://docs.cloud.google.com/sensitive-data-protection/docs/automating-classification-of-data-uploaded-to-cloud-storage)
    Implement an automated data quarantine and classification system using Sensitive Data Protection, Cloud Storage, and Cloud Run functions.

## Community contributions

The following are owned and managed by community members, and not by the Sensitive Data Protection team. For questions on these items, contact their respective owners.

[GitHub: Speech Redaction Framework](https://github.com/GoogleCloudPlatform/dataflow-speech-redaction)
    Redact sensitive information from audio files in Cloud Storage.
[GitHub: Speech Analysis Framework](https://github.com/GoogleCloudPlatform/dataflow-contact-center-speech-analysis)
    Transcribe audio, create a data pipeline for analytics of transcribed audio files, and redact sensitive information from audio transcripts.
[GitHub: Real-time anomaly detection using Google Cloud stream analytics and AI services](https://github.com/GoogleCloudPlatform/df-ml-anomaly-detection)
    Walk through a real-time artificial intelligence (AI) pattern for detecting anomalies in log files.

## Pricing

When you inspect a Cloud Storage bucket, you incur Sensitive Data Protection costs, according to the [storage inspection job pricing](https://cloud.google.com/sensitive-data-protection/pricing#storage-pricing).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
