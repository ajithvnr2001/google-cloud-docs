---
url: https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch/
title: Payment Gateway issuer switch roles and permissions \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:31:27.707403+00:00
---

# Payment Gateway issuer switch roles and permissions  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Payment Gateway issuer switch roles and permissions Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the IAM roles and permissions for Payment Gateway issuer switch. To search through all roles and permissions, see the [role and permission index](https://docs.cloud.google.com/iam/docs/roles-permissions).

## Payment Gateway issuer switch roles

Role | Permissions  
---|---  
  
#### Issuerswitch Admin Beta

(`roles/issuerswitch.admin`) Access to all issuer switch roles  |  `issuerswitch.*`

  * `issuerswitch.accountManagerTransactions.list`
  * `issuerswitch.accountManagerTransactions.update`
  * `issuerswitch.complaintTransactions.list`
  * `issuerswitch.complaints.create`
  * `issuerswitch.complaints.resolve`
  * `issuerswitch.disputes.create`
  * `issuerswitch.disputes.resolve`
  * `issuerswitch.financialTransactions.list`
  * `issuerswitch.issuerParticipants.get`
  * `issuerswitch.issuerParticipants.update`
  * `issuerswitch.managedAccounts.get`
  * `issuerswitch.managedAccounts.update`
  * `issuerswitch.mandateTransactions.list`
  * `issuerswitch.metadataTransactions.list`
  * `issuerswitch.operations.cancel`
  * `issuerswitch.operations.delete`
  * `issuerswitch.operations.get`
  * `issuerswitch.operations.list`
  * `issuerswitch.operations.wait`
  * `issuerswitch.ruleMetadata.list`
  * `issuerswitch.ruleMetadataValues.create`
  * `issuerswitch.ruleMetadataValues.delete`
  * `issuerswitch.ruleMetadataValues.list`
  * `issuerswitch.rules.list`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Issuerswitch Viewer Beta

(`roles/issuerswitch.viewer`) Viewer role for issuerswitch  |  `issuerswitch.accountManagerTransactions.list` `issuerswitch.complaintTransactions.list` `issuerswitch.financialTransactions.list` `issuerswitch.issuerParticipants.get` `issuerswitch.managedAccounts.get` `issuerswitch.mandateTransactions.list` `issuerswitch.metadataTransactions.list` `issuerswitch.operations.get` `issuerswitch.operations.list` `issuerswitch.operations.wait` `issuerswitch.ruleMetadata.list` `issuerswitch.ruleMetadataValues.list` `issuerswitch.rules.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Issuerswitch Account Manager Admin Beta

(`roles/issuerswitch.accountManagerAdmin`) This role can perform all account manager related operations  |  `issuerswitch.accountManagerTransactions.*`

  * `issuerswitch.accountManagerTransactions.list`
  * `issuerswitch.accountManagerTransactions.update`

`issuerswitch.managedAccounts.*`

  * `issuerswitch.managedAccounts.get`
  * `issuerswitch.managedAccounts.update`

`issuerswitch.operations.get` `issuerswitch.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Issuerswitch Account Manager Transactions Admin Beta

(`roles/issuerswitch.accountManagerTransactionsAdmin`) This role can perform all account manager transactions related operations  |  `issuerswitch.accountManagerTransactions.*`

  * `issuerswitch.accountManagerTransactions.list`
  * `issuerswitch.accountManagerTransactions.update`

`issuerswitch.operations.get` `issuerswitch.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Issuerswitch Account Manager Transactions Viewer Beta

(`roles/issuerswitch.accountManagerTransactionsViewer`) This role can view all account manager transactions  |  `issuerswitch.accountManagerTransactions.list` `issuerswitch.operations.get` `issuerswitch.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Issuerswitch Participants Admin Beta

(`roles/issuerswitch.issuerParticipantsAdmin`) Full access to issuer switch participants  |  `issuerswitch.issuerParticipants.*`

  * `issuerswitch.issuerParticipants.get`
  * `issuerswitch.issuerParticipants.update`

`resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Issuerswitch Resolutions Admin Beta

(`roles/issuerswitch.resolutionsAdmin`) Full access to issuer switch resolutions  |  `issuerswitch.complaintTransactions.list` `issuerswitch.complaints.*`

  * `issuerswitch.complaints.create`
  * `issuerswitch.complaints.resolve`

`issuerswitch.disputes.*`

  * `issuerswitch.disputes.create`
  * `issuerswitch.disputes.resolve`

`issuerswitch.operations.get` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Issuerswitch Rules Admin Beta

(`roles/issuerswitch.rulesAdmin`) Full access to issuer switch rules  |  `issuerswitch.ruleMetadata.list` `issuerswitch.ruleMetadataValues.*`

  * `issuerswitch.ruleMetadataValues.create`
  * `issuerswitch.ruleMetadataValues.delete`
  * `issuerswitch.ruleMetadataValues.list`

`issuerswitch.rules.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Issuerswitch Rules Viewer Beta

(`roles/issuerswitch.rulesViewer`) This role can view rules and related metadata.  |  `issuerswitch.ruleMetadata.list` `issuerswitch.ruleMetadataValues.list` `issuerswitch.rules.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
#### Issuerswitch Transactions Viewer Beta

(`roles/issuerswitch.transactionsViewer`) This role can view all transactions  |  `issuerswitch.complaintTransactions.list` `issuerswitch.financialTransactions.list` `issuerswitch.mandateTransactions.list` `issuerswitch.metadataTransactions.list` `issuerswitch.operations.get` `issuerswitch.operations.list` `resourcemanager.projects.get` `resourcemanager.projects.list`  
  
## Payment Gateway issuer switch permissions

Permission | Included in roles  
---|---  
  
#### `issuerswitch.accountManagerTransactions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.viewer) (`roles/issuerswitch.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Issuerswitch Account Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.accountManagerAdmin) (`roles/issuerswitch.accountManagerAdmin`)  [Issuerswitch Account Manager Transactions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.accountManagerTransactionsAdmin) (`roles/issuerswitch.accountManagerTransactionsAdmin`)  [Issuerswitch Account Manager Transactions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.accountManagerTransactionsViewer) (`roles/issuerswitch.accountManagerTransactionsViewer`)   
  
#### `issuerswitch.accountManagerTransactions.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Account Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.accountManagerAdmin) (`roles/issuerswitch.accountManagerAdmin`)  [Issuerswitch Account Manager Transactions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.accountManagerTransactionsAdmin) (`roles/issuerswitch.accountManagerTransactionsAdmin`)   
  
#### `issuerswitch.complaintTransactions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.viewer) (`roles/issuerswitch.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Issuerswitch Resolutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.resolutionsAdmin) (`roles/issuerswitch.resolutionsAdmin`)  [Issuerswitch Transactions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.transactionsViewer) (`roles/issuerswitch.transactionsViewer`)   
  
#### `issuerswitch.complaints.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Resolutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.resolutionsAdmin) (`roles/issuerswitch.resolutionsAdmin`)   
  
#### `issuerswitch.complaints.resolve`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Resolutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.resolutionsAdmin) (`roles/issuerswitch.resolutionsAdmin`)   
  
#### `issuerswitch.disputes.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Resolutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.resolutionsAdmin) (`roles/issuerswitch.resolutionsAdmin`)   
  
#### `issuerswitch.disputes.resolve`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Resolutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.resolutionsAdmin) (`roles/issuerswitch.resolutionsAdmin`)   
  
#### `issuerswitch.financialTransactions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.viewer) (`roles/issuerswitch.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Issuerswitch Transactions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.transactionsViewer) (`roles/issuerswitch.transactionsViewer`)   
  
#### `issuerswitch.issuerParticipants.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.viewer) (`roles/issuerswitch.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Issuerswitch Participants Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.issuerParticipantsAdmin) (`roles/issuerswitch.issuerParticipantsAdmin`)   
  
#### `issuerswitch.issuerParticipants.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Participants Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.issuerParticipantsAdmin) (`roles/issuerswitch.issuerParticipantsAdmin`)   
  
#### `issuerswitch.managedAccounts.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.viewer) (`roles/issuerswitch.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Issuerswitch Account Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.accountManagerAdmin) (`roles/issuerswitch.accountManagerAdmin`)   
  
