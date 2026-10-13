---
url: https://docs.cloud.google.com/data-fusion/docs/how-to/control-access-in-namespace/
title: Access control with a namespace service account \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:07.061602+00:00
---

# Access control with a namespace service account  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/how-to/control-access-in-namespace/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Access control with a namespace service account Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure an Identity and Access Management (IAM) service account for a namespace in a Cloud Data Fusion instance.

## About namespaces in Cloud Data Fusion

A namespace is a logical grouping of applications, data, and the associated metadata in a Cloud Data Fusion instance. You can think of namespaces as a partitioning of the instance. Any application or data, referred to here as an _entity_ , can exist independently in multiple namespaces. In a single instance, one namespace stores the data and metadata of an entity independently from another namespace.

## Access control with a namespace service account

To control access to Google Cloud resources, namespaces in Cloud Data Fusion use the [Cloud Data Fusion API Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent) by default.

For better data isolation, you can associate a customized IAM service account (known as a _Per Namespace Service Account_) with each namespace. The customized IAM service account, which can be different for different namespaces, lets you control access to Google Cloud resources between namespaces for pipeline design-time operations in Cloud Data Fusion, such as pipeline preview, Wrangler, and pipeline validation.

## Before You begin

  * Per Namespace Service Accounts are supported in RBAC-enabled instances in Cloud Data Fusion versions 6.10.0 and later.
  * Per Namespace Service Accounts are used to control and manage access to Google Cloud resources.



### Required roles and permissions

To get the permissions that you need to customize namespace service accounts and give user permissions within a namespace, ask your administrator to grant you the [Cloud Data Fusion Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.admin) (`roles/datafusion.admin`) IAM role on the Cloud Data Fusion instance in the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

#### Manage permissions for users in a namespace

