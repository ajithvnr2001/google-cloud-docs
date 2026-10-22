---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/define-alert-overflow-admin/
title: Configure alert overflow \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:21:50.709998+00:00
---

# Configure alert overflow  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-alerts/define-alert-overflow-admin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Configure alert overflow

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document is for administrators configuring the alert overflow mechanism to manage alerts and maintain system performance. The alert overflow mechanism is designed to prevent system overflow and improve noise reduction when large volumes of alerts from the same environment, product, and rule occur in a short period of time. This mechanism helps avoid repetitive attacks, such as brute force or DDoS, from flooding the platform and database, while making sure that the SOC continues to function as planned. 

The alert grouping mechanism intelligently groups alerts into cases based on mutual entities and time proximity, letting analysts perform a contextual analysis of multiple alerts in one case.  
In these cases, you'll see multiple alerts in one case, and mutual entities marked in the entities list and the **Explorer** page. 

## Overflow configuration

There are two distinct configurations for the overflow mechanism:

  * **Initial overflow configuration** : This configuration is hard-coded in the database and defines the trigger conditions. The mechanism activates when more than 50 similar alerts are ingested within a 10-minute timeframe. This is determined by the `Is_Overflow` method, which is configured on the connector side (added to the connector code in the Integrated Development Environment (IDE)). Once triggered, the system adds an overflow case to the case queue. This case contains one alert indicating the environment, product, and rule of the overflowing alert, along with an overflow tag. 
  * **Second overflow configuration** : This configuration defines the system's behavior _after_ the overflow mechanism is triggered. You can define this in **SOAR Settings > Advanced > Alerts Grouping** in the **Overflow** section.
    * **Timeframe for Overflow Case grouping (in hours):** Choose the number of hours in which to group the overflow alerts for the case. This is only applied to rules grouped solely by entities. 
    * **Max. alerts grouped into an Overflow Case:** Define the maximum number of overflow alerts to group together into one case.  
  
For example, if 50 phishing alerts are ingested within 8 minutes, the 51st alert triggers the overflow mechanism, and an overflow case is created. Over the next three hours another 119 phishing alerts are ingested, resulting in four overflow cases, each containing 30 alerts. Once the three hours expire, the system returns to the default configuration.

To optimize performance, the system intentionally bypasses entity extraction for overflow cases. Consequently, objects such as timestamps, IPs, hashes, or domains are not mapped during these events. 

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
