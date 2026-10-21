---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-intune/
title: Microsoft Intune \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T07:27:59.976750+00:00
---

# Microsoft Intune  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/microsoft-intune/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Microsoft Intune

This document explains how to integrate Microsoft Intune with Google Security Operations (Google SecOps).

## Configure Microsoft Intune integration to work with Google Security Operations

Complete the following steps to configure your Microsoft Intune instance.

### Prerequisite steps

To work with this integration, the Azure Active Directory (Azure AD) application is required.

#### Set up Azure Active Directory

  1. Log in to Azure tenant portal as a user with admin permissions.
  2. Go to **Azure Active Directory > App registrations > New registration**.
  3. In the registration form, choose a name for your application and supported account types depending on your environment.
  4. Click **Register**.



#### Specify permissions for the Azure AD application

  1. Go to the API permissions tab.
  2. Click **Add a permission**.
  3. In a new window, select **Microsoft Graph > Application permissions.**
  4. To ease the search, in a search field under **Select permissions** type in `managed`**.**
  5. In the **DeviceManagementManagedDevices** tab, select the following permissions:\ 
     1. **DeviceManagementManagedDevices.PrivilegedOperations.All** \
     2. **DeviceManagementManagedDevices.ReadWrite.All**
  6. Grant admin consent for new changes.



#### Create a client secret for the Azure AD application

  1. Go to **Certificates and Secrets**.
  2. In the **Client secrets** tab, click **New client secret**.
  3. Add required descriptions for the new secret.   
Once the secret is added, you will see its data.
  4. To use the secret in the integration, write down the client secret value.\



#### Complete the configuration

  1. At the Azure AD application configuration page, go to the **Essentials** tab.
  2. Provide the **Application (client) ID** and the **Directory (tenant) ID** from the previous steps.



Once the data is collected, the configuration of the Azure AD application for Microsoft Intune integration is completed.

## Configure Microsoft Intune integration in Google SecOps

**Important:** If you make any changes to the **Application Permissions** or **API Permissions** in your Microsoft Entra ID (Azure AD) App Registration after configuring this integration (for example, adding a new permission for a job to run), you must regenerate and update your credentials in Google SecOps. 

This typically means:

  * Generating a new client secret in your App Registration.
  * Updating the client secret (and regenerating the refresh token, if applicable) in the Google SecOps integration configuration.



Failure to update will prevent new permissions from being applied, causing actions to fail.

### Integration parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Azure AD endpoint | String | https://login.microsoftonline.com | True | Azure AD endpoint to connect to.  
Can be different for different tenant types.  
Microsoft Graph Endpoint | String | https://graph.microsoft.com | True | Microsoft Graph endpoint to connect to.  
Can be different for different tenant types.  
Client ID | String | N/A | True | Specify the client (application) ID of the Azure AD application  
to use for the integration.  
Client Secret Value | Password | N/A | True | Specify the client secret value (not the secret ID!) of the Azure AD app  
to use for the integration.  
Azure Active Directory ID | String | N/A | True | Specify the Azure Active Directory ID (tenant ID).  
To find it, go to the Azure AD page > App Registration >  
`Application you configured for your integration` >   
Directory (tenant) ID.  
Verify SSL | bool | Checked | N/A | If enabled, verify that the SSL certificate for connecting  
to the Microsoft Intune server is valid.  
  
## Actions

### Ping

#### Description

Test connectivity.

#### Parameters

N/A

#### Run on

The action is not running on entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
If action runs successfully, `is_success` should be set to `True`. Otherwise, `False`.

##### Case wall

