---
url: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/multi-org/
title: Adding multiple hybrid orgs to a cluster \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:21:13.970910+00:00
---

# Adding multiple hybrid orgs to a cluster  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/multi-org/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Adding multiple hybrid orgs to a cluster Stay organized with collections  Save and categorize content based on your preferences. 

You are currently viewing version 1.15 of the Apigee hybrid documentation. For more information, see [Supported versions](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions).

Version 1.15 keyboard_arrow_down

Supported versions:

  * [ v1.17 (latest) ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.17/multi-org.html)
  * [ v1.16 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.16/multi-org.html)
  * [ v1.15 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/multi-org.html)
  * [ v1.14 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.14/multi-org.html)
  * [ List of supported versions ](https://docs.cloud.google.com/apigee/docs/hybrid/supported-platforms#supported-versions)

Unsupported versions:

  * [ v1.13 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.13/multi-org.html)
  * [ v1.12 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/multi-org.html)
  * [ v1.11 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.11/multi-org.html)
  * [ v1.10 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.10/multi-org.html)
  * [ v1.9 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.9/multi-org.html)
  * [ v1.8 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.8/multi-org.html)
  * [ v1.7 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.7/multi-org.html)
  * [ v1.6 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.6/multi-org.html)
  * [ v1.5 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.5/multi-org.html)
  * [ v1.4 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.4/multi-org.html)
  * [ v1.3 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/multi-org.html)
  * [ v1.2 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.2/multi-org.html)
  * [ v1.1 ](https://docs.cloud.google.com/apigee/docs/hybrid/v1.1/multi-org.html)



This topic discusses how to add a second Apigee hybrid organization (org) to an existing Kubernetes cluster. In this multi-org configuration, both orgs use and share the same Cassandra ring. Each org can have multiple environments and environment groups configured. 

**Warning:** A multi-org per cluster configuration is supported with specific limitations. Until these limitations are mitigated, we do not recommend that you use this configuration.**Note:** If you are already using multi-org clusters and would like to migrate the orgs to single org clusters, see [ Migrating an org to another cluster](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/migrate-org).

##  Limitations 

A multi-org per cluster configuration is supported with the following limitations. **Until these limitations are mitigated, we do not recommend that you use this configuration:**

**Note:** The maximum number of orgs that you can add to a single cluster is limited. See [Limits](https://docs.cloud.google.com/apigee/docs/api-platform/reference/limits) for details. 

  * If you are going to have multiple Apigee hybrid instances, each instance should have its own cluster. Multiple Apigee hybrid instances running on the same kubernetes cluster can lead to issues of instability potentially causing downtime. 
  * All logging from the pods are sent to the first Google Cloud project that was configured. This limitation is most apparent in the Cloud Logging tool. The logs for the other Apigee orgs will not be sent to the matching Google Cloud project. Logs are still captured at the pod level and can be retrieved with `kubectl` commands. However, they are not sent to the correct Cloud project through Cloud Logging.
  * You cannot delete org data in the Cassandra database for just one org. This means you cannot remove orgs selectively. Any modification to the database configuration affects all orgs that are deployed to that cluster.
  * The hybrid upgrade procedure upgrades the entire cluster all at once.
  * Backup and restore is done as a cluster, and cannot be done for a specific org.
  * The Apigee API Monitoring feature (Timeline, Recent, Investigate) only works for the first org that was configured and deployed. It will not work for the other orgs in a multi-org cluster.



##  Multi-org options 

This section describes how Apigee Support handles existing multi-org clusters and recommendations for future deployments: 

  * If you have existing multi-org Kubernetes clusters deployed in non-production and production contexts, Apigee Support will continue to support them. However, note the technical limitations outlined in the next section. We recommend that you change any future production deployments to use one Apigee org per cluster.
  * If you have existing multi-org clusters in non-production contexts, Apigee Support will continue to support them. We recommend that you migrate any production clusters to a new configuration that uses one Apigee org per cluster.



##  Prerequisites 

Before continuing, note the following: 

  * You must have an existing hybrid org with one or more environments installed and configured in an existing Kubernetes cluster. See the [hybrid installation instructions](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/precog-overview).
  * When combining multiple orgs in a single cluster, the hybrid versions must all match. Before adding a second org to a cluster, upgrade the existing hybrid installation, if necessary. See [Upgrading Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/upgrade).



##  Create an org to add to the existing cluster 

To create the additional org, follow the steps in [Part 1: Project and org setup.](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/precog-overview)

**Note:** If you have an existing org you want to add to your Apigee hybrid installation, you can skip to Configure the new org.

##  Configure the new org 

In the following steps, you will create a new overrides file and configure it for the new org. An `overrides.yaml` file can only support one org's information. Therefore, you must create a new `overrides.yaml` file and apply it to the existing Kubernetes cluster. 

  1. Create service accounts for use with the new org. See [Create service accounts](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-service-accounts).
  2. Make note of the TLS certificate files (`.key` and `.pem`) in your `certs` directory. If you need to create them again, you can follow the instructions in [Create TLS certificates](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-create-tls-certificates).
  3. Copy your existing `overrides.yaml` to a new file to use as a starting point for configuring your new org. For example: `new-overrides.yaml`.
  4. Edit the new overrides file with the following configurations: 
         
         org: "new-org-name"
         instanceID: "instance-id"   ## Must match the instanceID of your existing org.
         
         multiOrgCluster: true ## Enables exporting metrics for this org to the Google Cloud Project named with gcp:projectID
         
         k8sCluster:
           name: "existing-cluster-name"
           region: "existing-cluster-analytics-region"
         
         gcp:
           projectID: "new-project-id"
           name: "new-project-id"
           region: "new-project-default-location"
         
         namespace: namespace ## must be the same for both new and existing orgs
         
         virtualhosts:
           - name: new-environment-group-name
             sslCertPath: ./certs/cert-file-name # .crt or .pem
             sslKeyPath: ./certs/key-file-name # .key
         
         envs:
           - name: new-environment-name
             serviceAccountPaths:
               runtime: ./new-service-accounts-directory/new-project-id-apigee-runtime.json
               synchronizer: ./new-service-accounts-directory/new-project-id-apigee-synchronizer.json
               udca: ./new-service-accounts-directory/new-project-id-apigee-udca.json
         
         connectAgent:
           serviceAccountPath: ./new-service-accounts-directory/new-project-id-apigee-mart.json
         
         mart:
           serviceAccountPath: ./new-service-accounts-directory/new-project-id-apigee-mart.json
         
         metrics:
           serviceAccountPath: ./new-service-accounts-directory/new-project-id-apigee-metrics.json
         
         watcher:
           serviceAccountPath: ./new-service-accounts-directory/new-project-id-apigee-watcher.json

The following table describes each of the property values that you must provide in the overrides file. For more information, see [Configuration property reference](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/config-prop-ref). 

Variable | Description  
---|---  
new-org-name | The name of your new org.  
instance-id | All orgs in this cluster must have the same instance ID. Therefore this must match the `instanceID` entry in the overrides file for your original org. For multi-region installations, each region requires its own cluster, because individual clusters do not span regions. Therefore, each cluster must have its own unique instance ID shared by every org in the cluster.  
existing-cluster-name | The name of the cluster you are adding this org to. It must match the `k8sCluster.name` entry in the overrides file for your original cluster.  
existing-cluster-analytics-region | The region where the original cluster is provisioned. It must match the `k8sCluster.region` entry in the overrides file for your original cluster.  
new-project-id | The project ID of your new project. The project ID and org name are the same.  
new-project-default-location | The analytics region you specified when you created the new org. It does not have to be the same as the region for the existing org.  
namespace | All orgs in the cluster must share the same namespace. Be sure to use the same namespace that was used for the original org. The namespace for most installations is `apigee`.   
new-environment-group-name | The new environment group you created for the new org. **Caution:** The environment group names for the new org should not be the same as the environment group names for any other org. The Helm releases names for envs would be the same, which would make managing the charts difficult.  
cert-file-name and  
key-file-name | The TLS cert and key files for the cluster that you checked or created in step 1 in this section.  
new-environment-name | The name of the environment you created for the new org. **Caution:** The environment names for the new org should not be the same as the environment names for any other org.  
new-service-accounts-directory | The directory where the service account key files you created for the new org are located.  



##  Apply the configuration 

Apply the new org configuration to your cluster: 

  1. Do a dry run installation to check for any problems: 
         
         helm upgrade ORG_NAME apigee-org/ \
           --install \
           --namespace apigee \
           --atomic \
           -f OVERRIDES_FILE.yaml \
           --dry-run=server
         

**Note:** It's a good practice to do a dry run before applying the configuration to determine if there are any issues.
  2. If there are no issues, apply the org-level components. This step installs the Cassandra jobs (user and schema), Apigee Connect, Apigee Watcher and MART services: 
         
         helm upgrade ORG_NAME apigee-org/ \
           --install \
           --namespace apigee \
           --atomic \
           -f NEW_OVERRIDES_FILE.yaml
         

  3. Install the environment. This step installs apigee-runtime, synchronizer and UDCA components, per environment: 
         
         helm upgrade ENV_NAME apigee-env/ \
           --install \
           --namespace apigee \
           --atomic \
           --set env=ENV_NAME \
           -f overrides.yaml \
           --dry-run=server
         
         
         helm upgrade ENV_NAME apigee-env/ \
           --install \
           --namespace apigee \
           --atomic \
           --set env=ENV_NAME \
           -f overrides.yaml
         

**Note:** If you have multiple environments in your new org, repeat this step for each environment.
  4. Apply the load balancer changes. This step configures the ingress to listen to the new virtual host(s) for the second org: **Important:** Do not duplicate hostnames/domain names between two orgs, as it can result in unpredictable routing.
         
         helm upgrade NEW_ENV_GROUP_NAME apigee-virtualhost/ \
           --install \
           --namespace apigee \
           --atomic \
           --set envgroup=NEW_ENV_GROUP_NAME \
           -f overrides.yaml \
           --dry-run=server
         
         
         helm upgrade NEW_ENV_GROUP_NAME apigee-virtualhost/ \
           --install \
           --namespace apigee \
           --atomic \
           --set envgroup=NEW_ENV_GROUP_NAME \
           -f overrides.yaml
         

  5. Enable synchronizer access for your new org following the steps in [Enable Control Plane access](https://docs.cloud.google.com/apigee/docs/hybrid/v1.15/install-enable-control-plane-access).
  6. By default, when you first install the Apigee hybrid runtime, the Telemetry component is configured with `multiOrgCluster` disabled. Use the following steps to enable multi-org telemetry for each org in your cluster: 
     1. Delete the existing Telemetry component with the following commands: 
            
            helm delete telemetry
            

**Note:** Deleting the Telemetry component will stop the metrics being exported to Google Monitoring. Perform the following steps to re-enable metrics.
     2. Add the following line to the `overrides.yaml` file for your existing org. 
            
            multiOrgCluster: true

     3. Apply the changes to install the Telemetry component for the org. 

Perform a dry-run first:
            
            helm upgrade telemetry apigee-telemetry/ \
              --install \
              --namespace apigee \
              --atomic \
              -f FIRST_OVERRIDES_FILE.yaml \
              --dry-run=server
            

If the dry-run is successful, apply the changes and install the Telemetry component:
            
            helm upgrade telemetry apigee-telemetry/ \
              --install \
              --namespace apigee \
              --atomic \
              -f FIRST_OVERRIDES_FILE.yaml
            

     4. Make sure the following line is in the `overrides.yaml` file for each new org. 
            
            multiOrgCluster: true

     5. Apply the changes to install the Telemetry component for each new org. Repeat this for every new org in your multi-org cluster. 

Perform a dry-run first:
            
            helm upgrade telemetry apigee-telemetry/ \
              --install \
              --namespace apigee \
              --atomic \
              -f NEW_OVERRIDES_FILE.yaml \
              --dry-run=server
            

If the dry-run is successful, apply the changes and install the Telemetry component:
            
            helm upgrade telemetry apigee-telemetry/ \
              --install \
              --namespace apigee \
              --atomic \
              -f NEW_OVERRIDES_FILE.yaml
            




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
