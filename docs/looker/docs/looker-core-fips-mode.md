---
url: https://docs.cloud.google.com/looker/docs/looker-core-fips-mode/
title: Enable FIPS 140-3 level 1 compliance on a Looker (Google Cloud core) instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:40.502645+00:00
---

# Enable FIPS 140-3 level 1 compliance on a Looker (Google Cloud core) instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-fips-mode/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Enable FIPS 140-3 level 1 compliance on a Looker (Google Cloud core) instance Stay organized with collections  Save and categorize content based on your preferences. 

To meet regulatory or data security requirements, you can enable [Federal Information Processing Standard Publication (FIPS) 140-3](https://csrc.nist.gov/pubs/fips/140-3/final) level 1 compliance for new Looker (Google Cloud core) instances. FIPS 140-3 is a US government computer security standard that certifies cryptographic modules. You can configure FIPS 140-3 validated encryption when you create new Looker (Google Cloud core) instances of the **Enterprise** or **Embed** edition.

This document explains how to configure FIPS 140-3 validated encryption.

If your Looker (Google Cloud core) instance was created with the **FIPS 140-2 level 1** standard, it will be automatically updated to FIPS 140-3 level 1 encryption upon upgrade to Looker 26.12.

## Create a FIPS 140-3 level 1 compliant Looker (Google Cloud core) instance

To create a new FIPS 140-3 level 1 compliant Looker (Google Cloud core) instance, in the **FIPS 140-3 level 1 Validated Encryption** portion of the **Encryption** section, select the **Enable FIPS 140-3 level 1 Validated encryption** checkbox when [you create the Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-instance-create).

Only new instances can be placed into FIPS-compliant mode.

Looker (Google Cloud core) doesn't support [exporting](https://docs.cloud.google.com/looker/docs/looker-core-import-export) or [migrating](https://docs.cloud.google.com/looker/docs/looker-core-self-service-migration) data from an instance that isn't FIPS compliant into a FIPS-compliant instance.

## FIPS and database dialects

Any database that was used by a Looker (Google Cloud core) instance that is in FIPS-compliant mode won't work with a Looker (Google Cloud core) instance that is not in FIPS-compliant mode.

Several database dialects that are otherwise supported by Looker (Google Cloud core) are not supported in FIPS-compliant mode. The following [dialects](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported-dialects-for) are not supported in FIPS-compliant mode:

  * Apache Druid
  * Denodo 8
  * Dremio 11+
  * IBM Netezza
  * Microsoft Azure SQL Database
  * Microsoft SQL Server (MSSQL)
  * PrestoDB
  * PrestoSQL
  * Teradata
  * Trino



## FIPS and group mirroring

FIPS-compliant Looker (Google Cloud core) instances that use Google OAuth for user authentication don't support [group mirroring](https://docs.cloud.google.com/looker/docs/looker-core-oauth-authentication#mirroring) between Google Groups and Looker (Google Cloud core).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
