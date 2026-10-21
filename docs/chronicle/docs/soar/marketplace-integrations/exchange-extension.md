---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/exchange-extension/
title: Exchange Extension Pack \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:46:02.929115+00:00
---

# Exchange Extension Pack  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/exchange-extension/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Exchange Extension Pack

This document describes how to integrate Exchange Extension Pack with Google Security Operations.

## Configure the integration to work with Exchange

Depending on the mail server that the integration is configured for, the configuration steps are different.

Below are the configuration instructions for Microsoft 365 and on-premises Exchange starting from version 2016, earlier versions are not supported.

## Configure the integration to work with Microsoft 365

This integration uses PowerShell scripts to execute operations. The PowerShell package needs to be installed on the Google Security Operations server or the Google SecOps remote agent that uses Exchange Extension Pack integration.

Here is an example of how to configure PowerShell for CentOS7:

  1. Install the PowerShell package.
         
         > curl https://packages.microsoft.com/config/rhel/7/prod.repo | sudo tee /etc/yum.repos.d/microsoft.repo
         > sudo yum install -y powershell
         

  2. Open PowerShell interpreter and install Exchange Online PowerShell V3 and WSMan modules:
         
         > pwsh
         > Install-Module -Name ExchangeOnlineManagement -RequiredVersion 3.5.0 -Force -Scope AllUsers
         > Install-Module -Name PSWSMan
         > Install-WSMan
         > exit
         

  3. Go to <https://github.com/jborean93/omi/releases> to get the `libmi.so` and `libpsrpclient.so` files for openssl 1.1. Download the latest `glibc-1.1.tar.gz` release to the CentOS host.

  4. Extract the downloaded tar archive:
         
         > tar -xzvf glibc-1.1.tar.gz
         

  5. Overwrite existing the `libmi.so` and `libpsrpclient.so` files in the `/opt/microsoft/powershell/7` directory.




**Configure account**

Add the account that will be used with the integration to the _Discover Management_ admin role in the Exchange Admin Center.

**Assign permissions to the user**

Assign the _Compliance data administrator_ role to the user.

## Configure the integration to work with on-premises Exchange

The following instruction is applicable to Exchange 2016, earlier versions are not supported.

This integration uses PowerShell scripts to execute operations. The PowerShell package needs to be installed on the Google SecOps server or the Google SecOps remote agent that uses Exchange Extension Pack integration.

Here is an example of how to configure PowerShell for CentOS7:

  1. Install the PowerShell package.
         
         > curl https://packages.microsoft.com/config/rhel/7/prod.repo | sudo tee /etc/yum.repos.d/microsoft.repo
         > sudo yum install -y powershell
         

  2. Install the gssapi package.

The gssapi package is required for authentication from the Google SecOps Linux server or remote agent to the Windows server where Exchange is running over the PowerShell session.

Example of the gssapi installation for CentOS 7:
         
         > sudo yum install -y gssntlmssp
         

  3. Enable Powershell remoting on the Windows server where Exchange is running according to the [Enable-PSRemoting](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/enable-psremoting?view=powershell-7.1) document available within the Microsoft documentation.

  4. Enable Basic Authentication in Exchange.

This integration uses Basic Authentication that should be explicitly enabled in the Exchange server.

