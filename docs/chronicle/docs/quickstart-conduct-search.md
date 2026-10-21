---
url: https://docs.cloud.google.com/chronicle/docs/quickstart-conduct-search/
title: Quickstart: Review potential security issues \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:24:11.288269+00:00
---

# Quickstart: Review potential security issues  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/quickstart-conduct-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Review potential security issues 

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This document describes how to conduct searches when investigating alerts and potential security issues using Google Security Operations.

## Before you begin

Google Security Operations supports the Google Chrome and Mozilla Firefox browsers. Upgrade your browser to the most current version for optimal performance and security. The latest Chrome version is available for download at <https://www.google.com/chrome/>. Mobile operating systems (iOS/Android) and mobile browsers are not supported.

**Note:** You can access multiple Google SecOps instances within the same browser profile as long as you log in using the same user identity (the same Cloud Identity account or the same workforce identity pool). However, your active session is invalidated if you switch user accounts or access an instance configured with different workforce pool or different Google Cloud organization. To maintain concurrent sessions across different identities or authentication setups, use a separate browser profile or an incognito/private window for each session.

## Authentication and access

Google SecOps integrates with SSO solutions. Access to the Google SecOps platform requires valid enterprise credentials.

  1. Launch Chrome or Firefox.

  2. Verify you have active access to the corporate account.

  3. Go to the following URL and replace customer_subdomain with the customer-specific identifier to access the Google SecOps application:

`https://customer_subdomain.backstory.chronicle.security`




## Viewing Alerts and IOC Matches

  1. In the navigation bar, select **Detections > Alerts and IOCs**.

  2. Click the **IOC Matches** tab.




## Searching for IOC matches in **Domain** view

The **Domain** column in the **IOC Domain Matches** tab contains a list of suspect domains. Clicking on a domain in this column opens **Domain** view, as shown in the following figure, providing detailed information about this domain.

![Domain View](https://docs.cloud.google.com/chronicle/images/qs/qs-search-domain-view.png)**Domain** view

## Using the Google Security Operations Search field

Initiate a search directly from the Google Security Operations home page, as shown in the following figure.

![Search Field](https://docs.cloud.google.com/chronicle/images/qs/qs-search-search-field.png) Google Security Operations **Search** field

On this page, you can enter the following search terms: 

  * Hostname displays **Domain** view

| (for example, plato.example.com)  
---|---  
  
  * Domain displays **Domain** view

| (for example, altostrat.com)  
  
  * IP address displays **IP Address** view

| (for example, 192.168.254.15)  
  
  * URL displays **Domain** view

| (for example, https://new.altostrat.com)  
  
  * Username displays **Asset** view

| (for example, betty-decaro-pc)  
  
  * File hash displays **Hash** view

| (for example, e0d123e5f316bef78bfdf5a888837577)  
  
You do not have to specify which type of search term you are entering, Google Security Operations determines it for you. The results are shown in the appropriate investigative view. For example, typing a username in the search field displays **Asset** view.

## Searching raw logs

You have the option of searching the indexed database or searching raw logs. Searching raw logs is a more comprehensive search, but takes longer than an indexed search.

To further pinpoint your search, you can use regular expressions, make the search entry case sensitive, or select log sources. You can also select the timeline you want using the **Start** and **End** time fields.

To conduct a raw log search, complete the following steps:

  1. Type in your search term, and then select **Raw Log Scan** in the dropdown menu, as shown in the following figure.

![Raw Log Scan menu](https://docs.cloud.google.com/chronicle/images/qs/qs-search-raw-log-scan-menu.png) Dropdown menu showing **Raw Log Scan** option

  2. After setting your raw search criteria, click the **Search** button.

  3. From **Raw Log Scan** view, you can further analyze your log data.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
