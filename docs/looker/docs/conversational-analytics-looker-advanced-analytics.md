---
url: https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics/
title: Enable and use Advanced Analytics \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:29.014588+00:00
---

# Enable and use Advanced Analytics  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Enable and use Advanced Analytics Stay organized with collections  Save and categorize content based on your preferences. 

Advanced Analytics in [Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview) translates your natural language questions into Python code and executes that code to provide advanced analysis and visualizations. Advanced Analytics is available for Conversational Analytics data agents in both Looker (original) and Looker (Google Cloud core) instances.

In contrast to standard SQL-powered BI experiences, Advanced Analytics supports a wide variety of data analytics—from basic computations and charting to more advanced tasks like time series forecasting. Advanced Analytics enhances Conversational Analytics by enabling users to perform these types of advanced analysis, which otherwise would typically require specialized knowledge of advanced coding or statistical methods.

This page describes how to enable Advanced Analytics for a Looker instance and how to use Advanced Analytics with a Conversational Analytics data agent.

**Warning:** The Python code that data agents return is designed to execute within a secure, Google-managed sandbox. Executing this code in a local or other unverified environment bypasses the sandbox's security protections and can expose your system to security risks, such as the execution of malicious code. For guidance on how to safely inspect and handle agent-generated Python code, see [How can I safely inspect and handle agent-generated Python code?](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/frequently-asked-questions#safe-python)

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Before you begin

To use Advanced Analytics, you must meet the requirements for using Conversational Analytics in [Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup#setup-and-requirements), including permissions to create and use data agents.

## Enable Advanced Analytics

This section describes how to enable Advanced Analytics in the following platforms:

  * Looker (original)
  * Looker (Google Cloud core)




###  Looker (original) 

### Enable Advanced Analytics in Looker (original)

In the Looker (original) instance, a Looker admin must follow these steps to enable Advanced Analytics and make it available to Conversational Analytics users:

  1. In the **Admin** panel, navigate to the **Platform** section and select the **Gemini in Looker** page.
  2. Under **Gemini in Looker enablement** , turn on the **Enable Gemini in Looker** setting.
  3. Under **Conversational Analytics** , turn on the **Conversational Analytics (Conversations page)** setting (for Explores) or the **Dashboard agents** setting (for dashboards), or both.
  4. Under **Additional options** , turn on the **Advanced Analytics** setting. When this setting is enabled, data agent creators can choose to enable Advanced Analytics for all conversations with their data agents.



###  Looker (Google Cloud core) 

### Enable Advanced Analytics in Looker (Google Cloud core)

In the Looker (Google Cloud core) instance, a Looker admin must follow these steps to enable Advanced Analytics and make it available to Conversational Analytics users:

  1. In the **Admin** panel, navigate to the **Platform** section and select the **Gemini in Looker** page.
  2. Under **Gemini in Looker enablement** , make sure that the **Gemini Enablement status** is **On**. If it isn't on, [enable Gemini in Looker](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini#enable-and-disable-gil-core) for this instance in the Google Cloud console, and then return to the **Gemini in Looker** admin page in the Looker (Google Cloud core) instance.
  3. Under **Conversational Analytics** , turn on the **Conversational Analytics (Conversations page)** setting (for Explores) or the **Dashboard agents** setting (for dashboards), or both.
  4. Under **Additional options** , turn on the **Advanced Analytics** setting. When this setting is enabled, data agent creators can choose to enable Advanced Analytics for all conversations with their data agents.



Advanced Analytics is disabled by default, even when **Gemini in Looker** is enabled in the Looker (Google Cloud core) instance settings in the Google Cloud console.

A Looker admin must [grant additional permissions](https://docs.cloud.google.com/looker/docs/looker-core-admin-gemini#grant-permissions-gil) to users before they can use Advanced Analytics.

## Use Advanced Analytics with a Conversational Analytics data agent

When Advanced Analytics is enabled for a given data agent, enhanced analytics capabilities are available for all conversations with that agent.

You can enable Advanced Analytics for a data agent when you are [creating or editing it](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents#create-and-edit-data-agents). Enable Advanced Analytics by turning on the **Enable Advanced Analytics** option.

## Known limitations

  * Advanced Analytics uses Python to solve problems. Since Python is more flexible than structured query languages, Advanced Analytics responses might have more variability than responses from the core Conversational Analytics experience.
  * Advanced Analytics supports only these Python libraries.
  * Map visualization chart types are not supported in Advanced Analytics responses.
  * Advanced Analytics isn't available in [a direct chat with an Explore](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data).



For information about additional limitations, see the documentation on [known limitations in Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview#known-limitations).

## Supported Python libraries

#### Show supported Python libraries

Advanced Analytics supports the following Python libraries:

  * `altair`
  * `attrs`
  * `chess`
  * `contourpy`
  * `cycler`
  * `entrypoints`
  * `fonttools`
  * `fpdf`
  * `geopandas`
  * `imageio`
  * `jinja2`
  * `joblib`
  * `jsonschema`
  * `jsonschema-specifications`
  * `kiwisolver`
  * `lxml`
  * `markupsafe`
  * `matplotlib`
  * `mpmath`
  * `numexpr`
  * `numpy`
  * `opencv-python`
  * `openpyxl`
  * `packaging`
  * `pandas`
  * `patsy`
  * `pdfminer-six`
  * `pillow`
  * `plotly`
  * `protobuf`
  * `pylatex`
  * `pyparsing`
  * `PyPDF2`
  * `python-dateutil`
  * `python-docx`
  * `python-pptx`
  * `pytz`
  * `referencing`
  * `reportlab`
  * `rpds-py`
  * `scikit-image`
  * `scikit-learn`
  * `scipy`
  * `seaborn`
  * `six`
  * `statsmodels`
  * `striprtf`
  * `sympy`
  * `tabulate`
  * `tensorflow`
  * `threadpoolctl`
  * `toolz`
  * `torch`
  * `tzdata`
  * `xlrd`



## Suggested questions

When you enable Advanced Analytics, Python's advanced analytic capabilities enable Conversational Analytics data agents to answer a wider range of questions, in addition to [the standard types of supported questions](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview#limitations-on-questions). For example:

  * Can you explain the key drivers for sales based on my data?
  * What is the lifetime value for each of my customer segments, taking into account the average purchase frequency and the average order value?
  * How do sales this year compare to sales last year?
  * Identify outliers in my sales data to help identify products or regions that are performing particularly well or particularly poorly.
  * Perform a cohort analysis to understand customer retention.
  * Are my highest margin products also the most popular products? Use this answer to provide a suggestion on how to optimize my product mix.
  * What is the compound annual growth rate (CAGR) for sales by product category for the last 3 years?
  * Show the CAGR as a bar chart with product category on the x-axis and CAGR on the y-axis.



## Related resources

  * [Conversational Analytics overview](https://docs.cloud.google.com/looker/data/conversational-analytics-overview)
  * [Converse with Looker data](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
