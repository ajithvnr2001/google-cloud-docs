---
url: https://docs.cloud.google.com/looker/docs/best-practices/looker-internet-explorer-11-support/
title: Looker Internet Explorer 11 support \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:11:38.249912+00:00
---

# Looker Internet Explorer 11 support  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/best-practices/looker-internet-explorer-11-support/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Best Practices ](https://docs.cloud.google.com/looker/docs/best-practices/home)



Send feedback 

#  Looker Internet Explorer 11 support Stay organized with collections  Save and categorize content based on your preferences. 

Starting in Looker 22.16, Internet Explorer 11 (IE11) is no longer supported for use with Looker. If you prefer or are required to use a Microsoft browser, for the best experience with Looker we suggest that you use Microsoft Edge, which is supported at Level 1. 

Microsoft recently [announced](https://blogs.windows.com/windowsexperience/2018/12/06/microsoft-edge-making-the-web-better-through-more-open-source-collaboration/#2c3WQhyRU8UTGTbt.97) plans to make Edge broadly [available](https://www.microsoftedgeinsider.com/en-us/download/) across more versions of Windows beyond Windows 10, as well as adoption of the open source project Chromium. 

If you are currently using IE11, we recommend you switch to Edge or another [Level 1 supported browser](https://docs.cloud.google.com/looker/docs/supported-browsers). 

## Why is Looker changing this?

In 2015, [Microsoft released the Edge browser as a replacement for IE](https://www.microsoft.com/en-us/microsoft-365/windows/end-of-ie-support). As Internet Explorer no longer receives major updates, it misses the latest security patches and new functionality for complex web apps like Looker. 

Looker strives to deliver products that meet our customers' needs. The increasing gap between IE11 and all other browsers has caused a disproportionate amount of effort relative to the user base to avoid and fix defects specific to the browser. This limits our technology choices and dampens our ability to deliver the reliability and functionality our customers expect. 

IE11 can be considerably slower, sometimes up to 10 times slower, when compared to other modern browsers on the Looker platform. IE11 is also susceptible to memory leaks which may impact performance, especially in Windows 7. IE11 is considered a legacy browser and is not recommended from the perspective of performance. For example, see the [Internet Explorer 11 process leaks memory in Windows 7 (not the JS Heap)](https://support.servicenow.com/kb?id=kb_article_view&sysparm_article=KB0563748) ServiceNow article about memory leaks with iframes. 

## What do I need to do?

We recommend that you update your systems to ensure that your users are on a Level 1 supported browser. See the [Supported browsers](https://docs.cloud.google.com/looker/docs/supported-browsers) documentation page for a list of Looker supported browsers. 

## Workarounds (if you are unable to migrate)

To help alleviate IE11 memory leak issues, request end users to completely close and reopen their browsers after they have been in use for extended periods of time. 

In contexts where Looker content is [embedded](https://docs.cloud.google.com/looker/docs/private-embedding) using iframes, we recommend that if you are supporting IE 11 use that you design your application to reduce the memory footprint of client-side code and iframe usage. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-22 UTC."],[],[]] 
