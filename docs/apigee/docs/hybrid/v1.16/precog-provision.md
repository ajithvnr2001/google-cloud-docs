---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision/
title: Step 2: Create an organization \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:47:27.733227+00:00
---

# Step 2: Create an organization  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Step 2: Create an organization Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.16 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.16 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/precog-provision.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-provision.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/precog-provision.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/precog-provision.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/precog-provision.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/precog-provision.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/precog-provision.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/precog-provision.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/precog-provision.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/precog-provision.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/precog-provision.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/precog-provision.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/precog-provision.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/precog-provision.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/precog-provision.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/precog-provision.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/precog-provision.html)



In this step, you create an [Apigee organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/basic-concepts).

**Note:** An Apigee organization is the top-level container in Apigee. The Apigee organization contains all your API proxies and related resources. Apigee organizations are not the same as Google Cloud organizations. 

  * For an overview of Apigee organizations, see [Organization structure](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/organization-structure).
  * For information about Google Cloud organizations, see [Organizations](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations).



### About organization creation

When provisioning an organization, note the following:

  * You cannot provision Apigee hybrid in an existing Apigee organization. You must create a new organization and the organization name must match the Google Cloud project ID.
  * An organization is bound to a single Google Cloud project.



**To create a new organization and provision it:**

**Note:** If you have an Apigee evaluation account, the organization you create will expire after 60 days. At that time, the organization will be deleted. 

If this occurs, you may encounter the following error: `"Project <my-project> doesn't have an Apigee organization provisioned."` To resolve this error, follow the steps to create a new organization and provision it.

  1. On the command line, get your `gcloud` authentication credentials using the following command:

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

  2. In [Step 1](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-enableapi), you created the `PROJECT_ID` environment variable. Add the following environment variables. Select the tab that corresponds to the type of organization you need: **No data residency** or with [ **Data residency**](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts): 

### No data residency

###  Linux / MacOS 
         
         export ORG_NAME=$PROJECT_ID
         export ANALYTICS_REGION="ANALYTICS_REGION"
         export RUNTIMETYPE=**HYBRID**

###  Windows 
         
         set ORG_NAME=$PROJECT_ID
         set ANALYTICS_REGION="ANALYTICS_REGION"
         set RUNTIMETYPE=**HYBRID**

**Tip:** Use the `echo %variable-name%` command to verify that the environment variables are properly set. 

Where: 

     * **`ORG_NAME`** **(Required)** : This value must match the `PROJECT_ID`. 
     * **`ANALYTICS_REGION`** **(Required)** : The primary region for analytics data storage. For a list of available Apigee API Analytics regions, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations). 
     * **`RUNTIMETYPE`** **(Required)** : Must be set to `HYBRID`. 

### Data residency

###  Linux / MacOS 
    
    export ORG_NAME=$PROJECT_ID
    export RUNTIMETYPE=**HYBRID**
    export CONTROL_PLANE_LOCATION="YOUR_CONTROL_PLANE_LOCATION"
    export CONSUMER_DATA_REGION="YOUR_CONSUMER_DATA_REGION"
    export BILLING_TYPE="**SUBSCRIPTION** "

###  Windows 
    
    set ORG_NAME=$PROJECT_ID
    set RUNTIMETYPE=**HYBRID**
    set CONTROL_PLANE_LOCATION="YOUR_CONTROL_PLANE_LOCATION"
    set CONSUMER_DATA_REGION="YOUR_CONSUMER_DATA_REGION"
    set BILLING_TYPE="**SUBSCRIPTION** "

**Tip:** Use the `echo %variable-name%` command to verify that the environment variables are properly set. 

