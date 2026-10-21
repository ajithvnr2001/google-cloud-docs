---
url: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/troubleshoot/known-issues/
title: Known issues for GKE on AWS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:15:13.276348+00:00
---

# Known issues for GKE on AWS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/troubleshoot/known-issues/

The product described by this documentation, GKE on AWS, is now in [maintenance mode](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/deprecations/deprecation-announcement) and will be shut down on March 17, 2027. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE Multi-Cloud ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs)
  * [ GKE on AWS ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/concepts/architecture)



Send feedback 

#  Known issues for GKE on AWS Stay organized with collections  Save and categorize content based on your preferences. 

This page lists selected known issues for GKE on AWS, and steps you can take to reduce their impact. 

To filter the known issues by a product version or category, select your filters from the following drop-down menus.

If you're part of the Google Developer Program, save this page to receive notifications when a release note related to this page is published. To learn more, see [Saved Pages](https://developers.google.com/profile/help/saved-pages).

Select your GKE on AWS version:

1.281.271.261.251.241.231.22

Select your problem category:

OperationsNetworkingUsability

Or, search for your issue:

Category | Identified version(s) | Issue and workaround  
---|---|---  
Operations | 1.28.0-gke.0 up to, but not including, 1.28.8-gke.800, 1.27.0-gke.0 up to, but not including, 1.27.12-gke.800, 1.26, 1.25, 1.24, 1.23, 1.22 | 

### Cluster autoscaler might incorrectly scale up from zero nodes

Cluster autoscaler doesn't correctly scale up from zero nodes for node pools with custom labels or taints. This issue occurs because the GKE on AWS cluster autoscaler didn't configure the node pool labels and taint tags on the corresponding node pool Auto Scaling Group during node pool provisioning. For node pools with zero nodes, the cluster autoscaler can't create the node templates correctly because of these missing tags. This could lead to incorrect scaling decisions, such as Pods not being scheduled to the applicable nodes, or nodes being provisioned that aren't really needed. For more information, see [Auto-Discovery Setup](https://github.com/kubernetes/autoscaler/blob/df0ce2d99ab23b631b87a272eac7c2c552c198dc/cluster-autoscaler/cloudprovider/aws/README.md#auto-discovery-setup).  
Networking | 1.26.0-gke.0 up to, but not including, 1.26.4-gke.220, 1.25.0-gke.0 up to, but not including, 1.25.10-gke.1200, 1.24 starting from 1.24.0-gke.0, 1.23 starting from 1.23.8-gke.1700 | 

### Application timeouts caused by conntrack table insertion failures

Clusters running on an Ubuntu OS that uses kernel 5.15 or higher are susceptible to netfilter connection tracking (conntrack) table insertion failures. Insertion failures can occur even when the conntrack table has room for new entries. The failures are caused by changes in kernel 5.15 and higher that restrict table insertions based on chain length. To see if you are affected by this issue, check the in-kernel connection tracking system statistics with the following command:
    
    
        sudo conntrack -S
        

The response looks like this:
    
    
    cpu=0       found=0 invalid=4 insert=0 insert_failed=0 drop=0 early_drop=0
    error=0 search_restart=0 clash_resolve=0 chaintoolong=0
    cpu=1       found=0 invalid=0 insert=0 insert_failed=0 drop=0 early_drop=0
    error=0 search_restart=0 clash_resolve=0 chaintoolong=0
    cpu=2       found=0 invalid=16 insert=0 insert_failed=0 drop=0 early_drop=0
    error=0 search_restart=0 clash_resolve=0 chaintoolong=0
    cpu=3       found=0 invalid=13 insert=0 insert_failed=0 drop=0 early_drop=0
    error=0 search_restart=0 clash_resolve=0 chaintoolong=0
    cpu=4       found=0 invalid=9 insert=0 insert_failed=0 drop=0 early_drop=0
    error=0 search_restart=0 clash_resolve=0 chaintoolong=0
    cpu=5       found=0 invalid=1 insert=0 insert_failed=0 drop=0 early_drop=0
    error=519 search_restart=0 clash_resolve=126 chaintoolong=0
        

If a `chaintoolong` value in the response is a non-zero number, you are affected by this issue. **Workaround:** If you are running version 1.26.2-gke.1001, upgrade to version 1.26.4-gke.2200 or later.  
Usability | 1.25.5-gke.1500, 1.25.4-gke.1300 | 

### Unreachable clusters detected error in UI

Some UI surfaces in Google Cloud console can't authorize to the cluster and might display the cluster as unreachable. **Workaround:** Upgrade your cluster to the latest available patch of version 1.25. This issue was fixed in version 1.25.5-gke.2000.  
Usability | 1.22 | 

### API errors

Kubernetes 1.22 deprecates and replaces several APIs. If you've upgraded your cluster to version 1.22 or later, any calls your application makes to one of the deprecated APIs fail. **Workaround:** Upgrade your application to [replace the deprecated API calls](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-22) with their newer counterparts.  
  
If you need additional assistance, reach out to [Cloud Customer Care](https://docs.cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/getting-support). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
