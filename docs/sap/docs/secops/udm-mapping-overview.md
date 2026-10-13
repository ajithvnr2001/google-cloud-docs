---
url: https://docs.cloud.google.com/sap/docs/secops/udm-mapping-overview/
title: UDM mapping for SAP logs \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:33.443849+00:00
---

# UDM mapping for SAP logs  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/secops/udm-mapping-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  UDM mapping for SAP logs Stay organized with collections  Save and categorize content based on your preferences. 

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document provides a reference for how Google SecOps for SAP log sources are mapped to the Unified Data Model (UDM) log types in Google SecOps.

## How mapping works

The Google SecOps for SAP uses SAP-specific standard parsers within Google SecOps to automatically transform raw SAP logs into the UDM format.

## Field mapping reference

This section provides an overview of the SAP log sources that are mapped to the UDM. For detailed field-level mapping information, see the reference documentation for each log source.

### SAP HANA Audit

The `SAP_HANA_AUDIT` parser captures security-relevant events within the SAP HANA database, such as system configuration changes, user authorization modifications, and access to sensitive data.

**Ingestion label** : `SAP_HANA_AUDIT`

For more information, see [SAP HANA Audit UDM mapping](https://docs.cloud.google.com/sap/docs/secops/sap-hana-audit-udm-mapping).

### SAP Change Document

The `SAP_CHANGE_DOCUMENT` parser tracks changes made to business objects in SAP systems, including creations, modifications, and deletions of data.

**Ingestion label** : `SAP_CHANGE_DOCUMENT`

For more information, see [SAP Change Document UDM mapping](https://docs.cloud.google.com/sap/docs/secops/sap-change-document-udm-mapping).

### SAP Web Dispatcher

The `SAP_WEBDISP` parser logs HTTP and HTTPS traffic passing through the SAP Web Dispatcher, providing visibility into external access to SAP web services and applications.

**Ingestion label** : `SAP_WEBDISP`

For more information, see [SAP Web Dispatcher UDM mapping](https://docs.cloud.google.com/sap/docs/secops/sap-webdisp-udm-mapping).

### SAP Security Audit

The `SAP_SECURITY_AUDIT` parser records security-critical events at the SAP application level, such as user logins, failed logon attempts, transaction executions, and report starts.

**Ingestion label** : `SAP_SECURITY_AUDIT`

For more information, see [SAP Security Audit UDM mapping](https://docs.cloud.google.com/sap/docs/secops/sap-security-audit-udm-mapping).

### SAP Gateway

The `SAP_GATEWAY` parser monitors communication between SAP systems and external applications through the SAP Gateway, logging connection attempts and security-related errors.

**Ingestion label** : `SAP_GATEWAY`

For more information, see [SAP Gateway UDM mapping](https://docs.cloud.google.com/sap/docs/secops/sap-gateway-udm-mapping).

### SAP ICM

The `SAP_ICM` parser records details of web-based communication (HTTP, HTTPS, SMTP) between the SAP Application Server and the internet.

**Ingestion label** : `SAP_ICM`

For more information, see [SAP ICM UDM mapping](https://docs.cloud.google.com/sap/docs/secops/sap-icm-udm-mapping).

## Use UDM in searches

To filter SAP events when searching in Google SecOps, use the `log_type` filter to narrow your results:
    
    
    log_type = "SAP_SECURITY_AUDIT" and principal.user.userid = "ADMIN_USER"
    

## Get support

For issues related to Google SecOps for SAP, [contact Google SecOps support](https://docs.cloud.google.com/chronicle/docs/getting-support). Our team provides assistance or guides you to the right resource to help ensure a timely resolution.

For issues involving SAP systems or the LogServ service, contact SAP support. For issues related to other third-party products, such as Bindplane, contact the appropriate third-party vendor for assistance.

Get technical answers and peer support in the [Google SecOps Community](https://security.googlecloudcommunity.com/google-security-operations-2).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
