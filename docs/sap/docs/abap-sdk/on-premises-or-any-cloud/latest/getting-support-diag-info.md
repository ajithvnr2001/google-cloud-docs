---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/getting-support-diag-info/
title: On-premises edition of ABAP SDK for Google Cloud diagnostic information \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:02:08.975373+00:00
---

# On-premises edition of ABAP SDK for Google Cloud diagnostic information  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/getting-support-diag-info/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Support ](https://docs.cloud.google.com/sap/docs/getting-support)



Send feedback 

#  On-premises edition of ABAP SDK for Google Cloud diagnostic information Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/getting-support-diag-info)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/getting-support-diag-info)



For problems that are related to on-premises or any cloud edition of ABAP SDK for Google Cloud, provide the following diagnostic information to Cloud Customer Care when you open a case:

  * A complete and detailed description of the problem
  * Error message encountered
  * API class and method name
  * Configuration details
  * SAP system environment details
  * Logs



You can also discuss ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).

## Detailed description of the problem

Provide a complete and detailed description of the problem, including the version of the ABAP SDK for Google Cloud, and the date and time when the problem occurred.

To see the version of your SDK, follow these steps:

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Utilities > Get Product Version**.




## Error message encountered

Provide the error messages that you have encountered in the ABAP SDK for Google Cloud.

## API class and method name

Provide the API class name and API method name. For example:

  * Client API class name/API name: `/GOOG/CL_PUBSUB_V1`
  * Client API method name/API method name: `PUBLISH_TOPICS`



## Configuration details

Provide the following configuration details:

  * Client key configurations maintained in the table `/GOOG/CLIENT_KEY`. For more information, see [Client key configuration table](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#client_key_config).

  * Service mapping configurations maintained in the table `/GOOG/SERVIC_MAP`. For more information, see [Service mapping table](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#service_mapping_config).

  * Log configurations maintained in the table `/GOOG/LOG_CONFIG`. For more information, see [Logging configuration table](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#log_config).

  * Parameter settings maintained in the table `/GOOG/SDK_PARAM`. For more information, see [Advanced settings parameters table](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#advanced_settings).




## SAP system environment details

Provide the following environment details of your SAP system:

  * Specify if your SAP system is hosted on Google Cloud or outside of Google Cloud.
  * Your SAP system version: 
    * `SAP_BASIS` component version.
    * Installed product version.
  * Environment language: 
    * SAP logon language.
    * Language of background mode.



## Logs

Provide the following logs:

  * ABAP SDK for Google Cloud logs. For information about how to find the SDK logs, see [Logging](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/troubleshooting#logging).
  * `ST22` dumps, and `SLG1` logs, if available.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