#### `issuerswitch.managedAccounts.update`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Account Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.accountManagerAdmin) (`roles/issuerswitch.accountManagerAdmin`)   
  
#### `issuerswitch.mandateTransactions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.viewer) (`roles/issuerswitch.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Issuerswitch Transactions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.transactionsViewer) (`roles/issuerswitch.transactionsViewer`)   
  
#### `issuerswitch.metadataTransactions.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.viewer) (`roles/issuerswitch.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Issuerswitch Transactions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.transactionsViewer) (`roles/issuerswitch.transactionsViewer`)   
  
#### `issuerswitch.operations.cancel`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)   
  
#### `issuerswitch.operations.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)   
  
#### `issuerswitch.operations.get`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.viewer) (`roles/issuerswitch.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Issuerswitch Account Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.accountManagerAdmin) (`roles/issuerswitch.accountManagerAdmin`)  [Issuerswitch Account Manager Transactions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.accountManagerTransactionsAdmin) (`roles/issuerswitch.accountManagerTransactionsAdmin`)  [Issuerswitch Account Manager Transactions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.accountManagerTransactionsViewer) (`roles/issuerswitch.accountManagerTransactionsViewer`)  [Issuerswitch Resolutions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.resolutionsAdmin) (`roles/issuerswitch.resolutionsAdmin`)  [Issuerswitch Transactions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.transactionsViewer) (`roles/issuerswitch.transactionsViewer`)   
  
#### `issuerswitch.operations.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.viewer) (`roles/issuerswitch.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Issuerswitch Account Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.accountManagerAdmin) (`roles/issuerswitch.accountManagerAdmin`)  [Issuerswitch Account Manager Transactions Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.accountManagerTransactionsAdmin) (`roles/issuerswitch.accountManagerTransactionsAdmin`)  [Issuerswitch Account Manager Transactions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.accountManagerTransactionsViewer) (`roles/issuerswitch.accountManagerTransactionsViewer`)  [Issuerswitch Transactions Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.transactionsViewer) (`roles/issuerswitch.transactionsViewer`)   
  
#### `issuerswitch.operations.wait`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.viewer) (`roles/issuerswitch.viewer`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)   
  
#### `issuerswitch.ruleMetadata.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.viewer) (`roles/issuerswitch.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Issuerswitch Rules Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.rulesAdmin) (`roles/issuerswitch.rulesAdmin`)  [Issuerswitch Rules Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.rulesViewer) (`roles/issuerswitch.rulesViewer`)   
  
#### `issuerswitch.ruleMetadataValues.create`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Rules Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.rulesAdmin) (`roles/issuerswitch.rulesAdmin`)   
  
#### `issuerswitch.ruleMetadataValues.delete`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Rules Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.rulesAdmin) (`roles/issuerswitch.rulesAdmin`)   
  
#### `issuerswitch.ruleMetadataValues.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.viewer) (`roles/issuerswitch.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Issuerswitch Rules Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.rulesAdmin) (`roles/issuerswitch.rulesAdmin`)  [Issuerswitch Rules Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.rulesViewer) (`roles/issuerswitch.rulesViewer`)   
  
#### `issuerswitch.rules.list`

|  [Admin](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/admin`)  [Owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/owner`)  [Writer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/writer`)  [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`)  [Reader](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/reader`)  [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)  [Security Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)  [Security Reviewer](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityReviewer) (`roles/iam.securityReviewer`)  [Issuerswitch Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.admin) (`roles/issuerswitch.admin`)  [Issuerswitch Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.viewer) (`roles/issuerswitch.viewer`)  [Security Auditor](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.securityAuditor) (`roles/iam.securityAuditor`)  [Support User](https://docs.cloud.google.com/iam/docs/roles-permissions/jobfunctions#iam.supportUser) (`roles/iam.supportUser`)  [Issuerswitch Rules Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.rulesAdmin) (`roles/issuerswitch.rulesAdmin`)  [Issuerswitch Rules Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/issuerswitch#issuerswitch.rulesViewer) (`roles/issuerswitch.rulesViewer`)   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
