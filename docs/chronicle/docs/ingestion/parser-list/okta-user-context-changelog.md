---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/okta-user-context-changelog/
title: Change log for OKTA_USER_CONTEXT \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:50.653508+00:00
---

# Change log for OKTA_USER_CONTEXT  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/parser-list/okta-user-context-changelog/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Change log for OKTA_USER_CONTEXT

Date | Changes  
---|---  
2026-08-27 |  Enhancement:  
\- `event.idm.entity.entity.labels`: Newly mapped `profile.aws`, `profile.github_user`, `profile.is_manager` raw log fields to `event.idm.entity.entity.labels` UDM field.  
\- `event.idm.entity.entity.user.attribute.labels`: Newly mapped `profile.levelCode`, `profile.titleCode` raw log fields to `event.idm.entity.entity.user.attribute.labels` UDM field.  
\- `event.idm.entity.entity.namespace`: Newly mapped `profile.subOrganization` raw log field to `event.idm.entity.entity.namespace` UDM field.  
\- `event.idm.entity.entity.resource.product_object_id`: Newly mapped `profile.id_idm` raw log field to `event.idm.entity.entity.resource.product_object_id` UDM field.  
\- `event.idm.entity.entity.user.user_display_name`: Newly mapped `profile.legalName` raw log field to `event.idm.entity.entity.user.user_display_name` UDM field.   
2026-08-13 |  Enhancement:  
-`event.idm.entity.entity.labels`: Newly mapped `record_status`, `manager`, `countryCode`, `passwordChanged`, `record.id`, `displayName`, `record_profile_title`, `activated`, `created`, `costCenter`, `type_id`, `statusChanged` and `href` raw log fields with `event.idm.entity.entity.labels` UDM field.  
-`event.idm.entity.entity.user.attribute.labels`: Newly mapped `secondEmail`, `mobilePhone`, `login`, `lastName`, `firstName`, `employeeNumber`, `email`, `department`, `lastUpdated`, `_lastUpdated`, `division`, `name`, `type`, `recovery_question` and `locale` raw log fields with `event.idm.entity.entity.user.attribute.labels` UDM field.  
-`event.idm.entity.entity.user.phone_numbers`: Newly mapped `mobilePhone` raw log field with `event.idm.entity.entity.user.phone_numbers` UDM field.  
-`event.idm.entity.entity.user.managers.user_display_name`: Newly mapped `manager` raw log field with `event.idm.entity.entity.user.managers.user_display_name` UDM field.  
-`event.idm.entity.entity.user.last_name`: Newly mapped `lastName` raw log field with `event.idm.entity.entity.user.last_name` UDM field.  
-`event.idm.entity.entity.user.first_name`: Newly mapped `firstName` raw log field with `event.idm.entity.entity.user.first_name` UDM field.  
-`event.idm.entity.entity.user.email_addresses` and `event.idm.entity.entity.user.attribute.labels`: Newly mapped `email` and `secondEmail` raw log fields with `event.idm.entity.entity.user.email_addresses` UDM field if it is a valid `email` and not equal to `email` else mapped to `event.idm.entity.entity.user.attribute.labels`.  
-`event.idm.entity.entity.user.employee_id`: Newly mapped `employeeNumber` raw log field with `event.idm.entity.entity.user.employee_id` UDM field.  
-`event.idm.entity.entity.user.department`: Newly mapped `department` raw log field with `event.idm.entity.entity.user.department` UDM field.  
-`event.idm.entity.entity.user.office_address.country_or_region`: Newly mapped `countryCode` raw log field with `event.idm.entity.entity.user.office_address.country_or_region` UDM field.  
-`event.idm.entity.entity.user.userid` and `event.idm.entity.entity.user.attribute.labels`: Newly mapped `login` raw log field with `event.idm.entity.entity.user.userid` UDM field if it is a valid `userid` else mapped to `event.idm.entity.entity.user.attribute.labels`.  
-`event.idm.entity.entity.user.last_login_time`: Newly mapped `lastLogin_1` raw log field with `event.idm.entity.entity.user.last_login_time` UDM field.  
-`event.idm.entity.entity.user.last_password_change_time`: Newly mapped `passwordChanged` raw log field with `event.idm.entity.entity.user.last_password_change_time` UDM field.  
-`event.idm.entity.entity.user.user_authentication_status`: Newly mapped `record_status` raw log field with `event.idm.entity.entity.user.user_authentication_status` UDM field if it is a valid enum else mapped to `event.idm.entity.entity.labels`.  
-`event.idm.entity.metadata.entity_type`: Set `event.idm.entity.metadata.entity_type` to `USER` when the log has user related data.   
2025-02-07 |  Bug-Fix:  
\- Removed the hardcoded customer name from the code.   
2024-12-30 |  Enhancement:  
\- Mapped `activated`, `created`, `statusChanged`, and `type.id` to `entity.entity.labels`.  
\- Mapped `profile.AD_ObjectGUID`, `profile.ADpwdLastSet`, `profile.AFF_Code`, `profile.Desk_Location_WD`, `profile.Mailing_Address_WD`, `profile.Manager_UPN`, `profile.PRIVATE_CONF_Profile`, `profile.Region_WD`, `profile.Subsidiary_Company`, `profile.Telephone_Work`, `profile.Temp_WD_Primary_Email`, `profile.VMware_WS1_Username`, `profile.Work_Street_Address_WD`, `profile.Workato_WD_Primary_Email`, `profile.Workday_ID`, `profile.Worker_Type_WD`, `profile.businessUnit`, `profile.companyName`, `profile.contingentSupplierName`, `profile.conversationId`, `profile.distinguishedName`, `profile.division`, `profile.emailPrefix`, `profile.employeeType`, `profile.homePostalAddress`, `profile.isManager`, `profile.leaveOfAbsence`, `profile.managerDn`, `profile.payGroup`, `profile.wdemployeeID`, and `profile.zipCode` to `entity.entity.user.attribute.labels`.   
2024-10-10 |  Enhancement:  
\- Added `yyyy-MM-dd` to match date format of `profile.Hiredate`.   
2024-08-21 |  Enhancement:  
\- Added `gsub` to parse unparsed JSON logs.  
\- Added `yyyy-MM-dd` to match date format of `profile.terminationdate`.   
2024-06-18 |  Enhancement:  
\- Mapped `profile.samaccountname` to `entity.entity.user.userid`.   
2023-08-16 |  Enhancement:  
\- Mapped `lastLogin` to `entity.user.attribute.labels`.   
2023-07-18 |  Enhancement:  
\- Mapped `lastLogin` to `entity.user.last_login_time`.  
\- Mapped `passwordChanged` to `entity.user.last_password_change_time`.   
2023-06-08 |  Enhancement:  
\- Mapped `profile.hiredate` to `event.idm.entity.entity.user.hire_date` and supports `MM/dd/yyyy`, `M/dd/yyyy`, `MM/d/yyyy`, `M/d/yyyy`, `MM-dd-yyyy`, `M-dd-yyyy`, `MM-d-yyyy`, `M-d-yyyy`,`yyyy-MM-ddTHH:mm:ss`.  
\- Mapped `profile.terminationdate` to `event.idm.entity.entity.user.termination_date` and supports `MM/dd/yyyy`, `M/dd/yyyy`, `MM/d/yyyy`, `M/d/yyyy`, `MM-dd-yyyy`, `M-dd-yyyy`, `MM-d-yyyy`, `M-d-yyyy`,`yyyy-MM-ddTHH:mm:ss`.   
2023-05-02 |  Enhancement:  
For the `HireDate` field, added the following date format `yyyy-MM-ddTHH:mm:ss`.   
2022-10-20 |  Enhancement:  
\- Added condition for `profile.login` to check to add only index usernames into this field. If it's email-id mapped it to `entity.user.email_addresses` else mapped to `entity.user.userid`.  
\- Mapped `profile.ldapUid` to `entity.user.userid`.  
\- Mapped `profile.Preferred_First_Name` to `entity.user.first_name`.  
\- Mapped `profile.country` to `entity.user.country`.  
\- Mapped `profile.firstBaseCity` to `entity.user.firstBaseCity`.  
\- Mapped `profile.preferred_Last_Name` to `entity.user.preferred_Last_Name`.  
\- Mapped `profile.EmployeeWorkGroup` to `entity.user.EmployeeWorkGroup`.  
\- Mapped `profile.manager` to `entity.user.managers.user_display_name`.  
\- Mapped `profile.organization` to `entity.user.organization`.  
\- Mapped `profile.company` to `entity.user.company`.  
\- Mapped `profile.state` to `entity.user.state`.  
\- Mapped `profile.streetAddress` to `entity.user.streetAddress`.  
\- Mapped `profile.mobile` to `entity.user.mobile`.  
\- Mapped `profile.Function` to `entity.entity.labels`.  
\- Mapped `profile.costCenter` to `entity.entity.labels`.  
\- Mapped `profile.location` to `entity.entity.location.name`.  
\- Mapped `profile.managerEmail` to `entity.user.managers.email_addresses`.  
\- Mapped `profile.managerId` to `entity.user.managers.employee_id`.  
\- Mapped `profile.spotify_username` to `entity.entity.labels`.   
2022-05-19 |  Enhancement:  
For `HireDate` field, added following date format `M/dd/yyyy`, `MM/d/yyyy`, `M/d/yyyy`, `MM-dd-yyyy`, `M-d-yyyy`.   
2022-03-29 |  Enhancement-  
For `HireDate` value, change data format from DD/MM/YYYY to MM/DD/YYYY   
2022-03-23 |  Enhancement-Added mappings for new field:  
`HireDate` field mapped to event.idm.entity.entity.user.hire_date.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
