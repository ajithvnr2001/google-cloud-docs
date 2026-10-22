---
url: https://docs.cloud.google.com/deployment-manager/docs/best-practices/
title: Best practices for using Deployment Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:44.567152+00:00
---

# Best practices for using Deployment Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deployment-manager/docs/best-practices/

Cloud Deployment Manager reached end of support on **March 31, 2026**.   
If you currently use Deployment Manager, please migrate to Infrastructure Manager or an alternative deployment technology.  
  
For more information on the deprecation and shutdown, see [Deployment Manager deprecation](https://docs.cloud.google.com/deployment-manager/docs/deprecations). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Infrastructure as code ](https://docs.cloud.google.com/docs/iac)
  * [ Cloud Deployment Manager ](https://docs.cloud.google.com/deployment-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment)



Send feedback 

#  Best practices for using Deployment Manager Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the best practices for creating deployments using Google Cloud Deployment Manager. This page is designed for users who are familiar with Deployment Manager; this page will not teach you how to use Deployment Manager.

If you are new to Deployment Manager, try the [Quickstart](https://docs.cloud.google.com/deployment-manager/docs/manage-cloud-resources-deployment) instead.

## Managing resources

❑  After you have created a resource as part of a deployment, use Deployment Manager if you need to modify the resource. If you modify a resource without using Deployment Manager, such as with the Google Cloud console or `gcloud` you might see errors if you try to modify the resource in your original deployment. If you want to remove a resource from a deployment without deleting the resource, use the following steps:

  1. In your deployment configuration, delete the definition of that resource. 
  2. [ Update the deployment](https://docs.cloud.google.com/deployment-manager/docs/deployments/updating-deployments), and in your `gcloud` command, add `--delete-policy ABANDON`. The resource is no longer associated with the deployment, and you can then modify the resource using the Google Cloud console or `gcloud`. 

  
---  
❑  If you have Compute Engine instances in your deployment and want to attach persistent disks to the instances, define the disk separately from the instance, so that you can manage it easily. For example, in the deployment below, the disk `example-disk` is defined separately from the instance `example-instance`. To attach the disk, the configuration has a [reference](https://docs.cloud.google.com/deployment-manager/docs/configuration/use-references) to the disk: 
    
    
        resources:
        # instance
        - name: example-instance
          type: compute.v1.instance
          properties:
            disks:
              - type: PERSISTENT
                source:$(ref.example-disk.selfLink)
       # disk
       - name: example-disk
         type: compute.v1.disk
         properties:
           zone: us-central1-a
           sizeGb: 10
           type: ...
          
  
❑  If you want to create and manage private Google Kubernetes Engine (GKE) clusters with Deployment Manager, set the following [ `privateClusterConfig`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#privateclusterconfig) and [ `ipAllocationPolicy`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/rest/v1/projects.locations.clusters#ipallocationpolicy) options in your deployment.
    
    
         privateClusterConfig:
            enablePrivateNodes: true
            enablePrivateEndpoint: true
            #  Configure the IP range for the hosted master network
            masterIpv4CidrBlock: IP_RANGE
          ipAllocationPolicy:
            useIpAliases: true
            createSubnetwork: true
        

For requirements and additional considerations when you are creating a private cluster with GKE, read [Setting up a private cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/private-clusters#overview).  
  
## Including credentials in your deployment

❑  Deployment Manager redacts some fields related to credentials from properties in your YAML configurations. This redaction occurs based on the key of the property. The following example demonstrates one such redaction: 
    
    
        # Config provided to Deployment Manager
        resources:
        - name: example-resource
          type: gcp-types/service-v1:sample-type-with-password
          properties:
            zone: us-central1-a
            username: test-user
            password: hunter2
    
       # Config as surfaced by Deployment Manager
       resources:
        - name: example-resource
          type: gcp-types/service-v1:sample-type-with-password
          properties:
            zone: us-central1-a
            username: test-user
            password: (redacted)
          
  
---  
❑  If you include the credential in a Jinja or Python template for your deployment, the credential is redacted from the resulting Expanded Config and Layout files, but is still visible in the original import file. For this reason, **we strongly recommend that you place all credentials which you intend to keep secret in your top-level YAML config**. You can reference them from there by using [template properties](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/define-template-properties).   
❑  Any credentials included in a key-value pair within a YAML file or list of items **will not be redacted** , such as in the following example. We strongly recommend that you do not provide credentials to Deployment Manager as key-value pairs within YAML files or lists of items for this reason. 
    
    
        # Not a valid instance configuration, used solely for demonstration
        resources:
        - name: example-resource
          type: gcp-types/compute-v1:instances
          properties:
            zone: us-central1-a
            disks:
            - autoDelete: true
              boot: true
        # Will not be redacted
              password: hunter2
          
  
## Building templates

❑  To speed up defining your templates, consider starting with the production-ready sample templates from the [Cloud Foundation Toolkit Project](https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit).   
---  
❑  If you have complex infrastructure requirements, such as the need to create multiple environments, read the tutorial and samples for [using Deployment Manager at scale](https://docs.cloud.google.com/deployment-manager/docs/at-scale).   
❑  Use Python to [build your templates](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template). You can use Python or Jinja2 to create templates. Jinja is easier to get started with, but Python is more flexible for complex deployments where you might have many resources split across multiple environments.   
❑  Structure your [configuration file](https://docs.cloud.google.com/deployment-manager/docs/configuration) (the YAML file) so it only uses one type, and use a top-level template as that type to call all of the other templates. Adopting this practice makes it easier to change a set of templates into a [ composite type](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-composite-types).   
❑  Use a [schema file](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/using-schemas). Schemas define a set of rules that a configuration file must follow to use a particular template. By defining a schema and encouraging others to review the requirements defined in a schema, your users have an easy way to understand what properties are settable or required for the respective template. This helps users consume the configuration without having to investigate the detail of the templates. At a minimum, define a schema file for the top-level template.   
❑  Use [template properties](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/define-template-properties) and [outputs](https://docs.cloud.google.com/deployment-manager/docs/configuration/expose-information-outputs). Using properties and outputs allows you to pass in variables like the zone, machine size, number of machines, or the app state (test, prod, staging) into your templates and get back output values such as the IP address and the `selfLink` to a VM instance. Properties and outputs allow your templates to be flexible so they can be reused with no modifications to the underlying templates.   
❑  Use individual template files that you import into your main configuration file. This provides you with a more manageable way of working with configurations.   
❑  Break your configurations up into logical units. For example, create separate configurations for stateful services such as databases and buckets and configurations for more transient services such as frontend instances.   
❑  Use [references](https://docs.cloud.google.com/deployment-manager/docs/configuration/use-references). References should be used for values that are not defined until a resource is created, such as a resource's `selfLink`, IP address, or system-generated ID. Without references, Deployment Manager creates all resources in parallel, so there is no guarantee that dependent resources are created in the correct order. Using references would enforce the order in which resources are created.   
❑  [Preview](https://docs.cloud.google.com/deployment-manager/docs/configuration/preview-configuration-file) your deployments to assess how making an update will affect your deployment. Deployment Manager does not instantiate any actual resources when you preview a configuration, but expands the full configuration and creates "shell" resources instead. This gives you the opportunity to see the changes to your deployment before committing to it.   
❑  Check the API methods for a specific resource to understand the implications of carrying out an update. Set [update policies](https://docs.cloud.google.com/deployment-manager/docs/deployments/updating-deployments#optional_determine_the_update_policies_to_use) when updating a deployment to help you control how Deployment Manager applies each update.   
❑  Use labels for your resources. If the resources you are defining supports labels, use them to label your resources. Labels can help categorize resources that belong to different deployments and are also a way to distinguish what stage the resources might be in, such as whether a resource is supporting a production or test environment.   
  
## Managing the size of your deployments

Deployment Manager can operate on a large number of resources, subject to [quota limits](https://docs.cloud.google.com/deployment-manager/quotas#deployment_manager). If you want to reduce the amount of time it takes to create, update, or delete your deployments, you can reduce the number of resources within each individual deployment.

**Note:** If you are not encountering other limitations within Deployment Manager, then you do not have to reduce the size of your deployments. The items presented in this section are intended only as suggestions that you can use to prevent runtime issues from occurring later on. ❑  If a group of resources does not depend on any resources outside of that group, you can move that group of resources into a separate deployment. For example, if your deployment contains several [templates](https://docs.cloud.google.com/deployment-manager/docs/configuration/templates/create-basic-template), you can potentially package each template as a separate deployment.   
---  
❑  Remove unnecessary resources from your configuration. If you need more resources later, you can add more resources to your deployment at that time.   
❑  Optionally, limit your deployments to 1000 or fewer resources.   
  
## Permissions

By default, Deployment Manager uses the credentials of the Google APIs service account to authenticate to other APIs. The Google APIs service account is designed specifically to run internal Google processes on your behalf.

When you want to grant other users access to your Deployment Manager project, you need to grant the user an [IAM role](https://docs.cloud.google.com/deployment-manager/docs/access-control) that has the appropriate permissions to use Deployment Manager. There are a number of predefined IAM roles you can use to determine how much access a user has to call Deployment Manager.

❑  Use IAM roles to restrict what permissions are granted to users to use Deployment Manager.   
---  
❑  If you want users to be able to access resources created by Deployment Manager, grant users the [roles](https://docs.cloud.google.com/iam/docs/understanding-roles) they require to use resources, but do not grant them permissions to deploy resources directly.   
❑  Granting the [owner](https://docs.cloud.google.com/iam/docs/roles-overview#basic) role to a principal will allow them to modify the IAM policy. Therefore, grant the owner role only if the principal has a legitimate purpose to manage the IAM policy, as your policy contains sensitive access control data. Having a minimal set of users manage it will simplify any auditing that you may have to do.   
❑  Deployment Manager uses the Google APIs service account to create and manage your resources. If you are using Deployment Manager to manage critical resources, such as [custom IAM roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles), you must assign additional IAM roles to the default Google APIs service account. For example, if you want to use Deployment Manager to create and manage custom IAM roles, you must add the Role Administrator role to the Google APIs service account.  For an overview of the Google APIs service account, see [Google- managed service accounts](https://docs.cloud.google.com/iam/docs/service-account-types#google-managed_service_accounts).  For steps to assign roles to a service account, see [Granting roles to service accounts](https://docs.cloud.google.com/iam/docs/granting-roles-to-service-accounts).   
  
## Automation

Consider automating the creation of projects as well as automating the creation of resources contained within the projects. This enables you to adopt an infrastructure-as-code approach for project provisioning. This approach provides many benefits, such as the ability to:

  * Allow enforcement of corporate requirements when providing projects to the teams who need access to Google Cloud resources.
  * Provide a series of predefined project environments that can be quickly and easily provisioned.
  * Use version control to manage your base project configuration.
  * Have confidence that you are deploying reproducible and consistent project configurations.
  * Incorporate project creation as part of an automated provisioning process.

❑  Automate the creation of projects using the [templates available on GitHub](https://github.com/GoogleCloudPlatform/cloud-foundation-toolkit/tree/master/dm/templates/project) as a starting point.   
---  
  
## Continuous Integration (CI) / Continuous Deployment (CD)

Use Deployment Manager as part of your CI/CD pipeline.

❑  Do not use a CI/CD pipeline to create and delete entire test and QA projects. 

  * You might choose to destroy VM instances or resources that might incur extra cost, but consider leaving reusable assets that could take a while to recreate, as deleting these resources could adversely impact how long it takes to complete your build pipelines. There are no costs for setting up networks, subnets, or firewall rules.
  * Be aware that if you do delete a project, it will remain part of your project quota for a few days until the project is completely removed. This also means you cannot reuse the project name.
  * Using Deployment Manager allows you to easily delete resources from a project so that you do not hit your resource quotas.

  
---  
❑  Use Deployment Manager to create the stateful parts of the project and network configuration and deploy these outside of the CI/CD process as part of the initial setup. After testing is completed, you can delete deployments that contain only stateless resources that were deployed as part of the pipeline.   
❑  As part of the CI/CD process, use a separate configuration to deploy resources to your test and QA projects. After you have finished testing, you can then use Deployment Manager to delete the resources from your test and QA projects.   
Test deployments. With the ability to incorporate resource provisioning as part of a CI/CD pipeline, Deployment Manager allows you to treat your project configuration as code that you can easily test, and reproduce consistent copies of the current production environment or the current environment with changes applied to test in confidence.   
❑  Use version control. Using a version control system as part of the development process for your deployments allows you to: 

  * Fall back to a previous known good configuration.
  * Provide an audit trail for changes.
  * Use the configuration as part of a continuous deployment system.

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
