---
url: https://docs.cloud.google.com/load-balancing/docs/https/roll-back-migrated-resources/
title: Roll back migrated resources to classic Application Load Balancer \u00a0|\u00a0 Cloud Load Balancing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:50.935378+00:00
---

# Roll back migrated resources to classic Application Load Balancer  |  Cloud Load Balancing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/load-balancing/docs/https/roll-back-migrated-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Load Balancing ](https://docs.cloud.google.com/load-balancing/docs)
  * [ Guides ](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview)



Send feedback 

#  Roll back migrated resources to classic Application Load Balancer Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to roll back the [migrated resources](https://docs.cloud.google.com/load-balancing/docs/https/migrate-from-classic-global) from the global external Application Load Balancer infrastructure to the classic Application Load Balancer infrastructure.

Use the following order to roll back a migrated resource within 90 days of changing its load balancing scheme:

  1. Roll back the forwarding rule.
  2. Roll back the backend buckets.
  3. Roll back all the backend services attached to the forwarding rule.



To roll back a backend service to the `EXTERNAL` load balancing scheme, you must first roll back the forwarding rule.

## Before you begin

Before you roll back migrated resources, make sure that you've [migrated the classic Application Load Balancer resources to the global external Application Load Balancer infrastructure](https://docs.cloud.google.com/load-balancing/docs/https/migrate-from-classic-global) and changed their load balancing schemes to `EXTERNAL_MANAGED`. Remember, only resources that were migrated to the `EXTERNAL_MANAGED` scheme from the `EXTERNAL` scheme in the last 90 days can be rolled back.

