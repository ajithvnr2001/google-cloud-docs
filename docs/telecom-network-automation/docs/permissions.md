---
url: https://docs.cloud.google.com/telecom-network-automation/docs/permissions/
title: Architecture and permissions \u00a0|\u00a0 Telecom Network Automation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:53:45.011904+00:00
---

# Architecture and permissions  |  Telecom Network Automation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/telecom-network-automation/docs/permissions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Industry solutions ](https://docs.cloud.google.com/docs/industry)
  * [ Telecom Network Automation ](https://docs.cloud.google.com/telecom-network-automation/docs)
  * [ Guides ](https://docs.cloud.google.com/telecom-network-automation/docs/overview)



Send feedback 

#  Architecture and permissions Stay organized with collections  Save and categorize content based on your preferences. 

The Telecom Network Automation architecture is hierarchical, and consists of three tiers or stages.

## Telecom automation architecture

The Telecom Network Automation architecture consists of three stages that follow the end-to-end workflow of telecom automation:

### Stage 1: Package authoring

The following tasks are commonly done by network function vendors, network infrastructure vendors, service orchestration (SO) vendors, and system integrators:

  * **Create`kpt` packages**: Develop configuration packages and create initial blueprints by defining `kpt` packages, network functions (NFs) and the necessary infrastructure custom resource definitions (CRDs).
  * **Publish packages** : Distribute the configuration packages to designated repositories.
  * **Determine repository type** : Choose between making the package available within a closed, proprietary repository (accessible only to the organization) or within a public repository (accessible to a wider community).



### Stage 2: Network designing

The following tasks are commonly done by CSPs and SIs:

  * **Collect and customize original blueprints** : Customize the CRD and resources. Align the blueprints with their organization-specific configurations and policies.



### Stage 3 : Deploying

The following tasks are commonly done by CSPs and SIs:

  * **Clone and customize blueprints** : Consume and render variants of the configuration and approve the final config.
  * **Initiate deployments** : Telecom Network Automation reconciles these deployments to match the network with the intent the user provides.



![Automation workflow](https://docs.cloud.google.com/static/telecom-network-automation/docs/images/nephio_personas.png)

**Figure 1.** Telco cloud-native automation end-to-end journey (based on Nephio)

## Roles and permissions

This section lists the Identity and Access Management (IAM) permissions and roles for Telecom Network Automation.

### Roles

Role  | Permissions  
---|---  
Telco Automation Admin `roles/telcoautomation.admin` The Admin is a super user and has all the Telecom Network Automation permissions. Only the admin role has these permissions in predefined roles:

  * blueprint approve
  * Orchestration cluster resource permissions
  * Edge SLM resource permissions
  * LRO resource permissions

| 

  * telcoautomation.blueprints.approve
  * telcoautomation.blueprints.create
  * telcoautomation.blueprints.delete
  * telcoautomation.blueprints.get
  * telcoautomation.blueprints.list
  * telcoautomation.blueprints.propose
  * telcoautomation.blueprints.update
  * telcoautomation.deployments.apply
  * telcoautomation.deployments.computeStatus
  * telcoautomation.deployments.create
  * telcoautomation.deployments.delete
  * telcoautomation.deployments.get
  * telcoautomation.deployments.list
  * telcoautomation.deployments.rollback
  * telcoautomation.deployments.update
  * telcoautomation.edgeSlms.create
  * telcoautomation.edgeSlms.delete
  * telcoautomation.edgeSlms.get
  * telcoautomation.edgeSlms.list
  * telcoautomation.locations.get
  * telcoautomation.locations.list
  * telcoautomation.operations.cancel
  * telcoautomation.operations.delete
  * telcoautomation.operations.get
  * telcoautomation.operations.list
  * telcoautomation.orchestrationClusters.create
  * telcoautomation.orchestrationClusters.delete
  * telcoautomation.orchestrationClusters.get
  * telcoautomation.orchestrationClusters.list
  * telcoautomation.publicBlueprints.get
  * telcoautomation.publicBlueprints.list

  
Telco Automation Blueprint Designer `roles/telcoautomation.blueprintDesigner` Blueprint designers have the primary responsibility to create and manage blueprints. They have all the permissions for blueprint resources except approve, and read permissions for all other Telecom Network Automation resources. | 

  * telcoautomation.blueprints.create
  * telcoautomation.blueprints.delete
  * telcoautomation.blueprints.get
  * telcoautomation.blueprints.list
  * telcoautomation.blueprints.propose
  * telcoautomation.blueprints.update
  * telcoautomation.deployments.computeStatus
  * telcoautomation.deployments.get
  * telcoautomation.deployments.list
  * telcoautomation.orchestrationClusters.get
  * telcoautomation.orchestrationClusters.list
  * telcoautomation.publicBlueprints.get
  * telcoautomation.publicBlueprints.list

  
Telco Automation Deployment Admin `roles/telcoautomation.deploymentAdmin` Deployment Admin have the primary responsibility to manage the deployment resources. They have all the corresponding permissions, plus read permissions for other Telecom Network Automation resources. | 

  * telcoautomation.blueprints.get
  * telcoautomation.blueprints.list
  * telcoautomation.deployments.apply
  * telcoautomation.deployments.computeStatus
  * telcoautomation.deployments.create
  * telcoautomation.deployments.delete
  * telcoautomation.deployments.get
  * telcoautomation.deployments.list
  * telcoautomation.deployments.rollback
  * telcoautomation.deployments.update
  * telcoautomation.orchestrationClusters.get
  * telcoautomation.orchestrationClusters.list

  
Telco Automation Service Orchestrator `roles/telcoautomation.serviceOrchestrator` The Service Orchestrator role is for service accounts which call the Telecom Network Automation APIs to manage the deployment resources. | 

  * telcoautomation.blueprints.get
  * telcoautomation.blueprints.list
  * telcoautomation.deployments.apply
  * telcoautomation.deployments.computeStatus
  * telcoautomation.deployments.create
  * telcoautomation.deployments.delete
  * telcoautomation.deployments.get
  * telcoautomation.deployments.list
  * telcoautomation.deployments.rollback
  * telcoautomation.deployments.update
  * telcoautomation.orchestrationClusters.get
  * telcoautomation.orchestrationClusters.list

  
Telco Automation Tier 1 Operations Admin `roles/telcoautomation.opsAdminTier1` Tier 1 Operations Admin has read access for Telecom Network Automation resources like blueprints, deployments and orchestration cluster to monitor their states. | 

  * telcoautomation.blueprints.get
  * telcoautomation.blueprints.list
  * telcoautomation.deployments.computeStatus
  * telcoautomation.deployments.get
  * telcoautomation.deployments.list
  * telcoautomation.orchestrationClusters.get
  * telcoautomation.orchestrationClusters.list

  
Telco Automation Tier 4 Operations Admin `roles/telcoautomation.opsAdminTier4` Tier 4 Operations Admin has all the permissions of a Tier 1 admin plus all other permissions to manage deployment resources. | 

  * telcoautomation.blueprints.approve
  * telcoautomation.blueprints.create
  * telcoautomation.blueprints.delete
  * telcoautomation.blueprints.get
  * telcoautomation.blueprints.list
  * telcoautomation.blueprints.propose
  * telcoautomation.blueprints.update
  * telcoautomation.deployments.apply
  * telcoautomation.deployments.computeStatus
  * telcoautomation.deployments.create
  * telcoautomation.deployments.delete
  * telcoautomation.deployments.get
  * telcoautomation.deployments.list
  * telcoautomation.deployments.rollback
  * telcoautomation.deployments.update
  * telcoautomation.edgeSlms.create
  * telcoautomation.edgeSlms.delete
  * telcoautomation.edgeSlms.get
  * telcoautomation.edgeSlms.list
  * telcoautomation.locations.get
  * telcoautomation.locations.list
  * telcoautomation.operations.cancel
  * telcoautomation.operations.delete
  * telcoautomation.operations.get
  * telcoautomation.operations.list
  * telcoautomation.orchestrationClusters.create
  * telcoautomation.orchestrationClusters.delete
  * telcoautomation.orchestrationClusters.get
  * telcoautomation.orchestrationClusters
  * telcoautomation.publicBlueprints.get
  * telcoautomation.publicBlueprints.list

  
  
### Permissions

Permission  | Target  
---|---  
telcoautomation.blueprints.approve  |  Approve on the target blueprint resource  
telcoautomation.blueprints.create  |  Create on blueprint resource  
telcoautomation.blueprints.delete  |  Delete on the target blueprint resource   
telcoautomation.blueprints.get  |  Retrieve on the target blueprint resource  
telcoautomation.blueprints.list  |  Lists on the blueprint resources  
telcoautomation.blueprints.propose |  Propose on the target blueprint resource  
telcoautomation.blueprints.update |  Update on the target blueprint resource  
telcoautomation.deployments.apply |  Apply the target deployment resource  
telcoautomation.deployments.computeStatus |  Compute status on the target deployment resource  
telcoautomation.deployments.create |  Create on the target deployment resource  
telcoautomation.deployments.delete |  Delete on the target deployment resource  
telcoautomation.deployments.get |  Retrieve on the target deployment resource  
telcoautomation.deployments.list |  Lists on the target deployment resources  
telcoautomation.deployments.rollback |  Rollback on the target deployment resource  
telcoautomation.deployments.update |  Update on the target deployment resource  
telcoautomation.locations.get  |  Retrieve on the target telcoautomation location resource  
telcoautomation.locations.list |  Lists on the target telcoautomation locatio resources   
telcoautomation.operations.cancel |  Cancel on the target telcoautomation operation resource  
telcoautomation.operations.delete | Delete on the target telcoautomation operation resource  
telcoautomation.operations.get | Retrieve on the target telcoautomation operation resource  
telcoautomation.operations.list | Lists on the target telcoautomation operation resources  
telcoautomation.orchestrationClusters.create |  Create on the target orchestration cluster resource  
telcoautomation.orchestrationClusters.delete |  Delete on the target orchestration cluster resource  
telcoautomation.orchestrationClusters.get |  Retrieve on the target orchestration cluster resource  
telcoautomation.orchestrationClusters.list |  Lists on the target orchestration cluster resources  
telcoautomation.publicBlueprints.get |  Retrieve on the target public blueprint resource  
telcoautomation.publicBlueprints.list |  Lists on the target public blueprint resources  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
