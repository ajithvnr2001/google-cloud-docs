---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/get-configuration-file-from-cluster/
title: Generate configuration files from a cluster \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:22.475816+00:00
---

# Generate configuration files from a cluster  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/get-configuration-file-from-cluster/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Generate configuration files from a cluster Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to generate a set of configuration files from an existing cluster.

One way to create a cluster is to use the `gkectl` command-line tool. First you create a set of configuration files for the cluster. Then you run one of the following commands:

  * `gkectl create admin` to create an admin cluster
  * `gkectl create cluster` to create a user cluster



Over time, your original configuration files might become out of sync with the actual state of your cluster. For example, if you update a cluster by editing a custom resource, then your original configuration files might not be an accurate representation of the cluster.

Another way to create a cluster is to use the Google Cloud console, and in that case, you would not have any cluster configuration files. Later you might need cluster configuration files so that you can make certain updates to the cluster.

If you suspect your original configuration files are out of sync with your cluster, or if you don't have configuration files, you can use the `gkectl get-config` command to generate a new set of configuration files that accurately represent the current state of the cluster.

You can use `gkectl get-config` with:

  * User clusters
  * Admin clusters



## Generate configuration files

To generate a new set of configuration files for a user cluster:
    
    
    gkectl get-config cluster --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --cluster-name USER_CLUSTER_NAME
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the path of the kubeconfig file for the admin cluster

  * USER_CLUSTER_NAME: the name of the user cluster




To generate a new set of configuration files for an admin cluster:
    
    
    gkectl get-config admin --kubeconfig ADMIN_CLUSTER_KUBECONFIG \
        --bundle-path BUNDLE
    

Replace the following:

  * ADMIN_CLUSTER_KUBECONFIG: the kubeconfig file for the admin cluster

  * BUNDLE: the path of the Google Distributed Cloud bundle file. The bundle file is on your admin workstation, typically at `/var/lib/gke/bundles/gke-onprem-vsphere-VERSION-full.tgz`. If you don't already have a bundle file, you can [download one](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/downloads#bundle).




By default, the generated configuration files are written to a sub-directory of the current directory. For a user cluster, the output directory is named `user-cluster-config-output`. For an admin cluster, the output directory is named `admin-cluster-config-output`.

If you prefer to have the generated files in a different directory, you can use the `--output-dir` parameter to specify the path of an output directory. For example:
    
    
    gkectl get-config cluster --kubeconfig my-kubeconfig \
        --cluster-name my-cluster \
        --output-dir /home/me/configuration/generated-files
    

If there are already files in the default output directory or a specified output directory, you must include the `--force` flag so that the newly generated files will replace the existing files. Otherwise the command will fail. For example:
    
    
    gkectl get-config cluster --kubeconfig my-kubeconfig \
        --cluster-name my-cluster \
        --output-dir /home/me/configuration/generated-files
        --force
    

## Generated files for an admin cluster

Filename| Description  
---|---  
`admin-cluster.yaml` |  [Admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest)   
Always generated   
`admin-cluster-creds.yaml` |  [Cluster credentials file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file)   
Always generated   
`component-access-key.json` |  JSON key file for your [component access service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#component_access_service_account)   
Always generated   
`vcenter-ca-cert.pem` |  [Root certificate](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-ca-cert-path) for your vCenter Server   
Always generated   
`admin-cluster-ipblock.yaml` |  [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) for cluster nodes   
Generated if the cluster nodes use [static IP addresses](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-ipmode-type-field)  
`connect-register-key.json` |  JSON key file for your [connect register service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#connect_register_service_account)   
Always generated   
`private-registry-ca.crt ` |  Root certificate for your private registry server   
Generated if the cluster uses a [private registry](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#privateregistry-cacertpath-field)  
`stackdriver-key.json` |  JSON key file for your [logging monitoring service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#logging_monitoring_service_account)   
Generated if the cluster is configured to to export logs and metrics to [Cloud Logging](https://docs.cloud.google.com/logging/docs) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) (`stackdriver` section in the cluster configuration file)   
`audit-logging-key.json` |  JSON key file for your [audit logging service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#audit_logging_service_account)   
Generated if the cluster uses Cloud Audit Logs   
  
## Generated files for a user cluster

Filename| Description  
---|---  
`user-cluster.yaml` |  [User cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest)   
Always generated   
`user-cluster-creds.yaml` |  [Cluster credentials file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/credentials-configuration-file)   
Generated if the cluster is not using prepared credentials   
`vcenter-ca-cert.pem` |  [Root certificate](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/vcenter-ca-cert-path) for your vCenter Server   
Always generated   
`user-cluster-ipblock.yaml` |  [IP block file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/ip-block-file) for cluster nodes   
Generated if the cluster nodes use [static IP addresses](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-ipmode-type-field)  
`private-registry-ca.crt ` |  Root certificate for your private registry server   
Generated if the cluster uses a [private registry](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#privateregistry-cacertpath-field)  
`component-access-key.json` |  JSON key file for your [component access service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#component_access_service_account)   
Generated if the cluster is not using a private registry   
`connect-register-key.json` |  JSON key file for your [connect register service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#connect_register_service_account)   
Always generated   
`stackdriver-key.json` |  JSON key file for your [logging monitoring service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#logging_monitoring_service_account)   
Generated if the cluster is configured to to export logs and metrics to [Cloud Logging](https://docs.cloud.google.com/logging/docs) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) (`stackdriver` section in the cluster configuration file)   
`audit-logging-key.json` |  JSON key file for your [audit logging service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#audit_logging_service_account)   
Generated if the cluster uses Cloud Audit Logs   
`usage-metering-key.json` |  JSON key file for your [usage metering service account](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/service-accounts#usage_metering_service_account)   
Generated if the cluster stores usage data in a BigQuery dataset   
`secrets.yaml` |  [Secrets configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/secrets-configuration-file)   
Generated if the cluster uses [prepared credentials](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/prepared-credentials)   
For this file to be generated, you must include the `--export-secrets-config` flag in the `gkectl get-config cluster` command.   
`sni-cert.pem` |  Additional serving certificate for the Kubernetes API server   
Generated if the cluster is configured to use [Server Name Indication (SNI)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#authentication-sni-section)  
`sni-key.json` |  Private key file for the additional serving certificate   
Generated if the cluster is configured to use SNI   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
