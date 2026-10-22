---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-cross-project-connect/
title: Enable cross-project connections \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:54.677924+00:00
---

# Enable cross-project connections  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/db-cross-project-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Enable cross-project connections Stay organized with collections  Save and categorize content based on your preferences. 

By default, a database cluster only allows connections from within the [user cluster](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/resource-hierarchy#cluster) and the same project. To allow connections from workloads in another project to all database clusters in your project:

### Console

  1. Sign in to the GDC console with an account bound to the `project-networkpolicy-admin` role to create firewall rules.
  2. From the main menu of the GDC console, choose **Firewall**.
  3. In the **User created rules** section, click **Create**.
  4. In **Firewall rule details** , create a name for your firewall rule.
  5. In the **Direction of traffic** dialog, choose **INGRESS**.
  6. In the **Target** dialog, choose **Service** and then select **dbs**.
  7. In the **From** dialog, choose **Another project** and select the project ID from which you would like to allow connectivity.
  8. Click **Create**.
  9. Wait for the **Status** column of the new rule to show **Ready**.



### API

Create a `ProjectNetworkPolicy` resource to allow connections from a client project.
    
    
    apiVersion: networking.gdc.goog/v1
    kind: ProjectNetworkPolicy
    metadata:
      name: dbs-allow-from-CLIENT_PROJECT
      namespace: USER_PROJECT
    spec:
      subject:
        managedServices:
          matchTypes:
          - dbs
        subjectType: ManagedService
      ingress:
      - from:
        - projects:
            matchNames:
            - CLIENT_PROJECT
      policyType: Ingress
    

Replace the following:

  * `CLIENT_PROJECT`: the name of the project from which you would like to allow connectivity.
  * `USER_PROJECT`: the name of the user project where the database cluster was created.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