To give users the permissions they need in a namespace, grant predefined Cloud Data Fusion roles to them. For more information, see the [predefined Cloud Data Fusion roles](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac#predefined-roles) available to users in RBAC-enabled instances.

## Configure a namespace service account

### Console

To configure a service account for the namespace, follow these steps:

  1. If you don't have an existing service account for the namespace, [create one](https://docs.cloud.google.com/iam/docs/service-accounts-create).
  2. In the Google Cloud console, go to the Cloud Data Fusion **Instances** page and open an instance in the Cloud Data Fusion web interface.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  3. Click **System admin > Configuration > Namespaces**.

  4. Click the namespace that you want to configure.

  5. Click the **Service accounts** tab, and then click **Add service account**.

**Note:** Only one namespace service account can be added to a namespace. If a service account has already been added to the namespace, **Add service account** doesn't appear.

![Add Service Account button.](https://docs.cloud.google.com/static/data-fusion/docs/images/how-to/control-access-in-namespaces/add-namespace-sa.png)

  6. Grant the Workload Identity User role (`roles/iam.workloadIdentityUser`).

**Note:** To use an IAM service account with the namespace, Cloud Data Fusion's internal Kubernetes Service Account (KSA) requires the permissions included in this role.

To grant the role, follow these steps:

     1. In the **Pipeline design service account** field, enter the service account email—for example, `SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`.
     2. Follow the instructions in the dialog that appears.
  7. To complete the service account configuration, go back to the namespace of your Cloud Data Fusion instance and click **Save**.

**Note:** The change to your IAM policy in step 6 might take several minutes to propagate. If you get a `403` error, you might need to wait for more time. For more information, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).
  8. Repeat the steps to configure a service account for each namespace.

**Note:** Any namespace that doesn't have a service account configured continues to use the [Cloud Data Fusion Service API Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datafusion#datafusion.serviceAgent), as before.



### REST API

  1. Grant the Workload Identity User role (`roles/iam.workloadIdentityUser`).

**Note:** To use an IAM service account with the namespace, Cloud Data Fusion's internal Kubernetes Service Account (KSA) requires the permissions included in this role.

To grant the role, follow these steps:

     1. Set the following environment variables:
            
            export TENANT_PROJECT_ID=TENANT_PROJECT
            export GSA_PROJECT_ID=SERVICE_ACCOUNT_PROJECT
            

Replace the following:

        * `TENANT_PROJECT`: the tenant project ID. To find it, go to the **Instances** page and click the instance name. The ID appears on the **Instance details** page.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

        * `SERVICE_ACCOUNT_PROJECT`: the Google Cloud project ID where the IAM service account is located.

     2. Grant the Workload Identity User role:
            
            gcloud iam service-accounts add-iam-policy-binding \
                --role roles/iam.workloadIdentityUser
                --member "serviceAccount:${TENANT_PROJECT_ID}.svc.id.goog[default/NAMESPACE_IDENTITY]" SERVICE_ACCOUNT_EMAIL \
                --project ${GSA_PROJECT_ID}
            

Replace the following:

        * `NAMESPACE_IDENTITY`: the identity of the namespace. For more information, see [Details of a namespace](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561041/Namespace+Microservices#Details-of-a-Namespace).

        * `SERVICE_ACCOUNT_EMAIL`: the email address of the service account—for example, `SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com`.

  2. Validate the namespace service account email from the previous step. Set the [`environment variables`](https://docs.cloud.google.com/reference/cdap-reference#set-up), then run the following command:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json" ${CDAP_ENDPOINT}/v3/namespaces/NAMESPACE_NAME/credentials/workloadIdentity/validate -X POST -d '{"serviceAccount":"SERVICE_ACCOUNT_EMAIL"}'
         

Replace the following:

     * `NAMESPACE_NAME`: the ID of the namespace.
     * `SERVICE_ACCOUNT_EMAIL`: the IAM service account email you want to set in the namespace.
**Note:** The change to your IAM policy in step 1b might take several minutes to propagate. If you get a `403` error, you might need to wait for more time. For more information, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).
  3. Set the namespace service account. Set the [`environment variables`](https://docs.cloud.google.com/reference/cdap-reference#set-up), then run the following command:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"
          ${CDAP_ENDPOINT}/v3/namespaces/NAMESPACE_NAME/credentials/workloadIdentity -X PUT -d '{"serviceAccount":"SERVICE_ACCOUNT_EMAIL"}'
         




## Edit a namespace service account

### Console

To edit a namespace service account, follow these steps:

  1. In your Cloud Data Fusion instance, click **System admin > Configuration > Namespaces**.
  2. Click the namespace that has the service account you want to edit.
  3. To edit the service account, go to the **Service accounts** tab. Next to the name of the service account, click more_vert  **Menu > Edit**.
  4. Follow the steps to configure a namespace service account.



### REST API

To edit a namespace service account, follow these steps:

  1. Set the [`environment variables`](https://docs.cloud.google.com/reference/cdap-reference#set-up), then run the following command:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" -H "Content-Type: application/json"
          ${CDAP_ENDPOINT}/v3/namespaces/NAMESPACE_NAME/credentials/workloadIdentity -X PUT -d '{"serviceAccount":"SERVICE_ACCOUNT_EMAIL"}'
         

Replace the following:

     * `NAMESPACE_NAME`: the ID of the namespace.
     * `SERVICE_ACCOUNT_EMAIL`: the IAM service account email you want to set in the namespace.



## Delete a namespace service account

### Console

To delete a namespace service account from a namespace, follow these steps:

  1. In your Cloud Data Fusion instance, click **System admin > Configuration > Namespaces**.
  2. Click the namespace that has the service account you want to delete.
  3. To remove the service account, go to the **Service accounts** tab. Next to the name of the service account, click more_vert  **Menu > Delete**.

**Note:** Deletion removes the service account association with the namespace, but doesn't delete the service account.

### REST API

To delete a namespace service account from a namespace, follow these steps:

  1. Set the [`environment variables`](https://docs.cloud.google.com/reference/cdap-reference#set-up), then run the following command:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" ${CDAP_ENDPOINT}/v3/namespaces/NAMESPACE_NAME/credentials/workloadIdentity -X DELETE
         

Replace the following:

     * `NAMESPACE_NAME`: the ID of the namespace.
**Note:** Deletion removes the service account association with the namespace, but doesn't delete the service account.



## Get the namespace service account

### Console

To get service account information for the namespace, follow these steps:

  1. In the Google Cloud console, go to the Cloud Data Fusion **Instances** page and open an instance in the Cloud Data Fusion web interface.

[Go to Instances](https://console.cloud.google.com/data-fusion/locations/-/instances)

  2. Click **System admin > Configuration > Namespaces**.

  3. Click a namespace name to view service account details.




### REST API

To get the namespace service account name, follow these steps:

  1. Set the [`environment variables`](https://docs.cloud.google.com/reference/cdap-reference#set-up), then run the following command:
         
         curl -H "Authorization: Bearer $(gcloud auth print-access-token)" ${CDAP_ENDPOINT}/v3/namespaces/NAMESPACE_NAME/credentials/workloadIdentity -X GET
         

Replace the following:

     * `NAMESPACE_NAME`: the ID of the namespace.

If successful, you get the service account email in the following response:
    
    Response: {"serviceAccount":"SERVICE_ACCOUNT_EMAIL"}
    




## What's next

  * Learn more about the [use case for access control with namespace service accounts](https://docs.cloud.google.com/data-fusion/docs/use-case/namespace-service-accounts).
  * Learn more about [role-based access control in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/rbac).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
