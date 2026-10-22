---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/shared-flow-bundle-configuration-reference/
title: Shared flow bundle configuration reference \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:20.231133+00:00
---

# Shared flow bundle configuration reference  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/shared-flow-bundle-configuration-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  Shared flow bundle configuration reference Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

A shared flow is reusable functionality similar to an API proxy. For more information, see [Creating reusable shared flows](https://docs.cloud.google.com/apigee/docs/api-platform/fundamentals/shared-flows).

## Shared flow bundle directory structure

The shared flow bundle directory structure, shown below, is similar to the [API proxy configuration directory structure](https://docs.cloud.google.com/apigee/docs/api-platform/reference/api-proxy-configuration-reference#apiproxystructure).

![Shared flow bundle directory structure](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/sharedflowbundlehierarchy.png)

A shared flow bundle configuration consists of the following contents:

Base configuration | Primary configuration settings.  
---|---  
Policies | XML-formatted configuration files that conform to the Apigee policy schemas.   
Resources | Scripts, JAR files, and XSLT files referenced by policies to execute custom logic.  
Shared flows | Shared flows included in this bundle.  
  
## Base configuration

The base configuration file is located at the bundle's root directory. Its name is the name of the bundle.
    
    
    /sharedflowbundle/traffic-management-shared.xml

The base configuration defines the contents of the shared flow bundle, along with information for tracking the bundle's revision history.
    
    
    <SharedFlowBundle revision="2" name="traffic-management-shared">
        <ConfigurationVersion majorVersion="4" minorVersion="0"/>
        <CreatedAt>1478637529218</CreatedAt>
        <CreatedBy>gladys@example.com</CreatedBy>
        <Description>Shared flow to moderate API traffic</Description>
        <DisplayName>traffic-management-shared</DisplayName>
        <LastModifiedAt>1481573374023</LastModifiedAt>
        <LastModifiedBy>gladys@example.com</LastModifiedBy>
        <Policies>
            <Policy>Auth-Flow-Callout</Policy>
            <Policy>Extract-Token</Policy>
            <Policy>Spike-Arrest</Policy>
        </Policies>
        <Resources>
            <Resource>jsc://extract-token.js</Resource>
        </Resources>
        <SharedFlows>
            <SharedFlow>default</SharedFlow>
        </SharedFlows>
    </SharedFlowBundle>

### Base configuration attributes

Name | Description | Default | Required?  
---|---|---|---  
**`SharedFlowBundle`** |   
`name` | Name of the shared flow bundle, which must be unique within an organization. Valid characters include: `A-Za-z0-9_-` | N/A | Yes  
`revision` | Revision number of the shared flow bundle configuration. You do not need to explicitly set the revision number since Apigee automatically tracks the current revision of the shared flow. | N/A | No  
  
### Base configuration elements

Name | Description | Default | Required?  
---|---|---|---  
**`SharedFlowBundle`** |   
`ConfigurationVersion` | Version of the shared flow bundle configuration schema to which this shared flow conforms. The only supported value currently is `majorVersion 4` and `minorVersion 0`. This setting may be used in the future to enable evolution of the shared flow bundle format. | 4.0 | No  
`CreatedAt` and `CreatedBy` | Date/time (in epoch time) that the shared flow bundle was created, and the email of the user who created it. |  |   
`Description` | Textual description of the shared flow. If provided, the description will display in the Apigee UI. | N/A | No  
`DisplayName` | User-friendly name that may be different from the `name` attribute of the shared flow configuration. | N/A | No  
`LastModifiedAt` and `LastModifiedBy` | Date/time (in epoch time) that the shared flow bundle was last modified, along with the email of the user who modified it. |  |   
`Policies` | List of policies in the `/policies` directory of this shared flow. You will normally only see this element when the shared flow was created using the Edge management UI. This is simply a 'manifest' setting, designed to provide visibility into the contents of the shared flow. | N/A | No  
`Resources` | List of resources (JavaScript, Python, Java, XSLT) in the `/resources` directory of this shared flow. You will normally only see this element when the shared flow was created using the Apigee UI. This is simply a manifest setting, designed to provide visibility into the contents of the shared flow. | N/A | No  
`SharedFlows` |  Shared flow that this bundle contains. **Note:** Currently, this element supports only one child `<SharedFlow>`. In other words, only one shared flow may be added to a shared flow bundle. | N/A | Yes  
  
## Policies
    
    
    /sharedflowbundle/policies

As in an API proxy, in a shared flow bundle the `/policies` directory contains configuration XML for all policies available to be attached to the shared flow in the bundle. Policies share a subset of elements, though this subset is augmented with elements that are specific to the policy. For more about how to configure a policy, [Policy reference overview](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy).

## Resources
    
    
    /sharedflowbundle/resources

Resources are scripts, code, and XSL transformations that can be attached to shared flows using policies. These appear in the Scripts section of the shared flow editor in the management UI.

See [Managing resources](https://docs.cloud.google.com/apigee/docs/api-platform/develop/resource-files) for the supported resource types.

## Shared flows
    
    
    /sharedflowbundle/sharedflows/default.xml

The SharedFlow configuration defines the sequence in which flow elements should be executed. The `<SharedFlow>` element's `<Step>` child elements each specify a part of the sequence, such as a call to a policy.

The following SharedFlow configuration specifies three policies to be executed in a top-to-bottom sequence (left to right in the management console), with the [SpikeArrest policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/spike-arrest-policy) first and a [FlowCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/flow-callout-policy) last.
    
    
    <SharedFlow name="default">
        <Step>
            <Name>Spike-Arrest</Name>
        </Step>
        <Step>
            <Name>Extract-Token</Name>
        </Step>
        <Step>
            <Name>Auth-Flow-Callout</Name>
        </Step>
    </SharedFlow>

### Shared flow configuration attributes

Name | Description | Default | Required?  
---|---|---|---  
**`SharedFlow`** |   
`name` | The name of the shared flow, which must be unique within an organization. Valid characters include: `A-Za-z0-9_-` | N/A | Yes  
`revision` | Revision number of the shared flow configuration. You do not need to explicitly set the revision number since Apigee automatically tracks the current revision of the shared flow. | N/A | No  
  
### Shared flow configuration elements

Name | Description | Default | Required?  
---|---|---|---  
**`SharedFlow`** | Sequence of policies in the shared flow. | N/A | Yes  
**`Step`** | Stage in the flow's sequence. | N/A | Yes  
**`Name`** | Name of the item referenced by the step. This element's value should be the same as the item's unique identifier, such as a policy's name attribute value. | N/A | Yes  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
