---
url: https://docs.cloud.google.com/service-mesh/legacy/anthos-service-mesh/managed-anthos-service-mesh/migrate-istio-operator/
title: Migrate from IstioOperator \u00a0|\u00a0 Cloud Service Mesh \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:40:13.873255+00:00
---

# Migrate from IstioOperator  |  Cloud Service Mesh  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/service-mesh/legacy/anthos-service-mesh/managed-anthos-service-mesh/migrate-istio-operator/

Anthos Service Mesh and Traffic Director are now Cloud Service Mesh. For more information, see the [Cloud Service Mesh overview](https://docs.cloud.google.com/service-mesh/docs/overview). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Service Mesh ](https://docs.cloud.google.com/service-mesh/docs)
  * [ Guides ](https://docs.cloud.google.com/service-mesh/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Migrate from IstioOperator

**Preview — Migration tool**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Caution:** In-cluster Cloud Service Mesh using the `ISTIOD` control plane on GKE on Google Cloud is [deprecated](https://docs.cloud.google.com/service-mesh/deprecations). Cloud Service Mesh with an in-cluster control plane on Google Distributed Cloud (software only) continues to be supported as described in [Supported platforms](https://docs.cloud.google.com/service-mesh/docs/supported-platforms#off-gcp). 

Managed control plane doesn't directly support `IstioOperator` for customization. Migrating to managed control plane from Cloud Service Mesh requires manually converting from an `IstioOperator`. This tool helps reduce the friction by automating that process.

## About the migration tool

The migration tool non-destructively evaluates the provided `IstioOperator` file to do the following:

  * Check for compatibility issues.
  * Convert compatible `IstioOperator` configurations to configuration supported by managed control plane, outputting the new configurations to files.
  * Output warnings about configuration values that would conflict with default values required by managed control plane.
  * Recommend how to use the generated files.



This tool does not examine cluster data or configurations nor does it make changes to a cluster configuration. You must separately apply all generated files.

Before using the migration tool, check the limitations on [managed control plane supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed) to verify that managed control plane supports your installation of Cloud Service Mesh.

## Using the migration tool

**Warning:** GitOps tools (including Config Sync, Argo CD, Terraform, and Jenkins) may interfere with your Cloud Service Mesh installation, migration, or upgrade processes. For best results, disable your GitOps tools before you install, migrate, or upgrade Cloud Service Mesh.

The migration tool is available as part of the `asmcli` script. You must [download the script](https://docs.cloud.google.com/service-mesh/docs/unified-install/get-started#download_asmcli) to use this tool.

  1. Run the migration tool:
         
         asmcli experimental mcp-migrate-check -f path/to/istiooperator.yaml
         

  2. Note the listed files output by the tool, specifically `asm/*meshconfig.yaml` and `asm/gateways*`.

  3. Examine configuration warnings.

  4. Review the output and follow the actions required to migrate.




## Unsupported MeshConfig fields

The following fields on MeshConfig are overridden by managed control plane.

**Note:** This list of fields is subject to change.

  * `trustDomain`
  * `trustDomainAliases`
  * `configSources`
  * `defaultConfig.proxyMetadata` \- These specific fields are overridden. You can add new fields: 
    * `XDS_ROOT_CA`
    * `CA_ROOT_CA`
    * `OUTPUT_CERTS`
    * `XDS_AUTH_PROVIDER`
    * `PROXY_CONFIG_XDS_AGENT`
  * `defaultConfig.meshId`
  * `defaultConfig.discoveryAddress`



## Example output
    
    
    $ asmcli experimental mcp-migrate-check -f some-iop.yaml
    asmcli: Downloading ASM..
    Generating equivalent configuration for Anthos Service Mesh managed control plane...
    
    Migrating MeshConfig settings...
    ✔ Wrote MeshConfig to asm-generated-configs/meshconfig.yaml.
    
    Migrating gateway deployments...
    
    Checking configuration compatibility...
    ! Found unsupported configurations:
        Components.Base: not configurable in managed control plane
        Components.Pilot: not configurable in managed control plane
        Hub=gcr.io/gke-release/asm: not configurable in managed control plane
        Tag=1.10.4-asm.6: not configurable in managed control plane
    
    Actions required to migrate:
    ! Found potentially unsupported configurations; review warnings above before proceeding
    - Found custom mesh configuration settings. To apply these settings to ASM managed
        control plane, run: `kubectl apply -f 'asm-generated-configs/meshconfig.yaml'`
    
    TIP: steps recommending `kubectl apply` to be run should be integrated into your
      CI/CD pipeline, if applicable.
    

## What's next

  * Learn more about [managed control plane supported features](https://docs.cloud.google.com/service-mesh/docs/supported-features-managed)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
