---
url: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-network-set-modes/
title: Set routing and best path selection modes \u00a0|\u00a0 Cloud Router \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:15:52.005013+00:00
---

# Set routing and best path selection modes  |  Cloud Router  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-network-set-modes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Router ](https://docs.cloud.google.com/network-connectivity/docs/router)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set routing and best path selection modes

The following Virtual Private Cloud (VPC) network settings control how all Cloud Routers work within the network:

  * Advertised routes are controlled by the dynamic routing mode of the VPC network.

  * Learned routes are controlled by both the dynamic routing mode _and_ the best path selection mode of the VPC network.




The dynamic routing mode of a VPC network is either _regional_ (default) or _global_.

The best path selection mode of a VPC network is either _legacy_ (default) or _standard_. As a best practice, we recommend using legacy best path selection mode for critical workloads.

For more information about best path selection modes, see [Best path selection](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#best-path-selection).

You can specify the dynamic routing mode and the best path selection mode when you create a VPC network, or when you update a VPC network.

## View a VPC network's dynamic routing and best path selection modes

To view the current dynamic routing mode and best path selection mode of a VPC network, follow these steps.

###  Console 

**Note:** Google Cloud console only shows a network's dynamic routing mode.

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. To view a network's details page, click the network's name.

  3. In the **Dynamic routing mode** section, the value indicates the type of dynamic routing mode, either **Regional** or **Global**.

  4. In the * **Best path selection mode** section, the value indicates the type of best path selection mode, either **Standard** or **Legacy**.




###  gcloud 

Run the [`gcloud compute networks describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/describe):
    
    
    gcloud compute networks describe NETWORK_NAME \
        --format="get(routingConfig)" \
        --project=PROJECT_ID

Replace the following:

  * `NETWORK_NAME`: the name of the VPC network
  * `PROJECT_ID`: the ID of the project that contains the VPC network



In the output, see the following:

  * The `routingMode` is the dynamic routing mode of the VPC network. Its value is either `REGIONAL` or `GLOBAL`.

  * The `bgpBestPathSelectionMode` is the best path selection mode of the VPC network. Its value is either `LEGACY` or `STANDARD`.

  * If the best path selection mode (`bgpBestPathSelectionMode`) is `STANDARD`, the output might contain the following additional items:

  * `bgpAlwaysCompareMed`: Values are either `True` or `False`. If `bgpAlwaysCompareMed` isn't included in the output, the implied default value is `False`.

  * `bgpInterRegionCost`: Values are either `DEFAULT` or `ADD_COST_TO_MED`. If `bgpInterRegionCost` isn't included in the output, the implied default value is `DEFAULT`.




###  API 

Use the [`networks.get` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/get):
    
    
    GET https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the VPC network
  * `NETWORK_NAME`: the name of the VPC network



In the output, see the following:

  * `routingMode` is the dynamic routing mode of the VPC network. Its value is either `REGIONAL` or `GLOBAL`.

  * `bgpBestPathSelectionMode` is the best path selection mode of the VPC network. Its value is either `LEGACY` or `STANDARD`.

  * If the best path selection mode, `bgpBestPathSelectionMode`, is `STANDARD`, the output might contain the following additional items:

  * `bgpAlwaysCompareMed`: Values are either `True` or `False`. If `bgpAlwaysCompareMed` isn't included in the output, the implied default value is `False`.

  * `bgpInterRegionCost`: Values are either `DEFAULT` or `ADD_COST_TO_MED`. If `bgpInterRegionCost` isn't included in the output, the implied default value is `DEFAULT`.




## Change a VPC network's dynamic routing and best path selection modes

To change either the current dynamic routing mode, best path selection mode, or both of a VPC network, follow these steps.

###  Console 

**Note:** The Google Cloud console only supports setting or changing a network's dynamic routing mode.

  1. In the Google Cloud console, go to the **VPC networks** page.

[Go to VPC networks](https://console.cloud.google.com/networking/networks/list)

  2. To view a network's details page, click the network's name.

  3. To modify the network, click edit**Edit**.

  4. In the **Dynamic routing mode** section, select **Regional** or **Global**.

  5. In the **Best path selection mode** section, select **Legacy** or **Standard**.

If you select standard best path selection mode, then you can do the following:

     * Choose if **Always compare MED** is enabled:

       * If selected, always compares MED values without considering ASN values.

       * If not selected, compares MED values within each neighbor's ASN values.

     * For **Inter region cost** , you can select the following:

       * **Default** : doesn't add inter-region costs to MED values.

       * **Add cost to MED** : adds inter-region costs to MED values.

  6. To confirm, click **Save**.




###  gcloud 

To set the dynamic routing and best path selection modes when creating a new VPC network, use the [`gcloud compute networks create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create):
    
    
    gcloud compute networks create NETWORK_NAME \
        --bgp-routing-mode=DYNAMIC_ROUTING_MODE \
        --bgp-best-path-selection-mode=BEST_PATH_SELECTION_MODE \
        --project=PROJECT_ID

To change the dynamic routing and best path selection modes for an existing VPC network, use the [`gcloud compute networks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/networks/create):
    
    
    gcloud compute networks update NETWORK_NAME \
        --bgp-routing-mode=DYNAMIC_ROUTING_MODE \
        --bgp-best-path-selection-mode=BEST_PATH_SELECTION_MODE \
        --project=PROJECT_ID

If you set `--bgp-best-path-selection-mode=STANDARD`, you can also use the `--bgp-bps-always-compare-med`, `--no-bgp-bps-always-compare-med`, or `--bgp-bps-inter-region-cost` flag. In the following example, you specify either `create` or `update`:
    
    
    gcloud compute networks {create|update} NETWORK_NAME \
        --bgp-routing-mode=DYNAMIC_ROUTING_MODE \
        --bgp-best-path-selection-mode=STANDARD \
        --[no-]bgp-bps-always-compare-med \
        --bgp-bps-inter-region-cost=COST_MODE \
        --project=PROJECT_ID

Replace the following:

  * `NETWORK_NAME`: the name of the VPC network to modify
  * `DYNAMIC_ROUTING_MODE`: the dynamic routing mode to use—specify `REGIONAL` or `GLOBAL`. The default value is `REGIONAL`.
  * `BEST_PATH_SELECTION_MODE`: the best path selection mode to use—specify `LEGACY` or `STANDARD`. The default value is `LEGACY`.
  * The following are only applicable when using `STANDARD` best path selection mode. These flags must be omitted if you use `LEGACY` best path selection mode.
  * `--bgp-bps-always-compare-med`: use this flag to always compare MED without considering the neighbor ASN values.
  * `--no-bgp-bps-always-compare-med`: use this flag to conditionally compare MED values within each neighbor ASN.
  * `COST_MODE`: controls whether an inter-region cost is added to the received MED value—specify `DEFAULT` or `ADD-COST-TO-MED`. 
    * `DEFAULT` doesn't add inter-region costs to MED values.
    * `ADD-COST-TO-MED` adds inter-region costs to MED values.



###  API 

To set the dynamic routing and best path selection modes when creating a new VPC network, use the [`networks.insert` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/insert):
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK_NAME
    {
      "routingConfig": {
        "routingMode": "DYNAMIC_ROUTING_MODE"
        "bgpBestPathSelectionMode": "BEST_PATH_SELECTION_MODE"
        "bgpAlwaysCompareMed": True | False
        "bgpInterRegionCost": "COST"
      }
    }
    

To change the dynamic routing and best path selection modes for an existing VPC network, use the [`networks.patch` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/networks/patch):
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/global/networks/NETWORK_NAME
    {
      "routingConfig": {
        "routingMode": "DYNAMIC_ROUTING_MODE"
        "bgpBestPathSelectionMode": "BEST_PATH_SELECTION_MODE"
        "bgpAlwaysCompareMed": True | False
        "bgpInterRegionCost": "COST"
      }
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the VPC network to modify
  * `NETWORK_NAME`: the name of the VPC network to modify
  * `DYNAMIC_ROUTING_MODE`: the dynamic routing mode to use—specify `REGIONAL` or `GLOBAL`. The default value is `REGIONAL`.
  * `BEST_PATH_SELECTION_MODE`: the best path selection mode to use—specify `LEGACY` or `STANDARD`. The default value is `LEGACY`.
  * `COST`: controls whether an inter-region cost is added to the received MED value—specify `DEFAULT` or `ADD-COST-TO-MED`.
  * `DEFAULT` does not add inter-region costs to MED values.
  * `ADD-COST-TO-MED` adds inter-region costs to MED values.



When `bgpAlwaysCompareMed` is `True`, always compare MED without considering the neighbor ASN values. When `False`, conditionally compare MED values within each neighbor ASN. The default is `False`. `bgpAlwaysCompareMed` is optional when `bgpBestPathSelectionMode` is `STANDARD` but must be omitted when `bgpBestPathSelectionMode` is `LEGACY`.

When `bgpBestPathSelectionMode` is `STANDARD`, `bgpInterRegionCost` is optional but must be omitted when `bgpBestPathSelectionMode` is `LEGACY`.

## What's next?

  * [Dynamic routing mode effects on learned routes](https://docs.cloud.google.com/network-connectivity/docs/router/concepts/learned-routes#dynamic-routing-mode-effects-on-learned-routes)
  * [Create a Cloud Router to connect a VPC network to a peer network](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/create-router-vpc-network)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
