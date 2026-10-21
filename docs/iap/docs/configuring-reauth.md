---
url: https://docs.cloud.google.com/iap/docs/configuring-reauth/
title: IAP reauthentication \u00a0|\u00a0 Identity-Aware Proxy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T07:11:51.473243+00:00
---

# IAP reauthentication  |  Identity-Aware Proxy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iap/docs/configuring-reauth/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Identity-Aware Proxy ](https://docs.cloud.google.com/iap/docs)
  * [ Guides ](https://docs.cloud.google.com/iap/docs/quickstarts)



Send feedback 

#  IAP reauthentication Stay organized with collections  Save and categorize content based on your preferences. 

IAP reauthentication lets service and application owners or Google Cloud administrators require authenticated end users to reauthenticate after a specified time when accessing an IAP-protected service or application and limit how long a user can access an IAP-protected service or application before authentication is required.

IAP reauthentication (or, reauth) is designed to enforce reauthentication policies for IAP-protected services and applications (or, apps). Using this service, you can enforce reauthentication policies for critical services and applications that handle confidential information. For example, you can specify that users accessing a critical HR application reauthenticate hourly using a second factor.

## Supported reauthentication methods

You can use the following methods to manage the reauthentication settings:

  * **Login** : End users reauthenticate using their login credentials.
  * **Secure key** : End users reauthenticate using their configured security key.
  * **Enrolled second factors** : End users reauthenticate using one of their enrolled second factors.



For more information, see [IapSettings](https://docs.cloud.google.com/iap/docs/reference/rest/v1/IapSettings).

## Set up a reauthentication policy

The `reauthSettings` are included as part of `IapSettings` and can be set on any resource type in the [resource hierarchy](https://docs.cloud.google.com/iam/docs/overview#resource-hierarchy). You can set `reauthSettings` at the organization, folder, project, or service level to apply restrictions. For example, you can limit the session length to a maximum of one hour for all applications in an organization or to a specific application.

There are two policy types that you can use to set reauthentication:

  * **Minimum** : If the policy type is set to `MINIMUM` on a resource, such as an organization, then, when evaluating the reauthentication settings on the lower-level resource, such as a folder, the two settings are merged. If the lower-level resource has no reauthentication settings, the merge result is the non-empty settings of the higher-level resource. Otherwise, the merge takes the shorter session duration and the higher precedence reauthentication method between the two resources. The resulting merged policy type is set to `MINIMUM`.

  * **Default** : If the policy type is set as `DEFAULT` on a resource, such as organization, then when evaluating the reauthentication setting on the lower-level resource, such as a folder, the lower-level resource setting is used if configured; otherwise, the higher-level resource reauthentication setting is applied.




For both policy types, the evaluation process is repeated to determine the `reauthSettings` for the target service or application. The effective `reauthSettings` at any level are determined as follows:

  * **Inheritance** : The settings from the higher-level resource are merged with the settings of the lower-level resource.

  * **Merge rules** : If the lower-level resource has no specific reauthentication settings, it inherits the settings from the higher level.

If both levels have `reauthSettings`, the merged result uses the following:

    * The shorter session duration.
    * The reauthentication method with the higher precedence.
    * The precedence is `Secure key` (highest), `Enrolled second factors` (medium), and `Login` (lowest).
  * **Resulting policy type** : The policy type of the merged settings is `MINIMUM`.




The following examples show the settings before and after evaluation. During evaluation, the folder and organization `reauthSettings` are merged, resulting in changing the policy type of the folder to `MINIMUM`. The merged settings are then used to merge with the service or application `reauthSettings`.

**Organization`IapSettings`:**
    
    
    accessSettings:
      reauthSettings:
        method: "ENROLLED_SECOND_FACTORS"
        maxAge: "3600s"
        policyType: "MINIMUM"
    

**Folder`IapSettings`:**
    
    
    accessSettings:
      reauthSettings:
        method: "LOGIN"
        maxAge: "1200s"
        policyType: "DEFAULT"
    

**Service or Application`IapSettings`:**
    
    
    accessSettings:
      reauthSettings:
        method: "SECURE_KEY"
        maxAge: "7200s"
        policyType: "DEFAULT"
    

Settings after merge:

**Organization`IapSettings`:**
    
    
    accessSettings:
      reauthSettings:
        method: "ENROLLED_SECOND_FACTORS"
        maxAge: "3600s"
        policyType: "MINIMUM"
    

**Folder`IapSettings`:**
    
    
    accessSettings:
      reauthSettings:
        method: "ENROLLED_SECOND_FACTORS"
        maxAge: "1200s"
        policyType: "MINIMUM"
    

**Service or Application`IapSettings`:**
    
    
    accessSettings:
      reauthSettings:
        method: "SECURE_KEY"
        maxAge: "1200s"
        policyType: "MINIMUM"
    

In this example, if the policy type of every resource is set to `DEFAULT`, then the `reauthSettings` of the service or application is used.

**MaxAge**

Use the `maxAge` parameter to specify how often an end user must reauthenticate, denoted in seconds. For example, to set a one hour reauthentication policy, set seconds to 3600, as shown in the following example:
    
    
    accessSettings:
      reauthSettings:
        method: "LOGIN"
        maxAge: "3600s"
        policyType: "MINIMUM"
    

The minimum value for `maxAge` is 300 seconds, or five minutes.

To set a reauthentication policy, complete the following steps.

###  Console 

  1. Go to the [IAP page](https://console.cloud.google.com/security/iap/).   
[Go to the Identity-Aware Proxy page](https://console.cloud.google.com/security/iap/)
  2. Select a project, and then select the resource that you want to set a reauthentication policy on.

  3. Open the **Settings** for the resource and under **Reauthentication policy** , select **Configure reauthentication**.

  4. Specify the reauthentication settings, and then click **Save**.




###  gcloud 

You can set a reauthentication policy on resources and services at the organization, project, and folder level. The following are some example commands for setting a reauthentication policy.

For more information, see [`gcloud iap settings set`](https://docs.cloud.google.com/sdk/gcloud/reference/iap/settings/set).

Run the following command:
    
    
    gcloud iap settings set SETTING_FILE [--organization=ORGANIZATION --folder=FOLDER --project=/PROJECT --resource-type=RESOURCE_TYPE --service=SERVICE --version=VERSION
    

To set a reauthentication policy on the resources within an organization, run the following command: 
    
    
    gcloud iap settings set SETTING_FILE --organization=ORGANIZATION
    

To set a reauthentication policy on the resources within a folder, run the following command: 
    
    
    gcloud iap settings set SETTING_FILE --folder=FOLDER
    

To set a reauthentication policy on all web type resources within a project, run the following command: 
    
    
    gcloud iap settings set SETTING_FILE --project=PROJECT --resource-type=iap_web
    

To set a reauthentication policy on an App Engine service within a project, run the following command:
    
    
    gcloud iap settings set SETTING_FILE --project=PROJECT --resource-type=app-engine --service=SERVICE
    

Where `SETTING_FILE` is:
    
    
    accessSettings:
      reauthSettings:
        method: "LOGIN"
        maxAge: "3600s"
        policyType: "MINIMUM"
    

Replace the following:

  * FOLDER: The folder ID.
  * ORGANIZATION: The organization ID.
  * PROJECT: The project ID.
  * RESOURCE_TYPE: The IAP resource type. Must be `app-engine`, `iap_web`, `compute`, `organization`, or `folder`.
  * SERVICE: The service name. This is optional when `resource-type` is set to `compute` or `app-engine`.
  * VERSION: The version name. This is not applicable for the `compute` resource type and is optional for the `app-engine` resource type.



###  API 

Run the following command to prepare an `iap_settings.json` file. Update the values as needed.
    
    
    cat << EOF > iap_settings.json
    {
      "access_settings": {
          "reauth_settings": {
                "method": "LOGIN",
                "maxAge": "300s",
                "policy_type": "DEFAULT"
            }
        }
    }
    EOF
    

Get the resource name by running the `gcloud iap settings get` command. Copy the name field from the output. You will need the name in the following step.
    
    
    gcloud iap settings get [--organization=ORGANIZATION --folder=FOLDER --project=/PROJECT --resource-type=RESOURCE_TYPE --service=SERVICE --version=VERSION]
    

Replace `RESOURCE_NAME` in the following command with the name from the previous step. The `IapSettings` will be updated.
    
    
    curl -X PATCH \
    -H "Authorization: Bearer $(gcloud auth print-access-token)" \
    -H "Accept: application/json" \
    -H "Content-Type: application/json" \
    -d @iap_settings.json \
    "https://iap.googleapis.com/v1/RESOURCE_NAME:iapSettings?updateMask=iapSettings.accessSettings.reauthSettings"
    

## Understanding reauthentication credentials

After successful reauthentication, IAP creates a cookie on the end user's browser. To prevent frequent reauthentication for applications on the same domain, the cookie is set on the top-level private domain and is valid for that entire domain.

For example, `foo.example.com` is an IAP protected resource and has an IAP reauthentication policy. After a successful reauthentication, IAP sets a cookie on `example.com` because that is the top-level private domain. Applications from the same top-level private domain, such as `bar.example.com` use the same reauthentication credentials and don't prompt the user to reauthenticate as long as the credentials are valid.

For URLs such as `myapp.appspot.com`, `appspot.com` is a public domain, therefore the top-level private domain is `myapp.appspot.com`.

## Known limitations

  * Reauthentication is only supported for browser flows. Programmatic [user account access](https://docs.cloud.google.com/iap/docs/authentication-howto#authenticating_a_user_account) isn't supported. For example, mobile and desktop applications cannot reauthenticate users because the resources that require reauthentication are inaccessible to these applications.
  * Service accounts and IAP-TCP are exempt from reauthentication requirements.
  * Reauthentication does not work with the Identity and Access Management member type `allUsers`.
  * [External identities](https://docs.cloud.google.com/iap/docs/enable-external-identities), such as OAuth and SAML, are not supported with reauthentication.
  * Workforce Identity Federation identities are not supported for IAP reauthentication.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
