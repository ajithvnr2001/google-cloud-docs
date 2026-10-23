---
url: https://docs.cloud.google.com/vpc/docs/manage-endpoints-published-services/
title: Manage endpoints used to access published services \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:37:16.651827+00:00
---

# Manage endpoints used to access published services  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/manage-endpoints-published-services/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage endpoints used to access published services

After you have created a Private Service Connect endpoint to access managed services, you can turn global access on or off. If you need to update other fields, delete the endpoint, and then create a new one.

## Roles

The following [IAM role](https://docs.cloud.google.com/iam/docs/understanding-roles) provides the permissions needed to perform the tasks in this guide.

Task | Roles  
---|---  
Update a Private Service Connect endpoint |  [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)   
  
## Configure global access

You can turn global access on or off after an endpoint is [created](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services).

### Turn on global access

You can turn on global access when you [create an endpoint](https://docs.cloud.google.com/vpc/docs/configure-private-service-connect-services#create-endpoint), or you can turn on global access at any time after the endpoint is created. Turning on global access does not cause traffic disruption for existing connections.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Connected endpoints** tab.

  3. Click the endpoint that you want to update.

  4. Click **Edit**.

  5. Select **Enable global access**.

  6. Click **Save**.




###  gcloud 
    
    
    gcloud compute forwarding-rules update ENDPOINT_NAME \
        --allow-psc-global-access \
        --region=REGION
    

### Turn off global access

You can turn off global access, which terminates any connections from regions other than the region where the endpoint is located.

###  Console 

  1. In the Google Cloud console, go to the **Private Service Connect** page.

[Go to Private Service Connect](https://console.cloud.google.com/net-services/psc)

  2. Click the **Connected endpoints** tab.

  3. Click the endpoint that you want to update.

  4. Click **Edit**.

  5. Clear **Enable global access**.

  6. Click **Save**.




###  gcloud 
    
    
    gcloud compute forwarding-rules update ENDPOINT_NAME \
        --no-allow-psc-global-access \
        --region=REGION
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
