---
url: https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/google-chat-apps-for-sap/
title: Send SAP notifications to Google Chat \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:58:49.362219+00:00
---

# Send SAP notifications to Google Chat  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/google-chat-apps-for-sap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Send SAP notifications to Google Chat Stay organized with collections  Save and categorize content based on your preferences. 

This document describes a reference architecture for building [Google Chat apps](https://developers.google.com/workspace/chat/overview) for SAP, by using the [on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/all-guides). With Chat apps, you can bring your SAP processes and workflows into Google Chat, enabling users to receive notifications such as alarm reporting, workflow alerts, system alerts, and job completion updates within their Google Workspace.

The intended audience for this document includes ABAP developers, SAP solution architects, and cloud architects. This document assumes that you're familiar with the [Chat apps](https://developers.google.com/workspace/chat/overview) available in [Google Workspace](https://developers.google.com/workspace/guides/get-started).

## Architecture

The following diagram shows a reference architecture for implementing one-way Chat apps for SAP that can send messages to a Chat space from an SAP ERP system:

![Chat apps for SAP](https://docs.cloud.google.com/static/sap/docs/architectures/architecture-images/abap-sdk/abap-sdk-one-way-chat-apps-for-sap.svg)

This reference architecture includes the following components:

# | Component | Details  
---|---|---  
1 | SAP processes or transactions | Any SAP process or transaction that needs to send user notifications. It's the starting point for triggering communication through Google Chat.   
2 | ABAP SDK for Google Cloud | Acts as a bridge between SAP systems and Google Cloud, enabling secure HTTPS communication with the Google Chat API.  
3 | Google Chat app project | The Google Cloud project where you've enabled the Google Chat API and configured your Chat app.  
4 | Chat space | A dedicated room within Google Chat where your SAP system can communicate with users. The Chat apps reside in this space, providing a real-time stream of information from your SAP systems through the Google Chat API.  
  
## Products used

This reference architecture uses the following Google products:

  * [ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/overview): Helps you develop ABAP applications that connect your SAP systems to Google Cloud services, such as Google Chat.
  * [Google Chat](https://developers.google.com/workspace/chat/overview): Helps you create interactive and collaborative Chat apps, enhancing communication and productivity.



## Use cases

One-way Chat apps are non-interactive and let you send messages to the Chat space users, but the users can't respond to the Chat apps. The following diagram illustrates the chat pattern for one-way Chat apps:

![Chat apps pattern](https://docs.cloud.google.com/static/sap/docs/architectures/architecture-images/abap-sdk/abap-sdk-ref-arch-chat-pattern.png)

The following list shows some use cases of Google Chat for SAP:

  * **Workflow event notification** : You can send messages to the Chat apps for different steps involved in the workflow process to alert a specific set of users present in a Chat space. For example, a purchase order is approved or rejected by a user.

  * **System alerts** : You can send alerts to a Chat space meant for the system admins to alert them of various system thresholds being reached. For example, disk space usage, long-running operations, cache locks, or license expiry.

  * **Job status updates** : You can send updates for long-running custom jobs to a set of users who are waiting for those jobs to complete and take up post-processing operations.




## Design considerations

When you design Chat apps for your use cases, there are several factors that might influence your design decisions. This section provides guidance to help you use this reference architecture to develop architectures that help you to meet your specific requirements for security, privacy, compliance, and cost.

### Google Chat app configuration

  * **Chat app name** : Provide a clear and meaningful name for your Chat app. For a seamless user experience, make sure your Chat app's name accurately reflects its functionalities or the services it integrates with.

  * **Time zones** : A Chat space can be shared by members belonging to various time zones. Therefore, configuring Chat apps to transmit messages at a time that is convenient for all users of the space is essential. Alternatively, for important alerts or notifications, you can designate members to Chat spaces with a shared time zone and build logic to determine which space the Chat app can send messages to.




### Security, privacy, and compliance

To maintain confidentiality, it is crucial to implement stringent controls over the sharing of sensitive information, such as customer contact details, IBAN, or other need-to-know data within Chat spaces. Additionally, when new users are added to Chat spaces, where the Chat apps are added, it is essential to establish clear regulations to ensure appropriate management of this activity.

You can also consider using [Cloud Data Loss Prevention (DLP) API](https://docs.cloud.google.com/sensitive-data-protection/docs/reference/rest) to desensitize the message contents. For information about how to protect sensitive enterprise data in SAP by using the DLP API, see [Data protection in SAP with the DLP API](https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/data-protection-with-cloud-dlp).

For security, ensure that Google Workspace admins follow the [Google recommended best practices](https://support.google.com/a/answer/7587183#zippy=%2Cgoogle-chat-and-classic-hangouts-google-workspace-only).

### Quotas and limits

Google Chat API is a shared service therefore quotas and limitations are applicable. If you exceed a quota, then you receive a `429: Too many requests` HTTP status code response. For more information about quotas and limits, see [Usage limits](https://developers.google.com/workspace/chat/limits).

Google Chat API itself does not have any usage fees, however, Google Chat is a Google Workspace product. Google Workspace, a suite of bundled productivity tools, encompasses Gmail, Docs, Sheets, Slides, Google Chat apps, and more. Its pricing structure is holistic, meaning that you cannot select and purchase individual components. For more information about pricing, see [Google Workspace Pricing](https://workspace.google.com/pricing.html).

## Design alternative

While this document focuses on the on-premises or any cloud edition of ABAP SDK for Google Cloud, you can achieve similar results by using the [SAP BTP edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/all-guides). You can adapt the provided resources to build similar solutions within your SAP BTP environment.

## Before you begin

Before implementing a solution based on this reference architecture, make sure that you have completed the following prerequisites:

  * You have a Business or Enterprise [Google Workspace](https://support.google.com/a/answer/6043576) account with access to [Google Chat](https://workspace.google.com/products/chat/).

  * You have a Google Cloud account and project. Each Chat app requires its own Google Cloud project. That means you can configure only a single Chat app in one Google Cloud project.

  * Billing is enabled for your project. For information about how to confirm that billing is enabled for your project, see [Verify the billing status of your projects](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled).

  * The [on-premises or any cloud edition of ABAP SDK for Google Cloud is installed and configured](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config).

  * The [Google Chat API](https://console.cloud.google.com/project/_/apis/library/chat.googleapis.com) is enabled in your Google Cloud project.




### Configure the Google Chat app

  1. In the Google Cloud console, search for "Google Chat API" and click **Google Chat API** , then click **Manage**.

[Go to Chat API](https://console.cloud.google.com/apis/api/chat.googleapis.com/hangouts-chat)

  2. Click **Configuration** and set up the Google Chat app:

     1. In **App name** , enter `Quickstart SAP App`.
     2. In **Avatar URL** , enter `https://developers.google.com/chat/images/quickstart-app-avatar.png`.
     3. In **Description** , enter `Quickstart app for SAP`.
  3. Disable interactive features.

  4. Click **Save**.




### Set up authentication for Google Chat apps

You can authenticate to Google Chat apps in two ways: as an app itself or as a user.

When your app needs to perform automated tasks, such as sending system notifications without direct user interaction, it uses a service account. If you want your app to act on behalf of a user, such as sending a message as that specific person, then you need user authentication. This dual authentication approach offers flexibility and control over how your app interacts with Google Chat.

The ABAP SDK for Google Cloud lets you set up both kinds of authentication. For information about how to setup authentication for Google Chat apps, see:

  * Authenticate as a Google Chat app: [Authenticate by using access tokens](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-access-token) or [Authenticate by using JSON Web Tokens](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-jwt)
  * Authenticate and authorize as a Google Chat user: [Authenticate to Google Workspace APIs by using OAuth 2.0 client credentials](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-oauth-client-credentials)



For information about Google Chat API methods and their supported authorization scopes, see [Authenticate and authorize Chat apps and Google Chat API requests](https://developers.google.com/workspace/chat/authenticate-authorize#asynchronous-chat-calls).

The reference architecture explained in this document uses authentication as a Chat app and uses access tokens for authentication.

To set up authentication as a Chat app, perform the following steps:

  1. In the Google Cloud console, [configure the OAuth consent screen and choose scopes](https://developers.google.com/workspace/guides/configure-oauth-consent).
  2. In the Google Cloud console, [create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating).
  3. Optional: Assign roles to your service account to grant access to your Google Cloud project resources. For more information, see [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).
  4. In the SAP system, configure a client key with the following details: 

Field | Description  
---|---  
**Google Cloud Key Name** | Specify a name of the client key configuration. For example, `ABAP_SDK_CHAT`.  
**Google Cloud Service Account Name** | Specify the name of the service account to which you have granted permissions to access the Google Chat API. For example, `sap-example-svc-acct@example-project-123456.iam.gserviceaccount.com`.  
**Google Cloud Scope** | Specify the API access scope: `https://www.googleapis.com/auth/chat.bot`.   
**Google Cloud Project Identifier** | Specify the ID of the Google Cloud project that contains your enabled Google Chat API.  
**Command name** | Leave this field blank.  
**Authorization Class** | Specify the authorization class, as appropriate:
     * For authentication by using access tokens: `/GOOG/CL_AUTH_GOOGLE`
     * For authentication by using JWT: `/GOOG/CL_AUTH_JWT`  
**Token Caching** |  The flag that determines whether or not the access tokens retrieved from Google Cloud are cached. We recommend that you enable token caching after you are done configuring and testing your connection to Google Cloud. For more information about token caching, see [Enable token caching](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config#token_caching).  
**Token Refresh Seconds** | The amount of time, in seconds, before an access token expires and must be refreshed. The default value is `3500`.  
**Authorization Parameter 1** | Leave this field blank.  
**Authorization Parameter 2** | Leave this field blank.  



For information about detailed steps to set up authentication, see [Authenticate by using access tokens](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-access-token) or [Authenticate by using JSON Web Tokens](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-jwt).

### Add the Google Chat app to spaces

  1. Open your Google Chat apps or Gmail app.
  2. Add the Chat app to a Chat space. For information about how to do this, see [Add apps to conversations or spaces](https://support.google.com/chat/answer/7655820).



## Send a message from your ABAP environment

Google Chat and Chat apps use a JSON-based message format, with each message containing details such as user ID, style, and content. Chat apps can send the following types of messages:

  * **Text messages** : Text messages contain plain text content to convey basic information.
  * **Card messages** : Card messages define the format, content, and behavior of cards to be displayed in a space. For example, a card message can include a button with a link that opens a dialog to collect information from a user.



For more information about Google Chat messages, see [Google Chat messages overview](https://developers.google.com/workspace/chat/messages-overview).

To send messages from an SAP system to a Chat space by using the ABAP SDK for Google Cloud, you use the `CREATE_MESSAGES` method of the [`/GOOG/CL_CHAT_V1`](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_chat_v1) class.

### Send a text message

The following code sample illustrates how to send a text message from an SAP system to a Chat space:
    
    
    REPORT zsend_text_message.
    
    DATA lv_client_key TYPE /goog/keyname.
    DATA ls_input      TYPE /goog/cl_chat_v1=>ty_072.
    DATA lv_space_id   TYPE string.
    
    lv_client_key = 'CLIENT_KEY'.
    ls_input-text = 'TEXT_MESSAGE'.
    lv_space_id   = 'SPACE_ID'.
    
    TRY.
        DATA(lo_chat) = NEW /goog/cl_chat_v1( iv_key_name = lv_client_key ).
      CATCH /goog/cx_sdk INTO DATA(lo_excp).
        " Handle exception here
    ENDTRY.
    
    TRY.
        lo_chat->create_messages( EXPORTING iv_p_spaces_id = lv_space_id
                                            is_input       = ls_input
                                  IMPORTING ev_ret_code    = DATA(return_code)
                                            ev_err_text    = DATA(error_text)
                                            es_err_resp    = DATA(err_resp) ).
      CATCH /goog/cx_sdk INTO lo_excp.
        " Handle exception here
    ENDTRY.
    
    IF /goog/cl_chat_v1=>is_success( iv_code = return_code ) = abap_true.
      " Handle success here
    ELSE.
      " Handle error here
    ENDIF.
    

Replace the following:

  * `CLIENT_KEY`: The client key configured for authentication.
  * `TEXT_MESSAGE`: A text message to be sent to the Chat space.
  * `SPACE_ID`: The unique identifier ID of the Chat space. To locate the Chat space ID, open Google Chat space in your web browser. You can find the ID in the URL, as illustrated in the following screenshot:

![Chat apps space ID](https://docs.cloud.google.com/static/sap/docs/architectures/architecture-images/abap-sdk/abap-sdk-ref-arch-chat-space-id.png)




### Send a card message

Cards provide a visually appealing and interactive way to present information, enhancing the overall user experience. They can include elements such as titles, images, buttons, and more, enabling users to engage with the content directly within the chat interface. For example, a purchase order workflow card might include the following information:

  * Purchase Order Number
  * Document Date
  * Document Type
  * Supplier
  * Shipping Type



For card development with the ABAP SDK for Google Cloud, use the custom interface `ZGOOG_IF_CHAT_CARDS_V2`, from the [GitHub repository](https://github.com/GoogleCloudPlatform/google-cloud-abap/tree/main/abap-sdk/ZGOOG_SDK_RECIPES/ZGOOG_SDK_CHAT_RECIPE). This custom interface contains the ABAP Types required to create cards. You can build cards such as the following order workflow example card:

![Chat apps card](https://docs.cloud.google.com/static/sap/docs/architectures/architecture-images/abap-sdk/abap-sdk-ref-arch-chat-msg-card.png)

For more information about designing card messages, see [Build cards for Google Chat apps](https://developers.google.com/workspace/chat/design-components-card-dialog).

The following code sample illustrates how to send a card message from an SAP system to a Chat space:
    
    
    REPORT zsend_card_message.
    
    DATA lv_client_key TYPE /goog/keyname.
    DATA ls_input      TYPE /goog/cl_chat_v1=>ty_072.
    DATA lv_space_id   TYPE string.
    DATA ls_widget     TYPE zgoog_if_chat_cards_v2=>ty_widget.
    DATA ls_section    TYPE zgoog_if_chat_cards_v2=>ty_sections.
    DATA ls_card_v2    TYPE zgoog_if_chat_cards_v2=>ty_cards_v2.
    DATA ls_card       TYPE /goog/cl_chat_v1=>ty_012.
    DATA ls_rb         TYPE zgoog_if_chat_cards_v2=>ty_selection_item.
    DATA ls_button     TYPE zgoog_if_chat_cards_v2=>ty_button.
    DATA ls_param      TYPE zgoog_if_chat_cards_v2=>ty_action_parameters.
    
    lv_client_key = 'CLIENT_KEY'.
    lv_space_id   = 'SPACE_ID'.
    
    TRY.
    
        DATA(lo_chat) = NEW /goog/cl_chat_v1( iv_key_name = lv_client_key ).
      CATCH /goog/cx_sdk INTO DATA(lo_excp).
        " Handle exception here
    ENDTRY.
    
    " Building the Card Structure
    
    " Set the header
    ls_card_v2-header = VALUE zgoog_if_chat_cards_v2=>ty_header(
                                  title     = 'Purchase Order Workflow - Level 2 Approval Alert!'
                                  subtitle  = 'PO Number: 8700000034'
                                  image_url = 'https://developers.google.com/chat/images/quickstart-app-avatar.png' ).
    
    " Create sections
    ls_section-header = 'Purchase Order Details'.
    
    ls_widget-decorated_text = VALUE zgoog_if_chat_cards_v2=>ty_decorated_text(
                                         icon = VALUE zgoog_if_chat_cards_v2=>ty_icon( known_icon = 'INVITE' )
                                         text = 'Document Date: 2024-10-23' ).
    ls_section-widgets = VALUE #( ( ls_widget ) ).
    CLEAR ls_widget.
    
    ls_widget-decorated_text = VALUE zgoog_if_chat_cards_v2=>ty_decorated_text(
        icon = VALUE zgoog_if_chat_cards_v2=>ty_icon(
                         material_icon = VALUE zgoog_if_chat_cards_v2=>ty_material_icon( name = 'category' ) )
        text = 'Document Type: Standard PO'  ).
    
    ls_section-widgets = VALUE #( BASE ls_section-widgets
                                  ( ls_widget ) ).
    CLEAR ls_widget.
    
    ls_widget-decorated_text = VALUE zgoog_if_chat_cards_v2=>ty_decorated_text(
        icon = VALUE zgoog_if_chat_cards_v2=>ty_icon(
                         material_icon = VALUE zgoog_if_chat_cards_v2=>ty_material_icon( name = 'conveyor_belt' ) )
        text = 'Supplier: 5300000061 - Cymbal Industries'  ).
    
    ls_section-widgets = VALUE #( BASE ls_section-widgets
                                  ( ls_widget ) ).
    CLEAR ls_widget.
    
    ls_widget-decorated_text = VALUE zgoog_if_chat_cards_v2=>ty_decorated_text(
                                         icon = VALUE zgoog_if_chat_cards_v2=>ty_icon( known_icon = 'TRAIN' )
                                         text = 'Shipping Type: RAIL' ).
    ls_section-widgets = VALUE #( BASE ls_section-widgets
                                  ( ls_widget ) ).
    CLEAR ls_widget.
    
    ls_widget-decorated_text = VALUE zgoog_if_chat_cards_v2=>ty_decorated_text( text = 'Approved By: User-Name' ).
    ls_section-widgets = VALUE #( BASE ls_section-widgets
                                  ( ls_widget ) ).
    CLEAR ls_widget.
    
    ls_section-widgets = VALUE #( BASE ls_section-widgets
                                  ( ls_widget ) ).
    
    ls_card_v2-sections = VALUE #( ( ls_section ) ).
    
    ls_card-card = REF #( ls_card_v2 ).
    ls_input-cards_v2 = VALUE #( (  ls_card ) ).
    
    TRY.
        lo_chat->create_messages( EXPORTING iv_p_spaces_id = lv_space_id
                                            is_input       = ls_input
                                  IMPORTING es_output      = DATA(ls_output)
                                            ev_ret_code    = DATA(lv_ret_code)
                                            ev_err_text    = DATA(lv_err_text)
                                            es_err_resp    = DATA(ls_err_resp) ).
      CATCH /goog/cx_sdk INTO lo_excp.
        " Handle exception here
    ENDTRY.
    
    IF lo_chat->is_error( lv_ret_code ).
      " Handle error here
    ELSE.
      " Handle success here
    ENDIF.
    
    

Replace the following:

  * `CLIENT_KEY`: The client key configured for authentication.
  * `SPACE_ID`: The unique identifier ID of the Chat space. To locate the Chat space ID, open Google Chat space in your web browser. You can find the ID in the URL, as illustrated in the following screenshot:

![Chat apps space ID](https://docs.cloud.google.com/static/sap/docs/architectures/architecture-images/abap-sdk/abap-sdk-ref-arch-chat-space-id.png)




## What's next

  * To deploy the example solution explained in this guide with minimal effort, use the code sample provided on [GitHub](https://github.com/GoogleCloudPlatform/google-cloud-abap/tree/main/abap-sdk/ZGOOG_SDK_RECIPES/ZGOOG_SDK_CHAT_RECIPE).

  * For information about Google Workspace products, see [common questions when considering Google Workspace](https://workspace.google.com/faq).

  * In addition to sending SAP notifications to Google Chat, if you need to interact with SAP workflows from Google Chat, then see the reference architecture [Interact with SAP workflows from Google Chat](https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/interactive-google-chat-apps-for-sap).

  * If you need help resolving problems with the ABAP SDK for Google Cloud, then do the following:

    * Refer to the [ABAP SDK for Google Cloud troubleshooting guide](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/troubleshooting).
    * Ask your questions and discuss the ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).
    * Collect all available diagnostic information and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).



## Contributors

Author: [Satish Inamdar](https://www.linkedin.com/in/satish-inamdar-14450a35/) | SAP Application Engineer

Other contributor: [Vikash Kumar](https://www.linkedin.com/in/vikash-kumar-91923636/) | Technical Writer

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
