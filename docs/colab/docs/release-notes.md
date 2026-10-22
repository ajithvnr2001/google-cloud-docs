---
url: https://docs.cloud.google.com/colab/docs/release-notes/
title: Colab Enterprise release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:43:05.979613+00:00
---

# Colab Enterprise release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/colab/docs/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Colab Enterprise ](https://docs.cloud.google.com/colab/docs)
  * [ Resources ](https://docs.cloud.google.com/colab/docs/release-notes)



Send feedback 

#  Colab Enterprise release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Colab Enterprise. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. Colab Enterprise is a component of Gemini Enterprise Agent Platform. For information on all Agent Platform releases, see the [Agent Platform release notes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/release-notes). 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/colabenterprise-release-notes.xml) directly. 

## July 13, 2026

Security

A Missing Authorization vulnerability was discovered in repositories in BigQuery, Dataform, and Colab Enterprise. An authenticated attacker could potentially escalate permissions and perform cross-tenant repository takeover. For more information, see the [GCP-2026-047](https://docs.cloud.google.com/support/bulletins#gcp-2026-047) security bulletin.

## May 26, 2026

Feature

**Data Science Agent**

[Generally available](https://cloud.google.com/products#product-launch-stages): Use the Data Science Agent to automate exploratory data analysis, perform machine learning tasks, and deliver insights from within a Colab Enterprise notebook. To get started, see [Use the Data Science Agent](https://docs.cloud.google.com/colab/docs/use-data-science-agent).

## April 13, 2026

Feature

**Visualization cells**

[Generally available](https://cloud.google.com/products#product-launch-stages): You can use visualization cells to generate interactive and editable visualizations from within a Colab Enterprise notebook. You can configure the chart type, aggregation, colors, labels, and other aspects of the visualization to help you explore data and discover insights. For more information, see [Use visualization cells](https://docs.cloud.google.com/colab/docs/visualization-cells).

## April 10, 2026

Feature

**SQL cells**

[Generally available](https://cloud.google.com/products#product-launch-stages): You can use SQL cells to write, edit, and run SQL queries directly from your Colab Enterprise notebooks. For more information, see [Use SQL cells](https://docs.cloud.google.com/colab/docs/sql-cells).

## January 21, 2026

Feature

**BigFrames, BigQuery ML, and Managed Service for Apache Spark**

The Data Science Agent supports BigFrames, BigQuery ML, and Managed Service for Apache Spark. Previously, these capabilities were supported only when using Colab Enterprise notebooks in BigQuery.

## December 17, 2025

Feature

**Post-startup scripts**

[Generally available (GA)](https://cloud.google.com/products#product-launch-stages): You can use a post-startup script to perform tasks after the startup process of your Colab Enterprise runtime. For example, you can use a post-startup script to install specific packages or make specific changes to your runtime's VM. For more information, see [Use a post-startup script](https://docs.cloud.google.com/colab/docs/post-startup-script).

## November 10, 2025

Feature

The default latest Python version is now 3.12. See [Python versions](https://docs.cloud.google.com/colab/docs/runtimes#python).

## October 20, 2025

Feature

**Visualization cells**

[Preview](https://cloud.google.com/products#product-launch-stages): You can use visualization cells to generate interactive and editable visualizations from within a Colab Enterprise notebook. You can configure the chart type, aggregation, colors, labels, and other aspects of the visualization to help you explore data and discover insights. For more information, see [Use visualization cells](https://docs.cloud.google.com/colab/docs/visualization-cells).

## October 14, 2025

Feature

**SQL cells**

[Preview](https://cloud.google.com/products#product-launch-stages): You can use SQL cells to write, edit, and run SQL queries directly from your Colab Enterprise notebooks. For more information, see [Use SQL cells](https://docs.cloud.google.com/colab/docs/sql-cells).

## October 07, 2025

Feature

**Post-startup scripts**

[Preview](https://cloud.google.com/products#product-launch-stages): You can use a post-startup script to perform tasks after the startup process of your Colab Enterprise runtime. For example, you can use a post-startup script to install specific packages or make specific changes to your runtime's VM. For more information, see [Use a post-startup script](https://docs.cloud.google.com/colab/docs/post-startup-script).

## August 05, 2025

Feature

[Generally available](https://cloud.google.com/products#product-launch-stages): You can consume reservations with Colab Enterprise runtimes. Reservations of Compute Engine zonal resources help you gain a high level of assurance that your runtimes have the necessary resources to run. For more information, see [Use reservations with Colab Enterprise](https://docs.cloud.google.com/colab/docs/reservations).

## August 04, 2025

Feature

You can now use the new Data Science Agent to automate exploratory data analysis, perform machine learning tasks, and deliver insights from within a Colab Enterprise notebook. To get started, see [Use the Data Science Agent](https://docs.cloud.google.com/colab/docs/use-data-science-agent). This feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## June 30, 2025

Feature

[Preview](https://cloud.google.com/products#product-launch-stages): You can consume reservations with Colab Enterprise runtimes. Reservations of Compute Engine zonal resources help you gain a high level of assurance that your runtimes have the necessary resources to run. For more information, see [Use reservations with Colab Enterprise](https://docs.cloud.google.com/colab/docs/reservations).

## May 28, 2025

Feature

Python 3.11 is now available in Colab Enterprise. Existing runtimes and runtime templates will remain using Python 3.10. For more information, see [Python versions](https://docs.cloud.google.com/colab/docs/runtimes#python).

Feature

When you create a runtime template, you can now configure it to use the latest Python version available to Colab Enterprise, or you can specify the Python version. Using `Latest` is a new option that means when a new version of Python is introduced to Colab Enterprise, runtimes that you create will use the latest Python version.

Existing runtime templates and runtimes remain using their current Python version (Python 3.10). This includes existing auto-generated default runtime templates. To create default runtime templates that use `Latest`, you must do one of the following:

  * Delete the existing default runtime templates. Then, when a new default runtime template is created, the Python version will be set to Latest.
  * [Change a runtime template's Python version](https://docs.cloud.google.com/colab/docs/runtimes#change-python-version) by using the REST API.



## April 29, 2025

Feature

Gemini in Colab Enterprise, which is a product in the Gemini for Google Cloud portfolio, now includes additional capabilities in [Preview](https://cloud.google.com/products/#product-launch-stages). See the following:

  * [Chat about your notebook with Gemini](https://docs.cloud.google.com/colab/docs/chat)
  * [Explain code cells with Gemini assistance](https://docs.cloud.google.com/colab/docs/explain-cells)
  * [Explain and fix errors with Gemini assistance](https://docs.cloud.google.com/colab/docs/explain-errors)



To enable and activate Gemini in Colab Enterprise features, see [Set up Gemini in Colab Enterprise](https://docs.cloud.google.com/gemini/docs/colab/set-up-gemini).

## April 21, 2025

Feature

**The notebook gallery is now available.**

The notebook gallery is a curated collection of notebooks to help you get started using Colab Enterprise. This collection consists of ready-to-use templates and examples to make it easier to learn new techniques, understand best practices, and get projects started quickly. Browse the notebooks by category or use the search bar to find a notebook that helps you get started. See the [notebook gallery](https://console.cloud.google.com/vertex-ai/colab/notebook-gallery).

## March 31, 2025

Feature

[Preview](https://cloud.google.com/products#product-launch-stages): You can switch to a default runtime with GPUs by using a button in your Colab Enterprise notebook. To enable a default runtime with GPUs for your users, see [Enable default runtimes with GPUs](https://docs.cloud.google.com/colab/docs/default-runtimes-with-gpus).

## February 27, 2025

Feature

You can use Terraform resources to schedule notebook runs, and to manage runtimes and runtime templates. To learn more, see the following:

  * [Schedule a notebook run](https://docs.cloud.google.com/colab/docs/schedule-notebook-run#run_notebook_once-terraform)
  * [Create a runtime](https://docs.cloud.google.com/colab/docs/create-runtime#colab-create-runtime-terraform)
  * [Create a runtime template](https://docs.cloud.google.com/colab/docs/create-runtime-template#colab-create-runtime-template-terraform)



## December 10, 2024

Feature

Gemini in Colab Enterprise, which is a product in the Gemini for Google Cloud portfolio, now includes error fixing in [Preview](https://cloud.google.com/products/#product-launch-stages). Gemini in Colab Enterprise can suggest fixes when your code produces errors. For more information, see [Fix errors](https://docs.cloud.google.com/colab/docs/use-code-completion#fix-errors).

To enable and activate Gemini in Colab Enterprise features, see [Set up Gemini in Colab Enterprise](https://docs.cloud.google.com/gemini/docs/colab/set-up-gemini).

## October 25, 2024

Feature

Colab Enterprise is now available in the following regions:

  * Hamina, Finland (`europe-north1`)
  * Milan, Italy (`europe-west8`)
  * Tel Aviv, Israel (`me-west1`)
  * Warsaw, Poland (`europe-central2`)



See [Colab Enterprise locations](https://docs.cloud.google.com/colab/docs/locations).

## October 03, 2024

Feature

Gemini in Colab Enterprise, which is a product in the Gemini for Google Cloud portfolio, is [generally available](https://cloud.google.com/products/#product-launch-stages). Gemini in Colab Enterprise helps you write code by suggesting code as you type. You can also use the Help me code tool to generate code from a description of what you want.

Gemini in Colab Enterprise is available to try at no cost through December 31, 2024.

To learn how to enable and activate Gemini in Colab Enterprise features, see [Set up Gemini in Colab Enterprise](https://docs.cloud.google.com/gemini/docs/colab/set-up-gemini).

## September 23, 2024

Feature

You can now use customer-managed encryption keys (CMEK) to protect notebooks in Colab Enterprise.

For more information, see [Use customer-managed encryption keys](https://docs.cloud.google.com/colab/docs/cmek).

## August 14, 2024

Feature

The notebook scheduler is now [generally available](https://cloud.google.com/products/#product-launch-stages). See [Schedule a notebook run](https://docs.cloud.google.com/colab/docs/schedule-notebook-run).

## August 05, 2024

Fixed

Fixed an issue in which users weren't able to access the Colab Enterprise UI when Colab Service Status was **OFF for everyone** in Google Workspace.

## July 16, 2024

Change

All Colab Enterprise runtimes are automatically configured with a 100 GiB boot disk in addition to the disk specified in the runtime template. Starting July 16, 2024, the boot disk of a newly created Colab Enterprise runtime automatically defaults to an SSD Persistent Disk. Previously, the boot disk default was a Standard Persistent Disk. 

Because of this change, default boot disks of Colab Enterprise runtimes are billed as SSD Persistent Disks instead of Standard Persistent Disks. For more information, see [Colab Enterprise pricing](https://cloud.google.com/colab/pricing).

## June 17, 2024

Feature

You can now use customer-managed encryption keys (CMEK) to protect runtimes in Colab Enterprise. Using CMEK for notebook files isn't currently supported.

For more information, see [Use customer-managed encryption keys for runtimes](https://docs.cloud.google.com/colab/docs/cmek).

## June 10, 2024

Feature

Gemini in Colab Enterprise, which is a product in the Gemini for Google Cloud portfolio, is available in [Preview](https://cloud.google.com/products/#product-launch-stages). Gemini in Colab Enterprise helps you write code by suggesting code as you type. You can also use the **Help me code** tool to generate code from a description of what you want.

To learn how to enable and activate Gemini in Colab Enterprise features, see [Set up Gemini in Colab Enterprise](https://docs.cloud.google.com/gemini/docs/colab/set-up-gemini).

Feature

The notebook scheduler is now available in [Preview](https://cloud.google.com/products/#product-launch-stages). You can schedule a notebook to run immediately one time, or on a recurring schedule.

For more information, see [Schedule a notebook run](https://docs.cloud.google.com/colab/docs/schedule-notebook-run).

## February 27, 2024

Feature

VPC Service Controls has [general availability](https://cloud.google.com/products#product-launch-stages) support in Colab Enterprise.

For more information, see [Use VPC Service Controls](https://docs.cloud.google.com/colab/docs/service-controls).

## October 11, 2023

Feature

Colab Enterprise is now generally available ([GA](https://cloud.google.com/products/#product-launch-stages)). Colab Enterprise combines the popular collaborative features of Colaboratory with the security and compliance capabilities of Google Cloud. Colab Enterprise includes:

  * Sharing and collaborating functionality, with IAM access control.
  * Google-managed compute and runtime provisioning, with configurable [runtime templates](https://docs.cloud.google.com/colab/docs/create-runtime-template).
  * Integrations with Vertex AI and [BigQuery](https://docs.cloud.google.com/bigquery/docs/explore-data-colab).
  * Inline code completion with [Duet AI](https://docs.cloud.google.com/duet-ai/docs/overview) ([Preview](https://cloud.google.com/products/#product-launch-stages)) assistance.
  * End-user credential authentication for running your notebook code.
  * [Idle shutdown](https://docs.cloud.google.com/colab/docs/idle-shutdown) for runtimes ([Experimental](https://cloud.google.com/products/#product-launch-stages)).



To get started, see [Introduction to Colab Enterprise](https://docs.cloud.google.com/colab/docs/introduction) or [create a notebook](https://docs.cloud.google.com/colab/docs/create-console-quickstart) and start coding.

## August 29, 2023

Feature

Colab Enterprise is now available in [Preview](https://cloud.google.com/products/#product-launch-stages). Colab Enterprise combines the popular collaborative features of Colaboratory with the security and compliance capabilities of Google Cloud. Colab Enterprise includes:

  * Sharing and collaborating functionality, with IAM access control.
  * Google-managed compute and runtime provisioning, with configurable runtime templates.
  * Integrations with Vertex AI and BigQuery.
  * Inline code completion with [Duet AI](https://docs.cloud.google.com/duet-ai/docs/overview) assistance.
  * End-user credential authentication for running your notebook code.



To get started, see [Introduction to Colab Enterprise](https://docs.cloud.google.com/colab/docs/introduction) or [create a notebook](https://docs.cloud.google.com/colab/docs/create-console-quickstart) and start coding.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