Where: 

     * **`ORG_NAME`** : This value must match the `PROJECT_ID`. 
     * **`RUNTIMETYPE`** : Must be set to `HYBRID`. 
     * **`CONTROL_PLANE_LOCATION`** : The location where customer core content like proxy bundles is stored. For a list see [Available Apigee API control plane regions](https://docs.cloud.google.com/apigee/docs/locations#available-apigee-api-control-plane-regions). 
     * **`CONSUMER_DATA_REGION`** : A sub-region of the control plane region. You must specify both the `CONTROL_PLANE_LOCATION` and the `CONSUMER_DATA_REGION`. For a list of available consumer data regions, see [ Apigee locations](https://docs.cloud.google.com/apigee/docs/locations#consumer-data-region). 
     * **`BILLING_TYPE`** : Must be set to `"SUBSCRIPTION"`. This is the billing type for your Apigee hybrid organization. See [Subscription entitlements](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements) for more information. 

For example:
    
    export ORG_NAME=$PROJECT_ID
    export RUNTIMETYPE=HYBRID
    export CONSUMER_DATA_REGION="us-west1"
    export CONTROL_PLANE_LOCATION="us"
    export BILLING_TYPE="SUBSCRIPTION"
    

  3. Call the following Apigee API to create the organization: 

### No data residency
         
         curl -H "Authorization: Bearer **$TOKEN** " -X POST -H "content-type:application/json" \
           -d '{
             "name":"'"**$ORG_NAME** "'",
             "runtimeType":"'"**$RUNTIMETYPE** "'",
             "analyticsRegion":"'"**$ANALYTICS_REGION** "'"
           }' \
           "https://apigee.googleapis.com/v1/organizations?parent=projects/**$PROJECT_ID** "

### Data residency
         
         curl -H "Authorization: Bearer **$TOKEN** " -X POST -H "content-type:application/json" \
           -d '{
             "name":"'"**$ORG_NAME** "'",
             "billingType":"'"**$BILLING_TYPE** "'",
             "runtimeType":"'"**$RUNTIMETYPE** "'",
             "apiConsumerDataLocation":"'"**$CONSUMER_DATA_REGION** "'"
           }' \
           "https://**$CONTROL_PLANE_LOCATION** -apigee.googleapis.com/v1/organizations?parent=projects/**$PROJECT_ID** "

**Tip:** The quotation mark structure (`"'"`) in the previous code sample is needed to pass the values of the environment variables within the JSON body.

On a successful creation request, the organizations API responds with a message similar to the following:
         
         {
           "name": "organizations/org_name/operations/LONG_RUNNING_OPERATION_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
             "operationType": "INSERT",
             "targetResourceName": "organizations/org_name",
             "state": "IN_PROGRESS"
           }
         }

Where:

     * LONG_RUNNING_OPERATION_ID is the UUID of an asynchronous, long-running operation. You can use this ID to check the status of your organization creation request (described in step 5).
     * org_name is the ID of your new organization that is currently being created.

As the `state` property in the response indicates, Apigee has started to create the new organization, so its state is `IN_PROGRESS`. This process can take several minutes.

If you get an error, see Troubleshooting organization creation.

  4. Save the long-running operation ID to an environment variable. It will be useful for future management tasks. 

### Syntax
         
         export LONG_RUNNING_OPERATION_ID=LONG_RUNNING_OPERATION_ID

### Example
         
         export LONG_RUNNING_OPERATION_ID=6abc8a72-46de-f9da-bcfe-70d9ab347e4f

  5. You can check the status of the long-running operation whose ID was returned by the creation request. To do this, use the operations API. For example: 

### No data residency
         
         curl -H "Authorization: Bearer **$TOKEN"** \
           "https://apigee.googleapis.com/v1/organizations/**$ORG_NAME** /operations/**$LONG_RUNNING_OPERATION_ID** "

The following examples show possible responses to this request:

### IN_PROGRESS

If Apigee is still creating the organization, Apigee responds with a status of `IN_PROGRESS`. For example:
         
         {
           "name": "organizations/ORG_NAME/operations/LONG_RUNNING_OPERATION_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
             "operationType": "INSERT",
             "targetResourceName": "organizations/ORG_NAME",
             "state": "IN_PROGRESS"
           }
         }

You should wait a little longer before attempting to verify that the creation process is complete.

### FINISHED

