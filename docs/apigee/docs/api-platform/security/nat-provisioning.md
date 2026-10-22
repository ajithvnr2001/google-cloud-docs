---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/nat-provisioning/
title: Provisioning NAT IPs \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:29.982676+00:00
---

# Provisioning NAT IPs  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/nat-provisioning/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Provisioning NAT IPs Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This section describes how to manage the NAT IPs for Apigee instances.

Apigee provides ephemeral IPs and dedicated IPs. In many cases, ephemeral IPs are sufficient. If your backend doesn't require IP allow-listing, you will not need to manage NAT IPs, and Apigee will automatically allocate ephemeral IPs for egress.

If you require IP allow-listing, you can reserve and activate IPs so that Apigee uses static IPs for egress traffic.

## Set up Apigee NAT IP provisioning

**To set NAT IP provisioning for your Apigee instance:**

  1. Create and populate the following environment variables: 

### Variables
         
         PROJECT_ID=YOUR_PROJECT_ID
         ORG_ID=YOUR_ORG_ID
         INSTANCE_NAME=YOUR_INSTANCE_NAME
         NAT_ID=1st_NAT_IP_ID

### Example
         
         PROJECT_ID=apigee-saas-prod
         ORG_ID=apigee-saas-prod
         INSTANCE_NAME=prod-us-west1-instance1
         NAT_ID=nat-1

Where:

     * YOUR_PROJECT_ID is the Cloud project ID that you created as part of the [Prerequisites](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/overview#prerequisites). If you're not sure what your project ID is, use Cloud console or the `gcloud projects list` command to find it.
     * YOUR_ORG_ID is your Apigee organization ID.
     * YOUR_INSTANCE_NAME is the name of your Apigee instance.
     * 1st_NAT_IP_ID is the name you are assigning to this NAT IP address; for example, `nat-1`. The value of this parameter must not exceed 20 characters.
  2. Reserve a NAT IP with the following commands: **Note:** These commands can take several minutes to execute.
     1. On the command line, get your `gcloud` authentication credentials, as the following example shows: 
            
            TOKEN=$(gcloud auth print-access-token)

To check that your token was populated, use `echo`, as the following example shows:
            
            echo $TOKEN

This should display your token as an encoded string.

For more information, see [gcloud command-line tool overview](https://cloud.google.com/sdk/gcloud/).

     2. The command to reserve the NAT IP returns the long-running operation. Therefore the command as shown here assigns the output to a variable `operation_name`: 
            
            operation_name=$(curl -H "Authorization: Bearer $TOKEN" \
              "https://apigee.googleapis.com/v1/organizations/${ORG_ID}/instances/${INSTANCE_NAME}/natAddresses" \
              -X POST -H "content-type:application/json" -d "{\"name\":\"${NAT_ID}\"}" | jq -r '.name')
            

     3. Poll the long-running operation until it shows a status of `done: true` by executing the following request: 
            
            curl -s -H "Authorization: Bearer $TOKEN" "https://apigee.googleapis.com/v1/$operation_name"

  3. After the operation is completed, activate the NAT IP with the following commands: **Note:** These commands can take several minutes to execute.
     1. Activate the IP and assign the long-running operation name to `operation_name`: 
            
            operation_name=$(curl -H "Authorization: Bearer $TOKEN" \
              "https://apigee.googleapis.com/v1/organizations/${ORG_ID}/instances/${INSTANCE_NAME}/natAddresses/${NAT_ID}:activate" \
              -X POST -H "content-type:application/json" -d "{}" | jq -r '.name')

     2. Poll the long-running operation until it shows a status of `done: true`: 
            
            curl -s -H "Authorization: Bearer $TOKEN" "https://apigee.googleapis.com/v1/$operation_name"

  4. Repeat this procedure with a new NAT IP name for each NAT IP you neet to set up.



## Fetching NAT IPs

List the NAT IPs for an instance with the following command:
    
    
    curl -H "Authorization: Bearer $TOKEN" \
      "https://apigee.googleapis.com/v1/organizations/${ORG_ID}/instances/${INSTANCE_NAME}/natAddresses"

An example response would look like:
    
    
    {
      "natAddresses": [
        {
          "name": "nat-1",
          "ipAddress": "35.203.160.18",
          "state": "ACTIVE"
        },
        {
          "name": "nat-2",
          "ipAddress": "35.230.14.174",
          "state": "RESERVED"
        },
        {
          "name": "nat-3",
          "state": "CREATING"
        }
      ]
    }

### States of a NAT IP

  * `CREATING `: The NAT IP creation is pending. Not ready to be used.
  * `RESERVED`: The NAT IP has been created but not used. This gives you the opportunity to allow-list this IP before activating it.
  * `ACTIVE`: The NAT IP is being used to send egress traffic.
  * `DELETING`: The NAT IP is being deleted.



## Deleting NAT IPs

You can delete NAT IPs with the following command:

  1. Delete the IP and assign the output to "`operation_name`." 
         
         operation_name=$(curl -H "Authorization: Bearer $TOKEN" \
           "https://apigee.googleapis.com/v1/organizations/${ORG_ID}/instances/${INSTANCE_NAME}/natAddresses/${NAT_ID}" \
           -X DELETE | jq -r '.name')

  2. Poll the long-running operation until it shows a status of `done: true`. 
         
         curl -s -H "Authorization: Bearer $TOKEN" "https://apigee.googleapis.com/v1/$operation_name"




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
