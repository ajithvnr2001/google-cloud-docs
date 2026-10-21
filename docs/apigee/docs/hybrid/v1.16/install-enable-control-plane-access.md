---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-enable-control-plane-access/
title: Step 8: Enable Control Plane access \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:02.270549+00:00
---

# Step 8: Enable Control Plane access  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-enable-control-plane-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 8: Enable Control Plane access Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/install-enable-control-plane-access.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-enable-control-plane-access.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-enable-control-plane-access.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/install-enable-control-plane-access.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/install-enable-control-plane-access.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/install-enable-control-plane-access.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/install-enable-control-plane-access.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/install-enable-control-plane-access.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/install-enable-control-plane-access.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/install-enable-control-plane-access.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/install-enable-control-plane-access.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/install-enable-control-plane-access.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/install-enable-control-plane-access.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/install-enable-control-plane-access.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/install-enable-control-plane-access.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/install-enable-control-plane-access.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/install-enable-control-plane-access.html)



In order for the runtime plane and control plane to communicate, you must enable the required permissions for Synchronizer and analytics publisher access with the [updateControlPlaneAccess API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/updateControlPlaneAccess). 

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

  1. Get the email address for the service account to which you are granting synchronizer access. For production environments, it should be `apigee-synchronizer`. For non-production environments it should be `apigee-non-prod`. Use the following command: 

### Production
         
         gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee-synchronizer"

### Non-production
         
         gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee-non-prod"

  2. Call the [updateControlPlaneAccess](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/updateControlPlaneAccess) API to enable the required permissions for Synchronizer using the following command: 

### No data residency
         
         curl -X PATCH -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type:application/json" \
           "https://apigee.googleapis.com/v1/organizations/${ORG_NAME}/controlPlaneAccess?update_mask=synchronizer_identities" \
           -d "{\"synchronizer_identities\": [\"serviceAccount:apigee-synchronizer@${ORG_NAME}.iam.gserviceaccount.com\"]}"
         

Where: 

     * **`${ORG_NAME}`** : The name of your hybrid organization.
     * **`apigee-synchronizer@${ORG_NAME}.iam.gserviceaccount.com`** : The email address of the service account.

### Data residency
    
    curl -X PATCH -H "Authorization: Bearer $TOKEN" \
      -H "Content-Type:application/json" \
      "https://$CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/${ORG_NAME}/controlPlaneAccess?update_mask=synchronizer_identities" \
      -d "{\"synchronizer_identities\": [\"serviceAccount:apigee-synchronizer@${ORG_NAME}.iam.gserviceaccount.com\"]}"
    

Where: 

     * **`CONTROL_PLANE_LOCATION`** : The location for your control plane data if your hybrid installation uses [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts). This is location where customer core content like proxy bundles are stored. For a list see [Available Apigee API control plane regions](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions).
     * **`${ORG_NAME}`** : The name of your hybrid organization.
     * **`apigee-synchronizer@${ORG_NAME}.iam.gserviceaccount.com`** : The email address of the service account.
  3. To verify that the service account was set, use the following command to call the API to get a list of service accounts: 

### No data residency
         
         curl -X GET -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type:application/json" \
           "https://apigee.googleapis.com/v1/organizations/${ORG_NAME}/controlPlaneAccess"
             

### Data residency
         
         curl -X GET -H "Authorization: Bearer $TOKEN" \
           -H "Content-Type:application/json" \
           "https://CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/${ORG_NAME}/controlPlaneAccess"
             

The output should look similar to the following: 
         
         {
           "synchronizerIdentities": [
             "serviceAccount:apigee-synchronizeriam.gserviceaccount.com@YOUR_ORG_NAME."
           ]
         }

