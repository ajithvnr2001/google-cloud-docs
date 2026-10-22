---
url: https://docs.cloud.google.com/migrate/kf/docs/2.1/reference/cluster-configuration/
title: Cluster Configuration \u00a0|\u00a0 Kf 2.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:30:58.741431+00:00
---

# Cluster Configuration  |  Kf 2.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/kf/docs/2.1/reference/cluster-configuration/

Version 2.1

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
  * [ 2.1 ](https://docs.cloud.google.com/migrate/kf/docs/2.1)
  * [ Reference ](https://docs.cloud.google.com/migrate/kf/docs/2.1/reference)



Send feedback 

#  Cluster Configuration Stay organized with collections  Save and categorize content based on your preferences. 

Kf uses a Kubernetes configmap named `config-defaults` in the `kf` namespace to store cluster wide configuration settings. This document explains its structure and fields.

## Structure of the config-defaults configmap

The configmap contains three types of key/value pairs in the `.data` field:

  * Comment keys prefixed by `_` contain examples, notes, and warnings.
  * String keys contain plain text values.
  * Object keys contain a JSON or YAML value that has been encoded as a string.



Example:
    
    
    _note: "This is some note"
    stringKey: "This is a string key that's not encoded as JSON or YAML."
    objectKey: |
      - "These keys contain nested YAML or JSON."
      - true
      - 123.45
    

**Note:** Kubernetes requires all configmap values to be strings. Kf validates the structure of the fields before the object is updated.

## Example section

The example section under the `_example` key contains explanations for other fields and examples. Changes to this section have no effect.

## Space container registry

The `spaceContainerRegistry` property is a plain text value that specifies the default container registry each space uses to store built images.

Example:
    
    
    spaceContainerRegistry: gcr.io/my-project
    

## Space cluster domains

The `spaceClusterDomains` property is a string encoded YAML array of domain objects.

Each space in the cluster adds all items in the array to its list of domains that developers can bind their apps to.

Fields  
---  
`domain` |  `string` The domain name to make available. May contain one of the following substitutions:

  * `$(SPACE_NAME)` \- Replaced in each space with the name of the space.
  * `$(CLUSTER_INGRESS_IP)` \- The IP address of the cluster ingress gateway.

  
`gatewayName` |  `string` (Optional) Overrides the Istio gateway routes will be bound to. Defaults to `kf/external-gateway`, but any other gateway in the `kf` namespace may be used.   
**Note:** All domains should contain the `$(SPACE_NAME)` substitution to prevent Apps in different namespaces from listening to the same hostname which causes undefined behavior.

Example:
    
    
    spaceClusterDomains: |
      # Support canonical and vanity domains
      - domain: $(SPACE_NAME).prod.example.com
      - domain: $(SPACE_NAME).kf.us-east1.prod.example.com
    
      # Using a dynamic DNS resolver
      - domain: $(SPACE_NAME).$(CLUSTER_INGRESS_IP).nip.io
    
      # Creating an internal domain only visible within the cluster
      - domain: $(SPACE_NAME)-apps.internal
        gatewayName: kf/internal-gateway
    

## Buildpacks V2 lifecycle builder

The `buildpacksV2LifecycleBuilder` property contains the version of the Cloud Foundry `builder` binary used execute buildpack v2 builds.

The value is a Git reference. To use a specific version, append an `@` symbol followed by a Git SHA to the end.

Example:
    
    
    buildpacksV2LifecycleBuilder: "code.cloudfoundry.org/buildpackapplifecycle/builder@GIT_SHA"
    

## Buildpacks V2 lifecycle launcher

The `buildpacksV2LifecycleLauncher` property contains the version of the Cloud Foundry `launcher` binary built into every buildpack V2 application.

The value is a Git reference. To use a specific version, append an `@` symbol followed by a Git SHA to the end.

Example:
    
    
    buildpacksV2LifecycleLauncher: "code.cloudfoundry.org/buildpackapplifecycle/launcher@GIT_SHA"
    

## Buildpacks V2 list

The `spaceBuildpacksV2` property is a string encoded YAML array that holds an ordered list of default buildpacks that are used to build applications compatible with the V2 buildpacks process.

Fields  
---  
`name` |  `string` A short name developers can use to reference the buildpack by in their application manifests.  
`url` |  `string` The URL used to fetch the buildpack.  
`disabled` |  `boolean` Used to prevent this buildpack from executing.  
  
## Stacks V2 list

The `spaceBuildpacksV2` property is a string encoded YAML array that holds an ordered list of stacks that can be used with Cloud Foundry compatible builds.

Fields  
---  
`name` |  `string` A short name developers can use to reference the stack by in their application manifests.  
`image` |  `string` URL of the container image to use as the stack. For more information, see <https://kubernetes.io/docs/concepts/containers/images>.   
**Note:** Use images tagged with SHAs to improve caching.

## Stacks V3 list

The `spaceStacksV3` property is a string encoded YAML array that holds an ordered list of stacks that can be used with [Cloud Native Buildpack](https://buildpacks.io/) builds.

Fields  
---  
`name` |  `string` A short name developers can use to reference the stack by in their application manifests.  
`description` |  `string` A short description of the stack shown when running `kf stacks`.  
`buildImage` |  `string` URL of the container image to use as the builder. For more information, see <https://kubernetes.io/docs/concepts/containers/images>.   
`runImage` |  `string` URL of the container image to use as the base for all apps built with . For more information, see <https://kubernetes.io/docs/concepts/containers/images>.   
`nodeSelector` |  `map (key: string, value: string)` (Optional) A NodeSelector used to indicate which nodes applications built with this stack can run on.   
**Note:** Use images tagged with SHAs to improve caching.

Example:
    
    
    spaceStacksV3: |
      - name: heroku-18
        description: The official Heroku stack based on Ubuntu 18.04
        buildImage: heroku/pack:18-build
        runImage: heroku/pack:18
        nodeSelector:
           kubernetes.io/os: windows
    

## Default to V3 Stack

The `spaceDefaultToV3Stack` property contains a quoted value `true` or `false` indicating whether spaces should use V3 stacks if a user doesn't specify one.

## Feature flags

The `featureFlags` property contains a string encoded YAML map of feature flags that can enable and disable features of Kf.

Flag names that aren't supported by Kf will be ignored.

Flag Name | Default | Purpose  
---|---|---  
`disable_custom_builds` | `false` | Disable developer access to arbitrary Tekton build pipelines.  
`enable_dockerfile_builds` | `true` | Allow developers to build source code from dockerfiles.  
`enable_custom_buildpacks` | `true` | Allow developers to specify external buildpacks in their applications.  
`enable_custom_stacks` | `true` | Allow developers to specify custom stacks in their applications.  
  
Example:
    
    
    featureFlags: |
      disable_custom_builds: false
      enable_dockerfile_builds: true
      enable_some_feature: true
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