![Enable Basic Authentication in
Exchange](https://docs.cloud.google.com/static/chronicle/images/integrations/exchange-extension-pack-enable-basic-auth-in-exchange.png)

  5. Configure the account.

Account to use with the integration should be added to the "Discover Management" admin role in the Exchange Admin Center (EAC) console. To run the Mail Flow Rules action, you need to add a Transport Rules role to the relevant user:

     * Go to the EAC and click **permissions**.
     * Select **Discovery Management** and open it.

![Exchange Admin
    Center](https://docs.cloud.google.com/static/chronicle/images/integrations/exchange-extension-pack-select-discovery-management.png)

     * In the Roles section, click ![Add
icon](https://docs.cloud.google.com/static/chronicle/images/integrations/exchange-extension-pack-icon-add.png)**Add** and select **Transport Rules**.

![Navigate to Transport
    Rules](https://docs.cloud.google.com/static/chronicle/images/integrations/exchange-extension-pack-add-transport-rules.png)

     * Click **add - >**, then **OK** and **Save**.

![Add Transport
    Rules](https://docs.cloud.google.com/static/chronicle/images/integrations/exchange-extension-pack-click-add-ok-save.png)

     * The role is now added to the Assigned Roles section. It may take some time for permissions to replicate.

![Verify assigned
    roles](https://docs.cloud.google.com/static/chronicle/images/integrations/exchange-extension-pack-assigned-roles.png)




## Configure Exchange Extension Pack integration in Google SecOps

For detailed instructions on how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

### Integration parameters

Use the following parameters to configure the integration:

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Exchange On-Prem Server Address | String | x.x.x.x | No | Mail server address (hostname or IP) to connect to.  
Exchange Office365 Compliance Uri | String | https://ps.compliance.protection.outlook.com/powershell-liveid/ | No | Microsoft 365 Security Compliance Center PowerShell Uri to use to execute compliance operations. For more information, see the [Connect to Security Compliance PowerShell](https://docs.microsoft.com/en-us/powershell/exchange/connect-to-scc-powershell?view=exchange-ps) document.  
Exchange Office365 Online Powershell Uri | String | https://outlook.office365.com/powershell-liveid | No | Microsoft 365 Online Powershell Uri to use to execute Microsoft 365 management operations. For more information, see the [Connect to Security Compliance PowerShell](https://docs.microsoft.com/en-us/powershell/exchange/connect-to-scc-powershell?view=exchange-ps) document.  
Domain | String | example.com | No | Domain to authenticate with on mail server.  
User name | String | user | No | Username to authenticate with on mail server. In case of Microsoft 365 provide a user mail address as the username.  
Password | Password | N/A | No | A password to authenticate with on mail server.  
Is Exchange On-Prem? | Checkbox | Unchecked | No | Specify if the target mail server is Exchange On-Prem.  
Is Office365 (Exchange Online)? | Checkbox | Unchecked | No | Specify if the target mail server is Microsoft 365 (Exchange Online).  
**Note:** You can make changes at a later stage if needed. Once configured, the Instances can be used in Playbooks. For detailed information on configuring and supporting multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

### Delete Compliance Search

#### Description

Delete Compliance Search and any associated with it fetch results or purge emails tasks.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Compliance Search Name | String | N/A | Yes | Name for the Compliance Search to delete. The name shouldn't contain special characters.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If the action is successful, compliance search and actions are deleted (is_success=true):_ "Action successfully executed and compliance search and any associated with it fetch results or purge emails tasks were deleted."**The action should fail and stop a playbook execution:**___If target is Exchange on premises or Microsoft 365 but powershell is not installed on Google SecOps server:_ "Failed to execute action because powershell is not installed on Google SecOps server! Please see the configuration instructions on how to install powershell. Error is {0}".format(exception.stacktrace)___If target is Exchange on premises but gssntlmssp OS package is not installed on Google SecOps server:_ "Failed to execute action because gssntlmssp package is not installed on Google SecOps server! Please see the configuration instructions on how to install powershell. Error is {0}".format(exception.stacktrace)___If a fatal error, like wrong credentials, no connection to the server, other is reported_ : "Failed to execute action! Error is {0}".format(exception.stacktrace) | General  
  
### Fetch Compliance Search Results

#### Description

Fetch results for the completed Compliance Search.

**Note:** A maximum of 200 elements is displayed, but actual search can have more findings that are shown.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Compliance Search Name | String | N/A | Yes | Name for the Compliance Search. The name shouldn't contain special characters.  
Max Emails To Return | Integer | N/A | No | Specify the number of emails that the action can return.  
Remove Compliance Search Once Action Completes? | Checkbox | Checked | No | Specify whether the action should remove from Exchange server the search action and any related fetch or purge tasks once the action completes.  
Create Case Wall Output Table? | Checkbox | Checked | No | Specify if the action should create case wall output table. If the "Max Emails To Return" parameter is set to a greater number, its recommended to uncheck this to increase the action performance.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
      {
        "Location": "test@example.com",
        "Sender": "James Bond",
        "Subject": "search test",
        "Type": "Email",
        "Size": "61772",
        "Received Time": "3/12/2021 9:43:59 AM",
        "Data Link": "data/All/FLDR5402c62d-7730-4c93-8f34-6bxxxxxxxxxx/BATCH0000/MSG192bc965-18c9-4c06-8834-2cxxxxxxxxxx.eml",
        "Name": "test"
      },
      {
        "Location": "test@example.com",
        "Sender": "James Bond",
        "Subject": "search test 2",
        "Type": "Email",
        "Size": "60881",
        "Received Time": "3/12/2021 9:43:59 AM",
        "Data Link": "data/All/FLDR5402c62d-7730-4c93-8f34-6bxxxxxxxxxx/BATCH0000/MSG9eefda9c-b1b5-46f0-8a54-bdxxxxxxxxxx.eml",
        "Name": "test"
      }
    ]
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If the action is successful and compliance action is created (is_success=true):_ "Action was executed successfully and task to fetch compliance search results is created"_Once the action is completed:_ "Results for the Compliance Search {0} were successfully fetched".format(compliance search name)_If the action is not able to find compliance search based on the provided name (is_success=false):_ "Action was not able to find compliance search {0}".format(compliance_search_name)_If the action is failed because of some other non-critical error (is_success=false):_ "Action did not complete successfully due to errors. Errors information: {0}".format(error.stacktrace)**The action should fail and stop a playbook execution:**___If target is Exchange on prem or Microsoft 365 but powershell is not installed on Google SecOps server:_ "Failed to execute action because powershell is not installed on Google SecOps server! Please see the configuration instructions on how to install powershell. Error is {0}".format(exception.stacktrace)___If target is Exchange on prem but gssntlmssp OS package is not installed on Google SecOps server:_ "Failed to execute action because gssntlmssp package is not installed on Google SecOps server! Please see the configuration instructions on how to install powershell. Error is {0}".format(exception.stacktrace)___If a fatal error, like wrong credentials, no connection to the server, other is reported_ : "Failed to execute action! Error is {0}".format(exception.stacktrace) | General  
Table | **Table Title:** Compliance Search Action Results**Table Columns:**

  * Received Time
  * Sender
  * Recipient
  * Subject

| General  
  
### Ping

#### Description

Test connectivity to the Exchange or Microsoft 365 server with parameters provided at the integration configuration page in the Google SecOps Content Hub page.

#### Parameters

N/A

#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If successful:_ "Successfully connected to the Exchange or Microsoft 365 server with the provided connection parameters!"**The action should fail and stop a playbook execution:**___If none checkboxes are checked (Microsoft 365/exchange on prem):_ "Please specify type of mail server to connect to - Exchange on-prem or Microsoft 365"___If both checkboxes are checked (Microsoft 365/exchange on prem):_ "Only one mail server type is supported at a time. Please specify type of mail server to connect to - Exchange on-prem or Microsoft 365"___If target is Exchange on prem or Microsoft 365 but powershell is not installed on Google SecOps server:_ "Failed to execute action because powershell is not installed on Google SecOps server! Please see the configuration instructions on how to install powershell. Error is {0}".format(exception.stacktrace)___If target is Exchange on prem but gssntlmssp OS package is not installed on Google SecOps server:_ "Failed to execute action because gssntlmssp package is not installed on Google SecOps server! Please see the configuration instructions on how to install powershell. Error is {0}".format(exception.stacktrace)___If a fatal error, like wrong credentials, no connection to the server, other is reported_ : "Failed to execute action! Error is {0}".format(exception.stacktrace) | General  
  
### Purge Compliance Search Results

#### Description

Purge emails found by the completed Compliance Search.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Compliance Search Name | String | N/A | Yes | Name for the Compliance Search. The name shouldn't contain special characters.  
Perform a HardDelete for deleted emails? | Checkbox | Unchecked | No | Specify whether HardDelete should be performed. This option applies only to Microsoft 365 and marks emails for permanent removal from the mailbox.  
Remove Compliance Search Once Action Completes? | Checkbox | Checked | No | Specify whether the action should remove from Exchange server the search action and any related fetch or purge tasks once the action completes.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
      "Item count": "5",
      "Purge Type": "SoftDelete"
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If the action is successful and compliance action is created (is_success=true):_ "Action was executed successfully and task to purge emails found with the compliance search is created"_Once the action is completed:_ "Results for the Compliance Search {0} were successfully purged".format(compliance search name)_If the action is not able to find compliance search based on the provided name (is_success=false):_ "Action was not able to find compliance search {0}".format(compliance_search_name)_If the action does not return any results:_ "The Compliance Search {0} didn't return any results . Please update the search results or edit the Compliance search query and run the search again".format(compliance search name)**The action should fail and stop a playbook execution:**___If target is Exchange on premises or Microsoft 365 but powershell is not installed on Google SecOps server:_ "Failed to execute action because powershell is not installed on Google SecOps server! Please see the configuration instructions on how to install powershell. Error is {0}".format(exception.stacktrace)___If target is Exchange on premises but gssntlmssp OS package is not installed on Google SecOps server:_ "Failed to execute action because gssntlmssp package is not installed on Google SecOps server! Please see the configuration instructions on how to install powershell. Error is {0}".format(exception.stacktrace)___If a fatal error, like wrong credentials, no connection to the server, other is reported_ : "Failed to execute action! Error is {0}".format(exception.stacktrace) | General  
  
### Run Compliance Search

#### Description

Run Exchange Compliance Search based on the provided search conditions. If the fetch compliance search results checkbox is set, the action returns the search results similarly to the Fetch Compliance Search Results action.

Exchange Compliance Search provides a fast mechanism to search in multiple mailboxes that are most useful for large Organizations with 1000+ mailboxes.

**Note:** This action is not working on the Google SecOps entities.

If the "Fetch Compliance Search Results?" checkbox is checked, maximum of 200 elements is displayed, but actual search can have more findings that are shown.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Compliance Search Name | String | N/A | Yes | Name for the Compliance Search. The name shouldn't contain special characters.  
Subject Filter | String | N/A | No | Filter condition, specify the subject to search for emails.  
Sender Filter | String | N/A | No | Filter condition, specify who should be the sender of needed emails.  
Recipient Filter | String | N/A | No | Filter condition, specify who should be the recipient of needed emails.  
Operator | DDL | AND | Yes | Operator to use to construct query from conditions above.  
Time Frame (hours) | String | N/A | No | Time frame interval in hours to search for emails.  
Location to Search Emails In | String | N/A | Yes | Location to search emails in, can be one of the following:

  * A comma-separated list of mailboxes
  * A distribution group or mail-enabled security group
  * All - for all mailboxes in organization

  
Fetch Compliance Search Results? | Checkbox | Unchecked | No | Specify whether the action should immediately fetch the compliance search results. A maximum of 200 elements is displayed, but actual search can have more findings that are shown.  
Max Emails To Return | Integer | N/A | No | Specify the number of emails that the action can return.  
Create Case Wall Output Table? | Checkbox | Checked | No | Specify if the action should create case wall output table. If the "Max Emails To Return" parameter is set to a greater number, it's recommended to uncheck this to increase action performance.  
Advanced Query | String | N/A | No | Instead of subject, sender or recipient filters, provide a query you want to run compliance search on. For more information, see the [Keyword Query Language (KQL) syntax reference](https://docs.microsoft.com/en-us/sharepoint/dev/general-development/keyword-query-language-kql-syntax-reference) and [Message properties indexed by Exchange Search](https://docs.microsoft.com/en-us/exchange/message-properties-indexed-by-exchange-search-exchange-2013-help?redirectedfrom=MSDN) documents.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
      "Name": "test",
      "RunBy": "James Bond",
      "JobEndTime": "2021-03-18T12:42:49.92",
      "Status": "Completed"
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**_If the action is successful and compliance is created (is_success=true):_ "Action was executed successfully and compliance search is created"_Once the action completed the search:_ "Compliance Search {0} successfully completed".format(compliance search name)_If checkbox to fetch compliance search results is set:_ "Results for the Compliance Search {0} were successfully fetched".format(compliance search name)_If checkbox to fetch compliance search results is set, but the action does not return any results:_ "The Compliance Search {0} didn't return any results . Please update the search results or edit the Compliance search query and run the search again".format(compliance search name)**The action should fail and stop a playbook execution:**___If target is Exchange on prem or Microsoft 365 but powershell is not installed on Google SecOps server:_ "Failed to execute action because powershell is not installed on Google SecOps server! Please see the configuration instructions on how to install powershell. Error is {0}".format(exception.stacktrace)___If target is Exchange on prem but gssntlmssp OS package is not installed on Google SecOps server:_ "Failed to execute action because gssntlmssp package is not installed on Google SecOps server! Please see the configuration instructions on how to install powershell. Error is {0}".format(exception.stacktrace)___If a fatal error, like wrong credentials, no connection to the server, other is reported_ : "Failed to execute action! Error is {0}".format(exception.stacktrace) | General  
  
### Add Domains to Exchange-Siemplify Mail Flow Rules

#### Description

The action gets a list of Domains as a parameter and can create a new rule, filtering the domains from your Exchange Server. Actions to take can be modified in the parameters using rule parameters.

**Note:** To use this action, configure Organization Management permissions. For more information, see [Feature permissions in Exchange Online](https://docs.microsoft.com/en-us/exchange/permissions-exo/feature-permissions).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Domains | String | N/A | No | Specify the Domains you would like to add to the rule, in a comma-separated list.  
Rule to add Domains to | DDL | Siemplify - Domains List - Permanently Delete | Yes | Specify the rule to add the Domains to. If the rule doesn't exist, the action creates it where it's missing.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
      "success": [
        "test1.com",
        "test2.com"
      ],
      "already_available": [
        "test3.com"
      ],
      "invalid": [
        "invalid"
      ]
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:**_If successful (Rules are updated accordingly, inputs are right):_ "Added the following inputs to the corresponding rules:  
Domains:  
successfull_domainsRules updated:  
Rules_updated_names_list _If at least on of the inputs is not correct (invalid email address in the parameter, invalid mail in the entity name):_ "Could not add the following inputs to the rule:"+  
Unsuccessful_email_addresses**Action should fail and stop playbook execution:**_If an error is reported:_ "Error performing "Add Domains to Exchange-Siemplify Mail Flow Rules" action : {0}".format(exception.stacktrace) | General  
  
### Add Senders to Exchange-Siemplify Mail Flow Rules

#### Description

The action gets a list of Email Addresses as a parameter or works on the User entities with Email regexes (if parameters are not provided), and can create a new rule, filtering the senders from your Exchange Server. Actions can be modified in the parameters using the rule parameter.

**Note:** To use this action, configure Organization Management permissions. For more information, see the [Feature permissions in Exchange Online](https://docs.microsoft.com/en-us/exchange/permissions-exo/feature-permissions) document available within the Microsoft Product Documentation.

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Email Addresses | String | N/A | No | Specify the email addresses you would like to add to the rule, in a comma separated list. If no parameter is provided, the action works with the User entities.  
Rule to add senders to | DDL | Siemplify - Senders List - Permanently Delete | Yes | Specify the rule to add the sender to. If the rule doesn't exist, the action creates it where it's missing.  
Should add senders' domain to the corresponding Domains List rule as well? | Checkbox | Unchecked | No | Specify whether the action should automatically take the domains of the provided email addresses and add them as well to the corresponding domain rules (same rule action for domains).  
  
#### Run On

This action works on the User entity, if the email regex is valid for it, and if parameters are not provided.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
      "success": [
        "test1@example.com",
        "test2@example.com"
      ],
      "already_available": [
        "test3@example.com"
      ],
      "invalid": [
        "invalid"
      ]
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:**_If successful (Rules are updated accordingly, inputs are right):_ "Added the following inputs to the corresponding rules:  
Email Addresses:"+  
Successful_email_addresses+  
"Domains:"+  
successfull_domains+"Rules updated:"+  
rules_updated_names_list _If at least one of the inputs is not correct (invalid email address in the parameter, invalid email in the entity name):_ "could not add the following inputs to the rule:"+  
Unsuccessful_email_addresses**Action should fail and stop playbook execution:**_If an error is reported:_ "Error performing "Add Senders to Exchange-Siemplify Mail Flow Rule" action : {0}".format(exception.stacktrace) | General  
  
### Delete Exchange-Siemplify Mail Flow Rules

#### Description

The action gets a rule name as a parameter and deletes it.

**Note:** To use this action, configure Organization Management permissions. For more information, see [Feature permissions in Exchange Online](https://docs.microsoft.com/en-us/exchange/permissions-exo/feature-permissions).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Rule Name To Delete | DDL | Siemplify - Senders List - Permanently DeletePossible Values:

  * Siemplify - Senders List - Permanently Delete
  * Siemplify - Domains List - Permanently Delete
  * All available Exchange-Siemplify Mail Flow Rules

| Yes | Specify the Rule name you would like to completely delete.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    N/A
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:**_For successfully deleted rules:_ "Successfully deleted the following rules :" succesful_rule_names _In case rules are not found in Exchange:_ "Could not delete the following rules: "+unseccessful_rule_names+", since they were not found in Exchange. Please make sure you have chosen the appropriate rule names and try again."_In case of no rules found in Exchange:_ "Could not delete any of the provided rule names, since they were not found in Exchange. Please make sure you have chosen the appropriate rule names and try again."**Action should fail and stop playbook execution:**_If an error is reported:_ "Error performing "Delete Exchange-Siemplify Mail Flow Rules" action : {0}".format(exception.stacktrace) | General  
  
### List Exchange-Siemplify Mail Flow Rules

#### Description

The action gets a rule name as a parameter and lists it.

**Note:** To use this action, configure Organization Management permissions. For more information, see [Feature permissions in Exchange Online](https://docs.microsoft.com/en-us/exchange/permissions-exo/feature-permissions).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Rule Name To List | DDL | Siemplify - Senders List - Permanently Delete Possible Values:

  * Siemplify - Senders List - Permanently Delete
  * Siemplify - Domains List - Permanently Delete
  * All available Exchange-Siemplify Mail Flow Rules

| Yes | Specify the Rule name you would like to list.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    [
      {
        "Priority": 0,
        "ManuallyModified": false,
        "Description": "If the message:\r\n\tIs received from 'test@example1.com' or 'test@example2.com'\r\nTake the following actions:\r\n\tDelete the message without notifying the recipient or sender\r\n",
        "Conditions": [
          "Microsoft.Exchange.MessagingPolicies.Rules.Tasks.FromPredicate"
        ],
        "Actions": [
          "Microsoft.Exchange.MessagingPolicies.Rules.Tasks.DeleteMessageAction"
        ],
        "State": "Enabled",
        "Mode": "Enforce",
        "FromAddressContainsWords": null,
        "Identity": "Siemplify - Senders List - Permanently Delete",
        "Name": "Siemplify - Senders List - Permanently Delete",
        "DistinguishedName": "CN=Siemplify - Senders List - Permanently Delete,CN=TransportVersioned,CN=Rules,CN=Transport Settings,CN=mwc,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=exlab,DC=local",
        "IsValid": true,
        "From": [
          "test@example1.com",
          "test@example2.com"
        ],
        "Guid": "xxxxx426-b665-41f9-82e0-0f1fd63xxxxx",
        "ImmutableId": "xxxxx426-b665-41f9-82e0-0f1fd63xxxxx",
        "WhenChanged": "/Date(1621952909000)/",
        "ExchangeVersion": "0.1 (8.0.535.0)",
        "OrganizationId": "",
        "ObjectState": "Unchanged"
      },
      {
        "Priority": 1,
        "ManuallyModified": false,
        "Description": "If the message:\r\n\tIncludes these words in the sender's address: 'example1.com' or 'example2.com'\r\nTake the following actions:\r\n\tDelete the message without notifying the recipient or sender\r\n",
        "Conditions": [
          "Microsoft.Exchange.MessagingPolicies.Rules.Tasks.FromAddressContainsPredicate"
        ],
        "Actions": [
          "Microsoft.Exchange.MessagingPolicies.Rules.Tasks.DeleteMessageAction"
        ],
        "State": "Enabled",
        "Mode": "Enforce",
        "FromAddressContainsWords": [
          "example1.com",
          "example2.com"
        ],
        "Identity": "Siemplify - Domains List - Permanently Delete",
        "Name": "Siemplify - Domains List - Permanently Delete",
        "DistinguishedName": "CN=Siemplify - Domains List - Permanently Delete,CN=TransportVersioned,CN=Rules,CN=Transport Settings,CN=mwc,CN=Microsoft Exchange,CN=Services,CN=Configuration,DC=exlab,DC=local",
        "IsValid": true,
        "From": null,
        "Guid": "xxxxx697-e143-41aa-8dee-b783a78xxxxx",
        "ImmutableId": "xxxxx697-e143-41aa-8dee-b783a78xxxxx",
        "WhenChanged": "/Date(1621952960000)/",
        "ExchangeVersion": "0.1 (8.0.535.0)",
        "OrganizationId": "",
        "ObjectState": "Unchanged"
      }
    ]
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:******_For successfully found rules:_ "Successfully listed the following rules :" succesful_rule_names _In case rules are not found in Exchange:_ "Could not list the following rules: "+unseccessful_rule_names+", since they were not found in Exchange. Please make sure you have chosen the appropriate rule names and try again."_In case no rules are found in Exchange:_ "Could not list any of the provided rule names, since they were not found in Exchange. Please make sure you have chosen the appropriate rule names and try again."**The action should fail and stop a playbook execution:******_If an error is reported:_ "Error performing "List Exchange-Siemplify Mail Flow Rules" action : {0}".format(exception.stacktrace) | General  
  
### Remove Domains from Exchange-Siemplify Mail Flow Rules

#### Description

The action gets a list of Domains as a parameter and can remove the provided domains from the existing rules.

**Note:** To use this action, configure Organization Management permissions. For more information, see [Feature permissions in Exchange Online](https://docs.microsoft.com/en-us/exchange/permissions-exo/feature-permissions).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Domains | String | N/A | No | Specify the Domains you would like to remove from the rule, in a comma-separated list. If no parameter is provided, the action works with entities.  
Rule to remove Domains from | DDL | Siemplify - Domains List - Permanently Delete | Yes | Specify the rule to remove the Domains from. If the rule doesn't exist, the action does nothing.  
Remove Domains from all available Rules | Checkbox | Unchecked | No | Specify whether the action should look for the provided domains in all of the Google SecOps Mail Flow rules.  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
      "success": [
        "test1.com",
        "test2.com"
      ],
      "didn't_exist": [
        "test3.com"
      ],
      "invalid": [
        "invalid"
      ]
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:**_If successful (Rules are updated accordingly, inputs are right):_ "Removed the following inputs from the corresponding rules:"  
Domains:  
successfull_domainsRules updated:  
Rules_updated_names_list**Action should fail and stop playbook execution:**_If an error is reported:_ "Error performing "Remove Domains from Exchange-Siemplify Mail Flow Rules" action : {0}".format(exception.stacktrace) | General  
  
### Remove Senders from Exchange-Siemplify Mail Flow Rules

#### Description

The action gets a a list of Senders as a parameter or works on the User entities (if parameters are not provided), and can remove the provided Senders from the existing rules.

**Note:** To use this action, configure Organization Management permissions. For more information, see [Feature permissions in Exchange Online](https://docs.microsoft.com/en-us/exchange/permissions-exo/feature-permissions).

#### Parameters

Parameter Display Name | Type | Default Value | Is Mandatory | Description  
---|---|---|---|---  
Senders | String | N/A | No | Specify the Senders you would like to remove from the rule, in a comma-separated list. If no parameter is provided, the action works with entities.  
Rule to remove Senders from | DDL | Siemplify Senders List - Permanently Delete | Yes | Specify the rule to remove the Senders from. If the rule doesn't exist, the action does nothing.  
Should remove senders' domains from the corresponding Domains List rule as well? | Checkbox | Unchecked | No | Specify whether the action should automatically take the domains of the provided email addresses and remove them as well from the corresponding domain rules (same rule action for domains).  
  
#### Run On

This action doesn't run on entities.

#### Action Results

##### Script Result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
##### JSON Result
    
    
    {
      "success": [
        "test1@example.com",
        "test2@example.com"
      ],
      "didn't_exist": [
        "test3@example.com"
      ],
      "invalid": [
        "invalid"
      ]
    }
    

##### Case Wall

Result type | Value / Description | Type  
---|---|---  
Output message* | **Action should not fail and not stop playbook execution:**_If successful (Rules are updated accordingly, inputs are right):_ message: "Removed the following inputs from the corresponding rules:"  
Senders :  
successfull_sendersRules updated:  
rules_updated_names_list _If at least on of the inputs is not correct (invalid email address in the parameter, invalid email in the entity name):_ "could not add the following inputs to the rule:"+  
Unsuccessful_email_addresses**Action should fail and stop playbook execution:**_If an error is reported:_ "Error performing "Remove Senders from Exchange-Siemplify Mail Flow Rules" action : {0}".format(exception.stacktrace) | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-18 UTC."],[],[]] 
