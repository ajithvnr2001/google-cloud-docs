---
url: https://docs.cloud.google.com/migration-center/docs/generate-estimate/
title: Quickstart: Generate a rapid cost estimate \u00a0|\u00a0 Migration Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:38:19.212956+00:00
---

# Quickstart: Generate a rapid cost estimate  |  Migration Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migration-center/docs/generate-estimate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migration Center ](https://docs.cloud.google.com/migration-center/docs)
  * [ Guides ](https://docs.cloud.google.com/migration-center/docs/migration-center-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Quickstart: Generate a rapid cost estimate 

Learn how to generate a rapid cost estimate for running your infrastructure on Google Cloud with Migration Center.

The estimates are generated based on Google Cloud best practices. Your actual cost can be higher or lower than the generated estimate.

In this example, you will estimate the cost of migrating an on-premises environment that has the following specifications:

  * Contains x86 vCPUs only
  * Includes SAP and Oracle vCPUs
  * Includes both Linux and Windows vCPUs
  * Has a migration timeline of 5 years



* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=migration-center--estimate--generate-estimate)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  4. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  5. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




## Start estimation

  1. In the Google Cloud console, go to the **Migration Center Estimate cost** page.

[Go to Estimate cost](https://console.cloud.google.com/migration/spend)

  2. In the **Estimate name** field, enter `demo_estimate`.

  3. In the **On-premises** calculator card, click **Select for estimate**.

  4. Click **Start Estimate**. 

  5. On the **Start your estimate** page, in the **On-premises** card, click **Start**.




## Specify infrastructure details

  1. On the **Estimate basics** page, leave the default location as is and click **Next**.

  2. On the **Infrastructure** page, in the **Total vCPUs to be migrated** section, in the **Number of vCPUs** field, enter `78250`.

Based on the default storage to compute ratio, which is `4:1`, the **Data center memory required** field is automatically updated to `313000`.

  3. Leave the **Include non-x86 infrastructure** checkbox blank.

  4. In the **Storage currently in use in your data center(s)** section, specify the following details:

     1. In the **Total storage (TB)** field, enter `110`.

     2. Leave the default values for **% File Storage** , **% Block Storage** , and **% Object Storage** as is.

  5. To specify the workload and license details, click **Next**.




## Specify workload and license details

  1. On the **Workloads and licenses** page, in the **Oracle and SAP workloads** section, select **Oracle** and **SAP**.

  2. In the additional **Oracle vCPUs** and **SAP vCPUs** fields that appear, enter the following values:

     * **% of total vCPUs running Oracle Database** : `32`
     * **% of total vCPUs running Oracle Exadata** : `0`
     * **% of total total vCPUs running Oracle Data Warehouse Database** : `0`
     * **Storage for Oracle database (GB)** : `50`
     * **% of total SAP Application vCPUs** : `38`
     * **% of total SAP Database vCPUs** : `12`
  3. In the **Licenses for all other workloads** section, select **Windows Server**.

  4. Select **Linux OS** and then select **Free Linux OS options (Ubuntu, CentOS, Debian, AlmaLinux, openSUSE, etc)**.

  5. In the **% of vCPUs running Windows Server** field, enter `30`.

  6. In the **% of vCPUs running free Linux OS** field, enter `70`.

  7. To set up the migration timeline, click **Next**.




## Set up the migration timeline

  1. On the **Migration timeline, pricing, and discounts** page, leave the default values as is.

  2. To review and export the results, click **Submit**.




## Review and export estimation results

This page displays the following:

  * Your 5-year cloud spend estimate range.

For this example, the range is **$57.5M - $70.3M**.

  * Estimated pricing for your selected environment.

In this example, to view the breakdown of the annual cost for migrating your on-premises infrastructure to Google Cloud and the breakdown of the annual cost for each product, click **View details** in the **On-premises** results card.

To view the breakdown of the annual cost for each product, click the product name. For example, to view the annual cost breakdown for Compute Engine, click **Compute**. The annual list price and percentage of the total estimate is displayed for each Compute Engine component.

Further, to see the details of how this cost is calculated for any Google Cloud component, click the component name. For example, click **Compute for Hot cores (N2)**. The details about how the sizing and price is calculated is displayed. These calculations are based on your inputs and the [default assumptions](https://docs.cloud.google.com/migration-center/docs/estimate/review-defaults) that you can edit if needed.




To export the estimation results, on the top of the results page, click **Export** and select the appropriate option.

## Clean up

To avoid incurring charges to your Google Cloud account for the resources used on this page, follow these steps. 

### Delete the project

The easiest way to eliminate billing is to delete the project that you created for the tutorial. 

To delete the project: 

**Caution** : Deleting a project has the following effects: 
     * **Everything in the project is deleted.** If you used an existing project for the tasks in this document, when you delete it, you also delete any other work you've done in the project. 
     * **Custom project IDs are lost.** When you created this project, you might have created a custom project ID that you want to use in the future. To preserve the URLs that use the project ID, such as an `appspot.com` URL, delete selected resources inside the project instead of deleting the whole project. 

If you plan to explore multiple architectures, tutorials, or quickstarts, reusing projects can help you avoid exceeding project quota limits. 

  1. In the Google Cloud console, go to the **Manage resources** page. 

[Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)

  2. In the project list, select the project that you want to delete, and then click **Delete**. 
  3. In the dialog, type the project ID, and then click **Shut down** to delete the project. 



## What's next

  * Learn more about [cost estimation](https://docs.cloud.google.com/migration-center/docs/estimate/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
