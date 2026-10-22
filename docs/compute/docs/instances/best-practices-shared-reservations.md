---
url: https://docs.cloud.google.com/compute/docs/instances/best-practices-shared-reservations/
title: Best practices for shared reservations \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:46.846387+00:00
---

# Best practices for shared reservations  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/best-practices-shared-reservations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Best practices for shared reservations Stay organized with collections  Save and categorize content based on your preferences. 

To maximize resource usage and reduce management overhead, you can share reservations of Compute Engine resources across multiple projects in your Google Cloud organization. A shared reservation allows up to 100 projects in the same organization to create Compute Engine instances by using the same reserved capacity.

Shared reservations offer the following benefits:

  * You maximize the use of reserved capacity.

  * You lower costs by minimizing idle resources.

  * You manage a single, shared reservation rather than many.




This document explains the best practices for creating and managing shared reservations. For more information about the different methods to reserve Compute Engine resources, see [Choose a reservation type](https://docs.cloud.google.com/compute/docs/instances/choose-reservation-type).

## Best practices for shared reservations

When you create a shared reservation, or Compute Engine creates one to fulfill a future reservation request, we recommend the following best practices to help you manage and use the reservation:

  * **Have the owner project create the shared reservation but not consume it.**

    * To distribute costs among projects, we recommend that only _consumer projects_ , the projects you share a reservation with, consume the reservation. Only use the _owner project_ , the project in which the reservation exists, to create shared reservations.
    * When you create a shared on-demand reservation or future reservation, the owner project must have sufficient quota for the total resources to reserve. Then, after Compute Engine creates the reservation, the owner project must have quota for any reserved resources that it wants to consume. For more information, see [ Additional quota requirements for shared reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements-shared-reservations).
  * **Minimize the number of projects in your organization that can create shared reservations.**

    * You can view only the reservations that exist in your project. Thus, you can only view a shared reservation in its owner project. Having only a few owner projects in your organization helps you monitor and manage your shared reservations. To control which projects can create shared reservations, see [ Manage shared reservation creation](https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation).
    * Share a reservation only with a few projects to better manage the quota of your reserved resources.
  * **Minimize the number of separate shared reservations with identical compute instance properties.**

    * An organization can have up to 100 shared reservations for each unique combination of [ compute instance properties](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#requirements). As a result, if you minimize the number of shared reservations with identical compute instance properties, you mitigate this limit.
    * Having fewer shared reservations improves manageability.
  * **Only share reservations between projects with the same Cloud Billing account.**

    * Limit each shared reservation to consumer projects that have the same Cloud Billing account as the owner project. This approach helps you track reservation consumption and associated billing. **Caution:** If you have a shared reservation and also have [ CUD sharing](https://docs.cloud.google.com/compute/docs/committed-use-discounts/share-resource-cuds-across-projects) enabled for your commitment's Cloud Billing account, then we recommend that you share your reservation _only_ with projects that are linked to the commitment's Cloud Billing account. Otherwise, when projects outside the Cloud Billing account consume that shared reservation, their usage won't be eligible for this Cloud Billing account's shared resource-based CUDs and will incur charges at on-demand rates. 
  * **For future reservation requests, carefully review the total count of compute instances that you request.**
    * If you are creating a [ future reservation request](https://docs.cloud.google.com/compute/docs/instances/create-shared-future-reservations), then verify that you request a _total count_ of compute instances that includes all of the following: 
      * All matching reserved compute instances that will already exist at the future date.
      * All matching unreserved compute instances that will already exist at the future date.
      * Any matching, unused on-demand reservations that will already exist at the future date.
      * The increase in usage that you want to reserve at the future date.

For example, suppose that you need 10 additional compute instances at a future date and you'll already have the following resources at that future date:

      * 40 matching reserved compute instances
      * 50 matching unreserved compute instances

or

      * 40 matching reserved compute instances
      * 50 matching unused on-demand reservations

Because your existing usage at the future date already adds up to 90 matching compute instances and reservations, and you need an additional ten compute instances, you must specify a total count of `100` in your future reservation request.

**Note:** If you create additional on-demand reservations after you submit the future reservation request and before the future date, then those reservations are counted toward your total count.  
  
If you add more on-demand reservations after the future date, then those reservations are added to the previous total. For example, if after the future date, you reserve another ten compute instances, then you end up with 110 compute instances as your total reserved resources. 

For more information, see [ Count and provision reserved resources](https://docs.cloud.google.com/compute/docs/instances/future-reservations-overview#count-reserved-resources).




## What's next

  * [Manage shared reservation creation](https://docs.cloud.google.com/compute/docs/instances/manage-shared-reservations-creation)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
