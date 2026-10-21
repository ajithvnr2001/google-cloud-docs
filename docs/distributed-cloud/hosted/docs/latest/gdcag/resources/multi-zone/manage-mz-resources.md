---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/manage-mz-resources/
title: Access zones with your tools \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:11:29.783530+00:00
---

# Access zones with your tools  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/manage-mz-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Access zones with your tools Stay organized with collections  Save and categorize content based on your preferences. 

This document provides the ways you can manage resources across multiple zones in a Google Distributed Cloud (GDC) air-gapped universe. Each surface, whether it be the GDC console, gdcloud CLI, APIs, or Terraform, provide mechanisms to appropriately manage your resources in a designated zone for zonal resources, or globally for resources supported for global provisioning. In a multi-zone universe, you must manage your zonal and global resources for high availability.

This document is for the following audience groups:

  * Platform administrators, such as IT administrators, who are responsible for developing disaster recovery workflows.
  * Application operators, such as application developers, who are responsible for developing and maintaining applications in a GDC universe.



For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Before you manage resources across zones, you must complete the following prerequisites based on your preferred surface:

  * To use the Distributed Cloud CLI, [install the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install).
  * To deploy zonal and global API custom resources, [install the `kubectl` component](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install#install-components).
  * To use Terraform, [configure the Terraform Kubernetes provider](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/configure-terraform).



## Switch to the global context

To manage resources that span all zones or are supported for global provisioning, switch to the global context.

###  Console 

The global context is set by navigating to the global URL, which follows this syntax:
    
    
      https://console.ORG_NAME.SUFFIX
    

Navigate to the global URL to have a global view of your resources across zones.

###  gdcloud 

The global URL is set with the `organization_console_url` parameter when initializing the [gdcloud CLI default configuration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install#init-default-config). The global context is assumed unless you have explicitly set a zonal context.

To revert back to the global URL, complete the following steps:

  1. Set your default organization console URL to the global URL:
         
         gdcloud config set core/organization_console_url GLOBAL_URL
         

  2. Sign in to the global context:
         
         gdcloud auth login --login-config-cert=CA_CERT
         

Replace `CA_CERT` with the certificate authority (CA) certificate installed in the system's trusted certificates store. For more information, see [Web TLS certificate configuration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/web-tls-cert-config).


**Note:** If you set your zonal context with the `gdcloud config set core/zone` command, you must [reinitialize your gdcloud CLI instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install#init-default-config) to reset back to the global context.

###  API 

You must explicitly define the kubeconfig file for the global management API server in your kubectl commands when managing or provisioning global KRM API custom resources. For example:
    
    
      kubectl apply -f resource.yaml --kubeconfig GLOBAL_API_SERVER
    

You can set the global context for your API calls automatically by setting your kubectl context to the global API server. For more information, see [Global API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig).

###  Terraform 

You must explicitly define the global management API server in your Terraform module and initialize it:

  1. Define the kubeconfig file for the global management API server in a Terraform file within your module, such as the `main.tf` file:
         
         provider "kubernetes" {
           config_path = "GLOBAL_API_SERVER"
         }
         

For more information about getting the kubeconfig file of the global API server, see [Global API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#global-resources-kubeconfig).

  2. Apply the new global context for your Terraform module:
         
         terraform apply
         




All subsequent Terraform actions are called in the global context.

## Switch to a zonal context

To manage resources hosted within a particular zone, switch to a zonal context.

###  Console 

The zonal context is set by navigating to the zonal URL, which follows this syntax:
    
    
      https://console.ORG_NAME.ZONE.SUFFIX
    

Navigate to the zonal URL to view the resources that are hosted within the single zone.

Many resource pages also offer zone scope pickers, which let you switch between zonal contexts from within the GDC console page.

![Select a zone to display the resources that are present in that specific zone.](https://docs.cloud.google.com/static/distributed-cloud/hosted/docs/latest/gdcag/images/zone-selector.png)

Select your zonal context from the provided mechanisms to view and manage your zonal resources.

###  gdcloud 

Because the global context is configured by default when using the gdcloud CLI, you must explicitly set your zonal context to manipulate zonal resources. You can perform this action in one of the following three ways, depending on your preferred workflow:

  * **Set the default zone configuration**: Recommended if you primarily work in zonal contexts.
  * **Set the zonal URL configuration**: Recommended if you plan to frequently switch between global and zonal contexts.
  * **Apply the`--zone` flag**: Recommended if you want flexibility to directly apply a zonal context without any gdcloud CLI configuration updates.



Complete the following steps to apply one of these approaches:

**Set the default zone configuration**

  * Set the zone configuration for your gdcloud CLI instance:
        
        gdcloud config set core/zone ZONE_NAME
        

Replace `ZONE_NAME` with the name of the zone to set for your context. For more information, see List zones in a universe.

**Note:** The gdcloud CLI doesn't support unsetting a configuration. Therefore, to remove the zonal context configuration and revert back to the global context, you must [reinitialize your gdcloud CLI instance](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install#init-default-config).



**Set the zonal URL configuration**

  1. Set your default organization console URL to the zonal URL:
         
         gdcloud config set core/organization_console_url ZONAL_URL
         

  2. Sign in to the zone:
         
         gdcloud auth login --login-config-cert=CA_CERT
         

Replace `CA_CERT` with the certificate authority (CA) certificate installed in the system's trusted certificates store. For more information, see [Web TLS certificate configuration](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/pki/web-tls-cert-config).




**Apply the`--zone` flag**

  * Run your gdcloud CLI command with the `--zone` flag included. For example:
        
        gdcloud auth print-identity-token --zone=ZONE_NAME
        

You can set the `--zone` flag for any command that supports it. To check if your specific command provides the `--zone` flag, see the [gdcloud CLI reference documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud).

You can use the `--zone` flag from any global or zonal context.




###  API 

You must explicitly define the kubeconfig file for the zonal management API server in your kubectl commands when managing or provisioning zonal KRM API custom resources. For example:
    
    
      kubectl apply -f resource.yaml --kubeconfig ZONAL_API_SERVER
    

You can set the zonal context for your API calls automatically by setting your kubectl context to the zone's management API server. For more information, see [Zonal management API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig).

###  Terraform 

You must explicitly define the zonal management API server in your Terraform module and initialize it:

  1. Define the kubeconfig file for the zonal management API server in a Terraform file within your module, such as the `main.tf` file:
         
         provider "kubernetes" {
           config_path = "ZONAL_API_SERVER"
         }
         

For more information about getting the kubeconfig file of the zonal management API server, see [Zonal management API server resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#zonal-resources-kubeconfig).

  2. Apply the new global context for your Terraform module:
         
         terraform apply
         




All subsequent Terraform actions are called in the context of the zone you configured.

## List zones in a universe

To manage zonal resources across multiple zones, you must be aware of all available zones in your universe.

  * List all zones in your universe:
        
        gdcloud zones list
        

The output looks similar to the following:
        
        METADATA.NAME
        us-east1-a
        us-east1-b
        us-east1-c
        




## What's next

  * Learn about the [global and zonal API servers](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/multi-zone/api-servers) available in a GDC universe.
  * Explore the [High availability guide](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/ha-apps/overview) to ensure your application is resilient to local zone failures.
  * Visit the [gdcloud CLI reference pages](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-reference/gdcloud) for a comprehensive list of gdcloud CLI commands that are available.
  * To configure Terraform, see the [Terraform overview](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/terraform).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
