---
url: https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically/
title: Renew commitments automatically \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:12:44.052961+00:00
---

# Renew commitments automatically  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/renew-commitments-automatically/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Renew commitments automatically Stay organized with collections  Save and categorize content based on your preferences. 

If you have workloads with predictable resource requirements, then you can lower your costs through [resource-based committed use discounts (CUDs)](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts). You can receive resource-based CUDs by purchasing resource-based _commitments_ for a term of either 1 or 3 years. By default, resource-based commitments expire at the end of their term. After a commitment's expiry, you must purchase a new commitment to continue receiving CUDs. _Auto-renewal_ of your resource-based commitment removes the need for you to manually repurchase the commitment every time that it expires. Auto-renewal of a commitment lets you indefinitely extend an existing commitment and continue receiving CUDs for those committed resources.

This document explains how auto-renewal works, and shows you how to enable and disable the auto-renewal setting on your commitments.

## How auto-renewal works

When you enable auto-renewal on a resource-based commitment, each time your commitment reaches the end of its term, Compute Engine automatically renews that commitment for a new term. After you enable auto-renewal on a commitment, the setting remains enabled until you manually disable it.

You must enable auto-renewal separately on each commitment that you want to automatically renew in a project. You can enable auto-renewal on both new and existing commitments as follows:

  * For **new commitments** , when you purchase a commitment, you have the option to specify whether you want the commitment to renew automatically.
  * For **existing commitments** that are active and don't have auto-renewal enabled, you can modify the commitment's properties and enable auto-renewal. You can't enable auto-renewal for expired commitments.



After you enable auto-renewal on a commitment, the end date and time of your commitment's ongoing term become the renewal date and time. All other properties of your commitment remain the same. At 12 AM US and Canadian Pacific Time (UTC-8, or UTC-7 during daylight saving time) on the renewal date, your commitment's renewed term automatically begins. For example, suppose that the end time of your commitment's ongoing term is 12:00 AM US and Canadian Pacific Time on January 1, 2026. If auto-renewal is enabled, then a new term automatically begins at 12:00 AM US and Canadian Pacific Time on January 1, 2026.

The renewed term length of an automatically renewing commitment always matches the preset term length defined by the commitment's plan, which is either 1 year or 3 years. You also receive the same discount percentage. Even if your commitment has a [ custom term length](https://docs.cloud.google.com/compute/docs/committed-use-discounts/extend-commitment-term), Compute Engine renews your commitment only for its preset term length of either 1 or 3 years. Auto-renewal of a custom term commitment won't be for another term of that custom length. For examples, see the following:

  * A commitment with a custom term of 1.5 years will renew only for 1 additional year.
  * A commitment with a custom term of 5.5 years will renew only for 3 additional years.



If you want a custom term commitment to stay active for a longer time period than the renewed term, then you can request another term extension after its renewal. Your term extension eligibility window also gets refreshed at the start of your renewed term. For a 1-year commitment, the eligibility window during the renewed term remains open for up to 4 months after the renewal. For 3-year commitments, this window remains open for up to 1 year after the renewal.

At the end of the renewed term, Compute Engine again renews your commitment for a new term, unless you manually disable auto-renewal during the commitment's term.

You can enable auto-renewal on your commitment anytime before the commitment is set to expire. Likewise, you can disable auto-renewal on your commitment anytime before its renewal date. For example, if you have a 1-year commitment that is set to expire at 12 AM (UTC-8) on January 1, 2024, then you can enable auto-renewal on that commitment anytime before 12 AM (UTC-8) on January 1, 2024. After you enable auto-renewal, your commitment automatically renews for an additional year at 12 AM (UTC-8) on January 1, 2024. If you then want to disable auto-renewal, then you can do so anytime before 12 AM (UTC-8) on January 1, 2025.

By activating auto-renewal on a commitment, you agree to the following:

  * You have your commitment automatically renewed for a new term at the end of its ongoing term.
  * You continue paying for your committed resources over the new term.



### Example of auto-renewal

Consider an example 1-year commitment `my-commitment-1` that doesn't renew automatically. Suppose that you purchase this commitment on January 1, 2020, for 100 N2 vCPUs. The term of your commitment is scheduled to end on January 1, 2021. Suppose that you perform the following series of operations on this commitment:

  1. You enable auto-renewal on this commitment before its end date.

  2. After the commitment's term gets renewed twice, you disable auto-renewal on the commitment and let your commitment expire on its new end date.




The following table shows how the commitment's properties behave throughout the lifetime of this commitment:

