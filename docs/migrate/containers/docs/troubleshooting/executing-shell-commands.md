---
url: https://docs.cloud.google.com/migrate/containers/docs/troubleshooting/executing-shell-commands/
title: Executing shell commands on your container \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:25.769173+00:00
---

# Executing shell commands on your container  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/troubleshooting/executing-shell-commands/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Executing shell commands on your container

To troubleshoot some isses, you might have to access the container to execute commands directly on the container itself. You can access a container through a `bash` shell or through PowerShell using the [ `kubectl exec` command. ](https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#exec)

**Note:** In the examples below, for PowerShell replace `/bin/bash` with `cmd.exe`, `powershell.exe`, or `pwsh.exe` depending on your version.

  1. Use `kubectl describe pods` to find the name of the Pod in your cluster that you want to connect to. 

In the following example, the command lists the suitecrm-0 pod.
         
         kubectl describe pods | grep Name
         
         Name:               suitecrm-0

  2. Execute shell commands using one of the following methods: 
     * Use `kubectl exec` to open a bash command shell where you can execute commands. 
           
           kubectl exec -it pod-name -- /bin/bash

The following example gets a shell to the suitecrm-0 pod:
           
           kubectl exec -it suitecrm-0 -- /bin/bash

     * Use `kubectl exec` to execute commands directly. 
           
           kubectl exec -it pod-name -- /bin/bash -c "command(s)"

The following example lists the root directory of the suitecrm-0 pod:
           
           kubectl exec -it suitecrm-0 -- /bin/bash -c "ls /"




For more information, see the [ Kubernetes documentation](https://kubernetes.io/docs/tasks/debug-application-cluster/get-shell-running-container/). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