You must also remove any [advanced traffic management features](https://docs.cloud.google.com/load-balancing/docs/https/traffic-management-global) configured on the resources before you start the rollback process.

### Required role

To get the permissions that you need to manage load balancer components, ask your administrator to grant you the [Compute Network Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.networkAdmin) (`roles/compute.networkAdmin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information, see the following pages:

  * [Roles and permissions](https://docs.cloud.google.com/load-balancing/docs/access-control)
  * [IAM Conditions for forwarding rules](https://docs.cloud.google.com/load-balancing/docs/access-control/iam-conditions)



## Roll back the forwarding rule

###  Console 

To roll back forwarding rules, use the gcloud CLI.

###  gcloud 

  1. Change the load balancing scheme of the forwarding rule from `EXTERNAL_MANAGED` to `EXTERNAL`.

If a backend bucket is attached to the forwarding rule, skip this step and roll back the backend bucket.
         
         gcloud compute forwarding-rules update FORWARDING_RULE_NAME \
             --load-balancing-scheme=EXTERNAL \
             --global
         

Replace `FORWARDING_RULE_NAME` with the name of the forwarding rule. For example, `web-map-http-forwarding-rule`.

Wait for some time (at least six minutes).

  2. Optional: Check the logs of the forwarding rule. You see the load balancing scheme has changed to `EXTERNAL`.




## Roll back the backend bucket

###  Console 

To roll back backend buckets, use the gcloud CLI.

###  gcloud 

  1. Change the scheme of the backend bucket to `EXTERNAL` and the migration state to `TEST_ALL_TRAFFIC`.
         
         gcloud compute forwarding-rules update FORWARDING_RULE_NAME \
             --load-balancing-scheme=EXTERNAL \
             --external-managed-backend-bucket-migration-state=TEST_ALL_TRAFFIC \
             --global
         

Wait for some time (at least six minutes).

  2. To send some classic Application Load Balancer network traffic to the backend bucket, change the migration state of the backend bucket to `TEST_BY_PERCENTAGE` and set the percentage. For example, `90`. This means that 90 percent of requests continue to go to the global external Application Load Balancer infrastructure and the remaining 10 percent of requests will go to the classic Application Load Balancer infrastructure for testing. 
         
         gcloud compute forwarding-rules update FORWARDING_RULE_NAME \
             --external-managed-backend-bucket-migration-state=TEST_BY_PERCENTAGE \
             --external-managed-backend-bucket-migration-testing-percentage=90 \
             --global
         

Wait for some time (at least six minutes).

You can check the [load balancer's metrics](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#monitoring_metrics) to verify that the overall balance of requests matches your configured rollback rate.

  3. Change the migration state of the backend bucket to `PREPARE`.
         
         gcloud compute forwarding-rules update FORWARDING_RULE_NAME \
             --external-managed-backend-bucket-migration-state=PREPARE \
             --global
         

Wait for some time (at least six minutes).

  4. Change the migration state of the backend bucket to its pre-migration state.
         
         gcloud compute forwarding-rules update FORWARDING_RULE_NAME \
             --clear-external-managed-backend-bucket-migration-state \
             --global
         

Wait for some time (at least six minutes).




## Roll back the backend service

###  Console 

**Send traffic to the classic Application Load Balancer infrastructure**

  1. In the Google Cloud console, go to the **Load balancing** page.

[Go to Load balancing](https://console.cloud.google.com/net-services/loadbalancing/list)

  2. Click the name of the load balancer. For example, `web-map-http`.

  3. Click the **Migration** tab.

  4. In the **Backend services** section, for the backend service, verify the following, and click **Revert**.

     * **Status** : **Migrated**
     * **Migration rate** : **100%**
     * **Scheme activity** : **EXTERNAL: 0% EXTERNAL_MANAGED: 100%**
  5. In the **Manage migration** pane, for **Status change** , select **Test all traffic**. This means that all requests are still sent to the global external Application Load Balancer infrastructure.

  6. Click **Save**. Wait for some time (at least six minutes) for the resource to be migrated. The **Status** column changes to **Testing all traffic** and **Scheme activity** to **EXTERNAL: 0% EXTERNAL_MANAGED: 100%**.

  7. Click **Manage migration**.

  8. In the **Manage migration** pane, for **Status change** , select **Test by percentage**.

  9. For **Testing percentage** , enter the percentage of requests that you want to go to the global external Application Load Balancer infrastructure. For example, `90`. This means that 90 percent of requests continue to go to the global external Application Load Balancer infrastructure and the remaining 10 percent of requests will go to the classic Application Load Balancer infrastructure for testing. 

  10. Click **Save**.

Wait for some time (at least six minutes) for the resource to be ready. The **Status** column changes to **Testing by %** , **Migration rate** to **90%** , and **Scheme activity** will be **EXTERNAL: 10% EXTERNAL_MANAGED: 90%**.

After the resource is ready, it sends 90% of requests to the global external Application Load Balancer infrastructure and 10% of requests to the classic Application Load Balancer infrastructure.

  11. Test the load balancer to ensure that requests are being served as expected.

Enter `http://IP_ADDRESS` in the address bar of the web browser. You should see the `Page served from: lb-backend-example-xxxx` message.

  12. You can repeat these steps to progressively decrease the percentage of traffic sent to the global external Application Load Balancer infrastructure.

The backend service rollback process is complete when you are sending all traffic to the classic Application Load Balancer. The **Status** column will be **Testing by %** , **Migration rate** set to **0%** , and **Scheme activity** will be **EXTERNAL: 100% EXTERNAL_MANAGED: 0%**.




###  gcloud 

  1. Change the scheme of the backend service to `EXTERNAL` and the migration state to `TEST_ALL_TRAFFIC`.
         
         gcloud compute backend-services update BACKEND_SERVICE_NAME \
             --load-balancing-scheme=EXTERNAL \
             --external-managed-migration-state=TEST_ALL_TRAFFIC \
             --global
         

Replace `BACKEND_SERVICE_NAME` with the name of the backend service. For example, `web-backend-service`.

Wait for some time (at least six minutes).

  2. To send some classic Application Load Balancer network traffic to the backend service, change the migration state of the backend service to `TEST_BY_PERCENTAGE` and set the percentage. For example, `90`. This means that 90 percent of requests continue to go to the global external Application Load Balancer infrastructure and the remaining 10 percent of requests will go to the classic Application Load Balancer infrastructure for testing. 
         
         gcloud compute backend-services update BACKEND_SERVICE_NAME \
             --external-managed-migration-state=TEST_BY_PERCENTAGE \
             --external-managed-migration-testing-percentage=90 \
             --global
         

Wait for some time (at least six minutes).

You can check the [load balancer's metrics](https://docs.cloud.google.com/load-balancing/docs/https/https-logging-monitoring#monitoring_metrics) to verify that the overall balance of requests matches your configured rollback rate.

  3. Change the migration state of the backend service to `PREPARE`.
         
         gcloud compute backend-services update BACKEND_SERVICE_NAME \
             --external-managed-migration-state=PREPARE \
             --global
         

Wait for some time (at least six minutes).

  4. Change the migration state of the backend service to its pre-migration state.
         
         gcloud compute backend-services update BACKEND_SERVICE_NAME \
             --clear-external-managed-migration-state \
             --global
         

Wait for some time (at least six minutes).

  5. After rolling back the backend service, check its log. You see the load balancing scheme has changed to `EXTERNAL`.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
