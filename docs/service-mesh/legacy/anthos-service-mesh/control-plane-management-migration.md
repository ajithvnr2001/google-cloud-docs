---
url: https://docs.cloud.google.com/service-mesh/legacy/anthos-service-mesh/control-plane-management-migration/
title: Migrate from controlPlaneManagement to management \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T08:36:39.239098+00:00
---

# Migrate from controlPlaneManagement to management  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/anthos-service-mesh/control-plane-management-migration/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate from controlPlaneManagement to management

The `controlPlaneManagement` setting for managing your service mesh control plane is deprecated. If you were previously using `controlPlaneManagement`, you must migrate to the `management` setting.

To check if you're using `controlPlaneManagement`, use the Feature State API:
    
    
      gcloud container fleet mesh describe
    

Any value for `controlPlane` under your membership spec indicates that you're using `controlPlaneManagement` and need to migrate to `management`.

## Differences between the controlPlaneManagement and management settings

The `management` setting enables additional automatic behaviors, compared to the `controlPlaneManagement` setting:

  * `management` automatically enables [managed data plane](https://docs.cloud.google.com/service-mesh/docs/onboarding/provision-control-plane#managed-data-plane).
  * `management` automatically enables [multi-cluster endpoint discovery](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/multi-cluster#configure_endpoint_discovery).



## Migration steps:

There are two possible scenarios depending on your setup. We'll outline the migration steps for each scenario.

### controlPlaneManagement is enabled and management is unset

Condition `DEPRECATED_SPEC_CONTROL_PLANE_MANAGEMENT` will be displayed through Feature State API. To migrate to `management`:

  1. [Enable automatic management](https://docs.cloud.google.com/service-mesh/docs/onboarding/provision-control-plane#configure) for the cluster, optionally disabling some capabilities. Run:
         
         gcloud container fleet mesh update \
             --management automatic \
             --memberships MEMBERSHIP_NAME \
             --project FLEET_PROJECT_ID \
             --location MEMBERSHIP_LOCATION
         

  2. Ensure you have the chosen configuration for multi-cluster endpoint discovery.

     * If you have multiple clusters, ensure you [enable prerequisites for endpoint discovery](https://docs.cloud.google.com/service-mesh/docs/onboarding/provision-control-plane#configure_endpoint_discovery_only_for_multi-cluster_installations), including ensuring firewall rules.
     * Alternately, follow the Disable instructions at [configure endpoint discovery](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/multi-cluster#configure_endpoint_discovery).
  3. Note that you have enabled the managed data plane.

     * Alternately, [disable data plane management](https://docs.cloud.google.com/service-mesh/docs/operate-and-maintain/managed-data-plane#disable_the_managed_data_plane_optional).
  4. Disable the no-longer-used controlPlaneManagement setting:
         
         gcloud container fleet mesh update \
               --control-plane unspecified \
               --memberships MEMBERSHIP_NAME \
               --project FLEET_PROJECT_ID \
               --location MEMBERSHIP_LOCATION
         




### Both the management and controlPlaneManagement settings are enabled

If you're already using the `management` setting, you might see the `DEPRECATED_SPEC_CONTROL_PLANE_MANAGEMENT_SAFE` condition displayed through the Feature State API. This indicates that the deprecated `controlPlaneManagement` setting is still present in your configuration even though it's no longer being used.

To remove this deprecated setting and ensure a clean configuration, run:
    
    
        gcloud container fleet mesh update \
          --control-plane unspecified \
          --memberships MEMBERSHIP_NAME \
          --project FLEET_PROJECT_ID \
          --location MEMBERSHIP_LOCATION
    

This will have no effect on your mesh's behavior, since the management setting already overrides the controlPlaneManagement setting.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
