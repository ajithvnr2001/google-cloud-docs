---
url: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/active-directory/
title: Integrate Active Directory with Google SecOps \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:01:36.144125+00:00
---

# Integrate Active Directory with Google SecOps  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/marketplace-integrations/active-directory/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Integrate Active Directory with Google SecOps

This document explains how to integrate Active Directory with Google Security Operations.

**Note:** This integration uses one or more open source components. You can download a zipped copy of the full source code of this integration from the [Cloud Storage bucket](https://storage.googleapis.com/csoar_public_integrations/ActiveDirectory.zip).

## Use cases

The **Active Directory** integration uses Google SecOps capabilities to support the following use cases:

  * **Activate and deactivate users:** Deactivate a potentially compromised user account and prevent further unauthorized access.

  * **Reset passwords:** Automatically reset the user password in Active Directory and notify the user of the change.

  * **Manage groups:** Add new users to the appropriate security groups based on their role and make sure that the users have the correct access permissions.

  * **Retrieve user information:** Retrieve user details such as group memberships, last sign in time, and contact information about a specific user account.

  * **Automate offboarding:** Disable accounts, remove them from groups, and transfer file ownership in a case when an employee offboards.




## Before you begin

Before you configure the **Active Directory** integration in Google SecOps, verify that your network environment, Active Directory Domain Services (AD DS), and service account credentials satisfy all operational prerequisites.

To prepare your environment for integration, complete the following prerequisites:

  1. Verify network connectivity and DNS resolution between your Google SecOps instance (or Remote Agent) and your Active Directory Domain Controllers.

  2. If connecting over LDAPS (port 636) (required for password resets), make sure directory certificates are configured. If using an internal Certificate Authority (CA), have your root or intermediate CA certificate ready for base64 encoding.

  3. Create a dedicated Active Directory service account adhering to the Principle of Least Privilege (PoLP).

  4. Review the required action permissions to determine the attributes and access rights needed for the specific playbooks you plan to run.

  5. Delegate permissions on target Organizational Units (OUs) using Active Directory Users and Computers (ADUC) or PowerShell (`dsacls`), making sure the service account has explicit Read and Write access to the `userAccountControl` attribute.




### Network and DNS requirements

Google SecOps communicates directly with Active Directory Domain Controllers using the Lightweight Directory Access Protocol (LDAP or LDAPS) over TCP.

Make sure your network environment meets the following connectivity rules:

  * **Port connectivity** : Ensure your network firewalls and routing allow outbound communication from Google SecOps (or your Remote Agent) to your Active Directory Domain Controllers on the following ports:

    * **LDAP (standard)** : Open port `389/TCP` for unencrypted LDAP communication.
    * **LDAPS (recommended - mandatory for passwords)** : Open port `636/TCP` (or your custom SSL/TLS port). LDAPS is required for encrypted directory traffic and is mandatory for password modification actions such as Set User Password.
  * **DNS and hostname resolution** : Active Directory requires accurate hostname resolution to match SSL/TLS certificates and directory service bindings. If your domain is resolved by a fully qualified DNS name through your internal DNS setup, no additional host configuration is needed. If DNS resolution isn't available on your remote agent container image, configure the `/etc/hosts` file.




#### Configure the `/etc/hosts` file

Active Directory requires accurate hostname resolution to match SSL/TLS certificates and directory service bindings. If your remote agent can't resolve the Active Directory domain controller using DNS, map the host manually.

To configure the `/etc/hosts` file, complete the following steps:

  1. Open `/etc/hosts` in a text editor with administrative privileges:
         
         sudo vi /etc/hosts
         

  2. Add an entry mapping the domain controller's IP address to its fully qualified domain name (FQDN):
         
         192.0.2.195 dc01.example.local
         

  3. Save and close the file.




If you don't need a CA certificate for the integration, proceed to configuring the authentication and service account requirements. Otherwise, configure your CA certificate.

### (_Optional_) Configure the CA certificate

When connecting over LDAPS (port 636) using certificates issued by a private or internal CA, provide the base64-encoded certificate string during setup to establish a trusted TLS connection.

To configure and upload the CA certificate, complete the following steps:

  1. Encode your PEM-formatted certificate file:

     * **Linux** : `bash base64 -w 0 mycert.crt`

     * **macOS** : `bash base64 -i mycert.crt`

  2. Copy the full output string (including encoded headers) and paste it into the **CA Certificate File - parsed into Base64 String** field in the Google SecOps integration configuration.

  3. Set the **Server** parameter to the FQDN of the domain controller (not its IP address) so the hostname matches the Common Name (CN) or Subject Alternative Name (SAN) on the certificate.

  4. Click **Test** to validate the TLS handshake.




### Authentication and service account requirements

The **Active Directory** integration authenticates using standard AD DS credentials.

Make sure your authentication setup complies with the following security practices:

  * **Dedicated service account** : Create a dedicated service account (such as `svc_secops_ad`) specifically for Google SecOps automated playbooks. Avoid using interactive user accounts or built-in domain administrator accounts.

  * **Username format** : The username can be provided as a User Principal Name (UPN) (such as `svc_secops@example.local`) or as a Down-Level Logon Name (`EXAMPLE\svc_secops`).

  * **PoLP** : Don't add the service account to privileged built-in groups such as **Domain Admins** , **Enterprise Admins** , or **Account Operators**. Instead, grant granular permissions on specific OUs where user, computer, or group objects reside.




### Configure action permissions (least privilege)

Grant the authenticating service account the specific Active Directory permissions and LDAP attribute access required for the actions your playbooks execute.

**Important:** Status-checking and lifecycle actions (including **Enable account** , **Disable account** , **Enable computer** , **Disable computer** , and **Enrich entities**) require explicit Read Property and Write Property rights on the `userAccountControl` attribute. 

If the service account can't read `userAccountControl`, Active Directory omits the attribute entirely from LDAP responses. In Google SecOps, this produces unhandled null exceptions (such as `TypeError: 'NoneType' object is not subscriptable`). Make sure this attribute is delegated explicitly on all target OUs.

Refer to the minimal permissions for Active Directory actions in the following table:

Action Name | Required AD DS Permission / Extended Right | Target Object Class | Description / Attribute Scope  
---|---|---|---  
**Ping** | `Read Property` | User, Domain Root | Queries the configured service account object (`sAMAccountName`, `userPrincipalName`, `mail`) to validate directory connectivity and credentials.  
**Enrich entities** | 

  * `List Contents`
  * `Read Property` (target attributes: `userAccountControl`, `sAMAccountName`, `mail`, `memberOf`, `lockoutTime`, `pwdLastSet`)

| User, Computer, Group | Queries user and computer attributes and resolves nested group memberships. Requires `Read Property` on `userAccountControl` to prevent null subscript errors.  
**Disable account** | 

  * `Read Property`: `userAccountControl`
  * `Write Property`: `userAccountControl`

| User | Reads and sets the `ACCOUNTDISABLE` flag (`0x0002`) on the target user object.  
**Enable account** | 

  * `Read Property`: `userAccountControl`
  * `Write Property`: `userAccountControl`

| User | Reads and clears the `ACCOUNTDISABLE` flag (`0x0002`) on the target user object.  
**Disable computer** | 

  * `Read Property`: `userAccountControl`
  * `Write Property`: `userAccountControl`

| Computer | Reads and sets the `ACCOUNTDISABLE` flag on the target computer object.  
**Enable computer** | 

  * `Read Property`: `userAccountControl`
  * `Write Property`: `userAccountControl`

| Computer | Reads and clears the `ACCOUNTDISABLE` flag on the target computer object.  
**Release Locked Account** | `Write Property`: `lockoutTime` | User | Sets the `lockoutTime` attribute to `0` to unlock a locked user account.  
**Force password update** | `Write Property`: `pwdLastSet` | User | Sets the `pwdLastSet` attribute to `0` to require the user to change their password at next logon.  
**Set User Password** | 

  * Extended Right: `Reset Password` (`User-Force-Change-Password`)
  * (Optional) `Write Property`: `unicodePwd`

| User | Resets the target user's password. Requires LDAPS (port 636) or StartTLS.  
**Add User To Group** | 

  * `Read Property`: `member`
  * `Write Property`: `member`

| Group | Adds the target user's Distinguished Name (`distinguishedName`) to the group's `member` attribute.  
**Remove User From Group** | 

  * `Read Property`: `member`
  * `Write Property`: `member`

| Group | Removes the target user's Distinguished Name (`distinguishedName`) from the group's `member` attribute.  
**Change User OU** | 

  * `Delete Child Object` (User) on source OU
  * `Create Child Object` (User) on destination OU
  * `Write Property`: `name`, `distinguishedName`

| Organizational Unit (OU), User | Moves user objects between OUs using LDAP `modify_dn`.  
**Change Host OU** | 

  * `Delete Child Object` (Computer) on source OU
  * `Create Child Object` (Computer) on destination OU
  * `Write Property`: `name`, `distinguishedName`

| Organizational Unit (OU), Computer | Moves computer objects between OUs using LDAP `modify_dn`.  
**Update attributes of an AD User** | `Write Property` on target attributes (such as `mail`, `title`, `department`, `telephoneNumber`, `description`, or `manager`) | User | Modifies specified attribute values on the target user object.  
**Update attributes of an AD Host** | `Write Property` on target attributes (such as `description`, or `location`) | Computer | Modifies specified attribute values on the target computer object.  
**Get Group Members** | 

  * `List Contents`
  * `Read Property`: `member`, `sAMAccountName`, `distinguishedName`

| Group, User, Computer | Queries group membership and member account attributes.  
**Get Manager Contact Details** | 

  * `Read Property`: `manager`
  * `Read Property`: `mail`, `displayName`, `telephoneNumber`, `title`

| User | Reads the `manager` attribute from the target user object and retrieves the manager's contact details.  
**Is User In Group** | 

  * `Read Property`: `memberOf`, `sAMAccountName`

| User, Group | Evaluates whether a user account belongs to the specified security or distribution group.  
**List User Groups** | 

  * `Read Property`: `memberOf`, `sAMAccountName`

| User, Group | Returns the list of all groups assigned to the specified user account.  
**Search Active Directory** | 

  * `List Contents`
  * `Read Property` on queried attributes

| User, Computer, Group, OU | Executes custom LDAP filter queries against the directory subtree.  
  
### Delegating permissions in Active Directory

To enforce the PoLP without granting broad administrative rights, use ADUC or PowerShell and dsacls to delegate permissions on target OUs using standard Active Directory management tools.

#### Delegate control using ADUC

If you prefer using a graphical interface, delegate object and property specific permissions by using the Delegation of Control Wizard in ADUC. 

Run the wizard on the target OU to grant the specific object and property permissions required for account management (such as reading and writing account control flags, resetting passwords, and unlocking accounts).

For step-by-step guidance on running the wizard, see the Microsoft documentation on [Delegation of Control in AD DS on Windows Server](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/delegation-control-wizard).

#### Delegate control using PowerShell and dsacls

If you prefer a command-line approach or need to automate and script permission assignments, use PowerShell alongside the built-in `dsacls.exe` command-line utility. 

Run the following command examples on an administrative workstation or Domain Controller, substituting your target OU and service account name:

  * **Grant Read and Write on`userAccountControl` (Disable/Enable user accounts and prevent enrichment errors)**: `powershell dsacls.exe "OU=Users,DC=example,DC=local" /I:S /G "EXAMPLE\svc_secops_ad:RPWP;userAccountControl;user"`
  * **Grant Read and Write on`userAccountControl` for computer objects (Disable/Enable computers)**: `powershell dsacls.exe "OU=Computers,DC=example,DC=local" /I:S /G "EXAMPLE\svc_secops_ad:RPWP;userAccountControl;computer"`
  * **Grant unlock account permissions (`lockoutTime`)**: `powershell dsacls.exe "OU=Users,DC=example,DC=local" /I:S /G "EXAMPLE\svc_secops_ad:WP;lockoutTime;user"`
  * **Grant force password change permissions (`pwdLastSet`)**: `powershell dsacls.exe "OU=Users,DC=example,DC=local" /I:S /G "EXAMPLE\svc_secops_ad:WP;pwdLastSet;user"`
  * **Grant password reset rights (`Reset Password` extended right)**: `powershell dsacls.exe "OU=Users,DC=example,DC=local" /I:S /G "EXAMPLE\svc_secops_ad:CA;Reset Password;user"`
  * **Grant membership modification rights on a security group** : `powershell dsacls.exe "CN=SecOps-Quarantine,OU=Groups,DC=example,DC=local" /G "EXAMPLE\svc_secops_ad:RPWP;member;group"`



For more details on syntax and parameter switches, see the Microsoft documentation on [dsacls](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-server-2012-r2-and-2012/cc771151\(v=ws.11\)).

**Note:** In Active Directory, members of protected administrative groups have inheritance disabled by the internal AdminSDHolder process. Delegated permissions assigned at an OU level won't apply to protected administrative accounts. 

For more information on managing protected objects, see the Microsoft documentation on [AdminSDHolder and Protected Accounts](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/appendix-c--protected-accounts-and-groups-in-active-directory).

## Integration parameters

The **Active Directory** integration requires the following parameters:

Parameter | Description  
---|---  
`Server` | Required. The hostname, DNS name, or IP address of the Active Directory server. The integration communicates using the LDAP protocol. To use a custom port, append it to the address (such as, `mydomain.com:636`). By default, the integration uses port 636 when SSL/TLS is enabled and port 389 when it's disabled.  
`Username` | Required.The email address of the user to connect to Active Directory, such as `user@example.com`.This parameter also accepts the `userPrincipalName` attribute.  
`Domain` | Required.The full DNS path to your domain within the network namespace.To configure this parameter, enter the fully qualified domain name (FQDN) of your domain if the following format: `SUBDOMAIN.ROOT_DOMAIN`. For example, if your internal Active Directory domain is `example.local`, the FQDN to enter is `example.local`. If your internal Active Directory domain is `corp.example.com`, the FQDN to enter is `corp.example.com`.  
`Password` | Required.The password for the user account.  
`Custom Query Fields` | Optional.Custom fields of the Active Directory integration, such as `customField1, customField2`.  
`CA Certificate File - parsed into Base64 String` | Optional.The CA certificate file string encoded into the base64 format that you obtained when configuring the CA certificate. To configure this parameter, enter the full BASE64_ENCODED_CERTIFICATE_STRING value.  
`Use SSL` | Optional.If selected, the integration validates the SSL certificate when connecting to the Active Directory server. The integration uses secure LDAPS (port 636) when selected. If not selected, it uses standard LDAP (port 389). Not selected by default.  
  
For instructions about how to configure an integration in Google SecOps, see [Configure integrations](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/configure-integrations).

You can make changes at a later stage, if needed. After you configure an integration instance, you can use it in playbooks. For more information about how to configure and support multiple instances, see [Supporting multiple instances](https://docs.cloud.google.com/chronicle/docs/soar/respond/integrations-setup/supporting-multiple-instances).

## Actions

For more information about actions, see [ Respond to pending actions from Your Workdesk](https://docs.cloud.google.com/chronicle/docs/soar/overview-and-introduction/your-workdesk/respond-to-pending-actions-from-workdesk) and [Perform a manual action](https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/perform-a-manual-action). 

### Add User to Group

Use the **Add User to Group** action to add user to groups.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **Add User to Group** action requires the following parameters:

Parameter | Description  
---|---  
`Group Name` | Required.A comma-separated list of groups to add users to.   
  
#### Action outputs

The **Add User to Group** action provides the following outputs:

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

The **Add User to Group** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully added the following users to the group "GROUP_NAME" in Active Directory: ENTITY_ID` `The following users were already a part of the group "GROUP_NAME" in Active Directory: ENTITY_ID` `Action wasn't able to add the following users to the group "GROUP_NAME" in Active Directory: ENTITY_ID` `No users were added to the group "GROUP_NAME" in Active Directory.` `No users were added to the provided groups in Active Directory.` | The action succeeded.  
`Error executing action "Add User to Group". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Add User to Group** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Change Host OU

Use the **Change Host OU** action to change the OU of a host.

This action runs on the Google SecOps `Hostname` entity.

#### Action inputs

The **Change Host OU** action requires the following parameters:

Parameter | Description  
---|---  
`OU Name` | Required.The name of the new user OU.  
  
#### Action outputs

The **Change Host OU** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Change Host OU** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Change User OU

Use the **Change User OU** action to change the OU of a user.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **Change User OU** action requires the following parameters:

Parameter | Description  
---|---  
`OU Name` | Required.The name of the new user OU.  
  
#### Action outputs

The **Change User OU** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Change User OU** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Disable Account

Use the **Disable Account** action to disable a user account.

This action runs on the Google SecOps `User` entity.

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
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Disable Account** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Disable Computer

Use the **Disable Computer** action to disable a computer account.

This action runs on the Google SecOps `Hostname` entity.

#### Action inputs

None.

#### Action outputs

The **Disable Computer** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Disable Computer** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Enable Account

Use the **Enable Account** action to enable a user account.

This action runs on the Google SecOps `User` entity.

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
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Enable Account** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Enable Computer

Use the **Enable Computer** action to enable a computer account.

This action runs on the Google SecOps `Hostname` entity.

#### Action inputs

None.

#### Action outputs

The **Enable Computer** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Enable Computer** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Enrich Entities

Use the **Enrich Entities** action to enrich the `Hostname` or `Username` entities with Active Directory properties.

This action is asynchronous. Adjust the script timeout value in the Google SecOps IDE for the action, if needed.

The **Enrich Entities** action runs on the following Google SecOps entities:

  * `User`
  * `Hostname`



#### Action inputs

The **Enrich Entities** action requires the following parameters:

Parameter | Description  
---|---  
`Mark entities as internal` | Required.If selected, the action automatically marks the successfully enriched entities as internal entities.  
`Specific Attribute Names To Enrich With` | Optional.A comma-separated list of attribute names to enrich the entities with.If you don't set any value, the action enriches entities with all available attributes. If an attribute contains multiple values, the action enriches the attribute with all available values. This parameter is case sensitive.  
`Should Case Wall table be filtered by the specified attributes?` | Optional.If selected, the action populates the case wall table only with attributes that you specified in the `Specific Attribute Names To Enrich With` parameter value. Not selected by default.  
`Should JSON result be filtered by the specified attributes?` | Optional.If selected, the JSON result returns only attributes that you specified in the `Specific Attribute Names To Enrich With` parameter value. Not selected by default.  
`Connection Timeout` | Optional.Network connection timeout limit in seconds. The default value is `10`.  
`Receive Timeout` | Optional.Network receive timeout limit in seconds. The default value is `60`.  
  
#### Action outputs

The **Enrich Entities** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Available  
JSON result | Available  
Script result | Available  
  
##### Entity enrichment

The **Enrich Entities** action supports the following entity enrichment:

Enrichment field name | Logic  
---|---  
`AD_primaryGroupID` | The action returns the value if it exists in the JSON result.  
`AD_logonCount` | The action returns the value if it exists in the JSON result.  
`AD_cn` | The action returns the value if it exists in the JSON result.  
`AD_countryCode` | The action returns the value if it exists in the JSON result.  
`AD_objectClass` | The action returns the value if it exists in the JSON result.  
`AD_userPrincipalName` | The action returns the value if it exists in the JSON result.  
`AD_adminCount` | The action returns the value if it exists in the JSON result.  
`AD_lastLogonTimestamp` | The action returns the value if it exists in the JSON result.  
`AD_manager` | The action returns the value if it exists in the JSON result.  
`AD_instanceType` | The action returns the value if it exists in the JSON result.  
`AD_distinguishedName` | The action returns the value if it exists in the JSON result.  
`AD_dSCorePropagationData` | The action returns the value if it exists in the JSON result.  
`AD_msDS-SupportedEncryptionTypes` | The action returns the value if it exists in the JSON result.  
`AD_objectSid` | The action returns the value if it exists in the JSON result.  
`AD_whenCreated` | The action returns the value if it exists in the JSON result.  
`AD_uSNCreated` | The action returns the value if it exists in the JSON result.  
`AD_lockoutTime` | The action returns the value if it exists in the JSON result.  
`AD_badPasswordTime` | The action returns the value if it exists in the JSON result.  
`AD_pwdLastSet` | The action returns the value if it exists in the JSON result.  
`AD_sAMAccountName` | The action returns the value if it exists in the JSON result.  
`AD_objectCategory` | The action returns the value if it exists in the JSON result.  
`AD_lastLogon` | The action returns the value if it exists in the JSON result.  
`AD_objectGUID` | The action returns the value if it exists in the JSON result.  
`AD_whenChanged` | The action returns the value if it exists in the JSON result.  
`AD_badPwdCount` | The action returns the value if it exists in the JSON result.  
`AD_accountExpires` | The action returns the value if it exists in the JSON result.  
`AD_displayName` | The action returns the value if it exists in the JSON result.  
`AD_name` | The action returns the value if it exists in the JSON result.  
`AD_memberOf` | The action returns the value if it exists in the JSON result.  
`AD_codePage` | The action returns the value if it exists in the JSON result.  
`AD_userAccountControl` | The action returns the value if it exists in the JSON result.  
`AD_sAMAccountType` | The action returns the value if it exists in the JSON result.  
`AD_uSNChanged` | The action returns the value if it exists in the JSON result.  
`AD_sn` | The action returns the value if it exists in the JSON result.  
`AD_givenName` | The action returns the value if it exists in the JSON result.  
`AD_lastLogoff` | The action returns the value if it exists in the JSON result.  
  
##### JSON result

The following example shows the JSON result output received when using the **Enrich Entities** action:
    
    
    [
        {
            "EntityResult": {
                "primaryGroupID": [513],
                "logonCount": [6505],
                "cn": ["user name"],
                "countryCode": [0],
                "objectClass": ["top", "person", "organizationalPerson"],
                "userPrincipalName": ["user@example.com"],
                "adminCount": [1],
                "lastLogonTimestamp": ["2019-01-09 08:42:03.540783+00:00"],
                "manager": ["CN=user name,OU=R&D,OU=TLV,OU=host name,DC=domain,DC=LOCAL"],
                "instanceType": [4],
                "distinguishedName": ["CN=user name,OU=R&D,OU=TLV,OU=host,DC=domain,DC=LOCAL"],
                "dSCorePropagationData": ["2019-01-14 14:39:16+00:00"],
                "msDS-SupportedEncryptionTypes": [0],
                "objectSid": ["ID"],
                "whenCreated": ["2011-11-07 08:00:44+00:00"],
                "uSNCreated": [7288202],
                "lockoutTime": ["1601-01-01 00:00:00+00:00"],
                "badPasswordTime": ["date"],
                "pwdLastSet": ["date"],
                "sAMAccountName": ["example"],
                "objectCategory": ["CN=Person,CN=Schema,CN=Configuration,DC=host,DC=LOCAL"],
                "lastLogon": ["2019-01-14 17:13:54.463070+00:00"],
                "objectGUID": ["GUID"],
                "whenChanged": ["2019-01-14 16:49:01+00:00"],
                "badPwdCount": [1],
                "accountExpires": ["9999-12-31 23:59:59.999999"],
                "displayName": ["example user"],
                "name": ["user"],
                "memberOf": ["CN=\\\\u05e7\\\\u05d1\\\\u05d5\\\\u05e6\\\\u05d4 \\\\u05d1\\\\u05e2\\\\u05d1\\\\u05e8\\\\u05d9\\\\u05ea,OU=TEST,OU=QA,OU=IT,OU=TLV,OU=host,DC=domain,DC=LOCAL", "CN=Organization Management,OU=Microsoft Exchange Security Groups,DC=domain,DC=LOCAL", "CN=Local Admin,OU=Groups,OU=IT,OU=TLV,OU=host,DC=domain,DC=LOCAL"],
                "codePage": [0],
                "userAccountControl": [111],
                "sAMAccountType": [805306368],
                "uSNChanged": [15301168],
                "sn": ["example"],
                "givenName": ["user"],
                "lastLogoff": ["1601-01-01 00:00:00+00:00"
                              ]},
            "Entity": "user@example.com"
        }
    ]
    

##### Script result

The following table lists the value for the script result output when using the **Enrich Entities** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Force Password Update

Use the **Force Password Update** action to require a user to change their password upon the following sign-in.

This action runs on the Google SecOps `User` entity.

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
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Force Password Update** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Group Members

Use the **Get Group Members** action to retrieve the members of a specified Active Directory group.

This action supports retrieving both the user and hostname members and supports searching within nested groups.

#### Action inputs

The **Get Group Members** action requires the following parameters:

Parameter | Description  
---|---  
`Group Name` | Required.The name of the group that contains the listed members.  
`Members Type` | Required.The member type of the group. The default value is `User`.  
`Perform Nested Search` | Optional.If selected, the action retrieves additional details about the groups that are a part of the main group.Not selected by default.  
`Limit` | Required.The maximum number of listings to retrieve from Active Directory.The default value is 100.  
  
#### Action outputs

The **Get Group Members** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Get Group Members** action:
    
    
    [
      {
        "cn":"Example User1",
        "displayName":"Example User1",
        "distinguishedName":"CN=Example User1,OU=User Accounts,DC=example,DC=local"
      },
      {
        "cn":"Example User2",
        "displayName":"Example User2",
        "distinguishedName":"CN=Example User2,CN=Users,DC=example,DC=local"
      },
      {
        "cn":"Example User3",
        "displayName":"Example User3",
        "distinguishedName":"CN=Example User3,CN=Users,DC=example,DC=local"
      }
    ]
    

##### Script result

The following table lists the value for the script result output when using the **Get Group Members** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Get Manager Contact Details

Use the **Get Manager Contact Details** action to obtain the manager contact details from Active Directory.

This action runs on the Google SecOps `User` entity.

#### Action inputs

None.

#### Action outputs

The **Get Manager Contact Details** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Entity enrichment table | Available  
JSON result | Available  
Output messages | Available  
Script result | Available  
  
##### Entity enrichment

The **Get Manager Contact Details** action supports the following entity enrichment:

Enrichment field name | Logic  
---|---  
`AD_Manager_Name` | The action returns the value if it exists in the JSON result.  
`AD_Manager_phone` | The action returns the value if it exists in the JSON result.  
`AD_primaryGroupID` | The action returns the value if it exists in the JSON result.  
`AD_logonCount` | The action returns the value if it exists in the JSON result.  
`AD_cn` | The action returns the value if it exists in the JSON result.  
`AD_countryCode` | The action returns the value if it exists in the JSON result.  
`AD_objectClass` | The action returns the value if it exists in the JSON result.  
`AD_userPrincipalName` | The action returns the value if it exists in the JSON result.  
`AD_adminCount` | The action returns the value if it exists in the JSON result.  
`AD_lastLogonTimestamp` | The action returns the value if it exists in the JSON result.  
`AD_manager` | The action returns the value if it exists in the JSON result.  
`AD_instanceType` | The action returns the value if it exists in the JSON result.  
`AD_distinguishedName` | The action returns the value if it exists in the JSON result.  
`AD_dSCorePropagationData` | The action returns the value if it exists in the JSON result.  
`AD_msDS-SupportedEncryptionTypes` | The action returns the value if it exists in the JSON result.  
`AD_objectSid` | The action returns the value if it exists in the JSON result.  
`AD_whenCreated` | The action returns the value if it exists in the JSON result.  
`AD_uSNCreated` | The action returns the value if it exists in the JSON result.  
`AD_lockoutTime` | The action returns the value if it exists in the JSON result.  
`AD_badPasswordTime` | The action returns the value if it exists in the JSON result.  
`AD_pwdLastSet` | The action returns the value if it exists in the JSON result.  
`AD_sAMAccountName` | The action returns the value if it exists in the JSON result.  
`AD_objectCategory` | The action returns the value if it exists in the JSON result.  
`AD_lastLogon` | The action returns the value if it exists in the JSON result.  
`AD_objectGUID` | The action returns the value if it exists in the JSON result.  
`AD_whenChanged` | The action returns the value if it exists in the JSON result.  
`AD_badPwdCount` | The action returns the value if it exists in the JSON result.  
`AD_accountExpires` | The action returns the value if it exists in the JSON result.  
`AD_displayName` | The action returns the value if it exists in the JSON result.  
`AD_name` | The action returns the value if it exists in the JSON result.  
`AD_memberOf` | The action returns the value if it exists in the JSON result.  
`AD_codePage` | The action returns the value if it exists in the JSON result.  
`AD_userAccountControl` | The action returns the value if it exists in the JSON result.  
`AD_sAMAccountType` | The action returns the value if it exists in the JSON result.  
`AD_uSNChanged` | The action returns the value if it exists in the JSON result.  
`AD_sn` | The action returns the value if it exists in the JSON result.  
`AD_givenName` | The action returns the value if it exists in the JSON result.  
`AD_lastLogoff` | The action returns the value if it exists in the JSON result.  
  
##### JSON result

The following example shows the JSON result output received when using the **Get Manager Contact Details** action:
    
    
    [
       {
            "EntityResult":
            {
                "primaryGroupID": [513],
                "logonCount": [6505],
                "cn": ["user name"],
                "countryCode": [0],
                "objectClass": ["top", "person", "organizationalPerson"],
                "userPrincipalName": ["user@example.com"],
                "adminCount": [1],
                "lastLogonTimestamp": ["2019-01-09 08:42:03.540783+00:00"],
                "manager": ["CN=user name,OU=R&D,OU=TLV,OU=host name,DC=domain,DC=LOCAL"],
                "instanceType": [4],
                "distinguishedName": ["CN=user name,OU=R&D,OU=TLV,OU=host,DC=domain,DC=LOCAL"],
                "dSCorePropagationData": ["2019-01-14 14:39:16+00:00"],
                "msDS-SupportedEncryptionTypes": [0],
                "objectSid": ["ID"],
                "whenCreated": ["2011-11-07 08:00:44+00:00"],
                "uSNCreated": [7288202],
                "lockoutTime": ["1601-01-01 00:00:00+00:00"],
                "badPasswordTime": ["date"],
                "pwdLastSet": ["date"],
                "sAMAccountName": ["example"],
                "objectCategory": ["CN=Person,CN=Schema,CN=Configuration,DC=host,DC=LOCAL"],
                "lastLogon": ["2019-01-14 17:13:54.463070+00:00"],
                "objectGUID": ["{id}"],
                "whenChanged": ["2019-01-14 16:49:01+00:00"],
                "badPwdCount": [1],
                "accountExpires": ["9999-12-31 23:59:59.999999"],
                "displayName": ["example"],
                "name": ["user"],
                "memberOf": ["CN= u05e7 u05d1 u05d5 u05e6 u05d4  u05d1 u05e2 u05d1 u05e8 u05d9 u05ea,OU=TEST,OU=QA,OU=IT,OU=TLV,OU=host,DC=domain,DC=LOCAL", "CN=Organization Management,OU=Microsoft Exchange Security Groups,DC=domain,DC=LOCAL", "CN=Local Admin,OU=Groups,OU=IT,OU=TLV,OU=host,DC=domain,DC=LOCAL"],
                "codePage": [0],
                "userAccountControl": [111],
                "sAMAccountType": [805306368],
                "uSNChanged": [15301168],
                "sn": ["example"],
                "givenName": ["user"],
                "lastLogoff": ["1601-01-01 00:00:00+00:00"]
            },
            "Entity": "user@example.com"
        }
    ]
    

##### Output messages

The **Ping** action can return the following output messages:

Output message | Message description  
---|---  
`All entities were processed successfully.` `Some entities were processed successfully and some weren't. Please check the action log for further information.` `No entities were processed.` | The action succeeded.  
`Error executing action "Get Manager Contact Details". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Get Manager Contact Details** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Is User in Group

Use the **Is User in Group** action to check if the user is a member of a specific group.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **Is User in Group** action requires the following parameters:

Parameter | Description  
---|---  
`Group Name` | Required.The group name to check, such as `administrators`.  
  
#### Action outputs

The **Is User in Group** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **Is User in Group** action:
    
    
    [
        {
            "EntityResult": true,
            "Entity": "USER1@EXAMPLE.COM"
        }, {
            "EntityResult": false,
            "Entity": "USER2@EXAMPLE.COM"
        }, {
            "EntityResult": true,
            "Entity": "USER3@EXAMPLE.COM"
        }
    ]
    

##### Script result

The following table lists the value for the script result output when using the **Is User in Group** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### List User Groups

Use the **List User Groups** action to obtain a list of all user groups that are available in Active Directory.

This action runs on the Google SecOps `User` entity.

#### Action inputs

None.

#### Action outputs

The **List User Groups** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Available  
Script result | Available  
  
##### JSON result

The following example shows the JSON result output received when using the **List User Groups** action:
    
    
    [
        {
            "EntityResult": ["Domain Users"],
            "Entity": "user@example.com"
        }
    ]
    

##### Script result

The following table lists the value for the script result output when using the **List User Groups** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Ping

Use the **Ping** action to test the connectivity to Active Directory.

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
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Ping** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Release Locked Account

Use the **Release Locked Account** action to unblock a locked account.

This action runs on the Google SecOps `User` entity.

#### Action inputs

None.

#### Action outputs

The **Release Locked Account** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Release Locked Account** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Remove User From Group

Use the **Remove User From Group** action to remove the user from groups.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **Remove User From Group** action requires the following parameters:

Parameter | Description  
---|---  
`Group Name` | Required.A comma-separated list of groups to remove the users from.  
  
#### Action outputs

The **Remove User From Group** action provides the following outputs:

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

The **Remove User From Group** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully removed the following users from the group "GROUP_NAME" in Active Directory: ENTITY_ID` `The following users were not a part of the group "GROUP_NAME" in Active Directory: ENTITY_ID` `Action wasn't able to remove the following users from the group "GROUP_NAME" in Active Directory: ENTITY_ID` `No users were removed from the group "GROUP_NAME" in Active Directory. ` `No users were removed from the provided groups in Active Directory.` | The action succeeded.  
`Error executing action "Remove User From Group". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Remove User From Group** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Search Active Directory

Use the **Search Active Directory** action to search Active Directory using a specified query.

This action doesn't run on Google SecOps entities.

#### Action inputs

The **Search Active Directory** action requires the following parameters:

Parameter | Description  
---|---  
`Query String` | Required.The query string to execute in Active Directory.  
`Limit` | Optional.The maximum number of listings to retrieve from Active Directory.  
  
#### Action outputs

The **Search Active Directory** action provides the following outputs:

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

The following example shows the JSON result output received when using the **Search Active Directory** action:
    
    
    [
          {
            "primaryGroupID": [
              513
            ],
            "logonCount": [
              6505
            ],
            "cn": [
              "user name"
            ],
            "countryCode": [
              0
            ],
            "objectClass": [
              "top",
              "person",
              "organizationalPerson"
            ],
            "userPrincipalName": [
              "user@example.com"
            ],
            "adminCount": [
              1
            ],
            "lastLogonTimestamp": [
              "2019-01-09 08:42:03.540783+00:00"
            ],
            "manager": [
              "CN=user name,OU=R&D,OU=TLV,OU=host name,DC=domain,DC=LOCAL"
            ],
            "instanceType": [
              4
            ],
            "distinguishedName": [
              "CN=user name,OU=R&D,OU=TLV,OU=host,DC=domain,DC=LOCAL"
            ],
            "dSCorePropagationData": [
              "2019-01-14 14:39:16+00:00"
            ],
            "msDS-SupportedEncryptionTypes": [
              0
            ],
            "objectSid": [
              "ID"
            ],
            "whenCreated": [
              "2011-11-07 08:00:44+00:00"
            ],
            "uSNCreated": [
              7288202
            ],
            "lockoutTime": [
              "1601-01-01 00:00:00+00:00"
            ],
            "badPasswordTime": [
              "date"
            ],
            "pwdLastSet": [
              "date"
            ],
            "sAMAccountName": [
              "example"
            ],
            "objectCategory": [
              "CN=Person,CN=Schema,CN=Configuration,DC=host,DC=LOCAL"
            ],
            "lastLogon": [
              "2019-01-14 17:13:54.463070+00:00"
            ],
            "objectGUID": [
              "GUID"
            ],
            "whenChanged": [
              "2019-01-14 16:49:01+00:00"
            ],
            "badPwdCount": [
              1
            ],
            "accountExpires": [
              "9999-12-31 23:59:59.999999"
            ],
            "displayName": [
              "example"
            ],
            "name": [
              "user"
            ],
            "memberOf": [
              "CN=\\\\u05e7\\\\u05d1\\\\u05d5\\\\u05e6\\\\u05d4 \\\\u05d1\\\\u05e2\\\\u05d1\\\\u05e8\\\\u05d9\\\\u05ea,OU=TEST,OU=QA,OU=IT,OU=TLV,OU=host,DC=domain,DC=LOCAL",
              "CN=Organization Management,OU=Microsoft Exchange Security Groups,DC=domain,DC=LOCAL",
              "CN=Local Admin,OU=Groups,OU=IT,OU=TLV,OU=host,DC=domain,DC=LOCAL"
            ],
            "codePage": [
              0
            ],
            "userAccountControl": [
              111
            ],
            "sAMAccountType": [
              805306368
            ],
            "uSNChanged": [
              15301168
            ],
            "sn": [
              "example"
            ],
            "givenName": [
              "user"
            ],
            "lastLogoff": [
              "1601-01-01 00:00:00+00:00"
            ]
          }
        ]
    

##### Output messages

The **Search Active Directory** action can return the following output messages:

Output message | Message description  
---|---  
`Successfully performed the query "QUERY_STRING" in Active Directory.` `No results to show following the query: "QUERY_STRING".` | The action succeeded.  
`Error executing action "Search Active Directory". Reason: ERROR_REASON` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Search Active Directory** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Set User Password

Use the **Set User Password** action to configure the user password.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **Set User Password** action requires the following parameters:

Parameter | Description  
---|---  
`New Password` | Required.A new password value.  
  
#### Action outputs

The **Set User Password** action provides the following outputs:

Action output type | Availability  
---|---  
Case wall attachment | Not available  
Case wall link | Not available  
Case wall table | Not available  
Enrichment table | Not available  
JSON result | Not available  
Script result | Available  
  
##### Script result

The following table lists the value for the script result output when using the **Set User Password** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update attributes of an AD Host

Use the **Update attributes of an AD Host** action to update the attributes for the current hosts in Active Directory.

This action runs on the Google SecOps `Hostname` entity.

#### Action inputs

The **Update attributes of an AD Host** action requires the following parameters:

Parameter | Description  
---|---  
`Attribute Name` | Required.The name of the attribute to update, such as `Description`.  
`Attribute Value` | Required.A new value for the attribute.  
  
#### Action outputs

The **Update attributes of an AD Host** action provides the following outputs:

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

The **Update attributes of an AD Host** action can return the following output messages:

Output message | Message description  
---|---  
`Active Directory - Following entities were updated successfully: ENTITY_ID_LIST. ` `No suitable entities were found.` | The action succeeded.  
`Failed to update the ATTRIBUTE_NAME for the following entities: ENTITY_ID_LIST.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Update attributes of an AD Host** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
### Update attributes of an AD User

Use the **Update attributes of an AD User** action to update the attributes for the current users in Active Directory.

This action runs on the Google SecOps `User` entity.

#### Action inputs

The **Update attributes of an AD User** action requires the following parameters:

Parameter | Description  
---|---  
`Attribute Name` | Required.The name of the attribute to update, such as `Description`.  
`Attribute Value` | Required.A new value for the attribute.  
  
#### Action outputs

The **Update attributes of an AD User** action provides the following outputs:

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

The **Update attributes of an AD User** action can return the following output messages:

Output message | Message description  
---|---  
`Active Directory - Following entities were updated successfully: ENTITY_ID_LIST. ` `No suitable entities were found.` | The action succeeded.  
`Failed to update the ATTRIBUTE_NAME for the following entities: ENTITY_ID_LIST.` | The action failed.Check the connection to the server, input parameters, or credentials.  
  
##### Script result

The following table lists the value for the script result output when using the **Update attributes of an AD User** action:

Script result name | Value  
---|---  
`is_success` | `True` or `False`  
  
**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
