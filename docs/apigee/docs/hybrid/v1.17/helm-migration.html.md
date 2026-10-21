---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/helm-migration.html
title: Migrate Apigee hybrid to Helm from apigeectl \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:01:49.158974+00:00
---

# Migrate Apigee hybrid to Helm from apigeectl  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/helm-migration.html

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)



Send feedback 

#  Migrate Apigee hybrid to Helm from apigeectl Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.17 (latest)keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/helm-migration.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/helm-migration.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/helm-migration.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/helm-migration.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/helm-migration.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/helm-migration.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/helm-migration.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/helm-migration.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/helm-migration.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/helm-migration.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/helm-migration.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/helm-migration.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/helm-migration.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/helm-migration.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/helm-migration.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/helm-migration.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/helm-migration.html)



This migration tool assists in migrating an `apigeectl`-based hybrid cluster to a Helm-based hybrid cluster. This tool performs no actual replacement of any cluster components. It is idempotent and can be run many times on the same cluster, preparing a subset of components and orgs each time. 

**Important:** This migration tool must be run _before_ running the Helm upgrade commands. 

There is a [known issue](https://docs.cloud.google.com/apigee/docs/release/known-issues) with the Helm migration tool in the hybrid v1.12 release. Until the issue is resolved, [Cassandra backup and restore](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-backup-overview) requires a workaround, see Troubleshooting for steps to install the workaround.

You can migrate all `apigee` components at one time, and Helm upgrade operations can be done on a per-component basis after the tool is run. 

See [Installing and managing Apigee hybrid with Helm charts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/helm-install) for information about managing hybrid clusters you have migrated to Helm management with this tool. 

## Prerequisites

  * Helm version v3.14.2+. 
  * A working `kubeconfig` file pointing to a cluster with a working Apigee hybrid 1.17 installation. 
  * Permissions to modify the metadata and annotations on the Kubernetes resources of the hybrid components that you wish to migrate. 



## Scope

This tool supports the following options at run-time:

  * Customization of namespace for `apigee` resources. Default namespace: `apigee`
  * Migration of selected hybrid components only. Default: all components are migrated 
  * Migration of a single org only
  * Migration of a single env only
  * Migration of a single env-group (`apigee-virtualhost`) only 
  * Customization of Helm release names for orgs, envs, and env-groups.



## Limitations

  * This tool does not support customizing Helm release names for these hybrid components: `apigee-operator`, `apigee-datastore`, `apigee-redis`, `apigee-telemetry`, and `apigee-ingress-manager`. 
  * Interactive customizations made to the Helm release names for orgs, envs, and env-groups do not automatically persist between runs. You can edit the temp file and supply it as an option in later runs. 
  * Env and env-group filtering is done by name only. In some cases this could result in multiple envs and env-groups being migrated on multi-org clusters. 

For example, on a multi-org cluster with orgs `org1` and `org2`, if the env `prod` is present in both orgs, and only `--env=prod` is specified, both envs will be migrated. If you wish to only migrate a single env, you must also specify an org filter `--org=org1` or `--org=org2`. 




## Usage

### Syntax
    
    
    apigee-helm-migration [--apigee-namespace=] [--components=] [--dry-run] [--env=org1] [--env-group=org2] [--org=baz] [--kubeconfig=] [-y] [-v] [-f /path/to/releaseNames.yaml]

### Generated Helm release names

Every Helm Chart that is deployed on a cluster needs to have a release name, which must be unique within a namespace. Helm release names don't have any naming convention or restriction relative to the chart name. The migration tool generates unique Helm release names for every component. 

Chart | Single-org cluster | Multi-org cluster  
---|---|---  
`apigee-operator` | `operator` | `operator`  
`apigee-datastore` | `datastore` | `datastore`  
`apigee-telemetry` | `telemetry` | `telemetry`  
`apigee-redis` | `redis` | `redis`  
`apigee-ingress-manager` | `ingress-manager` | `ingress-manager`  
`apigee-org` | `ORG_NAME` | `ORG_NAME`  
`apigee-env` | `ENV_NAME[-env[-n]](1)` | `ORG_NAME-ENV_NAME[-env[-n]]`(1)  
`apigee-virtualhost (envgroup)` | `VH_NAME[-env-group[-n]]`(1) | `ORG_NAME-VH_NAME[-env-group[-n]]`(1)  
(1) Names are suffixed with `-env` or `-env-group` if the generated name conflicts with another generated name. They are further suffixed with `-1` or `-2 …` if they still conflict.  
  
### Customizing Helm release names

The migration tool allows interactive customization of Helm release names. If you want to customize the Helm release names non-interactively: 

  1. Run the tool once and exit at the first prompt to create a temporary file containing the auto-generated release names. You should see a line like: 
         
         INFO: 21:32:56 using temp file for release names:  /tmp/apigee-helm-migration-1229129207-releaseNames

  2. Move or copy and then edit this file. You can pass this edited file in with the `-f` option when you run the migration tool. The auto-generated release names look like: 
         
         orgs:
           example-apigee-org:
             helmReleaseName: example-apigee-org
             envs:
               prod:
                 helmReleaseName: prod
             envGroups:
               prod-envgroup:
                 helmReleaseName: prod-envgroup

To customize the Helm release names for an org, env, or envgroup, edit the `helmReleaseName` field of that object. For example, to rename the org release to `custom-org`, the env release to `custom-env`, and the envgroup release to `custom-group`, the resulting file looks like: 
         
         orgs:
           example-apigee-org:
             helmReleaseName: custom-org
             envs:
               prod:
                 helmReleaseName: custom-env
             envGroups:
               prod-envgroup:
                 helmReleaseName: custom-group




### Using custom namespaces

Apigee hybrid v1.13 and newer runs in a single Kubernetes namespace. All hybrid components run in this namespace. `apigee` is the default name. You can use any custom namespace for these components.

If you use a custom namespace, you must specify the it with the `--apigee-namespace _my_custom_namespace_` flag when you run the Helm migration tool.

You must also add the `namespace: _my_custom_namespace_` top-level property to your overrides file.

### Directions

  1. Locate the migration tool.

The migration tool is packaged with `apigeectl` under `/tools/migration/`. 

  2. Extract the compressed files using one of the following commands:

     * **Mac:**
           
           tar -xzf apigee-helm-migration_1.0.2_mac_64.tar.gz

     * **Linux:**
           
           tar -xzf apigee-helm-migration_1.0.2_linux_64.tar.gz

     * **Windows:**
           
           tar -xzf apigee-helm-migration_1.0.2_windows_64.zip

  3. Run the migration tool. If the default options are acceptable, it is sufficient to run the tool without any arguments, and approve the prompt if the generated helm release names are satisfactory. Some example scenarios are given below: 
     * A simple installation, using the default `kubeconfig` (`~/.kube/config`), default `apigee` namespace, and default Helm release names. 

**The following command should be sufficient for most, if not all, installations.** Helm upgrade operations can be done on a per-component basis after the tool is run. 
           
           ./apigee-helm-migration
           

     * Migrating all components using a custom namespace: 
           
           ./apigee-helm-migration --apigee-namespace my_custom_namespace
           

     * Migrating only the `operator` and `datastore` components:
           
           ./apigee-helm-migration --components operator,datastore
           
           
           INFO: 00:22:48 using kubeconfig file  /usr/local/google/home/example/.kube/config
             INFO: 00:22:48 namespace for apigee resources:
             INFO: 00:22:48 	 apigee
             INFO: 00:22:48 processing all organizations in cluster
             INFO: 00:22:48 Components to migrate:
             INFO: 00:22:48 	 operator,datastore
             INFO: 00:22:48 dry-run:
             INFO: 00:22:48 	 false
             Continue with patching apigee resources for Helm migration? [y/n]: y
             INFO: 00:22:52 Processing component:  operator
             INFO: 00:22:54 Processing component:  datastore
             INFO: 00:22:55 Migration successful!

     * Pointing to a specific `kubeconfig` file and specifying a different name for the `apigee` namespace. 
           
           ./apigee-helm-migration --kubeconfig /abs/path/to/kubeconf --namespace org1_namespace
           

     * Migrating all components, but only a single org:
           
           ./apigee-helm-migration --org=some-test-org
           

The following shows an example output from a successful migration: 
    
    INFO: 21:32:55 using kubeconfig file  /usr/local/google/home/example/.kube/config
    INFO: 21:32:55 namespace for apigee resources:
    INFO: 21:32:55 	 apigee
    INFO: 21:32:55 processing all organizations in cluster
    INFO: 21:32:55 processing all components
    INFO: 21:32:55 dry-run:
    INFO: 21:32:55 	 false
    INFO: 21:32:55 cluster Apigee information:
    INFO: 21:32:55 Apigee Organizations found:
    INFO: 21:32:56 	 example-hybrid-dev
    INFO: 21:32:56 Apigee Environments found (org: env):
    INFO: 21:32:56 	 example-hybrid-dev : prod
    INFO: 21:32:56 Apigee EnvGroups(apigeerouteconfigs) found (org: envGroup):
    INFO: 21:32:56 	 example-hybrid-dev : prod-envgroup
    INFO: 21:32:56 using temp file for release names:  /tmp/apigee-helm-migration-1229129207-releaseNames
    INFO: 21:32:56 Helm release names for Apigee orgs/envs/envgroups:
    orgs:
    example-hybrid-dev:
    helmReleaseName: example-hybrid-dev
    envs:
      prod:
        helmReleaseName: prod
    envGroups:
      prod-envgroup:
        helmReleaseName: prod-envgroup
    Make changes to the release names for Apigee orgs/env/envgroups? [y/n]: n
    Continue with patching apigee resources for Helm migration? [y/n]: y
    INFO: 21:32:59 Processing component:  operator
    INFO: 21:33:01 Processing component:  datastore
    INFO: 21:33:01 Processing component:  redis
    INFO: 21:33:02 Processing component:  ingress-manager
    INFO: 21:33:02 Processing component:  telemetry
    INFO: 21:33:03 Processing component:  orgs
    INFO: 21:33:05 Processing component:  envs
    INFO: 21:33:06 Processing component:  env-groups
    INFO: 21:33:07 Migration successful!

Potential errors:

     * **Error parsing release names file:** Check the passed in release names file. 
     * **Resources not found:** Check that Apigee hybrid is fully installed, and you have permissions to access the `apigee` resources. 



### Configuration properties changes

Make the following changes in your overrides files:

  * Apigee hybrid managed with Helm uses `apigeeIngressGateway` properties to configure all Apigee ingress gateways in your cluster. `ingressGateways` properties override the settings in `apigeeIngressGateway` for the individual named ingress gateway. 

See [`apigeeIngressGateway`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#apigeeingressgateway)

    * Change any `ingressGateways` properties that are global to all ingress gateways in your cluster to `apigeeIngressGateway` properties. Your overrides file should contain at least: 
          
          apigeeIngressGateway:
            image:
              url: "PATH_TO_REPOSITORY/apigee-asm-ingress"
              tag: "TAG"
          

For example:
          
          apigeeIngressGateway:
            image:
              url: "gcr.io/apigee-release/hybrid/apigee-asm-ingress"
              tag: "1.17.1"
          

    * Make sure to include `ingressGateways.name`. It is required to instantiate your ingress gateway. For example: 
    
    ingressGateways:
      name: INGRESS_GATEWAY_NAME
    

  * The properties to enable Workload Identity have changed: 
    * `gcp.workloadIdentity.enabled` replaces `gcp.workloadIdentityEnabled`.
    * If you are using a single service account for all components, you can specify it with: `gcp.workloadIdentity.gsa`. For example: 
          
          gcp:
            workloadIdentity:
              enabled: true
              gsa: "apigee-non-prod@my-hybrid-project.iam.gserviceaccount.com"
          

    * If you are using a separate service account for each component (the standard for most prod installations), specify the service account with the component's `gsa` property. For example: 
          
          logger:
            gsa: "apigee-logger@my-hybrid-project.iam.gserviceaccount.com"
          

See: [`gcp.workloadIdentity.enabled`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#gcp-workloadidentity-enabled), [`gcp.federatedWorkloadIdentity.enabled`](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/config-prop-ref#gcp-federatedworkloadidentity-enabled), [Enabling Workload Identity on GKE](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enable-workload-identity-gke) or [Enabling Workload Identity Federation on AKS and EKS](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/enable-workload-identity-federation).




### Troubleshooting

There is a [known issue](https://docs.cloud.google.com/apigee/docs/release/known-issues) with the Helm migration tool in the hybrid v1.12 release. Until the issue is resolved, [Cassandra backup and restore](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/cassandra-backup-overview) requires additional steps.

You can follow these steps: 

  * Before or after running the migration tool
  * Before installing Helm charts



To install the patch for the workaround: 

  1. Make sure that your current `kubeconfig` is pointing to the cluster you want to migrate. You can can perform these steps from any directory.
  2. Create a file named `migration-operator-patch.yaml` with the following contents: 
         
         # migration-operator-patch.yaml
         metadata:
           annotations:
             meta.helm.sh/release-name: operator
             meta.helm.sh/release-namespace: APIGEE_NAMESPACE
           labels:
             app.kubernetes.io/managed-by: Helm

  3. Create a file called `migration-datastore-patch.yaml` with the following contents: 
         
         # migration-datastore-patch.yaml
         metadata:
           annotations:
             meta.helm.sh/release-name: datastore
             meta.helm.sh/release-namespace: apigee
           labels:
             app.kubernetes.io/managed-by: Helm

  4. Run the following `kubectl` commands: 
         
         kubectl patch clusterrole apigee-cassandra-backup --patch-file ./migration-operator-patch.yaml
         kubectl patch clusterrole apigee-cassandra-restore --patch-file ./migration-operator-patch.yaml
         kubectl patch clusterrolebinding apigee-cassandra-backup --patch-file ./migration-operator-patch.yaml
         kubectl patch clusterrolebinding apigee-cassandra-restore --patch-file ./migration-operator-patch.yaml
         kubectl patch -n APIGEE_NAMESPACE cronjob apigee-cassandra-backup --patch-file ./migration-datastore-patch.yaml
         kubectl patch -n APIGEE_NAMESPACE certificate apigee-cassandra-backup-tls --patch-file ./migration-datastore-patch.yaml --type merge
         kubectl patch -n APIGEE_NAMESPACE secret apigee-cassandra-backup-svc-account --patch-file ./migration-datastore-patch.yaml
         kubectl patch -n APIGEE_NAMESPACE secret apigee-cassandra-backup-key-file --patch-file ./migration-datastore-patch.yaml
         kubectl patch -n APIGEE_NAMESPACE ServiceAccount apigee-cassandra-backup-sa --patch-file ./migration-datastore-patch.yaml
         kubectl patch -n APIGEE_NAMESPACE job apigee-cassandra-restore --patch-file ./migration-datastore-patch.yaml
         kubectl patch -n APIGEE_NAMESPACE certificate apigee-cassandra-restore-tls --patch-file ./migration-datastore-patch.yaml --type merge
         kubectl patch -n APIGEE_NAMESPACE secret apigee-cassandra-restore-svc-account --patch-file ./migration-datastore-patch.yaml
         kubectl patch -n APIGEE_NAMESPACE secret apigee-cassandra-restore-key-file --patch-file ./migration-datastore-patch.yaml
         kubectl patch -n APIGEE_NAMESPACE ServiceAccount apigee-cassandra-restore-sa --patch-file ./migration-datastore-patch.yaml

**Note** : You can ignore any `not found` errors.
  5. Clean up the patch files using the following commands: 
         
         rm migration-operator-patch.yaml
         rm migration-datastore-patch.yaml




### Next step

Continue your installation of the Apigee hybrid Helm charts with the instructions in [Installing and managing Apigee hybrid with Helm charts](https://docs.cloud.google.com/apigee/docs/hybrid/preview/helm-install). 

**Important:** When following the instructions for your migrated cluster, you must omit the `‑‑atomic` flag from any Helm commands to avoid accidentally deleting resources if the `helm upgrade` command fails. 

## Output of -help
    
    
    ./apigee-helm-migration --help
    
    
    
    Usage of ./apigee-helm-migration:
      -apigee-namespace string
          namespace used for apigee resources (default "apigee")
      -components string
          CSV of components to migrate. If empty then all components are migrated. Valid values are: operator,datastore,redis,ingress-manager,telemetry,orgs,envs,env-groups
      -dry-run
          perform a dry-run
      -env string
          restrict migration to a singular supplied env. If empty then all envs detected in the cluster are migrated
      -env-group string
          restrict migration to a singular supplied envGroup. If empty then all envGroups detected in the cluster are migrated
      -kubeconfig string
          (optional) absolute path to the kubeconfig file (default "/usr/local/google/home/example/.kube/config")
      -org string
          restrict migration to a singular supplied org. If empty then all orgs detected in the cluster are migrated
      -v	Increased logging verbosity
      -y	don't prompt for confirmation or for configuration of Helm releases

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
