---
url: https://docs.cloud.google.com/resource-manager/docs/manage-essential-contacts/
title: Manage Essential Contacts \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:57:58.662705+00:00
---

# Manage Essential Contacts  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/manage-essential-contacts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Manage Essential Contacts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the available methods for viewing, adding, modifying, or removing Essential Contacts and configuring [notification categories](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories) for them.

If you are an Organization Admin, you can manage your Essential Contacts by using the Google Cloud console, the Google Cloud CLI, or the REST API. Follow [best practices](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#best-practices) for managing Essential Contacts.

If you are an essential contact, ask your administrator to send you a test email to verify reception for the specific notification category. If you are not receiving notifications, verify the following:

  * Check your email spam or junk folder.
  * Verify that the email address registered as a contact is correct and can receive external emails.
  * Make sure your contact information is assigned to the relevant notification categories.



## Before you begin

To receive notifications, the contact must be able to receive emails from Google.

If you want to manage contacts by using the gcloud CLI or the REST API, enable the Essential Contacts API. If you only want to manage contacts by using the Google Cloud console, you don't need to enable the API.

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=essentialcontacts.googleapis.com)

### Required roles

To get the permissions that you need to manage contacts, ask your administrator to grant you the following IAM roles on the project, folder, or organization where the contact is assigned: 

  * To view contacts: [Essential Contacts Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/essentialcontacts#essentialcontacts.viewer) (`roles/essentialcontacts.viewer`) 
  * To view, edit, delete, and create contacts: [Essential Contacts Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/essentialcontacts#essentialcontacts.admin) (`roles/essentialcontacts.admin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage contacts. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage contacts:

  * To view contacts: 
    * `essentialcontacts.contacts.get`
    * `essentialcontacts.contacts.list`
  * To edit, delete, and create contacts: 
    * `essentialcontacts.contacts.create`
    * `essentialcontacts.contacts.delete`
    * `essentialcontacts.contacts.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View contacts

Child resources, which refer to folders and projects, inherit contacts from their ancestors, which can be organizations and other folders. When viewing contacts from a child resource, you can also view contacts inherited from its ancestor if you have the corresponding permissions for the ancestor. To gain this ability, obtain a role on the ancestor resource that includes the required permissions to view contacts. When you view contacts from an organization or top-level folder, you don't see contacts from their child resources.

To view the list of all Essential Contacts in your project, folder, or organization, do the following:

### Console

  1. In the Google Cloud console, go to the **Essential Contacts** page.

[Go to the Essential Contacts page](https://console.cloud.google.com/iam-admin/essential-contacts)

  2. Make sure the name of your project, folder, or organization appears in the resource selector of the page. The resource selector lets you select the project, folder, or organization from which you want to view Essential Contacts.

  3. Next to **View by** , you can choose one of the following options:

     * To view the list of contacts by category, select **Category**.
     * To view the list of contacts alphabetically, select **Contact**.



### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. With the Google Cloud CLI, you can either list the contacts that are defined on a resource or list all contacts and inherited contacts for a resource. 

#### List contacts defined on a resource

To view Essential Contacts defined on a specific project, folder, or organization, use the [`gcloud essential-contacts list`](https://docs.cloud.google.com/sdk/gcloud/reference/essential-contacts/list) command:
         
         gcloud essential-contacts list --RESOURCE_TYPE="RESOURCE_ID"

Replace the following:

     * `RESOURCE_TYPE`: the resource type that you want to list contacts from. Use the value `project`, `folder`, or `organization`.
     * `RESOURCE_ID`: your Google Cloud project number, organization ID, or folder ID. Project numbers, folder IDs, and organization IDs are numeric, like `123456789012`. For projects, you must use the numeric [project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects). Alphanumeric project IDs are not supported.

Alternatively, if you don't specify a resource type or ID, the gcloud CLI lists contacts from the current project.

The response is similar to the following example:
    
    ---
    email: my-contact-1@example.com
    languageTag: en-US
    name: projects/my-projects/contacts/1
    notificationCategorySubscriptions:
    - ALL
    ---
    email: my-contact-2@example.com
    languageTag: en-US
    name: projects/my-projects/contacts/2
    notificationCategorySubscriptions:
    - BILLING
    ---
    

#### List contacts and inherited contacts

If you want to list all contacts from a resource and its inherited contacts from an ancestor, you must have a role on the ancestor resource that includes the required permissions to view contacts. Then, use the [`gcloud essential-contacts compute`](https://docs.cloud.google.com/sdk/gcloud/reference/essential-contacts/compute) command:
    
    gcloud essential-contacts compute --notification-categories="NOTIFICATION_CATEGORY" \
      --RESOURCE_TYPE="RESOURCE_ID"

Replace the following:

     * `NOTIFICATION_CATEGORY`: a comma-separated list of the notification categories that you want to view contacts for. The list can contain any of the following values:

       * `billing`
       * `legal`
       * `product-updates`
       * `security`
       * `suspension`
       * `technical`
       * `all`
       * `notification-category-unspecified`

For more information, see [Notification categories](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories).

     * `RESOURCE_TYPE`: the resource type that you want to view contacts from. Use the value `project`, `folder`, or `organization`.

     * `RESOURCE_ID`: your Google Cloud project number, organization ID, or folder ID. Project numbers, folder IDs, and organization IDs are numeric, like `123456789012`. For projects, you must use the numeric [project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects). Alphanumeric project IDs are not supported.

If you don't specify a resource type and ID, the gcloud CLI lists contacts for the current project.

The response is similar to the following example:
    
    ---
    email: my-contact-1@example.com
    languageTag: en-US
    name: projects/my-projects/contacts/1
    notificationCategorySubscriptions:
    - ALL
    ---
    email: my-contact-2@example.com
    languageTag: en-US
    name: projects/my-projects/contacts/2
    notificationCategorySubscriptions:
    - BILLING
    ---
    email: my-organization-contact@example.com
    languageTag: en-US
    name: organizations/my-organization/contacts/1
    notificationCategorySubscriptions:
    - ALL
    ---
    




### REST

With the Essential Contacts REST API, you can either list the contacts that are defined on a resource or list all contacts and inherited contacts for a resource.

#### List contacts defined on a resource

To view the contacts defined on a specific project, folder, or organization, use the Essential Contacts API's [`contacts.list`](https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest/v1/projects.contacts/list) method.

**Request** :
    
    
    GET essentialcontacts.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/contacts?pageSize=PAGE_SIZE&pageToken=NEXT_PAGE_TOKEN
    

Replace the following:

  * `RESOURCE_TYPE`: the resource type that you want to list contacts from. Use the value `projects`, `folders`, or `organizations`.
  * `RESOURCE_ID`: your Google Cloud project number, organization ID, or folder ID. Project numbers, folder IDs, and organization IDs are numeric, like `123456789012`. For projects, you must use the numeric [project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects). Alphanumeric project IDs are not supported.
  * `PAGE_SIZE`: Optional. The number of contacts to include in the response. The default value is `50`, and the maximum value is `100`. If the number of contacts is greater than the page size, the response contains a pagination token that you can use to retrieve the next page of results.
  * `NEXT_PAGE_TOKEN`: Optional. The pagination token returned in an earlier response from this method. If specified, the list of contacts starts where the previous response ended.



To send your request, expand one of these options:

####  curl (Linux, macOS, or Cloud Shell) 

Set the [`GOOGLE_APPLICATION_CREDENTIALS`](https://docs.cloud.google.com/docs/authentication/production) environment variable to your service account private key path. Then, make the request: 
    
    
    curl -X GET \
    -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
    https://essentialcontacts.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/contacts?pageSize=PAGE_SIZE&pageToken=NEXT_PAGE_TOKEN
      

####  PowerShell (Windows) 

Set the [`GOOGLE_APPLICATION_CREDENTIALS`](https://docs.cloud.google.com/docs/authentication/production) environment variable to your service account private key path. Then, make the request: 
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method GET `
      -Headers $headers `
      -Uri "https://essentialcontacts.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/contacts?pageSize=PAGE_SIZE&pageToken=NEXT_PAGE_TOKEN" | Select-Object -Expand Content
      

After sending the request, you receive a JSON response similar to the following example:
    
    
    {
      "contacts": [
        {
          "name": "projects/my-projects/contacts/1",
          "email": "my-contact-1@example.com",
          "notificationCategorySubscriptions": [
            "ALL"
          ],
          "languageTag": "en-US"
        },
        {
          "name": "projects/my-projects/contacts/2",
          "email": "my-contact-2@example.com",
          "notificationCategorySubscriptions": [
            "BILLING"
          ],
          "languageTag": "en-US"
        }
      ]
    }
    

#### List contacts and inherited contacts

If you want to list all contacts from a resource and its inherited contacts from an ancestor, you must have a role on the ancestor resource that includes the required permissions to view contacts. Then, use the Essential Contacts API's [`contacts.compute`](https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest/v1/projects.contacts/compute) method.

**Request** :
    
    
    GET essentialcontacts.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/contacts:compute?notificationCategories=NOTIFICATION_CATEGORY&pageSize=PAGE_SIZE&pageToken=NEXT_PAGE_TOKEN
    

Replace the following:

  * `RESOURCE_TYPE`: the resource type that you want to view contacts from. Use the value `projects`, `folders`, or `organizations`.
  * `RESOURCE_ID`: your Google Cloud project number, organization ID, or folder ID. Project numbers, folder IDs, and organization IDs are numeric, like `123456789012`. For projects, you must use the numeric [project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects). Alphanumeric project IDs are not supported.
  * `NOTIFICATION_CATEGORY`: the notification category you want to view contacts from. You can repeat this field to list contacts from multiple notification categories. It can take any of the following values:

    * `BILLING`
    * `LEGAL`
    * `PRODUCT_UPDATES`
    * `SECURITY`
    * `SUSPENSION`
    * `TECHNICAL`
    * `ALL`
    * `NOTIFICATION_CATEGORY_UNSPECIFIED`

For more information, see [Notification categories](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories).

  * `PAGE_SIZE`: Optional. The number of contacts to include in the response. The default value is `50`, and the maximum value is `100`. If the number of contacts is greater than the page size, the response contains a pagination token that you can use to retrieve the next page of results.

  * `NEXT_PAGE_TOKEN`: Optional. The pagination token returned in an earlier response from this method. If specified, the list of contacts starts where the previous response ended.




To send your request, expand one of these options:

####  curl (Linux, macOS, or Cloud Shell) 

Set the [`GOOGLE_APPLICATION_CREDENTIALS`](https://docs.cloud.google.com/docs/authentication/production) environment variable to your service account private key path. Then, make the request: 
    
    
    curl -X GET \
    -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
    https://essentialcontacts.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/contacts:compute?notificationCategories=NOTIFICATION_CATEGORY&pageSize=PAGE_SIZE&pageToken=NEXT_PAGE_TOKEN
    

####  PowerShell (Windows) 

Set the [`GOOGLE_APPLICATION_CREDENTIALS`](https://docs.cloud.google.com/docs/authentication/production) environment variable to your service account private key path. Then, make the request: 
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method GET `
      -Headers $headers `
      -Uri "https://essentialcontacts.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/contacts:compute?notificationCategories=NOTIFICATION_CATEGORY&pageSize=PAGE_SIZE&pageToken=NEXT_PAGE_TOKEN" | Select-Object -Expand Content
    

After sending the request, you receive a JSON response similar to the following example:
    
    
    {
      "contacts": [
        {
          "name": "projects/my-projects/contacts/1",
          "email": "my-project-contact-1@example.com",
          "notificationCategorySubscriptions": [
            "ALL"
          ],
          "languageTag": "en-US"
        },
        {
          "name": "projects/my-projects/contacts/2",
          "email": "my-project-contact-2@example.com",
          "notificationCategorySubscriptions": [
            "BILLING"
          ],
          "languageTag": "en-US"
        },
        {
          "name": "organizations/my-organization/contacts/1",
          "email": "my-organization-contact@example.com",
          "notificationCategorySubscriptions": [
            "ALL"
          ],
          "languageTag": "en-US"
        }
      ]
    }
    

## Add a contact

**Important:** Some Google Cloud services capture the list of recipients for a notification campaign, such as a Mandatory Service Announcement (MSA), in advance. If you add a new contact after this date, they might not receive that specific notification, even if it is delivered after you added them.

To add a contact, do the following:

### Console

  1. In the Google Cloud console, go to the **Essential Contacts** page.

[Go to the Essential Contacts page](https://console.cloud.google.com/iam-admin/essential-contacts)

  2. Make sure the name of your project, folder, or organization appears in the resource selector of the page. The resource selector lets you select the project, folder, or organization from which you want to add Essential Contacts.

  3. Click person_add **Add contact**.

![A screenshot highlighting the option to add a contact from the Essential Contacts page.](https://docs.cloud.google.com/static/resource-manager/img/essential-contacts-add-contact.png)

  4. In the **Email** and **Confirm email** fields, enter the email address of the contact you want to add.

  5. From the **Notification categories** drop-down menu, select the categories that you want the contact to receive notifications for.

For a list of notification categories and recommended contacts, see [Notification categories](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories).

  6. Click **Save**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Add a new contact with the [`gcloud essential-contacts create`](https://docs.cloud.google.com/sdk/gcloud/reference/essential-contacts/create) command:
         
         gcloud essential-contacts create --email="EMAIL" \
             --notification-categories="NOTIFICATION_CATEGORY" \
             --language="LANGUAGE" \
             --RESOURCE_TYPE="RESOURCE_ID"

Replace the following:

     * `EMAIL`: the email address of the contact you want to add. You cannot change this field after you create your contact.
     * `NOTIFICATION_CATEGORY`: a comma-separated list of the categories that you want the contact to receive notifications for. The list can contain any of the following values: 
       * `billing`
       * `legal`
       * `product-updates`
       * `security`
       * `suspension`
       * `technical`
       * `all`
       * `notification-category-unspecified`
For a list of notification categories and recommended contacts, see [Notification categories](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories). 
     * `LANGUAGE`: the language code for your contact's preferred notification language. You can include the language code of any of the [supported languages](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#supported-languages).
     * `RESOURCE_TYPE`: the resource type that you want to create a contact for. Use the value `project`, `folder`, or `organization`.
     * `RESOURCE_ID`: your Google Cloud project number, organization ID, or folder ID. Project numbers, folder IDs, and organization IDs are numeric, like `123456789012`. For projects, you must use the numeric [project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects). Alphanumeric project IDs are not supported. 

If you don't specify a resource type and ID, the gcloud CLI creates a contact in the current project.

If the command is successful, you don't receive any response.




### REST

To add a new contact, use the Essential Contacts API's [`contacts.create`](https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest/v1/projects.contacts/create) method.

**Request** :
    
    
    POST essentialcontacts.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/contacts
    

**Request body** :
    
    
    {
      "email": "EMAIL",
      "notificationCategorySubscriptions": [
        "NOTIFICATION_CATEGORY_1",
        "NOTIFICATION_CATEGORY_2"
      ],
      "languageTag": "LANGUAGE"
    }
    

Replace the following:

  * `RESOURCE_TYPE`: the resource type that you want to create a contact for. Use the value `projects`, `folders`, or `organizations`.
  * `RESOURCE_ID`: your Google Cloud project number, organization ID, or folder ID. Project numbers, folder IDs, and organization IDs are numeric, like `123456789012`. For projects, you must use the numeric [project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects). Alphanumeric project IDs are not supported.
  * `EMAIL`: the email address of your contact. You cannot change this field after you create your contact.
  * `NOTIFICATION_CATEGORY_1` and `NOTIFICATION_CATEGORY_2`: the categories that you want the contact to receive notifications for. You can add more notification categories by including more of these values. The list can take one or more of the following values:

    * `BILLING`
    * `LEGAL`
    * `PRODUCT_UPDATES`
    * `SECURITY`
    * `SUSPENSION`
    * `TECHNICAL`
    * `ALL`

For a list of notification categories and recommended contacts, see [Notification categories](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories).

  * `LANGUAGE`: the language code for your contact's preferred notification language. You can include the language code of any of the [supported languages](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#supported-languages).




To send your request, expand one of these options:

####  curl (Linux, macOS, or Cloud Shell) 

Set the [`GOOGLE_APPLICATION_CREDENTIALS`](https://docs.cloud.google.com/docs/authentication/production) environment variable to your service account private key path. Then, save the request body in a JSON file called `request.json` and make the request: 
    
    
    curl -X POST \
    -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
    -H "Content-Type: application/json; charset=utf-8" \
    -d @request.json \
    https://essentialcontacts.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/contacts
      

####  PowerShell (Windows) 

Set the [`GOOGLE_APPLICATION_CREDENTIALS`](https://docs.cloud.google.com/docs/authentication/production) environment variable to your service account private key path. Then, save the request body in a JSON file called `request.json` and make the request: 
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -InFile request.json `
      -Uri "https://essentialcontacts.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/contacts" | Select-Object -Expand Content
      

After sending the request, you receive a JSON response similar to the following example:
    
    
    {
      "name": "projects/my-project/contacts/3",
      "email": "my-new-contact@example.com",
      "notificationCategorySubscriptions": [
        "SUSPENSION",
        "TECHNICAL"
      ],
      "languageTag": "en"
    }
    

## Modify contact information

You can change the [notification categories](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories) or [preferred language](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#supported-languages) for a contact, but you can't change a contact's email address. If a contact's email address changes, add a new contact with the updated email address and delete the old contact.

To change the notification categories assigned to a contact or their preferred language, do the following:

### Console

  1. In the Google Cloud console, go to the **Essential Contacts** page.

[Go to the Essential Contacts page](https://console.cloud.google.com/iam-admin/essential-contacts)

  2. Make sure the name of your project, folder, or organization appears in the resource selector of the page. The resource selector lets you select the project, folder, or organization from which you want to manage Essential Contacts.

  3. Next to **View by** , select **Contact**.

![A screenshot highlighting the option to select Contact from the Essential Contacts page.](https://docs.cloud.google.com/static/resource-manager/img/essential-contacts-view-by-contact.png)

  4. Click **Edit** edit next to the contact whose notification category you want to change.

![A screenshot highlighting the option to edit a contact from the Essential Contacts page.](https://docs.cloud.google.com/static/resource-manager/img/essential-contacts-edit-contact.png)

  5. Select the notification categories you want to modify from the **Notification categories** drop-down menu and click **Save**.




When you manage contacts from the Google Cloud console, the Google Cloud console automatically configures the contact's preferred language based on the contact creator's [preferred language settings](https://console.cloud.google.com/user-preferences/languages). For more information, see [Supported languages](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#supported-languages).

### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Update an existing contact with the [`gcloud essential-contacts update`](https://docs.cloud.google.com/sdk/gcloud/reference/essential-contacts/update) command:
         
         gcloud essential-contacts update CONTACT_ID \
             --notification-categories="NOTIFICATION_CATEGORY" \
             --language="LANGUAGE"
             --RESOURCE_TYPE="RESOURCE_ID"

Replace the following:

     * `CONTACT_ID`: the numeric ID of the contact you want to update. To see the IDs of all contacts in your project, folder, or organization, view your contacts. The numeric ID is the entire value after `contacts` in the contact's name.
     * `NOTIFICATION_CATEGORY`: a comma-separated list of the new categories that you want the contact to receive notifications for. This list replaces the existing list of notification categories. 

The list can contain any of the following values: 

       * `billing`
       * `legal`
       * `product-updates`
       * `security`
       * `suspension`
       * `technical`
       * `all`
       * `notification-category-unspecified`
For a list of notification categories and recommended contacts, see [Notification categories](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories). 
     * `LANGUAGE`: the language code for your contact's preferred notification language. You can include the language code of any of the [supported languages](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#supported-languages).
     * `RESOURCE_TYPE`: the resource type where you want to modify contact information. Use the value `project`, `folder`, or `organization`.
     * `RESOURCE_ID`: your Google Cloud project number, organization ID, or folder ID. Project numbers, folder IDs, and organization IDs are numeric, like `123456789012`. For projects, you must use the numeric [project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects). Alphanumeric project IDs are not supported.

If you don't specify a resource type and ID, the gcloud CLI updates the contact with the specified ID in the current project. If no contact with the specified ID exists, the gcloud CLI returns an error.

If the command is successful, you don't receive any response.




### REST

To change the notification categories or preferred language of an existing contact, use the Essential Contacts API's [`contacts.patch`](https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest/v1/projects.contacts/patch) method.

**Request** :
    
    
    PATCH essentialcontacts.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/contacts/CONTACT_ID?updateMask="UPDATE_MASK"
    

**Request body** :
    
    
    {
      "name": "RESOURCE_TYPE/RESOURCE_ID/contact/CONTACT_ID",
      "email": "EMAIL",
      "notificationCategorySubscriptions": [
        "NOTIFICATION_CATEGORY_1",
        "NOTIFICATION_CATEGORY_2"
      ],
      "languageTag": "LANGUAGE"
    }
    

Replace the following:

  * `RESOURCE_TYPE`: the resource type where you want to modify contact information. Use the value `projects`, `folders`, or `organizations`.
  * `RESOURCE_ID`: your Google Cloud project number, organization ID, or folder ID. Project numbers, folder IDs, and organization IDs are numeric, like `123456789012`. For projects, you must use the numeric [project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects). Alphanumeric project IDs are not supported.
  * `CONTACT_ID`: the numeric ID of the contact you want to update. To see the IDs of all contacts in your project, folder, or organization, view your contacts. The numeric ID is the entire value after `contacts` in the contact's name.
  * `UPDATE_MASK`: Optional. A mask describing which fields of the contact you want to change. The format for the mask is a comma-separated list of fully qualified names of fields, for example, `notificationCategorySubscriptions,languageTag`.
  * `EMAIL`: the email address of your contact. This field must match the email address associated with the `CONTACT_ID` that you include in the request.
  * `NOTIFICATION_CATEGORY_1` and `NOTIFICATION_CATEGORY_2`: Optional. The updated categories that you want the contact to receive notifications for. You can add more notification categories by including more of these values. The list can take one or more of the following values:

    * `BILLING`
    * `LEGAL`
    * `PRODUCT_UPDATES`
    * `SECURITY`
    * `SUSPENSION`
    * `TECHNICAL`
    * `ALL`

For a list of notification categories and recommended contacts, see [Notification categories](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories).

  * `LANGUAGE`: the language code for the contact's preferred notification language. You can include the language code of any of the [supported languages](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#supported-languages).




To send your request, expand one of these options:

####  curl (Linux, macOS, or Cloud Shell) 

Set the [`GOOGLE_APPLICATION_CREDENTIALS`](https://docs.cloud.google.com/docs/authentication/production) environment variable to your service account private key path. Then, save the request body in a JSON file called `request.json` and make the request: 
    
    
    curl -X PATCH \
    -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
    -H "Content-Type: application/json; charset=utf-8" \
    -d @request.json \
    https://essentialcontacts.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/contacts/CONTACT_ID?updateMask="UPDATE_MASK"
      

####  PowerShell (Windows) 

Set the [`GOOGLE_APPLICATION_CREDENTIALS`](https://docs.cloud.google.com/docs/authentication/production) environment variable to your service account private key path. Then, save the request body in a JSON file called `request.json` and make the request: 
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method PATCH `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -InFile request.json `
      -Uri "https://essentialcontacts.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/contacts/CONTACT_ID?updateMask="UPDATE_MASK"" | Select-Object -Expand Content
      

After sending the request, you receive a JSON response similar to the following example:
    
    
    {
      "name": "projects/my-project/contacts/2",
      "email": "my-new-contact@example.com",
      "notificationCategorySubscriptions": [
        "ALL"
      ],
      "languageTag": "en"
    }

## Delete a contact

To delete a contact, do the following:

### Console

  1. In the Google Cloud console, go to the **Essential Contacts** page.

[Go to the Essential Contacts page](https://console.cloud.google.com/iam-admin/essential-contacts)

  2. Make sure the name of your project, folder, or organization appears in the resource selector of the page. The resource selector lets you select the project, folder, or organization from which you want to delete Essential Contacts.

  3. Next to **View by** , select **Contact**.

![A screenshot highlighting the option to select Contact from the Essential Contacts page.](https://docs.cloud.google.com/static/resource-manager/img/essential-contacts-view-by-contact.png)

  4. Click **Delete** delete next to the email address of the contact you want to delete. Then, in the dialog, confirm that you want to delete the contact.

![A screenshot highlighting the option to delete a contact from the Essential Contacts page.](https://docs.cloud.google.com/static/resource-manager/img/essential-contacts-delete-contact.png)




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. Delete an existing contact with the [`gcloud essential-contacts delete`](https://docs.cloud.google.com/sdk/gcloud/reference/essential-contacts/delete) command:
         
         gcloud essential-contacts delete CONTACT_ID \
             --RESOURCE_TYPE="RESOURCE_ID"

Replace the following:

     * `CONTACT_ID`: the numeric ID of the contact you want to delete. To see the IDs of all contacts in your project, folder, or organization, view your contacts. The numeric ID is the entire value after `contacts` in the contact's name.
     * `RESOURCE_TYPE`: the resource type where the contact is defined on. Use the value `project`, `folder`, or `organization`.
     * `RESOURCE_ID`: your Google Cloud project number, organization ID, or folder ID. Project numbers, folder IDs, and organization IDs are numeric, like `123456789012`. For projects, you must use the numeric [project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects). Alphanumeric project IDs are not supported.

If you don't specify a resource type and ID, the gcloud CLI deletes the contact with the specified ID in the current project. If no contact with the specified ID exists, the gcloud CLI returns an error.

If the command is successful, you don't receive any response.




### REST

To delete a contact, use the Essential Contacts API's [`contacts.delete`](https://docs.cloud.google.com/resource-manager/docs/reference/essentialcontacts/rest/v1/projects.contacts/delete) method.

**Request** :
    
    
    DELETE essentialcontacts.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/contacts/CONTACT_ID
    

Replace the following:

  * `RESOURCE_TYPE`: the resource type where the contact is defined on. Use the value `projects`, `folders`, or `organizations`.
  * `RESOURCE_ID`: your Google Cloud project number, organization ID, or folder ID. Project numbers, folder IDs, and organization IDs are numeric, like `123456789012`. For projects, you must use the numeric [project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects). Alphanumeric project IDs are not supported.
  * `CONTACT_ID`: the numeric ID of the contact you want to delete. To see the IDs of all contacts in your project, folder, or organization, view your contacts. The numeric ID is the entire value after `contacts` in the contact's name.



To send your request, expand one of these options:

####  curl (Linux, macOS, or Cloud Shell) 

Set the [`GOOGLE_APPLICATION_CREDENTIALS`](https://docs.cloud.google.com/docs/authentication/production) environment variable to your service account private key path. Then, make the request: 
    
    
    curl -X DELETE \
    -H "Authorization: Bearer "$(gcloud auth application-default print-access-token) \
    https://essentialcontacts.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/contacts/CONTACT_ID
      

####  PowerShell (Windows) 

Set the [`GOOGLE_APPLICATION_CREDENTIALS`](https://docs.cloud.google.com/docs/authentication/production) environment variable to your service account private key path. Then, make the request: 
    
    
    $cred = gcloud auth application-default print-access-token
    $headers = @{ "Authorization" = "Bearer $cred" }
    
    Invoke-WebRequest `
      -Method DELETE `
      -Headers $headers `
      -Uri "https://essentialcontacts.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/contacts/CONTACT_ID" | Select-Object -Expand Content
      

If the request is successful, the response body is empty.

## Manage contacts by category

In the Google Cloud console, you can manage contacts by [notification category](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories) by going to the **Category** tab on the **Essential Contacts** page.

To add, change, or delete the contacts assigned to a single notification category, do the following:

  1. In the Google Cloud console, go to the **Essential Contacts** page.

[Go to the Essential Contacts page](https://console.cloud.google.com/iam-admin/essential-contacts)

  2. Make sure the name of your project, folder, or organization appears in the resource selector of the page. The resource selector lets you select the project, folder, or organization from which you want to manage Essential Contacts.

  3. Next to **View by** , select **Category**.

![A screenshot highlighting the option to select Category from the Essential Contacts page.](https://docs.cloud.google.com/static/resource-manager/img/essential-contacts-view-by-category.png)

  4. Click **Edit** edit in the same row as the category whose contacts you want to manage.

![A screenshot highlighting the option to edit a contact from the Essential Contacts page.](https://docs.cloud.google.com/static/resource-manager/img/essential-contacts-edit-by-category.png)

![](https://docs.cloud.google.com/static/resource-manager/img/essential-contacts-edit-by-category.png)

  5. Manage the contacts assigned to the notification category:

     * To add a new contact, click **Add contact** and follow the steps to add a contact.
     * To change the notification category assigned to a contact, click **Edit** edit next to the contact whose category you want to change. Then, select the notification categories you want from the **Notification categories** drop-down menu and click **Save**.
     * To delete a contact, click **Delete** delete next to the contact's email address.



## Send a test email to verify reception

You can send a test email to contacts in each category to verify whether the email accounts can receive emails from Google Cloud. You can send a maximum of one test email every 24 hours to each contact in every category and resource.

You can use the Google Cloud console to validate your contacts annually and make sure your directory is current. The Google Cloud console might prompt you to verify your contacts if they haven't been verified in the past year. However, an unvalidated status doesn't impact a contact's ability to receive notifications. A contact continues to receive messages unless their email address is invalid or they are removed from the Essential Contacts list.

To send a test email to contacts in a specific [notification category](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories), do the following:

  1. In the Google Cloud console, go to the **Essential Contacts** page.

[Go to the Essential Contacts page](https://console.cloud.google.com/iam-admin/essential-contacts)

  2. Make sure the name of your project, folder, or organization appears in the resource selector of the page. The resource selector lets you select the project, folder, or organization from which you want to manage Essential Contacts.

  3. Next to **View by** , select **Category**.

![A screenshot highlighting the option to select Category from the Essential Contacts page.](https://docs.cloud.google.com/static/resource-manager/img/essential-contacts-view-by-category.png)

  4. Click **Send** mail in the same row as the notification category whose contacts you want to deliver test emails to.

  5. Select the checkboxes next to the contacts to whom you want to send emails.

  6. Click **Send**. The system sends a test email to the selected contacts.

  7. Communicate with each contact to make sure they received the test email from `gcp-essential-contacts-noreply@google.com`.




## Set advanced configurations and automation

This section covers options for further management of your Essential Contacts, including restricting contact domains, using Infrastructure as Code (IaC) with Terraform for automation, and creating custom organization policies.

### Limit allowed domains for contacts

To restrict the email address domains that new contacts can have, set the organization policy constraint `constraints/essentialcontacts.allowedContactDomains`. Existing contacts are not impacted by this constraint.

To learn how to set organization policy constraints, see [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

### Manage contacts with Terraform

You can use Terraform to manage your Essential Contacts. Contacts have the following format in Terraform language:
    
    
    resource "google_essential_contacts_contact" "contact" {
      parent = "RESOURCE_TYPE/RESOURCE_ID"
      email = "EMAIL"
      language_tag = "LANGUAGE"
      notification_category_subscriptions = [NOTIFICATION_CATEGORY]
    }
    

When managing a contact, replace the following:

  * `RESOURCE_TYPE`: the resource type where you want to manage the contact. Use the value `projects`, `folders`, or `organizations`.
  * `RESOURCE_ID`: your Google Cloud project number, organization ID, or folder ID. Project numbers, folder IDs, and organization IDs are numeric, like `123456789012`. For projects, you must use the numeric [project number](https://docs.cloud.google.com/resource-manager/docs/view-update-projects#identifying_projects). Alphanumeric project IDs are not supported.
  * `EMAIL`: the email address of your contact. You cannot change this field after you create the contact.
  * `LANGUAGE`: Optional. The language code for the contact's preferred notification language. You can include the language code of any of the [supported languages](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#supported-languages).
  * `NOTIFICATION_CATEGORY`: an array of the categories that you want the contact to receive notifications for, such as `["BILLING", "LEGAL"]`. This array can contain any of the following values:

    * `BILLING`
    * `LEGAL`
    * `PRODUCT_UPDATES`
    * `SECURITY`
    * `SUSPENSION`
    * `TECHNICAL`
    * `ALL`

For a list of notification categories and recommended contacts, see [Notification categories](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts#notification-categories).




To add, modify or remove a contact, add, modify or remove a contact resource in your Terraform configuration file. For more details, see [Terraform Essential Contacts documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/essential_contacts_contact).

## What's next

  * Learn more about [Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts).
  * [Create custom constraints for Essential Contacts](https://docs.cloud.google.com/resource-manager/docs/essentialcontacts-custom-org-policies).
  * Learn how to [associate a domain with a project](https://docs.cloud.google.com/resource-manager/docs/managing-notifications#associate-domain) for verification purposes.
  * Understand how to [manage notification preferences](https://docs.cloud.google.com/resource-manager/docs/managing-notifications#manage-preferences).
  * Learn about [Advisory Notifications](https://docs.cloud.google.com/advisory-notifications/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
