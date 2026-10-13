---
url: https://docs.cloud.google.com/identity/docs/reference/rest/
title: Cloud Identity API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:33.783528+00:00
---

# Cloud Identity API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Cloud Identity API Stay organized with collections  Save and categorize content based on your preferences. 

API for provisioning and managing identity resources.

## Service: cloudidentity.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://cloudidentity.googleapis.com/$discovery/rest?version=v1>
  * <https://cloudidentity.googleapis.com/$discovery/rest?version=v1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://cloudidentity.googleapis.com`



## REST Resource: [v1beta1.allowlistedDomains](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/allowlistedDomains)

Methods  
---  
`[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/allowlistedDomains/create)` |  `POST /v1beta1/allowlistedDomains`   
Adds a domain to the allowlist.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/allowlistedDomains/delete)` |  `DELETE /v1beta1/{name=allowlistedDomains/*}`   
Removes a domain from the allowlist.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/allowlistedDomains/get)` |  `GET /v1beta1/{name=allowlistedDomains/*}`   
Retrieves a specific domain from the allowlist.  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/allowlistedDomains/list)` |  `GET /v1beta1/allowlistedDomains`   
Lists the domains in the allowlist.  
  
## REST Resource: [v1beta1.customers.userinvitations](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations/cancel)` |  `POST /v1beta1/{name=customers/*/userinvitations/*}:cancel`   
Cancels a `[UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations#UserInvitation)` that was already sent.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations/get)` |  `GET /v1beta1/{name=customers/*/userinvitations/*}`   
Retrieves a `[UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations#UserInvitation)` resource.  
`[isInvitableUser](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations/isInvitableUser)` |  `GET /v1beta1/{name=customers/*/userinvitations/*}:isInvitableUser`   
Verifies whether a user account is eligible to receive a `[UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations#UserInvitation)` (is an unmanaged account).  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations/list)` |  `GET /v1beta1/{parent=customers/*}/userinvitations`   
Retrieves a list of `[UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations#UserInvitation)` resources.  
`[send](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations/send)` |  `POST /v1beta1/{name=customers/*/userinvitations/*}:send`   
Sends a `[UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/customers.userinvitations#UserInvitation)` to email.  
  
## REST Resource: [v1beta1.devices](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices)

Methods  
---  
`[cancelWipe](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices/cancelWipe)` |  `POST /v1beta1/{name=devices/*}:cancelWipe`   
Cancels an unfinished device wipe.  
`[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices/create)` |  `POST /v1beta1/devices`   
Creates a device.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices/delete)` |  `DELETE /v1beta1/{name=devices/*}`   
Deletes the specified device.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices/get)` |  `GET /v1beta1/{name=devices/*}`   
Retrieves the specified device.  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices/list)` |  `GET /v1beta1/devices`   
Lists/Searches devices.  
`[wipe](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices/wipe)` |  `POST /v1beta1/{name=devices/*}:wipe`   
Wipes all data on the specified device.  
  
## REST Resource: [v1beta1.devices.deviceUsers](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices.deviceUsers)

Methods  
---  
`[approve](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices.deviceUsers/approve)` |  `POST /v1beta1/{name=devices/*/deviceUsers/*}:approve`   
Approves device to access user data.  
`[block](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices.deviceUsers/block)` |  `POST /v1beta1/{name=devices/*/deviceUsers/*}:block`   
Blocks device from accessing user data  
`[cancelWipe](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices.deviceUsers/cancelWipe)` |  `POST /v1beta1/{name=devices/*/deviceUsers/*}:cancelWipe`   
Cancels an unfinished user account wipe.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices.deviceUsers/delete)` |  `DELETE /v1beta1/{name=devices/*/deviceUsers/*}`   
Deletes the specified DeviceUser.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices.deviceUsers/get)` |  `GET /v1beta1/{name=devices/*/deviceUsers/*}`   
Retrieves the specified DeviceUser  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices.deviceUsers/list)` |  `GET /v1beta1/{parent=devices/*}/deviceUsers`   
Lists/Searches DeviceUsers.  
`[lookup](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices.deviceUsers/lookup)` |  `GET /v1beta1/{parent=devices/*/deviceUsers}:lookup`   
Looks up resource names of the DeviceUsers associated with the caller's credentials, as well as the properties provided in the request.  
`[wipe](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices.deviceUsers/wipe)` |  `POST /v1beta1/{name=devices/*/deviceUsers/*}:wipe`   
Wipes the user's account on a device.  
  
## REST Resource: [v1beta1.devices.deviceUsers.clientStates](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices.deviceUsers.clientStates)

Methods  
---  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices.deviceUsers.clientStates/get)` |  `GET /v1beta1/{name=devices/*/deviceUsers/*/clientStates/*}`   
Gets the client state for the device user  
`[patch](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/devices.deviceUsers.clientStates/patch)` |  `PATCH /v1beta1/{clientState.name=devices/*/deviceUsers/*/clientStates/*}`   
Updates the client state for the device user**Note** : This method is available only to customers who have one of the following SKUs: Enterprise Standard, Enterprise Plus, Enterprise for Education, and Cloud Identity Premium  
  
## REST Resource: [v1beta1.groups](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups)

Methods  
---  
`[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/create)` |  `POST /v1beta1/groups`   
Creates a `Group`.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/delete)` |  `DELETE /v1beta1/{name=groups/*}`   
Deletes a `Group`.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/get)` |  `GET /v1beta1/{name=groups/*}`   
Retrieves a `Group`.  
`[getSecuritySettings](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/getSecuritySettings)` |  `GET /v1beta1/{name=groups/*/securitySettings}`   
Get Security Settings  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/list)` |  `GET /v1beta1/groups`   
Lists the `Group` resources under a customer or namespace.  
`[lookup](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/lookup)` |  `GET /v1beta1/groups:lookup`   
Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a `Group` by its `EntityKey`.  
`[patch](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/patch)` |  `PATCH /v1beta1/{resource.name=groups/*}`   
Updates a `Group`.  
`[search](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/search)` |  `GET /v1beta1/groups:search`   
Searches for `Group` resources matching a specified query.  
`[updateSecuritySettings](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups/updateSecuritySettings)` |  `PATCH /v1beta1/{securitySettings.name=groups/*/securitySettings}`   
Update Security Settings  
  
