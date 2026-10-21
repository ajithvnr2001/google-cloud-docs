---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-recording-data-storage/
title: Call Recording - Data Storage \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:41:22.157292+00:00
---

# Call Recording - Data Storage  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/call-recording-data-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Call Recording - Data Storage Stay organized with collections  Save and categorize content based on your preferences. 

Once a call is completed, the call recording is uploaded to your CRM. Call recordings are then deleted from the original server as soon the recording is successfully upload to your CRM. Successful uploads usually occur >99% of the time.

There are only three (3) scenarios when a call recording deletion would be delayed after call completion:

  1. Customer CRM has not sent an acknowledgment of successful data upload,

  2. The CRM API limit has been reached, or

  3. The call recording file is too large for the CRM system to upload.




The CCAI Platform service utilizes a retry mechanism with an exponential back off to upload the call recording to the customer CRM system in these scenarios.

As soon as the recording is successfully submitted, it is deleted from the carrier platform. In all cases, the call recording is retained for no more than seven (7) days. During the delayed retention of the recording, the carrier cannot access the recording at any time. The recording is only accessible using MFA handshakes and only the authenticated CRM keys can access that.

## Maximum file size

If the call recording size exceeds 50MB, CCAI Platform will split the file into smaller size files then attach them to CRM ticket in order.

Example: if the file size is 70MB, CCAI Platform will divide it into 50MB and 20MB files then attach them as separate recordings to the CRM ticket.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
