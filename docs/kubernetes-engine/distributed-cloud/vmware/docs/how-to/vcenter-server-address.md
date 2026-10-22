---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-server-address/
title: Finding your vCenter server address \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:26.120949+00:00
---

# Finding your vCenter server address  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-server-address/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Finding your vCenter server address Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to determine the value you should enter for your vCenter server address in a Google Distributed Cloud [admin workstation configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-workstation-configuration-file) or an [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest). In some cases, you might also want to to enter this value in a [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest).

This page is for IT administrators and Operators who manage the lifecycle of the underlying tech infrastructure. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

In certain situations you must enter an IP address, and in other situations you must enter a hostname. And in some cases, it doesn't matter. You can determine the appropriate value by inspecting the serving certificate of your vCenter server.

Download the serving certificate of your vCenter server, and save it to a file named `vcenter.pem`:
    
    
    true | openssl s_client -connect VCENTER_IP:443 -showcerts 2>/dev/null | sed -ne '/-BEGIN/,/-END/p' > vcenter.pem
    

Replace `VCENTER_IP` with the IP address of your vCenter Server.

Open the certificate file to see the Subject Common Name and the Subject Alternative Name:
    
    
    openssl x509 -in vcenter.pem -text -noout
    

The output shows the Subject Common Name (CN). This might be an IP address, or it might be a hostname. For example:
    
    
    Subject: ... CN = 203.0.113.100
    
    
    
    Subject: ... CN = my-host.my-domain.example
    

The output might also include one or more DNS names under `Subject Alternative Name`:
    
    
    X509v3 Subject Alternative Name:
        DNS:vcenter.my-domain.example
    

Choose the Subject Common Name or one of the DNS names under `Subject Alternative Name` to use as the value of the vCenter server address in your configuration file. For example:
    
    
    vCenter:
      credentials:
        address: "203.0.113.1"
    
    
    
    vCenter:
      credentials:
        address: "my-host.my-domain.example"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
