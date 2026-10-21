---
url: https://docs.cloud.google.com/architecture/architecture-decision-records/
title: Architecture decision records overview \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:22:27.609491+00:00
---

# Architecture decision records overview  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/architecture-decision-records/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Architecture decision records overview Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2024-08-16 UTC

To help explain why your infrastructure or application teams make certain design choices, you can use architecture decision records (ADRs). This document explains when and how to use ADRs as you build and run applications on Google Cloud.

An ADR captures the key options available, the main requirements that drive a decision, and the design decisions themselves. You often store ADRs in a [Markdown](https://en.wikipedia.org/wiki/Markdown) file close to the codebase relevant to that decision. If someone needs to understand the background of a specific architectural decision, such as why you use a [regional Google Kubernetes Engine (GKE) cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/regional-clusters), they can review the ADR and then the associated code.

ADRs can also help you run more reliable applications and services. The ADR helps you understand your current state and troubleshoot when there's a problem. ADRs also build a collection of engineering decisions to help future decision choices and deployments.

## When to use ADRs

You use ADRs to track the key areas that you think are important to your deployment. Your ADR might include the following categories:

  * Specific product choices, such as the choice between [Pub/Sub and Cloud Tasks](https://docs.cloud.google.com/pubsub/docs/choosing-pubsub-or-cloud-tasks).
  * Specific product options and configurations, such as the use of regional GKE clusters with [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress) for highly available applications.
  * General architectural guidance, such as best practices for [Dockerfile](https://docs.docker.com/engine/reference/builder/) manifests.



Some specific examples that might prompt you to create an ADR could be for the following choices:

  * How and why do you set up high availability (HA) for your [Cloud SQL](https://docs.cloud.google.com/sql/docs/introduction) instances?
  * How do you approach uptime of GKE clusters? Do you use regional clusters? Do you use canary releases? Why or why not?



As you evaluate the products to use, the ADR helps to explain each of your decisions. You can revisit the ADR as the team evolves and learns more about the stack and additional decisions are made or adjusted. If you make adjustments, include the previous decision and why a change is made. This history keeps a record of how the architecture has changed as business needs evolve, or where there are new technical requirements or available solutions.

The following prompts help you to know when to create ADRs:

  * When you have a technical challenge or question and there's no existing basis for a decision, such as a recommended solution, standard operation procedure, blueprint, or codebase.
  * When you or your team offers a solution that's not documented somewhere accessible to the team.
  * When there are two or more engineering options and you want to document your thoughts and reasons behind the selection.



When you write an ADR, it helps to have potential readers in mind. The primary readers are members of the team that work on the technology covered by the ADR. Broader groups of potential readers of the ADR might include adjacent teams who want to understand your decisions, such as architecture and security teams.

You should also consider that the application might change owners or include new team members. An ADR helps new contributors understand the background of the engineering choices that were made. An ADR also makes it easier to plan future changes.

## Format of an ADR

A typical ADR includes a set of chapters. Your ADRs should help capture what you feel is important to the application and your organization. Some ADRs might be one page long, whereas others require a longer explanation.

The following example ADR outline shows how you might format an ADR to include the information that's important for your environment:

  * Authors and the team
  * Context and problem you want to solve
  * Functional and non-functional requirements you want to address
  * Potential critical user journey (CUJ) the decision impacts
  * Overview of the key options
  * Your decision and reasons behind the accepted choice



To help keep a record of decisions, you might include a timestamp for each decision to show when the choice was made.

## How ADRs work

ADRs work best when engineers, developers, or application owners can easily access information they contain. When they have a question about the why something is done a certain way, they can look at the ADR to find the answer.

To make the ADR accessible, some teams host it in a central wiki that's also accessible to business owners, instead of in their source control repository. When someone has a question about a specific engineering decision, the ADR is there to provide answers.

ADRs work well in the following scenarios:

  * **Onboarding** : New team members can easily learn about the project, and they can review the ADR if they have questions while they're learning a new codebase.
  * **Evolution of the architecture** : If there's a transfer of technology stack between teams, the new owners can review past decisions to understand the current state. The team can also review past decisions when there's a new technology available to them. The ADR can help teams avoid a repeat of the same discussion points, and it can help provide historical context when teams revisit topics.
  * **Sharing best practices** : Teams can align on best practices across the organization when ADRs detail why certain decisions were made and alternatives were decided against.



An ADR is often written in [Markdown](https://en.wikipedia.org/wiki/Markdown) to keep it lightweight and text-based. Markdown files can be included in the source control repository with your application code.

Store your ADRs close to your application code, ideally in the same version control system. As you make changes to your ADR, you can review previous versions from source control as needed.

You could also use another medium like a shared Google Doc or an internal wiki. These alternate locations might be more accessible to users not part of the ADR's team. Another option is to create your ADR in a source control repository, but mirror key decisions into a more accessible wiki.

## What's next

  * The [Cloud Architecture Center](https://docs.cloud.google.com/architecture) and the [Google Cloud Well-Architected Framework](https://docs.cloud.google.com/architecture/framework) provide additional guidance and best practices.
  * For some areas that might be in your ADR, see [Patterns for scalable and resilient apps](https://docs.cloud.google.com/architecture/scalable-and-resilient-apps).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2024-08-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2024-08-16 UTC."],[],[]] 
