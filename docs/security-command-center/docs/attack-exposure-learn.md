---
url: https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn/
title: Overview of attack exposure scores and attack paths \u00a0|\u00a0 Security Command Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T06:50:43.575807+00:00
---

# Overview of attack exposure scores and attack paths  |  Security Command Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Security Command Center ](https://docs.cloud.google.com/security-command-center/docs)
  * [ Guides ](https://docs.cloud.google.com/security-command-center/docs/security-command-center-overview)



Send feedback 

#  Overview of attack exposure scores and attack paths Stay organized with collections  Save and categorize content based on your preferences. 

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation)) The Security Command Center Enterprise service tier will shut down on May 21, 2027. If your organization uses the Enterprise service tier, then the organization will automatically move to the Premium service tier on or after May 21, 2027. Contact your account representative or a [Google Cloud sales specialist](https://cloud.google.com/contact) if you have questions. 

The Security Command Center Risk Engine generates attack exposure scores and attack paths to help you identify and prioritize high-risk exposure routes to your high-value cloud resources. These simulations evaluate how external exposures, vulnerabilities, misconfigurations, and toxic combinations interact so that you can focus remediation on critical threats.

## Overview of attack exposure scores and attack paths

Attack path scores and attack paths are generated for the following:

  * External exposure ([Preview](https://cloud.google.com/products/#product-launch-stages)), vulnerability, and misconfiguration findings that expose the resource instances in your effective high-value resource set.
  * The resources in your effective high-value resource set.
  * Issues in Security Command Center Premium or Enterprise, which contain [toxic combinations and chokepoints](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview).



**Support statement:** Risk Engine attack path simulations are subject to certain supportability constraints and limits. For more information, see [Attack exposure feature support](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features#gc-services-in-aps). 

To use attack exposure scores and attack paths, you must activate Security Command Center Premium or Enterprise at the organization level. You can't use attack exposure scores and attack paths with project-level activations.

## Attack paths represent possibilities

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

You won't see evidence of an actual attack in an attack path.

Risk Engine generates attack paths and attack exposure scores by simulating what hypothetical attackers could do if they gained access to your Google Cloud environment and discovered the attack paths and vulnerabilities that Security Command Center has already found.

Each attack path shows you one or more attack methods an attacker could use if they gained access to a particular resource. Don't confuse these attack methods with actual attacks.

Similarly, a high attack-exposure score on any of the following does not mean that an attack is in progress:

  * A Security Command Center finding or resource
  * A Security Command Center Premium or Enterprise issue



To watch for actual attacks, monitor the `THREAT` class findings produced by the threat detection services, like [Event Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-event-threat-detection-overview) and [Container Threat Detection](https://docs.cloud.google.com/security-command-center/docs/concepts-container-threat-detection-overview).

For more information, see the following sections on this page:

  * Attack exposure scores
  * Attack paths
  * Attack path simulations



## Attack exposure scores

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

An attack exposure score appears for the following:

  * A Security Command Center finding or resource
  * A Security Command Center Premium or Enterprise issue



An _attack exposure score_ is a measure of how exposed resources are to potential attack if a malicious actor were to gain access to your Google Cloud environment.

An attack exposure score on a [toxic combination or chokepoint](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview) finding is referred to as a _toxic combination score_ in some contexts, such as the **Findings** page in the Google Cloud console.

In descriptions of how scores are calculated, in general guidance about prioritizing finding remediation, and in certain other contexts, the term _attack exposure score_ also applies to toxic combination scores.

On a finding, the score is a measure of how much a detected security issue exposes one or more high-value resources to potential cyberattacks. On a high-value resource, the score is a measure of how exposed the resource is to potential cyberattacks.

Use the scores on external exposure, software vulnerability, misconfiguration, and toxic combination or chokepoint findings to prioritize the remediation of those findings.

Use attack exposure scores on resources to proactively secure the resources that are the most valuable to your business.

**Caution:** To get scores that accurately reflect your security priorities, you must define a high-value resource set. For more information, see High-value resource sets.

In the attack path simulations, Risk Engine always starts the simulated attacks from the public internet. Consequently, the attack exposure scores don't account for any possible exposure to malicious or negligent internal actors.

### Findings that receive attack exposure scores

Attack exposure scores are applied to active finding classes that are listed in [Supported finding categories](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features#aes-finding-support).

Attack path simulations include only active and unmuted findings in their calculations. Findings that have a status of `INACTIVE` or `MUTED` are not included in the simulations, don't receive scores, and are not included in attack paths.

**Note:** Muting findings does not generally affect the environment state during simulations. For example, muting an `Overprivileged Service Account` finding won't remove the Service Account or its permissions from the simulations; this action only causes the finding to not get scored. The exception to this is muting vulnerability findings, in which case the `MUTED` status is considered an indication that the vulnerability is not exploitable. Be careful not to expose your environment to unnecessary risk by disabling vulnerability findings that might still be exploitable.

### Resources that receive attack exposure scores

Attack path simulations calculate attack exposure scores for supported resource types in your high-value resource set. You specify which resources belong in the high-value resource set by creating [_resource value configurations_](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-learn#resource-value-configurations).

If a resource in a high-value resource set has an attack exposure score of 0, the attack path simulations did not identify any paths to the resource that a potential attacker could leverage.

Attack path simulations support the following resource types:

  * `aiplatform.googleapis.com/Dataset`
  * `aiplatform.googleapis.com/Featurestore`
  * `aiplatform.googleapis.com/MetadataStore`
  * `aiplatform.googleapis.com/Model`
  * `aiplatform.googleapis.com/ReasoningEngine`
  * `aiplatform.googleapis.com/TrainingPipeline`
  * `artifactregistry.googleapis.com/Repository`
  * `bigquery.googleapis.com/Dataset`
  * `cloudbuild.googleapis.com/BitbucketServerConfig`
  * `cloudbuild.googleapis.com/BuildTrigger`
  * `cloudbuild.googleapis.com/Connection`
  * `cloudbuild.googleapis.com/GithubEnterpriseConfig`
  * `cloudbuild.googleapis.com/Repository`
  * `cloudbuild.googleapis.com/WorkerPool`
  * `cloudfunctions.googleapis.com/CloudFunction`
  * `compute.googleapis.com/Instance`
  * `container.googleapis.com/Cluster`
  * `dataproc.googleapis.com/Cluster`
  * `dataproc.googleapis.com/Job`
  * `run.googleapis.com/Job`
  * `run.googleapis.com/Service`
  * `spanner.googleapis.com/Instance`
  * `sqladmin.googleapis.com/Instance`
  * `storage.googleapis.com/Bucket`



### Score calculation

Each time the attack path simulations run, they recalculate the attack exposure scores. Each attack path simulation actually runs several simulations in which a simulated attacker tries known attack methods and techniques to reach and compromise the valued resources.

Attack path simulations run on a schedule, and new results are available up to every 48 hours. Simulation runs aren't triggered by the creation, modification, or deletion of resources or resource value configurations.

The simulations calculate the scores using a variety of metrics, including the following:

  * The priority value that is assigned to the high-value resources that are exposed. The priority values that you can assign have the following values: 
    * HIGH = 10
    * MED = 5
    * LOW = 1
  * The number of possible paths an attacker could take to reach a given resource.
  * The number of times in which a simulated attacker is able to reach and compromise a high-value resource at the end of a given attack path, expressed as a percentage of the total number of simulations.
  * For findings only, the number of high-value resources that are exposed by the detected external exposure, vulnerability, or misconfiguration.



For resources, attack exposure scores can be in the range from 0 to 10.

At a high level, the simulations calculate resource scores by multiplying the percentage of successful attacks by the numerical priority value of the resources.

For findings, scores don't have a fixed upper limit. The more often a finding occurs on attack paths to exposed resources in the high-value resource set, and the higher the priority values of those resources, the higher the score is.

At a high level, the simulations calculate finding scores by using the same calculation as they do for resource scores, but for finding scores, the simulations then multiply the result of the calculation by the number of high-value resources the finding exposes.

### Changing scores

The scores can change each time an attack path simulation runs. A finding or resource that has a score of zero today might have a non-zero score tomorrow.

Scores change for a variety of reasons, including the following:

  * The detection or remediation of a vulnerability that directly or indirectly exposes a high-value resource.
  * The addition or removal of resources in your environment.



Changes to findings or resources after a simulation has run are not reflected in the scores until the next simulation runs.

### Using scores to prioritize finding remediations

To effectively prioritize the remediation of findings based on their attack exposure or toxic combination scores, consider the following points:

  * Any finding that has a score that is greater than zero exposes a high-value resource to potential attack in some way, so the remediation should be prioritized over findings that have a score of zero.
  * The higher the score of a finding is, the more the finding exposes your high-value resources and the higher you should prioritize its remediation.



Generally, place the highest priority on the remediation of the findings that have the highest scores and that most effectively block the attack paths to your high-value resources.

If the scores of a toxic combination and chokepoint finding and a finding in another finding class are roughly equal, prioritize the remediation of the toxic combination and chokepoint finding, because it represents a complete path from the public internet to one or more high-value resources that an attacker can potentially follow if they gained access to your cloud environment.

On the Security Command Center **Findings** page in the [Google Cloud console](https://console.cloud.google.com/security/command-center/findingsv2), you can sort the findings on the page panel by score by clicking the column heading.

In the Google Cloud console, you can also view the findings with the highest scores by adding a filter to the findings query that returns only findings with an attack exposure score greater than a number that you specify.

On the **Cases** page in Security Command Center Enterprise, you can also sort the toxic combinations and chokepoint cases by the attack exposure score.

#### Findings that can't be remediated

In some cases, you might not be able to remediate a finding with a high attack exposure score, either because it represents a known and accepted risk, or because the finding cannot be remediated immediately. In these cases, you might need to mitigate the risk in other ways. Reviewing the associated attack path might give you ideas for other possible mitigations.

### Secure resources by using attack exposure scores

A non-zero attack exposure score on a resource means that the attack path simulations identified one or more attack paths from the public internet to the resource.

To see the attack exposure scores for your high-value resources, follow these steps:

  1. In the Google Cloud console, go to the **Assets** page of Security Command Center.

[Go to Assets](https://console.cloud.google.com/security/command-center/assetsv2/resources)

  2. Select the organization where you activated Security Command Center.

  3. Select the **High value resource set** tab. The resources in your high-value resource set are displayed in descending order of attack exposure score.

  4. Display the attack paths for a resource by clicking the number on its row in the **Attack exposure score** column. The attack paths from the public internet to the resource are displayed.

  5. Review the attack paths. For information about how to interpret the attack paths, see Attack paths.

  6. To display a detail window with links to view related findings, click a node.

  7. Click a related findings link. The **Finding** window opens with detail about the finding and how to remediate it.




You can also view the attack exposure scores of your high-value resources on the **Attack path simulations** tab in [Settings](https://console.cloud.google.com/security/command-center/config) > **Attack Path simulation** tab. Click **View valued resources used in last simulation**.

The **High value resource set** tab is also available in the [**Assets** page](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console#view-resources-in-secops-console) of the Security Operations console.

### Attack exposure scores of `0`

An attack exposure score of `0` on a resource means that, in the latest attack path simulations, Security Command Center did not identify any potential paths an attacker could take to reach the resource.

An attack exposure score of `0` on a finding means that, in the latest attack simulation, the simulated attacker couldn't reach any high-value resources through the finding.

However, an attack exposure score of `0` does not mean that there is no risk. An attack exposure score reflects exposure of supported Google Cloud service, resources, and Security Command Center findings to potential threats originating from the public internet. For example, the scores don't take into account threats from internal actors, zero-day vulnerabilities, or third-party infrastructure.

### No attack exposure score

If a finding or resource does not have a score, it can be for the following reasons:

  * The finding was generated after the latest attack path simulation.
  * The resource was added to your high-value resource set after the latest attack path simulation.
  * The attack exposure feature doesn't support the finding category or the resource type.



For a list of the supported finding categories, see [Risk Engine feature support](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features).

For a list of supported resource types, see Resources that receive attack exposure scores.

## Resource values

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

Although all of your resources on Google Cloud have value, Security Command Center identifies attack paths and calculates attack exposure scores for only the resources that you designate as _high-value resources_ (sometimes referred to as _valued resources_).

### High-value resources

A high-value resource on Google Cloud is a resource that is especially important for your business to protect from potential attacks. For example, your high-value resources might be the resources that store your valuable or sensitive data or that host your business-critical workloads.

You designate a resource as a high-value resource by defining the attributes of the resource in a _resource value configuration_. Up to a limit of 1,000 resource instances, Security Command Center treats any resource instance that matches the attributes that you specify in the configuration as a high-value resource.

### Priority values

Among the resources that you designate as high value, you are likely to need to prioritize the security of some more than others. For example, a set of data resources might contain high-value data, but certain of those data resources might contain data that is more sensitive than the rest.

So that your scores reflect your need to prioritize the security of the resources within your high-value resource set, you assign a priority value in the resource value configurations that designates resources as high value.

If you use Sensitive Data Protection, you can also prioritize resources automatically by the sensitivity of the data that the resources contain.

#### Set resource priority values manually

In a resource value configuration, you assign a priority to the matching high-value resources by specifying one of the following priority values:

  * `LOW` = 1
  * `MEDIUM` = 5
  * `HIGH` = 10
  * `NONE` = 0



If you specify a priority value of `LOW` in a resource value configuration, the matching resources are still high-value resources; the attack path simulations just treat them with a lower priority and assign them a lower attack exposure score than high-value resources that have a priority value of `MEDIUM` or `HIGH`.

If multiple configurations assign different values for the same resource, the highest value applies, unless a configuration assigns a value of `NONE`.

A resource value of `NONE` excludes the matching resources from being considered a high-value resource and overrides any other resource value configurations for the same resource. For this reason, make sure that any configuration that specifies `NONE` applies to only a limited set of resources.

### Set resource priority values automatically by data sensitivity

If you use [Sensitive Data Protection discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) and [publish the data profiles to Security Command Center](https://docs.cloud.google.com/sensitive-data-protection/docs/send-profiles-to-scc), then you can configure Security Command Center to automatically set the priority value of certain high-value resources by the sensitivity of the data that the resources contain.

You enable data-sensitivity prioritization when you specify the resources in a [resource value configuration](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set#create_a_resource_value_configuration).

When enabled, if Sensitive Data Protection discovery classifies the data in a resource to be either `MEDIUM` or `HIGH` sensitivity, the attack path simulations by default set the priority value of the resource to that same value.

The [data sensitivity levels](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitivity-risk-calculation#sensitivity-level) are defined by Sensitive Data Protection, but you can interpret them as follows:

High sensitivity data
    Sensitive Data Protection discovery found at least one instance of high-sensitivity data in the resource.
Medium sensitivity data
    Sensitive Data Protection discovery found at least one instance of medium-sensitivity data in the resource and no instances of high-sensitivity data.
Low sensitivity data
    Sensitive Data Protection discovery did not detect sensitive data or any freeform text or unstructured data in the resource.

If Sensitive Data Protection discovery identifies only low-sensitivity data in a matching data resource, the resource is not designated as a high-value resource.

If you need data resources that contain only low-sensitivity data to be designated as high-value resources with a low priority, create a duplicate resource value configuration, but specify a priority value of `LOW` instead of enabling data-sensitivity prioritization. The configuration that uses Sensitive Data Protection overrides the configuration that assigns the `LOW` priority value, but only for resources that contain `HIGH` or `MEDIUM` sensitivity data.

You can change the default priority values that Security Command Center uses when sensitive data is detected in the resource value configuration.

For more information about Sensitive Data Protection, see [Sensitive Data Protection overview](https://docs.cloud.google.com/sensitive-data-protection/docs/sensitive-data-protection-overview).

#### Data-sensitivity prioritization and the default high-value resource set

Before you create your own high-value resource set, Security Command Center uses a default high-value resource set to calculate attack exposure scores and attack paths.

If you use Sensitive Data Protection discovery, Security Command Center automatically adds instances of supported data resource types that contain `HIGH` or `MEDIUM` sensitivity data to the default high-value resource set.

#### Supported Google Cloud resource types for automated data-sensitivity priority values

Attack path simulations can automatically set priority values based on data-sensitivity classifications from [Sensitive Data Protection discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) for only the following data resource types:

  * `aiplatform.googleapis.com/Dataset`
  * `bigquery.googleapis.com/Dataset`
  * `sqladmin.googleapis.com/Instance`
  * `storage.googleapis.com/Bucket`



#### Supported AWS resource types for automated data-sensitivity priority values

Attack path simulations can automatically set priority values based on data-sensitivity classifications from [Sensitive Data Protection discovery](https://docs.cloud.google.com/sensitive-data-protection/docs/data-profiles) for only the following AWS data resource types:

  * Amazon S3 bucket



## High-value resource sets

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

A _high-value resource set_ is a defined collection of the resources in your Google Cloud environment that are the most important to secure and protect.

To define your high-value resource set, you need to specify which resources in your Google Cloud environment belong in your high-value resource set. Until you define your high-value resource set, attack exposure scores, attack paths, and toxic combination findings don't accurately reflect your security priorities.

You specify the resources in your high-value resource set by creating _resource value configurations_. The combination of all of your resource value configurations defines your high-value resource set. For more information, see Resource value configurations.

Until you define your first resource value configuration, Security Command Center uses a _default high-value resource set_. The default set applies across your organization to all of the resource types that attack path simulations support. For more information, see Default high-value resource set.

To view the high-value resource set that was used in the last attack path simulation, including the attack exposure scores and matching configurations, see [View the high-value resource set](https://docs.cloud.google.com/security-command-center/docs/work-with-resources-in-the-console#hvr).

### Resource value configurations

You manage the resources in your high-value resource set with resource value configurations.

You create resource value configurations on the [Attack path simulation](https://console.cloud.google.com/security/command-center/config/attack-path-simulation) tab of the Security Command Center **Settings** page in the Google Cloud console.

In a resource value configuration, you specify the attributes that a resource must have for Security Command Center to add it to your high-value resource set.

The attributes that you can specify include the resource type, resource tags, resource labels, and the parent project, folder, or organization.

You also assign a resource value to the resources in a configuration. The resource value prioritizes the resources in a configuration relative to the other resources in the high-value resource set. For more information, see Resource values.

You can create up to 100 resource value configurations in a Google Cloud organization.

Together, all of the resource value configurations that you create define the high-value resource set that Security Command Center uses for the attack path simulations.

### Resource attributes

For a resource to be included in your high-value resource set, its attributes must match the attributes that you specify in a resource value configuration.

The attributes that you can specify include:

  * A resource type or `Any`. When `Any` is specified, the configuration applies to all of the supported resource types within the specified scope. `Any` is the default value.
  * A scope (the parent organization, folder, or project) within which the resources must reside. The default scope is your organization. If you specify an organization or folder, the configuration also applies to the resources in the child folders or projects.
  * Optionally, one or more [tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) or [labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) that each resource must contain.



If you specify one or more resource value configurations, but no resources in your Google Cloud environment match the attributes specified in any of the configurations, Security Command Center generates an `SCC Error` finding and falls back to the default high-value resource set.

### Default high-value resource set

Security Command Center uses a default high-value resource set to calculate attack exposure scores when no resource value configurations are defined or when no defined configurations match any resources.

Security Command Center assigns resources in the default high-value resource a priority value of `LOW`, unless you use Sensitive Data Protection discovery, in which case, Security Command Center assigns resources that contain high-sensitivity or medium-sensitivity data a corresponding priority value of `HIGH` or `MEDIUM`.

Risk Engine uses heuristics to identify the risk exposure score of resources by analyzing common industry terminology that is used within tags, labels, and resource names. The most critical security issues in the default high-value resource set are assigned risk exposure scores first. Then, Risk Engine calculates the attack exposure score for non-production resources, which are considered of lower importance.

If you have at least one resource value configuration that matches at least one resource in your environment, Security Command Center stops using the default high-value resource set.

To receive attack exposure and toxic combination scores that accurately reflect your security priorities, replace the default high-value resource set with your own high-value resource set. For more information, see [Define and manage your high-value resource set](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set).

The following list shows the resource types that are included in the default high-value resource set:

  * `aiplatform.googleapis.com/Model`
  * `aiplatform.googleapis.com/ReasoningEngine`
  * `artifactregistry.googleapis.com/Repository`
  * `bigquery.googleapis.com/Dataset`
  * `cloudbuild.googleapis.com/BuildTrigger`
  * `cloudfunctions.googleapis.com/CloudFunction`
  * `compute.googleapis.com/Instance`
  * `run.googleapis.com/Job`
  * `run.googleapis.com/Service`
  * `spanner.googleapis.com/Instance`
  * `sqladmin.googleapis.com/Instance`
  * `storage.googleapis.com/Bucket`



### Limit on resources in a high-value resource set

Security Command Center limits the number of resources in a high-value resource set to 1,000 per cloud service provider.

If the attribute specifications in one or more resource value configurations are very broad, the number of resources that match the attribute specifications can exceed 1,000.

When the number of matching resources exceeds the limit, Security Command Center excludes resources from the set until the number of resources is within the limit. Security Command Center excludes resources with the lowest assigned value first. Among resources with the same assigned value, Security Command Center excludes resource instances by an algorithm that distributes the excluded resources across resource types.

A resource that is excluded from the high-value resource set is not considered in the calculation of attack exposure scores.

To alert you when the instance limit for the score calculation is exceeded, Security Command Center generates an `SCC error` finding and displays a message on the **Attack path simulation** settings tab in the Google Cloud console. Security Command Center doesn't generate an `SCC error` finding if the default high-value set exceeds the instance limit.

To avoid exceeding the limit, adjust your resource value configurations to refine the instances in your high-value resource set.

Some of the things you can do to refine your high-value resource set include the following options:

  * Use [tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview) or [labels](https://docs.cloud.google.com/resource-manager/docs/creating-managing-labels) to reduce the number matches for a given resource type or within a specified scope.
  * Create a resource value configuration that assigns a value of `NONE` to a subset of the resources that are specified in another configuration. Specifying a value of `NONE` overrides any other configurations and excludes the resource instances from your high-value resource set.
  * Reduce the scope specification in the resource value configuration.
  * Delete resource value configurations that assign a value of `LOW`.



## High-value resources

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

To populate your high-value resource set, you need to decide which resource instances in your environment are truly high value.

Generally, your true high-value resources are the resources that process and store your sensitive data. For example, on Google Cloud, these might be Compute Engine instances, a BigQuery dataset, or a Cloud Storage bucket.

You don't need to designate resources that are adjacent to your high-value resources, such as a jump server, as high value. The attack path simulations account for these adjacent resources already, and if you designate them as high value also, it can make your attack exposure scores less reliable.

## Attack paths

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

An _attack path_ is an interactive, visual depiction of one or more potential paths that a hypothetical attacker could take to get from the public internet to one of your high-value resource instances.

Attack path simulations identify potential attack paths by modeling what would happen if an attacker applied known attack methods to the vulnerabilities and misconfigurations that Security Command Center has detected in your environment to try to reach your high-value resources.

You can view attack paths by clicking on the attack exposure score on a finding or resource in the Google Cloud console.

On the Enterprise tier, when viewing a toxic combination case, you can view a simplified attack path for the toxic combination on the case **Overview** tab. The simplified attack path includes a link to the full attack path. For more information about attack paths for toxic combination findings, see [Toxic combination attack paths](https://docs.cloud.google.com/security-command-center/docs/toxic-combinations-overview#toxic-combination-attack-path).

When viewing larger attack paths, you can change your view of the attack path by dragging the red square area-of-focus selector around the miniature view of the attack path at the right side of the display.

In an attack path, resources on an attack path are represented as boxes or _nodes_. The lines represent potential accessibility between resources. Together, the nodes and lines represent the attack path.

### Attack path nodes

The nodes in an attack path represent the resources on an attack path.

#### Displaying node information

You can display more information about each node in an attack path by clicking it.

Clicking the resource name in a node displays more information about the resource, as well as any findings that affect the resource.

Clicking **Expand node** displays possible attack methods that could be used if an attacker gained access to the resource.

#### Types of nodes

There are three different types of nodes:

  * The starting point or _entry point_ of the simulated attack, which is the public internet. Clicking on an entry point node displays a description of the entry point along with attack methods an attacker could use to gain access to your environment.
  * The _affected resources_ that an attacker can use to move forward on a path.
  * The _exposed resource_ at the end of a path, which is one of the resources in your high-value resource set. Only a resource in a defined or default high-value resource set can be an exposed resource. You define a high-value resource set by creating [_resource value configurations_](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set).



#### Upstream and downstream nodes

In an attack path, a node can be _upstream_ or _downstream_ from the other nodes. An upstream node is closer to the entry point and the top of the attack path. A downstream node is closer to the exposed high-value resource at the bottom of the attack path.

#### Nodes representing multiple container resource instances

A node can represent multiple instances of certain container resource types if the instances share the same characteristics.

Multiple instances of the following container resource types can be represented by a single node:

  * ReplicaSet Controller
  * Deployment Controller
  * Job Controller
  * CronJob Controller
  * DaemonSet Controller



### Attack path lines

In an attack path, lines between the boxes represent potential accessibility between resources that an attacker could leverage to reach high-value resources.

The lines don't represent a relationship between resources that is defined in Google Cloud.

If there are multiple paths pointing to a downstream node from multiple upstream nodes, the upstream nodes can have either an `AND` relationship with each other or an `OR` relationship with each other.

An `AND` relationship means that an attacker needs access to both upstream nodes to access a downstream node on the path.

For example, a direct line from the public internet to a high-value resource at the end of an attack path has an `AND` relationship with at least one other line in the attack path. An attacker couldn't reach the high-value resource unless they gain access to both your Google Cloud environment and at least one other resource shown in the attack path.

An `OR` relationship means that an attacker needs access to only one of the upstream nodes to access the downstream node.

## Attack path simulations

Premium and Enterprise (Deprecated) [service tiers](https://docs.cloud.google.com/security-command-center/docs/service-tiers) (requires [organization-level activation](https://docs.cloud.google.com/security-command-center/docs/activate-scc-overview#overview_of_organization-level_activation))

To determine all possible attack paths and to calculate attack exposure scores, Security Command Center conducts advanced attack path simulations.

### Simulation schedule

Attack path simulations run on a schedule, and new results are available up to every 48 hours. Simulation runs aren't triggered by the creation, modification, or deletion of resources or resource value configurations.

### Attack path simulation steps

The simulation consists of the following steps:

  1. Model generation: A model of your Google Cloud environment is automatically generated based on the environment data. The model is a graph representation of your environment, tailored for attack path analyses.
  2. Attack path simulation: Attack path simulations are conducted on the graph model. The simulations have a virtual attacker try to reach and compromise the resources in your high-value resource set. The simulations leverage the insights on each specific resource and relations, including networking, IAM, configurations, misconfigurations, and vulnerabilities.
  3. Insight reporting: Based on the simulations, Security Command Center assigns attack exposure scores to your high-value resources and to the findings that expose them and visualizes the potential paths an attacker could take to those resources.



### Simulation execution characteristics

In addition to providing the attack exposure scores, attack path insights, and attack paths, attack path simulations have the following characteristics:

  * They don't touch your live environment: All simulations are conducted on a virtual model and use only read access for model creation.
  * They are dynamic: The model is created without agents through API read access only, which enables the simulations to dynamically follow changes to your environment over time.
  * They have a virtual attacker try as many methods and vulnerabilities as possible to reach and compromise your high-value resources. This includes not only "the knowns", such as the vulnerabilities, configurations, misconfigurations, and network relations, but also lower-probability "known unknowns"—risks we know exist, such as the possibility of phishing or leaked credentials.
  * They are automated: The attack logic is built into the tool. You don't need to build or maintain extensive sets of queries or large datasets.



### Attacker scenario and capabilities

In the simulations, Security Command Center has a logical representation of an attacker attempt to exploit your high-value resources by gaining access to your Google Cloud environment and following potential paths of access through your resources and detected vulnerabilities.

#### The virtual attacker

The virtual attacker that the simulations use has the following characteristics:

  * The attacker is external: The attacker is not a legitimate user of your Google Cloud environment. The simulations don't model or include attacks from malicious or negligent users who have legitimate access to your environment.
  * The attacker starts from the public internet. To start an attack, the attacker must first gain access to your environment from the public internet.
  * The attacker is persistent. The attacker won't be discouraged or lose interest due to the difficulty of a particular attack method.
  * The attacker is skilled and knowledgeable. The attacker tries known methods and techniques to access your high-value resources.



#### Initial access

Each simulation has a virtual attacker try the following methods to gain access from the public internet to the resources in your Google Cloud environment:

  * Discover and connect to services and resources that are accessible from the public internet. In a Google Cloud environment, this could include the following: 
    * Services on Compute Engine virtual machine (VM) instances and Google Kubernetes Engine nodes
    * Databases
    * Containers
    * Cloud Storage buckets
    * Cloud Run functions
  * Gain access to keys and credentials. In a Google Cloud environment, this could include the following: 
    * Service account keys
    * User-supplied encryption keys
    * VM instance SSH keys
    * Project-wide SSH keys
    * External key management systems
    * User accounts where multi-factor authentication (MFA) is not enforced
    * Intercepted virtual MFA tokens
  * Gaining access to publicly reachable cloud assets by use of stolen credentials or by exploiting vulnerabilities.



If the simulation finds a possible entry point into the environment, the simulation then has the virtual attacker try to reach and compromise your high-value resources from the entry point by consecutively exploring and exploiting security configurations and vulnerabilities within the environment.

#### Tactics and techniques

The simulation uses a wide variety of tactics and techniques, including leveraging legitimate access, lateral movement, privilege escalation, vulnerabilities, misconfigurations, and code execution.

### Incorporation of CVE data

When calculating attack exposure scores for vulnerability findings, the attack path simulations consider data from the vulnerability's [CVE record](https://www.cve.org/ResourcesSupport/Glossary), the [CVSS scores](https://www.first.org/cvss/), as well as assessments of the exploitability of the vulnerability that are provided by Mandiant.

The following CVE information is considered:

  * **Attack vector** : The attacker needs to have the level of access that is specified in the CVSS attack vector to use the CVE. For example, a CVE with a network attack vector that is found on an asset with a public IP address and open ports can be exploited by an attacker with network access. If an attacker has network access only and the CVE requires physical access, then the attacker cannot exploit the CVE.
  * **Attack complexity** : Generally, a vulnerability or misconfiguration finding with a low attack complexity is more likely to get a high attack exposure score than a finding with high attack complexity.
  * **Exploitation activity** : Generally, a vulnerability finding with wide exploitation activity, as determined by cyber threat intelligence analysts at Mandiant, is more likely to get a high attack exposure score than a finding with only anticipated exploitation activity. A vulnerability with no known exploitation activity is not considered in the attack path simulations.



## Multicloud risk assessments

Enterprise (Deprecated) [service tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers)

In addition to Google Cloud, Security Command Center can run attack path simulations to assess risk in your deployments on multiple cloud service provider platforms.

After you establish a connection to another platform, you can designate your high-value resources on the other cloud service provider by creating resource value configurations, as you would for resources on Google Cloud.

Security Command Center runs simulations for a cloud platform independently of simulations that are run for other cloud platforms.

Before you create the first resource value configuration for another cloud service provider, Security Command Center uses a default high-value resource set that is specific to each cloud service provider.

For more information, see the following:

### AWS

  * [Connect to AWS for configuration and resource data collection](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-aws)
  * [Risk Engine support for AWS resources](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features#aws-support)



### Microsoft Azure

  * [Connect to Azure for configuration and resource data collection](https://docs.cloud.google.com/security-command-center/docs/connect-scc-to-azure)
  * [Risk Engine support for Azure resources](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features#azure-support)



What's next

  * Learn more about [Risk Engine feature support](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-supported-features).

  * Learn how to [Define and manage your high-value resource set](https://docs.cloud.google.com/security-command-center/docs/attack-exposure-define-high-value-resource-set).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
