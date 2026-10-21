---
url: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/xmltojson-deployment-errors/
title: XML to JSON policy deployment error troubleshooting \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T02:38:52.701059+00:00
---

# XML to JSON policy deployment error troubleshooting  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/xmltojson-deployment-errors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Support ](https://docs.cloud.google.com/apigee/docs/support/getting-started-with-support)



Send feedback 

#  XML to JSON policy deployment error troubleshooting Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/troubleshoot/policies/deployment/xmltojson-deployment-errors) documentation._

Was this troubleshooting playbook helpful? Please let us know by clicking [ Send Feedback ](https://docs.cloud.google.com/apigee/docs/api-platform/troubleshoot/policies/deployment/xmltojson-deployment-errors/).

## EitherOptionOrFormat

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision [revision_number]
    XMLToJSON[{0}]: Either Options or Format must be specified.

### Example error
    
    
    Error Saving Revision 1
    XMLToJSON[{0}]: Either Options or Format must be specified.
    

### Example screenshot

![Either options or format must be specified error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/json2xml-error-1.png)

### Cause

If one of the elements `<Options>` or `<Format>` is not declared in the XML to JSON Policy, then the deployment of the API proxy fails.

`<Options>` is required if `<Format>` isn't used.

Use either the `<Format>` element or `<Options>` element group. You cannot use both `<Format>` and `<Options>`. Predefined formats include: `xml.com`, `yahoo`, `google`, and `badgerFish`.

### Diagnosis

  1. Examine all the XML to JSON policies in the specific API proxy where the failure has occurred. If there is any XML to JSON policy in which either of the elements `<Options>` or `<Format>` is not declared, then that's the cause of the error.

For example, the following policy does not have either of the elements declared:
         
         <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
         <XMLToJSON async="false" continueOnError="false" enabled="true" name="XMLToJSON">
             <DisplayName>XMLToJSON</DisplayName>
             <Properties/>
             <OutputVariable>response</OutputVariable>
             <Source>response</Source>
         </XMLToJSON>
         




### Resolution

Ensure that the XML of the XML to JSON policy has one of the elements `<Options>` or `<Format>` declared in the policy.

Example 1:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <XMLToJSON async="false" continueOnError="false" enabled="true" name="XMLToJSON">
        <DisplayName>XMLToJSON</DisplayName>
        <Properties/>
        <Format>google</Format>
        <OutputVariable>response</OutputVariable>
        <Source>response</Source>
    </XMLToJSON>
    

Example 2:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <XMLToJSON async="false" continueOnError="false" enabled="true" name="XMLToJSON">
        <DisplayName>XMLToJSON</DisplayName>
        <Properties/>
        <Options>
            <RecognizeNumber>true</RecognizeNumber>
            <RecognizeBoolean>true</RecognizeBoolean>
            <RecognizeNull>true</RecognizeNull>
        </Options>
        <OutputVariable>response</OutputVariable>
        <Source>response</Source>
    </XMLToJSON>
    

## UnknownFormat

### Error message

Deployment of the API proxy through either the Apigee UI or API fails with this error message:
    
    
    Error Saving Revision [revision_number]
    XMLToJSON[policy_name]: Unknown Format [unknown_format].

### Example error
    
    
    Error Saving Revision 1
    XMLToJSON[WithFormat]: Unknown Format google.com.
    

### Example screenshot

![Unknown format error message.](https://docs.cloud.google.com/static/apigee/docs/api-platform/images/json2xml-error-2.png)

### Cause

If the `<Format>` element within the XML to JSON policy has an unknown format defined, then the deployment of the API proxy fails.

Predefined formats include: `xml.com`, `yahoo`, `google`, and `badgerFish`.

### Diagnosis

  1. Identify the XML to JSON policy where the error occurred and the unknown format. You can find this information from the error message. For example, in the following error, the policy name is `WithFormat` and the unknown format is `google.com`:
         
         Error Saving Revision 1
         XMLToJSON[WithFormat]: Unknown Format google.com.
         

  2. Verify that the unknown format specified in the failed XML to JSON policy matches with the value identified in the error message (step #1 above). For example, the following policy specifies the format as `google.com`, which matches what's in the error message:
         
         <XMLToJSON async="false" continueOnError="false" enabled="true" name="WithFormat">
           <DisplayName>WithFormat</DisplayName>
           <Properties/>
           <Format>google.com</Format>
           <OutputVariable>response</OutputVariable>
           <Source>response</Source>
         </XMLToJSON>
         

  3. If the Format specified is not one among the predefined formats `xml.com`, `yahoo`, `google`, or `badgerFish`, then that's the cause of the error.

In the example XML to JSON Policy shown above, the format is `google.com` which is invalid. Therefore, the deployment of the API Proxy fails with the error:
         
         XMLToJSON[WithFormat]: Unknown Format google.com.
         




### Resolution

Ensure that the format specified in the `<Format>` element of the XML to JSON policy is valid. For example:
    
    
    <?xml version="1.0" encoding="UTF-8" standalone="yes"?>
    <XMLToJSON async="false" continueOnError="false" enabled="true" name="WithFormat">
      <DisplayName>WithFormat</DisplayName>
      <Properties/>
      <Format>google</Format>
      <OutputVariable>response</OutputVariable>
      <Source>response</Source>
    </XMLToJSON>
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
