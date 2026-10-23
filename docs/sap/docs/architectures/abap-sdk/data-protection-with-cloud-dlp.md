---
url: https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/data-protection-with-cloud-dlp/
title: Data protection in SAP with the DLP API \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:39.434861+00:00
---

# Data protection in SAP with the DLP API  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/data-protection-with-cloud-dlp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Data protection in SAP with the DLP API Stay organized with collections  Save and categorize content based on your preferences. 

This document describes a reference architecture for protecting sensitive enterprise data in SAP by using the [Cloud Data Loss Prevention (DLP) API](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest) with the [SAP BTP edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/all-guides).

It's essential to protect the sensitive enterprise data such as personally identifiable information (PII) that you store in SAP. Sharing sensitive enterprise data from SAP with the wrong people or systems can damage your company's reputation and lead to financial losses. The DLP API provides a powerful and flexible way to add a layer of protection for sensitive data. This API can discover, classify, and de-identify sensitive information before it is stored in or transmitted from SAP. It helps you proactively identify and safeguard confidential information, reducing the risk of data breaches and ensuring compliance with privacy regulations.

The intended audience for this document includes ABAP developers, SAP solution architects, and cloud architects whose responsibilities include data security, data processing, or data analytics. This document assumes that you're familiar with data processing and data privacy, [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview) and related [concepts](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts), such as [InfoTypes and infoType detectors](https://docs.cloud.google.com/sensitive-data-protection/docs/concepts-infotypes).

## Architecture

The following diagram shows a reference architecture for a DLP solution, encompassing components from an SAP BTP ABAP environment and Google Cloud.

![DLP solution for data protection in SAP](https://docs.cloud.google.com/static/sap/docs/architectures/architecture-images/abap-sdk/abap-sdk-data-protection-with-cloud-dlp.svg)

This DLP solution architecture includes the following components:

Component | Subsystem | Details  
---|---|---  
1 | Input source | Acts as the entry point for data.  
2 | Client service | An ABAP class that interacts with all other components. It receives the source data, sends data to the DLP API through the ABAP SDK for Google Cloud for processing, and stores the processed data in SAP datastore.  
3 | ABAP SDK for Google Cloud | The SAP BTP edition of ABAP SDK for Google Cloud for accessing the DLP API.   
4 | DLP API | The DLP API provides various [transformation methods](https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference) for de-identification of PII.   
5 | Target datastore | An SAP ERP system, running on the cloud or on-premises, where the data is stored after the PII is processed and de-identified.  
  
## Products used

This reference architecture uses the following Google Cloud products:

  * [ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/overview)
  * [Sensitive Data Protection](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview)



## Use case

This section provides examples of use cases for which you can use the [DLP API](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest) to protect sensitive enterprise data in SAP.

### Complying with data privacy regulations

Organizations are often required to de-identify sensitive data. There are many government policies such as GDPR and DPDP, which mandate that PII is not stored under certain conditions.

## Cost

For an estimate of the cost of the Google Cloud resources that the DLP API uses, see the precalculated estimate in the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator/).

## Design alternative

While this document focuses on the SAP BTP edition of ABAP SDK for Google Cloud, you can achieve similar results by using the on-premises or any cloud edition of ABAP SDK for Google Cloud. In this setup, you can store the processed and de-identified sensitive data (PII) within your on-premises SAP system.

## Deployment

This section shows you how to deploy a solution that protects sensitive data during the creation of a business partner (person) in your SAP system. Based on the configuration set by your organization, this solution can redact, de-identify, or anonymize data.

### Before you begin