When the organization has been provisioned, the state of the long-running operation is `FINISHED`. For example:
         
         {
           "name": "organizations/ORG_NAME/operations/LONG_RUNNING_OPERATION_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
             "operationType": "INSERT",
             "targetResourceName": "organizations/ORG_NAME",
             "state": "FINISHED"
           },
           "done": true,
           "response": {
             "@type": "type.googleapis.com/google.cloud.apigee.v1.Organization",
             "name": "ORG_NAME",
             "description": "",
             "createdAt": "1626237148461",
             "lastModifiedAt": "1626237149384",
             "properties": {
               "property": [
                 {
                   "name": "features.hybrid.enabled",
                   "value": "true"
                 },
                 {
                   "name": "features.mart.connect.enabled",
                   "value": "true"
                 }
               ]
             },
             "analyticsRegion": "ANALYTICS_REGION",
             "runtimeType": "HYBRID",
             "subscriptionType": "TRIAL",
             "state": "ACTIVE",
             "billingType": "EVALUATION",
             "expiresAt": "1631421073171",
             "addonsConfig": {
               "advancedApiOpsConfig": {},
               "integrationConfig": {},
               "monetizationConfig": {}
             }
           }
         }

### Data residency
         
         curl -H "Authorization: Bearer **$TOKEN** " \
           "https://**$CONTROL_PLANE_LOCATION** -apigee.googleapis.com/v1/organizations/**$ORG_NAME** /operations/**$LONG_RUNNING_OPERATION_ID** "

The following examples show possible responses to this request:

### IN_PROGRESS

If Apigee is still creating the organization, Apigee responds with a status of `IN_PROGRESS`. For example:
         
         {
           "name": "organizations/ORG_NAME/operations/LONG_RUNNING_OPERATION_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
             "operationType": "INSERT",
             "targetResourceName": "organizations/ORG_NAME",
             "state": "IN_PROGRESS",
             "progress": {
               "percentDone": 30
             }
           }
         }

You should wait a little longer before attempting to verify that the creation process is complete.

### FINISHED

When the organization has been provisioned, the state of the long-running operation is `FINISHED`. For example:
         
         {
           "name": "organizations/ORG_NAME/operations/LONG_RUNNING_OPERATION_ID",
           "metadata": {
             "@type": "type.googleapis.com/google.cloud.apigee.v1.OperationMetadata",
             "operationType": "INSERT",
             "targetResourceName": "organizations/ORG_NAME",
             "state": "FINISHED"
           },
           "done": true,
           "response": {
             "@type": "type.googleapis.com/google.cloud.apigee.v1.Organization",
             "name": "ORG_NAME",
             "description": "",
             "createdAt": "1626237148461",
             "lastModifiedAt": "1626237149384",
             "properties": {
               "property": [
                 {
                   "name": "features.hybrid.enabled",
                   "value": "true"
                 },
                 {
                   "name": "features.mart.connect.enabled",
                   "value": "true"
                 }
               ]
             },
             "analyticsRegion": "ANALYTICS_REGION",
             "runtimeType": "HYBRID",
             "subscriptionType": "TRIAL",
             "state": "ACTIVE",
             "billingType": "SUBSCRIPTION",
             "apiConsumerDataLocation": "CONSUMER_DATA_REGION",
             "expiresAt": "1631421073171",
             "addonsConfig": {
               "advancedApiOpsConfig": {},
               "integrationConfig": {},
               "monetizationConfig": {}
             }
           }
         }

  6. You can use the Apigee organizations API to retrieve information about an organization after it is created. 

For example:

### No data residency
         
         curl -H "Authorization: Bearer **$TOKEN** " \
           "https://apigee.googleapis.com/v1/organizations/**$ORG_NAME** "

The response to your request contains details about the specified organization in JSON format.
         
         {
           "name": "apigee-example",
           "createdAt": "1626237148461",
           "lastModifiedAt": "1626237149384",
           "properties": {
             "property": [
               {
                 "name": "features.hybrid.enabled",
                 "value": "true"
               },
               {
                 "name": "features.mart.connect.enabled",
                 "value": "true"
               }
             ]
           },
           "analyticsRegion": "us-west1",
           "runtimeType": "HYBRID",
           "subscriptionType": "PAID",
           "projectId": "my-project",
           "state": "ACTIVE",
           "billingType": "SUBSCRIPTION",
           "expiresAt": "1631421073171",
           "addonsConfig": {
             "advancedApiOpsConfig": {},
             "integrationConfig": {},
             "monetizationConfig": {}
           }
         }

