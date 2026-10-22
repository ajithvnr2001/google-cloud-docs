---
url: https://docs.cloud.google.com/app-lifecycle-manager/overview/
title: App Lifecycle Manager overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:04.372613+00:00
---

# App Lifecycle Manager overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/overview/

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Guides ](https://docs.cloud.google.com/app-lifecycle-manager/overview)



Send feedback 

#  App Lifecycle Manager overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

App Lifecycle Manager (previously known as SaaS Runtime) lets you store, host, manage, and monitor software as a service (SaaS) applications on Google Cloud. App Lifecycle Manager manages Terraform deployments at scale, allowing you to manage both your SaaS application and the infrastructure that it runs on.

App Lifecycle Manager can be used in many ways by a variety of stakeholders within the SaaS pipeline. If your work identifies with any of these roles, you may be interested in using App Lifecycle Manager:

  * Platform administrator
  * Application developer
  * Architect
  * Compliance administrator
  * Platform engineer
  * Finance operations



App Lifecycle Manager provides the following benefits:

  * Simplify your service management at scale by automating service management tasks (such as deployment, rollouts, and feature flag management) across your SaaS tenants.
  * Expand your observability and control by fine tuning your updates and releases across configurable units to manage your App offering with precision at scale.
  * Build consistency across your Google Cloud ecosystem by managing services across various Google Cloud products including Google Cloud, Google Distributed Cloud, Billing, Observability, and Resource Manager.
  * Use flexible and templatizable architecture that promotes unit-based group updates and deployments for improved efficiency and reusability.



## How does App Lifecycle Manager work?

App Lifecycle Manager deploys artifacts that define your _App offering_. These artifacts must have a Terraform configuration. The deployment is organized into distinct _units_ that can be updated with _releases_ containing changes to your offering through a configurable rollout process.

For more information about App Lifecycle Manager nomenclature, see the [Glossary](https://docs.cloud.google.com/app-lifecycle-manager/glossary).

## Prepare your workload for App Lifecycle Manager

Before you deploy your App offering, we recommend that you determine the ideal arrangement of your App offering within the App Lifecycle Manager ecosystem.

Organize parts of your App offering that should be updated or modified together into distinct Terraform configurations. As you plan your App offering, use _unit kinds_ for each grouping of your App offering.

Once you've worked out the ideal structure for your workload on App Lifecycle Manager, you can create your App offering, unit kinds, and then deploy your units using a rollout.

For an example of the setup for App Lifecycle Manager, see the [quickstart](https://docs.cloud.google.com/app-lifecycle-manager/deploy-sql).

## Use composite templates with App Lifecycle Manager

You can use [composite templates](https://docs.cloud.google.com/application-design-center/docs/design-composite-templates#create_a_composite_application_template) through Application Design Center to define the infrastructure of your App Lifecycle Manager application offerings.

Once you attach a composite template to your App offering, App Lifecycle Manager will populate the unit kinds defined in your template. This lets you deploy units based on the structure and resources defined in your composite template.

You can edit your composite templates in App Design Center, and see the changes reflected in your App Lifecycle Manager App offerings.

For more information about composite templates, see [Design composite templates](https://docs.cloud.google.com/application-design-center/docs/design-composite-templates) documentation. For more information about attaching composite templates to App Lifecycle Manager offerings, see [Model and package units of deployment](https://docs.cloud.google.com/app-lifecycle-manager/model-saas-offering).

## App Lifecycle Manager service accounts

App Lifecycle Manager uses a combination of Google-managed and user-managed service accounts:

  * _App Lifecycle Manager service account (Google-managed)_ : This account is automatically created after creating the first App offering resource. It is managed by Google. It performs actions on your behalf, such as interacting with other Google Cloud services during unit provisioning.

  * _Actuation service account (User-managed)_ : You create and manage this service account. App Lifecycle Manager (via Infrastructure Manager) uses this account to execute your Terraform configurations when provisioning or updating units. This account acts as the identity for creating and managing the resources defined in your Terraform. The actuation service account permissions are directly tied to the resources your Terraform configuration manages.

You can have multiple actuation service accounts. We recommend that you should have one actuation service account for each tenant.

  * _Optional: Artifact creation service account (User-managed)_ : This service account is used for building and uploading your Terraform packaged into OCI artifacts. This is often a Cloud Build service account, but it can be any service account with appropriate permissions for your App offering.


**Caution:** Careful management of these service accounts is crucial for the security and proper functioning of your App Lifecycle Manager deployment. You should always follow the principle of least privilege, and grant only the necessary permissions to each service account.

### App Lifecycle Manager service account (Google-managed)

The _App Lifecycle Manager service account_ is a Google-managed [service agent](https://docs.cloud.google.com/iam/docs/service-accounts#service-agents) used by App Lifecycle Manager to perform operations within your project.

This service account is automatically provisioned when you create your first App Lifecycle Manager resource. The App Lifecycle Manager service account is created using this format:
    
    
      service-PROJECT_NUMBER@gcp-sa-saasservicemgmt.iam.gserviceaccount.com
    

Replace:

  * PROJECT_NUMBER: Your project number.

**Note:** You can find your project number in the Google Cloud console on the [Dashboard page](https://console.cloud.google.com/).

### Actuation service account (User-managed)

The _actuation service account_ is a user-managed service account that you must create. App Lifecycle Manager (via Infra Manager) uses this service account to execute your Terraform configurations. It's the identity that creates, modifies, and deletes the resources defined in your Terraform.

You are responsible for creating this service account within your project, or within your tenant project.

#### Actuation service account input variables

When you create a unit, you must provide the actuation service account as an key-value pair input variable for the Terraform configuration:

  * **Name** : `actuation_sa`
  * **Variable type** : `String`
  * **Variable value** : Actuation service account email address:
        
        my-actuation-sa@my-identifier.iam.gserviceaccount.com
        




#### Required Permissions

The _actuation service account_ requires sufficient permissions to manage the resources defined in your Terraform configuration. At a minimum, it needs:

  * `roles/iam.serviceAccountTokenCreator`: Allows the service account to generate tokens for authentication.
  * `roles/config.admin`: Grants full control over Infra Manager resources.
  * `roles/storage.admin`: Grants full control of Cloud Storage.



The actuation service account also needs permissions to create and manage the specific Google Cloud resources used by your application.

For example:

  * If your Terraform creates Google Kubernetes Engine (GKE) clusters, the service account needs appropriate GKE roles (`roles/container.admin`, for example).
  * If your Terraform creates Compute Engine instances, the service account needs the `roles/compute.admin` role.
  * If your Terraform creates Cloud SQL instances, the service account needs the appropriate Cloud SQL roles (`roles/cloudsql.admin`, for example).



Consult the documentation for each Google Cloud resource you use in your Terraform to determine the necessary permissions. Grant the _least privilege_ necessary for your application to function.

**Note:** It's best practice to create a dedicated actuation service account for each tenant (unit) to isolate and limit the severity of potential issues.

### Artifact creation service account (User-managed)

The _artifact creation service account_ is a user-managed service account you create to use a build system (such as Cloud Build) to package and upload your Terraform artifacts to Artifact Registry.

This service account is separate from the App Lifecycle Manager and actuation service accounts, and builds your Terraform code and pushes the resulting artifact to Artifact Registry. Often, this is the Cloud Build service account.

#### Manual artifact creation

If you manually build and upload your Terraform artifacts (using Docker build and Docker push directly, for example), you don't need a separate artifact creation service account.

Instead, you should authenticate using your own credentials or a service account with the necessary Artifact Registry permissions.

#### Required Permissions

If you are using Cloud Build, the Cloud Build service account typically needs the following roles:

  * `roles/artifactregistry.writer`: To push artifacts to Artifact Registry.
  * `roles/artifactregistry.repoAdmin`: To manage the Artifact Registry repository.
  * `roles/storage.admin`: To manage the Cloud Storage buckets.
  * `roles/developerconnect.admin`: Permissions to use Developer Connect.
  * `roles/developerconnect.readTokenAccessor`: Permissions to get Developer Connect read token.
  * `roles/logging.logWriter`: Permissions to write logs.
  * If you are deploying your Terraform configuration using Developer Connect: `roles/cloudbuild.builds.builder`: To execute builds.
  * Any other permissions required by your build process (for example, access to source code repositories).



## Rollout strategies

App Lifecycle Manager employs several rollout strategies to manage how units in your App offering are updated. These rollout strategies follow [Google Cloud's approach to change](https://docs.cloud.google.com/docs/cloud-approach-to-change#safe-rollouts) by applying consistent approaches to the deployment of changes across your App offering.

Use rollout strategies to minimize negative customer impacts and isolate issues to individual logical and physical failure domains. Define your rollout strategies by creating a rollout kind specifying one of the following rollout strategies:

  * **One location at a time (simple)** : One location rolls out at a time, with no wait in-between locations. Units are selected arbitrarily within a location, with a maximum of 5% of the location's units updated at a given time.

This strategy is recommended for development environments and emergency scenarios.

  * **All at once (simple)** : All locations begin rolling out at the same time.

This strategy is recommended for development environments and emergency scenarios.

  * **Progressive (gradual)** : Within each location, units are rolled out in static percentage-based batches (for example, 1%, 10%, 20%, 30%, ~40%) with soak times between batches. Across locations, the rollout progresses with an exponential increase in the number of concurrent locations (for example, one location, then two, then four) with soak times (18 hours, for example) between waves. Units within a location are selected randomly. 

This strategy is designed for safe and predictable rollouts across multiple locations. It starts with a small footprint and gradually expands as confidence grows. This strategy is recommended in production environments with _more than one location_.

  * **Progressive (single location)** : Units are updated in static percentage-based batches (for example, 1%, 10%, 20%, 30%, ~40%) with longer soak times (18 hours, for example) between batches to allow ample time for issue detection and to limit the adverse impact of rollout changes.

This strategy is tailored for App offerings operating in a single location, prioritizing safety and caution. We recommend this strategy in production environments with _one location_.




For more information about creating rollout kinds, see [Create a rollout kind](https://docs.cloud.google.com/app-lifecycle-manager/update-saas-offering#create_a_rollout_kind).

## App Lifecycle Manager regionalization

_App offering_ resources define where your App Lifecycle Manager units can reside, and how your rollouts are managed. When you create an App offering, the regions you select serve as a single source of truth for the supported regions of your App offering. The regions you select are the _available regions_ you've defined for your App offering.

When you use App Lifecycle Manager through Google Cloud console, App Lifecycle Manager automates the replication of the resources you define in your App offering across regions. This ensures consistency and availability of your App Lifecycle Manager resources across all of the available regions you've defined in your App offering.

**Caution:** Resource replication _isn't automated_ if you create or update App Lifecycle Manager using Google Cloud CLI. If you want to sync create or update operations across regions, use Google Cloud console.

App Lifecycle Manager replicates these resources:

  * App offering (`Saas`)
  * Unit kind (`UnitKind`)
  * Release (`Release`)



### Using `global` as a region

Including `global` as a region within your App offering is generally _not recommended_ for deployment targets. App Lifecycle Manager uses the `global` region to propagate regional rollouts. Regional rollouts cannot run in the `global` region.

### Rollout regionalization

Supported locations for rollouts are determined by the top-level regions defined in your App offering's available regions.

Rollouts read the list of available regions from the associated App offering.

### Resource replication

App Lifecycle Manager handles the creation and updates of resources to all of your App offering's available regions.

When you update your App offering's available regions, the App Lifecycle Manager handles the replication:

  * **Locations added:** Resources are replicated to the newly added locations.
  * **Locations with old copies:** The content is updated.



### Artifact Registry and Developer Connect locations

The locations of your Artifact Registry repository and Developer Connect instance have specific requirements:

  * The region of your Artifact Registry repository and Developer Connect instance can be _any_ valid Google Cloud region. They don't need to be included in your App offering's available regions.

  * The region of your Artifact Registry repository _must_ match the region of your Developer Connect instance.

This necessitates the presence of App offering, release, and unit kind resources in all regions defined in your App offering, even though the Artifact Registry and Developer Connect reside in a single (potentially different) region.

  * Units can only be created in regions specified in your App offering.

**Note:** Units _aren't_ propagated to the `global` region.



### App Lifecycle Manager regions configuration example

We have provided this example to demonstrate how regionalization works when using App Lifecycle Manager with managed resource replication.

For example, if you wanted to deploy your App offering in `us-central1` and `europe-west4`, while hosting your Artifact Registry repository and Developer Connect instance in `us-east1`, your App Lifecycle Manager regions infrastructure would be something like:

  * **App offering available regions:** `['us-central1', 'europe-west4']`
  * **Artifact Registry repository** region: `us-east1`
  * **Developer Connect instance** region: `us-east1`
  * **Unit kind, and release** resources: App Lifecycle Manager manages the creation and updates of these resources across `global`, `us-central1`, and `europe-west4` regions
  * **Units:** Units could be created in either `us-central1`, or `europe-west4`



This configuration lets you manage your deployments across two regions while keeping your artifact management centralized in a third, distinct region with automated resource replication. You should consider your latency, compliance, and data residency requirements carefully when selecting your regions.

## What's next

  * Try the [quickstart](https://docs.cloud.google.com/app-lifecycle-manager/deploy-sql) to learn how to deploy a VM using App Lifecycle Manager.
  * To get started with App Lifecycle Manager, begin with [Create an App offering](https://docs.cloud.google.com/app-lifecycle-manager/create-saas-offering).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
