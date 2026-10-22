---
url: https://docs.cloud.google.com/identity/docs/how-to/manage-user-invitations/
title: Creating and managing user invitations \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:20.228557+00:00
---

# Creating and managing user invitations  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/how-to/manage-user-invitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Guides ](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Creating and managing user invitations

This page explains how to perform some fundamental operations with the Cloud Identity User Invitation API.

## Before you begin

**Note:** Before you use any of the Cloud Identity APIs, you must set up Cloud Identity. See [Setting up Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin) for instructions.

Perform the following tasks before proceeding with the information on this page:

  * Read the [User Invitation API overview](https://docs.cloud.google.com/identity/docs/concepts/overview-user-invitations).
  * Set up the [User Invitation API](https://docs.cloud.google.com/identity/docs/how-to/setup-user-invitations).



## Determining invitation eligibility

As noted in the [overview](https://docs.cloud.google.com/identity/docs/concepts/overview-user-invitations), to be invited a user account must meet multiple criteria. You can use the [`IsInvitableUser()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations/isInvitableUser) method to find out if a given user account is eligible.

###  REST 

To check the eligibility of a user account, call [`customers.userinvitations.isInvitableUser()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations/isInvitableUser) with the customer ID and the account's email address.

**Sample request**
    
    
    GET https://cloudidentity.googleapis.com/v1/customers/C00000000/userinvitations/writer@altostrat.com:isInvitableUser
    

## Retrieving user invitations

The User Invitation API provides methods for retrieving a single user invitation and retrieving all of them. When retrieving all user invitations, you can optionally filter them by state and set the sorting order.

### Retrieving a single user invitation

###  REST 

To retrieve a single user invitation, call [`customers.userinvitations.get()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations/get) with the customer ID and the account's email address.

**Sample request**
    
    
    GET https://cloudidentity.googleapis.com/v1/customers/C00000000/userinvitations/writer@altostrat.com
    

### Retrieving a list of user invitations

All unmanaged users appear automatically as invitations in the `NOT_YET_SENT` state until otherwise acted upon by either the admin or the end user. Once an invitation is accepted by the user, the account is no longer considered unmanaged.

  * If you call [`customers.userinvitations.list()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations/list) with the state in the request, it will return only users whose invitation is in that state.
  * If you call [`customers.userinvitations.list()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations/list) without the state in the request, it will return all user invitations.



You can check for multiple states by adding an `or` operator in the filter: `state=='accepted'||state=='declined'`

###  REST 

To retrieve a list of user invitations, call [`customers.userinvitations.list()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations/list) with the customer ID and any desired query parameters to filter, order, and paginate the results. The following example returns a list of all unmanaged users, ordered by the last updated time in descending order.

**Sample request**
    
    
    GET https://cloudidentity.googleapis.com/v1/customers/C00000000/userinvitations?filter=state!='accepted'&orderBy='updateTime desc'
    

## Sending user invitations

User invitations are not automatically sent to eligible users. Once you have a list of the users you want to invite, you can use the [`customers.userinvitations.send()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations/send) method. This will also create an invitation if it doesn't exist.

###  REST 

To send a user invitation email to a user, call [`customers.userinvitations.send()`](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations/send) with the customer ID and the user account's email address.

**Sample request**
    
    
    POST https://cloudidentity.googleapis.com/v1/customers/C00000000/userinvitations/writer@altostrat.com:send
    

## Canceling user invitations

User invitations can be canceled until they are either accepted or declined. Call the [customers.userinvitations.cancel()](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations/cancel) method to cancel an invitation.

###  REST 

To cancel a user invitation, call [customers.userinvitations.cancel()](https://docs.cloud.google.com/identity/docs/reference/rest/v1/customers.userinvitations/cancel) with the customer ID and the user account's email address.

**Sample request**
    
    
    POST https://cloudidentity.googleapis.com/v1/customers/C00000000/userinvitations/writer@altostrat.com:cancel
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
