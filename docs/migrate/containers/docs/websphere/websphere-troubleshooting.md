---
url: https://docs.cloud.google.com/migrate/containers/docs/websphere/websphere-troubleshooting/
title: MQ configurations are not extracted for Open Liberty targets \u00a0|\u00a0 Migrate to Containers \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:37:11.871205+00:00
---

# MQ configurations are not extracted for Open Liberty targets  |  Migrate to Containers  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/containers/docs/websphere/websphere-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Containers ](https://docs.cloud.google.com/migrate/containers/docs)
  * [ Guides ](https://docs.cloud.google.com/migrate/containers/docs/getting-started)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# MQ configurations are not extracted for Open Liberty targets

If MQ configurations are not extracted for Open Liberty targets, use the following workaround:

  1. Extract the `wmq.jmsra.rar` file from the source VM by adding it to the migration plan.
         
         applications:
         - appName: brownear-ear
           httpEndpoints:
           - httpPort: 9080
             httpsPort: 9443
             id: defaulthttpendpoint
           image:
             name: brownear-ear
         includeFiles:
         - /opt/IBM/WebSphere/AppServer/installedConnectors/wmq.jmsra.rar
         

  2. Edit the server XML file to ensure following features are included in the feature manager:
         
         <featureManager>
             <feature>ejb-3.2</feature>
             <feature>jms-2.0</feature>
             <feature>mdb-3.2</feature>
             <feature>localConnector-1.0</feature>
             <feature>jaxrs-2.1</feature>
             <feature>cdi-2.0</feature>
           </featureManager>
         

  3. In the same file, ensure that the username and password are set for `jmsActivationSpec`:
         
         <jmsActivationSpec …>
             <properties.mqJmsRa … userName="USER_NAME" password="PASSWORD"/>
           </jmsActivationSpec>
         

**Note:** You need to set `includeSensitiveData` to `true`.**Note:** these username and password also can be found in the `wsadmin.py` artifact.
  4. In addition, it's possible a JNDI issue may occur, which you'll need to resolve according to the error message.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
