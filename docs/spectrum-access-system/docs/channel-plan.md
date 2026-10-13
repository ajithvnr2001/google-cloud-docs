---
url: https://docs.cloud.google.com/spectrum-access-system/docs/channel-plan/
title: Use a channel plan \u00a0|\u00a0 Spectrum Access System \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:06:24.173910+00:00
---

# Use a channel plan  |  Spectrum Access System  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spectrum-access-system/docs/channel-plan/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Spectrum Access System ](https://docs.cloud.google.com/spectrum-access-system/docs)
  * [ Guides ](https://docs.cloud.google.com/spectrum-access-system/docs/overview)



Send feedback 

#  Use a channel plan Stay organized with collections  Save and categorize content based on your preferences. 

You can review and implement a channel plan for your Citizens Broadband Radio Service (CBRS) network from the Google Spectrum Access System (SAS) Portal. The channel plan is optimized to minimize interference with another Citizens Broadband Radio Service Device (CBSD).

## When to use a channel plan

You can use a channel plan to do the following:

  * **Deploy new CBSDs**.

You can add or upload the CBSD's parameters for your future deployment to the SAS Portal. The SAS Portal then recommends channels for every CBSD. These recommendations are based on each CBSD configuration, their frequency management groups, and deployments by other nearby operators.

  * **Resolve interference**.

As a first option to mitigate interference, you must review the SAS Portal's proposed channel plan. If the proposed plan doesn't meet your needs, contact [SAS Support](https://docs.cloud.google.com/spectrum-access-system/docs/getting-support) to explain your requirements and receive a solution.




## Before you begin

For the channel plan recommendations to be useful, review the frequency management groups and make sure that they're accurate. To optimize channel allocations for minimal interference, SAS needs to know which devices can and can't interfere with each other.

All CBSD configurations in the SAS Portal, including those of unregistered CBSDs, are accounted for in the channel plan.

## Review the channel plan

**Important:** The channel plan available to you in the SAS Portal is the result of assigning channels for only your CBSDs.

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/).
  2. Click **View deployments**.
  3. Select a deployment, and then click **Open**.
  4. Click _table_chart_ **Table view**.
  5. On the **Device table** page, click _view_column_ **Select columns**.
  6. Add the following columns to the table: 
     * **Freq. plan:** a diagram of future grants after the plan is implemented.
     * **Freq. plan EIRP:** the EIRP for all grants after the plan is implemented.
     * **Freq. plan quality:** the average channel quality score anticipated for the new grants after the plan is implemented.
     * **Freq. plan cohort:** a group of CBSDs whose channel assignments need to be considered together to avoid interference issues.
  7. Click **Apply**.
  8. Optional: To download the plan as a CSV, click _file_download_ **Frequency planning**.



## Optimize a cohort of the CBSDs to find new clean channels

If one of your CBSDs experiences interference, and there are no channels available with high quality scores, you can use the channel plan to find clean channels.

To optimize a group of CBSDs, implement the recommended channel plan for that cohort. For example, if some CBSDs must remain on a specific channel, you can remove them from the channel plan before you optimize the cohort. All other CBSDs then move to the suggested channels just before the next Coordinated Periodic Activities among SASs (CPAS).

The channel plan is designed for all CBSDs in a cohort to switch to the recommended channels. While the channel plan feature is in [Preview](https://cloud.google.com/products#product-launch-stages), you might find that only certain CBSDs in the cohort need to change channels. For these rare scenarios, you can remove individual CBSDs when you optimize the cohort. If you find issues with your channel plan, we recommend that you verify the frequency management groups.

To optimize your channel plan, follow these steps:

  1. After you review your channel plan, select the CBSD that you want to optimize or resolve interference for.
  2. On the right of the CBSD page, click _lock_**Unlock CBSD**.
  3. On the **Coex** tab, click **Optimize cohort**.
  4. If some CBSDs must remain on a specific channel, clear them from the list of CBSDs in the selected cohort.
  5. If a cohort has more than 1,000 CBSDs, select the CBSD to optimize the entire cohort.
  6. Click **Schedule planning**. All changes take effect just before the next CPAS.

**Tip:** You can find the scheduled changes in the **Pending changes** section of the **Coex** tab.



## Determine how the channel plan affects a single CBSD

  1. Go to the [SAS Portal](https://wirelessconnectivity.google.com/sas/).
  2. Click **View deployments**.
  3. Select the deployment, and then click **Open**.
  4. Select a CBSD.
  5. On the right, select the **Coex** tab.
  6. In the **Frequency planning** section, review the current and future channels and channel quality.

**Tip:** If a current channel is also one of the frequency plan's future channels, move the mouse over the channel to find the current and future channel quality.



## What's next

  * [Choose the best channels for a CBSD](https://docs.cloud.google.com/spectrum-access-system/docs/cbsd/channels).
  * Learn about [Spectrum Access System](https://docs.cloud.google.com/spectrum-access-system/docs/overview).
  * Learn about [key SAS terms](https://docs.cloud.google.com/spectrum-access-system/docs/key-terms).
  * [Troubleshoot SAS issues](https://docs.cloud.google.com/spectrum-access-system/docs/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
