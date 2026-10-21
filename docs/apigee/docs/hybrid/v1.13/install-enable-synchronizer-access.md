---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-enable-synchronizer-access/
title: Step 7: Enable Synchronizer access \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T11:57:20.721579+00:00
---

# Step 7: Enable Synchronizer access  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-enable-synchronizer-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 7: Enable Synchronizer access Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.13 of the Apigee hybrid documentation. **This version is end of life.** You should upgrade to a newer version. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.13 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-enable-synchronizer-access.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-enable-synchronizer-access.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-enable-synchronizer-access.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-enable-synchronizer-access.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-enable-synchronizer-access.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-enable-synchronizer-access.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-enable-synchronizer-access.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-enable-synchronizer-access.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-enable-synchronizer-access.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-enable-synchronizer-access.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-enable-synchronizer-access.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-enable-synchronizer-access.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-enable-synchronizer-access.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-enable-synchronizer-access.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-enable-synchronizer-access.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-enable-synchronizer-access.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-enable-synchronizer-access.html)



##  Get an authorization token 

To make the Apigee API calls described later in this topic, you need to get an authorization token that has the Apigee Organization Admin role. 

  1. If you are not the owner of the Google Cloud project that is associated with your Apigee hybrid organization, be sure that your Google Cloud user account has the **roles/apigee.admin** (Apigee Organization Admin) role. You can check the roles assigned to you with this command: 
         
         gcloud projects get-iam-policy ${PROJECT_ID}  \
           --flatten="bindings[].members" \
           --format='table(bindings.role)' \
           --filter="bindings.members:your_account_email"
         

For example: 
         
         gcloud projects get-iam-policy my-project  \
           --flatten="bindings[].members" \
           --format='table(bindings.role)' \
           --filter="bindings.members:myusername@example.com"

The output should include `roles/apigee.admin`. 

  2. If you do not have `roles/apigee.admin`, add the **Apigee Organization Admin** role to your user account. Use the following command to add the role to your user account: 
         
         gcloud projects add-iam-policy-binding ${PROJECT_ID} \
           --member user:your_account_email \
           --role roles/apigee.admin

For example: 
         
         gcloud projects add-iam-policy-binding my-project \
           --member user:myusername@example.com \
           --role roles/apigee.admin

  3. On the command line, get your `gcloud` authentication credentials using the following command:

###  Linux / MacOS 
         
         export TOKEN=$(gcloud auth print-access-token)

To check that your token was populated, use `echo`, as the following example shows:
         
         echo $TOKEN

This should display your token as an encoded string.

###  Windows 
         
         for /f "tokens=*" %a in ('gcloud auth print-access-token') do set TOKEN=%a

To check that your token was populated, use `echo`, as the following example shows:
         
         echo %TOKEN%

This should display your token as an encoded string.




##  Enable synchronizer access 

To enable synchronizer access: 

  1. Get the email address for the service account to which you are granting synchronizer access. For non-production environments (as suggested in this tutorial) it should be `apigee-non-prod`. For production environments, it should be `apigee-synchronizer`. Use the following command: 
         
         gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee-synchronizer"

  2. Call the [setSyncAuthorization](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/setSyncAuthorization) API to enable the required permissions for Synchronizer using the following command: 

### No data residency
         
         curl -X POST -H "Authorization: Bearer ${TOKEN}" \
           -H "Content-Type:application/json" \
           "https://apigee.googleapis.com/v1/organizations/${ORG_NAME}:setSyncAuthorization" \
            -d "{\"identities\":[\"serviceAccount:apigee-synchronizer@${ORG_NAME}.iam.gserviceaccount.com\"]}"
         

Where: 

     * **`${ORG_NAME}`** : The name of your hybrid organization.
     * **`apigee-synchronizer ${ORG_NAME}.iam.gserviceaccount.com`**: The email address of the service account.

### Data residency
    
    curl -X POST -H "Authorization: Bearer ${TOKEN}" \
      -H "Content-Type:application/json" \
      "https://$CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/${ORG_NAME}:setSyncAuthorization" \
       -d "{\"identities\":[\"serviceAccount:apigee-synchronizer@${ORG_NAME}.iam.gserviceaccount.com\"]}"
    

Where: 

     * **`CONTROL_PLANE_LOCATION`** : The location for your control plane data if your hybrid installation uses [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts). This is location where customer core content like proxy bundles are stored. For a list see [Available Apigee API control plane regions](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions).
     * **`${ORG_NAME}`** : The name of your hybrid organization.
     * **`apigee-synchronizer ${ORG_NAME}.iam.gserviceaccount.com`**: The email address of the service account.
  3. To verify that the service account was set, use the following command to call the API to get a list of service accounts: 

### No data residency
         
         curl -X GET -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type:application/json" \
           "https://apigee.googleapis.com/v1/organizations/${ORG_NAME}:getSyncAuthorization"
             

### Data residency
         
         curl -X GET -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type:application/json" \
           "https://CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/${ORG_NAME}:getSyncAuthorization"
             

The output looks similar to the following: 
         
         {
            "identities":[
               "serviceAccount:apigee-synchronizer@my_project_id.iam.gserviceaccount.com"
            ],
            "etag":"BwWJgyS8I4w="
         }

**Note:** The call to the Apigee API uses ${ORG_NAME}, and the results from the IAM service account mappings use my_project_id. In most cases, the values are the same. One uncommon exception is when using a [multi-org cluster](https://docs.cloud.google.com/apigee/docs/hybrid/latest/multi-org), where there would be more than one org name, and the service accounts could be different per org. 



You have now enabled your Apigee hybrid runtime and management planes to communicate. Next, install cert-manager to enable Apigee hybrid to interpret and manage certificates.

## Next step

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-download-charts) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-create-namespace) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-service-accounts) [5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-create-tls-certificates) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-create-overrides) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-enable-synchronizer-access) [(NEXT) Step 8: Install cert-manager](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-cert-manager) [9](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-crds) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-helm-charts) [11](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-workload-identity)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