| **Original term**  
**(before enabling auto-renewal)** | **Original term**  
**(after enabling auto-renewal)** | **First automatically renewed term**  
**(auto-renewal remains enabled)** | **Second automatically renewed term**  
**(before disabling auto-renewal)** | **Second automatically renewed term**  
**(after disabling auto-renewal)**  
---|---|---|---|---|---  
**Term duration** | 1 year | 1 year | 1 year | 1 year | 1 year  
**Discount** | 37% | 37% | 37% | **37% 3** | **37% 3**  
**Original commitment start date 1** | January 1, 2020 | January 1, 2020 | January 1, 2020 | January 1, 2020 | January 1, 2020  
**Term start date 1** | January 1, 2020 | January 1, 2020 | January 1, 2021 | January 1, 2022 | January 1, 2022  
**End date or renewal date 2** | January 1, 2021 | January 1, 2021 | January 1, 2022 | January 1, 2023 | January 1, 2023  
**Action on the end or renewal date** | Commitment scheduled to expire | Commitment scheduled to renew | Commitment scheduled to renew | Commitment scheduled to renew | Commitment scheduled to expire  
**Term extension eligibility window open until** | May 1, 2020 | May 1, 2021 | May 1, 2021 | May 1, 2022 | May 1, 2022  
  
1Each 1-year term in this example starts at 12 AM US and Canadian Pacific Time (UTC-8 or UTC-7) on the specified start date.  
2Each 1-year term in this example ends at 12 AM US and Canadian Pacific Time (UTC-8 or UTC-7) on the specified end date.  
3Even if the total duration of your commitment period becomes 3 years or more, the CUD rate for your auto-renewed commitment remains unchanged because the duration of each term is still 1 year. 

### Quota considerations

You don't need to request additional quota because renewed commitments use the same quota as the original commitment. For more information about quota for commitments, see [Quotas for commitments and committed resources](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#quota).

### Pricing implications

Your commitment fee is the sum of the discounted prices of all your committed resources. When you renew your commitment's term, the discounted prices of all your committed resources are recalculated and might change. To do this recalculation, Compute Engine uses the prevailing on-demand prices of the resources on the day that your renewed term becomes active. You retain these prices for your resources throughout your new term, even if the on-demand prices change.

**Note:** If you merge or split your commitments, then the discounted prices for your committed resources might change on the day that your merged or split commitments become active.

## Limitations

  * You can enable auto-renewal only on your resource-based commitments.
  * You can enable auto-renewal only on your active commitments.
  * You can't enable auto-renewal on software license commitments.
  * You can't enable auto-renewal on commitments that you purchased through [future reservations for capacity blocks](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type#reserve-capacity-aihc).



## Enable auto-renewal on commitments

To have your commitment automatically renew at the end of its term, enable auto-renewal in one of the following ways:

  * Enable auto-renewal while purchasing a new commitment.
  * Enable auto-renewal on an existing commitment.



### Enable auto-renewal while purchasing a new commitment {: #enable-auto-renewal-new-commitment }

You can enable auto-renewal while purchasing a new commitment by using the Google Cloud console, the gcloud CLI, or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions):

  * `compute.commitments.create` on the project



To purchase a commitment that has auto-renewal enabled, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Committed use discounts** page.