Before implementing a solution based on this reference architecture, make sure that you have completed the following prerequisites:

  * You have a Google Cloud account and project.

  * Billing is enabled for your project. For information about how to confirm that billing is enabled for your project, see [Verify the billing status of your projects](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  * The [SAP BTP edition of ABAP SDK for Google Cloud is installed and configured](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/install-config).

  * Authentication to access Google Cloud APIs is set up. For information about how to set up authentication, see [Set up authentication for the SAP BTP edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/authentication).

  * The [DLP API](https://console.cloud.google.com/project/_/apis/library/dlp.googleapis.com) is enabled in your Google Cloud project.




### Implement a client service for PII de-identification

Input from the data source is processed in a client service that you implement within your SAP BTP ABAP Environment. This client service can consist of the following subcomponents:

  * Rule configuration: Stores business rules that need to be applied for different kinds of PII relevant fields.
  * DLP Proxy module: Calls the DLP API through the SAP BTP edition of ABAP SDK for Google Cloud.



#### Rule configuration

In your SAP BTP ABAP environment, you create a configuration table to maintain the transformation rules that need to be applied for different kinds of PII relevant fields. In a production environment, you can use a tool such as SAP Fiori to maintain the data in this table.

You can implement the following sample rules:

  * Any field with an email address must be replaced with a dummy value.
  * Any field with a phone number must be masked.
  * Any field with comments, notes, or remarks must not contain any information related to email address.
  * Any field with bank account details must be tokenized by using crypto based de-identification method.



The following is the definition of a sample configuration table:
    
    
    define table zgoog_dlp_config {
     key client         : abap.clnt not null;
     key keyword        : abap.char(60) not null;
     key infotype       : abap.char(60) not null;
     surrogate_infotype : abap.char(60);
     common_alphabhet   : abap.char(20);
     masking_char       : abap.char(1);
     number_to_mask     : int4;
    }
    

The following example shows the sample transformation rules:
    
    
       lt_dlp_config = VALUE #(
          ( client = sy-mandt keyword  = 'EMAIL' infotype = 'EMAIL_ADDRESS'  )
          ( client = sy-mandt keyword  = 'PHONE NUMBER' infotype = 'PHONE_NUMBER' number_to_mask = 5 masking_char = '*' )
          ( client = sy-mandt keyword  = 'REMARKS' infotype = 'EMAIL_ADDRESS'  )
          ( client = sy-mandt keyword  = 'REMARKS' infotype = 'PHONE_NUMBER'  )
          ( client = sy-mandt keyword  = 'BANK ACCOUNT' infotype = 'FINANCIAL_ACCOUNT_NUMBER' surrogate_infotype = 'ACCOUNT' common_alphabhet = 'ALPHA_NUMERIC' )
        ).
    

#### DLP proxy module

You can create a dedicated subcomponent named as DLP proxy module. This module can be an ABAP class or a REST service. Its primary function is to de-identify PII by using the transformation rules that you defined earlier.

The DLP proxy module uses the `DEIDENTIFY_CONTENT` method of the [`/GOOG/CL_DLP_V2`](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_dlp_v2) class within the SAP BTP edition of ABAP SDK for Google Cloud.

The following sections show sample implementations of how to use the DLP proxy module for PII de-identification in various scenarios.

##### Replacement: Replaces a detected sensitive value with a specified surrogate value

To replace a detected email ID with a generic value, perform the following steps:

  1. Create a client object for the [`/GOOG/CL_DLP_V2`](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_dlp_v2) class.

  2. Use the configuration table to determine the type of transformation to apply.

  3. To mask the email IDs, substitute them with the replacement value such as `EMAIL_ID@EXAMPLE.COM`.

  4. Call the DLP API.

  5. Use the `DEIDENTIFY_CONTENT` method with all relevant parameters including the replacement value and return the output to the client service.




The following code sample illustrates the preceding steps:
    
    
    DATA:    ls_input           TYPE /goog/cl_dlp_v2=>ty_055,
             ls_transformations TYPE /goog/cl_dlp_v2=>ty_100.
    
    TRY.
       DATA(lo_client) = NEW /goog/cl_dlp_v2( iv_key_name = 'CLIENT_KEY' ).
       DATA(lv_p_projects_id) = CONV string( lo_client->gv_project_id ).
    
       "As a developer, you need to read the configuration into mt_dlp_config
       TRY.
       "As a developer, you need to read the configuration
        DATA(ls_dlp_config) = mt_dlp_config[ keyword = iv_input_type ].
            "Populate the input parameters to DLP API for replacement
    INSERT VALUE #( name = ls_dlp_config-infotype ) INTO TABLE ls_input-inspect_config-info_types.ls_transformations-primitive_transformation-replace_config-new_value-string_value  = 'REPLACEMENT_VALUE'.
    INSERT ls_transformations INTO TABLE ls_input-deidentify_config-info_type_transformations-transformations.
            ls_input-item-value = iv_input_value.
            "Call DLP API client stub
            TRY.
                lo_client->deidentify_content(
                   EXPORTING
                       iv_p_projects_id = lv_p_projects_id
                       is_input         = ls_input
                   IMPORTING
                       es_output        = DATA(ls_output)
                       ev_ret_code      = DATA(lv_ret_code)
                       ev_err_text      = DATA(lv_err_text)
                    ).
            CATCH /goog/cx_sdk INTO DATA(lx_sdk_exception).
                 ev_message = lx_sdk_exception->get_text( ).
            ENDTRY.
            IF lo_client->is_success( lv_ret_code ).
                 ev_message = lv_err_text.
            ELSE.
                ev_output_value = ls_output-item-value.
            ENDIF.
        CATCH cx_sy_itab_line_not_found INTO DATA(lx_not_found).
            ev_output_value = iv_input_value.
        ENDTRY.
    "Close the http client
    lo_client->close_http_client( ).
    CATCH /goog/cx_sdk INTO DATA(lx_sdk).
       ev_message = lx_sdk->get_text(  ).
    ENDTRY.
    

Replace the following:

  * `CLIENT_KEY`: The client key configured for authentication.
  * `REPLACEMENT_VALUE`: The replacement value, such as `EMAIL_ID@EXAMPLE.COM`.



##### Redaction: Deletes all or part of a detected sensitive value

To delete all or part of a detected sensitive value, perform the following steps:

  1. Create a client object for the [`/GOOG/CL_DLP_V2`](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_dlp_v2) class.

  2. Use the configuration table to determine the type of transformation to apply.

  3. Specify to delete all or part of a detected sensitive value.

  4. Call the DLP API.

  5. Use the `DEIDENTIFY_CONTENT` method with all relevant parameters and return the output to the client service.



    
    
    DATA:    ls_input           TYPE /goog/cl_dlp_v2=>ty_055,
             ls_transformations TYPE /goog/cl_dlp_v2=>ty_100,
     lo_redact          TYPE REF TO data.
    
       DATA(lo_client) = NEW /goog/cl_dlp_v2( iv_key_name = 'CLIENT_KEY' ).
       DATA(lv_p_projects_id) = CONV string( lo_client->gv_project_id ).
    
       "As a developer, you need to read the configuration into mt_dlp_config
       TRY.
            "Read the configuration
    DATA(ls_dlp_config) = mt_dlp_config[ keyword = iv_input_type ].
            "Populate the input parameters to DLP API for redaction
    CREATE DATA lo_redact TYPE REF TO string.
    INSERT VALUE #( name = ls_dlp_config-infotype ) INTO TABLE ls_input-inspect_config-info_types.
    INSERT VALUE #( name = ls_dlp_config-infotype ) INTO TABLE ls_transformations-info_types.
            ls_transformations-primitive_transformation-redact_config = lo_redact.
    INSERT ls_transformations INTO TABLE ls_input-deidentify_config-info_type_transformations-transformations.
            ls_input-item-value = iv_input_value.
            "Call DLP API client stub
            TRY.
    lo_client->deidentify_content(
                            EXPORTING
                                    iv_p_projects_id = lv_p_projects_id
                                is_input         = ls_input
                            IMPORTING
                                es_output        = DATA(ls_output)
                                ev_ret_code      = DATA(lv_ret_code)
                                ev_err_text      = DATA(lv_err_text)
                     ).
    CATCH /goog/cx_sdk INTO lx_sdk_exception.
                  ev_message = lx_sdk_exception->get_text( ).
            ENDTRY.
         IF lo_client->is_success( lv_ret_code ).
               ev_message = lv_err_text.
            ELSE.
              ev_output_value = ls_output-item-value.
            ENDIF.
      CATCH cx_sy_itab_line_not_found INTO lx_not_found.
          ev_output_value = iv_input_value.
      ENDTRY.
    
      "Close the http client
         lo_client->close_http_client( ).
    CATCH /goog/cx_sdk INTO DATA(lx_sdk).
       ev_message = lx_sdk->get_text(  ).
    ENDTRY.
    

Replace `CLIENT_KEY` with the client key configured for authentication.

##### Masking: Replaces a number of characters of a sensitive value with a specified character, such as a hash (#) or asterisk (*)

To replace values with a specified character, perform the following steps:

  1. Create a client object for the [`/GOOG/CL_DLP_V2`](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_dlp_v2) class.

  2. Use the configuration table to determine the type of transformation to apply.

  3. Set the masking character and number of characters to mask according to the configuration table.

  4. Call the DLP API.

  5. Use the `DEIDENTIFY_CONTENT` method with all relevant parameters including the replacement value and return the output to client service.



    
    
    DATA:    ls_input           TYPE /goog/cl_dlp_v2=>ty_055,
             ls_transformations TYPE /goog/cl_dlp_v2=>ty_100.
    TRY.
       DATA(lo_client) = NEW /goog/cl_dlp_v2( iv_key_name = 'CLIENT_KEY' ).
       DATA(lv_p_projects_id) = CONV string( lo_client->gv_project_id ).
    
       "As a developer, you need to read the configuration into mt_dlp_config
       TRY.
    "Read the configuration
            DATA(ls_dlp_config) = mt_dlp_config[ keyword = iv_input_type ].
        "Populate the input parameters to DLP API for masking
    INSERT VALUE #( name = ls_dlp_config-infotype ) INTO TABLE ls_input-inspect_config-info_types.
    ls_transformations-primitive_transformation-character_mask_config-number_to_mask =  ls_dlp_config-number_to_mask.
    ls_transformations-primitive_transformation-character_mask_config-masking_character = ls_dlp_config-masking_char.
    INSERT ls_transformations INTO TABLE ls_input-deidentify_config-info_type_transformations-transformations.
            ls_input-item-value = iv_input_value.
            "Call DLP API client stub
             TRY.
                       lo_client->deidentify_content(
                           EXPORTING
                             iv_p_projects_id = lv_p_projects_id
                             is_input         = ls_input
                           IMPORTING
                             es_output        = DATA(ls_output)
                             ev_ret_code      = DATA(lv_ret_code)
                             ev_err_text      = DATA(lv_err_text)
                         ).
                  CATCH /goog/cx_sdk INTO lx_sdk_exception.
                       ev_message = lx_sdk_exception->get_text( ).
                  ENDTRY.
                  IF lo_client->is_success( lv_ret_code ).
                     ev_message = lv_err_text.
                  ELSE.
                     ev_output_value = ls_output-item-value.
                  ENDIF.
          CATCH cx_sy_itab_line_not_found INTO lx_not_found.
             ev_output_value = iv_input_value.
          ENDTRY.
       "Close the http client
         lo_client->close_http_client( ).
    CATCH /goog/cx_sdk INTO DATA(lx_sdk).
       ev_message = lx_sdk->get_text(  ).
    ENDTRY.
    

Replace `CLIENT_KEY` with the client key configured for authentication.

##### Crypto-based tokenization: Encrypts the original sensitive data value by using a cryptographic key

For crypto-based tokenization, you need to [create a crypto key and a wrapped key](https://docs.cloud.google.com/sensitive-data-protection/docs/create-wrapped-key). This guide uses format-preserving encryption. This method creates a token that has the same length and characters as the original input value.

To de-identify sensitive data value by using crypto hash mapping, perform the following steps:

  1. Create a client object for the [`/GOOG/CL_DLP_V2`](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/reference/googcl_dlp_v2) class.

  2. Use the configuration table to determine the type of transformation to apply.

  3. Set the crypto key and wrapped key created earlier.

  4. Call the DLP API.

  5. Use the `DEIDENTIFY_CONTENT` method with all relevant parameters for cryptographic encryption and return the output to client service.



    
    
    DATA:    ls_input               TYPE /goog/cl_dlp_v2=>ty_055,
             ls_transformations     TYPE /goog/cl_dlp_v2=>ty_100,
             ls_kms_wrapped_key     TYPE /goog/cl_dlp_v2=>ty_123,
             ls_crypto_key          TYPE /goog/cl_dlp_v2=>ty_040,
             ls_crypto_hash_config  TYPE /goog/cl_dlp_v2=>ty_039.
    
    TRY.
       DATA(lo_client) = NEW /goog/cl_dlp_v2( iv_key_name = 'CLIENT_KEY' ).
       DATA(lv_p_projects_id) = CONV string( lo_client->gv_project_id ).
    
       "As a developer, you need to read the configuration into lt_dlp_config
       "As a developer, you need to populate the crypto key name and wrapped key
    
       ls_kms_wrapped_key-crypto_key_name = 'CRYPTO_KEY_NAME'. "Crypto_key_name.
       ls_kms_wrapped_key-wrapped_key = 'WRAPPED_KEY_NAME'. "Wrapped_key.
       ls_crypto_key-kms_wrapped = ls_kms_wrapped_key.
       ls_crypto_hash_config-crypto_key = ls_crypto_key.
       TRY.
    "Read the configuration
            DATA(ls_dlp_config) = mt_dlp_config[ keyword = iv_input_type ].
        "Populate the input parameters to DLP API for cryptographic encryption
    INSERT VALUE #( name = ls_dlp_config-infotype ) INTO TABLE ls_input-inspect_config-info_types.
    INSERT VALUE #( name = ls_dlp_config-infotype ) INTO TABLE ls_transformations-info_types.             ls_transformations-primitive_transformation-crypto_replace_ffx_fpe_config-crypto_key-kms_wrapped = ls_kms_wrapped_key.             ls_transformations-primitive_transformation-crypto_replace_ffx_fpe_config-surrogate_info_type-name = ls_dlp_config-surrogate_infotype.          ls_transformations-primitive_transformation-crypto_replace_ffx_fpe_config-common_alphabet = ls_dlp_config-common_alphabhet.
    INSERT ls_transformations INTO TABLE ls_input-deidentify_config-info_type_transformations-transformations.
            ls_input-item-value = iv_input_value.
        "Add the info type identification string to map the subsequent value to relevant infotype
    CONCATENATE 'Bank Account' ls_input-item-value INTO ls_input-item-value SEPARATED BY space.
    "Call DLP API client stub
    TRY.
                    lo_client->deidentify_content(
                            EXPORTING
                                iv_p_projects_id = lv_p_projects_id
                                is_input         = ls_input
                            IMPORTING
                                es_output        = DATA(ls_output)
                                ev_ret_code      = DATA(lv_ret_code)
                                ev_err_text      = DATA(lv_err_text)
                     ).
    CATCH /goog/cx_sdk INTO DATA(lx_sdk_exception).
                            ev_message = lx_sdk_exception->get_text( ).
                    ENDTRY.
             IF lo_client->is_success( lv_ret_code ).
                ev_message = lv_err_text.
             ELSE.
    "Removing the info type identification string added earlier and keeping only the encrypted value
        REPLACE ALL OCCURRENCES OF SUBSTRING 'Bank Account' IN ls_output-item-value WITH ''.
        REPLACE ALL OCCURRENCES OF SUBSTRING 'ACCOUNT(10):' IN ls_output-item-value WITH ''.
            ev_output_value  = ls_output-item-value.
            ENDIF.
          CATCH cx_sy_itab_line_not_found INTO lx_not_found.
             ev_output_value = iv_input_value.
          ENDTRY.
     "Close the http client
       lo_client->close_http_client( ).
    CATCH /goog/cx_sdk INTO DATA(lx_sdk).
       ev_message = lx_sdk->get_text(  ).
    ENDTRY.
    

Replace the following:

  * `CLIENT_KEY`: The client key configured for authentication.
  * `CRYPTO_KEY_NAME`: The crypto key name.
  * `WRAPPED_KEY_NAME`: The wrapped key name.



### Transmit the input data to the client service

Transmit data from your input source system to the client service. You can transmit data by using an API call, a frontend UI application, a local file, a third party application or any other source.

For information about building an SAP Fiori App, see [Build an SAP Fiori App Using the ABAP RESTful Application Programming Model](https://developers.sap.com/mission.sap-fiori-abap-rap100.html).

### Call the DLP proxy module

Call the DLP proxy module from the client service, which receives the source input.

The following code sample illustrates how to call the DLP proxy module from the client service:
    
    
     DATA : lv_input  TYPE string,
                lv_output TYPE String.
    
    "As a developer, you need to populate input data into relevant fields
    "Redaction: Deletes all or part of a detected sensitive value
    " - Remarks
    lv_input = lv_email_address.
    zgoog_cl_dlp_proxy=>call_dlp( EXPORTING iv_input_value  = lv_input iv_input_type = 'EMAIL'
                                  IMPORTING ev_output_value = lv_output ev_message = ev_message ).
    ls_bupa_email_address-email_address = lv_output.
    
    "Masking: Replaces a number of characters of a sensitive value with a specified surrogate character, such as a hash (#) or asterisk (*).
    " - Phone Number
    lv_input = lv_phone_number.
    zgoog_cl_dlp_proxy=>call_dlp( EXPORTING iv_input_value = lv_input iv_input_type = 'PHONE NUMBER'
                                  IMPORTING ev_output_value = lv_output ev_message = ev_message ).
    ls_bupa_phone_number-phone_number = lv_output.
    
    "Replacement: Replaces a detected sensitive value with a specified surrogate value.
    " - Email ID
    lv_input = lv_address_comm_remarks.
    zgoog_cl_dlp_proxy=>call_dlp( EXPORTING iv_input_value  = lv_input iv_input_type = 'REMARKS'
                                  IMPORTING ev_output_value = lv_output ev_message = ev_message ).
    ls_bupa_email_address-address_comm_remarks = lv_output.
    
    "Crypto-based tokenization: Encrypts the original sensitive data value by using a cryptographic key. Sensitive Data Protection supports several types of tokenization,
    "including transformations that can be reversed, or "re-identified."
    " - Bank account number
    lv_input = lv_bank_account.
    zgoog_cl_dlp_proxy=>call_dlp( EXPORTING iv_input_value  = lv_input iv_input_type = 'BANK ACCOUNT'
                                  IMPORTING ev_output_value = lv_output ev_message = ev_message ).
    ls_bupa_bank_details-bank_account = lv_output.
    

### Store data into SAP ERP system

After the relevant fields have been de-identified, in the client service, implement the logic to save the data to the target storage. This could be a Cloud Storage service or your on-premises SAP system.

## What's next

  * To deploy the example solution explained in this guide with minimal effort, use the code sample provided in [GitHub](https://github.com/GoogleCloudPlatform/abapsdk-btp-samples/tree/main/src/zgoog_sdk_btp_dlp_recipe).

  * Explore the full range of [transformation methods](https://docs.cloud.google.com/sensitive-data-protection/docs/transformations-reference) available in the DLP API to find the best fit for your specific business needs.

  * To learn about ABAP SDK for Google Cloud, see [Overview of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/overview).

  * If you need help resolving problems with the ABAP SDK for Google Cloud, then do the following:

    * Refer to the [ABAP SDK for Google Cloud troubleshooting guide](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/troubleshooting).
    * Ask your questions and discuss the ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).
    * Collect all available diagnostic information and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).



## Contributors

Author: [Sanchita Mohta](https://www.linkedin.com/in/sanchita-mohta/) | SAP Application Engineer

Other contributor: [Vikash Kumar](https://www.linkedin.com/in/vikash-kumar-91923636/) | Technical Writer

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