## REST Resource: [v1beta1.groups.memberships](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships)

Methods  
---  
`[checkTransitiveMembership](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/checkTransitiveMembership)` |  `GET /v1beta1/{parent=groups/*}/memberships:checkTransitiveMembership`   
Check a potential member for membership in a group.  
`[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/create)` |  `POST /v1beta1/{parent=groups/*}/memberships`   
Creates a `Membership`.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/delete)` |  `DELETE /v1beta1/{name=groups/*/memberships/*}`   
Deletes a `Membership`.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/get)` |  `GET /v1beta1/{name=groups/*/memberships/*}`   
Retrieves a `Membership`.  
`[getMembershipGraph](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/getMembershipGraph)` |  `GET /v1beta1/{parent=groups/*}/memberships:getMembershipGraph`   
Get a membership graph of just a member or both a member and a group.  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/list)` |  `GET /v1beta1/{parent=groups/*}/memberships`   
Lists the `Membership`s within a `Group`.  
`[lookup](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/lookup)` |  `GET /v1beta1/{parent=groups/*}/memberships:lookup`   
Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a `Membership` by its `EntityKey`.  
`[modifyMembershipRoles](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/modifyMembershipRoles)` |  `POST /v1beta1/{name=groups/*/memberships/*}:modifyMembershipRoles`   
Modifies the `MembershipRole`s of a `Membership`.  
`[searchDirectGroups](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/searchDirectGroups)` |  `GET /v1beta1/{parent=groups/*}/memberships:searchDirectGroups`   
Searches direct groups of a member.  
`[searchTransitiveGroups](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/searchTransitiveGroups)` |  `GET /v1beta1/{parent=groups/*}/memberships:searchTransitiveGroups`   
Search transitive groups of a member.  
`[searchTransitiveMemberships](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/groups.memberships/searchTransitiveMemberships)` |  `GET /v1beta1/{parent=groups/*}/memberships:searchTransitiveMemberships`   
Search transitive memberships of a group.  
  
## REST Resource: [v1beta1.inboundOidcSsoProfiles](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundOidcSsoProfiles)

Methods  
---  
`[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundOidcSsoProfiles/create)` |  `POST /v1beta1/inboundOidcSsoProfiles`   
Creates an `[InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundOidcSsoProfiles#InboundOidcSsoProfile)` for a customer.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundOidcSsoProfiles/delete)` |  `DELETE /v1beta1/{name=inboundOidcSsoProfiles/*}`   
Deletes an `[InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundOidcSsoProfiles#InboundOidcSsoProfile)`.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundOidcSsoProfiles/get)` |  `GET /v1beta1/{name=inboundOidcSsoProfiles/*}`   
Gets an `[InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundOidcSsoProfiles#InboundOidcSsoProfile)`.  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundOidcSsoProfiles/list)` |  `GET /v1beta1/inboundOidcSsoProfiles`   
Lists `[InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundOidcSsoProfiles#InboundOidcSsoProfile)` objects for a Google enterprise customer.  
`[patch](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundOidcSsoProfiles/patch)` |  `PATCH /v1beta1/{inboundOidcSsoProfile.name=inboundOidcSsoProfiles/*}`   
Updates an `[InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundOidcSsoProfiles#InboundOidcSsoProfile)`.  
  
## REST Resource: [v1beta1.inboundSamlSsoProfiles](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles)

Methods  
---  
`[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles/create)` |  `POST /v1beta1/inboundSamlSsoProfiles`   
Creates an `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles#InboundSamlSsoProfile)` for a customer.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles/delete)` |  `DELETE /v1beta1/{name=inboundSamlSsoProfiles/*}`   
Deletes an `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles#InboundSamlSsoProfile)`.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles/get)` |  `GET /v1beta1/{name=inboundSamlSsoProfiles/*}`   
Gets an `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles#InboundSamlSsoProfile)`.  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles/list)` |  `GET /v1beta1/inboundSamlSsoProfiles`   
Lists `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles#InboundSamlSsoProfile)`s for a customer.  
`[patch](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles/patch)` |  `PATCH /v1beta1/{inboundSamlSsoProfile.name=inboundSamlSsoProfiles/*}`   
Updates an `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles#InboundSamlSsoProfile)`.  
  
## REST Resource: [v1beta1.inboundSamlSsoProfiles.idpCredentials](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles.idpCredentials)

Methods  
---  
`[add](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles.idpCredentials/add)` |  `POST /v1beta1/{parent=inboundSamlSsoProfiles/*}/idpCredentials:add`   
Adds an `[IdpCredential](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles.idpCredentials#IdpCredential)`.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles.idpCredentials/delete)` |  `DELETE /v1beta1/{name=inboundSamlSsoProfiles/*/idpCredentials/*}`   
Deletes an `[IdpCredential](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles.idpCredentials#IdpCredential)`.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles.idpCredentials/get)` |  `GET /v1beta1/{name=inboundSamlSsoProfiles/*/idpCredentials/*}`   
Gets an `[IdpCredential](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles.idpCredentials#IdpCredential)`.  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles.idpCredentials/list)` |  `GET /v1beta1/{parent=inboundSamlSsoProfiles/*}/idpCredentials`   
Returns a list of `[IdpCredential](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles.idpCredentials#IdpCredential)`s in an `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles#InboundSamlSsoProfile)`.  
  
## REST Resource: [v1beta1.inboundSsoAssignments](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments)

Methods  
---  
`[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments/create)` |  `POST /v1beta1/inboundSsoAssignments`   
Creates an `[InboundSsoAssignment](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#InboundSsoAssignment)` for users and devices in a `Customer` under a given `Group` or `OrgUnit`.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments/delete)` |  `DELETE /v1beta1/{name=inboundSsoAssignments/*}`   
Deletes an `[InboundSsoAssignment](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#InboundSsoAssignment)`.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments/get)` |  `GET /v1beta1/{name=inboundSsoAssignments/*}`   
Gets an `[InboundSsoAssignment](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#InboundSsoAssignment)`.  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments/list)` |  `GET /v1beta1/inboundSsoAssignments`   
Lists the `[InboundSsoAssignment](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#InboundSsoAssignment)`s for a `Customer`.  
`[patch](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments/patch)` |  `PATCH /v1beta1/{inboundSsoAssignment.name=inboundSsoAssignments/*}`   
Updates an `[InboundSsoAssignment](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#InboundSsoAssignment)`.  
  
## REST Resource: [v1beta1.orgUnits.memberships](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships)

Methods  
---  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships/list)` |  `GET /v1beta1/{parent=orgUnits/*}/memberships`   
List `[OrgMembership](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships#OrgMembership)` resources in an OrgUnit treated as 'parent'.  
`[move](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships/move)` |  `POST /v1beta1/{name=orgUnits/*/memberships/*}:move`   
Move an `[OrgMembership](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/orgUnits.memberships#OrgMembership)` to a new OrgUnit.  
  
## REST Resource: [v1beta1.policies](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies)

Methods  
---  
`[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies/create)` |  `POST /v1beta1/policies`   
Create a policy.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies/delete)` |  `DELETE /v1beta1/{name=policies/*}`   
Delete a policy.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies/get)` |  `GET /v1beta1/{name=policies/*}`   
Get a policy.  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies/list)` |  `GET /v1beta1/policies`   
List policies.  
`[patch](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/policies/patch)` |  `PATCH /v1beta1/{policy.name=policies/*}`   
Update a policy.  
  
## REST Resource: [v1.allowlistedDomains](https://docs.cloud.google.com/identity/docs/reference/rest/v1/allowlistedDomains)

Methods  
---  
`[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1/allowlistedDomains/create)` |  `POST /v1/allowlistedDomains`   
Adds a domain to the allowlist.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1/allowlistedDomains/delete)` |  `DELETE /v1/{name=allowlistedDomains/*}`   
Removes a domain from the allowlist.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1/allowlistedDomains/get)` |  `GET /v1/{name=allowlistedDomains/*}`   
Retrieves a specific domain from the allowlist.  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1/allowlistedDomains/list)` |  `GET /v1/allowlistedDomains`   
Lists the domains in the allowlist.  
  
## REST Resource: [v1.customers.userinvitations](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations)

Methods  
---  
`[cancel](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations/cancel)` |  `POST /v1/{name=customers/*/userinvitations/*}:cancel`   
Cancels a `[UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations#UserInvitation)` that was already sent.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations/get)` |  `GET /v1/{name=customers/*/userinvitations/*}`   
Retrieves a `[UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations#UserInvitation)` resource.  
`[isInvitableUser](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations/isInvitableUser)` |  `GET /v1/{name=customers/*/userinvitations/*}:isInvitableUser`   
Verifies whether a user account is eligible to receive a `[UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations#UserInvitation)` (is an unmanaged account).  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations/list)` |  `GET /v1/{parent=customers/*}/userinvitations`   
Retrieves a list of `[UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations#UserInvitation)` resources.  
`[send](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations/send)` |  `POST /v1/{name=customers/*/userinvitations/*}:send`   
Sends a `[UserInvitation](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations#UserInvitation)` to email.  
  
## REST Resource: [v1.devices](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices)

Methods  
---  
`[cancelWipe](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices/cancelWipe)` |  `POST /v1/{name=devices/*}:cancelWipe`   
Cancels an unfinished device wipe.  
`[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices/create)` |  `POST /v1/devices`   
Creates a device.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices/delete)` |  `DELETE /v1/{name=devices/*}`   
Deletes the specified device.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices/get)` |  `GET /v1/{name=devices/*}`   
Retrieves the specified device.  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices/list)` |  `GET /v1/devices`   
Lists/Searches devices.  
`[wipe](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices/wipe)` |  `POST /v1/{name=devices/*}:wipe`   
Wipes all data on the specified device.  
  
## REST Resource: [v1.devices.deviceUsers](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers)

Methods  
---  
`[approve](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/approve)` |  `POST /v1/{name=devices/*/deviceUsers/*}:approve`   
Approves device to access user data.  
`[block](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/block)` |  `POST /v1/{name=devices/*/deviceUsers/*}:block`   
Blocks device from accessing user data  
`[cancelWipe](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/cancelWipe)` |  `POST /v1/{name=devices/*/deviceUsers/*}:cancelWipe`   
Cancels an unfinished user account wipe.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/delete)` |  `DELETE /v1/{name=devices/*/deviceUsers/*}`   
Deletes the specified DeviceUser.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/get)` |  `GET /v1/{name=devices/*/deviceUsers/*}`   
Retrieves the specified DeviceUser  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/list)` |  `GET /v1/{parent=devices/*}/deviceUsers`   
Lists/Searches DeviceUsers.  
`[lookup](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/lookup)` |  `GET /v1/{parent=devices/*/deviceUsers}:lookup`   
Looks up resource names of the DeviceUsers associated with the caller's credentials, as well as the properties provided in the request.  
`[wipe](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers/wipe)` |  `POST /v1/{name=devices/*/deviceUsers/*}:wipe`   
Wipes the user's account on a device.  
  
## REST Resource: [v1.devices.deviceUsers.clientStates](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers.clientStates)

Methods  
---  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers.clientStates/get)` |  `GET /v1/{name=devices/*/deviceUsers/*/clientStates/*}`   
Gets the client state for the device user  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers.clientStates/list)` |  `GET /v1/{parent=devices/*/deviceUsers/*}/clientStates`   
Lists the client states for the given search query.  
`[patch](https://docs.cloud.google.com/identity/docs/reference/rest/v1/devices.deviceUsers.clientStates/patch)` |  `PATCH /v1/{clientState.name=devices/*/deviceUsers/*/clientStates/*}`   
Updates the client state for the device user**Note** : This method is available only to customers who have one of the following SKUs: Enterprise Standard, Enterprise Plus, Enterprise for Education, and Cloud Identity Premium  
  
## REST Resource: [v1.groups](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups)

Methods  
---  
`[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/create)` |  `POST /v1/groups`   
Creates a Group.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/delete)` |  `DELETE /v1/{name=groups/*}`   
Deletes a `Group`.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/get)` |  `GET /v1/{name=groups/*}`   
Retrieves a `Group`.  
`[getSecuritySettings](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/getSecuritySettings)` |  `GET /v1/{name=groups/*/securitySettings}`   
Get Security Settings  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/list)` |  `GET /v1/groups`   
Lists the `Group` resources under a customer or namespace.  
`[lookup](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/lookup)` |  `GET /v1/groups:lookup`   
Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a `Group` by its `EntityKey`.  
`[patch](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/patch)` |  `PATCH /v1/{resource.name=groups/*}`   
Updates a `Group`.  
`[search](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/search)` |  `GET /v1/groups:search`   
Searches for `Group` resources matching a specified query.  
`[updateSecuritySettings](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups/updateSecuritySettings)` |  `PATCH /v1/{securitySettings.name=groups/*/securitySettings}`   
Update Security Settings  
  
