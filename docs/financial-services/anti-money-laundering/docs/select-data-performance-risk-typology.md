---
url: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/select-data-performance-risk-typology/
title: Select data for best performance and risk typology coverage \u00a0|\u00a0 Anti Money Laundering AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:10.114905+00:00
---

# Select data for best performance and risk typology coverage  |  Anti Money Laundering AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/select-data-performance-risk-typology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Anti Money Laundering AI ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs)
  * [ Guides ](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/concepts/overview)



Send feedback 

#  Select data for best performance and risk typology coverage Stay organized with collections  Save and categorize content based on your preferences. 

AML AI has MANDATORY fields which are essential for the detection of money laundering, such as transaction value and time. The product also has RECOMMENDED fields which are used to improve risk coverage, for fairness analysis, and to help manage data lineage.

To optimize coverage, you should provide RECOMMENDED fields because some of them enable additional features that are critical risk indicators for some typologies.

Data fields categorized as RECOMMENDED can improve risk typology coverage in two ways:

  * By supporting typologies that don't have any supporting features calculated from the MANDATORY data fields (for example, money laundering through high-risk jurisdictions)
  * By strengthening the coverage for an already supported typology with new features that yield additional results (for example, money muling)



The following table summarizes the purpose of all RECOMMENDED fields in the AML AI schema.

Field| Tables| Performance impact?| Typology coverage impact?| Other uses  
---|---|---|---|---  
`counterparty_account.region_code`| [Transaction](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#transaction)| Depends on engine version | Yes, multiple | N/A  
`nationalities`| [Party](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#party)| Yes | Yes, multiple | N/A  
`residencies`| [Party](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#party)| Yes | Yes, multiple | N/A  
`birth_date`| [Party](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#party) | Depends on engine version | Yes, multiple | Field can be used for your own fairness analysis.  
`establishment_date` | [Party](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#party) | Depends on engine version | Yes, multiple | No  
`gender` | [Party](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#party) | Depends on engine version | Yes, multiple | Field can be used for your own fairness analysis.  
`is_entity_deleted`| 

  * [Party](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#party)
  * [Transaction](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#transaction)
  * [PartySupplementaryData](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#partysupplementarydata)
  * [AccountPartyLink](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#accountpartylink)

| No| No| Field can be necessary to correctly model how entities change over time, depending on how you manage your data internally (see [Understanding how data changes over time](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#data-changes-over-time)).  
`source_system`| 

  * [Party](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#party)
  * [Transaction](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#transaction)
  * [PartySupplementaryData](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#partysupplementarydata)
  * [AccountPartyLink](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#accountpartylink)

| No| No| Field helps you to manage dataset quality.  
`risk_typology_measurements` | [RiskCaseEvent](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-input-data-model#riskcaseevent) | No| No| Enables typology-level recall measurement in [ObservedRecallValuesPerTypology](https://docs.cloud.google.com/financial-services/anti-money-laundering/docs/reference/schemas/aml-output-data-model#backtest-results) metric for supported engine versions.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
