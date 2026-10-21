---
url: https://docs.cloud.google.com/gemini/enterprise/docs/use-case-analyze-financial-statements/
title: Analyze financial statements and calculate ratios \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T22:58:32.556102+00:00
---

# Analyze financial statements and calculate ratios  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/use-case-analyze-financial-statements/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ App user guide ](https://docs.cloud.google.com/gemini/enterprise/docs/get-started)



Send feedback 

#  Analyze financial statements and calculate ratios Stay organized with collections  Save and categorize content based on your preferences. 

Analyze raw financial statements, calculate key performance indicators (KPIs), and generate an initial interpretation.

## Example prompt

In the chat box, enter a prompt such as the following:
    
    
    You are a senior financial analyst. Based on the following financial data for
    Cymbal Superstore for Q3 2025, perform the following tasks:
    
    1. Calculate the following financial ratios:
    
      * Gross Profit Margin
    
      * Operating Profit Margin
    
      * Net Profit Margin
    
      * Current Ratio
    
    2. Present the results in a table.
    
    3. In the table, include a column with a brief, one-sentence interpretation of
       each ratio.
    
    [Paste financial data here.]
    

## Example output

In response to this prompt, Gemini Enterprise produces output similar to the following:

> Ratio | Calculation | Result | Interpretation  
> ---|---|---|---  
> **Gross Profit Margin** | ($5M - $2M) / $5M | 60.0% | For every dollar of sales, the company keeps 60 cents after accounting for the direct costs of goods sold.  
> **Operating Profit Margin** | ($5M - $2M - $1.5M) / $5M | 30.0% | After paying for both direct production costs and core operational expenses, the company earns 30 cents per dollar of revenue.  
> **Net Profit Margin** | ($5M - $2M - $1.5M - $0.5M) / $5M | 20.0% | The company's final profitability is 20%, meaning it keeps 20 cents of profit for every dollar of revenue generated.  
> **Current Ratio** | $4M / $2M | 2.0x | The company has $2.00 of current assets available to cover every $1.00 of its short-term liabilities, indicating strong liquidity.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
