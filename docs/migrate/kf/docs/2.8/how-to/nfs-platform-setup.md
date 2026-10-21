---
url: https://docs.cloud.google.com/migrate/kf/docs/2.8/how-to/nfs-platform-setup/
title: Set up NFS platform \u00a0|\u00a0 Kf 2.8 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:35:26.183385+00:00
---

# Set up NFS platform  |  Kf 2.8  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.8/how-to/nfs-platform-setup/

Version 2.8

Available versions

[2.11 - Latest version](https://docs.cloud.google.com/migrate/kf/docs/2.11)  
[2.10](https://docs.cloud.google.com/migrate/kf/docs/2.10)  
[2.9](https://docs.cloud.google.com/migrate/kf/docs/2.9)  
[2.8 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.8)  
[2.7 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.7)  
[2.6 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.6)  
[2.5 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.5)  
[2.4 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.4)  
[2.3 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.3)  
[2.2 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.2)  
[2.1 - EOL/Unsupported](https://docs.cloud.google.com/migrate/kf/docs/2.1)  


  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Kf ](https://docs.cloud.google.com/migrate/kf/docs)
  * [ 2.8 ](https://docs.cloud.google.com/migrate/kf/docs/2.8)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.8/getting-started)



Send feedback 

#  Set up NFS platform Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Kf supports Kubernetes native NFS, and exposes them with a dedicated `nfsvolumebroker` service broker for developers to consume. This broker has an `nfs` service offering which has a service plan named `existing`.

Use `kf marketplace` to see the service offering:
    
    
    $ kf marketplace
    ...
    Broker           Name  Namespace  Description
    nfsvolumebroker  nfs              mout nfs shares
    ...
    

Use `kf marketplace -s nfs` to see the service plan:
    
    
    $ kf marketplace -s nfs
    ...
    Broker           Name      Free  Description
    nfsvolumebroker  existing  true  mount existing nfs server
    ...
    

## Requirements

You need an NFS volume that can be accessed by your Kubernetes cluster. [Filestore](https://docs.cloud.google.com/filestore) is Google's managed NFS solution that provides access to clusters in the same gcloud project.

## Prepare NFS

If you have an existing NFS service, you can use that. If you want a Google managed NFS service, [create a Filestore instance](https://docs.cloud.google.com/filestore/docs/creating-instances) and Kf will automaticlaly configure the cluster to use it.

**Warning:** You only need to create the NFS instance. Kf will create relevant Kubernetes objects, including PersistentVolume and PersistentVolumeClaims. Do not manually mount the volume.

## What's next?

  * [Configure NFS volumes](https://docs.cloud.google.com/migrate/kf/docs/2.8/how-to/nfs-getting-started)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
