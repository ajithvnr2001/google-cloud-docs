---
url: https://docs.cloud.google.com/firewall/docs/manage-wildfire-submissions/
title: Manage Advanced malware sandbox submissions \u00a0|\u00a0 Cloud Next Generation Firewall \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:46:06.664486+00:00
---

# Manage Advanced malware sandbox submissions  |  Cloud Next Generation Firewall  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/firewall/docs/manage-wildfire-submissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud NGFW ](https://docs.cloud.google.com/firewall/docs)
  * [ Guides ](https://docs.cloud.google.com/firewall/docs/about-firewalls)



Send feedback 

#  Manage Advanced malware sandbox submissions Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

When Cloud Next Generation Firewall Enterprise detects unknown files or potential real-time threats in your network, it evaluates the traffic using on-box machine learning models and asynchronous cloud sandboxing according to your Advanced malware sandbox (WildFire) security profiles. Before you begin, review the concepts in the [Advanced malware sandbox security profile](https://docs.cloud.google.com/firewall/docs/about-security-profiles#wildfire-profile) overview.

This page explains how to manage files submitted to the Advanced malware sandbox service for analysis, monitor malware sandboxing results, and track dynamic verdicts using the Google Cloud console and gcloud.

Use the **Advanced malware sandbox submissions** tab on the **NGFW Enterprise logs** page to audit file submissions, download analysis reports or malware samples, and change verdict overrides. To view a summary of the Advanced malware sandbox submissions file analysis activity and malware detected during a specific timeframe in your network, go to the Cloud NGFW [Dashboard](https://console.cloud.google.com/net-security/firewall-manager/dashboard/cards).

To learn more about how file submissions work, see [Advanced malware sandbox overview](https://docs.cloud.google.com/firewall/docs/about-wildfire).

To understand the JSON layout of the logging record, see [Advanced malware sandbox logs](https://docs.cloud.google.com/firewall/docs/wildfire-logs).

## Roles and permissions

To view the list of submissions and access Advanced malware sandbox data, ask your administrator to grant you the necessary Identity and Access Management (IAM) roles for your organization.

Ability | Necessary role  
---|---  
View configuration and basic submission records  | [Compute Network Viewer](https://docs.cloud.google.com/compute/docs/access/iam#compute.networkViewer) (`roles/compute.networkViewer`)   
To access dynamic analysis reports, download original malware samples, or submit verdict change requests | Any of the following roles on the organization or the project:   


  * [Compute Network Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`)
  * The following specific permissions:   

    * `networksecurity.firewallEndpoints.getWildfireReport` for downloading PDF analysis reports.
    * `networksecurity.firewallEndpoints.getWildfireSample` for downloading original malware sample binaries.
    * `networksecurity.firewallEndpoints.createVerdictChangeRequest` for filing manual verdict overrides for false positives or false negatives.
    * `networksecurity.firewallEndpoints.getVerdictChangeRequest` for getting verdict change request details.
    * `networksecurity.firewallEndpoints.listVerdictChangeRequests` for listing verdict change requests.

  
  
For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Change the verdict of a submission

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.firewallEndpoints.createVerdictChangeRequest`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`) 



To submit a verdict change request for a file submitted to Advanced malware sandbox by an endpoint, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Advanced malware sandbox submissions** page.

[Go to WildFire submissions](https://console.cloud.google.com/net-security/ngfw/enterprise-logs/wildfire-submissions/list)

  2. In the project selector menu, select your project.

  3. To change the verdict of the Advanced malware sandbox submission, click _more_vert_ **More actions** for the file whose verdict you want to change.

  4. Click **Change verdict**.

  5. In the **Verdict** list, select the verdict. For example, Malware, Phishing.

  6. In the **Comment** field, enter the justification for the verdict change.

  7. Click **Create**.




###  gcloud 

To submit a verdict change request, use the [`gcloud beta network-security firewall-endpoints wildfire-verdict-change-requests create` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/firewall-endpoints/wildfire-verdict-change-requests/create).
    
    
    gcloud beta network-security firewall-endpoints wildfire-verdict-change-requests create \
        --endpoint ENDPOINT_NAME \
        --organization ORGANIZATION_ID \
        --hash HASH \
        --zone ZONE \
        --verdict VERDICT \
        --comment COMMENT
    

Replace the following:

  * `ENDPOINT_NAME`: the unique full name of the endpoint.

  * `ORGANIZATION_ID`: the organization ID in which the firewall endpoint is located.

  * `HASH`: the hash of the file to submit a verdict change request for.

  * `ZONE`: the zone in which the firewall endpoint is located.

  * `VERDICT`: the verdict requested for the file.

  * `COMMENT`: the justification for the verdict change request. The maximum length is 2,048 characters.




## List verdict change requests

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.firewallEndpoints.listVerdictChangeRequests`



**Roles**

  * Compute Network Viewer (`roles/compute.networkViewer`) 



###  Console 

**Note:** You cannot view a list of all verdict change requests in the Google Cloud console. You can view individual verdict change request status on the details page of the associated Advanced malware sandbox submission.

To list individual verdict change requests, do the following:

  1. In the Google Cloud console, go to the **Advanced malware sandbox submissions** page.

[Go to WildFire submissions](https://console.cloud.google.com/net-security/ngfw/enterprise-logs/wildfire-submissions/list)

  2. In the project selector menu, select your project.

  3. The **Advanced malware sandbox submissions** page lists the configured Advanced malware sandbox submissions.




###  gcloud 

To list individual verdict change requests, use the [`gcloud beta network-security firewall-endpoints wildfire-verdict-change-requests list` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/firewall-endpoints/wildfire-verdict-change-requests/list).

**Note:** When you list verdict change requests, the response includes requests for all firewall endpoints in your organization, even if you specify a specific endpoint in the command.
    
    
    gcloud beta network-security firewall-endpoints wildfire-verdict-change-requests list \
        --endpoint ENDPOINT_NAME \
        --organization ORGANIZATION_ID \
        --zone ZONE
    

Replace the following:

  * `ENDPOINT_NAME`: the unique full name of the endpoint.

  * `ORGANIZATION_ID`: the organization ID in which to list verdict change requests.

  * `ZONE`: the zone in which to list verdict change requests.




## Get verdict change request details

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.firewallEndpoints.getVerdictChangeRequest`



**Roles**

  * Compute Network Viewer (`roles/compute.networkViewer`) 



To get the details of the verdict change request, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Advanced malware sandbox submissions** page.

[Go to WildFire submissions](https://console.cloud.google.com/net-security/ngfw/enterprise-logs/wildfire-submissions/list)

  2. In the project selector menu, select your project.

  3. Click the name of the Advanced malware sandbox submission. The submission details page displays the status and details of the verdict change request.




###  gcloud 

To get the details of the verdict change request, use the [`gcloud beta network-security firewall-endpoints wildfire-verdict-change-requests get` command](https://docs.cloud.google.com/sdk/gcloud/reference/beta/network-security/firewall-endpoints/wildfire-verdict-change-requests/get).
    
    
    gcloud beta network-security firewall-endpoints wildfire-verdict-change-requests get \
        --name NAME \
        --endpoint ENDPOINT_NAME \
        --organization ORGANIZATION_ID \
        --zone ZONE
    

Replace the following:

  * `NAME`: the unique name of the verdict change request.

  * `ENDPOINT_NAME`: the unique full name of the endpoint.

  * `ORGANIZATION_ID`: the organization ID in which to get the verdict change request.

  * `ZONE`: the zone in which to get the verdict change request.




## Download an analysis report

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.firewallEndpoints.getWildfireReport`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`) 



To download the Advanced malware sandbox submission analysis report, do the following:

  1. In the Google Cloud console, go to the **Advanced malware sandbox submissions** page.

[Go to WildFire submissions](https://console.cloud.google.com/net-security/ngfw/enterprise-logs/wildfire-submissions/list)

  2. In the project selector menu, select your project.

  3. Click _more_vert_ **More actions** for the file to download the Advanced malware sandbox analysis report.

  4. Click **Download analysis report**.




## Download a malware sample

#### Permissions required for this task

To perform this task, you must have been granted the following permissions _or_ one of the following IAM roles on your organization.

**Permissions**

  * `networksecurity.firewallEndpoints.getWildfireSample`



**Roles**

  * Compute Network Admin (`roles/compute.networkAdmin`) 



To download the malware sample from a Advanced malware sandbox submission, do the following:

  1. In the Google Cloud console, go to the **Advanced malware sandbox submissions** page.

[Go to WildFire submissions](https://console.cloud.google.com/net-security/ngfw/enterprise-logs/wildfire-submissions/list)

  2. In the project selector menu, select your project.

  3. Click _more_vert_ **More actions** for the file to download the malware sample.

  4. Click **Download malware sample**.




## What's next

  * [Configure Advanced malware sandbox service](https://docs.cloud.google.com/firewall/docs/configure-wildfire)
  * [Create and manage Advanced malware sandbox security profiles](https://docs.cloud.google.com/firewall/docs/configure-wildfire-security-profiles)
  * [Create firewall endpoints and endpoint associations](https://docs.cloud.google.com/firewall/docs/configure-firewall-endpoints)
  * [Manage firewall endpoints and endpoint associations](https://docs.cloud.google.com/firewall/docs/manage-firewall-endpoints)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
