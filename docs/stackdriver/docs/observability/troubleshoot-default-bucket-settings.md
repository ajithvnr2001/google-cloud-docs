---
url: https://docs.cloud.google.com/stackdriver/docs/observability/troubleshoot-default-bucket-settings/
title: Troubleshoot observability buckets \u00a0|\u00a0 Google Cloud Observability \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:58.140870+00:00
---

# Troubleshoot observability buckets  |  Google Cloud Observability  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/stackdriver/docs/observability/troubleshoot-default-bucket-settings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Google Cloud Observability ](https://docs.cloud.google.com/stackdriver/docs)



Send feedback 

#  Troubleshoot observability buckets Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to resolve failures that might be related to observability buckets. For example, this page describes how to resolve issues related to configuring default settings for observability buckets. You configure these default settings for a resource, which can be an organization, folder, or project, and they let you do the following:

  * Configure a default storage location for your observability buckets.
  * For each location where you choose to store data, you can configure use of customer-managed encryption keys (CMEKs).



Descendants in the resource hierarchy automatically use these settings, except for those descendants where you've configured default settings.

## You don't see any trace data

You expect to see data in the **Trace Explorer** page, but there isn't any data.

Trace data is stored in an observability buckets named `_Trace`. There are several reasons why you might not see trace data. To learn how to resolve this failure, see [No data in the **Trace Explorer** page](https://docs.cloud.google.com/trace/docs/troubleshooting#no-data-refresh).

## Issues related to the storage location

This section lists common issues related to setting or clearing the default storage location, which is a field in the default settings for observability buckets.

### Setting the default storage location for a resource fails

You try to [set the default storage location](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets#set-default-location) for a resource, but the command fails:

  * An attempt to set a location that isn't supported by observability buckets fails with a `400 (Bad Request)` error code. The failure message is similar to the following:
        
        Unsupported default storage location: my-region
        

  * An attempt to set the location to a value that an organization policy doesn't allow fails with a `400 (Bad Request)` error code. The failure message is similar to the following:
        
        Constraint `constraints/gcp.resourceLocations` violated for `folders/12345` attempting to change `folders/12345/locations/global/settings` with location `invalid`. The location must be in the allowed location list configured by the organization policy administrator.
        




To resolve these failures, do the following:

  * Make sure that the location you specify in the command is a [supported observability bucket location](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations).

  * Review your [organization policies](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets#app-org-policies) to make sure that these policies allow your location.




### A command to clear the default storage location fails

You issue an `updateSettings` command to a resource with the value of the default storage location set to an empty string. The command fails with a `400 (Bad Request)` error code. The error message is similar to one of the following:
    
    
    Before you can clear the default storage location for this resource, you must set a default storage location for an ancestor in the resource hierarchy.
    

or
    
    
    The default storage location may not be removed from an organization's Settings.
    

This is expected behavior.

After a default storage location for a resource is set, you can change the value but you can't clear or unset the value unless the default storage location is specified for an ancestor in the resource hierarchy. You can't clear or unset the default storage location for an organization because they don't have ancestors.

### The location of an observability bucket conflicts with an organization policy

You notice that the locations of some observability buckets conflict with the allowed locations an organization policy specifies.

This is not an error.

Organization policies that restrict location aren't honored by observability buckets.

There are several reasons why the location of an observability bucket might be in a location that an organization policy doesn't allow:

  * The observability bucket was created before June 1, 2026, which is the date when enforcement of the organization policy that restricts location began.

  * The organization policy changed after the observability bucket was created.




## Issues related to CMEKs

This section lists common issues related to using CMEKs.

### A command to clear the default Cloud KMS key fails

You issue an `updateSettings` command to a resource and location with the value of the default Cloud KMS key set to an empty string. The command fails with a `400 (Bad Request)` error code. The error message is similar to one of the following:
    
    
    The default KMS key cannot be empty because you have an organization policy that requires CMEK and because no ancestor defines a default KMS key.
    

or
    
    
    The default KMS key cannot be empty because you have an organization policy that requires CMEK.
    

This is expected behavior.

If you have an organization policy that requires use of CMEKs and have set a default Cloud KMS key for a resource and location, then you can't remove that key unless an ancestor of the resource has an appropriate default key. Because organizations don't have ancestors, you can't remove the default Cloud KMS key from the organization's default settings.

### How can I find the key used by an observability bucket?

To get information about the encryption key used for an observability buckets, [list your observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/storage-manage#list-buckets).

The response data includes information about the Cloud KMS key, its version, and the service account used to access the key.

### How do I resolve key configuration errors

After you configure a default Cloud KMS key for a resource and location you either receive an email notification from Google Cloud Observability about access issues or you notice read or write errors from observability buckets with CMEKs enabled. The email, which is sent to [essential Contacts](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts), contains information like the following:

  * Cloud KMS key name.
  * Cloud KMS key version.
  * Name of the service account used for encryption and decryption.
  * The error code seen by Google Cloud Observability when encrypting or decrypting data.
  * The error message seen when encrypting or decrypting data



The notification provides information about the failure and it lists actions that you can take to mitigate the issue:

Error | Recommendation  
---|---  
Cryptographic key permission denied | The resource's service account doesn't have sufficient IAM permissions to operate on the specified Cloud KMS key. To resolve this failure, follow the instructions in the error. The following information might be helpful to you:

  * Verify service account has required role
  * [Grant service account access to a key](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets#grant-role)

  
Cryptographic key is disabled | The specified Cloud KMS key was disabled. Follow the instructions in the error to re-enable the key. The following information might be helpful to you:

  * Verify a Cloud KMS key is usable
  * [Grant service account access to a key](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets#grant-role)

  
Cryptographic key was destroyed | The specified Cloud KMS key was destroyed. Follow the instructions or see [Manage your Cloud KMS key for a resource](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets#manage-keys).   
  
## Provisioning fails for an observability bucket

You are an [essential contact](https://docs.cloud.google.com/resource-manager/docs/managing-notification-contacts) or owner of a resource, and you receive an email notification from Google Cloud Observability about a provisioning failure.

Provisioning an observability bucket might fail due to a configuration error or to an internal error:

  * When provisioning fails due to an internal error, you don't need to take action. The system automatically recovers from these failures by retrying the create command until it is successful.

  * When provisioning fails due to a configuration error, you need to correct the error. Provided data continues to arrive, the system automatically issues at least one create observability bucket command per day. Configuration errors include the following:

    * An organization policy doesn't allow any supported observability bucket locations.
    * A default storage location conflicts with an organization policy.
    * An organization policy that requires CMEKs, but a default key isn't configured.
    * A Cloud KMS key isn't usable.
    * A service account is missing a required role.



The remainder of this section describes how to investigate common configuration issues.

### Review organization policy that constrains locations

Review the allowed locations specified by an organization policy with a constraint ID `constraints/gcp.resourceLocations`. This policy defines the set of locations where new resources can be created.

Make sure that the list of allowed locations includes at least one [supported observability bucket location](https://docs.cloud.google.com/stackdriver/docs/observability/observability-bucket-locations). Provisioning fails if the default storage location isn't an allowed location.

For more information, see [Viewing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies#viewing_organization_policies).

### Review the default storage locations for your resources

Review, and if necessary, update the default settings for observability buckets for organization, folder, or project with a default storage location.

To learn more, see [View default settings for observability buckets](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets#view-obs-settings).

### Review organization policies that require CMEKs

There are two constraints that govern CMEKs. One constraint restricts the Cloud KMS keys that can be used for encryption. The other constraint requires the use of Cloud KMS keys.

#### Restrict policy

Determine whether you have configured a policy with the constraint ID `constraints/gcp.restrictCmekCryptoKeyProjects`.

If you have, then make sure that your default Cloud KMS keys are allowed by the organization policy.

#### Require policy

Determine whether you have configured a `Deny` policy with the constraint ID `constraints/gcp.restrictNonCmekServices`.

If so, then make sure that a default Cloud KMS key is defined for the default storage location. If you've also configured a policy to restrict which keys can be used, then make sure that your default Cloud KMS key is allowed.

For example, if your policies apply at the organization level, then make sure that you configured the default settings for observability buckets for your organization with a default storage location and, for that location, a default Cloud KMS key.

Google Cloud Observability can't provision observability buckets when CMEKs are required but a key to encrypt or decrypt that data isn't available.

### Verify a Cloud KMS key is usable

To determine whether a Cloud KMS key is usable, run [`gcloud kms keys list`](https://docs.cloud.google.com/sdk/gcloud/reference/kms/keys/list):
    
    
    gcloud kms keys list \
    --location=LOCATION_ID \
    --keyring=KMS_KEY_RING
    

Before running the previous command, make the following replacements:

  * LOCATION_ID: The location of your Cloud KMS key.
  * KMS_KEY_RING: The Cloud KMS key ring's name.



The previous command returns information about each key in the specified location. For your Cloud KMS key, make sure the following is true:

  * The Cloud KMS key is listed in the table.
  * The `STATUS` column lists `ENABLED`.
  * The `PURPOSE` column lists `ENCRYPT_DECRYPT`. This setting indicates that the purpose of the key is symmetric encryption:



If necessary, [create a new Cloud KMS key](https://docs.cloud.google.com/kms/docs/create-key) and update your default settings for observability buckets for the associated resource and location.

### Verify service account has required role

Verify that the resource's service account has been granted the [Cloud KMS CryptoKey Encrypter/Decrypter](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) role for the Cloud KMS key listed as part of the default settings for observability buckets for the resource.

To determine the bindings for a Cloud KMS key, run the following command:
    
    
    gcloud kms keys get-iam-policy KMS_KEY_NAME
    

If necessary, grant the resource's service account the Cloud KMS CryptoKey Encrypter/Decrypter role for the key. To learn more, see [Grant service account access to a key](https://docs.cloud.google.com/stackdriver/docs/observability/set-defaults-for-observability-buckets#grant-role).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
