---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/
title: Attaching and configuring policies in XML files \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:53.326713+00:00
---

# Attaching and configuring policies in XML files  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/attaching-and-configuring-policies-xml-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Attaching and configuring policies in XML files Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

You can create and edit policies locally, using your favorite text or XML-aware editor or IDE. This topic uses the Quota policy type as an example of how to create, configure, attach, deploy, and test policies.

Most API proxies enforce a quota. Quotas provide control over how often a client app is permitted to invoke an API over a given time interval. In the example below, a Quota policy is configured to limit apps to 1 request per minute. (While this may not be realistic, it does provide a simple way to see the effects of a policy.)

In an API proxy configuration, Policy files are stored as XML files under `/apiproxy/policies` directory.

For example, a policy of type Quota called Quota Policy could be created as a file called `QuotaPolicy.xml` with the following content:
    
    
    <Quota enabled="true" continueOnError="false" name="QuotaPolicy">
        <Allow count="1"/>
        <Interval>1</Interval>
        <TimeUnit>minute</TimeUnit>
    </Quota>

You can create a text file by hand, or you can generate the policy from an XML schema. All policies have some settings that are specific to the policy type, and some settings that are generic across all policies. 

When you attach policies in the management UI, the API proxy builder generates the policy instance from the XML schema for the policy type you selected. Therefore, you may see elements in the policy configuration that, for clarity, are not always included in documentation. 

All policies define the following attributes:

  * `enabled`: Indicates whether the policy is turned _on_ or _off_. Policies can be enabled/disabled at runtime by changing this setting. A policy that has `enabled` set to `false` is not enforced.
  * `continueOnError`: Defines whether the pipeline should continue processing the message if the policy fails. When enforcing quota policies, errors likely indicate that the quota has been exceeded, and, therefore, this attribute should be set to false.
  * `name`: The name that you give to this policy. This name is unique to this policy instance, and it is used to attach the policy to the flow as a processing step.

**Note:** Except for `name`, you rarely need to modify the default settings for these policy attributes. For this reason, and for clarity, they are often excluded from the policy samples in the documentation.

In the example above, the elements `Allow`, `Interval`, and `TimeUnit` are specific to the Quota policy. These elements provide settings that API Services enforces on behalf of an API. Other policy types define their own settings, which you can learn about in the [Policy Reference](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
