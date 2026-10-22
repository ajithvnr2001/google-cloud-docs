---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/get-access-dashboards/
title: Get access to dashboards \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:37.078338+00:00
---

# Get access to dashboards  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/admin/get-access-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)



Send feedback 

#  Get access to dashboards Stay organized with collections  Save and categorize content based on your preferences. 

This page helps you access dashboards for system monitoring and data observability. Dashboards let you query, visualize, and receive alerts on your metrics, logs, and traces.

## View operational logs and metrics for Platform Admins (PA)

To sign in, query, and visualize logs and metrics on the UI of the system monitoring instance for data observability, ask your Organization IAM Admin to grant you the Organization Grafana Viewer (`organization-grafana-viewer`) role in the `platform-obs` project. The Organization IAM Admin can assign and remove the Organization Grafana Viewer role. This role-based access control process lets you access data visualizations safely on dashboards of the system monitoring instance of your project. For more information about role assignments, see [Predefined role descriptions](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/role-descriptions).

The Organization IAM Admin can grant you access by creating a role binding:
    
    
    kubectl --kubeconfig ADMIN_KUBECONFIG create rolebinding pa-grafana-viewer-binding -n platform-obs --user=USER_NAME --clusterrole=organization-grafana-viewer
    

Replace the following:

  * ADMIN_KUBECONFIG: The path of the kubeconfig file for the admin cluster.
  * USER_NAME: The account name of the user that requires the role binding.



For information about setting role bindings from the GDC console, see [Grant access to resources](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/platform/pa-user/iam/set-up-role-bindings#set-up-role-bindings).

## View project logs and metrics for Application Operators (AO)

To sign in, query, and visualize logs and metrics on the UI of the system monitoring instance for data observability, ask your Project IAM Admin to grant you the Project Grafana Viewer (`project-grafana-viewer`) role in your project namespace. The Project IAM Admin can assign and remove the Project Grafana Viewer in the scope of a specified project. This role-based access control process lets you access data visualizations safely on dashboards of the system monitoring instance of your project.

The Project IAM Admin can grant you access by creating a role binding:
    
    
    kubectl --kubeconfig ADMIN_KUBECONFIG create rolebinding project-grafana-viewer-binding -n PROJECT_NAMESPACE --user=USER_NAME --role=project-grafana-viewer
    

Replace the following:

  * ADMIN_KUBECONFIG: The path of the kubeconfig file for the admin cluster.
  * PROJECT_NAMESPACE: The namespace of your project.
  * USER_NAME: The account name of the user that requires the role binding.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
