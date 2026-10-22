---
url: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/explore-entities-and-alerts-investigation/
title: Investigate entities and alerts \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:14.058188+00:00
---

# Investigate entities and alerts  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/investigate/working-with-cases/explore-entities-and-alerts-investigation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Investigate entities and alerts

Supported in:

Google SecOps  [ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

This document explains how to investigate case-related entities and alerts using the **Security Graph** (referred to as the **Entity Graph** in the enhanced experience) page in Google Security Operations The **Security Graph** page provides a visual representation of entity relationships and alert activity,helping you understand the context, sequence, and impact of suspicious events. This document also explains how to interpret entity types, explore correlations, and perform follow-up actions based on the visual analysis.

You can explore the entities and alerts associated with a case using the **Security Graph** page. In the center of the page, a visual representation—called a visual family—displays how alerts and entities relate to one another.

This view helps you:

  * Understand the cause-and-effect relationships between entities and alerts
  * See the chronological order of events
  * Identify connections between suspicious events



## Identify visual family elements

The visual family includes two types of nodes:

  * **Entities** : Displayed as hexagons
  * **Artifacts** : Displayed as circles



Color is used to convey meaning:

  * **Blue hexagons** : Internal entities
  * **Green circles** : Internal artifacts
  * **Red** : Indicates suspicious items



## Identify internal and external entities

Entities can appear in two styles:

  * Color-filled shapes represent internal entities
  * Outlined-only shapes represent external entities



For example, an IP address that belongs to a known internal network would appear as a color-filled hexagon, signaling it's internal. Conversely, an IP from outside the network appears as an outlined hexagon, indicating it's external. 

**Note:** Artifacts are always internal and are always displayed as a color-filled circle. 

## Understand entity relationships in the visual family

The **Security Graph** page shows how entities and artifacts relate to each other using visual cues and connections. To identify different types of entities and artifacts, click help **Help**. This opens the **Entity Legend** , which defines each shape and color used in the visual.

### Relationship types

Entities and artifacts may be linked by lines that represent their relationships. There are two types of relationships:

  * **Actions** : Displayed as arrows; indicate a direct action (for example, sending an email)
  * **Connections** : Displayed as dotted lines; show general associations (for example, a user tied to a machine hostname)



For example:

  * An arrow may connect two user entities if one sends an email to the other.
  * A dotted line might connect a user entity with a host entity they've accessed



### Visual families and mapping rules

Entities and artifacts are derived from mapping rules, and their relationships (connected by lines) are defined by visual families.

If visual families aren't configured, entities and artifacts still appear in the center workspace. However, no connecting lines are displayed between them.

### Configure mapping and visual families

To configure mapping rules or assign visual families on the **Event Configuration** page, click  settings **Settings** in one of the following places in the Google SecOps platform:

  * [Alerts Events tab](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/deciding-what-events-to-configure)
  * [Ontology Status page](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/viewing-model-family-and-field-mapping)



For more details about how to configure mapping and assign visual families, see [Configure mapping and assign visual families](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/configure-mapping-and-assign-visual-families). 

## Use the Security Graph page

To analyze entities and alerts visually, open a case and on the **Cases** page, click **View Security Graph** (or click **View Entity Graph** if you are using the enhanced cases experience). The **Security Graph** page contains the following workspace elements: 

  * **Left pane** : displays the alerts associated with the selected case and their corresponding timestamps. 
  * **Middle pane** : displays a graph of interconnected entities, a graphical alert timeline, and playback controls. 
  * **Side drawer** : shows details of the selected alerts or entities, including raw enrichment data (if available). When you select an alert or an event, the side drawer displays the relevant information.  
If you're a Google SecOps unified user, you'll see an **Explore** button at the bottom of this drawer. Click it to continue investigating the alert on a dedicated page. For more information, see [Investigation views](https://docs.cloud.google.com/chronicle/docs/investigation/investigation-views). 
  * **Bottom of page** : displays video control buttons to play the events, together with a visual time range (which can be manipulated further using  add **Add** and  remove **Remove**). Click  play_arrow **Play Event** to go through the events in chronological order on the graph. 



Click an alert in the left pane to highlight the related entities highlighted in the middle pane. The node indicating this alert appears bigger than the other nodes (alerts) on the graph. Hold the pointer over the nodes to see their respective alert names. Entities not involved in the selected alert appear dimmed (unavailable).

The following options are available on the **Security Graph** page: 

Options | Descriptions  
---|---  
[ ![exploreentities1](https://docs.cloud.google.com/static/chronicle/images/soar/exploreentities1.png)](https://docs.cloud.google.com/static/chronicle/images/soar/exploreentities1.png) |  **Fit to Screen** : autofits the graph to fit the entire visible area.   
[ ![exploreentities2](https://docs.cloud.google.com/static/chronicle/images/soar/exploreentities2.png)](https://docs.cloud.google.com/static/chronicle/images/soar/exploreentities2.png) |  **Circular layout** : default graph layout. Click **Change Graph Layout** for other options.   
[ ![exploreentities3](https://docs.cloud.google.com/static/chronicle/images/soar/exploreentities3.png)](https://docs.cloud.google.com/static/chronicle/images/soar/exploreentities3.png) |  **Play Event** : plays all alerts of the case in sequence. Highlights associated entities for each step. The graph displays the alert flow, highlighting each played alert with a larger node.   
[ ![exploreentities4](https://docs.cloud.google.com/static/chronicle/images/soar/exploreentities4.png)](https://docs.cloud.google.com/static/chronicle/images/soar/exploreentities4.png) |  **Next Event** : plays the next alert in order. Starts from the top of the list.   
[ ![exploreentities5](https://docs.cloud.google.com/static/chronicle/images/soar/exploreentities5.png)](https://docs.cloud.google.com/static/chronicle/images/soar/exploreentities5.png) |  **Previous Event** : steps back to the previous alert. Disabled until the first alert is played.   
[ ![exploreentities6](https://docs.cloud.google.com/static/chronicle/images/soar/exploreentities6.png)](https://docs.cloud.google.com/static/chronicle/images/soar/exploreentities6.png) |  **Fast Forward** and **Fast Backward** : plays alerts at 3× speed, in chronological (ascending) or reverse chronological (descending) order, respectively.   
[ ![exploreentities7](https://docs.cloud.google.com/static/chronicle/images/soar/exploreentities7.png)](https://docs.cloud.google.com/static/chronicle/images/soar/exploreentities7.png) |  **Time Range Slider** : expands or narrows the visible time range on the X-axis.   
[ ![exploreentities8](https://docs.cloud.google.com/static/chronicle/images/soar/exploreentities8.png)](https://docs.cloud.google.com/static/chronicle/images/soar/exploreentities8.png) |  This opens an entity legend.  
  
  
## Take manual action after investigation

After reviewing the visual timeline, you can take further manual actions for further investigation. For example, you can scan IP addresses to check for known threats or investigate downstream effects like data exfiltration. 

Common follow-up actions include: 

  * Quarantine computers 
  * Check and scan infected systems 
  * Investigate suspicious emails 
  * Identify missing or exfiltrated data. 

**Note:** For more information on how mapping rules and visual families are configured, see [Ontology overview](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/ontology/ontology-overview). 

## Supported entity types in Google SecOps

This section provides a list of the supported entity types that can be utilized within the Google Security Operations platform for security investigation, analysis, and enrichment.

0: "SourceHostName"  
1: "SourceAddress"  
2: "SourceUserName"  
3: "SourceProcessName"  
4: "SourceMacAddress"  
5: "DestinationHostName"  
6: "DestinationAddress"  
7: "DestinationUserName"  
8: "DestinationProcessName"  
9: "DestinationMacAddress"  
10: "DestinationURL"  
11: "Process"  
12: "FileName"  
13: "FileHash"  
14: "EmailSubject"  
15: "ThreatSignature"  
16: "USB"  
17: "Deployment"  
18: "CreditCard"  
19: "PhoneNumber"  
20: "CVE"  
21: "ThreatActor"  
22: "ThreatCampaign"  
23: "GenericEntity"  
24: "ParentProcess"  
25: "ParentHash"  
26: "ChildProcess"  
27: "ChildHash"  
28: "SourceDomain"  
29: "DestinationDomain"  
30: "IPSET"  
31: "Cluster"  
32: "Application"  
33: "Database"  
34: "Pod"  
35: "Container"  
36: "Service"

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
