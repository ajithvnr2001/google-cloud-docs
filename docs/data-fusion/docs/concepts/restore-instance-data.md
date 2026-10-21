---
url: https://docs.cloud.google.com/data-fusion/docs/concepts/restore-instance-data/
title: Back up and restore instance data \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:24:19.659100+00:00
---

# Back up and restore instance data  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/concepts/restore-instance-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Guides ](https://docs.cloud.google.com/data-fusion/docs/create-data-pipeline)



Send feedback 

#  Back up and restore instance data Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Data Fusion backup and recovery APIs let you save and restore your instance resources, including pipelines, plugins, and configurations. This helps protect critical workloads against accidental loss and prepares your environment for disaster recovery.

## Supported backup and recovery

You can back up and restore the following types of information using the Cloud Data Fusion REST API.

**Important:** To fully restore data pipelines, you must recover all of the dependent information in the following table.

Recommended: To restore the pipelines, [import the pipelines](https://docs.cloud.google.com/data-fusion/docs/how-to/exporting-pipelines#import) from the Cloud Data Fusion UI, which lets you adjust the version number in the pipeline JSON. Deployment through the API requires a proper JSON adoption.

Types of information | Backup API | Restore API  
---|---|---  
Plugins | [List artifacts](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477692148/Artifact+Microservices#List-Available-Artifacts)  
You can get a list of deployed artifacts, but not artifact archives. | [Deploy an artifact](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+Microservices#Deploy-an-Artifact-and-Application)  
Pipelines | [Export a single pipeline's details](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+Microservices#Details-of-an-Application)  
[Export all application details](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+Microservices#Export-All-Application-Details) | [Deploy an application](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+Microservices#Deploy-an-Artifact-and-Application)  
This API requires application JSON adoption.  
[Import a pipeline through UI](https://docs.cloud.google.com/data-fusion/docs/how-to/exporting-pipelines#import)  
Compute profiles | [List profiles](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477593901/Profile+Microservices#List-Profiles) | [Write a profile](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477593901/Profile+Microservices#Write-a-Profile)  
Schedules | [List schedules](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+Microservices#List-Schedules) | [Add a schedule](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477560983/Lifecycle+Microservices#Add-a-Schedule)  
Connections | [List connections](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/975929350/Pipeline+Microservices#List-Connection) | [Create a connection](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/975929350/Pipeline+Microservices#Create-a-Connection)  
Secure keys | [List all secure keys](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477790661/Security+Microservices#List-all-Secure-Keys)  
[Retrieve a secure key](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477790661/Security+Microservices#Retrieve-a-Secure-Key) | [Create a secure key](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477790661/Security+Microservices#Create-a-Secure-Key)  
Preferences | [Get preferences](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561058/Preferences+Microservices#Get-Preferences) | [Set preferences](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/477561058/Preferences+Microservices#Set-Preferences)  
Pipeline drafts | [List draft pipelines](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/975929350/Pipeline+Microservices#List-Draft-Pipelines)  
[Details of a draft pipeline](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/975929350/Pipeline+Microservices#Details-of-a-Draft-Pipeline) | [Create a draft pipeline](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/975929350/Pipeline+Microservices#Create-or-Update-a-Draft-Pipeline)  
Replication job drafts | [List replication job drafts](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1765507073/Replication+Microservices#Draft-Replication-Jobs)  
[Details of a replication job draft](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1765507073/Replication+Microservices#Details-of-a-Replication-Job-Draft) | [Create a replication job draft](https://cdap.atlassian.net/wiki/spaces/DOCS/pages/1765507073/Replication+Microservices#Create-or-Update-a-Draft-Replication-Job)  
  
## Unsupported backup and recovery

Operational history about runs, such as run records, logs, metrics, or lineage, cannot be restored.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
