---
url: https://docs.cloud.google.com/apigee/docs/api-platform/develop/adding-custom-java-callout-security-policy/
title: Adding a custom JavaCallout security policy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:46.414476+00:00
---

# Adding a custom JavaCallout security policy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/develop/adding-custom-java-callout-security-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Adding a custom JavaCallout security policy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## What is a custom JavaCallout security policy?

The [JavaCallout policy](https://docs.cloud.google.com/apigee/docs/api-platform/develop/how-create-java-callout) enables you to customize your API's behavior using Java code. When you implement JavaCallout, Apigee sets default permissions for the API using [Java permission policies](https://docs.cloud.google.com/apigee/docs/api-platform/reference/java-permission-reference). In Apigee hybrid, you can change the default permissions by creating a custom JavaCallout security policy.

**Note:** Custom JavaCallout security policies are only available in Apigee hybrid. The security policy is scoped to the environment, and there can only be one security policy in an environment.

You can create a custom JavaCallout security policy using a [resource](https://cloud.google.com/apis/design/resource_names), which is defined in a resource file of type `securityPolicy`. The resource is configured at the environment level. The resource file can have any name, but you must add the suffix `.policy` to the custom java policy file name. For example: `strict-security.policy`. 

The following command adds a resource file named `strict-security.policy`. 
    
    
    curl -X POST "https://apigee.googleapis.com/v1/organizations/my-organization/environments/test/resourcefiles?name=CustomJavaSecurityPolicy&type=securityPolicy"
    -H "Authorization: Bearer $TOKEN" \
    -H "Content-type: multipart/form-data" \
    -F file=@/Users/home/strict-security.policy

Security policy files support the same syntax as standard Java security policy; see [ Default Policy Implementation and Policy File Syntax](https://docs.oracle.com/javase/7/docs/technotes/guides/security/PolicyFiles.html). 

Once you have created a security policy file defining a custom JavaCallout policy, Apigee runtime can detect the policy and use the custom permissions the policy defines. If no custom JavaCallout policy is present, Apigee uses the default security policy for custom Java or Python code.

## Security policy file

The following examples show sample content of a security policy file.

The lines below specify the location of the code for a custom JavaCallout policy and grant all permissions to the directory.
    
    
    Relaxed security policy file for testing
    // javacallout code has just read permission in the installed dir and everything below it
      grant codeBase "file:${javacallout.dir}/-"  {
        permission java.security.AllPermission;
    }

These lines specify the location of the code for a custom Jython/Python Callout and grant read permissions to the directory.
    
    
    // Jython/Python secure
    grant codeBase "file:${jython-secure-jar}" {
        // No logging permissions for secure jar. Hence value of the AllExcept target parameter set to 0
        permission com.apigee.securitypolicy.AllExcept "0", "java.io.FilePermission";
        permission java.io.FilePermission "{T}conf_security-policy_install.dir{/T}/lib/-" , "read";
        // Add JRE read permissions to jython. Existing permissions have two formats to java home. Keep the same.
        permission java.io.FilePermission "${java.home}/-", "read,readLink";
        permission java.io.FilePermission "${JAVA_HOME}/-", "read,readLink";
    }

## Examples

The following examples show how to perform specific tasks related to custom JavaCallout security policies.

### Create a custom JavaCallout security policy

The following command creates a custom JavaCallout security policy, defined in the resource file named `strict-security.policy`.
    
    
    curl -X POST "https://apigee.googleapis.com/v1/organizations/my-organization/environments/test/resourcefiles?name=CustomJavaSecurityPolicy&type=securityPolicy"
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: multipart/form-data" \
      -F file=@/Users/home/strict-security.policy

### View all security policies

The following command lets you view all existing custom JavaCallout security policies in your API.
    
    
    curl -X GET "https://apigee.googleapis.com/v1/organizations/my-organization/environments/test/resourcefiles/securityPolicy" \
      -H "Authorization: Bearer $TOKEN"

### View the contents of a security policy file

The following command gets the contents of an individual security policy file so you can view it.
    
    
    curl -X GET "https://apigee.googleapis.com/v1/organizations/my-organization/environments/test/resourcefiles/securityPolicy/CustomJavaSecurityPolicy" \
      -H "Authorization: Bearer $TOKEN"

### Update a policy scoped to an environment

The following command updates a security policy scoped to an environment.
    
    
    curl -X PUT "https://apigee.googleapis.com/v1/organizations/my-organization/environments/test/resourcefiles/securityPolicy/CustomJavaSecurityPolicy"
      -H "Authorization: Bearer $TOKEN" \
      -H "Content-type: multipart/form-data" \
      -F file=@/Users/home/strict-security-revised.policy

### Delete security policy scoped to an environment

The following command deletes a security policy scoped to an environment.
    
    
    curl -X DELETE https://apigee.googleapis.com/v1/organizations/my-organization/environments/test/resourcefiles/securityPolicy/CustomJavaSecurityPolicy \
      -H "Authorization: Bearer $TOKEN"

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
