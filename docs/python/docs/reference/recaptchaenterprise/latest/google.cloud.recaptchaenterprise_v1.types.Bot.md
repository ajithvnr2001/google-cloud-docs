---
url: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Bot
title: Class Bot (1.34.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:54.234775+00:00
---

# Class Bot (1.34.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Bot

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Bot (1.34.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.34.0 (latest)  1.33.0  1.32.0  1.29.0  1.28.2  1.27.0  1.26.1  1.25.0  1.24.1  1.23.0  1.22.0  1.21.2  1.20.0  1.19.1  1.18.1  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.1  1.10.0  1.9.0  1.8.3  1.7.1  1.6.1  1.5.0  1.4.1  1.3.1  1.2.0  1.1.2  1.0.0  0.4.2  0.3.3  0.2.1  0.1.0 
    
    
    Bot(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Bot information and metadata.

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Optional. Enumerated string value that indicates the identity of the bot, formatted in kebab-case. Current example values include the following: \- google-agent - AI_AGENT \- browser-base - AI_AGENT \- chat-gpt - AI_AGENT \- aws-bedrock - AI_AGENT \- cybaa-bot - AI_AGENT \- cloudflare - AI_AGENT \- payhawk - AI_AGENT \- duck-duck-go - SEARCH_INDEXER \- mediaboard - CONTENT_SCRAPER \- marker-io - AI_AGENT \- broadcom - AI_AGENT \- anchor-browser - AI_AGENT \- shopify - AI_AGENT \- stackscope - CONTENT_SCRAPER \- manus - AI_AGENT \- kernel-sh - AI_AGENT \- zvelo - SEARCH_INDEXER Ensure that your applications can handle identifier values not explicitly listed here. Deprecated values might take some time to stop showing up in responses. New values can be pushed so this list should be taken as non exhaustive.   
`bot_type` |  `[google.cloud.recaptchaenterprise_v1.types.Bot.BotType](https://docs.cloud.google.com/python/docs/reference/recaptchaenterprise/latest/google.cloud.recaptchaenterprise_v1.types.Bot.BotType)`   
Optional. Enumerated field representing the type of bot.   
  
## Classes 

### BotType
    
    
    BotType(value)

Types of bots. Ensure that applications can handle values not explicitly listed.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
