---
url: https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/DevTools.Source.V1.SourceContext
title: Common Protos for Google Cloud APIs V1 Client - Class SourceContext (1.0.3) \u00a0|\u00a0 PHP client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:30.809613+00:00
---

# Common Protos for Google Cloud APIs V1 Client - Class SourceContext (1.0.3)  |  PHP client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/DevTools.Source.V1.SourceContext

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ PHP ](https://docs.cloud.google.com/php/docs)
  * [ Client libraries ](https://docs.cloud.google.com/php/docs/reference)



Send feedback 

#  Common Protos for Google Cloud APIs V1 Client - Class SourceContext (1.0.3) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.3 (latest)  1.0.0  0.8.3  0.7.0  0.6.0  0.5.2  0.4.2  0.3.8 

Reference documentation and code samples for the Common Protos for Google Cloud APIs V1 Client class SourceContext.

A SourceContext is a reference to a tree of files. A SourceContext together with a path point to a unique revision of a single file or directory.

Generated from protobuf message `google.devtools.source.v1.SourceContext`

## Namespace

Google \ Cloud \ DevTools \ Source \ V1

## Methods 

### __construct

Constructor.

**Parameters**  
---  
**Name** | **Description**  
`data` |  `array`   
Optional. Data for populating the Message object.  
`↳ cloud_repo` |  `[CloudRepoSourceContext](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/DevTools.Source.V1.CloudRepoSourceContext)`   
A SourceContext referring to a revision in a cloud repo.  
`↳ cloud_workspace` |  `[CloudWorkspaceSourceContext](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/DevTools.Source.V1.CloudWorkspaceSourceContext)`   
A SourceContext referring to a snapshot in a cloud workspace.  
`↳ gerrit` |  `[GerritSourceContext](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/DevTools.Source.V1.GerritSourceContext)`   
A SourceContext referring to a Gerrit project.  
`↳ git` |  `[GitSourceContext](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/DevTools.Source.V1.GitSourceContext)`   
A SourceContext referring to any third party Git repo (e.g. GitHub).  
  
### getCloudRepo

A SourceContext referring to a revision in a cloud repo.

**Returns**  
---  
**Type** | **Description**  
`[CloudRepoSourceContext](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/DevTools.Source.V1.CloudRepoSourceContext)|null` |   
  
### hasCloudRepo

### setCloudRepo

A SourceContext referring to a revision in a cloud repo.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[CloudRepoSourceContext](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/DevTools.Source.V1.CloudRepoSourceContext)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getCloudWorkspace

A SourceContext referring to a snapshot in a cloud workspace.

**Returns**  
---  
**Type** | **Description**  
`[CloudWorkspaceSourceContext](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/DevTools.Source.V1.CloudWorkspaceSourceContext)|null` |   
  
### hasCloudWorkspace

### setCloudWorkspace

A SourceContext referring to a snapshot in a cloud workspace.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[CloudWorkspaceSourceContext](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/DevTools.Source.V1.CloudWorkspaceSourceContext)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getGerrit

A SourceContext referring to a Gerrit project.

**Returns**  
---  
**Type** | **Description**  
`[GerritSourceContext](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/DevTools.Source.V1.GerritSourceContext)|null` |   
  
### hasGerrit

### setGerrit

A SourceContext referring to a Gerrit project.

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[GerritSourceContext](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/DevTools.Source.V1.GerritSourceContext)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getGit

A SourceContext referring to any third party Git repo (e.g. GitHub).

**Returns**  
---  
**Type** | **Description**  
`[GitSourceContext](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/DevTools.Source.V1.GitSourceContext)|null` |   
  
### hasGit

### setGit

A SourceContext referring to any third party Git repo (e.g. GitHub).

**Parameter**  
---  
**Name** | **Description**  
`var` |  `[GitSourceContext](https://docs.cloud.google.com/php/docs/reference/cloud-common-protos/latest/DevTools.Source.V1.GitSourceContext)`   
  
**Returns**  
---  
**Type** | **Description**  
`$this` |   
  
### getContext

**Returns**  
---  
**Type** | **Description**  
`string` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