[Go to Committed use discounts](https://console.cloud.google.com/compute/commitments)

  2. Click add_box **Purchase commitment**. The **Purchase a commitment** page appears.

  3. On the **Purchase a commitment** page, specify the properties for your commitment, as follows:

     1. To configure the auto-renewal setting for your commitment, in the **Term** section, select the **Auto-renew commitment** checkbox.

     2. For instructions on how to configure other properties for your commitment, see one of the following pages depending on your use case:

        * [Purchase hardware commitments without attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments)
        * [Purchase hardware commitments with attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations)

At a minimum, you must specify the name, region, resources, [commitment type](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#commitment-types-for-hardware-commitments), and [commitment plan](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts#commitment-plan).

  4. In the **Summary** pane, review your commitment details and any potential quota limitations.

  5. To finish purchasing your commitment, do the following:

     1. Navigate to the bottom of the page.

     2. Review the **Disclosures** section that contains information about fees, discount eligibility, and terms and conditions.

     3. To confirm your acceptance of the [commitment price](https://cloud.google.com/products/compute/pricing) and [service specific terms](https://cloud.google.com/terms/service-terms), select the checkbox.

     4. Click **Purchase**.




###  gcloud 

To purchase a commitment that renews automatically, run the [`gcloud compute commitments create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/create) and include the `--auto-renew` flag.

For example, the following gcloud CLI command creates a 3-year commitment that renews automatically.
    
    
    gcloud compute commitments create COMMITMENT_NAME \
        --auto-renew \
        --plan=36-month \
        --region=us-west1 \
        --project=PROJECT_ID \
        --resources=vcpu=4,memory=9GB
    

Replace the following:

  * `COMMITMENT_NAME`: the name of the new commitment for which you want to enable auto-renewal.
  * `PROJECT_ID`: the ID of the project where you want to purchase the commitment.



###  REST 

To purchase a commitment that renews automatically, make a `POST` request to the [`regionCommitments.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCommitments/insert) and set the `autoRenew` field to `true`.

For example, the following Compute Engine API request creates a 3-year commitment that renews automatically.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/commitments
    
    {
      "name": "COMMITMENT_NAME",
      "plan": "THIRTY_SIX_MONTH",
      "resources": [
        {
          "type": "VCPU",
          "amount": 4
        },
        {
          "type": "MEMORY",
          "amount": 9
        }
      ],
      "autoRenew": true
    }
    

Replace the following:

  * `COMMITMENT_NAME`: the name of the new commitment for which you want to enable auto-renewal.
  * `PROJECT_ID`: the ID of the project where you want to purchase the commitment.



### Enable auto-renewal on an existing commitment {: #enable-auto-renewal-existing-commitment }

You can enable auto-renewal on an existing commitment by using the Google Cloud console, the gcloud CLI, or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions):

  * `compute.commitments.update` on the project or organization



###  Console 

  1. In the Google Cloud console, go to the **Committed use discounts** page.

[Go to Committed use discounts](https://console.cloud.google.com/compute/commitments)

  2. In the **Commitment list** , select the **Hardware commitments** or **Block storage commitments** tab, and then click the **Name** of the commitment.

  3. On the **Hardware commitment details** or **Block storage commitment details** page that opens, click the **Auto renew** toggle.




###  gcloud 

To enable auto-renewal on an existing commitment, run the [`gcloud compute commitments update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/update) and include the `--auto-renew` flag.
    
    
    gcloud compute commitments update COMMITMENT_NAME \
        --auto-renew
    

Replace `COMMITMENT_NAME` with the name of the commitment for which you want to enable auto-renewal.

###  REST 

To enable auto-renewal on an existing commitment, make a `PATCH` request to the [`regionCommitments.update`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCommitments/update) method and set the `autoRenew` field to `true`.

For example, the following Compute Engine API request enables auto-renewal for a commitment in the `us-west1` region.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/commitments/COMMITMENT_NAME
    
    {
      "name": "COMMITMENT_NAME",
      "autoRenew": true
    }
    

Replace the following:

  * `COMMITMENT_NAME`: the name of the commitment for which you want to enable auto-renewal.
  * `PROJECT_ID`: the ID of the project where you purchased the commitment.



## Disable auto-renewal on commitments

When you purchase new commitments, auto-renewal is disabled by default unless you specifically enable it. If you don't want your commitment to automatically renew at the end of its term, then you can do one of the following:

  * Keep auto-renewal disabled while purchasing a new commitment.
  * Disable auto-renewal on an existing commitment.



### Disable auto-renewal while purchasing a new commitment

For detailed steps to purchase new commitments that have auto-renewal disabled by default, see the following pages. Select the option that is relevant to your use case.

  * [Purchase hardware commitments without attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments)
  * [Purchase hardware commitments with attached reservations](https://docs.cloud.google.com/compute/docs/committed-use-discounts/purchase-commitments-with-reservations)



### Disable auto-renewal on an existing commitment

You can disable auto-renewal on an existing commitment by using the Google Cloud console, the gcloud CLI, or REST.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions):

  * `compute.commitments.update` on the project or organization



###  Console 

  1. In the Google Cloud console, go to the **Committed use discounts** page.

[Go to Committed use discounts](https://console.cloud.google.com/compute/commitments)

  2. In the **Commitment list** , select the **Hardware commitments** or **Block storage commitments** tab, and then click the **Name** of the commitment.

  3. On the **Hardware commitment details** or **Block storage commitment details** page that opens, click the **Auto renew** toggle.




###  gcloud 

To disable auto-renewal on an existing commitment, run the [`gcloud compute commitments update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/commitments/update):
    
    
    gcloud compute commitments update COMMITMENT_NAME --no-auto-renew
    

Replace `COMMITMENT_NAME` with the name of the commitment for which you want to disable auto-renewal.

###  REST 

To disable auto-renewal on an existing commitment, use the [`regionCommitments.update`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/regionCommitments/update) method.

For example, the following Compute Engine API request disables auto-renewal for a commitment in the `us-west1` region.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/us-west1/commitments/COMMITMENT_NAME
    
    {
      "name": "COMMITMENT_NAME",
      "autoRenew": false
    }
    

Replace the following:

  * `COMMITMENT_NAME`: the name of the commitment for which you want to disable auto-renewal.
  * `PROJECT_ID`: the ID of the project where you purchased the commitment.



## What's next

  * Learn how to [troubleshoot auto-renewal for resource-based commitments](https://docs.cloud.google.com/compute/docs/troubleshooting/automatic-commitment-renewal).
  * Learn how to [extend the term of resource-based commitments](https://docs.cloud.google.com/compute/docs/committed-use-discounts/extend-commitment-term).
  * Learn how to [upgrade resource-based commitments](https://docs.cloud.google.com/compute/docs/instances/upgrade-commitment-term).
  * Learn how to [merge and split resource-based commitments](https://docs.cloud.google.com/compute/docs/instances/merge-and-split-commitments).
  * Learn how to [analyze the effectiveness of your CUDs](https://docs.cloud.google.com/billing/docs/how-to/analyze-cuds).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
