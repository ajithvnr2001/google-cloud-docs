---
url: https://docs.cloud.google.com/looker/docs/fips-mode/
title: Enabling FIPS 140-2 level 1 compliance \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:33:36.634882+00:00
---

# Enabling FIPS 140-2 level 1 compliance  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/fips-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  Enabling FIPS 140-2 level 1 compliance Stay organized with collections  Save and categorize content based on your preferences. 

The [Federal Information Processing Standard Publication (FIPS) 140-2](https://csrc.nist.gov/pubs/fips/140-2/upd2/final) is a US government computer security standard that is used to approve cryptographic modules. New customer-hosted Looker instances can be created to meet FIPS 140-2 level 1 standards.

## Creating a FIPS 140-2 compliant Looker instance

To create a new FIPS 140-2 compliant Looker instance, include the `--fips` [startup option](https://docs.cloud.google.com/looker/docs/startup-options) when you first start the instance. This puts the new instance in FIPS-compliant mode.

Only new instances can be placed into FIPS-compliant mode. An instance that has an existing Looker database will fail to start when the `--fips` startup option is specified.

## FIPS and SSL

Looker provides FIPS-compliant SSL for outgoing connections (for example, databases, query result delivery endpoints, OAuth, and others). However, the customer must provide an external SSL termination endpoint for incoming `https` requests.

We recommend using NGINX with a FIPS 140-2 compliant build of OpenSSL, as described in the [NGINX documentation](https://docs.nginx.com/nginx/fips-compliance-nginx-plus/).

Follow NGINX instructions to [configure SSL termination](https://docs.nginx.com/nginx/admin-guide/security-controls/terminating-ssl-http/).

## FIPS and database dialects

Any database that was used by a Looker instance that is in FIPS-compliant mode won't work with a Looker instance that is not in FIPS-compliant mode.

Several database [dialects](https://docs.cloud.google.com/looker/docs/dialects) that are otherwise supported by Looker are not supported in FIPS-compliant mode. The following dialects are not supported in FIPS-compliant mode:

  * Actian Avalanche
  * Denodo 7
  * Denodo 8
  * Dremio
  * Dremio 11+
  * Druid
  * Exasol
  * IBM Netezza
  * Microsoft SQL Server (MSSQL)
  * PrestoDB
  * PrestoSQL
  * Teradata
  * Trino
  * Vector



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
