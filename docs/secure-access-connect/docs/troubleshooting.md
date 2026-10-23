---
url: https://docs.cloud.google.com/secure-access-connect/docs/troubleshooting/
title: Troubleshoot Secure Access Connect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:45:22.161667+00:00
---

# Troubleshoot Secure Access Connect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secure-access-connect/docs/troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Secure Access Connect ](https://docs.cloud.google.com/secure-access-connect/docs)
  * [ Guides ](https://docs.cloud.google.com/secure-access-connect/docs/overview)



Send feedback 

#  Troubleshoot Secure Access Connect Stay organized with collections  Save and categorize content based on your preferences. 

This page shows you how to resolve issues with Secure Access Connect.

## Attachment creation errors

This section lists errors that you might encounter when creating attachments and provides suggestions for how to fix each of them.

### Symantec attachment creation errors

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

#### Symantec connection is unsuccessful

When you identify the Symantec site that you want to connect your attachment to using the [`gcloud network-security secure-access-connect realms describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/network-security/secure-access-connect/realms/describe), the output indicates whether your Symantec connection is successful.

If the connection to Symantec is successful, the output contains the following line:
    
    
    symantecConnectionState: SUCCEEDED
    

If the output doesn't contain the preceding line, or the `symantecConnectionState` isn't `SUCCEEDED`, your connection to Symantec is unsuccessful.

This issue can be caused by one of the following reasons.

  * The API key that you uploaded when you [created a realm](https://docs.cloud.google.com/secure-access-connect/docs/create-realms#create-realm) isn't valid.

To resolve this issue, [verify the format of the secret](https://docs.cloud.google.com/secret-manager/docs/access-secret-version) that contains the API key. The secret must use the following format and must not include any white spaces or tabs:
        
        USERNAME:PASSWORD
        

If the secret doesn't match the preceding format, [edit the secret](https://docs.cloud.google.com/secret-manager/docs/edit-secrets). If the secret matches the preceding format, try generating and uploading a new API key.

  * The secret doesn't exist, the secret isn't associated with the realm, or the service account lacks permissions.

To resolve this issue, do the following:

    * [View the realm details](https://docs.cloud.google.com/secure-access-connect/docs/view-realms#view-realm-details) and confirm that the secret name is correct.

    * Verify and correct the permissions granted in [Create a Secure Access Connect realm](https://docs.cloud.google.com/secure-access-connect/docs/create-realms#create-realm).

  * The Symantec location might already be in use by an existing attachment.

To resolve this issue, make sure that you use a location that's not in use.

  * The Symantec site is temporarily unavailable.

To resolve this issue, check with Symantec about the availability of their service.




#### Connection states to Symantec

The following table lists the connection states to Symantec and what they mean.

State | Description  
---|---  
SYMANTEC_CONNECTION_STATE_UNSPECIFIED  | The default value when the state is omitted.   
SUCCEEDED  | Successfully connected to Symantec.   
READ_SECRET_FAILED  | Can't access the API key in the provided secret_path because the secret doesn't exist or the service account doesn't have the required permissions to read it.   
REQUEST_TO_SYMANTEC_FAILED  | Failed to get a successful response from Symantec API due to an invalid API key or Symantec API unavailability.   
  
### Palo Alto Network Prisma Access attachment creation errors

If you encounter a Palo Alto Network Prisma Access attachment creation error, check for the following issues.

  * You aren't setting Symantec-specific fields.

  * You aren't specifying an invalid resource name.

To resolve this issue, make sure that your resource name conforms with [RFC 1034](https://datatracker.ietf.org/doc/html/rfc1034), is restricted to lowercase letters, numbers and hyphens, and has a maximum length of 63 characters. Additionally, the first character must be a letter and the last a letter or a number.

  * A corresponding partner realm already exists and the associated realm is in the `PARTNER_ATTACHED` state.

If the realm isn't in the `PARTNER_ATTACHED` state, you must complete the attachment process in the Palo Alto Network Prisma Access console.




### Realm states

The following table lists the realm attachment states and what they mean.

Realm state | Description  
---|---  
STATE_UNSPECIFIED  | The default value used when the state is omitted.   
PENDING_PARTNER_ATTACHMENT  | This realm has never been attached to a partner realm. Used only for Palo Alto Networks Prisma Access.   
PARTNER_ATTACHED  | This realm is attached to a partner.   
PARTNER_DETACHED  | This realm was attached to a partner before but has been detached.   
KEY_EXPIRED  | This realm is not attached to a partner realm, and its pairing key has expired and needs key regeneration. Used only for Palo Alto Networks Prisma Access.   
  
### Attachment states

The following table lists the Secure Access Connect attachment states and what they mean.

Attachment state | Description  
---|---  
STATE_UNSPECIFIED  | No state specified.   
PENDING_PARTNER_ATTACHMENT  | The partner hasn't connected to the attachment. This is a transitional state and goes into PARTNER_ATTACHED after the attachment is successful.   
PARTNER_ATTACHED  | Attached to a partner.   
PARTNER_DETACHED  | Was attached to a partner before but has been detached.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
