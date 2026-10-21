---
url: https://docs.cloud.google.com/security-command-center/docs/error-messages/
title: Error messages \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:46:46.543052+00:00
---

# Error messages  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/error-messages/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Error messages Stay organized with collections  Save and categorize content based on your preferences. 

Standard-legacy, Standard, Premium, and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

Learn how to resolve some errors raised by Security Command Center. This topic discusses errors whose resolutions require more steps than can be easily described in an error message.

**Note:** For more troubleshooting information, see [Troubleshooting](https://docs.cloud.google.com/security-command-center/docs/troubleshooting). In addition, Security Command Center provides error detectors, which report configuration errors that prevent Security Command Center and its services from working properly. Each error finding includes suggested remediation steps. For more information, see [Security Command Center errors](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors).

## Notifications

You might get the following errors when you use the Security Command Center API notifications feature.

### Error reading credential file from environment variable

`java.lang.RuntimeException: java.io.IOException: Error reading credential file from environment variable GOOGLE_APPLICATION_CREDENTIALS`

This error occurs when you try to use the Security Command Center notifications API and the service account keys aren't accessible. To resolve this error, do the following:

  * Complete the steps to [set up a service account](https://docs.cloud.google.com/security-command-center/docs/how-to-notifications) and get the service account key.
  * If you're using an IDE like Intellij, make sure that your development environment is configured to point to the location where the service account key is stored.



### Invalid choice: `add-iam-policy-binding`

`ERROR: (gcloud.pubsub.topics) Invalid choice: 'add-iam-policy-binding'`

This error most commonly occurs when you aren't using the most current version of the Google Cloud CLI. To resolve this error, update to the latest gcloud CLI version by running:
    
    
    gcloud components update
    

## Web Security Scanner

To contact us about the error messages below, [send feedback](https://docs.cloud.google.com/security-command-center/docs/getting-support) about the specific scan.

Error message | Description  
---|---  
The app often redirected the scanner to an authentication page |  If you're using Google authentication, the scanner detects auth redirects. Most likely the credentials you're using to scan the site are invalid. To check the validity of credentials, start a Chrome incognito session and try to log in with the test credentials on your application.   
The app produced a high number of errors during this scan |  Web Security Scanner found that a high percentage of requests resulted in `4xx` or `5xx` HTTP responses. Verify your scanning credentials and the target URL. If the problem continues to occur, [file a bug](https://docs.cloud.google.com/security-command-center/docs/getting-support).   
The scan found a small number of results during crawling |  Web Security Scanner didn't find many pages to test. This error is expected for sites that don't often change the URL and sites that have application features behind multi-step navigation bars. Try adding more seed URLs, like the URL for each feature that a navigation bar leads to.   
The scan found too many URLs while crawling results and has not tested all of them.  |  This problem can appear if your app has many URLs that lead to the same template. In this case, [file a feature request](https://docs.cloud.google.com/security-command-center/docs/getting-support) and the team might be able to tune the duplicate-page logic for you.   
An internal error occurred during the scan. |  This message can indicate one or more internal errors. If you get this message, [send feedback](https://docs.cloud.google.com/security-command-center/docs/getting-support) about the specific scan.   
The scan timed out while crawling the app |  There is a time limit for each stage of the crawler.

  * If you have a large site, then this error may occur. [File a feature request](https://docs.cloud.google.com/security-command-center/docs/getting-support), and the team can manually increase your crawl timeout. 
  * If you have a small site, then something might have gone wrong with the crawler. [File a bug](https://docs.cloud.google.com/security-command-center/docs/getting-support) with your scan details to request a review. 

  
The scan triggered a DDOS protection mechanism and has been stopped |  This error is caused by too many queries, too fast. Try reducing the Queries Per Second (QPS).   
  
### Fixing issues

If Web Security Scanner reports an issue, you need to disable browser cross-site scripting (XSS) protection and then verify the location. For more information, see [Verify the issue](https://docs.cloud.google.com/security-command-center/docs/how-to-remediate-web-security-scanner-findings#verify_the_issue).

**Important:** If you disable XSS protection in the browser, only use that browser instance to test your own security issues.

## What's next

Learn about [Security Command Center errors](https://docs.cloud.google.com/security-command-center/docs/concepts-scc-errors).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
