---
url: https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview/
title: Google SecOps APIs and libraries overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:54.501495+00:00
---

# Google SecOps APIs and libraries overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Google SecOps APIs and libraries overview

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Caution:** The Backstory API and Ingestion API are [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) and will be discontinued on July 20, 2027. Use the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest) instead. For details on how to migrate, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api).

This page provides an overview of the APIs available for Google Security Operations. While you can use the APIs directly by making raw requests to the server, client libraries let you code in your preferred language and provide simplifications that significantly reduce the amount of code you need to write. For a more general overview of client libraries within Google Cloud, see [Client libraries explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

To use the APIs, you must authenticate your client's identity. You can learn more about per API authentication in the respective API documentation.

## Chronicle API

The Chronicle API is the new-generation, unified API for Google SecOps. You can use it to programmatically manage the product suite, including UDM search, detection rules, and incident response workflows. Built on Google's [API Improvement Proposals](http://aip.dev/) (AIP) standards, it provides a consistent, resource-oriented design that simplifies integration and accelerates development with idiomatic client libraries. This modern foundation empowers security teams to build robust automation and extend their capabilities using a single, cohesive standard across the platform.

For more information about this API and its usage, see [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest?rep_location=africa-south1).

## Backstory API

The Backstory API is the previous-generation API for Google SecOps SOAR workflows. It includes the Feed Management, Detection Engine, Search, Forwarder Management, Data Export and Customer Management APIs. You can authenticate to this API through a Google Developer Service Account Credential. Your Google SecOps representative provides the service account and the credentials (JSON key) to let the API client communicate with the API.

Google SecOps recommends using the newer generation Chronicle API for a more robust, secure, and extensible experience.

For steps to migrate from the Backstory API to the Chronicle API, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api) and [SIEM API endpoint mapping](https://docs.cloud.google.com/chronicle/docs/administration/siem-endpoint-mapping-table).

For more information about this API and its usage, see [Backstory API](https://docs.cloud.google.com/chronicle/docs/reference/detection-engine-api).

**Note:** To access Backstory API endpoints, you must use a service account from a **Google-managed** Google Cloud project.  
If you attempt to use Backstory API endpoints with a service account from your own Google Cloud project, the system returns the following error: 

> Backstory API has not been used in project {your_project_id} before or it is disabled. Enable it by visiting `https://console.developers.google.com/apis/api/backstory.googleapis.com/overview?project={your_project_id}` then retry.   
> If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry.

There are two options to resolve this: 

  1. Use the [legacy Backstory API](https://docs.cloud.google.com/chronicle/docs/reference/detection-engine-api) using a service account which is linked to your **Google-managed Google Cloud project**.
  2. Use the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest) with a service account from your own [**Google Cloud project linked to your Google SecOps instance**](https://docs.cloud.google.com/chronicle/docs/onboard/configure-cloud-project).



## Ingestion API

The Ingestion API provides a high-volume interface designed for sending unstructured logs and telemetry data to Google SecOps. You can authenticate to this API through a Google Developer Service Account Credential. Your Google SecOps representative provides the service account and the credentials (JSON key) to let the API client communicate with the API.

Google SecOps recommends using the newer generation Chronicle API because it improves and expands on the functionality offered by Ingestion API.

For steps to migrate from the Ingestion API to the Chronicle API, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api) and [SIEM API endpoint mapping](https://docs.cloud.google.com/chronicle/docs/administration/siem-endpoint-mapping-table).

For more information about this API and its usage, see [Ingestion API](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-api).

## SOAR API

The SOAR API is a legacy API originally designed for SOAR modules in Google SecOps.

Google SecOps recommends using the unified Chronicle API for the modern platform, case management and response workflows that provide a secure, compliant and extensible experience. Chronicle API also enables various services, including IAM for access control, Cloud Monitoring, and Cloud Audit Logs.

For more information about this API, see [SOAR API](https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/tipcommon). You can switch to Chronicle API as part of stage 2 of [SOAR migration to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
