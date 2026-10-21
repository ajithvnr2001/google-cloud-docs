---
url: https://docs.cloud.google.com/web-risk/docs/best-practices-submission/
title: Best practices for using the Submission API \u00a0|\u00a0 Web Risk \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:30:09.831404+00:00
---

# Best practices for using the Submission API  |  Web Risk  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/web-risk/docs/best-practices-submission/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Web Risk ](https://docs.cloud.google.com/web-risk/docs)
  * [ Guides ](https://docs.cloud.google.com/web-risk/docs/detect-malicious-urls)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Best practices for using the Submission API

This document describes the recommended implementation for the Submission API:

  * **Submit complete URLs** : Provide the full, direct URL to the malicious content, not just the domain.
  * **Submit only active URLs** : Submit live URLs only. Offline or unreachable sites can't be processed.
  * **Include policy violations** : Only submit URLs that you have reason to believe are unsafe and violate [Google Safe Browsing Policies](https://safebrowsing.google.com/#policies).

  * **Programmatic submission** : Use the [Submission API](https://docs.cloud.google.com/web-risk/docs/submission-api) to automate high-volume reports from external sources like Security Operations Center teams or end-user reports.

  * **Include additional metadata** : To help improve the speed and accuracy of threat detection, provide metadata with your submissions. For more information, see Improve detection with `ThreatInfo` and `ThreatDiscovery`.




## Improve detection with `ThreatInfo` and `ThreatDiscovery`

We recommend using the following [`ThreatInfo`](https://docs.cloud.google.com/web-risk/docs/reference/rest/v1/projects.uris/submit#threatinfo) and [`ThreatDiscovery`](https://docs.cloud.google.com/web-risk/docs/reference/rest/v1/projects.uris/submit#threatdiscovery) fields to provide additional information about submissions, which can improve detection and increase the chances of a submission being blocked.

  * Use `ThreatInfo` to provide more information about why the URI is being submitted.
  * Use `ThreatDiscovery` to provide more information about how the threat was found.



### Example

An attacker launches a credential phishing site targeting clients of a bank based in Italy. Targeted clients begin receiving deceptive text messages from that attacker with a link to a fake login page. The bank receives reports from clients that received the texts, launches an investigation, and confirms that the site is phishing for credentials.

To help protect their clients, the bank submits the phishing site to Web Risk with the following request body:
    
    
    {
      "submission": {
        "uri": "http://example.com/login.html"
      },
      "threatDiscovery": {
        "platform": "ANDROID",
        "regionCodes": "IT"
      },
      "threatInfo": {
        "abuseType": "SOCIAL_ENGINEERING",
        "abuseSubtype": "BANK_PHISHING",
        "threatJustification": {
          "labels": ["USER_REPORT", "MANUAL_VERIFICATION"],
          "comments": "Site is impersonating a bank and phishing for login credentials"
        },
        "threatConfidence": {
          "level": "HIGH"
        },
        "targetedBrand": {
          "brandName": "Altostrat",
          "domain": "altostrat.com"
        }
      }
    }
    

**Note:** `abuseSubtype` and `targetedBrand` are available in [Preview](https://cloud.google.com/products#product-launch-stages).

When the bank checks the status of the submission with the operation name returned by the Submission API, the status is `SUCCEEDED`. This status indicates that the submitted URL was added to the Safe Browsing block list.

## What's next

  * View the API reference for `ThreatInfo` and `ThreatDiscovery` ([RPC](https://docs.cloud.google.com/web-risk/docs/reference/rpc/google.cloud.webrisk.v1#submiturirequest), [REST](https://docs.cloud.google.com/web-risk/docs/reference/rest/v1/projects.uris/submit)).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
