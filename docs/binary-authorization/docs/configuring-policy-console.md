---
url: https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console/
title: Configure a policy using the Google Cloud console \u00a0|\u00a0 Binary Authorization \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:11:40.667277+00:00
---

# Configure a policy using the Google Cloud console  |  Binary Authorization  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Binary Authorization ](https://docs.cloud.google.com/binary-authorization/docs)
  * [ Guides ](https://docs.cloud.google.com/binary-authorization/docs/overview)



Send feedback 

#  Configure a policy using the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for configuring a Binary Authorization policy by using the Google Cloud console. As an alternative, you can perform these tasks by using the [Google Cloud CLI](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli) or the [REST API](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-rest). This step is part of [setting up Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/setting-up).

A [policy](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#policies) is a set of rules that govern the deployment of one or more container images.

**Note:** This page describes how to configure a policy for the container-based platforms that Binary Authorization supports, including Google Kubernetes Engine (GKE), Distributed Cloud, Cloud Run, and Cloud Service Mesh. Policy settings, such as rule type, rule parameters, and parameter format can vary depending on the platforms you use. Because of this, each section in this page notes the platforms the settings apply to. Make sure the settings you use are supported for your platforms.

## Before you begin

  1. [Enable Binary Authorization](https://docs.cloud.google.com/binary-authorization/docs/enabling).

  2. Enable Binary Authorization for your platform:

     * **Google Kubernetes Engine (GKE) users** : [Create a cluster with Binary Authorization enabled](https://docs.cloud.google.com/binary-authorization/docs/creating-cluster).

     * **Cloud Run users:** [Enable Binary Authorization on your service](https://docs.cloud.google.com/binary-authorization/docs/run/enabling-binauthz-cloud-run).

  3. If you intend to use [attestations](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestations), we recommend that you create [attestors](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#attestors) before configuring the policy. You can create attestors using the [Google Cloud console](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-console) or through a [command-line tool](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-cli).

  4. Select the project ID for the project in which you enabled Binary Authorization.




## Set the default rule

This section applies to _GKE, GKE Multi-Cloud, Distributed Cloud, Cloud Run, and Cloud Service Mesh_.

A [rule](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#rules) is the part of a policy that defines constraints that images must satisfy before they can be deployed. The [default rule](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#default-rules) defines constraints that apply to all [non-exempt](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#exempt_images) container images that don't have their own cluster-specific rules. Every policy has a default rule.

To set the default rule, do the following:

  1. In the **Google Cloud console** , go to the **Binary Authorization** page.

[Go to the Binary Authorization page](https://console.cloud.google.com/security/binary-authorization/)

  2. Click the **Policy** tab.

  3. Click **Edit Policy**.

  4. Set the [evaluation mode](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#evaluation_modes) for the default rule.

The evaluation mode specifies the type of constraint that Binary Authorization enforces at deploy time. To set the evaluation mode, select one of the following options:

     * **Allow all images** : Allows all images to be deployed.
     * **Deny all images** : Disallows all images from being deployed.
     * **Allow only images that have been approved by the following attestors** : Allows an image to be deployed if the image has one or more attestations that can be verified by all of the attestors that you add to this rule. To learn about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-console).

If you selected **Allow only images that have been approved by the following attestors** :

     1. Get the name or resource ID of your attestor.

In the **Google Cloud console** , on the **Attestors** page, you can view your existing attestors, or create a new one.

[Go to the Binary Authorization Attestors page](https://console.cloud.google.com/security/binary-authorization/attestors)

     2. Click **Add Attestors**.

     3. Select one of the following options:

        * **Add by project and attestor name**

The project refers to the project ID of the project that stores your attestors. An example of an attestor name is `build-qa`.

        * **Add by attestor resource ID**

A resource ID has the format:
              
              projects/PROJECT_ID/attestors/ATTESTOR_NAME
              

     4. Under **Attestors** , enter appropriate value(s) for the option you selected.

     5. Click **Add Another Attestor** if you want to add additional attestors.

     6. Click **Add Attestor(s)** to save the rule.


**Note:** We don't recommend using the **Allow all** evaluation mode in the default rule. Doing so allows all container images to deploy unless they fail to satisfy a cluster-specific or other specific rule in the policy.

If you want to enable [dry run mode](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#enforcement-modes), do the following:

  1. Select **Dry Run Mode**.

  2. Click **Save Policy**.


**Note:** It can take a few minutes for the policy to take effect.

## Set cluster-specific rules (optional)

This section applies to _**GKE, Distributed Cloud, and Cloud Service Mesh**_.

A policy can also have one or more [cluster-specific rules](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#cluster-specific_rules). This type of rule applies to container images that are to be deployed to specific Google Kubernetes Engine (GKE) clusters only. Cluster-specific rules are an optional part of a policy.

### Add a cluster-specific rule (GKE)

This section applies to _**GKE and Distributed Cloud**_.

To add a cluster-specific rule for a GKE cluster, do the following:

  1. In the **Google Cloud console** , go to the **Binary Authorization** page.

[Go to the Binary Authorization page](https://console.cloud.google.com/security/binary-authorization/)

  2. Click the **Policy** tab.

  3. Click **Edit Policy**.

  4. Expand the **Additional settings for GKE deployments** section.

  5. If no specific rule type is set, click **Create Specific Rules**.

     1. To select the rule type, click **Specific Rule Type**.

     2. To change the rule type, click **Change**.

  6. Click **Add Specific Rule**.

  7. In the **Cluster resource ID** field, enter the resource ID for the cluster.

The resource ID for the cluster has the format `LOCATION.NAME`, for example, `us-central1-a.test-cluster`.

  8. Set the [evaluation mode](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#evaluation_modes) for the default rule.

The evaluation mode specifies the type of constraint that Binary Authorization enforces at deploy time. To set the evaluation mode, select one of the following options:

     * **Allow all images** : Allows all images to be deployed.
     * **Deny all images** : Disallows all images from being deployed.
     * **Allow only images that have been approved by the following attestors** : Allows an image to be deployed if the image has one or more attestations that can be verified by all of the attestors that you add to this rule. To learn about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-console).

If you selected **Allow only images that have been approved by the following attestors** :

     1. Get the name or resource ID of your attestor.

In the **Google Cloud console** , on the **Attestors** page, you can view your existing attestors, or create a new one.

[Go to the Binary Authorization Attestors page](https://console.cloud.google.com/security/binary-authorization/attestors)

     2. Click **Add Attestors**.

     3. Select one of the following options:

        * **Add by project and attestor name**

The project refers to the project ID of the project that stores your attestors. An example of an attestor name is `build-qa`.

        * **Add by attestor resource ID**

A resource ID has the format:
              
              projects/PROJECT_ID/attestors/ATTESTOR_NAME
              

     4. Under **Attestors** , enter appropriate value(s) for the option you selected.

     5. Click **Add Another Attestor** if you want to add additional attestors.

     6. Click **Add Attestor(s)** to save the rule.

  9. Click **Add** to add the cluster-specific rule.

You might see a message that reads, "It looks like this cluster doesn't exist. This rule will still take effect if this cluster becomes available in GKE in the future." If so, click **Add** again to save the rule.

  10. If you want to enable [dry run mode](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#evaluation-modes), select **Dry Run Mode**.

  11. Click **Save Policy**.


**Note:** It can take a few minutes for the policy to take effect.

### Add a cluster-specific rule (GKE Multi-Cloud,Distributed Cloud)

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This section applies to _**Distributed Cloud**_.

To add a cluster-specific rule for an GKE cluster, do the following:

  1. In the **Google Cloud console** , go to the **Binary Authorization** page.

[Go to the Binary Authorization page](https://console.cloud.google.com/security/binary-authorization/)

  2. Click the **Policy** tab.

  3. Click **Edit Policy**.

  4. Expand the **Additional settings for GKE deployments** section.

  5. If no specific rule type is set, click **Create Specific Rules**.

     1. To select the rule type, click **Specific Rule Type**.

     2. To update the rule type, click **Change**.

  6. Click **Add Specific Rule**.

  7. In the **Cluster resource ID** field, enter the resource ID for the cluster.

     * For GKE attached clusters, and GKE on AWS, the format is `CLUSTER_LOCATION.CLUSTER_NAME`—for example, `us-central1-a.test-cluster`.
     * For Google Distributed Cloud and Google Distributed Cloud, the format is `FLEET_MEMBERSHIP_LOCATION.FLEET_MEMBERSHIP_ID`—for example, `global.test-membership`.
  8. Set the [evaluation mode](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#evaluation_modes) for the default rule.

The evaluation mode specifies the type of constraint that Binary Authorization enforces at deploy time. To set the evaluation mode, select one of the following options:

     * **Allow all images** : Allows all images to be deployed.
     * **Deny all images** : Disallows all images from being deployed.
     * **Allow only images that have been approved by the following attestors** : Allows an image to be deployed if the image has one or more attestations that can be verified by all of the attestors that you add to this rule. To learn about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-console).

If you selected **Allow only images that have been approved by the following attestors** :

     1. Get the name or resource ID of your attestor.

In the **Google Cloud console** , on the **Attestors** page, you can view your existing attestors, or create a new one.

[Go to the Binary Authorization Attestors page](https://console.cloud.google.com/security/binary-authorization/attestors)

     2. Click **Add Attestors**.

     3. Select one of the following options:

        * **Add by project and attestor name**

The project refers to the project ID of the project that stores your attestors. An example of an attestor name is `build-qa`.

        * **Add by attestor resource ID**

A resource ID has the format:
              
              projects/PROJECT_ID/attestors/ATTESTOR_NAME
              

     4. Under **Attestors** , enter appropriate value(s) for the option you selected.

     5. Click **Add Another Attestor** if you want to add additional attestors.

     6. Click **Add Attestor(s)** to save the rule.

  9. Click **Add** to save the rule.

You might see a message that reads "It looks like this cluster doesn't exist. This rule still takes effect if the specified cluster becomes available in GKE in the future." In this case, click **Add** again to save the rule.

  10. If you want to enable [dry run mode](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#enforcement-modes), select **Dry Run Mode**.

  11. Click **Save Policy**.


**Note:** It can take a few minutes for the policy to take effect.

### Add specific rules

**Note** : This feature can only be enabled on clusters running on the following GKE releases: 

  * 1.18.12-gke.700+
  * 1.19.4-gke.700+
  * 1.20.0-gke.600+
  * 1.21+



You can create rules that are scoped to either a mesh service identity, a Kubernetes service account, or a Kubernetes namespace. You can add or modify a specific rule as follows:

  1. In the **Google Cloud console** , go to the **Binary Authorization** page.

[Go to the Binary Authorization page](https://console.cloud.google.com/security/binary-authorization/)

  2. Click the **Policy** tab.

  3. Click **Edit Policy**.

  4. Expand the **Additional settings for GKE and Anthos deployments** section.

  5. If no specific rule type is set, click **Create Specific Rules**.

     1. Click **Specific Rule Type** to select the rule type.

     2. Click **Change** to update the rule type.

  6. If the specific rule type exists, you can change the rule type by clicking **Edit Type**.

**Note:** You can set one specific rule type per policy. If the rule type is changed, the rules created for the original type will be deleted when the policy page is saved.
  7. To add a specific rule, click **Add Specific Rule**. Depending on the rule type you choose, you enter an ID, as follows:

     * **ASM Service Identity** : Enter your ASM service identity, which has the following format: PROJECT_ID.svc.id.goog/ns/NAMESPACE/sa/SERVICE_ACCOUNT
     * **Kubernetes Service Account** : Enter your Kubernetes service account, which has the following format: NAMESPACE:SERVICE_ACCOUNT.
     * **Kubernetes Namespace** : Enter your Kubernetes namespace, which has the following format: NAMESPACE

Replace the following, as required, depending on the rule type:

     * PROJECT_ID: the project ID in which you define your Kubernetes resources.
     * NAMESPACE: the Kubernetes namespace.
     * SERVICE_ACCOUNT: the service account.
  8. Set the [evaluation mode](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#evaluation_modes) for the default rule.

The evaluation mode specifies the type of constraint that Binary Authorization enforces at deploy time. To set the evaluation mode, select one of the following options:

     * **Allow all images** : Allows all images to be deployed.
     * **Deny all images** : Disallows all images from being deployed.
     * **Allow only images that have been approved by the following attestors** : Allows an image to be deployed if the image has one or more attestations that can be verified by all of the attestors that you add to this rule. To learn about creating attestors, see [Creating attestors](https://docs.cloud.google.com/binary-authorization/docs/creating-attestors-console).

If you selected **Allow only images that have been approved by the following attestors** :

     1. Get the name or resource ID of your attestor.

In the **Google Cloud console** , on the **Attestors** page, you can view your existing attestors, or create a new one.

[Go to the Binary Authorization Attestors page](https://console.cloud.google.com/security/binary-authorization/attestors)

     2. Click **Add Attestors**.

     3. Select one of the following options:

        * **Add by project and attestor name**

The project refers to the project ID of the project that stores your attestors. An example of an attestor name is `build-qa`.

        * **Add by attestor resource ID**

A resource ID has the format:
              
              projects/PROJECT_ID/attestors/ATTESTOR_NAME
              

     4. Under **Attestors** , enter appropriate value(s) for the option you selected.

     5. Click **Add Another Attestor** if you want to add additional attestors.

     6. Click **Add Attestor(s)** to save the rule.

  9. Click **Dry run mode** to enable [dry run mode](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#evaluation-modes).

  10. Click **Add** to save the specific rule.

  11. Click **Save Policy**.


**Note:** It can take a few minutes for the policy to take effect.

## Manage exempt images

This section applies to _**GKE, Distributed Cloud, Cloud Run, and Cloud Service Mesh**_.

An [exempt image](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#exempt_images) is an image, specified by a path, that is exempt from policy rules. Binary Authorization always allows exempt images to be deployed.

This path can specify a location either in [Container Registry](https://docs.cloud.google.com/container-registry/docs) or another container image registry.

### Cloud Run

This section applies to _**Cloud Run**_.

You cannot _directly_ specify image names that contain a tag. For example, you cannot specify `IMAGE_PATH`:latest.

If you want to specify image names that contain tags, you must specify the image name using a [wildcard](https://docs.cloud.google.com/binary-authorization/docs/policy-yaml-reference#admissionwhitelistpatterns) as follows:

  * `*` for all versions of a single image; for example, `us-docker.pkg.dev/myproject/container/hello@*`
  * `**` for all images in a project; for example, `us-docker.pkg.dev/myproject/**`



You can use path names to specify a digest in the format `IMAGE_PATH`@`DIGEST`.

## Enable the system policy

This section applies to _**GKE and Distributed Cloud**_.

[Trust all Google-provided system images](https://docs.cloud.google.com/binary-authorization/docs/key-concepts#google-maintained_system_images) is a policy setting that enables the Binary Authorization system policy. When this setting is enabled at deploy time, Binary Authorization exempts a list of Google-maintained system images that are required by GKE from further policy evaluation. The system policy is evaluated before any of your other policy settings.

**Note:** We recommend that you select `Trust all Google-provided system images`. Doing so allows Google to manage the allowlist of system images that GKE uses. Google updates this allowlist with each GKE release. If you don't enable the setting, you must manage the allowlist yourself.

To enable the system policy, do the following:

  1. Go to the **Binary Authorization** page in **Google Cloud console**.

[Go to Binary Authorization](https://console.cloud.google.com/security/binary-authorization/)

  2. Click **Edit Policy**.

  3. Expand the **Additional settings for GKE and Anthos deployments** section.

  4. Select **Trust all Google provided system images** in the **Google system image exemption** section.

To view the images exempted by the system policy, click **View Details**.

**Note:** The system policy information might temporarily differ from region to region while Google updates the allowlist. The list of images displayed is from the last group of regions that was updated. Since most changes to the system policy are additions the list shows the set of system images that are currently allowed in all regions. You can view the system policy for a specific region [using a `gcloud` command](https://docs.cloud.google.com/binary-authorization/docs/configuring-policy-cli#global-policy-evaluation-mode).
  5. To manually specify additional exempt images, expand the **Custom exemption rules** section under **Images exempt from this policy**.

Then, click **Add Image Pattern** and enter the registry path to any additional image you want to exempt.

  6. Click **Save Policy**.


**Note:** It can take a few minutes for the policy to take effect.

## What's next

  * Use the `built-by-cloud-build` attestor to [deploy only images built by Cloud Build](https://docs.cloud.google.com/binary-authorization/docs/deploy-cloud-build) ([Preview](https://cloud.google.com/products#product-launch-stages)).
  * [Use attestations](https://docs.cloud.google.com/binary-authorization/docs/attestations).
  * [Deploy a GKE image](https://docs.cloud.google.com/binary-authorization/docs/deploying-containers).
  * [View Cloud Audit Logs events](https://docs.cloud.google.com/binary-authorization/docs/viewing-audit-logs).
  * [Use continuous validation](https://docs.cloud.google.com/binary-authorization/docs/overview-cv).
  * [Use legacy continuous validation](https://docs.cloud.google.com/binary-authorization/docs/using-cv) ([deprecated](https://docs.cloud.google.com/binary-authorization/docs/deprecations/cv-project-singleton-policy)) to check policy conformance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
