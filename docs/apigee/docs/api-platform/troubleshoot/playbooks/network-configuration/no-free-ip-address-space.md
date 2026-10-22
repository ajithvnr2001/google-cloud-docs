---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/network-configuration/no-free-ip-address-space/
title: No free IP address space troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:32:00.376549+00:00
---

# No free IP address space troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/network-configuration/no-free-ip-address-space/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  No free IP address space troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## Symptom

During Apigee provisioning, if you select a network CIDR range that is not completely free, you may see an error message. 

## Error message
    
    
    error waiting for creating
    instance: error code 9: message: couldn't find a free ip space of /22 to
    launch an instance. verify the peering ranges are available.

## Possible cause

The IP address range specified during provisioning is not available. Each Apigee instance requires a non-overlapping CIDR range of /22 as described in [ Network sizing](https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/peering-ranges#sizing). 

### Diagnosis

  1. In the Google Cloud console, go to the **VPC Network Peering** page. See also [ Using VPC Network Peering](https://docs.cloud.google.com/vpc/docs/using-vpc-peering#console_1). 

[Go to VPC Network Peering](https://console.cloud.google.com/networking/vpc-connectivity/peering)

  2. Select your VPC network peering connection. For example, `servicenetworking-googleapis-com`. The **Peering connection details** page opens:  
  


![](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/images/peering-connection-details.png)![](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/images/peering-connection-details.png)

  3. Locate the CIDR range you specified during the [ provisioning process](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/provisioning-intro) and verify that it does not overlap with any of the IP addresses listed on the **Peering connection details** page. 



### Resolution

During the provisioning process, for the **IP range allocation** , select one of: 

  * **Automatic (recommended)**
  * **Custom** , and then specify a non-overlapping range: 

![](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/images/ip-range-allocation.png)![](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/playbooks/images/ip-range-allocation.png)




## Must gather diagnostic information

If the problem persists even after following the above instructions, gather the following diagnostic information and then contact [Google Cloud Customer Care](https://cloud.google.com/support-hub/): 

  * Apigee organization 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
