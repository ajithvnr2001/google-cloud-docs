---
url: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/ops-developer-platform-applications/
title: Operations for both the developer platform and applications \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:35:36.626072+00:00
---

# Operations for both the developer platform and applications  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/ops-developer-platform-applications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Operations for both the developer platform and applications Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-12-13 UTC

Operating a developer platform and containerized applications requires a number of different administrative tasks that you must conduct on an ongoing basis. Such tasks include, for example, creating new applications from a template, authorizing new developer groups to use the developer platform, planning capacity needs, and debugging run-time issues.

Operations can be automated or performed manually.

## Common automated operations

The blueprint provides automation for some of the most common tasks in the form of [webhook triggers](https://docs.cloud.google.com/build/docs/automate-builds-webhook-events?generation=2nd-gen), which are a simple type of API. Triggers are automatically connected to webhook events that come from one of the source control repositories. Developer platform developers can connect the other triggers. Typically, developer platform developers write a _developer portal_ , which can be a simple web form that calls a webhook trigger when a form is submitted.

The following table describes the common tasks that the blueprint automates using webhook triggers. The task frequencies are meant to be illustrative because the frequency of a task depends on many factors. Tasks don't necessarily recur at precise intervals.

Task | User | Description | Task frequency  
---|---|---|---  
Add a tenant. | Developer platform administrator | The administrator submits a form on the developer portal. The new tenant form fields include the tenant name and team members. An automated trigger creates the resources for the new tenant. | A few times each year  
Add an application based on an existing application template. | Application developer | The developer submits a form on the developer portal. The new application form fields include the tenant name, the application name, and the base application template. An automated trigger creates resources for a new application. | A few times each year  
Build and deploy source code changes for an application to the development environment. | Application developer | The developer edits the source code, runs and tests the code locally, and commits the code. The blueprint isn't involved in local developer workflows, but the Skaffold tool supports a [local builds](https://skaffold.dev/docs/builders/build-environments/local/) step. | A few times each day for each application  
Deploy YAML configuration changes for an application to the development environment. An example of YAML configuration change is to increase the CPU of a deployment resource. | Application developer | The developer edits the application configuration and commits the change. | A few times each week for each application  
Deploy application infrastructure changes to the development environment. The application infrastructure is the cloud resources in an application's project. An example change is an increase to the CPU count for an AlloyDB for PostgreSQL instance. | Application developer | The developer edits the application resource Terraform project and commits the change. The developer submits a form on the developer portal. An automated trigger starts the plan and apply pipeline. | Many times each year  
Promote application changes from development to non-production (or from non-production to production). Application changes can include new application images or application YAML configuration changes. | Application operator | The operator merges changes from the development branch to the non-production branch (or from the non-production branch to production branch). The operator supervises the rollout. | Several times each week for each application  
Promote application infrastructure changes from development to non-production (or from non-production to production). | Application operator | The operator merges select changes from the development branch to the non-production branch (or from the non-production branch to the production branch). The operator supervises rollout. | Several times each quarter for each application  
  
## Common manual operations

Some developer platform operations are less structured in nature, and don't use automation with a developer platform. You can develop your own playbooks based on this blueprint and perform these tasks in the Google Cloud console.

The following table describes these non-automated tasks. The task frequencies are meant to be illustrative because the frequency of a task depends on many factors. Tasks don't necessarily recur at precise intervals.

Task | User | Description | Task Frequency  
---|---|---|---  
Define a new application template. | Developer platform developer | The developer modifies an application template that is based on a blueprint template, or ports a template to a new language. | A few times each year  
Investigate service run-time errors in the development environment. | Application developer | The developer uses the Logs Explorer and [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer) in the Google Cloud console to review the error logs, monitoring metrics, and time series data for tenants and applications. | A few times each month  
Investigate service run-time errors in production or non-production environments. | Application operator | The operator uses the Logs Explorer and Metrics Explorer in the Google Cloud console to review the error logs, monitoring metrics, and time series data for tenants and applications. | A few times each month  
Investigate build errors. | Application developers | The developer views the [Cloud Build history](https://docs.cloud.google.com/build/docs/view-build-results), including build status and logs, in the Google Cloud console. | A few times each week  
Investigate deployment errors in the development environment | Application developers | The developer views the [Cloud Deploy release and rollout history](https://docs.cloud.google.com/deploy/docs/view-release) in the Google Cloud console for success status and logs from a deployment attempt, including any errors. | A few times each month  
Investigate deployment errors in the non-production and production environments | Application operators | The operator views the Cloud Deploy release and rollout history in the Google Cloud console for success status and logs from a deployment attempt, including error logs. | A few times each month  
Connect to clusters to debug GKE issues. | Developer platform administrator | The administrator uses the [Connect gateway](https://docs.cloud.google.com/anthos/multicluster-management/gateway) to connect to private clusters. For common issues, such as unscheduled pods, the administrator can review information about common issues (such as [unscheduled pods](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting#PodUnschedulable)) in the Google Cloud console. | A few times each month  
Plan capacity and optimize costs. | Developer platform administrator | The administrator reviews [GKE resource utilization](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-usage-metering), aggregated by scope or namespace, in the Google Cloud console. | Scheduled as a monthly recurring task.  
Resize, add, or remove node pools. | Developer platform administrator | The administrator edits the IaC as appropriate and redeploys the applications. | Done in response to capacity planning.  
Check security posture. | Developer platform administrator | The administrator checks for vulnerabilities and compliance to standards using the [GKE security posture dashboard](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-security-posture-dashboard). | Scheduled as a monthly recurring task.  
Upgrade cluster system software versions (for example, the Kubernetes version). | Developer platform administrator | The administrator uses the GKE maintenance windows and exclusions to allow upgrades only during planned times. The administrator uses the open upgrade window in the development environment first. After assessing the health of the upgrade, the administrator upgrades the non-production environment and then the production environment. | Scheduled as a quarterly recurring task.  
Install critical cluster security updates. | None | Automatic, done by GKE. | A few times each year  
Test regional failover. | Developer platform administrator and application administrator | The administrators schedule and manually initiate a regional failover of the environment as appropriate. | Yearly as part of disaster recovery exercises  
Add a [region](https://docs.cloud.google.com/docs/geography-and-regions#regions_and_zones). | Developer platform administrator, developer platform developer, and application administrator | The developer platform administrator deploys additional GKE clusters in the new region. The administrator updates the application template to add the new deployment step for relevant environments. The application operator then integrates the change to add deployment sequence to include the new region. | Very rarely  
Move to a new region. | Developer platform administrator, developer platform developer, and application administrator | The users add the new region as described in Add a region. After testing the new configuration, the users remove the old region. | Very rarely  
  
## What's next

  * Read about [managing costs and attributions for the developer platform](https://docs.cloud.google.com/architecture/blueprints/enterprise-application-blueprint/manage-costs-attributions) (next document in this series).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-12-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-12-13 UTC."],[],[]] 
