---
url: https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/gemini-powered-business-rule-engine/
title: Gemini-powered business rule engine for SAP \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:47.417125+00:00
---

# Gemini-powered business rule engine for SAP  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/gemini-powered-business-rule-engine/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Gemini-powered business rule engine for SAP Stay organized with collections  Save and categorize content based on your preferences. 

This document describes a reference architecture for building a business rule engine powered by Large Language Models (LLMs) such as Gemini, to automate decision-making within your SAP business applications. It uses the various integration capabilities of [ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/overview). 

The intended audience for this document includes ABAP developers, SAP solution architects, and cloud architects. The document assumes a basic understanding of [ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/overview), [Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/overview), and basic [introduction to LLMs](https://www.cloudskillsboost.google/course_templates/539).

## What is a business rule engine (BRE)?

A [business rule engine](https://en.wikipedia.org/wiki/Business_rules_engine) (BRE) is a software system that lets you define, deploy, and execute business rules. These rules are essentially logic statements that dictate how your business operates. Instead of hardcoding the business rules into your applications, a BRE externalizes the logic statements, making it efficient to manage and modify the rules.

A Gemini-powered BRE uses the advanced language processing and reasoning capabilities of Gemini, Google's next-generation AI model, to automate decision-making based on a repository of engineered prompts that function as business rules. These prompts, crafted with specific instructions and expected output formats, guide Gemini in analyzing data, identifying patterns, and making decisions in a manner consistent with predefined business logic.

## Architecture

The following diagram shows a reference architecture for creating a Gemini-powered BRE for SAP applications:

![Gemini-powered business rule engine for SAP](https://docs.cloud.google.com/static/sap/docs/architectures/architecture-images/abap-sdk/abap-sdk-gemini-powered-business-rule-engine-sap.svg)

This reference architecture includes the following components:

Component | Subsystem | Details  
---|---|---  
1 | SAP ERP | An SAP ERP system such as SAP S/4HANA, which uses a Gemini-powered BRE to derive insights for automated decision-making. Based on your use case, you provide the BRE module with a rule ID and necessary input data.   
2 | BRE module | The BRE module uses the ABAP SDK for Google Cloud to retrieve configured rules from Cloud Storage and calls Gemini by using the Agent Platform SDK for ABAP to process the rules.  
3 | Rules Repository | Stores rules (engineered prompts) in Cloud Storage as text files, such as `.txt` or `.prompt`, with a consistent naming convention. For example, `RiskShiftingClause.prompt`. For structured management of engineered prompts, you can also consider using a database such as Cloud SQL.  
4 | Rule Processor | The Agent Platform SDK for ABAP sends the input data (for example, delivery instructions) and the retrieved rule (prompt) to Gemini. Gemini processes the prompt and the input data, performs analysis, and returns the results in the specified format.  
  
## Products used

This reference architecture uses the following Google Cloud products:

  * [ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/overview): Helps you develop ABAP applications that connect your SAP systems to Google Cloud services, such as Cloud Storage.

  * [Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/overview): Lets you use Google Cloud's Agent Platform within your SAP environment. This simplifies building AI-powered features in your SAP applications.

  * [Cloud Storage](https://docs.cloud.google.com/storage/docs/introduction): A cloud service for storing and accessing any amount of data online.

  * [Agent Platform](https://docs.cloud.google.com/vertex-ai/docs/start/introduction-unified-platform): Lets you build, deploy, and scale machine learning models for various applications.




## Use case

Consider a scenario where your company receives inbound purchase orders (PO) as PDFs and uses an automated process to generate sales orders in SAP. You need to update this process to identify and mitigate _risk-shifting clauses_ found in the delivery comments of incoming POs.

Risk-shifting clauses in a contract are terms that transfer risk from one party to another. Failing to identify and address these clauses can blindside your company with unexpected costs, legal battles, and reputational damage.

The following is an example of a risk-shifting clause written in the delivery comment of a PO document.

"Seller warrants that the products will be free from defects for a period of ten years from the date of delivery."

You need to write a rule for the following:

  * Identify and categorize the risk-shifting clauses.
  * Provide an explanation on why it is considered as a potential red flag.
  * Provide recommendations on how to mitigate the risk.



You can build a BRE with Gemini to generate an intelligent JSON response, which enables your SAP business application to take automated decisions, trigger any process rejection, or initiate downstream human validations.

**Note:** This document does not showcase capabilities of [Retrieval-Augmented Generation (RAG)](https://cloud.google.com/use-cases/retrieval-augmented-generation) to ground the rule (prompt) to enterprise specific content, such as organization's legal policies. You can achieve this by adding a context retrieval module in the architecture and by passing this module as a context when calling Gemini. For illustrative purposes, Gemini pre-trained capabilities are used in this document to provide issue specific explanation and recommendation.

### Sample risk-shifting clauses

The following table lists the sample risk-shifting clauses that can be found in inbound purchase orders:

Issue category | Example clause (Delivery instructions) | Potential issues  
---|---|---  
Indemnification overreach | Seller shall indemnify the buyer against all claims, losses, damages, and expenses, including but not limited to attorney's fees, arising from or related to the products. | This could be problematic if it's too broad and holds the seller liable for unforeseen events or customer misuse.  
Confidentiality overextension | All information disclosed by buyer to seller, including but not limited to pricing, specifications, and marketing plans, shall be considered confidential and proprietary to buyer. | This could hinder the seller's ability to use general industry knowledge or work with other clients.  
Ambiguous governing law | This agreement shall be governed by the laws of the location, for example, the State of Illinois. | This could lead to conflicts of law if the buyer and seller are in different jurisdictions.  
Force majeure limitation | Seller shall not be excused from performance under this agreement due to any force majeure event, including acts of God, war, or terrorism. | This could hold the seller liable for events beyond their control.  
Intellectual property ambiguity | All intellectual property rights in the products shall belong to the buyer. | This could be a red flag if the seller is from a sanctioned country or has ties to one.  
  
### Sample engineered prompt

The section describes a sample prompt engineered by using the RTF framework. The RTF framework in prompt engineering stands for Role, Task, and Format. It's an effective way to structure your prompts to get better and more consistent results from LLMs such as Gemini.

  * **Role** : Persona that you want the LLM to adopt, such as "sales expert" or "legal advisor".
  * **Task** : Specific action for the LLM, such as, "summarize this text" or "analyze something".
  * **Format** : Desired output structure, such as list or JSON.



To learn about common prompting strategies that you can use to affect the model's responses, see [Overview of prompting strategies](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/prompts/prompt-design-strategies)

The following prompt acts as a _defining rule_ to helps Gemini identify issues such as the risk-shifting clause:

RTF framework  
---  
**Prompt:**
    
    
    **Role**
    
    You are a legal advisor for my company.
    
    **Task**
    
    Analyze the below delivery instruction on a purchase order from my
    customer and let me know if it could cause any issues to my company.
    
    **Format**
    
    Respond to me in plain text JSON format with 4 fields.
    
    Field 1 should be "issue" with possible values Yes or No.
    
    Field 2 should be "issueCategory" with possible values Indemnification
    Overreach, Unilateral Termination Clause, Confidentiality Overextension,
    Unreasonable Warranty, Ambiguous Governing Law, Unclear Dispute Resolution,
    Force Majeure Limitation, Unbalanced Liability,
    Intellectual Property Ambiguity, Compliance with Sanctions, Others or None.
    
    Field 3 should be "explanation" - use this field to give a short
    explanation for your response on Field 1.
    
    Field 4 should be "recommendation" - use this field to give a short
    recommendation of how to mitigate such issues.
    
    Do not include backticks in the response.
    

**Input data:**
    
    
    
    Delivery Instruction: "Seller warrants that the products will be free
    from defects for a period of ten years from the date of delivery."
    
    

**Response:**
    
    
    {
      "issue": "Yes",
      "issueCategory": "Unreasonable Warranty",
      "explanation":   "A ten-year warranty is significantly longer than
      industry standard for most products. This could expose your company to
      substantial financial risk if issues arise with the products years
      down the line.",
      "recommendation": "Negotiate a shorter warranty period that aligns
      with industry standards and your product's expected lifespan.
      Offer extended warranty options at an additional cost if the
      customer requires longer coverage."
    }
      
  
You can store this prompt in a repository such as Cloud Storage. The input data can be passed by the SAP transactions to the BRE module.

You then use the ABAP SDK for Google Cloud to retrieve the prompt from Cloud Storage and pass it to Gemini for execution, by using the Agent Platform SDK for ABAP.

The sample JSON response is generated by Gemini for this risk-shifting clause example.

The following sample code shows how to retrieve the rules and use it in your code. It assumes that you're implementing a BRE service as an ABAP class, such as `lcl_bre`.
    
    
     DATA(lo_bre) = NEW lcl_bre( iv_key_name  = 'CLIENT_KEY'
                                 iv_model_key = 'MODEL_KEY' ).
    
     " Sample delivery text
     DATA(lv_delivery_text) = |Seller warrants that the products will be free from defects for| &&
                              |a period of ten years from the date of delivery.|.
    
     " Execute the rule for identifying Risk-Shifting clauses.
     DATA(lv_response) = lo_bre->execute_rule( iv_rule_id = 'RiskShiftingClause-Rule-001.prompt'
                                               iv_data    = lv_delivery_text ).
     " JSON response
     cl_demo_output=>display_json( lv_response ).
    

Replace the following:

  * `CLIENT_KEY`: The client key configured for authentication to Agent Platform and Cloud Storage.
  * `MODEL_KEY`: The model key name to access the LLM, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).



The `execute_rule` method performs the following:

  1. Reads the rule file from Cloud Storage by using the [`/GOOG/CL_STORAGE_V1`](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_storage_v1) class.

  2. Sends the processing rules to Gemini, which is set as instruction to the model, by using the [`/GOOG/CL_GENERATIVE_MODEL`](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/invoke-gemini-models#send-request-gemini) class. The model then generates a JSON response.




The following is the complete sample code for your reference:
    
    
    REPORT zra_bre_example.
    
    " Local class definition
    CLASS lcl_bre DEFINITION FINAL.
    
      PUBLIC SECTION.
        METHODS constructor
          IMPORTING iv_key_name  TYPE /goog/keyname
                    iv_model_key TYPE /goog/model_key
          RAISING   /goog/cx_sdk.
    
        METHODS convert_xstring_to_string
          IMPORTING iv_xstring       TYPE xstring
          RETURNING VALUE(iv_string) TYPE string.
    
        METHODS execute_rule
          IMPORTING iv_rule_id              TYPE string
                    iv_data                 TYPE string
          RETURNING VALUE(rv_response_text) TYPE string
          RAISING   /goog/cx_sdk.
    
      PRIVATE SECTION.
        DATA mo_storage TYPE REF TO /goog/cl_storage_v1.
        DATA mo_model   TYPE REF TO /goog/cl_generative_model.
    ENDCLASS.
    
    " Local class implementation
    CLASS lcl_bre IMPLEMENTATION.
      METHOD constructor.
        mo_storage = NEW /goog/cl_storage_v1( iv_key_name = iv_key_name ).
        mo_model = NEW /goog/cl_generative_model( iv_model_key = iv_model_key ).
      ENDMETHOD.
    
      METHOD convert_xstring_to_string.
    DATA lv_file_length TYPE i.
        DATA lt_bin_data    TYPE STANDARD TABLE OF char1024.
    
        " Call function module to convert xstring to binary format
        CALL FUNCTION 'SCMS_XSTRING_TO_BINARY'
          EXPORTING buffer        = iv_xstring
          IMPORTING output_length = lv_file_length
          TABLES    binary_tab    = lt_bin_data.
        IF sy-subrc <> 0.
          " Handle error
        ENDIF.
    
        " Call function module to convert from binary to string format
        CALL FUNCTION 'SCMS_BINARY_TO_STRING'
          EXPORTING input_length = lv_file_length
          IMPORTING text_buffer  = iv_string
          TABLES    binary_tab   = lt_bin_data.
        IF sy-subrc <> 0.
          " Handle error
        ENDIF.
      ENDMETHOD.
    
      METHOD execute_rule.
        DATA lv_xdata       TYPE xstring.
        DATA lv_instruction TYPE string.
    
        " Get the rule file from rule repository(cloud storage)
        mo_storage->add_common_qparam( iv_name  = 'alt'
                                       iv_value = 'media' ).
    
        mo_storage->get_objects( EXPORTING iv_p_bucket = 'gemini-bre-repo'
                                           iv_p_object = iv_rule_id
                                 IMPORTING es_output   = DATA(ls_output)
                                           ev_ret_code = DATA(lv_ret_code)
                                           ev_err_text = DATA(lv_err_text)
                                           es_err_resp = DATA(ls_err_resp)
                                           es_raw      = lv_xdata ).
    
        IF mo_storage->is_success( lv_ret_code ) = abap_true.
          " Set the instruction for Gemini as per the configured rule
          lv_instruction = convert_xstring_to_string( iv_xstring = lv_xdata ).
        ELSE.
          " Handle error
        ENDIF.
    
        " Set the text to be analyzed
        DATA(lv_prompt) = |Please analyze the Delivery Instruction:{ cl_abap_char_utilities=>newline }{ iv_data }|.
    
        " Call Gemini to process the rule and identify Risk-Shifting clauses
        rv_response_text = mo_model->set_system_instructions( iv_text = lv_instruction
                          )->add_safety_settings( iv_harm_category        = 'HARM_CATEGORY_DANGEROUS_CONTENT'
                                                  iv_harm_block_threshold = 'BLOCK_NONE'
                          )->generate_content( iv_prompt_text = lv_prompt
                          )->get_text( ).
      ENDMETHOD.
    ENDCLASS.
    
    START-OF-SELECTION.
      TRY.
          DATA(lo_bre) = NEW lcl_bre( iv_key_name  = 'DEMO_AIPLATFORM'
                                      iv_model_key = 'gemini-flash' ).
    
          " Sample delivery text
     DATA(lv_delivery_text) = |Seller warrants that the products will be free from defects for| &&
                                 |a period of ten years from the date of delivery.|.
    
          " Execute the rule for identifying Risk-Shifting clauses.
          DATA(lv_response) = lo_bre->execute_rule( iv_rule_id = 'RiskShiftingClause-Rule-001.prompt'
                                                    iv_data    = lv_delivery_text ).
          " JSON response
          cl_demo_output=>display_json( lv_response ).
    
        CATCH /goog/cx_sdk INTO DATA(lo_exception).
          DATA(lv_msg) = lo_exception->get_text( ).
          " Handle error
      ENDTRY.
    

## Design considerations

This section provides guidance to help you use this reference architecture to develop one or more architectures that help you to meet your specific requirements for security, privacy, compliance, cost, and performance.

### Security, privacy, and compliance

Security and compliance are shared responsibilities. For detailed information, see [Gemini Enterprise Agent Platform shared responsibility](https://docs.cloud.google.com/vertex-ai/docs/shared-responsibility).

For information about how Gemini uses your data, see [How Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

### Cost

For an estimate of the cost of the Google Cloud resources like Cloud Storage, use the [Google Cloud Pricing Calculator](https://cloud.google.com/products/calculator/).

For information about Agent Platform API pricing, see [Gemini Enterprise Agent Platform pricing](https://cloud.google.com/vertex-ai/pricing).

## Design alternative

While this document focuses on the on-premises or any cloud edition of ABAP SDK for Google Cloud, you can achieve similar results by using the SAP BTP edition of ABAP SDK for Google Cloud. The Agent Platform SDK for ABAP is not available for the SAP BTP environment, but you can use the code sample provided in this document for the on-premises edition of the SDK, adjust it, and build similar solutions within your SAP BTP environment.

## What's next

  * To learn about the Agent Platform SDK for ABAP, see [Overview of the Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/overview).
  * To learn about the ABAP SDK for Google Cloud, see [Overview of the ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/overview).
  * If you need help resolving problems with the ABAP SDK for Google Cloud, then do the following:

    * Refer to the [ABAP SDK for Google Cloud troubleshooting guide](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/troubleshooting).
    * Ask your questions and discuss the ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).
    * Collect all available diagnostic information and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).



## Contributors

Authors: [Ameya Suvarna](https://www.linkedin.com/in/ameyasuvarna/) | SAP Application Engineer Team Lead

Other contributors: [Vikash Kumar](https://www.linkedin.com/in/vikash-kumar-91923636/) | Technical Writer

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