### Data residency
         
         curl -H "Authorization: Bearer **$TOKEN** " \
           "https://**$CONTROL_PLANE_LOCATION** -apigee.googleapis.com/v1/organizations/**$ORG_NAME** "

The response to your request contains details about the specified organization in JSON format.
         
         {
           "name": "apigee-example",
           "createdAt": "1626237148461",
           "lastModifiedAt": "1626237149384",
           "properties": {
             "property": [
               {
                 "name": "features.hybrid.enabled",
                 "value": "true"
               },
               {
                 "name": "features.mart.connect.enabled",
                 "value": "true"
               }
             ]
           },
           "analyticsRegion": "us-west1",
           "runtimeType": "HYBRID",
           "subscriptionType": "PAID",
           "projectId": "my-project",
           "state": "ACTIVE",
           "billingType": "SUBSCRIPTION",
           "expiresAt": "1631421073171",
           "addonsConfig": {
             "advancedApiOpsConfig": {},
             "integrationConfig": {},
             "monetizationConfig": {}
           }
         }




## Troubleshooting organization creation

When you create an organization with the [Create organizations API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations/create), you might get an error response. Responses look like the following:
    
    
    {
      "error": {
        "code": HTTP_error_code,
        "message": "short_error_message",
        "status": "high_level_error_type",
        "details": [
          {
            "@type": "specific_error_type",
            "detail": "expanded_error_description"
          }
        ]
      }
    }

The following table lists errors you might receive and potential resolutions when you try to create a new organization:

HTTP Error Code | HTTP Error | Description  
---|---|---  
`400` | `Invalid JSON payload received` | Either the structure of the data in your request contains a syntax error or the path to the endpoint is incorrect.  
`400` | `Invalid organization ID` | The organization ID that you request cannot contain uppercase letters or any special characters other than hyphens. It must contain only lowercase letters, numbers, and/or hyphens. It can be up to a maximum of 32 characters long.  
`400` | `Unsupported analytics region` | You either did not specify the value of the `analyticsRegion` in your request body, or the value you specified is not one of the valid options.  
`400` | `Does not have an Apigee entitlement` | Your Google Cloud project has not yet been hybrid enabled. This could indicate an issue with your billing or some other error related to your Google Cloud account. For more information, contact [Apigee Sales](https://pages.apigee.com/contact-sales-reg.html).  
`400` | `'global' violates constraint in constraints/gcp.resourceLocations on the resource projects/PROJECT_ID, Control Plane Region` | You tried to create an org that may not be entitled with PAID subscription. Apigee Hybrid orgs of type EVAL do not support [ Data Residency.](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/drz-concepts)  
`400` | `runtimeType HYBRID is not supported for PAYG_V2, use CLOUD instead: invalid argument` | You tried to create an organization on a project with a "Pay As You Go" (PAYG) entitlement. Reach out to your Google Cloud account representative for questions about organization entitlement.   
`401` | `Request had invalid authentication credentials` | Your `gcloud` authentication token is either bad or outdated, or you did not include one in the request. Generate a new token and resend the address.  
`403` | `Permission denied on resource project PROJECT_ID` | You might have sent a request that contained an incorrect project ID or path.  
`403` | `Unable to retrieve project information` | The organization has not yet been created or provisioned. You can issue a request to the [Operations API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.operations) to check the status of the long-running operation, as described in step 5.  
`403` | `Permission denied on resource project organizations/PROJECT_ID/deployedIngressConfig` | You tried to create an organization but it does not have the correct entitlements. Reach out to your Google Cloud account representative for questions about organization entitlement.  
`409` | `Organization already exists` | You tried to create more than one organization for the Google Cloud project. You can only create one organization per project.  
`409` | `Org PROPOSED_ORG_NAME already exists` | You tried to create an organization that has the same ID as one that already exists. Organization IDs must be unique across all hybrid customers. Resubmit with a new proposed organization ID; for example, append a numeric value to the end of the previous ID that you tried.  
  
##  Next step 

Go to Step 3: [Create an environment group](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/precog-add-environment). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
