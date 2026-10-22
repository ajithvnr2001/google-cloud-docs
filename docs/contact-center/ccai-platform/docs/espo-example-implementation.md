---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/espo-example-implementation/
title: EspoCRM reference implementation \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:28.386819+00:00
---

# EspoCRM reference implementation  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/espo-example-implementation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  EspoCRM reference implementation Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an example integration with Contact Center AI Platform (CCAI Platform) custom CRM using EspoCRM. EspoCRM is a free, open-source CRM application that helps businesses manage sales, marketing, and customer support with a customizable interface. It offers features like contact management, activity tracking, sales automation, and inventory management, with options for self-hosting or cloud deployment.

To set up your own instance of EspoCRM, see the [EspoCRM installation page](https://docs.espocrm.com/administration/installation/).

## Before you begin

Do the following:

  * Configure your firewall to permit traffic from CCAI Platform.

  * Create an API user in your EspoCRM instance—for example, `google_integration_user`. For more information, see [API](https://docs.espocrm.com/administration/users-management/#api) in the EspoCRM Documentation.

  * Create a role in your EspoCRM instance with the **Create** , **Read** , and **Update** actions that accesses the following:

    * **Contacts** : to find or create callers
    * **Cases** : to search for and log tickets

For more information, see [Role Management](https://docs.espocrm.com/administration/roles-management/) in the ExpoCRM documentation.


**Important:** Be sure that all of the API endpoints that you configure use a valid TLS certificate.

## Configure a connection from EspoCRM to CCAI Platform

To configure a connection from EspoCRM to CCAI Platform, follow these steps:

  1. In the CCAI Platform portal, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click **Menu**.
  2. For **Agent Platform** , select **Custom CRM**.
  3. Click the **Display CRM in CCAI Platform portal Portal** toggle to the on position.
  4. In the **Display URL** field, enter the URL to embed in the CCAI Platform portal–for example, `https://YOUR_ESPO_DOMAIN/#Case/view/{RECORD_ID}`.
  5. For **CRM lookup method** , select **Generic API**.
  6. To authenticate using a custom header, do the following: 
     1. In the **Authentication Method** section, select **Custom Header**.
     2. Click **Add field**. The **Add Field** dialog appears. 
        1. In the **Field Key** field, enter `X-Api-Key`.
        2. In the **Field Value** field, enter the API key generated when you created an API user in your EspoCRM.
        3. Click **Save**.
  7. To set the CRM lookup URL, do the following: 
     1. In the **CRM lookup URL** section, in the **Record lookup URL** field, enter the URL to look up a record—for example, `https://YOUR_ESPO_DOMAIN/#Case/view/{RECORD_ID}`.
     2. In the **Account lookup URL** field, enter the URL to look up an account—for example, `https://YOUR_ESPO_DOMAIN/#Contact/view/{ACCOUNT_ID}`.
     3. Click **Save**. ## Configure API endpoints



Configure endpoints that are compatible with EspoCRM to ensure that your integration has the components for looking up accounts (contacts) and records (cases). For more information about compatible variables, see [API Overview](https://docs.espocrm.com/development/api/) in the EspoCRM documentation.

### Configure API account endpoints

This section explains how to configure API account endpoints.

#### Configure a Find an account by query endpoint

To configure the **Find an account by query endpoint** , follow these steps:

  1. In the CCAI Platform, click **Settings > Developer Settings**. If you don't see the **Settings** menu, click **Menu**.
  2. In the **CRM** pane, go to the **API account** section.
  3. For **Find an account by query endpoint** , click **Setup**. The **Generic API Endpoint Setup** page appears.
  4. In the **URL** field, enter the URL to look up an account–for example, `https://YOUR_ESPO_DOMAIN/api/v1/Contact`.
  5. For **Method** , select **GET**.
  6. To configure request parameters, do the following:

     1. To configure the first request parameter, follow these steps: 
        1. Click **Add field**. The **Add Field** dialog appears.
        2. In the **Field Key** field, enter `where[0][attribute]`.
        3. In the **Field Value** field, enter `phoneNumber`.
        4. Click **Save**.
     2. To configure the rest of the request parameters, repeat the previous steps using the information in the following table. You've already created the first request parameter.

Field Key | Field Value  
---|---  
`where[0][attribute]` | `phoneNumber`  
`where[0][type]` | `equals`  
`where[0][value]` | `{PHONE_NUMBER}`  
`sortBy` | `createdAt`  
`asc` | `false`  
  7. In the **Response Data Location** field, enter `data.list`.

  8. Click **Save**.

  9. Click **Back to Developer Settings** to return to the **Developer Settings** page.




#### Configure a Find an account by ID endpoint

To configure the **Find an account by ID endpoint** , follow these steps:

  1. In the **CRM** pane, go to the **API account** section.
  2. For **Find an account by ID endpoint** , click **Setup**. The **Generic API Endpoint Setup** page appears.
  3. In the **URL** field, enter the URL to look up an account–for example, `https://YOUR_ESPO_DOMAIN/api/v1/Contact/{ACCOUNT_ID}`. 
     1. For **Method** , select **GET**.
  4. Set the **Response Data Location** to `data`.
  5. Click **Save**.
  6. Click **Return to developer settings** to return to the **Developer Settings** page.



#### Configure a Create an account endpoint

To configure the **Create an account endpoint** , follow these steps:

  1. In the **CRM** pane, go to the **API account** section.
  2. For **Create an account endpoint** , click **Setup**. The **Generic API Endpoint Setup** page appears.
  3. In the **URL** field, enter the URL to look up an account–for example, `https://YOUR_ESPO_DOMAIN/api/v1/Contact`.
  4. For **Method** , select **POST**.
  5. To configure **Request Parameters** , do the following:

     1. To configure the first request parameter, follow these steps: 
        1. For **Request Parameters** , click **Add field**. The **Add Field** dialog appears.
        2. In the **Field Key** field, enter `phoneNumber`.
        3. In the **Field Value** field, enter `{PHONE_NUMBER}`.
        4. Click **Save**.
     2. To configure the rest of the request parameters, repeat the previous step, using the information in the following table. You've already created the first request parameter.

Parameter Key | Parameter Value  
---|---  
`phoneNumber` | `{PHONE_NUMBER}`  
`firstName` | `New Caller`  
`lastName` | `{CALL_ID}`  
`name` | `New Caller {CALL_ID}`  
  6. Set the **Response data location** to `data`.

  7. Set the **Object ID location** to `id`.

  8. Click **Save**.

  9. Click **Return to developer settings** to return to the **Developer Settings** page.




#### Configure an Update an account endpoint

To configure the **Update an account endpoint** , follow these steps:

  1. In the **CRM** pane, go to the **API account** section.
  2. For **Update an account endpoint** , click **Setup**. The **Generic API Endpoint Setup** page appears.
  3. In the **URL** field, enter the URL to look up an account–for example, `https://YOUR_ESPO_DOMAIN/api/v1/Contact`.
  4. For **Method** , select **PUT**.
  5. To configure **Request Parameters** , do the following:

     1. To configure the first request parameter, follow these steps: 
        1. For **Request Parameters** , click **Add field**. The **Add Field** dialog appears.
        2. In the **Field Key** field, enter `contactId`.
        3. In the **Field Value** field, enter `{PHONE_NUMBER}`.
        4. Click **Save**.
     2. To configure the rest of the request parameters, repeat the previous step, using the information in the following table. You've already created the first request parameter.

Parameter Key | Parameter Value  
---|---  
`contactId` | `{PHONE_NUMBER}`  
`phoneNumber` | `New Caller`  
  6. Set the **Response data location** to `data`.

  7. Click **Save**.

  8. Click **Return to developer settings** to return to the **Developer Settings** page.




### Configure API record endpoints

This section explains how to configure API record endpoints.

#### Configure a Find a record by query endpoint

To configure the **Find a record by query endpoint** , follow these steps:

  1. In the **CRM** pane, go to the **API record** section.
  2. For **Find a record by query endpoint** , click **Setup**. The **Generic API Endpoint Setup** page appears.
  3. In the **URL** field, enter the URL to look up an account–for example, `https://YOUR_ESPO_DOMAIN/api/v1/Case`.
  4. For **Method** , select **GET**.
  5. To configure **Request Parameters** , do the following:

     1. To configure the first request parameter, follow these steps: 
        1. For **Request Parameters** , click **Add field**. The **Add Field** dialog appears.
        2. In the **Field Key** field, enter `where[0][attribute]`.
        3. In the **Field Value** field, enter `contactId`.
        4. Click **Save**.
     2. To configure the rest of the request parameters, repeat the previous step, using the information in the following table. You've already created the first request parameter.

Field Key | Field Value  
---|---  
`where[0][attribute]` | `contactId`  
`where[0][type]` | `equals`  
`where[0][value]` | `{ACCOUNT_ID}`  
`contactId` | `{ACCOUNT_ID}`  
`sortBy` | `createdAt`  
`asc` | `false`  
  6. In the **Response Data Location** field, enter `data.list`.

  7. Click **Save**.

  8. Click **Return to developer settings** to return to the **Developer Settings** page.




#### Configure a Find a record by ID endpoint

Often used in SDK based interactions, this lets you pass a specific record ID to associate the interaction with. To configure the **Find a record by ID endpoint** , follow these steps:

  1. In the **CRM** pane, go to the **API record** section.
  2. For **Find a record by ID endpoint** , click **Setup**. The **Generic API Endpoint Setup** page appears.
  3. In the **URL** field, enter the URL to look up an account–for example, `https://YOUR_ESPO_DOMAIN/api/v1/Case/{RECORD_ID}`.
  4. For **Method** , select **GET**.
  5. In the **Response Data Location** field, enter `data`.
  6. Click **Save**.
  7. Click **Return to developer settings** to return to the **Developer Settings** page.



#### Configure a Create a record endpoint

To configure the **Create a record endpoint** , follow these steps:

  1. In the **CRM** pane, go to the **API record** section.
  2. For **Create a record endpoint** , click **Setup**. The **Generic API Endpoint Setup** page appears.
  3. In the **URL** field, enter the URL to look up an account–for example, `https://YOUR_ESPO_DOMAIN/api/v1/Case`.
  4. For **Method** , select **POST**.
  5. To configure **Request Parameters** , do the following:

     1. To configure the first request parameter, follow these steps: 
        1. For **Request Parameters** , click **Add field**. The **Add Field** dialog appears.
        2. In the **Field Key** field, enter `description`.
        3. In the **Field Value** field, enter `CALL Session:{CALL_ID}`.
        4. Click **Save**.
     2. To configure the rest of the request parameters, repeat the previous step, using the information in the following table. You've already created the first request parameter.

Parameter Key | Parameter Value  
---|---  
`description` | `Call Session: {CALL_ID}`  
`name` | `Inbound Call from {ANI}`  
`contactId` | `{ACCOUNT_ID}`  
`status` | `New`  
`cchatId` | `{CHAT_ID}`  
`ccallId` | `{CALL_ID}`  
`cChannel` | `{CHANNEL}`  
`Type` | `{SESSION_TYPE}`  
  6. In the **Response Data Location** field, enter `data`.

  7. In the **Object ID Location** field, enter `id`.

  8. Click **Save**.

  9. Click **Return to developer settings** to return to the **Developer Settings** page.




#### Configure an Update a record endpoint

To configure the **Update a record endpoint** , follow these steps:

  1. In the **CRM** pane, go to the **API record** section.
  2. For **Update a record endpoint** , click **Setup**. The **Generic API Endpoint Setup** page appears.
  3. In the **URL** field, enter the URL to look up an account–for example, `https://YOUR_ESPO_DOMAIN/api/v1/Case/{RECORD_ID}`.
  4. For **Method** , select **PUT**.
  5. To configure **Request Parameters** , do the following:

     1. To configure the first request parameter, follow these steps: 
        1. For **Request Parameters** , click **Add field**. The **Add Field** dialog appears.
        2. In the **Field Key** field, enter `parentId`.
        3. In the **Field Value** field, enter `{RECORD_ID}`.
        4. Click **Save**.
     2. To configure the rest of the request parameters, repeat the previous step, using the information in the following table. You've already created the first request parameter.

Parameter Key | Parameter Value  
---|---  
`parentId` | `{RECORD_ID}`  
`parentType` | `Case`  
`status` | `New`  
`description` | `{TICKET_DESCRIPTION}`  
  6. In the **Response data location** field, enter `data`.

  7. Click **Save**.

  8. Click **Return to developer settings** to return to the **Developer Settings** page.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
