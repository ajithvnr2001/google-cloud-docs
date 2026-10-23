---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management/
title: Fleet team management \u00a0|\u00a0 Fleet management \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:24:51.733408+00:00
---

# Fleet team management  |  Fleet management  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ Fleet management ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)



Send feedback 

#  Fleet team management Stay organized with collections  Save and categorize content based on your preferences. 

A common task for platform admins is making sure that application and service teams have the infrastructure resources they need to run their workloads. Depending on your organization, teams may need to use specific clusters, or they may need to run workloads on every cluster in a fleet, with appropriate access control set up for each team. Fleet team management features make it easier for admins to provision and manage infrastructure resources like this for teams, with each team acting as a separate "tenant" on your fleet. Teams can run and manage their workloads, as well as view logs, resource utilization, error rates, and other metrics, all scoped to their own set of clusters and namespaces.

This page is for platform admins and application team members who want to learn about fleet team management features.

## Fleet team management overview

Fleet team management is based around two key concepts that give admins a "team-level" abstraction to use when managing fleets:

  * **Team scopes** let you define subsets of fleet resources on a per-team basis, with each scope associated with one or more fleet member clusters. Team scopes can include clusters on Google Cloud or outside Google Cloud, though all the clusters must be members of the same fleet. A cluster can be associated with more than one team scope, letting different teams run workloads on the same cluster.
  * **Fleet namespaces** provide a way to control who has access to specific namespaces within your fleet. By default, any namespaces with the same name defined on clusters in the fleet are treated as if they were the same namespace. However, fleet team management provides a way to add more granular control over namespaces. You can create fleet namespaces within specific team scopes, and then grant team members access to them _only on clusters within their team scope_. Fleet namespaces can be used in the same way as any other Kubernetes namespace on the member clusters in the team scope. Platform admins can create fleet namespaces themselves, or, with some extra permissions, delegate namespace creation to team admins.



### Team management example

For example, suppose you are a platform admin for the company Cymbal Group setting up resources for two teams on a single fleet. 

  * The **Backend team** consists of one Google Group, `backend-team@cymbalgroup.com`. You decide that this team can run workloads on cluster 1 and cluster 2, using their namespace `backend`. You create a team scope including the two clusters, and define a `backend` fleet namespace within that scope.
  * The **Frontend team** consists of two Google Groups, `frontend-admin@cymbalgroup.com` and `frontend-dev@cymbalgroup.com`. You decide that the frontend team can run workloads on cluster 2 and cluster 3, using the namespaces `frontend-foo` and `frontend-bar`. Again you create a team scope with the two clusters, and define two fleet namespaces within that scope.



![Diagram showing an example of two teams using a fleet](https://docs.cloud.google.com/static/kubernetes-engine/fleet-management/images/team-example.svg)

As you can see in the diagram, once you have set up the teams, both teams can use cluster 2, with each team using their own namespaces. In addition, the Backend team can use their namespace on cluster 1, and the Frontend team can use their namespaces on cluster 3. Both teams can run their workloads on the clusters and view their own resources without having to consider the other team. 

In each case, you specify that the team leads (individual user Dana in the case of the Backend team, `frontend-admin` group members in the case of the Frontend team) have `admin` access to the team scope, meaning that they can create roles and role bindings within the scope, while the remaining team members have `editor` access. 

While you could set up all this configuration manually with `kubectl` or other tools, using team management features makes it easier to quickly onboard the teams, and lets admins and team members use additional features based on team scopes, such as team-scoped metrics.

In a real life situation, you would also probably have separate fleets for your production, development, and test environments. You would create team scopes for the Frontend and Backend teams within each of these fleets, providing the teams with their own production, development, and test clusters. You can find out more about this in our fleet [best practices](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/best-practices) and [examples](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-concepts/examples).

## Team-enabled features

After team scopes are set up, application operators and admins can view team-scoped information such as resource utilization, logs, errors by namespace, and other metrics from across their scope, making it easier for them to assess how they're using their total resources, troubleshoot problems, and more. You can find out more about these in [Use the team overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management-overview). Team scopes can also be used for [sequencing upgrade rollouts](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-rollout-sequencing).

## Accessing team scopes

We recommend that team members access their team scope clusters with `kubectl` using the special cluster credentials for the [Connect Gateway](https://docs.cloud.google.com/kubernetes-engine/enterprise/multicluster-management/gateway). The Connect Gateway is a consistent, secured service that lets users log in with their Google IDs to any cluster in the fleet, including using Google Groups for authorization. While this isn't strictly required to authenticate to GKE clusters on Google Cloud, using the gateway credentials provides a simple, consistent way to authenticate to fleet member clusters, even across projects. Fleet team management does not currently support third-party identity providers.

## Existing resources

Fleet team management can also be used to "onboard" existing namespaces and clusters used by your organization's teams, letting admins and teams start using team-based features with existing workloads. If you create a fleet namespace and there is an existing Kubernetes namespace with that name on one of the clusters associated with its team scope, that namespace will be considered to be an instantiation of the fleet namespace, and hence part of the team scope.

**Note:** There are currently no warnings or other notifications provided if you create a fleet namespace that has the same name as an existing Kubernetes namespace in your scope. Be careful!

## What's next?

  * If you're a platform admin, follow the instructions in [Set up teams](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/setup-teams) to set up, configure, and manage team scopes and namespaces.
  * Learn how to view team-level metrics and other team-specific information in [Use the team overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/team-management-overview) (limited preview only).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
