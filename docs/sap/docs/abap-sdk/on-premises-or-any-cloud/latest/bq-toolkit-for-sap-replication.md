---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-replication/
title: Replication of SAP data into BigQuery by using the BigQuery Toolkit for SAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:02:10.621195+00:00
---

# Replication of SAP data into BigQuery by using the BigQuery Toolkit for SAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Replication of SAP data into BigQuery by using the BigQuery Toolkit for SAP Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/bq-toolkit-for-sap-replication)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-replication)



For replication of SAP data into BigQuery, you use the data load class `/GOOG/CL_BQTR_DATA_LOAD` within your SAP applications such as custom ABAP programs, user exits, Business Add-Ins (BAdIs), and enhancements. Your SAP application needs to pass the data to be replicated as an input to the class.

## Call the data replication method

You instantiate the BigQuery data load class `/GOOG/CL_BQTR_DATA_LOAD` by passing the mass transfer key and the name of the dictionary object configured in the BigQuery Data Transfer configuration.

To send the data to BigQuery, you call the `REPLICATE_DATA` method of the class `/GOOG/CL_BQTR_DATA_LOAD`.
    
    
    DATA(lo_bq_data_load) =
      NEW /GOOG/CL_BQTR_DATA_LOAD( IV_MASS_TR_KEY = 'MASS_TRANSFER_KEY'
                                   IV_DATA_SOURCE = 'DATA_SOURCE'
                                   IV_CDC_FRAMEWORK = 'CDC_FRAMEWORK'
                                   IV_FLDNM_MANDT = 'MANDT_FIELDNAME'
                                   IV_MANDT_VALUE = 'MANDT_VALUE'
     ).
    "Write Logic to populate ITAB_DATA, WA_HEADER
    
    "Replicate Data to BigQuery
    lo_bq_data_load->replicate_data(
      EXPORTING
        it_content       = ITAB_DATA
        IS_HEADER_INFO   = WA_HEADER
      IMPORTING
        ev_error_code    = data(lv_error_code)
        et_return        = data(lt_return) ).
    

Replace the following:

  * `MASS_TRANSFER_KEY`: The mass transfer key configured in the BigQuery Data Transfer configuration.
  * `DATA_SOURCE`: The name of the SAP dictionary object such as table, dictionary view, or CDS view.
  * `CDC_FRAMEWORK`: Optional. The Change Data Capture (CDC) framework used by the calling program. The supported values are `ODQ` and `SLT`.

The BigQuery Toolkit for SAP has built-in logic to determine the operation flag (insert, update, and delete) based on the CDC framework. For more information, see [Extra fields for record changes and count queries](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-overview#fields-for-changes-and-counts).

When `CDC_FRAMEWORK` is passed as `ODQ`, the BigQuery Toolkit for SAP gets the value of column `ODQ_CHANGEMODE` in payload passed in the input:

    * If the value = `C`, the `operation_flag` is set to `I`.
    * If the value = `U`, the `operation_flag` is set to `U`.
    * If the value = `D`, the `operation_flag` is set to `D`.
    * For all other values, the `operation_flag` is set to `L`.

When `CDC_FRAMEWORK` is passed as `SLT`, the BigQuery Toolkit for SAP gets the value of column 'OPERATION' from `WA_HEADER`:

    * If the value = `I`, the `operation_flag` is set to `I`.
    * If the value = `U`, the `operation_flag` is set to `U`.
    * If the value = `D`, the `operation_flag` is set to `D`.
    * For all other values, the `operation_flag` is set to `L`.

If `CDC_FRAMEWORK` is not passed or passed as any other value, then the `operation_flag` is set to `L`.

  * `MANDT_FIELDNAME`: Optional. The name of the SAP client field that needs to be appended to the BigQuery table definition. This can be used for SAP dictionary objects such as CDS entities, which don't have the client field in their definition, but you want the field to be added to BigQuery.

  * `MANDT_VALUE`: Optional. The value of the SAP client field that needs to be populated in BigQuery. This can be only used when `IV_FLDNM_MANDT` is also populated.

  * `ITAB_DATA`: An internal table of type `DATA_SOURCE`. You populate `ITAB_DATA` with the data that needs to be replicated to the BigQuery table.

  * `WA_HEADER`: A flat structure, which contains header information about the replication. This is used to determine the `operation_flag` when `CDC_FRAMEWORK` is `SLT`.




When you call this method, the BigQuery Data Transfer module does the following actions:

  * Sync BigQuery table definition with SAP dictionary object definition based on the table and field settings maintained in BigQuery Data Transfer configuration.
  * Map data populated in `ITAB_DATA` from SAP format to BigQuery format based on field level settings maintained in the BigQuery Data Transfer configuration. If field level settings are not maintained, then the default data mapping rules are used.
  * Call the BigQuery API `InsertAllTabledata` method to load data to the target BigQuery table.



If all steps are successful, then the exporting parameter `ev_error_code` returns the value `0`. If there was an error in any step, `ev_error_code` returns a non-zero value and the corresponding error message is populated in `et_return`.

As an application developer, you can handle errors, including saving them for later analysis and retrying the loading of records that failed replication.

## Get support

Google Cloud offers support for issues and questions related to the installation, configuration, operation, and maintenance of the BigQuery Toolkit for SAP.

For issues originating from SAP-managed components or third-party software, Google Cloud Customer Care makes its best effort to identify the root cause. To resolve these issues, contact the respective vendor or support provider.

To troubleshoot problems with the BigQuery Toolkit for SAP, see [Troubleshooting the BigQuery Toolkit for SAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-toolkit-for-sap-troubleshooting).

If you need help resolving problems with the on-premises or any cloud edition of ABAP SDK for Google Cloud, then do the following:

  * Refer to the [ on-premises or any cloud edition of ABAP SDK for Google Cloud troubleshooting guide](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/troubleshooting).

  * Ask your questions and discuss ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).

  * Collect all available [diagnostic information](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/getting-support-diag-info) and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
