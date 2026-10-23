---
url: https://docs.cloud.google.com/web-risk/docs/brand-phishing-protection/
title: Brand Phishing Protection \u00a0|\u00a0 Web Risk \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:57:35.017519+00:00
---

# Brand Phishing Protection  |  Web Risk  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/web-risk/docs/brand-phishing-protection/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Web Risk ](https://docs.cloud.google.com/web-risk/docs)
  * [ Guides ](https://docs.cloud.google.com/web-risk/docs/detect-malicious-urls)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Brand Phishing Protection

Web Risk Brand Phishing Protection is a premium Google Cloud security service that proactively detects and disrupts phishing attacks impersonating brands, with a primary focus on financial institutions. Brand Phishing Protection uses Google's real-time telemetry from billions of users and AI-driven models to identify malicious sites. Detected sites show a Safe Browsing interstitial warning to users.

## Key features

  * **Proactive threat detection** : Uses brand-specific AI models to identify new phishing sites in real time.
  * **Rapid Disruption** : Identified threats are added to the Google Safe Browsing block list within minutes, protecting users across major browsers. 

**Note:** Brand Phishing Protection access is managed through an allowlist. To see if this product is a good fit for you and to request access, contact your sales representative.




## Get started

Access to Brand Phishing Protection requires onboarding with the Google Cloud security team.

  1. Enable the Web Risk API within your Google Cloud console project.

     1. In the Google Cloud console, search for **Web Risk API**.

[Go to the Google Cloud console](https://console.cloud.google.com/security)

     2. Click **Enable**.

  2. Give the required Identity and Access Management permissions to users who need to access Brand Phishing Protection features.

     1. If you don't have the Google Cloud CLI installed, [install](https://cloud.google.com/sdk/docs/install) it.
     2. Grant the Web Risk Viewer role by running the following command for each user: `gcloud projects add-iam-policy-binding {project-id} --member='user:{email}' --role='roles/webrisk.viewer`



## Console dashboard overview

The Brand Phishing Protection Dashboard in the Google Cloud console provides visibility into threat metrics and analytics, including the following features:

  * **Summary Metrics** : The total number of warnings shown to users and the number of malicious hosts blocked.
  * **Geographical Breakdown** : A map-based visualization of global user protection.
  * **Screenshot Gallery** : Screenshots showing detected phishing sites impersonating your brand.
  * **Host Analytics** : A list of detected malicious hosts, including the time that each was first blocked and the number of unique malicious URLs per host.



## Glossary of metrics

The Brand Phishing Protection dashboard uses the following metrics to quantify the impact of phishing attacks and the effectiveness of protection measures.

Metric | Definition  
---|---  
**Warnings shown** | The total number of times Chrome Safe Browsing users were presented with a Google Safe Browsing warning page when attempting to access a malicious URL that's relevant to your brand.  
**Malicious hosts found and blocked** | The number of unique hosts identified as hosting phishing content and subsequently added to the block list.  
**Unique URLs** | The count of distinct relevant malicious URLs associated with a specific host that were identified by Google's detection systems.  
**Unique URLs (customer submitted)** | The number of unique malicious URLs for a host that were explicitly reported to Google by the customer using the Submission API.  
**First blocked** | The timestamp (date and time) when a malicious host was first identified and added to the Google Safe Browsing block list.  
**Last warning** | The most recent date a warning was issued for malicious URLs on this host.  
**Total blocked hosts** | The total number of unique malicious hosts detected that are relevant to your brand.  
  
## Submission best practices

Even though Brand Phishing Protection is proactive, you can also programmatically submit phishing URLs using the Submission API to help improve detection accuracy and accelerate disruption of known threats.

For more information, see [Best practices for using the Submission API](https://docs.cloud.google.com/web-risk/docs/best-practices-submission).

### Submission closed reasons

Web Risk Brand Phishing Protection customers receive access to additional context on closed submissions.

For more information about why a submission might be closed without being added to a block list, see [Understanding CLOSED reasons](https://docs.cloud.google.com/web-risk/docs/long-running-operations#closed-reasons).

### Submission API dashboard overview

**Note:** The _Submission API_ tab is available exclusively to Brand Phishing Protection customers. Standalone Submission API customers must continue to use the API to check submission status. The submissions dashboard shares the same project setup, API enablement, and IAM permissions (such as the `roles/webrisk.viewer` role) described in Get started.

For Brand Phishing Protection customers, the Google Cloud console includes a _Submission API_ tab. Even though the Submission API is designed for programmatic, high-volume reporting, the _Submission API_ tab provides a user-friendly interface to track the status of your submissions in real time. The dashboard helps you monitor submission volume, verify acceptance rates, and understand verdict outcomes without the need to build custom monitoring tools or manually poll the API for operation results.

#### Submission API metrics

The _Submission API_ tab provides the following metrics to track the status of submissions:

Metric | Definition  
---|---  
**Total submissions** | The total number of URLs submitted during the selected time range.  
**Submission API SUCCEEDED rate** | The percentage of submitted URLs that were approved and added to the Google Safe Browsing block list.  
**Median SUCCEEDED time** | The median duration between submission and the URL being added to the Google Safe Browsing block list.  
  
#### Submissions table details

The submissions table in the Google Cloud console shows the following details about each submission:

Column | Description  
---|---  
**Status** | The current state of the submission (for example, `RUNNING`, `SUCCEEDED`, or `CLOSED`).  
**Submitted URL** | The URL that was reported.  
**Submission Time** | The date and time when the URL was submitted.  
**Time to Analyze** | The duration starting from the time of submission to the time the analysis was completed.  
**Verdict Rationale** | The reason for closed submissions, see [Understanding CLOSED reasons](https://docs.cloud.google.com/web-risk/docs/long-running-operations#closed-reasons).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
