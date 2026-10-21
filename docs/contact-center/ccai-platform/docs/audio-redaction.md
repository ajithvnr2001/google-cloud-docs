---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/audio-redaction/
title: Customer Experience Insights audio redaction \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:36:22.950122+00:00
---

# Customer Experience Insights audio redaction  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/audio-redaction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Customer Experience Insights audio redaction Stay organized with collections  Save and categorize content based on your preferences. 

Customer Experience Insights audio redaction is an open-source framework that automatically detects and redacts sensitive personally identifiable information (PII) from audio recordings. It provides a secure, scalable, and customizable solution for organizations that need to process audio data while maintaining compliance with privacy regulations.

This solution acts as a middleware between your raw audio ingestion points and your long-term storage or analytics platforms. It automatically processes audio files to remove sensitive data such as:

  * Credit card numbers
  * Social Security numbers
  * Phone numbers
  * Email addresses
  * Custom entities defined by your organization



By redacting this information before permanent storage, you ensure that your data lakes and analytics tools remain free of toxic data, reducing compliance risk and data exposure.

## Key features

  * **Automated redaction** : Uses Speech-to-Text and Sensitive Data Protection to transcribe, identify, and redact sensitive segments from audio files.
  * **Dual trigger support** : Flexible deployment options lets you trigger redaction either immediately upon file upload to Cloud Storage or downstream after processing by Customer Experience Insights.
  * **Enterprise security** : Designed with a "secure by default" architecture, Customer Experience Insights audio redaction supports private VPCs, VPC Service Controls, and supply-chain security checks to prevent unauthorized access and code tampering.
  * **Scalability** : Built on Dataflow, the pipeline automatically scales to handle massive volumes of audio data, making it suitable for high-throughput contact centers.
  * **Verifiable output** : Produces both the redacted audio file and a redaction transcript, enabling verification and audit trails.



## How it works

The solution follows a linear processing pipeline:

  1. **Ingestion and triggering** :

     * **Option A (Direct)** : An audio file is uploaded to a "raw" Cloud Storage bucket. A Cloud Run trigger immediately launches the pipeline.
     * **Option B (Insights)** : CX Insights processes a conversation. A Pub/Sub message triggers the Cloud Run service, which then launches the pipeline.
  2. **Processing (Dataflow)**. The Dataflow worker does the following:

     1. Retrieves the audio file.
     2. Sends the audio to Speech-to-Text to generate a time-stamped transcript.
     3. Sends the transcript to Sensitive Data Protection to identify the time offsets of sensitive information.
     4. Uses `ffmpeg` to silence the audio segments corresponding to the identified PII.
  3. **Output**. A Cloud Run function does the following:

     1. Optional: Moves the original raw audio to a secure "archive" bucket.
     2. Writes the redacted audio back to the original location or a specified output bucket, replacing the sensitive segments with silence or a tone.



## Get started

To use this solution, you need a Google Cloud project with billing enabled.

### Prerequisites

  * Google Cloud project
  * `gcloud` CLI installed and authenticated
  * Enablement and access to Dataflow, Speech-to-Text, and Sensitive Data Protection Google Cloud services.



### Access and deployment

The full source code and deployment instructions are available in the [GitHub repository](https://github.com/GoogleCloudPlatform/ccaas-audio-redaction).

**Note:** This solution is open-source. We welcome contributions and feedback using GitHub issues.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
