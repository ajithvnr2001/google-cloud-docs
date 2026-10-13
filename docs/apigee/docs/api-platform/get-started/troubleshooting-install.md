---
url: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/troubleshooting-install/
title: Troubleshooting the Apigee installation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:02.151665+00:00
---

# Troubleshooting the Apigee installation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/get-started/troubleshooting-install/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Troubleshooting the Apigee installation Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** , but not to **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This document lists common errors and describes possible resolutions for when you install and configure Apigee.

## Creating a new instance

This section describes common errors and possible resolutions after sending a request to Apigee to create a new instance:

  * `401 (UNAUTHENTICATED)` indicates that your credentials may have timed out. Try renewing your authorization token, as the following example shows: 
        
        AUTH="Authorization: Bearer $(gcloud auth print-access-token)"

  * `RANGES_EXHAUSTED` indicates that the range of IP addresses that you initially requested could not be accommodated and that you must request a new range. You initially created a range request in [Step 2: Set up networking](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/configure-service-networking). 
    1. Create these environment variables 
    
    **RANGE_NAME_1** =YOUR_RANGE_NAME_1
      **RANGE_NAME_2** =YOUR_RANGE_NAME_2
      **NETWORK_NAME** =YOUR_NETWORK_NAME

    2. Verify the details of the existing address ranges and ensure it will not overlap with the new range. 
    
    gcloud compute addresses list --global --project=**$PROJECT_ID**
    
    gcloud compute addresses describe **$RANGE_NAME_1** --global --project=**$PROJECT_ID** 

    3. To request a new range from which Apigee chooses an IP address for the private service connections execute the following **gcloud** command: 
    
    gcloud compute addresses create **$RANGE_NAME_2**
                --project=**$PROJECT_ID** --global --prefix-length=16
                --description="additional peering range for Google services" --network=**$NETWORK_NAME**
                --purpose=VPC_PEERING 

This command creates a new range named **$RANGE_NAME_2**. 

    4. Verify the details of both the old and new address range 
    
    gcloud compute addresses list --global --project=**$PROJECT_ID** 
    
    gcloud compute addresses describe **$RANGE_NAME_1** --global --project=**$PROJECT_ID** 
    
    gcloud compute addresses describe **$RANGE_NAME_2** --global --project=**$PROJECT_ID** 

    5. Verify the existing VPC peering details: 
    
    gcloud services vpc-peerings list \
                --network=**$NETWORK_NAME** \
                --service=servicenetworking.googleapis.com \
                --project=**$PROJECT_ID** 

    6. Execute the following command to update your connection request: 
    
    gcloud services vpc-peerings update
                --service=servicenetworking.googleapis.com --network=**$NETWORK_NAME**
                --ranges=**$RANGE_NAME_1** ,**$RANGE_NAME_2** --project=**$PROJECT_ID** 

**Note:** You must specify the name of your first range (in this case, `RANGE_NAME_1`) and a name for your newly requested range (in this case, `RANGE_NAME_2`). For more information, see [gcloud services vpc-peerings update](https://docs.cloud.google.com/sdk/gcloud/reference/services/vpc-peerings/update).
    7. Verify the existing VPC peering details: 
    
    gcloud services vpc-peerings list \
                --network=**$NETWORK_NAME** \
                --service=servicenetworking.googleapis.com \
                --project=**$PROJECT_ID** 




## Creating an Apigee organization

The following example shows a common error that Apigee might display when you first try to create an organization:
    
    
      Apigee API (staging) has not been used in project 59387731598 before or it is disabled.
      Enable it by visiting https://console.developers.google.com/apis/api/staging-apigee.sandbox.googleapis.com/overview?project=59387731598 then retry.
      If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry.

This means that one or more of the required APIs is not enabled. Review the APIs listed in [Step 1: Enable required APIs](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/enable-apis) and be sure that all APIs are enabled before you continue.

In addition, you might get one of the following HTTP errors:

  * `401 (UNAUTHENTICATED)` indicates that your credentials may have timed out. Try renewing your authorization token, as the following example shows: 
        
        AUTH="Authorization: Bearer $(gcloud auth print-access-token)"

  * `404 (Not Found)` can be the result of the following: 
    * You entered the wrong endpoint/request URL. Check that you specified `apigee.googleapis.com` for the API call's domain.
    * Your project might not yet be provisioned. Contact [Apigee Sales](https://pages.apigee.com/contact-sales-reg.html).
  * `409 (Conflict)` usually indicates that the given organization name already exists. Organization names must be globally unique. Choose another name for the organization and re-issue the command. (You specify the name in the payload of the request if you are creating an organization on the command line. Keep in mind that you must create an organization that has the same name as your project, so this really shouldn't happen unless there's a typo.)



The following is a possible error that Apigee might return when you check the status of a new organization request:

  * `403 (Permission Denied)` could indicate that the organization has not yet been created. Wait another minute and try again. If Apigee returns a `403` when you first try to create the new organization, it could mean that one or more of your APIs have not been enabled. Be sure that you enabled all the APIs as described in [Step 1: Enable required APIs](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/enable-apis) .



## Deploying samples

###  Load balancer not healthy 

When deploying a sample proxy, Apigee might return a `502 (Bad Gateway)` HTTP error. In this case, try the following:

  1. Check the health of the Load Balancer. The Load balancer tab shows all load balancers for the project and their statuses. A yellow triangle indicates that the load balancer backend service is not healthy. 

In the Google Cloud console, go to the **Network services > Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing)

  2. After confirming an issue with the load balancer, check the VMs in your runtime instance to ensure that they are up and healthy.
  3. Look at the log files to see if you can find an error or other type of issue that might have lead to a problem. For more information on enabling and viewing logs, see [Viewing logs](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#viewing_logs). 
  4. Try doing a rolling restart on the instance group in Cloud console: 
     1. In the Google Cloud console, go to the **Compute Engine > Instance groups** page.

[Go to Instance groups](https://console.cloud.google.com/compute/instanceGroups)

     2. From the list of instance groups, click the one that is not responding in the **Name** column.
     3. Click **Rolling Restart/Replace**. 
     4. On the next screen, click **Restart**. 

This restarts the Envoy instance.




###  Incorrect instance IP 

If at any time you delete and recreate your Apigee instance, the Apigee instance IP changes and can become out of sync with the managed instance group (MIG) template's endpoint IP. For example, the MIG template will still have the old IP from the deleted instance. The MIG template was created during the Apigee [provisioning process](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/install-cli#external). In this situation, try the following steps to update the MIG template with the correct Apigee IP:

  1. In the Google Cloud console, go to the **Apigee > Admin > Instances** page.

[Go to Instances](https://console.cloud.google.com/apigee/instances)

  2. Note the IP Address of the instance. You will need to know this IP in a later step. For example: `10.117.200.2`.
  3. In the Google Cloud console, go to the **Instance templates** page.

[Go to Instance templates](https://console.cloud.google.com/compute/instances)

  4. Open the instance template. You need to open the instance template that is used by the backend that is mapped to your load balancer.
  5. Scroll down to find the `ENDPOINT` IP under the **Custom metadata** section.
  6. If the endpoint IP differs from the one you noted in the Apigee UI, you must change the Instance template IP to match the Apigee instance IP. See [Changing instance IPs.](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/change-instance-ips)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
