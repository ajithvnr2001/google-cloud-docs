---
url: https://docs.cloud.google.com/data-studio/conversational-analytics-code-interpreter/
title: Enable and use the Code Interpreter \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:31.016624+00:00
---

# Enable and use the Code Interpreter  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/conversational-analytics-code-interpreter/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Enable and use the Code Interpreter Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Code Interpreter is a feature of [Conversational Analytics](https://docs.cloud.google.com/data-studio/conversational-analytics-overview) that translates natural language questions into Python code to provide advanced analysis and visualizations. In contrast to standard SQL-powered BI experiences, the Code Interpreter supports a wide variety of data analytics—from basic computations and charting to more advanced tasks like time series forecasting. The Code Interpreter enhances Conversational Analytics by enabling users to perform these types of advanced analysis, which otherwise would typically require specialized knowledge of advanced coding or statistical methods.

The Code Interpreter is available for Conversational Analytics as part of a Data Studio Pro subscription.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Before you begin

To use the Code Interpreter, you must meet the requirements for using Conversational Analytics in [Data Studio](https://docs.cloud.google.com/data-studio/conversational-analytics-setup#setup_and_requirements):

  * You must be a user under a Data Studio Pro subscription.
  * [Gemini in Data Studio and the **Code Interpreter** setting must be enabled](https://docs.cloud.google.com/data-studio/enable-and-disable-gemini-in-data-studio) for the Google Cloud project that is associated with your Data Studio Pro subscription.



### Enable the Code Interpreter for agents

To enable the Code Interpreter for all conversations and data agents, follow these steps:

  1. In the left navigation panel within Conversational Analytics, click the **Advanced analytics** toggle to enable the Code Interpreter.
  2. With the Code Interpreter enabled, you can use Conversational Analytics as usual to start conversations and ask questions of your data. The Code Interpreter uses [the engine that powers Gemini chat](https://support.google.com/gemini/answer/14903178) to translate your queries into Python code and execute that code.



## Known limitations

  * The Code Interpreter uses Python to solve problems. Since Python is more flexible than structured query languages, Code Interpreter responses might have more variability than responses from the core Conversational Analytics experience.
  * [For Looker data](https://docs.cloud.google.com/data-studio/conversational-analytics-data#converse-with-a-looker-data-source), Conversational Analytics can return a maximum of 5,000 rows per query.
  * The Code Interpreter supports only these Python libraries.
  * The following visualization chart types are not supported in Code Interpreter responses: 
    * Maps



> This feature is in Pre-GA. For support with errors, unexpected results, feedback, or to request support for additional Python libraries, send an email to [conversational-analytics-feedback@google.com](mailto:conversational-analytics-feedback@google.com).

For information about additional limitations, see the documentation on [known limitations in Conversational Analytics](https://docs.cloud.google.com/data-studio/conversational-analytics-data#known-limitations).

## Supported Python libraries

#### Show supported Python libraries

The Code Interpreter supports the following Python libraries:

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

When you enable the Code Interpreter, Python's advanced analytic capabilities enable Conversational Analytics to answer a wider range of questions, in addition to [the standard types of supported questions](https://docs.cloud.google.com/data-studio/conversational-analytics-data#limitations-on-questions). For example:

  * Can you explain the key drivers for sales based on my data?
  * What is the lifetime value for each of my customer segments, taking into account the average purchase frequency and the average order value?
  * How do sales this year compare to sales last year?
  * Identify outliers in my sales data to help identify products or regions that are performing particularly well or particularly poorly.
  * Perform a cohort analysis to understand customer retention.
  * Are my highest margin products also the most popular products? Use this answer to provide a suggestion on how to optimize my product mix.
  * What is the compound annual growth rate (CAGR) for sales by product category for the last 3 years?
  * Show the CAGR as a bar chart with product category on the x-axis and CAGR on the y-axis.



## Related resources

  * [Conversational Analytics overview](https://docs.cloud.google.com/data-studio/conversational-analytics-overview)
  * [Converse with Data Studio data](https://docs.cloud.google.com/data-studio/conversational-analytics-data)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
