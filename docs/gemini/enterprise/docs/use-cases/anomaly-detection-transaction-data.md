---
url: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/anomaly-detection-transaction-data/
title: Detect anomalies in transaction data \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:36:53.749236+00:00
---

# Detect anomalies in transaction data  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/use-cases/anomaly-detection-transaction-data/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Detect anomalies in transaction data Stay organized with collections  Save and categorize content based on your preferences. 

Review monthly corporate credit card expense reports for unusual or non-compliant spending.

## Example prompt

In the chat box, enter a prompt such as the following:
    
    
    You are an internal auditor. Review the following list of employee expense
    transactions. Identify and list any items that meet the following criteria:
    
    * Are potential duplicates (same vendor and amount on consecutive days).
    
    * Occur on a weekend (Saturday or Sunday).
    
    * Are for an unusually high amount (over $1,000).
    
    For each flagged item, provide a brief reason for flagging it.
    

## Example output

In response to this prompt, Gemini Enterprise produces output similar to the following:

> The following transactions have been flagged for review based on your criteria:
> 
>   * **Transaction 1 (Charlie S., Cymbal Superstore, $1,250):**
>     * **Reason:** Flagged for high value (exceeds the $1,000 threshold).
>   * **Transactions 3 & 4 (Luka D., Cymbal Direct, $45):**
>     * **Reason:** Flagged as a potential duplicate transaction (same employee, vendor, and amount on the same day).
>   * **Transaction 5 (Tristan J., Cymbal Shops, $250):**
>     * **Reason:** Flagged for occurring on a weekend (Saturday), which may be outside of company policy for this vendor type.
> 


Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
