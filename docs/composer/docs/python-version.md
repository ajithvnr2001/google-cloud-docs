---
url: https://docs.cloud.google.com/composer/docs/python-version/
title: Supported Python versions \u00a0|\u00a0 Managed Service for Apache Airflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:27:36.623618+00:00
---

# Supported Python versions  |  Managed Service for Apache Airflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/composer/docs/python-version/

To more strongly embrace the success and growing customer preference for OSS solutions, Cloud Composer is evolving to become **Managed Service for Apache Airflow**. This name change provides improved customer understanding of our portfolio while reinforcing our commitment to being the most open cloud ecosystem. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Managed Service for Apache Airflow ](https://docs.cloud.google.com/composer/docs)
  * [ Resources ](https://docs.cloud.google.com/composer/docs/resources)



Send feedback 

#  Supported Python versions Stay organized with collections  Save and categorize content based on your preferences. 

Managed Airflow supports Python 3.

To see the `major.minor.patch` versions of Python 3 used in a specific Managed Airflow image, see [Managed Airflow version list](https://docs.cloud.google.com/composer/docs/composer-versions).

After an environment is created, you cannot switch an existing environment to a different minor Python version.

## Python 2 support in Managed Airflow (Legacy Gen 1)

Support for Python 2 was deprecated in Managed Airflow version 1.19.0:

  * Starting from version 1.19.0, it is not possible to create new environments with Python 2, or upgrade existing environments with Python 2 to 1.19.0 and later versions of Cloud Composer.

  * Starting from version 1.19.6, it is no longer possible to use any operators that call Python 2. In particular, `PythonVirtualenvOperator` can no longer create virtual environments with Python 2.

  * Existing environments with Python 2 are not impacted by this change. It is possible to upgrade such environments to Cloud Composer version 1.18.12 and earlier through gcloud CLI, API, and Terraform.

  * New Airflow operators, sensors, and hooks are only developed for Python 3, which may cause connectivity options to be outdated for Python 2 environments. As such, we highly recommend migrating your DAGs to a Python 3 environment, and creating all new environments with Python 3.


**Note:** If you want to continue using Python 2, note that samples located in [python-docs-samples](https://github.com/GoogleCloudPlatform/python-docs-samples) are no longer checked for compatibility with Python 2.7.

## What's next

  * [Creating environments](https://docs.cloud.google.com/composer/docs/composer-2/create-environments)
  * [Managed Airflow version list](https://docs.cloud.google.com/composer/docs/composer-versions)
  * [Release Notes](https://docs.cloud.google.com/composer/docs/release-notes)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