Result type | Value/Description | Type (Entity/General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
_if successful:_  
print "Successfully connected to the Microsoft Intune service with the provided connection parameters!"  
  
**The action should fail and stop a playbook execution:**  
_if critical error, like wrong credentials or lost connectivity:_   
print "Failed to connect to the Microsoft Intune service! Error is {0}".format(exception.stacktrace)  | General  
  
### List managed devices

#### Description

List managed devices available in the Microsoft Intune instance based on provided criteria.

**Note:** This action doesn't run on Google SecOps entities.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Filter Key | DDL | Select One  
  
DDL possible values: 

  * deviceName
  * userId
  * operatingSystem
  * osVersion
  * userDisplayName

| False | Specify the key that needs to be used to filter managed devices.  
Filter Logic | DDL | Not Specified  
  
DDL possible values: 

  * Not Specified
  * Equal
  * Contains

| False | Specify what filter logic should be applied.  
Filtering logic works based on the value provided in the `Filter Key` parameter.  
Filter Value | String | N/A | False | Specify what value should be used in the filter.  
If `Equal` is selected, action will try to find the exact match among results, and if `Contains` is selected, action will try to find results that contain that substring.  
If nothing is provided in this parameter, the filter will not be applied.  
The filtering logic works based on the value provided in the `Filter Key` parameter.  
Max Records To Return | Int | 50 | False | Specify how many records to return.  
If nothing is provided, action will return 50 records by default.  
Max value is 100 records.  
  
#### Run on

The action is not running on entities.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
If action runs successfully (data is returned, server response is 200 OK), `is_success` should be set to `True`.

##### JSON result
    
    
    {
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#deviceManagement/managedDevices",
      "@odata.count": 8,
      "value": [
          {
              "id": "a80a77c5-c26f-4def-b350-2b80ae9b5e00",
              "userId": "",
              "deviceName": "CROWDSTRIKEV2",
              "managedDeviceOwnerType": "personal",
              "enrolledDateTime": "2022-03-01T20:42:04Z",
              "lastSyncDateTime": "2022-03-04T04:42:03Z",
              "operatingSystem": "Windows",
              "complianceState": "noncompliant",
              "jailBroken": "Unknown",
              "managementAgent": "mdm",
              "osVersion": "10.0.19043.1526",
              "easActivated": false,
              "easDeviceId": "",
              "easActivationDateTime": "0001-01-01T00:00:00Z",
              "azureADRegistered": null,
              "deviceEnrollmentType": "windowsAutoEnrollment",
              "activationLockBypassCode": null,
              "emailAddress": "",
              "azureADDeviceId": "a80a77c5-c26f-4def-b350-2b80ae9b5e00",
              "deviceRegistrationState": "registered",
              "deviceCategoryDisplayName": "Unknown",
              "isSupervised": false,
              "exchangeLastSuccessfulSyncDateTime": "0001-01-01T00:00:00Z",
              "exchangeAccessState": "none",
              "exchangeAccessStateReason": "none",
              "remoteAssistanceSessionUrl": null,
              "remoteAssistanceSessionErrorDetails": null,
              "isEncrypted": false,
              "userPrincipalName": "",
              "model": "VMware7,1",
              "manufacturer": "VMware, Inc.",
              "imei": "",
              "complianceGracePeriodExpirationDateTime": "2022-10-16T16:36:51Z",
              "serialNumber": "VMware-422238ba4acad659-63a1867ec4889b06",
              "phoneNumber": "",
              "androidSecurityPatchLevel": "",
              "userDisplayName": "",
              "configurationManagerClientEnabledFeatures": null,
              "wiFiMacAddress": "",
              "deviceHealthAttestationState": null,
              "subscriberCarrier": "",
              "meid": "",
              "totalStorageSpaceInBytes": 63766003712,
              "freeStorageSpaceInBytes": 38917898240,
              "managedDeviceName": "",
              "partnerReportedThreatState": "unknown",
              "requireUserEnrollmentApproval": null,
              "managementCertificateExpirationDate": "2023-02-27T08:10:12Z",
              "iccid": null,
              "udid": null,
              "notes": null,
              "ethernetMacAddress": null,
              "physicalMemoryInBytes": 0,
              "deviceActionResults": []
          },
          ...
    

##### Case wall

Result type | Value/Description | Type (Entity/General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
_If data is available(is_success = true):_  
print "Successfully found managed device(s) for the provided criteria in the Microsoft Intune instance".​  
  
 _If data is not available (is_success=false):_  
print "No managed devices were found for the provided criteria in the Microsoft Intune instance".  
  
_If "Filter Value" is empty (is_success=true):_  
The filter was not applied because the parameter "Filter Value" has an empty value.  
  
**The action should fail and stop a playbook execution:**  
  
_If Filter Key == "Select One" and Filter Logic "Equal" or "Contains":_  
Error executing the _List Managed Devices_ action. Reason: you need to select a field from the `Filter Key` parameter.  
  
_If invalid value is provided for Max Records to Return or the value is bigger than 100:_  
Error executing the _List Managed Devices_ action. Reason: "Invalid value was provided for "Max Records to Return": <provided value>. Positive number in range from 1 to 100 should be provided".  
​  
 _If fatal error, like wrong credentials, no connection to server, or other:_  
"Error executing the _List Managed Devices_ action. Reason: {0}''.format(error.Stacktrace) | General  
Case Wall Table  
  
| Name: Available Managed Devices  
Columns:  


  * Id
  * User Id
  * Device Name
  * Operating System
  * Compliance State
  * Enrolled Date Time
  * Last Sync Date Time

| General  
  
### Get managed device

#### Description

Get managed device information from the Microsoft Intune service, including information on specific actions, for example, locate device (`deviceActionResults` section of the json result).  
The hostname to run the action on can be provided either as a Google SecOps entity or as an action input parameter. If the hostname is passed to action both as an entity and an input parameter, the action will be executed on the input parameter. Hostname is case insensitive. Action also can be provided with the host ID to run on.  
If both host ID **and** hostname are provided, the action will run on the host ID as a priority.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Hostname | String | N/A | False | Specify the Hostname to run the action on. Hostname is case insensitive. If the action does not run on a Hostname entity, it can run either on Hostname or Host ID. Multiple values can be set as a comma-separated string.  
Host ID | String | N/A | False | Specify the host ID to run the action on. If the action does not run on a Hostname entity, it can run either on Hostname or Host ID. Multiple values can be set as a comma-separated string.  
  
#### Run on

Hostname, if provided.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
If action runs successfully (host found, server response is 200 OK), `is_success` should be set to `True`.

##### JSON result
    
    
    {
      "@odata.context": "https://graph.microsoft.com/v1.0/$metadata#deviceManagement/managedDevices/$entity",
      "id": "6caa05f6-563d-4a47-bcd8-e91c5dbab10a",
      "userId": "b786d3cf-e97d-4511-b61c-0559e9f4da75",
      "deviceName": "msintune2",
      "managedDeviceOwnerType": "company",
      "enrolledDateTime": "2023-05-11T09:45:08.6273921Z",
      "lastSyncDateTime": "2023-05-17T06:41:23.6481049Z",
      "operatingSystem": "Windows",
      "complianceState": "compliant",
      "jailBroken": "Unknown",
      "managementAgent": "mdm",
      "osVersion": "10.0.19045.2965",
      "easActivated": false,
      "easDeviceId": null,
      "easActivationDateTime": "0001-01-01T00:00:00Z",
      "azureADRegistered": true,
      "deviceEnrollmentType": "windowsAzureADJoin",
      "activationLockBypassCode": null,
      "emailAddress": "example@example.com",
      "azureADDeviceId": "a5fe5437-cc0e-4ecf-9216-5d60032d149d",
      "deviceRegistrationState": "registered",
      "deviceCategoryDisplayName": "",
      "isSupervised": false,
      "exchangeLastSuccessfulSyncDateTime": "0001-01-01T00:00:00Z",
      "exchangeAccessState": "none",
      "exchangeAccessStateReason": "none",
      "remoteAssistanceSessionUrl": "",
      "remoteAssistanceSessionErrorDetails": "",
      "isEncrypted": false,
      "userPrincipalName": "example@example.com",
      "model": "VMware7,1",
      "manufacturer": "VMware, Inc.",
      "imei": null,
      "complianceGracePeriodExpirationDateTime": "9999-12-31T23:59:59.9999999Z",
      "serialNumber": "VMware-42366cbe5a53838a-d95202d5e9a468c5",
      "phoneNumber": null,
      "androidSecurityPatchLevel": null,
      "userDisplayName": "example_user",
      "configurationManagerClientEnabledFeatures": null,
      "wiFiMacAddress": null,
      "deviceHealthAttestationState": null,
      "subscriberCarrier": "",
      "meid": null,
      "totalStorageSpaceInBytes": 52998176768,
      "freeStorageSpaceInBytes": 27044872192,
      "managedDeviceName": "example_Windows_5/11/2023_11:43 AM",
      "partnerReportedThreatState": "unknown",
      "requireUserEnrollmentApproval": null,
      "managementCertificateExpirationDate": "2024-05-10T00:50:50Z",
      "iccid": "",
      "udid": "",
      "notes": null,
      "ethernetMacAddress": "005056B6FD6F",
      "physicalMemoryInBytes": 0,
      "deviceActionResults": [
          {
              "@odata.type": "#microsoft.graph.locateDeviceActionResult",
              "actionName": "locateDevice",
              "actionState": "pending",
              "startDateTime": "2023-05-17T12:36:50.1982608Z",
              "lastUpdatedDateTime": "2023-05-17T12:36:50Z",
              "deviceLocation": null
          }
      ]
    }
    

##### Case wall

Result type | Value/Description | Type (Entity/General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
  
_if host is found(is_success = true):_  
_Hostname provided:_  
print "Successfully fetched managed device information for hostname: <hosntame>"  
_Host ID provided:_  
print "Successfully fetched managed device information for host id: <host id>"  
​  
 _If data is not available (is_success=false)_  
_Hostname provided:_  
print "The following hostname was not found in the Microsoft Intune: <hostname>"  
_Host ID provided:_  
print "The following host id was not found in the Microsoft Intune: <host id>"  
​  
 _If multiple intune agents are returned for the hostname:_  
print "Multiple managed devices were found for the provided hostname: <hostname>. Taking the managed device with the most recent `lastSyncDateTime`"  
  
**The action should fail and stop a playbook execution:**  
  
_If fatal error, like wrong credentials, no connection to server, other:_  
"Error executing action "Get Managed Device". Reason: {0}''.format(error.Stacktrace) | General  
  
### Sync managed device

#### Description

Synchronize a managed device with the Microsoft Intune service. The hostname to run the action on can be provided either as a Google SecOps entity or as an action input parameter. If the hostname is passed to action both as an entity and input parameter, the action will be executed on the input parameter. Hostname is case insensitive. Action also can be provided with the host ID to run on.  
If both host ID **and** hostname are provided, action will run on the host ID as a priority.

**Note:** Check the [Supported platforms](https://learn.microsoft.com/en-us/mem/intune/remote-actions/device-sync#supported-platforms) for this action.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Hostname | CSV | N/A | False | Specify a comma-separated list of hostnames to run the action on. Hostname is case insensitive. If the action does not run on a hostname entity, it can run either on hostname or host ID. Note: if both Hostname and Host ID are provided, the Host ID value has a priority. Multiple values can be set as a comma-separated string.   
Host ID | CSV | N/A | False | Specify a comma-separated list of host ids to run the action on. If the action does not run on a hostname entity, it can run either on Hostname or Host ID. Note: if both Hostname and Host ID are provided, the Host ID value has priority. Multiple values can be set as a comma-separated string.  
  
#### Run on

Hostname, if provided.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
If action runs successfully (host found, server response is 204), `is_success` should be set to `True`.

##### Case wall

Result type | Value/Description | Type (Entity/General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
  
_If at least one host is found (`is_success = true`, if ALL hosts in the scope of alert were found, in other case `is_success=false`):_  
_Hostname provided:_  
print "Successfully started sync for managed devices with hostnames in the Microsoft Intune: CSV of <hosntame>"  
_Host ID provided:_  
print "Successfully started sync for managed devices with host ids in the Microsoft Intune: CSV of <host id>"  
  
_If at least one host is not available (`is_success=false`)_  
_Hostname provided:_  
print "The following hostnames were not found in the Microsoft Intune: CSV of <hostname>"  
_Host ID provided:_  
print "The following host ids were not found in the Microsoft Intune: CSV of <host ids>"  
​  
 _If multiple Intune agents are returned for the hostname (`is_success = true`):_  
print "Multiple managed devices were found for the provided hostnames in the Microsoft Intune: <hostnames>. Taking the managed device with the most recent `lastSyncDateTime`"  
​  
 _If none of the hostnames or hosts were found or 400 status code for all (`is_success=false`):_  
No tasks were created on the provided hosts in Microsoft Intune.  
​  
**The action should fail and stop a playbook execution:**  
  
_if fatal error, like wrong credentials, no connection to server, other:_  
"Error executing action "Sync Managed Device". Reason: {0}''.format(error.Stacktrace)  
​  
 _If entity is not provided and input is also not provided (`is_success=false`):_  
Error executing action "Sync Managed Device". Reason: Action failed to start since Hostname or Host ID was not provided either as Google SecOps entity or action input parameter. | General  
  
### Locate managed device

#### Description

Locate the managed device with the Microsoft Intune service. The action starts the task to check the current task status, run the _Get Managed Device_ action, and see the `deviceActionResults` section for task status.  
The hostname to run the action on can be provided either as a Google SecOps entity or as an action input parameter.  
If the hostname is passed to action both as an entity and an input parameter, the action will be executed on the input parameter. The hostname is case insensitive. The action also can be provided with the host ID to run on.  
If both host ID and hostname are provided, action will run on the host ID as a priority.

**Note:** Check the [Supported platforms](https://learn.microsoft.com/en-us/mem/intune/remote-actions/device-locate#supported-platforms) for this action.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Hostname | String | N/A | False | Specify a comma-separated list of hostnames to run the action on. Hostname is case insensitive. If the action does not run on a hostname entity, it can run either on Hostname or Host ID. Note: if both Hostname and Host ID are provided, the Host ID value has a priority. Multiple values can be set as a comma-separated string.  
Host Id | String | N/A | False | Specify a comma-separated list of host ids to run the action on. If the action does not run on a hostname entity, it can run either on Hostname or Host ID. Note: if both Hostname and Host ID are provided, the Host ID value has a priority. Multiple values can be set as a comma-separated string.  
  
#### Run on

Hostname, if provided.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
If action runs successfully (host found, server response is 204), `is_success` should be set to `True`.

##### Case wall

Result type | Value/Description | Type (Entity/General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
  
_If at least one host is found(`is_success = true`, if ALL hosts in the scope of alert were found, in other case `is_success=false`):_  
_Hostname provided:_  
print "Successfully started locate task for managed devices with hostnames in the Microsoft Intune: CSV of <hosntame>"  
_Host iID provided:_  
print "Successfully started locate task for managed devices with host ids in the Microsoft Intune: CSV of <host id>"  
  
_If at least one host is not available (`is_success=false`)_  
_Hostname provided:_  
print "The following hostnames were not found in the Microsoft Intune: CSV of <hostname>"  
_Host ID provided:_  
print "The following host ids were not found in the Microsoft Intune: CSV of <host ids>"  
  
_If multiple intune agents are returned for the hostname (`is_success = true`):_  
print "Multiple managed devices were found for the provided hostnames in the Microsoft Intune: <hostnames>. Taking the managed device with the most recent lastSyncDateTime"  
  
_If 400 status code:_  
Action wasn't able to create a task for the following hosts in the Microsoft Intune: {hostname/hostids}  
​  
 _If none of the hostnames or hosts were found or 400 status code for all (`is_success=false`:_  
No tasks were created on the provided hosts in Microsoft Intune.  
​  
**The action should fail and stop a playbook execution:**  
  
_if fatal error, like wrong credentials, no connection to server, other:_  
"Error executing action "Locate Managed Device". Reason: {0}''.format(error.Stacktrace)  
​  
 _If entity is not provided and input is also not provided (`is_success=false`):_  
Error executing action "Locate Managed Device". Reason: Action failed to start since Hostname or Host ID was not provided either as Google SecOps entity or action input parameter.  
| General  
  
### Wipe managed device

#### Description

Wipe a managed device with the Microsoft Intune service.  
The hostname to run the action on can be provided either as a Google SecOps entity or as an action input parameter. If the hostname is passed to action both as an entity and input parameter, the action will be executed on the input parameter.  
Hostname is case insensitive. Action also can be provided with the host ID to run on.  
If both host ID and hostname are provided, action will run on the host ID as a priority.

**Note:**

  * The Wipe action is not available for iOS/iPadOS devices enrolled with User Enrollment.
  * The Retain enrollment state and user account option is only available for Windows 10 version 1709 or later.



#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Hostname | String | N/A | False | Specify a comma-separated list of hostnames to run the action on. Hostname is case insensitive. If the action does not run on a hostname entity, it can run either on Hostname or Host ID. Note: if both the Hostname and Host ID are provided, the Host ID value has a priority. Multiple values can be as a comma-separated string.  
Host ID | String | N/A | False | Specify a comma-separated list of hostnames to run the action on. Hostname is case insensitive. If the action does not run on a hostname entity, it can run either on Hostname or Host ID. Note: if both the Hostname and Host ID are provided, the Host ID value has a priority. Multiple values can be as a comma-separated string.  
Keep Enrollment Data | Checkbox | Checkbox Unchecked | False | If enabled, keep the enrollment data on the device.  
Keep User Data | Checkbox | Checkbox Unchecked | False | If enabled, keep the user data on the device.  
Persist eSIM Data Plan | Checkbox | Checkbox Unchecked | False | If enabled, persist eSIM data plan for the device.  
Mac OS Unlock Code | String | N/A | False | Specify Mac OS unlock code, if applicable.  
  
#### Run on

Hostname, if provided.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
If action runs successfully (host found, server response is 204), `is_success` should be set to `True`.

##### Case wall

Result type | Value/Description | Type (Entity/General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
  
_If at least one host is found (`is_success = true`, if ALL hosts in the scope of alert were found, in other case `is_success=false`):_  
_Hostname provided:_  
print "Successfully started wipe task for managed devices with hostnames in the Microsoft Intune: CSV of <hosntame>"  
_Host ID provided:_  
print "Successfully started wipe task for managed devices with host ids in the Microsoft Intune: CSV of <host id>"  
​  
 _If at least one host is not available (`is_success=false`)_  
_Hostname provided:_  
print "The following hostnames were not found in the Microsoft Intune: CSV of <hostname>"  
_Host ID provided:_  
print "The following host ids were not found in the Microsoft Intune: CSV of <host ids>"  
​  
 _If multiple intune agents are returned for the hostname (is_success = true):_  
print "Multiple managed devices were found for the provided hostnames in the Microsoft Intune: <hostnames>. Taking the managed device with the most recent `lastSyncDateTime`"  
  
_If none of the hostnames or hosts were found or 400 status code for all (`is_success=false`):_  
No tasks were created on the provided hosts in Microsoft Intune.  
  
**The action should fail and stop a playbook execution:**  
  
_If fatal error, like wrong credentials, no connection to server, or other:_  
"Error executing action "Wipe Managed Device". Reason: {0}''.format(error.Stacktrace)  
  
_If entity is not provided and input is also not provided (`is_success=false`):_  
Error executing action "Wipe Managed Device". Reason: Action failed to start since Hostname or Host ID was not provided either as Google SecOps entity or action input parameter. | General  
  
### Reset managed device passcode

#### Description

Reset the passcode of a managed device. The action starts the task to check the current task status, run the _Get Managed Device_ action, and see the `deviceActionResults` section for a task status.  
The hostname to run the action on can be provided either as a Google SecOps entity or as an action input parameter. If the hostname is passed to action both as an entity and input parameter, the action will be executed on the input parameter.  
Hostname is case insensitive. Action also can be provided with the host ID to run on.  
If both host ID and hostname are provided, action will run on the host ID as a priority.

**Note:** Check the [Supported platforms](https://learn.microsoft.com/en-us/mem/intune/remote-actions/device-passcode-reset#supported-platforms-for-device-level-passcode-reset) for this action.

#### Parameters

Parameter Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Hostname | String | N/A | False | Specify a comma-separated list of hostnames to run the action on. Hostname is case insensitive. If the action does not run on a hostname entity, it can run either on Hostname or Host ID. Note: if both Hostname and Host ID are provided, the Host ID value has a priority. Multiple values can be as a comma-separated string.  
Host ID | String | N/A | False | Specify a comma-separated list of hostnames to run the action on. If the action does not run on a hostname entity, it can run either on Hostname or Host ID. Note: if both Hostname and Host ID are provided, the Host ID value has a priority. Multiple values can be as a comma-separated string.  
  
#### Run on

Hostname, if provided.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
If action runs successfully (host found, server response is 204), `is_success` should be set to `True`.

##### Case wall

Result type | Value/Description | Type (Entity/General)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
  
_If at least one host is found(`is_success = true`, if ALL hosts in the scope of alert were found, in other case `is_success=false`):_  
_Hostname provided:_  
print "Successfully started reset task for managed devices with hostnames in the Microsoft Intune: CSV of <hosntame>"  
_Host ID provided:_  
print "Successfully started reset task for managed devices with host ids in the Microsoft Intune: CSV of <host id>"  
  
_If at least one host is not available (`is_success=false`)_  
_Hostname provided:_  
print "The following hostnames were not found in the Microsoft Intune: CSV of <hostname>"  
_Host ID provided:_  
print "The following host ids were not found in the Microsoft Intune: CSV of <host ids>"  
  
_If multiple intune agents are returned for the hostname (`is_success = true`):_  
print "Multiple managed devices were found for the provided hostnames in the Microsoft Intune: <hostnames>. Taking the managed device with the most recent `lastSyncDateTime`"  
  
  
_If none of the hostnames or hosts were found or 400 status code for all (`is_success=false)`:_  
No tasks were created on the provided hosts in Microsoft Intune.  
​  
**The action should fail and stop a playbook execution:**  
  
_If fatal error, like wrong credentials, no connection to server, other:_  
"Error executing action "Reset Managed Device Passcode". Reason: {0}''.format(error.Stacktrace)  
​  
Error executing action "Reset Managed Device". Reason: Action failed to start since Hostname or Host ID was not provided either as Google SecOps entity or action input parameter.  
| General  
  
### Remote lock managed device

#### Description

Remote lock the managed device.  
The action starts the task to check the current task status, run "Get Managed Device" action and see `deviceActionResults` section for task status. The hostname to run the action on can be provided either as a Google SecOps entity or as an action input parameter. If the hostname is passed to action both as an entity and input parameter, the action will be executed on the input parameter.  
Hostname is case insensitive. Action also can be provided with the host ID to run on. If both host ID and hostname are provided, action will run on the host ID as a priority.  
Action can run on either entity or action input parameter.

**Note:** Check the [Supported platforms](https://learn.microsoft.com/en-us/mem/intune/remote-actions/device-remote-lock#supported-platforms) for this action.

#### Parameters

Parameter Display Name | Type | Default Value | Is mandatory | Description  
---|---|---|---|---  
Hostname | String | N/A | False | Specify a comma-separated list of hostnames to run the action on. Hostname is case insensitive. If the action does not run on a hostname entity, it can run either on Hostname or Host ID. Note: if both Hostname and Host ID are provided, the Host ID value has a priority. Multiple values can be as a comma-separated string.  
Host Id | String | N/A | False | Specify a comma-separated list of host ids to run the action on. If the action does not run on a hostname entity, it can run either on Hostname or Host ID. Note: if both Hostname and Host ID are provided, the Host ID value has a priority. Multiple values can be as a comma-separated string.  
  
#### Run on

Hostname, if provided.

#### Action results

##### Script result

Script Result Name | Value Options | Example  
---|---|---  
is_success | True/False | is_success:False  
  
If action runs successfully (host found, server response is 204), `is_success` should be set to `True`.

##### Case wall

Result type | Value/Description | Type (Entity/GGeneral)  
---|---|---  
Output message* | **The action should not fail nor stop a playbook execution:**  
​ _If at least one host is found(`is_success = true`, if ALL hosts in the scope of alert were found, in other case `is_success=false`):_  
_Hostname provided:_  
print "Successfully started remote lock task for managed devices with hostnames in the Microsoft Intune: CSV of <hostname>"  
_Host ID provided:_  
print "Successfully started remote lock task for managed devices with host ids in the Microsoft Intune: CSV of <host id>"  
  
​ _If at least one host is not available (`is_success=false`):_  
_Hostname provided:_  
print "The following hostnames were not found in the Microsoft Intune: CSV of <hostname>"  
_Host ID provided:_  
print "The following host ids were not found in the Microsoft Intune: CSV of <host ids>"​  
 _If multiple intune agents are returned for the hostname (`is_success = true`):  
_print "Multiple managed devices were found for the provided hostnames in the Microsoft Intune: <hostnames>. Taking the managed device with the most recent `lastSyncDateTime`"  
  
_If none of the hostnames or hosts were found or 400 status code for all (`is_success=false`):_  
No tasks were created on the provided hosts in Microsoft Intune.  
  
​**The action should fail and stop a playbook execution:**  
_If fatal error, like wrong credentials, no connection to server, other:_  
"Error executing action "Reset Lock Managed Device". Reason: {0}''.format(error.Stacktrace)  
  
​Error executing action "Reset Lock Managed Device". Reason: Action failed to start since Hostname or Host ID was not provided either as Google SecOps entity or action input parameter. | General  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