**Note:** The call to the Apigee API uses ${ORG_NAME}, and the results from the IAM service account mappings use PROJECT_ID. In most cases, the values are the same. One uncommon exception is when using a [multi-org cluster](https://docs.cloud.google.com/apigee/docs/hybrid/latest/multi-org), where there would be more than one org name, and the service accounts could be different per org. 



##  Enable analytics publisher access 

Several Apigee hybrid runtime components publish analytics and debug records to provide information for reporting and debugging. To enable publishing this data, you need to grant additional permissions to the service accounts that run these apigee components to publish data directly to the control plane. 

To enable analytics publisher access: 

  1. Get the email address for the service accounts to which you are granting analytics publisher access. For production environments, they should be `apigee-runtime`, `apigee-mart`, and `apigee-mint-task-scheduler` (if you are enabling [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid)). For non-production environments it should be `apigee-non-prod`. 

### Production
         
         gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee-runtime OR apigee-mart OR apigee-mint-task-scheduler"

### Non-production
         
         gcloud iam service-accounts list --project ${PROJECT_ID} --filter "apigee-non-prod"

  2. Set permissions for the service accounts for the runtime, MART, and mint task scheduler (if you are enabling [Monetization for Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/monetization-for-hybrid) on [v1.15.1](https://docs.cloud.google.com/apigee/docs/hybrid/release-notes#hybrid_v1151) and later) components to publish data to the control plane with the following command: 

### No data residency

Call the `updateControlPlaneAccess` API to enable permissions for the runtime and MART service accounts:
         
         curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type:application/json" \
           "https://apigee.googleapis.com/v1/organizations/$ORG_NAME/controlPlaneAccess?update_mask=analytics_publisher_identities" \
           -d "{\"analytics_publisher_identities\": [\"serviceAccount:apigee-mart@$ORG_NAME.iam.gserviceaccount.com\",\"serviceAccount:apigee-runtime@$ORG_NAME.iam.gserviceaccount.com\"]}"
         

If you are enabling Monetization for Apigee hybrid, set the permissions for the mint task scheduler service account:
         
         curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
           -H "Content-Type:application/json" \
           "https://apigee.googleapis.com/v1/organizations/$ORG_NAME/controlPlaneAccess?update_mask=analytics_publisher_identities" \
           -d "{\"analytics_publisher_identities\": [\"serviceAccount:apigee-mart@$ORG_NAME.iam.gserviceaccount.com\",\"serviceAccount:apigee-runtime@$ORG_NAME.iam.gserviceaccount.com\",\"serviceAccount:apigee-mint-task-scheduler@$ORG_NAME.iam.gserviceaccount.com\"]}"
         

Where the following are the email addresses of the service accounts:

     * `apigee-mart@${ORG_NAME}.iam.gserviceaccount.com`
     * `apigee-mint-task-scheduler@${ORG_NAME}.iam.gserviceaccount.com`
     * `apigee-runtime@${ORG_NAME}.iam.gserviceaccount.com`

### Data residency

Call the `updateControlPlaneAccess` API to enable permissions for the runtime and MART service accounts:
    
    curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type:application/json" \
      "https://$CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/$ORG_NAME/controlPlaneAccess?update_mask=analytics_publisher_identities" \
      -d "{\"analytics_publisher_identities\": [\"serviceAccount:apigee-mart@$ORG_NAME.iam.gserviceaccount.com\",\"serviceAccount:apigee-runtime@$ORG_NAME.iam.gserviceaccount.com\"]}"
    

If you are enabling Monetization for Apigee hybrid, set the permissions for the mint task scheduler service account:
    
    curl -X PATCH -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type:application/json" \
      "https://$CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/$ORG_NAME/controlPlaneAccess?update_mask=analytics_publisher_identities" \
      -d "{\"analytics_publisher_identities\": [\"serviceAccount:apigee-mart@$ORG_NAME.iam.gserviceaccount.com\",\"serviceAccount:apigee-runtime@$ORG_NAME.iam.gserviceaccount.com\",\"serviceAccount:apigee-mint-task-scheduler@$ORG_NAME.iam.gserviceaccount.com\"]}"
    

Where: 

     * **`CONTROL_PLANE_LOCATION`** is the location for your control plane data if your hybrid installation uses [data residency](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts). This is location where customer core content like proxy bundles are stored. For a list see [Available Apigee API control plane regions](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions).
     * The following are the email addresses of the service accounts: 
       * `apigee-mart@${ORG_NAME}.iam.gserviceaccount.com`
       * `apigee-mint-task-scheduler@${ORG_NAME}.iam.gserviceaccount.com`
       * `apigee-runtime@${ORG_NAME}.iam.gserviceaccount.com`

The response should look similar to the following:
    
    {
      "name": "organizations/YOUR_ORG_NAME/operations/8316aa78-c137-4733-92ec-cc0d2d92fd29",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
        "operationType": "UPDATE",
        "targetResourceName": "organizations/YOUR_ORG_NAME/controlPlaneAccess",
        "state": "IN_PROGRESS"
      }
    }
    

  3. Verify state of the operation using the identifier in the **name** field of the update response: 

### No data residency
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
           -H "Content-Type:application/json"  \
           "https://apigee.googleapis.com/v1/organizations/$ORG_NAME/operations/$OPERATION_ID"

### Data residency
         
         curl -X GET -H "Authorization: Bearer $(gcloud auth print-access-token)"  \
           -H "Content-Type:application/json"  \
           "https://CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/$ORG_NAME/operations/$OPERATION_ID"

The response should look like the following:
         
         {
           "name": "organizations/YOUR_ORG_NAME/operations/$OPERATION_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
             "operationType": "UPDATE",
             "targetResourceName": "organizations/YOUR_ORG_NAME/controlPlaneAccess",
             "state": "FINISHED"
           },
           "done": true,
           "response": {
             "@type": "type.googleapis.com/google.cloud.apigee.v1.ControlPlaneAccess",
             "name": "organizations/YOUR_ORG_NAME/controlPlaneAccess"
           }
         }
         

  4. Verify the organization's ControlPlaneAccess configuration: 

### No data residency
         
         curl "https://apigee.googleapis.com/v1/organizations/$ORG_NAME/controlPlaneAccess" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)"

### Data residency
         
         curl "https://CONTROL_PLANE_LOCATION-apigee.googleapis.com/v1/organizations/$ORG_NAME/controlPlaneAccess" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)"

The response should look like the following:
         
         {
           "synchronizerIdentities": [
             "serviceAccount:apigee-synchronizer@YOUR_ORG_NAME.iam.gserviceaccount.com"
           ],
           "analyticsPublisherIdentities": [
             "serviceAccount:apigee-mart@YOUR_ORG_NAME.iam.gserviceaccount.com",
             "serviceAccount:apigee-mint-task-scheduler@YOUR_ORG_NAME.iam.gserviceaccount.com",
             "serviceAccount:apigee-runtime@YOUR_ORG_NAME.iam.gserviceaccount.com"
           ]
         }
         




You have now enabled your Apigee hybrid runtime and management planes to communicate. Next, install cert-manager to enable Apigee hybrid to interpret and manage certificates.

## Next step

[1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-cluster) [2](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-download-charts) [3](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-namespace) [4](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-service-accounts) [5](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-sa-authentication) [6](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-tls-certificates) [7](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-create-overrides) [8](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-enable-control-plane-access) [(NEXT) Step 9: Install cert-manager](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-cert-manager) [10](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-crds) [11](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/install-helm-charts)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
