---
url: https://docs.cloud.google.com/looker/docs/best-practices/flows/troubleshooting-embed-setup/
title: Troubleshooting embed setup \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:41:57.382436+00:00
---

# Troubleshooting embed setup  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/flows/troubleshooting-embed-setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Troubleshooting embed setup Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to troubleshoot issues with setting up Looker embedding. If your embedded content fails to load, there are several possible reasons to check.

## Decision tree

Use the following decision tree to troubleshoot embed setup issues:

## Troubleshooting steps

The following sections describe the scenarios in the tree in further detail.

### Is this signed embedding?

See the [Signed embedding](https://docs.cloud.google.com/looker/docs/signed-embedding) documentation for more information about signed embedding.

If you're using signed embedding, proceed to Does private embed work?. If you aren't using signed embedding, see Third-party cookie issue.

### Does private embedding work?

Check whether [private embedding](https://docs.cloud.google.com/looker/docs/private-embedding) works.

If private embedding works, proceed to Signed embedding troubleshooting. If private embedding doesn't work, see Third-party cookie issue.

### Third-party cookie issue

Check the domain of the embedded platform and the domain of the embed URL. If the base domains don't match, the issue may be caused by third-party cookies being blocked by the browser.

For example, if your embed application is hosted on `example.com` but your Looker instance URL used for embedding is `customer.cloud.looker.com`, browsers may block cookies from `customer.cloud.looker.com` when the Looker iframe is embedded in `example.com`. If your Looker instance was instead on `looker.example.com`, cookies would be first-party as base domain `example.com` matches.

If the issue is caused by third-party cookie denial, you can either enable third-party cookies in your browser or configure a custom domain. For Looker (Google Cloud core) instances, you can configure a [custom domain](https://docs.cloud.google.com/looker/docs/looker-core-custom-domain) using self-service. For Looker (original) instances, a [custom domain](https://docs.cloud.google.com/looker/docs/best-practices/how-to-change-the-looker-instance-url) can be configured by request to align your instance domain with the embedding application's base domain.

### Troubleshooting signed embedding

If you're experiencing issues with signed embedding, see the following troubleshooting pages:

  * If you don't see the Looker UI or see only the login page, consult [Troubleshooting signed embed authentication errors](https://docs.cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-signed-embed-authentication-errors).
  * If you see the Looker UI but are encountering 404s, permissions, or content access issues, consult [Troubleshooting signed embed 404s, permissions, and content access](https://docs.cloud.google.com/looker/docs/best-practices/how-to-troubleshoot-signed-embed-404s-permissions-content-access).



## Final review and support

If the embedded iframe is still failing to load, review the troubleshooting steps on this page. If you still need help, gather the following information before you [contact Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details):

  * A [HAR file](https://support.zendesk.com/hc/en-us/articles/4408828867098-Generating-a-HAR-file-for-troubleshooting) from a network capture taken while reproducing the embed issue
  * The type of embedding being used: [Public](https://docs.cloud.google.com/looker/docs/publishing-looks-with-public-urls), [Private](https://docs.cloud.google.com/looker/docs/private-embedding), or [Signed](https://docs.cloud.google.com/looker/docs/signed-embedding)
  * When the issue started occurring



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
