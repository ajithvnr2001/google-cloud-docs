---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc/
title: Using VPC Service Controls with Apigee and Apigee hybrid \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:55.914397+00:00
---

# Using VPC Service Controls with Apigee and Apigee hybrid  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Using VPC Service Controls with Apigee and Apigee hybrid Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

**Note** : VPC Service Controls are not supported for the non-VPC peering Apigee setup. See also [Apigee networking options](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/networking-options).

Apigee integrates with [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview), which let you isolate resources of your Google Cloud projects. This helps prevent data leaks/exfiltration.

This section describes how to use VPC Service Controls with Apigee.

## Overview

VPC Service Controls defines a _service perimeter_ that acts as a boundary between a project and other services. Service perimeters are an organization-level method to protect Google Cloud services in your projects in order to mitigate the risk of data exfiltration. 

VPC Service Controls can also ensure that clients within a perimeter that have private access to resources do not have access to unauthorized resources outside the perimeter.

For a detailed look at the benefits of service perimeters, refer to the [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

When using VPC Service Controls, note that:

  * Both the Google Cloud project and its associated runtime are included within that project's VPC Service Controls perimeter.
  * Interaction among services inside a perimeter can be restricted using the [VPC network accessible services](https://docs.cloud.google.com/vpc-service-controls/docs/vpc-accessible-services) feature.



Both Apigee and Apigee hybrid integrate with VPC Service Controls. For a complete list of products that integrate with VPC Service Controls, see [Supported products](https://docs.cloud.google.com/vpc-service-controls/docs/supported-products).

##  Impact on internet connectivity 

When VPC Service Controls are enabled, access to the internet is disabled: the Apigee runtime will no longer communicate with any public internet target. You have to route traffic to your VPC by establishing custom routes. See [Importing and exporting custom routes](https://docs.cloud.google.com/vpc/docs/vpc-peering#importing-exporting-routes). 

## Setting up VPC Service Controls with Apigee

The general process for setting up VPC Service Controls with Apigee is as follows:

  1. Enable VPC Service Controls.
  2. Create a new service perimeter.
  3. Configure the service perimeter.

**Note:** For Apigee hybrid installations, there are additional steps that you must execute to integrate with VPC Service Controls.

These steps are described in more detail below.

**To set up VPC Service Controls with Apigee:**

  1. Enable VPC Service Controls for the peered connection from your network to Apigee by executing the following command:
         
         gcloud services vpc-peerings enable-vpc-service-controls \
           --network=SHARED_VPC_NETWORK --project=PROJECT_ID

Where:

     * SHARED_VPC_NETWORK is the name of your shared VPC network. 
     * PROJECT_ID is the name of the project hosting the shared VPC network; it is not the project used to create the Apigee organization.

This command enables VPC Service Controls for your project. You can execute this command multiple times to enable VPC Service Controls for more than one project.

  2. Create a new perimeter as described in the [the VPC Service Controls Quickstart](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-service-perimeter). When you create a perimeter, you choose which projects to add within that perimeter as well as which services to secure.

For Apigee and Apigee hybrid, Google recommends that you secure all services when you create a perimeter, including the [Apigee API](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest).

For more information, see [Creating a service perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/create-service-perimeters).

  3. Configure the service perimeter, as described in [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).



To add an integrated portal within your perimeter, see Adding an integrated portal to the perimeter.

## Setting up VPC Service Controls with Apigee hybrid

Apigee hybrid supports VPC Service Controls, but there are additional steps that you must perform. The general process for integrating Apigee hybrid with VPC Service Controls is as follows:

  1. Set up private connectivity.
  2. Secure additional services within the perimeter.
  3. Set up a _private repository_. (A private repository is one that is within the perimeter; it does not necessarily need to be a local repository as long as it is inside the perimeter.)
  4. Push the Apigee images to your private repository.
  5. Update overrides to use the private repository during the hybrid installation and configuration process.



Each of these steps are described in more detail in the following procedure.

**To set up VPC Service Controls with Apigee hybrid:**

  1. Set up private IP addresses for your hybrid network hosts, as described in [Setting up private connectivity to Google APIs and services](https://docs.cloud.google.com/vpc-service-controls/docs/set-up-private-connectivity). This involves configuring routes, firewall rules, and DNS entries to let the Google APIs access those private IPs.
  2. Follow the steps in Setting up VPC Service Controls with Apigee.

During this process, you must be sure to secure the following services in addition to those specified for Apigee, within your perimeter:

     * Anthos Service Mesh
     * Cloud Monitoring (Stackdriver)
     * Google Kubernetes Engine (if you are running on GKE)
     * Google Container Registry (if you are using this as your local repository)

To add these services to your perimeter, follow the instructions in [Service perimeter details and configuration](https://docs.cloud.google.com/vpc-service-controls/docs/service-perimeters).

  3. Copy the Apigee images into your private repository: 
     1. Download the signed Apigee images from Docker Hub as described [here](https://docs.cloud.google.com/apigee/docs/hybrid/v1.3/signed-docker-images). Be sure to specify the latest version numbers.

For example:
            
            docker pull google/apigee-installer:1.3.3
            docker pull google/apigee-authn-authz:1.3.3
            docker pull google/apigee-mart-server:1.3.3
            docker pull google/apigee-synchronizer:1.3.3
            docker pull google/apigee-runtime:1.3.3
            docker pull google/apigee-hybrid-cassandra-client:1.3.3
            docker pull google/apigee-hybrid-cassandra:1.3.3
            docker pull google/apigee-cassandra-backup-utility:1.3.3
            docker pull google/apigee-udca:1.3.3
            docker pull google/apigee-stackdriver-logging-agent:1.6.8
            docker pull google/apigee-prom-prometheus:v2.9.2
            docker pull google/apigee-stackdriver-prometheus-sidecar:0.7.5
            docker pull google/apigee-connect-agent:1.3.3
            docker pull google/apigee-watcher:1.3.3
            docker pull google/apigee-operators:1.3.3
            docker pull google/apigee-kube-rbac-proxy:v0.4.1

     2. Tag the images.

The following example tags the images in a US-based GCR repo:
            
            docker tag google/apigee-installer:1.3.3 us.gcr.io/project_ID/apigee-installer:1.3.3
            docker tag google/apigee-authn-authz:1.3.3 us.gcr.io/project_ID/apigee-authn-authz:1.3.3
            docker tag google/apigee-mart-server:1.3.3 us.gcr.io/project_ID/apigee-mart-server:1.3.3
            docker tag google/apigee-synchronizer:1.3.3 us.gcr.io/project_ID/apigee-synchronizer:1.3.3
            docker tag google/apigee-runtime:1.3.3 us.gcr.io/project_ID/apigee-runtime:1.3.3
            docker tag google/apigee-hybrid-cassandra-client:1.3.3 us.gcr.io/project_ID/apigee-hybrid-cassandra-client:1.3.3
            docker tag google/apigee-hybrid-cassandra:1.3.3 us.gcr.io/project_ID/apigee-hybrid-cassandra:1.3.3
            docker tag google/apigee-cassandra-backup-utility:1.3.3 us.gcr.io/project_ID/apigee-cassandra-backup-utility:1.3.3
            docker tag google/apigee-udca:1.3.3 us.gcr.io/project_ID/apigee-udca:1.3.3
            docker tag google/apigee-stackdriver-logging-agent:1.6.8 us.gcr.io/project_ID/apigee-stackdriver-logging-agent:1.6.8
            docker tag google/apigee-prom-prometheus:v2.9.2 us.gcr.io/project_ID/apigee-prom-prometheus:v2.9.2
            docker tag google/apigee-stackdriver-prometheus-sidecar:0.7.5 us.gcr.io/project_ID/apigee-stackdriver-prometheus-sidecar:0.7.5
            docker tag google/apigee-connect-agent:1.3.3 us.gcr.io/project_ID/apigee-connect-agent:1.3.3
            docker tag google/apigee-watcher:1.3.3 us.gcr.io/project_ID/apigee-watcher:1.3.3
            docker tag google/apigee-operators:1.3.3 us.gcr.io/project_ID/apigee-operators:1.3.3
            docker tag google/apigee-kube-rbac-proxy:v0.4.1 us.gcr.io/project_ID/apigee-kube-rbac-proxy:v0.4.1

While not required, Google recommends that you include the project ID or other identifying value in the repo path for each image.

     3. Push the images to your private repository.

The following example pushes the images to a US-based GCR repo:
            
            docker push us.gcr.io/project_ID/apigee-installer:1.3.3
            docker push us.gcr.io/project_ID/apigee-authn-authz:1.3.3
            docker push us.gcr.io/project_ID/apigee-mart-server:1.3.3
            docker push us.gcr.io/project_ID/apigee-synchronizer:1.3.3
            docker push us.gcr.io/project_ID/apigee-runtime:1.3.3
            docker push us.gcr.io/project_ID/apigee-hybrid-cassandra-client:1.3.3
            docker push us.gcr.io/project_ID/apigee-hybrid-cassandra:1.3.3
            docker push us.gcr.io/project_ID/apigee-cassandra-backup-utility:1.3.3
            docker push us.gcr.io/project_ID/apigee-cassandra-backup-utility:1.3.3
            docker push us.gcr.io/project_ID/apigee-udca:1.3.3
            docker push us.gcr.io/project_ID/apigee-stackdriver-logging-agent:1.6.8
            docker push us.gcr.io/project_ID/apigee-prom-prometheus:v2.9.2
            docker push us.gcr.io/project_ID/apigee-stackdriver-prometheus-sidecar:0.7.5
            docker push us.gcr.io/project_ID/apigee-connect-agent1.3.3
            docker push us.gcr.io/project_ID/apigee-watcher1.3.3
            docker push us.gcr.io/project_ID/apigee-operators1.3.3
            docker push us.gcr.io/project_ID/apigee-kube-rbac-proxy:v0.4.1

While not required, Google recommends that you include the project ID or other identifying value in the repo path for each image.

  4. Update your overrides file to point the image URLs to your private repository, as described in [Specify configuration overrides](https://docs.cloud.google.com/apigee/docs/hybrid/latset/2-6-install-configure-cluster)

You must change the image URLs for the following components: 

Component Name (in overrides file) | Image URL  
---|---  
`ao` | `your_private_repo/apigee-operators`  
`authz` | `your_private_repo/apigee-authn-authz`  
`cassandra` |  `your_private_repo/apigee-hybrid-cassandra  
  
auth: your_private_repo/apigee-hybrid-cassandra-client  
backup: your_private_repo/apigee-cassandra-backup-utility  
restore: your_private_repo/apigee-cassandra-backup-utility`  
`connectAgent` | `your_private_repo/apigee-connect-agent`  
`installer` | `your_private_repo/apigee-installer`  
`kubeRBACProxy` |  `your_private_repo/apigee-kube-rbac-proxy`  
`logger` | `your_private_repo/apigee-stackdriver-logging-agent`  
`mart` | `your_private_repo/apigee-mart-server`  
`metrics` | `your_private_repo/apigee-prom-prometheus  
  
sdSidecar: your_private_repo/apigee-stackdriver-prometheus-sidecar`  
`runtime` | `your_private_repo/apigee-runtime`  
`synchronizer` | `your_private_repo/apigee-synchronizer`  
`udca` |  `your_private_repo/apigee-udca  
  
fluentd: your_private_repo/apigee-stackdriver-logging-agent`  
`watcher` | `your_private_repo/apigee-watcher`  
  5. Apply your changes using the new images in GCR, as described in [Apply the configuration to the cluster](https://docs.cloud.google.com/apigee/docs/hybrid/latest/2-7-install-hybrid-runtime#apply-the-configuration-to-the-cluster). 



## Private Service Connect projects and perimeter boundaries

If you use [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) together with [Private Service Connect](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints), the Google Cloud project at the far end of the Private Service Connect connection must be reachable from the same service perimeter as your Apigee project.

From December 1, 2026, Apigee evaluates the peer project as an additional protected resource on the operations in the following list. If your Apigee project is inside a service perimeter and the peer project is outside it, those operations return `PERMISSION_DENIED`.

### Affected operations

This requirement affects only the following control plane operations:

  * Creating an instance (`[organizations.instances.create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances/create)`) or updating one (`[organizations.instances.patch](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.instances/patch)`), when the request sets the [consumer accept list](https://docs.cloud.google.com/apigee/docs/api-platform/architecture/southbound-networking-patterns-endpoints). The projects in the consumer accept list are the peer projects.
  * Creating an endpoint attachment (`[organizations.endpointAttachments.create](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest/v1/organizations.endpointAttachments/create)`). The project that owns the target service attachment is the peer project.

**Note** : API traffic is not affected. Private Service Connect connections that already exist keep carrying traffic, and endpoint attachments that you have already created keep working. This change applies only when you create or update the configuration listed above.

### Check whether you are affected

  1. Determine whether your Apigee project belongs to a service perimeter that restricts `apigee.googleapis.com`. See [Managing service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters).
  2. List the peer projects you use with Private Service Connect: 
     * For inbound connections, the projects in the consumer accept list of each instance.
     * For outbound connections, the project that owns the service attachment named by each endpoint attachment.
  3. For each peer project, check whether it is protected by the same perimeter as your Apigee project.



If every peer project is in the same perimeter, no action is needed.

### Resolve a peer project outside the perimeter

Choose whichever option matches your security requirements:

  * **Add the peer project to the perimeter.** Use this when both projects belong to the same trust boundary. See [Managing service perimeters](https://docs.cloud.google.com/vpc-service-controls/docs/manage-service-perimeters).
  * **Allow the access with an ingress or egress rule.** Use this when the projects must stay in separate perimeters. See [Ingress and egress rules](https://docs.cloud.google.com/vpc-service-controls/docs/ingress-egress-rules).
  * **Remove the cross-perimeter reference.** Remove the project from the consumer accept list, or delete the endpoint attachment that points outside the perimeter.



Before you change a perimeter, you can use [dry run mode](https://docs.cloud.google.com/vpc-service-controls/docs/dry-run-mode) to see the effect of the change without enforcing it.

## Granting integrated portals access to the perimeter

VPC-SC supports granting VPC-SC access levels to integrated portals, but this process requires additional steps, as described in this section.

**Note:** Apigee with VPC-SC only supports granting access for _integrated_ portals; it does _not_ support granting access for _Drupal-based_ portals.

If you do not grant an access level to integrated portals, then integrated portals are unavailable for VPC-SC-enabled Apigee organizations.

Granting an access level to portals:

  * Does not put integrated portals within the perimeter.
  * Allows integrated portals to be accessed from outside the perimeter.
  * Allows VPC-SC protected Apigee data (such as application data) exposure to portal users outside the VPC-SC perimeter.



For more information, see [Allowing access to protected resources from outside a perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/use-access-levels).

### Prerequisites

Before granting perimeter access to an integrated portal, you must enable the `Access Context Manager API` for your project, if it is not already enabled. You can do this in Cloud console or by using the [gcloud services enable](https://docs.cloud.google.com/sdk/gcloud/reference/services/enable) command.

To check if the API is enabled, examine the output of the [gcloud services list](https://docs.cloud.google.com/sdk/gcloud/reference/services/list) command, as described in [Step 2: Enable Apigee APIs](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/enable-apis).

In addition, you must have the service account email address for the project that the portal is used in. To get this, you need the Google Cloud project ID and project number. The following steps describe how to get these values:

  1. Get Google Cloud project details by using the [gcloud projects list](https://docs.cloud.google.com/sdk/gcloud/reference/projects/list) command, as the following example shows: 
         
         gcloud projects list

This command returns the project ID (in the `PROJECT_ID` column) and the project number (in the `PROJECT_NUMBER` column) for each project in your GCP organization.

  2. Identify the Apigee service account email address. This is the same account that the Apigee installer created when you provisioned your organization in [Step 3: Create an organization](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/create-org).

**Terminology Note:** The term _service account_ and _service agent_ are used interchangeably.

To get this email address, use the [`iam service-accounts list`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/list) command, which uses the following syntax:
         
         gcloud iam service-accounts list --project GCP_PROJECT_ID

For example:
         
         gcloud iam service-accounts list --project my-project
         
         DISPLAY NAME                              EMAIL                                                DISABLED
         Apigee default service account            service-8675309@gcp-sa-apigee.iam.gserviceaccount.com  False
         Compute Engine default service account     8675309-compute@developer.gserviceaccount.com          False

The service account that you want is the one whose email address matches the following format:  
`service-GCP_PROJECT_NUMBER@gcp-sa-apigee.iam.gserviceaccount.com`

For example:  
``service-`8675309`@gcp-sa-apigee.iam.gserviceaccount.com``

  3. Get the policy (or perimeter) ID by using the [`access-context-manager policies list`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/policies/list) command. Pass the organization ID to this command, as the following example shows:
         
         gcloud access-context-manager policies list --organization=organizations/GCP_ORG_ID

`gcloud` responds with a list of policies associated with the specified organization; for example:
         
         gcloud access-context-manager policies list --organization=organizations/2244340
         
         NAME          ORGANIZATION      TITLE                 ETAG
         04081981      2244340           Default policy        421924c5a97c0Icu8

**Terminology Note:** The term _policy_ in this context is synonymous with _perimeter_.

VPC-SC's **policy ID** (also known as the _perimeter ID_) is the ID of the VPC-SC _service perimeter_ that acts as a boundary between your project and other services). It is the value in the `NAME` column.




### Steps to grant perimeter access to integrated portals

**To grant perimeter access to an integrated portal:**

  1. Gather the service account email address and VPC-SC's policy ID, as described in Prerequsites.
  2. Create a conditions file on your admin machine that specifies the service account address that will grant the portal access through the perimeter.

The file can be any name you want, but it must have a `*.yaml` extension. For example, `my-portal-access-rules.yaml`.

  3. In the conditions file, add a `members` section that specifies the Apigee service account, as the following example shows:
         
         - members:
           - serviceAccount:service-8675309@gcp-sa-apigee.iam.gserviceaccount.com

Note that adding a `members` section is sufficient; you do not need to add an access level section. For more information on creating a conditions file, see [Limit access by user or service account](https://docs.cloud.google.com/access-context-manager/docs/create-basic-access-level#members-example).

  4. Create an access level with the [`access-context-manager levels create`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/levels/create) command; for example: 
         
         gcloud access-context-manager levels create ACCESS_LEVEL_ID \
           --title ACCESS_LEVEL_TITLE \
           --basic-level-spec PATH/TO/CONDITIONS_FILE.yaml \
           --policy=POLICY_ID

Where:

     * ACCESS_LEVEL_ID is an identifier for the new access level that is being granted; for example, `my-portal-access-level`.
     * ACCESS_LEVEL_TITLE is a title for the access level. The title can be anything you want, but Google recommends that you give it a meaningful value so that you and other administrators will know what it applies to. For example, My Portal Access Level.
     * CONDITIONS_FILE is the path to the YAML file that you created in the previous step.
     * POLICY_ID is the policy or perimeter ID.

For example:
    
    gcloud access-context-manager levels create my-portal-access-level \
      --title My Portal Access Level \
      --basic-level-spec ~/my-portal-access-rules.yaml \
      --policy=04081981

  5. Update the perimeter with the new access level by using the [`access-context-manager perimeters update`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/access-context-manager/perimeters/update) command: 
         
         gcloud access-context-manager perimeters update POLICY_ID \
           --add-access-levels=ACCESS_LEVEL_ID \
           --policy=POLICY_ID

For example:
         
         gcloud access-context-manager perimeters update 04081981 \
           --add-access-levels=my-portal-access-level \
           --policy=04081981




### Troubleshooting

Check the following:

  * If the Access Context Manager API is not enabled for your Google Cloud project, `gcloud` prompts you to enable it when you try to list or set policies.
  * Make sure that you use the _Google Cloud_ organization ID and not the _Apigee_ organization ID when you get details about the organization.
  * Some commands described in this section require elevated permissions; for example, to get details about service accounts for a project, you must be an owner of that project.
  * To verify that the service account exists, execute the [`iam service-accounts describe`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/describe) command, as the following example shows:
        
        gcloud iam service-accounts describe service-8675309@gcp-sa-apigee.iam.gserviceaccount.com

`gcloud` responds with information about the service account, including the display name and project ID to which it belongs. If the service account doesn't exist, `gcloud` responds with a `NOT_FOUND` error.




## Limitations

Apigee integrations with VPC Service Controls have the following limitations:

  * Integrated portals require [additional steps](https://docs.cloud.google.com/apigee/docs/api-platform/security/vpc-sc#portal) to configure.
  * You must deploy Drupal portals within the service perimeter.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
