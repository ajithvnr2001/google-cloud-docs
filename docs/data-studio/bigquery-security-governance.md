---
url: https://docs.cloud.google.com/data-studio/bigquery-security-governance/
title: Security, governance, and VPC Service Controls \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:45.296185+00:00
---

# Security, governance, and VPC Service Controls  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/bigquery-security-governance/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Security, governance, and VPC Service Controls Stay organized with collections  Save and categorize content based on your preferences. 

Protect your BigQuery data in Data Studio by using VPC Service Controls and service accounts. You can enforce IP-based access levels and configure dedicated credentials that support automated reporting.

## Support for VPC Service Controls

Data Studio can connect securely to BigQuery projects that are protected by **VPC Service Controls (`VPC-SC`)** perimeters. The connector passes the report viewer's end-user IP address to BigQuery, allowing Google Cloud to enforce any configured [viewer IP-based access levels](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels).

### Limits of VPC Service Controls

By default, automated background deliveries—such as scheduled email snapshots, threshold alerts, and scheduled data extracts—don't work with datasets that are protected solely by IP-based access levels. Because background tasks don't run from an end-user IP address, VPC Service Controls blocks the request.

To use automated reporting features behind VPC Service Controls perimeters, configure your data source connection to use [service account credentials](https://docs.cloud.google.com/data-studio/set-up-a-google-cloud-service-account) or create an access level that allows background requests.

Because Data Studio runs on Google-managed infrastructure with dynamic IP addresses and project allocations, you can't configure VPC Service Controls perimeters by using static IP allowlists or project rules. To permit Data Studio access through a VPC Service Controls perimeter, you must add a service account as a principal in your access levels or ingress and egress rules.

## Set up a Google Cloud service account

Service accounts prevent reports from breaking if an employee leaves the company, and they allow secure network access inside VPC-SC perimeters. Instead of delegating access by using **Owner's credentials** , or requiring individual report viewers to have access to the data by using **Viewer's credentials** , administrators can configure a dedicated Google Cloud service account to query data.

To review required role assignments (`roles/bigquery.dataViewer`, `roles/bigquery.jobUser`) and setup steps in the Google Cloud console, see [Set up a Google Cloud service account for Data Studio](https://docs.cloud.google.com/data-studio/set-up-a-google-cloud-service-account).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
