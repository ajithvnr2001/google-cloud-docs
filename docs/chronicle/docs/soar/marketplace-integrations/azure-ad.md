---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/azure-ad/
title: Integrate Microsoft Entra ID with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:10:54.765201+00:00
---

# Integrate Microsoft Entra ID with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/azure-ad/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Microsoft Entra ID with Google SecOps

This document provides guidance on how to integrate Microsoft Entra ID with Google Security Operations (Google SecOps).

**Important:** Azure Active Directory was renamed to Microsoft Entra ID. In the Google SecOps platform, the integration for Microsoft Entra ID is called _Azure Active Directory_.

This integration uses one or more open source components. You can download a zipped copy of the full source code of this integration from the [Cloud Storage bucket](https://storage.googleapis.com/csoar_public_integrations/AzureActiveDirectory.zip).

## Use cases

Integrating Microsoft Entra ID with Google SecOps can help you solve the following use cases:

  * **User account management:** use the Google SecOps capabilities to automate the disabling and enabling of user accounts in Microsoft Entra ID based on security events, such as suspected compromise or employee offboarding.

  * **Password reset:** use the Google SecOps capabilities to orchestrate password resets for compromised accounts or users locked out of their accounts. Resetting passwords can help you streamline the password recovery process and reduce help desk tickets.

  * **Group management:** use the Google SecOps capabilities to automate creating, modificating, and deleting Microsoft Entra ID groups.

  * **Conditional access policy enforcement:** use the Microsoft Entra ID conditional access policies within Google SecOps playbooks to dynamically control access based on context and allow for granular control over access to resources based on factors like location, device, and user risk.

  * **Security alerting and incident response:** integrate the Microsoft Entra ID security alerts into Google SecOps to automate incident response workflows.




## Before you begin

Before you configure the integration in Google SecOps, verify that you have the following requirements met in your Microsoft environment:

  * **Azure App Registration** : You must register an application in the Microsoft Entra admin center to obtain a Client ID and Tenant ID.

For detailed instructions, see the [Register an application in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app).

  * **API permissions** : Grant the following **Microsoft Graph > Application permissions** to your app and provide admin consent:

    * `Directory.Read.All`
    * `Directory.ReadWrite.All`
    * `Group.ReadWrite.All`
    * `User.ReadWrite.All`
    * `AuditLog.Read.All` (Required to use the **Include MFA Details** parameter)
  * **Role assignments** : To run password-related actions, such as Force Password Update or Reset User Password, you must assign the `Password Administrator` role to your application within Microsoft Entra ID.

  * **Client secret** : Generate a client secret in the **Certificates & secrets** section of your Azure app. Save the secret Value (not the Secret ID) immediately, as it's only displayed once and is required for configuration.




## Integration parameters

The Microsoft Entra ID integration requires the following parameters:

Parameter | Description  
---|---  
`Login API Root` | _Optional_ The API root used to authenticate with the Microsoft identity platform. The default value is `https://login.microsoftonline.com`.  
`API Root` | _Optional_ The API root of the Azure Active Directory instance. The default value is `https://graph.microsoft.com`.  
`Client ID` | _Required_ The application (client) ID value of your Microsoft Entra ID account.  
`Client Secret` | _Required_ The client secret value of your Microsoft Entra ID account.  
`Directory ID` | _Required_ The directory (tenant) ID value of your Microsoft Entra ID account.  
`Verify SSL` | _Optional_ If selected, the integration verifies that the SSL certificate used to connect to the Microsoft Entra ID server is valid. Selected by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add User to a Group

Use the **Add User to a Group** action to add a user to the specific Microsoft Entra ID group. This action expects you to configure the `User` entity in the `username@domain` format.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **Add User to a Group** action requires the following parameters:

Parameter | Description  
---|---  
`Group ID` | _Required_ The ID of the Microsoft Entra ID group to add the user to, such as `00e40000-1971-439d-80fc-d0e000001dbd`.  
  
#### Action outputs

The **Add User to a Group** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Add User to a Group** action can return the following output messages:

Output message | Message description  
---|---  
`Member USER_ID was added to the group GROUP_ID successfully.` `Some errors occurred. Please check the logs.` | The action succeeded.  
`Member could not be added successfully. ` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add User to a Group** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Disable Account

Use the **Disable Account** action to disable an account in Microsoft Entra ID. This action expects you to configure the `User` entity in the `username@domain` format.

To run the **Disable Account** action, grant administrative privileges to the Microsoft Entra ID account that you use in the integration.

This action runs on the Google SecOps `User` entity.

#### Configure additional permissions

The **Disable Account** action requires you to additionally configure the following API permission for the application:

  * `User.EnableDisableAccount.All`



For guidance on how to configure API permissions in Microsoft Entra ID, see the Configure API permissions section of this document.

#### Action inputs

None.

#### Action outputs

The **Disable Account** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Disable Account** action can return the following output messages:

Output message | Message description  
---|---  
`User account disabled successfully.` `Some errors occurred. Please check the logs.` | The action succeeded.  
`Disable user account was not successful.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Disable Account** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Enable Account

Use the **Enable Account** action to enable an account in Microsoft Entra ID. This action expects you to configure the `User` entity in the `username@domain` format.

This action runs on the Google SecOps `User` entity.

#### Configure additional permissions

The **Enable Account** action requires you to additionally configure the following API permission for the application:

  * `User.EnableDisableAccount.All`



For guidance on how to configure API permissions in Microsoft Entra ID, see the Configure API permissions section of this document.

#### Action inputs

None.

#### Action outputs

The **Enable Account** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Enable Account** action can return the following output messages:

Output message | Message description  
---|---  
`User account was enabled successfully.` `Some errors occurred. Please check the logs.` | The action succeeded.  
`Enable user account was not successful.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enable Account** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Enrich Host

Use the **Enrich Host** action to enrich the Google SecOps `Host` entity with information from Microsoft Entra ID. This action finds a match for a provided `Host` entity using on the device `displayName` field in Microsoft Entra ID.

This action runs on the Google SecOps `Host` entity.

#### Action inputs

None.

#### Action outputs

The **Enrich Host** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Entity enrichment table

The **Enrich Host** action supports the following entity enrichment:

Enrichment field | Logic  
---|---  
`AAD_Name` | Returns if it exists in the JSON result.  
`AAD_Enabled` | Returns if it exists in the JSON result.  
`AAD_Property Device ID` | Returns if it exists in the JSON result.  
`AAD_OS` | Returns if it exists in the JSON result.  
`AAD_Version` | Returns if it exists in the JSON result.  
`AAD_Profile Type` | Returns if it exists in the JSON result.  
`AAD_Compliant` | Returns if it exists in the JSON result.  
`AAD_Last Sign In` | Returns if it exists in the JSON result.  
  
##### JSON result

The following example shows the JSON result output received when using the **Enrich Host** action:
    
    
    [
        {
            "EntityResult": {
                "deletedDateTime": "1234569",
                "complianceExpirationDateTime": "1234567",
                "profileType": "RegisteredDevice",
                "key": "007",
                "if":"889922-aaaa-123123"
            },
            "Entity": "us-lt-v13001"
        }
    ]
    

##### Output messages

The **Enrich Host** action can return the following output messages:

Output message | Message description  
---|---  
`Host details were fetched successfully: HOSTNAME.` `Some errors occurred. Please check log.` | The action succeeded.  
`Host details were not found.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enrich Host** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Enrich User

Use the **Enrich User** action to enrich the Google SecOps `User` entity with information from Microsoft Entra ID. This action expects you to configure the `User` entity in the `username@domain` format.

This action runs on the Google SecOps `Host` entity.

#### Action inputs

The **Enrich User** action requires the following parameters:

Parameter | Description  
---|---  
`Include MFA Details` | Optional. If selected, the action returns MFA details about the user. **Note:** This parameter requires the `AuditLog.Read.All` Microsoft Graph application permission in your Azure App Registration.   
`Include Last Sign In Details` | Optional. If selected, the action retrieves the user's sign-in activity (including both interactive and non-interactive sign-in timestamps).  
  
#### Action outputs

The **Enrich User** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Entity enrichment table

The **Enrich User** action supports the following entity enrichment:

Enrichment field | Logic  
---|---  
`AAD_Name` | Returns if it exists in the JSON result.  
`AAD_Mobile Phone` | Returns if it exists in the JSON result.  
`AAD_Preferred Language` | Returns if it exists in the JSON result.  
`AAD_Job Title` | Returns if it exists in the JSON result.  
`AAD_Username` | Returns if it exists in the JSON result.  
  
##### JSON result

The following example shows the JSON result output received when using the **Enrich User** action:
    
    
    [
      {
        "Entity": "user@domain.com",
        "EntityResult": {
          "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users/$entity",
          "accountEnabled": true,
          "ageGroup": null,
          "businessPhones": [],
          "city": "New York",
          "companyName": "ExampleCorp",
          "consentProvidedForMinor": null,
          "country": "US",
          "createdDateTime": "2025-01-01T00:00:00Z",
          "creationType": null,
          "department": "Security",
          "displayName": "User Name",
          "mail": "user@domain.com",
          "employeeId": "12345",
          "employeeHireDate": null,
          "employeeType": null,
          "externalUserStateChangeDateTime": null,
          "faxNumber": null,
          "givenName": "User",
          "imAddresses": [],
          "externalUserState": null,
          "jobTitle": "Security Analyst",
          "surname": "Surname",
          "lastPasswordChangeDateTime": "2025-01-01T00:00:00Z",
          "legalAgeGroupClassification": null,
          "mailNickname": "usernickname",
          "mobilePhone": "+11234567890",
          "id": "user-id-12345",
          "officeLocation": null,
          "onPremisesSamAccountName": null,
          "onPremisesDistinguishedName": null,
          "onPremisesDomainName": null,
          "onPremisesImmutableId": null,
          "onPremisesLastSyncDateTime": null,
          "onPremisesProvisioningErrors": [],
          "onPremisesSecurityIdentifier": null,
          "onPremisesSyncEnabled": null,
          "onPremisesUserPrincipalName": null,
          "otherMails": [],
          "passwordPolicies": "None",
          "preferredDataLocation": null,
          "preferredLanguage": "en-US",
          "proxyAddresses": [],
          "signInSessionsValidFromDateTime": "2025-01-01T00:00:00Z",
          "state": "NY",
          "streetAddress": "123 Main St",
          "usageLocation": "US",
          "userPrincipalName": "user@domain.com",
          "userType": "Member",
          "postalCode": "10001",
          "deletedDateTime": null,
          "showInAddressList": null,
          "isResourceAccount": null,
          "refreshTokensValidFromDateTime": "2025-01-01T00:00:00Z",
          "employeeOrgData": null,
          "passwordProfile": null,
          "authorizationInfo": {
            "certificateUserIds": []
          },
          "mfa_details": {
            "id": "user-id-12345",
            "userPrincipalName": "user@domain.com",
            "userDisplayName": "User Name",
            "userType": "member",
            "isAdmin": false,
            "isSsprRegistered": true,
            "isSsprEnabled": true,
            "isSsprCapable": true
            "isMfaRegistered": true,
            "isMfaCapable": true,
            "isPasswordlessCapable": false,
            "methodsRegistered": [
              "email",
              "mobilePhone"
            ],
            "defaultMfaMethod": "mobilePhone",
            "isSystemPreferredAuthenticationMethodEnabled": false,
            "systemPreferredAuthenticationMethods": [],
            "userPreferredMethodForSecondaryAuthentication": "oath",
            "lastUpdatedDateTime": "2026-01-01T00:00:00Z"
          }
        }
      }
    ]
    

##### Output messages

The **Enrich User** action can return the following output messages:

Output message | Message description  
---|---  
`User details were fetched successfully: USERNAME.` `Some errors occurred. Please check the logs.` | The action succeeded.  
`Users list fetch was not successful.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Enrich User** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Force Password Update

Use the **Force Password Update** action to force a password update for the user. This action requires the user to change their password on the next sign-in attempt.

The **Force Password Update** action expects you to configure the `User` entity in the `username@domain` format.

This action runs on the Google SecOps `User` entity.

#### Configure additional permissions

The **Force Password Update** action requires you to additionally configure the following API permission for the application:

  * `User-PasswordProfile.ReadWrite.All`



For guidance on how to configure API permissions in Microsoft Entra ID, see the Configure API permissions section of this document.

#### Assign a role to your application

The **Force Password Update** action requires you to assign the `Password Administrator` role to your application.

To assign the `Password Administrator` role to your application, complete the following steps:

  1. Sign in to the Azure portal using your Microsoft account.
  2. In **Microsoft Entra ID** , search for **Roles and administrators**.
  3. Select or search for the `Password Administrator` role from the list.
  4. Click **Add Assignment**.
  5. Select an account (member) that you use in the integration and click **Next**.
  6. Enter justification for assigning a role.
  7. Click **Assign**.



#### Action inputs

None.

#### Action outputs

The **Force Password Update** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Force Password Update** action can return the following output messages:

Output message | Message description  
---|---  
`Force password update on the user was successful.` `Some errors occurred. Please check the logs.` | The action succeeded.  
`Attempt to Force user password update was not successful.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Force Password Update** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Manager Contact Details

Use the **Get Manager Contact Details** action to obtain the manager contact details for the user.

The **Get Manager Contact Details** action expects you to configure the `User` entity in the `username@domain` format.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **Get Manager Contact Details** action requires the following parameter:

Parameter | Description  
---|---  
`Fields To Return` | Optional. A comma-separated list of specific manager profile attributes to retrieve. If no value is provided, the action returns the default set of attributes defined by the API. The default value is `accountEnabled,ageGroup,assignedLicenses, businessPhones,city,companyName,consentProvidedForMinor,country, createdDateTime,creationType,department,displayName,mail,employeeId, employeeHireDate,employeeOrgData,employeeType,onPremisesExtensionAttributes, externalUserStateChangeDateTime,faxNumber,givenName,imAddresses,identities, externalUserState,jobTitle,surname,lastPasswordChangeDateTime, legalAgeGroupClassification,mailNickname,mobilePhone,id,officeLocation, onPremisesSamAccountName,onPremisesDistinguishedName,onPremisesDomainName, onPremisesImmutableId,onPremisesLastSyncDateTime, onPremisesProvisioningErrors,onPremisesSecurityIdentifier, onPremisesSyncEnabled,onPremisesUserPrincipalName,otherMails, passwordPolicies,passwordProfile,preferredDataLocation,preferredLanguage, proxyAddresses,signInSessionsValidFromDateTime,sponsors,state,streetAddress, usageLocation,userPrincipalName,userType,postalCode,authorizationInfo, deletedDateTime,showInAddressList,isResourceAccount, refreshTokensValidFromDateTime`.  
`Include MFA Details` | Optional. If selected, the action returns MFA details about the user. **Note:** This parameter requires the `AuditLog.Read.All` Microsoft Graph application permission in your Azure App Registration.   
`Include Last Sign In Details` | Optional. If selected, the action retrieves the user's sign-in activity (including both interactive and non-interactive sign-in timestamps).  
  
#### Action outputs

The **Get Manager Contact Details** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **Get Manager Contact Details** action can return the following table in Google SecOps:

Table name: **Manager contact**

Columns:

  * **Name**
  * **Phone number**



##### Entity enrichment table

The **Get Manager Contact Details** action supports the following entity enrichment:

Enrichment field | Logic  
---|---  
`Display Name` | Returns if it exists in the JSON result.  
`Mobile Phone` | Returns if it exists in the JSON result.  
`@odata.context` | Returns if it exists in the JSON result.  
`AAD_Job Title` | Returns if it exists in the JSON result.  
`AAD_Username` | Returns if it exists in the JSON result.  
  
##### JSON result

The following example shows the JSON result output received when using the **Get Manager Contact Details** action:
    
    
    [
      {
        "Entity": "user@example.com",
        "EntityResult": {
          "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#users/$entity",
          "accountEnabled": true,
          "ageGroup": null,
          "businessPhones": [],
          "city": "Anytown",
          "companyName": "Example Corporation",
          "consentProvidedForMinor": null,
          "country": "US",
          "createdDateTime": "2025-01-01T00:00:00Z",
          "creationType": null,
          "department": "Security Operations",
          "displayName": "Internal User",
          "mail": "user@example.com",
          "employeeId": "ID-00001",
          "employeeHireDate": null,
          "employeeType": "Full-time",
          "externalUserStateChangeDateTime": null,
          "faxNumber": null,
          "givenName": "Alex",
          "imAddresses": [],
          "externalUserState": null,
          "jobTitle": "Security Lead",
          "surname": "Doe",
          "lastPasswordChangeDateTime": "2025-01-01T00:00:00Z",
          "legalAgeGroupClassification": null,
          "mailNickname": "alexdoe",
          "mobilePhone": "+1 555-0100",
          "id": "00000000-0000-0000-0000-000000000000",
          "officeLocation": null,
          "usageLocation": "US",
          "userPrincipalName": "user@example.com",
          "userType": "Member",
          "postalCode": "00000",
          "deletedDateTime": null,
          "showInAddressList": null,
          "isResourceAccount": null,
          "refreshTokensValidFromDateTime": "2025-01-01T00:00:00Z",
          "employeeOrgData": null,
          "authorizationInfo": {
            "certificateUserIds": []
          },
          "sponsors": [],
          "mfa_details": {
            "id": "00000000-0000-0000-0000-000000000000",
            "userPrincipalName": "user@example.com",
            "userDisplayName": "Internal User",
            "userType": "member",
            "isAdmin": true,
            "isSsprRegistered": false,
            "isSsprEnabled": true,
            "isSsprCapable": false,
            "isMfaRegistered": true,
            "isMfaCapable": true,
            "isPasswordlessCapable": false,
            "methodsRegistered": [
              "mobilePhone",
              "softwareOneTimePasscode"
            ],
            "defaultMfaMethod": "softwareOneTimePasscode",
            "isSystemPreferredAuthenticationMethodEnabled": true,
            "systemPreferredAuthenticationMethods": [
              "SoftwareOTP"
            ],
            "userPreferredMethodForSecondaryAuthentication": "oath",
            "lastUpdatedDateTime": "2026-01-01T00:00:00Z"
          }
        }
      }
    ]
    

##### Output messages

The **Get Manager Contact Details** action can return the following output messages:

Output message | Message description  
---|---  
`User manager details were fetched successfully.` `Some errors occurred. Please check the logs.` | The action succeeded.  
`Could not fetch user manager's details successfully.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Manager Contact Details** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Is User in Group

Use the **Is User in Group** action to check if the user has membership in a specific Microsoft Entra ID group. This action expects you to configure the `User` entity in the `username@domain` format.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **Is User in Group** action requires the following parameters:

Parameter | Description  
---|---  
`Group ID` | _Required_ The ID of the Microsoft Entra ID group to add the user to, such as `00e40000-1971-439d-80fc-d0e000001dbd`.  
  
#### Action outputs

The **Is User in Group** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Is User in Group** action:
    
    
    [
        {
            "EntityResult": "true",
            "Entity": "user@example.com"
        }
    ]
    

##### Output messages

The **Is User in Group** action can return the following output messages:

Output message | Message description  
---|---  
`The following user was found in the group: USER_ID.` `Some errors occurred. Please check the logs.` | The action succeeded.  
`User was not found in the group.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Is User in Group** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Groups

Use the **List Groups** action to list Microsoft Entra ID groups using the specified search criteria.

For the **List Groups** action, filtering works with the `Name` field.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **List Groups** action requires the following parameters:

Parameter | Description  
---|---  
`Order By` | _Optional_ The order to sort the returned groups by their name. The default value is `ASC`. The possible values are as follows:

  * `DESC`
  * `ASC`

  
`Results Limit` | _Optional_ The maximum number of groups to return.  
`Filter Logic` | _Optional_ The logic to filter groups by their name. The default value is `Equal`. The possible values are as follows:

  * `Equal`
  * `Contains`

  
`Filter Value` | _Optional_ The value to filter groups using the selected filter logic. This value applies to the group name. If you select `Equal`, the action attempts to find the exact match among results. If you select `Contain`, the action attempts to find results that contain the provided substring. If you don't set a value, the filter doesn't apply.  
  
#### Action outputs

The **List Groups** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **List Groups** action can return the following table in Google SecOps:

Table name: **Groups**

Columns:

  * **Name**
  * **ID**
  * **Description**
  * **Mail**
  * **Created Time**
  * **Group Type**



##### Entity enrichment table

The **List Groups** action supports the following entity enrichment:

Enrichment field | Logic  
---|---  
`Group Type` | Returns if it exists in the JSON result.  
`ID` | Returns if it exists in the JSON result.  
`Name` | Returns if it exists in the JSON result.  
`Description` | Returns if it exists in the JSON result.  
`Created Time` | Returns if it exists in the JSON result.  
  
##### JSON result

The following example shows the JSON result output received when using the **List Groups** action:
    
    
    [
      {
        "Group_Type": "managed",
        "Id": "1212-12312-123",
        "Name": "Group Name",
        "Description": "This group is ...",
        "Created_Time": "2019-10-24T19:10:18Z",
        "onPremisesSamAccountName": "alext"
      }
    ]
    

##### Output messages

The **List Groups** action can return the following output messages:

Output message | Message description  
---|---  
`Groups list was fetched successfully.` `Some errors occurred. Please check the logs.` | The action succeeded.  
`Groups list fetch was not successful.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Groups** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Members in the Group

Use the **List Members in the Group** action to list members in the specified Microsoft Entra ID group.

The filtering logic works based on the `Filter Key` parameter value.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **List Members in the Group** action requires the following parameters:

Parameter | Description  
---|---  
`Max Records To Return` | _Optional_ The maximum number of records to return. The default value is 50.  
`Group Name` | _Optional_ The name of the Microsoft Entra ID group to list members.  
`Group ID` | _Optional_ The ID of the Microsoft Entra ID group to list members. If you configure both the `Group Name` and `Group ID` parameters, the action uses the `Group ID` parameter value.  
`Filter Key` | _Optional_ The field to filter group members by, such as `User Display Name`. The possible values are as follows:

  * `Select One`
  * `User Display Name`
  * `User Principal Name`
  * `User Mail Name`

  
`Filter Logic` | _Optional_ The logic to apply to the filter. The possible values are as follows:

  * `Not Specified`
  * `Equal`
  * `Contains`

  
`Filter Value` | _Optional_ The value to use for filtering group members based on the selected `Filter Key` and `Filter Logic` parameter values. If you select `Equal`, the action attempts to find the exact match among results. If you select `Contain`, the action attempts to find results that contain the provided substring. If you don't set a value, the filter doesn't apply.  
  
#### Action outputs

The **List Members in the Group** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **List Members in the Group** action can return the following table in Google SecOps:

Table name: **Available members of the group**

Columns:

  * **ID**
  * **User Principal Name**
  * **Display Name**
  * **Surname**
  * **Given Name**
  * **Mail**
  * **Job Title**
  * **Business Phones**
  * **Mobile Phone**
  * **Office Location**
  * **Preferred Language**



##### JSON result

The following example shows the JSON result output received when using the **List Members in the Group** action:
    
    
    [
      {
        "@odata.type": "#microsoft.graph.user",
        "id": "b786d3cf-e97d-4511-b61c-0559e9f4da75",
        "businessPhones": [],
        "displayName": "Alex T",
        "givenName": "Alex",
        "jobTitle": "Software Engineer",
        "mail": "alex.t@example.com",
        "mobilePhone": null,
        "officeLocation": "Building A",
        "preferredLanguage": "en-US",
        "surname": "T",
        "userPrincipalName": "alex.t@example.com"
      }
    ]
    

##### Output messages

The **List Members in the Group** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully found members for the provided criteria in Azure AD group.` `No members were found for the provided criteria in Azure AD group.` `The filter was not applied, because parameter "Filter Value" has an empty value.` | The action succeeded.  
`Error executing action "List Members in the Group". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Members in the Group** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List User's Groups Membership

Use the **List User's Groups Membership** action to list the Microsoft Entra ID groups of which the user is a member.

You can provide the username as an entity or an action input parameter. If you configure the username as both the entity and the input parameter, the action uses the input parameter.

To configure the username, follow the `username@domain` format.

This action runs on the Google SecOps `Username` entity.

#### Action inputs

The **List User's Groups Membership** action requires the following parameters:

Parameter | Description  
---|---  
`User Name` | _Optional_ A comma-separated list of usernames to retrieve group memberships for, such as `username@domain`. If you don't set a value, the action uses the user identifiers from the `Username` entity.  
`Return Only Security Enabled Groups` | _Optional_ If selected, the action returns only security-enabled groups to which the user belongs.Not selected by default.  
`Return Detailed Groups Information` | _Optional_ If selected, the action returns detailed information about the Microsoft Entra ID groups.Not selected by default.  
`Filter Key` | _Optional_ The key to use for filtering groups. The default value is `Select One`. The possible values are as follows:

  * `Select One`
  * `Group Display Name`
  * `Group Description`

  
`Filter Logic` | _Optional_ The logic to apply when filtering the groups. The default value is `Not Specified`. Possible values are as follows:

  * `Not Specified`
  * `Equal`
  * `Contains`

  
`Filter Value` | _Optional_ The value to use for filtering groups. If you select `Equal`, the action attempts to find the exact match among results. If you select `Contain`, the action attempts to find results that contain the provided substring. If you don't set a value, the filter doesn't apply.  
`Max Records To Return` | _Optional_ The maximum number of records to return. If you don't set a value, the action returns 50 records by default.  
  
#### Action outputs

The **List User's Groups Membership** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **List User's Groups Membership** action can return the following table in Google SecOps:

Table name: **Group Memberships**

Columns:

  * **ID**
  * **Display Name**
  * **Description**
  * **Security Enabled**
  * **Security Identifier**
  * **Created DateTime**
  * **Classification**
  * **Visibility**
  * **Mail**
  * **Mail Enabled**
  * **Mail Nickname**



##### JSON result

The following example shows the JSON result output received when using the **List User's Groups Membership** action:
    
    
    {
        "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#Collection(Edm.String)",
        "value": [
            "ID",
            "ID",
            "ID",
        ]
    }
    

##### Output messages

The **List User's Groups Membership** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully found groups for the provided criteria for the following entities: ENTITY_ID ` `The following entities were not found in the Azure AD: ENTITY_ID` `No groups were found in Azure Active Directory for the following entities: ENTITY_ID` `The filter was not applied, because parameter "Filter Value" has an empty value.` | The action succeeded.  
`Error executing action "List User's Groups Membership". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List User's Groups Membership** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List Users

Use the **List Users** action to list Microsoft Entra ID users using the specified search criteria.

For the **List Users** action, filtering works with the `Username` (`userPrincipalName`) field.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **List Users** action requires the following parameters:

Parameter | Description  
---|---  
`Filter` | _Optional_ The fields to include in the results. The default value is `All Fields`. The possible values are as follows:

  * `All Fields`
  * `displayName`
  * `userPrincipalName`
  * `id`
  * `jobTitle`
  * `mail`
  * `mobilePhone`
  * `preferredLanguage`
  * `surname`
  * `givenName`

  
`Order By Field` | _Optional_ The field to order the results by. The default value is `displayName`. The possible values are as follows:

  * `displayName`
  * `userPrincipalName`

  
`Order By` | _Optional_ The order of the results (ascending or descending). The default value is `ASC`. The possible values are as follows:

  * `DESC`
  * `ASC`

  
`Results Limit` | _Optional_ The maximum number of users to return.  
`Advanced Filter Logic` | _Optional_ The logic to use for advanced filtering that applies to the `Username` (`userPrincipalName`) field. The default value is `Equal`. Possible values are as follows:

  * `Equal`
  * `Contains`

  
`Advanced Filter Value` | _Optional_ The value to use in the advanced filter for the `Username` (`userPrincipalName`) field. If you select `Equal`, the action attempts to find the exact match among results. If you select `Contain`, the action attempts to find results that contain the provided substring. If you don't set a value, the filter doesn't apply.  
  
#### Action outputs

The **List Users** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Case wall table

The **List Users** action can return the following table in Google SecOps:

Table name: **Users**

Columns:

  * **Name**
  * **Username**
  * **ID**
  * **Given name**
  * **Preferred language**
  * **Mail**
  * **Mobile Phone**
  * **Surname**
  * **Job Title**



##### Entity enrichment table

The **List Users** action supports the following entity enrichment:

Enrichment field | Logic  
---|---  
`Username` | Returns if it exists in the JSON result.  
`Surname` | Returns if it exists in the JSON result.  
`Name` | Returns if it exists in the JSON result.  
`Job Title` | Returns if it exists in the JSON result.  
`Mail` | Returns if it exists in the JSON result.  
  
##### JSON result

The following example shows the JSON result output received when using the **List Users** action:
    
    
    [
        {
            "Group Type": "managed",
            "Id": "ID",
            "Name": "Example",
            "Description": "Example",
            "Created Time":"2019-10-24T19:10:18Z"
        }
    ]
    

##### Output messages

The **List Users** action can return the following output messages:

Output message | Message description  
---|---  
`List of users was fetched successfully.` `Some errors occurred. Please check the logs.` | The action succeeded.  
`User list fetch was not successful.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **List Users** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test the connectivity to Microsoft Entra ID.

This action runs on all Google SecOps entities.

#### Action inputs

None.

#### Action outputs

The **Ping** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`Connection established successfully.` | The action succeeded.  
`Connection could not be established successfully.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Remove User from the Group

Use the **Remove User from the Group** action to remove a user from the specified group in Microsoft Entra ID.

You can provide the username as an entity or an action input parameter. If you configure the username as both the entity and the input parameter, the action uses the input parameter.

To configure the username, follow the `username@domain` format.

This action runs on the Google SecOps `Username` entity.

#### Action inputs

The **Remove User from the Group** action requires the following parameters:

Parameter | Description  
---|---  
`User Name` | _Optional_ A comma-separated string of usernames to remove from the specified group. To configure this parameter value, use the `username@domain` format.If you don't set a value, the action runs on the usernames of the user entities from an action incident.  
`Group Name` | _Optional_ The name of the group to remove the user from.  
`Group ID` | _Optional_ The ID of the group to remove the user from.If you set both the `Group Name` and `Group ID` parameters, the action prioritizes the `Group ID` value.  
  
#### Action outputs

The **Remove User from the Group** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Remove User from the Group** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully removed the following entities from the Azure AD group: ENTITY_ID` `The following entities were not found in the Azure AD: ENTITY_ID` `No usernames were removed from the Azure AD group.` | The action succeeded.  
`Error executing action "Remove User from the Group". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Remove User from the Group** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Reset User Password

Use the **Reset User Password** action to reset the user password to the one that you specify in the action. This action requires the user to change their password on the next sign-in attempt.

The **Reset User Password** action expects you to configure the `User` entity in the `username@domain` format.

This action runs on the Google SecOps `User` entity.

#### Assign a role to your application

The **Reset User Password** action requires you to assign the `Password Administrator` role to your application.

To assign the `Password Administrator` role to your application, complete the following steps:

  1. Sign in to the Azure portal using your Microsoft account.
  2. In **Microsoft Entra ID** , search for **Roles and administrators**.
  3. Select or search for the `Password Administrator` role from the list.
  4. Click **Add Assignment**.
  5. Select an account (member) that you use in the integration and click **Next**.
  6. Enter justification for assigning a role.
  7. Click **Assign**.



#### Action inputs

The **Reset User Password** action requires the following parameters:

Parameter | Description  
---|---  
`Password` | _Required_ The new password to set for the user.  
  
#### Action outputs

The **Reset User Password** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Output messages | Available  
Script result | Available  
  
##### Output messages

The **Reset User Password** action can return the following output messages:

Output message | Message description  
---|---  
`User password was reset successfully.` `Some errors occurred. Please check the logs.` `` | The action succeeded.  
`User password reset was not successful.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Reset User Password** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Revoke User Session

Use the **Revoke User Session** action to revoke a user session.

This action runs on the following Google SecOps entities:

  * `Username`
  * `Email Address`



#### Action inputs

None.

#### Action outputs

The **Revoke User Session** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### JSON result

The following examples show the JSON result outputs received when using the **Revoke User Session** action:

  * If the user exists:
        
        {
            "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#Edm.Boolean",
            "value": true
        }
        

  * If the user is not found:
        
        {
            "error": "User not found."
        }
        




##### Output messages

The **Revoke User Session** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully revoked sessions for the following users in Azure AD: ENTITY_ID` `Action wasn't able to find the following users in Azure AD: ENTITY_ID` `None of the provided users were found in Azure AD.` | The action succeeded.  
`Error executing action "Revoke User Session". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Revoke User Session** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
