---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-user-management/
title: Bulk user management \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:20.047077+00:00
---

# Bulk user management  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-user-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Bulk user management Stay organized with collections  Save and categorize content based on your preferences. 

Bulk user management lets you use the contents of a CSV file to create or modify large numbers of users simultaneously. Bulk user management features can be found in the CCAI Platform portal by going to **Settings > Users & teams**.

Feature benefits include:

  * Maintain essential user data (for example, email address and user name).

  * Grant edit permissions for each individual user property; granularly configure which user roles can make updates to each column in the user record when uploading the CSV file. For more information see [Bulk user management roles & permissions](https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-user-management#bulk_user_management_roles_and_permissions).

  * Set user roles, activate or deactivate a user, and maintain other properties such as setting chat concurrency and locations.




From the **import users** display, you can use the template provided to populate the information for your new users or download a CSV file of all your current users that can be updated to modify existing users. For more information see [Bulk user management templates](https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-user-management#bulk-user-management-templates).

If your CSV file upload contains errors, a message is displayed indicating how many records contained errors and how many records were uploaded successfully. Click **Download Error Log** to download a file showing which records contained errors and the specific fields in which the errors are located. For more information see [Bulk user management: Resolve errors](https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-user-management#resolve_errors).

To add and update users see [Bulk user management: Upload new or updated users](https://docs.cloud.google.com/contact-center/ccai-platform/docs/bulk-user-management#bulk_user_management_upload_new_or_updated_users).

To add users individually, see [Add and view users](https://docs.cloud.google.com/contact-center/ccai-platform/docs/add-edit-user#add-users).

## Bulk user management templates

You can add new users by populating the template provided and uploading the CSV file to import the user data. You can also download a CSV file of all your existing users and modify the file to make changes to those existing user accounts.

You can also upload your own CSV file rather than using one of the templates provided, but the columns in your file **must** correspond to those in the template and display in the same order. The file must be in CSV file format to be uploaded.

Both of the template files provided contain the following columns in the specified order:

**Note:** When updating users, leaving a cell empty indicates that there is no change to this field. Entering a 0 (zero) indicates that this field should be removed from the user record or made inactive.

**Table 1. Bulk user management template**

Order | Column type | Number of columns | Column(s) name | Valid values | Required column  
---|---|---|---|---|---  
1 | Email | 1 | Email | Email | Yes  
2 | Email | 1 | New email | Email | No  
3 | Alias | 1 | Alias | String | No  
4 | Agent ID | 1 | Agent ID | String | No  
5 | First name | 1 | First name | String | Yes  
6 | Last name | 1 | Last name | String | Yes  
7 | Status | 1 | Status | 

  * Active
  * Inactive
  * Empty

| No  
8 | Location | 1 | Location | 

  * A string that is a location name
  * Empty (no change)
  * Null (remove current location)

| No  
9 | Chat concurrency | 1 | Chat concurrency | 

  * 1 to X (where X is configured value)
  * Empty

| No  
10 | Chat concurrency status | 1 | Chat concurrency status | 

  * 0
  * 1
  * Empty

| No  
11 | Roles | Multiple | Role: role name A Role: role name B Role: role name C [etc.] | 

  * 0
  * 1
  * Empty

| No  
12 | Non-restricted international calling | 1 | Non-restricted international calling | 

  * 0
  * 1
  * Empty

| No  
13 | External user | 1 | External user | 

  * 0
  * 1
  * Empty

| No  
14 | SIP URI | 1 | External SIP URI | String | No  
15 | Contact Center AI Platform username | 1 | Contact Center AI Platform username | String | No  
16 | Team | Multiple | Team: team name A Team: team name B Team: team name C [etc.] | 

  * 0
  * 1
  * Empty

| No  
17 | Phone number | Multiple | Direct Inbound Number: 1 Direct Inbound Number: 2 Direct Inbound Number: 3 [etc.] | Phone number in E. 164 format | No  
18 | Extension | 1 | Extension | 

  * Empty: no change to extension config for a given agent
  * Null: will remove the extension value for a given agent (case insensitive)
  * Auto: will create an auto-generated extension for the agent (case insensitive)

| No  
  
For the **roles** and **team** fields, you must include additional columns to assign the user to multiple roles or teams. Each role or team needs to be entered as a separate column in the CSV file with the format shown in the previous table (for example, Role: role name A, Role: role name B). These values must also correspond to roles and teams that already exist in the CCAI Platform portal.

## Bulk user management roles and permissions

On the **roles & permissions** display, administrators can grant edit permissions to a role for each field in the user record. There is a specific permission available for each field in the user record and only fields to which the assigned role has access will be included in the CSV file.

A role must be assigned: Either **create users** or **edit user** permissions before the individual field permissions can be set. If the create users permission is set, then the assigned role can add new users but not edit existing users. If the edit user permission is granted, the assigned role can edit existing user records, but cannot create new users. If both permissions are assigned, the role can create new users and edit existing ones.

**Note:** For both the create users and edit user permissions, only the individual fields to which the role has access can be used.

Based on these permissions, the assigned role will only be able to make changes to the columns in the CSV file if they have edit user permissions and are assigned edit permissions for the corresponding field in the record. If the assigned role does not have the edit permissions for a field, the column won't be included when downloading the CSV file or template.

![Bulk user management](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ca1ff49c67.png)

Each of the following columns has individual permissions that can be set to allow edit access:

  * Email

  * Agent ID

  * First name and last name

  * Status

  * Location

  * Chat concurrency and chat concurrency status

  * Roles

  * Teams




If the user's assigned role does not include edit permissions, then the user cannot make changes to that field. If the user tries to make changes to a field to which they don't have edit permissions, an error will occur during validation and that record won't be uploaded.

## Bulk user management: Upload new or updated users

To upload multiple new users simultaneously, you can either download the sample template provided in the **Import Bulk Users** section or upload your own CSV file using the columns outlined.

If you want to edit existing users, download the Complete List of Users CSV file, make any necessary changes, and then upload the CSV file again.

**Note:** There is no limit on the number of users you can include in the CSV file.

  1. From the CCAI Platform portal, go to **Settings > Users & Teams**.

  2. On the **Users & teams settings** display, click the **Bulk User Management** tab.

![Bulk user management](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ca1ff68356.png)

  3. Click **Upload users**.

![Upload users](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ca1ff9309f.png)

  4. On the **import users** display, use the buttons in the **Step 1: Download Template** section to download a file to use for adding or modifying users.

![Import users display](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ca1ff974ef.jpg)

  5. To add new users, click **Template** to download a sample CSV file that you can populate with the information for the users being added.

  6. To modify existing users, click **Complete list of users** to download the information for all current users as a CSV file. You can then make any necessary changes to modify existing users in this file.

**Note:** When modifying an existing user, if the first name, last name, or email values are unchanged, leave the current entry in the field. These fields are required and leaving these fields blank will result in an error during the validation stage.
  7. Once the CSV file has been updated, proceed to the **Step 3: Upload CSV** section and either drag-and-drop the updated CSV file into the space provided or click **Browse your files** to manually select the file to upload.

![Browse CSV files](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ca1ffac713.png)

  8. Click **Process** in Step 4. The CCAI Platform portal will validate the CSV file and return to the **bulk user management** display.

  9. If the file is successfully validated, the users will be added or modified as requested and email notifications will be sent to any users with the **manage user lists** permissions indicating the changes that were made.

  10. If any fields in the file fail validation, an error message is displayed indicating the number of errors and how many records were updated successfully. Click **Download error log** to view a list of errors, or click **Retry** to attempt to validate the file again.

**Note:** Even if your file contains errors, any records that pass validation will be uploaded.



See Resolve errors for more information on potential sources of errors and how to resubmit your updated CSV file.

## Resolve errors

If your file upload contains errors, a message is displayed indicating how many records contained errors and how many records were uploaded successfully. Click **Download error log** to download a file showing which records contained errors and the specific fields in which the errors are located.

![File upload errors](https://docs.cloud.google.com/static/contact-center/ccai-platform/docs/images/1632ca1ffb0e28.png)

The **error log** will list the reason for the error and indicate which row and column in which the error occurred. The Error Log will also contain any warnings, such as your assigned role not having the necessary permissions to edit a specific column.

**Table 2. Sample error log results**

Error | Column | Row  
---|---|---  
Role name A must exist in the CCAI Platform Platform | 9 |   
Team name A must exist in the CCAI Platform Platform | 19 |   
The email must be unique | 1 | 25  
First name must not be empty | 3 | 190  
Last name must not be empty | 4 | 195  
Status must be `Active`, `Inactive`, or empty | 5 | 89  
Location must match the existing location in the CCAI Platform or be Null | 6 | 20  
Chat concurrency must be within 1 to X range | 7 | 78  
Role Name A must be 0, 1, or empty | 9 | 22  
Team name A must be 0, 1, or empty | 19 | 165  
  
Make any necessary changes to your CSV file to resolve the errors from the log. Once the errors have been resolved, upload the CSV file again for validation using the same method described in the previous section.

If there are no errors, the file will process successfully. If errors still remain in your file, download the new Error Log and repeat this process.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
