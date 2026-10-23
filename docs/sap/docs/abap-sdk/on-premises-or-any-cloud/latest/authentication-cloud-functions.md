---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-cloud-functions/
title: Authenticate with ID tokens for Cloud Run functions \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:02:12.614988+00:00
---

# Authenticate with ID tokens for Cloud Run functions  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-cloud-functions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Authenticate with ID tokens for Cloud Run functions Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/authentication-cloud-functions)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-cloud-functions)



As a developer, you can write [Cloud Run functions](https://docs.cloud.google.com/functions/docs/concepts/overview), which provide HTTP endpoints. You invoke Cloud Run functions from the ABAP SDK class `/GOOG/CL_CLOUDFUNC_INVOKER` using their HTTP endpoints.

The process involves calling a Cloud Run function using its name and location to obtain the HTTP endpoint of the function. This endpoint is then used to invoke the function. Authentication to Cloud Run functions requires an ID token to invoke the HTTP endpoint.

The high-level configuration steps are as follows:

  * In Google Cloud, enable the Google Cloud APIs.
  * Create a service account and grant roles to get the Cloud Run function details.
  * Create another service account and grant roles to invoke Cloud Run functions.
  * Set up authentication to Cloud Run functions.
  * Configure client key to invoke Cloud Run functions.



## Enable the Google Cloud APIs

In the Google Cloud console, enable the following Google Cloud APIs:

  * [IAM Service Account Credentials API](https://console.cloud.google.com/project/_/apis/library/iamcredentials.googleapis.com)
  * [Cloud Functions API](https://console.cloud.google.com/project/_/apis/library/cloudfunctions.googleapis.com)



For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/docs/getting-started#enabling_apis).

## Create a service account to get Cloud Run function details

  1. In the Google Cloud console, create an IAM service account to get your Cloud Run function details.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

For information about how to create a service account, see [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating).

  2. Grant the following roles to the service account:

     * [`Service Account Token Creator`](https://docs.cloud.google.com/compute/docs/access/iam#iam.serviceAccountTokenCreator)
     * [`Cloud Functions Viewer`](https://docs.cloud.google.com/functions/docs/reference/iam/roles#cloudfunctions.viewer)

For instructions, see [Grant a single role](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#grant-single-role).




## Create another service account to invoke Cloud Run functions

  1. In the Google Cloud console, create a dedicated service account to invoke Cloud Run functions.

[Go to Service accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

For information about how to create a service account, see [Create a service account](https://docs.cloud.google.com/iam/docs/service-accounts-create#creating).

  2. Depending on the generation of Cloud Run functions that you're invoking, grant the appropriate roles to the service account:

     * For 1st gen functions: Grant the [`Cloud Functions Invoker`](https://docs.cloud.google.com/functions/docs/reference/iam/roles#cloudfunctions.invoker) role to the service account.
     * For 2nd gen functions: Grant the [`Cloud Run Invoker`](https://docs.cloud.google.com/run/docs/reference/iam/roles#run.invoker) role to the service account.

For more information about the permissions to invoke a function, see [Authenticate for invocation](https://docs.cloud.google.com/functions/docs/securing/authenticating).




## Set up authentication to Cloud Run functions

Depending on the environment where your SAP system is hosted, you can use one of the following methods to set up token-based authentication to access the Cloud Run functions API:

  * SAP system hosted on Compute Engine VM
  * SAP RISE or SAP system hosted outside Google Cloud



### SAP system hosted on Compute Engine VM

For instructions to set up authentication to access the Cloud Run functions API when your SAP system is hosted on a Compute Engine VM instance, see [Authenticate by using access tokens](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-access-token). Configure a client key with the service account that you created to get the Cloud Run function details.

### SAP RISE or SAP system hosted outside Google Cloud

Set up authentication to access Cloud Run functions APIs using one of the following authentication methods:

  * [Authenticate by using JSON Web Tokens (JWT)](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-jwt)
  * [Authenticate by using tokens through Workload Identity Federation](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-wif)



Configure a client key with the service account that you created to get the Cloud Run function details.

## Configure client key to invoke Cloud Run functions

Depending on the environment where your SAP system is hosted, you use different values for the client key configuration:

  * SAP system hosted on Compute Engine VM
  * SAP RISE or SAP system hosted outside Google Cloud



### SAP system hosted on Compute Engine VM

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Configure Client Key**.

  3. Click **New Entries**.

  4. Enter values for the following fields:

Field | Description  
---|---  
**Google Cloud Key Name** | Specify a name of the client key configuration.  
**Google Cloud Service Account Name** |  Specify the name of the service account to which you have granted permissions to invoke Cloud Run functions. For example: `sap-example-svc-acct@example-project-123456.iam.gserviceaccount.com`.   
**Google Cloud Scope** | Specify the access scope, `https://www.googleapis.com/auth/cloud-platform`.   
**Project ID** | Specify the ID of the Google Cloud project that has the Cloud Run functions API enabled.  
**Command name** | Leave this field blank.  
**Authorization Class** | Specify the authorization class, `/GOOG/CL_AUTH_ID_TOKEN`.   
**Authorization Field** | Leave this field blank.  
**Token Caching** | Leave this field blank.  
**Token Refresh Seconds** | Leave this field blank.  
**Authorization Parameter 1** | Leave this field blank.  
**Authorization Parameter 2** | Leave this field blank.  
  5. Save the new entry.




### SAP RISE or SAP system hosted outside Google Cloud

  1. In SAP GUI, execute the transaction code `/GOOG/SDK_IMG`.

Alternatively, execute the transaction code `SPRO`, and then click **SAP Reference IMG**.

  2. Click **ABAP SDK for Google Cloud > Basic Settings > Configure Client Key**.

  3. Click **New Entries**.

  4. Enter values for the following fields:

Field | Description  
---|---  
**Google Cloud Key Name** | Specify a name of the client key configuration.  
**Google Cloud Service Account Name** |  Specify the name of the service account to which you have granted permissions to invoke Cloud Run functions. For example: `sap-example-svc-acct@example-project-123456.iam.gserviceaccount.com`.   
**Google Cloud Scope** | Specify the access scope, `https://www.googleapis.com/auth/cloud-platform`.   
**Project ID** | Specify the ID of the Google Cloud project that has the Cloud Run functions API enabled.  
**Command name** | Leave this field blank.  
**Authorization Class** | Specify the authorization class as follows: 
     * For authentication by using JWT, specify `/GOOG/CL_AUTH_JWT_ID_TOKEN`.
     * For authentication by using Workload Identity Federation, specify the child class, which contains the implementation of class `/GOOG/CL_AUTH_WIF_ID_TOKEN`. For more information, see [Implement ABAP code to retrieve security tokens from your IdP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-wif#implement_abap_code_to_retrieve_token).  
**Authorization Field** | Leave this field blank.  
**Token Caching** | Leave this field blank.  
**Token Refresh Seconds** | Leave this field blank.  
**Authorization Parameter 1** | 
     * For authentication by using JWT, if you're using a custom name for the SSF application, then specify the name of the SSF application that you created in the section [Create a new Secure Store and Forward (SSF) Application](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication-jwt#jwt-create-ssf-application).
     * For authentication by using Workload Identity Federation, specify the workload identity pool ID.  
**Authorization Parameter 2** | 
     * For authentication by using JWT, leave this field blank.
     * For authentication by using Workload Identity Federation, specify the workload identity provider ID.  
  5. Save the new entry.




## Get support

If you need help resolving problems with the on-premises or any cloud edition of ABAP SDK for Google Cloud, then do the following:

  * Refer to the [ on-premises or any cloud edition of ABAP SDK for Google Cloud troubleshooting guide](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/troubleshooting).

  * Ask your questions and discuss ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).

  * Collect all available [diagnostic information](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/getting-support-diag-info) and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