## REST Resource: [v1.groups.memberships](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships)

Methods  
---  
`[checkTransitiveMembership](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/checkTransitiveMembership)` |  `GET /v1/{parent=groups/*}/memberships:checkTransitiveMembership`   
Check a potential member for membership in a group.  
`[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/create)` |  `POST /v1/{parent=groups/*}/memberships`   
Creates a `Membership`.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/delete)` |  `DELETE /v1/{name=groups/*/memberships/*}`   
Deletes a `Membership`.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/get)` |  `GET /v1/{name=groups/*/memberships/*}`   
Retrieves a `Membership`.  
`[getMembershipGraph](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/getMembershipGraph)` |  `GET /v1/{parent=groups/*}/memberships:getMembershipGraph`   
Get a membership graph of just a member or both a member and a group.  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/list)` |  `GET /v1/{parent=groups/*}/memberships`   
Lists the `Membership`s within a `Group`.  
`[lookup](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/lookup)` |  `GET /v1/{parent=groups/*}/memberships:lookup`   
Looks up the [resource name](https://cloud.google.com/apis/design/resource_names) of a `Membership` by its `EntityKey`.  
`[modifyMembershipRoles](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/modifyMembershipRoles)` |  `POST /v1/{name=groups/*/memberships/*}:modifyMembershipRoles`   
Modifies the `MembershipRole`s of a `Membership`.  
`[searchDirectGroups](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchDirectGroups)` |  `GET /v1/{parent=groups/*}/memberships:searchDirectGroups`   
Searches direct groups of a member.  
`[searchTransitiveGroups](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchTransitiveGroups)` |  `GET /v1/{parent=groups/*}/memberships:searchTransitiveGroups`   
Search transitive groups of a member.  
`[searchTransitiveMemberships](https://docs.cloud.google.com/identity/docs/reference/rest/v1/groups.memberships/searchTransitiveMemberships)` |  `GET /v1/{parent=groups/*}/memberships:searchTransitiveMemberships`   
Search transitive memberships of a group.  
  
## REST Resource: [v1.inboundOidcSsoProfiles](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles)

Methods  
---  
`[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles/create)` |  `POST /v1/inboundOidcSsoProfiles`   
Creates an `[InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles#InboundOidcSsoProfile)` for a customer.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles/delete)` |  `DELETE /v1/{name=inboundOidcSsoProfiles/*}`   
Deletes an `[InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles#InboundOidcSsoProfile)`.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles/get)` |  `GET /v1/{name=inboundOidcSsoProfiles/*}`   
Gets an `[InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles#InboundOidcSsoProfile)`.  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles/list)` |  `GET /v1/inboundOidcSsoProfiles`   
Lists `[InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles#InboundOidcSsoProfile)` objects for a Google enterprise customer.  
`[patch](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles/patch)` |  `PATCH /v1/{inboundOidcSsoProfile.name=inboundOidcSsoProfiles/*}`   
Updates an `[InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles#InboundOidcSsoProfile)`.  
  
## REST Resource: [v1.inboundSamlSsoProfiles](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles)

Methods  
---  
`[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles/create)` |  `POST /v1/inboundSamlSsoProfiles`   
Creates an `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles#InboundSamlSsoProfile)` for a customer.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles/delete)` |  `DELETE /v1/{name=inboundSamlSsoProfiles/*}`   
Deletes an `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles#InboundSamlSsoProfile)`.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles/get)` |  `GET /v1/{name=inboundSamlSsoProfiles/*}`   
Gets an `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles#InboundSamlSsoProfile)`.  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles/list)` |  `GET /v1/inboundSamlSsoProfiles`   
Lists `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles#InboundSamlSsoProfile)`s for a customer.  
`[patch](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles/patch)` |  `PATCH /v1/{inboundSamlSsoProfile.name=inboundSamlSsoProfiles/*}`   
Updates an `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles#InboundSamlSsoProfile)`.  
  
## REST Resource: [v1.inboundSamlSsoProfiles.idpCredentials](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials)

Methods  
---  
`[add](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials/add)` |  `POST /v1/{parent=inboundSamlSsoProfiles/*}/idpCredentials:add`   
Adds an `[IdpCredential](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials#IdpCredential)`.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials/delete)` |  `DELETE /v1/{name=inboundSamlSsoProfiles/*/idpCredentials/*}`   
Deletes an `[IdpCredential](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials#IdpCredential)`.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials/get)` |  `GET /v1/{name=inboundSamlSsoProfiles/*/idpCredentials/*}`   
Gets an `[IdpCredential](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials#IdpCredential)`.  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials/list)` |  `GET /v1/{parent=inboundSamlSsoProfiles/*}/idpCredentials`   
Returns a list of `[IdpCredential](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials#IdpCredential)`s in an `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles#InboundSamlSsoProfile)`.  
  
## REST Resource: [v1.inboundSsoAssignments](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSsoAssignments)

Methods  
---  
`[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSsoAssignments/create)` |  `POST /v1/inboundSsoAssignments`   
Creates an `[InboundSsoAssignment](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSsoAssignments#InboundSsoAssignment)` for users and devices in a `Customer` under a given `Group` or `OrgUnit`.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSsoAssignments/delete)` |  `DELETE /v1/{name=inboundSsoAssignments/*}`   
Deletes an `[InboundSsoAssignment](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSsoAssignments#InboundSsoAssignment)`.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSsoAssignments/get)` |  `GET /v1/{name=inboundSsoAssignments/*}`   
Gets an `[InboundSsoAssignment](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSsoAssignments#InboundSsoAssignment)`.  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSsoAssignments/list)` |  `GET /v1/inboundSsoAssignments`   
Lists the `[InboundSsoAssignment](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSsoAssignments#InboundSsoAssignment)`s for a `Customer`.  
`[patch](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSsoAssignments/patch)` |  `PATCH /v1/{inboundSsoAssignment.name=inboundSsoAssignments/*}`   
Updates an `[InboundSsoAssignment](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSsoAssignments#InboundSsoAssignment)`.  
  
## REST Resource: [v1.policies](https://docs.cloud.google.com/identity/docs/reference/rest/v1/policies)

Methods  
---  
`[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1/policies/create)` |  `POST /v1/policies`   
Create a policy.  
`[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1/policies/delete)` |  `DELETE /v1/{name=policies/*}`   
Delete a policy.  
`[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1/policies/get)` |  `GET /v1/{name=policies/*}`   
Get a policy.  
`[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1/policies/list)` |  `GET /v1/policies`   
List policies.  
`[patch](https://docs.cloud.google.com/identity/docs/reference/rest/v1/policies/patch)` |  `PATCH /v1/{policy.name=policies/*}`   
Update a policy.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-19 UTC."],[],[]] 
