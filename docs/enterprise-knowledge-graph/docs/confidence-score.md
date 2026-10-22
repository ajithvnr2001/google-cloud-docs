---
url: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/confidence-score/
title: Understand reconciliation confidence score \u00a0|\u00a0 Enterprise Knowledge Graph \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:51:08.914652+00:00
---

# Understand reconciliation confidence score  |  Enterprise Knowledge Graph  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/confidence-score/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Enterprise Knowledge Graph ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)
  * [ Guides ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/overview)



Send feedback 

#  Understand reconciliation confidence score Stay organized with collections  Save and categorize content based on your preferences. 

Reconciliation (or clustering) confidence score is a metric for the confidence level of the assignment of an entity to a cluster. You can then filter out predictions that the clustering model is uncertain about and make decisions based on the remaining, confident outcomes.

## How a confidence score is produced

Clustering produces hard assignments: each entity is assigned to exactly one cluster. The confidence score describes the confidence level that a node belongs to its assigned cluster, valued between [0, 1].

  * 1.0 = very certain the entity belongs to its assigned cluster

  * 0.0 = very uncertain the entity belongs to its assigned cluster




There is a notion of similarity/distance between any pair of entities. Entity pairs within a cluster are more likely to have lower distances than pairs that span different clusters. The further away an entity is from other members of its cluster, the lower the confidence value.

Other clusters also influence the confidence score. If there are other clusters close to an entity, its confidence is diminished according to the distances from those clusters.

The cluster density is related to the distances between all entity pairs of the cluster, and also has an effect on the confidence value: for any entity at a fixed distance from the cluster, the confidence value is high if the cluster density is low; and the confidence is low if the cluster density is high.

For the reconciliation pipeline to scale to millions or billions of entities, the confidence score calculation exploits randomized sampling methods to limit the computational complexity. As such, confidence scores are bucketed into 0.1-sized intervals. As a result, we recommend you do not depend on the exact confidence values to make review or human-in-the-loop decisions.

## Diagram Key

Use the following descriptions to understand the diagrams.

Description | Diagram  
---|---  
Entity | ![](https://docs.cloud.google.com/static/enterprise-knowledge-graph/docs/images/confidence-key-1-entity.png)  
A cluster of entities.   
  
Entity cluster depicted by a circle. Cluster spread is represented by the size of the circle. | ![](https://docs.cloud.google.com/static/enterprise-knowledge-graph/docs/images/confidence-key-3-cluster.png)  
Multiple entity clusters. Color coded: an entity and its assigned cluster share the same color. | ![](https://docs.cloud.google.com/static/enterprise-knowledge-graph/docs/images/confidence-key-4-multiple-clusters.png)  
In some cases we focus on a single entity and its relation to other clusters. All other entities are hidden from view.  
  
d_a: Distance from the entity to cluster A's centroid  
d_b: Distance from the entity to cluster B's centroid  
c: cluster confidence score of the entity | ![](https://docs.cloud.google.com/static/enterprise-knowledge-graph/docs/images/confidence-key-5-distance.png)  
  
## Illustrated examples

The follow diagrams serve as examples to help you visualize the high-level concept in determining confidence scores.

Situation | Diagram  
---|---  
The entity is assigned to cluster A. If A is the only cluster in the entire embedding space, then the confidence score will always be 1 regardless of the distance between them. | ![](https://docs.cloud.google.com/static/enterprise-knowledge-graph/docs/images/confidence-diag-1.png)  
A and B are clusters that have the same spread, and their centroids are equally distant from the entity.Both clusters have the same influence on the entity, so the confidence score is 0.5. | ![](https://docs.cloud.google.com/static/enterprise-knowledge-graph/docs/images/confidence-diag-2.png)  
The presence of other clusters nearby will exert their influence on the entity and dilute the confidence score.If there are three clusters of identical spread, and the entity is equally distant from all three, then the confidence score is 0.33. | ![](https://docs.cloud.google.com/static/enterprise-knowledge-graph/docs/images/confidence-diag-3.png)  
A and B are clusters that have the same spread, but the entity is closer to A than it is to B.A has a higher influence on the entity. Because the entity is also assigned to A, the confidence score will be larger than 0.5. | ![](https://docs.cloud.google.com/static/enterprise-knowledge-graph/docs/images/confidence-diag-4.png)  
A and B are clusters that have the same spread, but the entity is closer to B than it is to A.A's influence on the entity is thus lowered. The confidence score will be lower than 0.5. | ![](https://docs.cloud.google.com/static/enterprise-knowledge-graph/docs/images/confidence-diag-5.png)  
A has a larger spread than B, but their centroids are equally distant from the entity.A has a higher influence on the entity. Because the entity is also assigned to A, the confidence score will be larger than 0.5. | ![](https://docs.cloud.google.com/static/enterprise-knowledge-graph/docs/images/confidence-diag-6.png)  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
