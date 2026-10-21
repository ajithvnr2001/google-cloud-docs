---
url: https://docs.cloud.google.com/migrate/kf/docs/2.4/how-to/compute-isolation/
title: Compute Isolation \u00a0|\u00a0 Kf 2.4 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:09:08.131884+00:00
---

# Compute Isolation  |  Kf 2.4  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.4/how-to/compute-isolation/

Version 2.4

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
  * [ 2.4 ](https://docs.cloud.google.com/migrate/kf/docs/2.4)
  * [ Guides ](https://docs.cloud.google.com/migrate/kf/docs/2.4/getting-started)



Send feedback 

#  Compute Isolation Stay organized with collections  Save and categorize content based on your preferences. 

Kf Apps can be deployed on dedicated nodes in the cluster. This feature is required if you have the circumstances where you may want more control on a node where an App pod lands. For example, if you are sharing a same cluster for different Apps but want dedicated nodes for a particular App, if you want dedicated nodes for a given organization(Kf Space), to target a specific operating system like Windows, or to co-locate pods from two different services that frequently communicate.

To enable compute isolation, Kf uses the Kubernetes [nodeSelector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node). To use this feature, first add labels on the nodes or node pools where you want your App pods to land and then add the same qualifying labels on the Kf Space. All the Apps installed in this Space will then land on the nodes with matching labels.

## Configuring nodeSelector in a Kf cluster

By default, compute isolation is disabled. Use the following procedure to configure labels and nodeSelector.

  1. Add a label (`distype=ssd`) on the node where you want your application pods to land.
         
         kubectl label nodes nodeid disktype=ssd 

  2. Add the same label on the Kf Space. All Apps deployed in this Space will then land on the qualifying nodes.
         
         kf configure-space set-nodeselector space-name disktype ssd

You can add multiple labels by running the same command again.

  3. Check the label is configured.
         
         kf configure-space get-nodeselector space-name

  4. Delete the label from the space.
         
         kf configure-space unset-nodeselector space-name disktype




## Override nodeSelector for [kf Stacks](https://docs.cloud.google.com/migrate/kf/docs/2.4/cli/kf-stacks)

Deployment of Kf Apps can be further taregetted based on what Stack (buildpack) is being used to build and package the App. For example, if you want your applications built with `spaceStacksV2` to land on nodes with Linux kernel 4.4.1. `nodeSelector` values on a Stack will override the values configured on the Space.

To configure the `nodeSelector` on Stack.

  1. Edit the `config-defaults` of your Kf cluster and add the labels. 
         
         $ kubectl -n kf edit configmaps config-defaults
         

  2. Add `nodeSelector` to the stacks definition.
         
         .....
         .....
         spaceStacksV2: |
         - name:  cflinuxfs3
                 image: cloudfoundry/cflinuxfs3
                 nodeSelector:
                       OS_KERNEL: LINUX_4.4.1 
         .....
         .....
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
