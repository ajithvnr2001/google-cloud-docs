---
url: https://docs.cloud.google.com/migrate/kf/docs/2.10/how-to/compute-isolation/
title: Enable compute isolation \u00a0|\u00a0 Kf 2.8 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:43:38.552692+00:00
---

# Enable compute isolation  |  Kf 2.8  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.10/how-to/compute-isolation/

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



Send feedback 

#  Enable compute isolation Stay organized with collections  Save and categorize content based on your preferences. 

Kf Apps can be deployed on dedicated nodes in the cluster. This feature is required if you have the circumstances where you might want more control on a node where an App Pod lands. For example:

  * If you are sharing the same cluster for different Apps but want dedicated nodes for a particular App.
  * If you want dedicated nodes for a given organization (Kf Space).
  * If you want to target a specific operating system like Windows.
  * If you want to co-locate Pods from two different services that frequently communicate.



To enable compute isolation, Kf uses the Kubernetes [nodeSelector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node). To use this feature, first add labels on the nodes or node pools where you want your App Pods to land and then add the same qualifying labels on the Kf Space. All the Apps installed in this Space then land on the nodes with matching labels.

Kf creates a Kubernetes pod to execute each Kf Build, the buildNodeSelector feature can be used to isolate compute resources to execute only the Build pods. One use case is to isolate Build pods to run on nodes with SSD, while running the App pods on other nodes. The BuildNodeSelectors feature provides compute resource optimization and flexibility in the cluster. Please refer to chapter 'Configure BuildNodeSelectors and a build node pool' on this page.

## Configure nodeSelector in a Kf cluster

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




## Override nodeSelector for [Kf stacks](https://docs.cloud.google.com/migrate/kf/docs/2.8/cli/kf-stacks)

Deployment of Kf Apps can be further targeted based on what stack (buildpack) is being used to build and package the App. For example, if you want your applications built with `spaceStacksV2` to land on nodes with Linux kernel 4.4.1., `nodeSelector` values on a stack override the values configured on the Space.

To configure the `nodeSelector` on a stack:

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
         




## Configure BuildNodeSelectors and a Build node pool

Build node selectors are only effective at overriding the node selectors for the Build pods, they do not affect App pods. For example, if you specify both the node selectors on the Space and the Build node selectors in Kfsystem, App pods will have the Space node selectors while the Build pods will have the Build node selectors from Kfsystem; if node selectors are only specified in the Space, both the App and Build pods will have the node selector from the Space.

  1. Add labels (`disktype:ssd` for example) on the nodes that you want your Build pods to be assigned to.
         
         kubectl label nodes nodeid disktype=ssd

  2. Add/update Build node selectors (in the format of `key:value` pairs) by patching KfSystem CR.
         
         kubectl patch kfsystem kfsystem --type='json' -p='[{'op': 'replace', 'path': '/spec/kf/config/buildNodeSelectors', 'value': {<key>:<value>}}]'

For example, to add `disktype=ssd` as the Build node selector:
         
         kubectl patch kfsystem kfsystem --type='json' -p='[{'op': 'replace', 'path': '/spec/kf/config/buildNodeSelectors', 'value': {"disktype":"ssd"}}]'




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
