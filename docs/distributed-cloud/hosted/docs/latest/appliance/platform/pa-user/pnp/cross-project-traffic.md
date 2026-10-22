---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pnp/cross-project-traffic/
title: Create cross-project traffic network policies \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:56:49.697106+00:00
---

# Create cross-project traffic network policies  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pnp/cross-project-traffic/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Create cross-project traffic network policies Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions to configure cross-project traffic network policies in Google Distributed Cloud (GDC) air-gapped appliance.

Cross-project traffic refers to the communication between services and workloads from different project namespaces but within the same organization.

Services and workloads in a project are isolated from external services and workloads by default. However, services and workloads from different project namespaces and within the same organization can communicate with each other by applying cross-project traffic network policies.

## Before you begin

To configure intra-project traffic network policies, you must have the following:

  * The necessary identity and access roles. For more information, see [Prepare predefined roles and access](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/pnp/pnp-overview#prepare-predefined-roles-and-access).
  * An existing project. For more information, see [Create a project](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/create-a-project).



## Create a cross-project traffic policy

You can define ingress or egress cross-project traffic policies to manage the communication between projects.

### Create an ingress firewall rule for cross-project traffic

For project workloads or services to allow connections from other workloads in another project, you must configure an ingress firewall rule to allow the inbound traffic of other project workloads.

Work through the following steps to create a new firewall rule and allow inbound traffic from workloads in another project:

###  Console 

  1. Within the GDC console of the project you are configuring, go to **Networking** > **Firewall** in the navigation menu to open the **Firewall** page.
  2. Click **Create** in the action bar to begin creating a new firewall rule.
  3. On the **Firewall rule details** page, fill out the following information:

     1. In the **Name** field, enter a valid name for your firewall rule.
     2. In the **Direction of traffic** section, select **Ingress** to allow inbound traffic from workloads in other projects.
     3. In the **Target** section, select one of the following options: 
        * **All user workloads:** allow connections to the workloads of the project you are configuring.
        * **Service:** indicate that this firewall rule targets a specific service within the project you are configuring.
     4. If your target is a project service, select the name of the service from the list of available services on the **Service** drop-down menu.
     5. In the **From** section, select one of the following two options: 
        * **All projects:** allow connections from workloads in all the projects.
        * **Another project** and **All user workloads:** allow connections from workloads in another project.
     6. If you want to transfer workloads only from another project, select a project that you can access from the list of projects on the **Project ID** drop-down menu.
     7. If your target is all user workloads, select one of the following options in the **Protocols and ports** section: 
        * **Allow all:** allow connections using any protocol or port.
        * **Specified protocols and ports:** allow connections using only the protocols and ports that you specify in the corresponding fields for the ingress firewall rule.
  4. On the **Firewall rule details** page, click **Create**.




You've now permitted connections from other project workloads. After creating the firewall rule, the rule is visible in a table on the **Firewall** page.

###  API 

The following policy enables workloads in the `PROJECT_1` project to permit connections from workloads in the `PROJECT_2` project, as well as the return traffic for the same flows. Apply the policy:
    
    
    kubectl --kubeconfig API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT_1
      name: allow-inbound-traffic-from-PROJECT_2
    spec:
      policyType: Ingress
      subject:
        subjectType: UserWorkload
      ingress:
      - from:
        - projectSelector:
            projects:
              matchNames:
              - PROJECT_2
    EOF
    

Replace `API_SERVER` with the API server's kubeconfig path. If you have not yet generated a kubeconfig file for the API server, see [Sign in](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/sign-in#cli) for details.

The preceding command allows `PROJECT_2` to go to `PROJECT_1`, but doesn't allow connections initiated from `PROJECT_1` to `PROJECT_2`. For the latter, you require a reciprocal policy in the `PROJECT_2` project. Apply the reciprocal policy:
    
    
    kubectl --kubeconfig API_SERVER apply -f - <<EOF
    apiVersion: networking.global.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      namespace: PROJECT_2
      name: allow-inbound-traffic-from-PROJECT_1
    spec:
      policyType: Ingress
      subject:
        subjectType: UserWorkload
      ingress:
      - from:
        - projectSelector:
            projects:
              matchNames:
              - PROJECT_1
    EOF
    

Connections are now permitted to and from `PROJECT_1` and `PROJECT_2`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
