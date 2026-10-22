---
url: https://docs.cloud.google.com/universal-ledger/preview-onboarding/
title: Preview onboarding \u00a0|\u00a0 Universal Ledger \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:24.279194+00:00
---

# Preview onboarding  |  Universal Ledger  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/universal-ledger/preview-onboarding/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Universal Ledger ](https://docs.cloud.google.com/universal-ledger)
  * [ Guides ](https://docs.cloud.google.com/universal-ledger/overview)



Send feedback 

#  Preview onboarding Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://cloud.google.com/application/web3/universal-ledger). 

This guide will help you enable the Universal Ledger Preview API and get started in your Google Cloud projects.

## Allowlist request

As the product is in Preview, some initial onboarding steps are needed to gain access to the API. Once complete, you can enable the API, assign IAM roles, and start sending requests.

  1. **Determine your customer or organization ID**

Before onboarding, your organization will need to be added to an internal allowlist for the API. You'll need to provide one of:

     * The **customer ID** of your organization, which can be retrieved by an administrator following the instructions to [Find your customer ID](https://support.google.com/a/answer/10070793). This ID typically starts with "C" followed by a series of alphanumeric characters.

     * The **organization ID** holding your Google Cloud projects and resources. For guidance see [Getting your organization resource ID](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#retrieving_your_organization_id). This ID is formatted as a large decimal number.

  2. **Select Google Cloud project(s)**

Identify or create the Google Cloud projects that you would like to use with the API. To learn more, see [Creating and managing projects](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects). Ensure that these projects exist within the same customer organization from step (1).

  3. **Get in touch**

Send an email to gcul-help@google.com containing:

     * Your **Customer ID** or **Organization ID** from step (1)
     * The list of **Project IDs** from step (2)

You will receive a confirmation email once your organization and projects have been successfully added to the preview allowlist. Once this step has been completed, you may proceed to enabling the API.




## Enabling the API

Once your projects have been added to the allowlist, you can enable the Universal Ledger API using `gcloud`, and assign granular access to your team members using specific IAM roles.

  1. **Enable the API using gcloud**

To enable the API, use the [`gcloud services enable` command](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable):
         
         gcloud services enable universalledger.googleapis.com \
             --project=PROJECT_ID
         

Replace `PROJECT_ID` with the ID of the project where you want to enable the API.

If you are a project owner, you should now be able to send requests to the API.

  2. **Set up granular access using IAM roles**

To manage granular access to the Universal Ledger API for other members of your organization, you may assign them IAM roles. The API has three IAM roles configured, each providing different layers of access:

     * `roles/universalledger.viewer`: Read-only access to available endpoints and networks. Grants the ability to view the endpoints, and query the network using an endpoint.
     * `roles/universalledger.editor`: Full access to available endpoints and networks. Grants access to query the networks and submit transactions.
     * `roles/universalledger.admin`: Full access to available endpoints and networks. Grants the access to query the networks and submit transactions. This role has the same permissions as the Universal Ledger Editor role, subject to change in the future.

To add a new IAM role to a user, use the [`gcloud projects add-iam-policy-binding` command](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding):
    
    gcloud projects add-iam-policy-binding PROJECT_ID \
        --member="PRINCIPAL" \
        --role="ROLE"
    

Replace the following:

     * `PROJECT_ID`: the project where to add the IAM policy binding
     * `PRINCIPAL`: the principal to whom the role is added, for example: `user:test-user@gmail.com` or `serviceAccount:test123@example.domain.com`.
     * `ROLE`: one of the previously described roles to assign to the principal



## Sending your first request

Now you can start using the API!

To validate that the previous configuration is working correctly, first authenticate using the [`gcloud auth application-default login` command](https://cloud.google.com/sdk/gcloud/reference/auth/application-default/login):
    
    
    gcloud auth application-default login
    

Then try sending an [`endpoints.list` request](https://docs.cloud.google.com/universal-ledger/reference/rest/v1/projects.locations.endpoints/list):
    
    
    curl -H "Authorization: Bearer $(gcloud auth application-default print-access-token)" \
        -X GET "https://universalledger.us-central1.rep.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/endpoints"
    

Requests to a given Universal Ledger network are sent using API endpoints, which will have the form
    
    
    https://universalledger.REGION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/endpoints/NETWORK_NAME
    

Completing these steps validates your access to the Universal Ledger API. In order to submit transactions to a network, however, you will need to create an Universal Ledger account first. See What's next for pointers to the following steps.

## Available networks and regions

There are two networks available during the preview:

  * `gcul-pilot-testing`: Receives **frequent updates** with experimental features. This is the most commonly used network for **fast iteration** and testing new asset types and products.
  * `gcul-user-testing`: The **less frequently updated** network, intended for integrating into payment and settlement workflows, handling both test and live transactions. Only available upon request for limited use cases.



The following table summarizes the regions where validators are available for each of these networks.

Region | gcul-pilot-testing | gcul-user-testing  
---|---|---  
us-central1 |  |   
us-east1 |  |   
us-east4 |  |   
us-east5 |  |   
us-west1 |  |   
europe-west2 |  |   
europe-west3 |  |   
  
## What's next

  * Request the [creation of an account on the ledger](https://docs.cloud.google.com/universal-ledger/how-to/request-account).
  * Learn how to [send RPC requests with Python](https://docs.cloud.google.com/universal-ledger/tutorial/send-rpc-request-py).
  * Explore the [Universal Ledger API protocol buffer definitions](https://github.com/googleapis/googleapis/tree/master/google/cloud/universalledger/v1).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-02 UTC."],[],[]] 
