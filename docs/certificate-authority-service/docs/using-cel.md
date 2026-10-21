---
url: https://docs.cloud.google.com/certificate-authority-service/docs/using-cel/
title: Use Common Expression Language \u00a0|\u00a0 Certificate Authority Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:59:35.549758+00:00
---

# Use Common Expression Language  |  Certificate Authority Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/certificate-authority-service/docs/using-cel/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Certificate Authority Service ](https://docs.cloud.google.com/certificate-authority-service/docs)
  * [ Guides ](https://docs.cloud.google.com/certificate-authority-service/docs/ca-service-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Use Common Expression Language

This page describes how you can use Common Expression Language (CEL) with certificate issuance policies, certificate templates, and Identity and Access Management (IAM) conditions on your CA pool.

## Overview

[Common Expression Language (CEL)](https://opensource.google/projects/cel) is an open source non-Turing complete language that implements common semantics for expression evaluation. Certificate Authority Service supports CEL to enforce various policy controls for certificate issuance.

There are two CEL dialects that can be used with CA Service:

  * A flexible dialect that can be used in a CA pool's certificate issuance policies and certificate templates.
  * A more limited dialect that can be used in IAM conditions.



## CEL dialect for certificate issuance policies and certificate templates

When creating a CA pool or a certificate template, you can specify a CEL expression as part of the certificate identity constraints. The CEL expression lets you validate the Subject and Subject Alternative Name (SAN) fields.

For more information about issuance policies, see [Add certificate issuance policies](https://docs.cloud.google.com/certificate-authority-service/docs/use-issuance-policy).

For more information about certificate templates, see [Overview of policy controls](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls).

The CEL dialect for the identity constraints of CA pools and certificate templates exposes the following variables for accessing and validating the subject and SAN fields:

  * Subject: `subject`
  * SAN: `subject_alt_names`



#### Subject

You can validate all the fields in a certificate's subject domain name (including the common name), as specified in the certificate request using a variable of type `Subject` and name `subject`.

`Subject` is a structure that contains the following fields:

Type | Name  
---|---  
`String` | common_name  
`String` | country_code  
`String` | organization  
`String` | organizational_unit  
`String` | locality  
`String` | province  
`String` | street_address  
`String` | postal_code  
  
#### Subject Alternative Names (SANs)

You can validate all SANs as specified in the certificate request using the `subject_alt_names` variable. The `subject_alt_names` variable contains a list SAN structs, where each SAN is of type `SubjectAltName`.

`SubjectAltName` is a struct that contains the following fields:

Type | Name  
---|---  
`String` | value  
`[]Int32` | oid  
`Enum` | type  
  
You can use the following values for the `SubjectAltName` type:

  * `DNS`
  * `URI`
  * `EMAIL`
  * `IP_ADDRESS`
  * `CUSTOM`



The `subject_alt_names` variable contains a list with all the requested SANs.

You can use the following macros on SANs:

  * `subject_alt_names.all(san, predicate)`
  * `subject_alt_names.exists(san, predicate)`
  * `subject_alt_names.exists_one(san, predicate)`
  * `subject_alt_names.filter(san, predicate)`



For more information about macros, see [Language definition: Macros](https://github.com/google/cel-spec/blob/master/doc/langdef.md#macros).

**Note:** CA Service doesn't support CEL expressions with nested macros. We recommend that you use `and` and `or` operators to implement the same feature.

### Example expressions

**Ensuring a specific common name and a set of countries**
    
    
    subject.common_name == "google.com" && (subject.country_code == "US" || subject.country_code == "IR")
    

**Ensuring all DNS names end with a custom string**
    
    
    subject_alt_names.all(san, san.type == DNS && san.value.endsWith(".test.com"))
    

**Ensuring all SANs are of type DNS or EMAIL**
    
    
    subject_alt_names.all(san, san.type == DNS || san.type == EMAIL )
    

**Ensuring only one custom SAN with a specific OID**
    
    
    subject_alt_names.size() == 1 && subject_alt_names[0].oid == [1, 2, 3, 5, 17]
    

**Ensuring custom SANs are only a set of OIDs**
    
    
    subject_alt_names.all(san, san.oid == [1, 2, 4, 5, 55] || san.oid == [1, 2, 4, 5, 54])
    

## CEL dialect for IAM policies

Use IAM conditions to subject IAM role bindings to a conditional expression. If the condition evaluates to `true`, then the IAM role binding is effective, otherwise it is ignored. CA Service lets you add IAM conditional bindings to a CA pool.

The IAM condition is a CEL expression that references a set of contextual attributes about the request and evaluates to a boolean. Users set conditions on the role bindings in an IAM policy, which is stored by IAM and evaluated to see whether the operation that is about to be performed is permitted.

For more information about IAM conditions, see [Overview of IAM conditions](https://docs.cloud.google.com/iam/docs/conditions-overview).

The following attributes are exposed during CEL evaluation of IAM conditions:

  * **`privateca.googleapis.com/subject`**

The `privateca.googleapis.com/subject` is accessible as `api.getAttribute('privateca.googleapis.com/subject', {})`.


Type | Description  
---|---  
`map{string, string}` | This field contains the subject distinguished name (including the common name) as specified in the incoming certificate request.  
  
**Example**  
  
`{  
'common_name': 'Foobar',  
'organization': 'Example LLC'  
'country_code' :'US'  
'organizational_unit':'Foobar'  
'locality':'Mountain View'  
'Province':'California'  
'street_address':'Foobar 22'  
'postal_code':55555  
}`  
  
  * **`privateca.googleapis.com/subject_alt_names`**

The `privateca.googleapis.com/subject_alt_names` is accessible as `api.getAttribute('privateca.googleapis.com/subject_alt_names', [])`.


Type | Description  
---|---  
`list{string}` | This field contains all requested SANs as specified in the incoming certificate request. Each of the requested SANs is prefixed with its type. SANs with unknown types are prefixed with the type's serialized OID.  
  
**Example**  
  
`{  
'dns:foo.bar.com',  
'uri:spiffe://foo/ns/bar/sa/baz'  
'email:foo@bar.com'  
'ip:169.169.254.254'  
'custom:1.2.3.4.5.6.3:foobar'  
}`  
  
  * **`privateca.googleapis.com/template`**

The `privateca.googleapis.com/template` is accessible as `api.getAttribute('privateca.googleapis.com/template', '')`.


Type | Description  
---|---  
`String` | The certificate template that was used, if any. The format is `{project_id}/-/{template_id}`.  
  
**Example** : `my-project-pki/-/workload_tls`  
  
The template syntax uses `{project_id}/-/{template_id}` instead of the standard full resource name `projects/{project_id}/locations/{location}/certificateTemplates/{template_id}` because certificate templates must reside in the same location as the CA pool. In this format, the hyphen (`-`) acts as a location wildcard, which keeps CEL conditions concise, readable, and location-agnostic.

The template name provided in the IAM condition must match the template name in the certificate request. So, if you're providing a project ID in the `privateca.googleapis.com/template` attribute of the CEL expression, you must also provide a project ID when requesting the certificate. If you provide a project number in the CEL expression, you must provide a project number in the certificate request as well.

### Example expressions

**Ensuring that all subjects have organization set as 'Example' and country code set as`US` or `UK`**
    
    
    api.getAttribute('privateca.googleapis.com/subject', {})['organization'] == 'Example' &&
    api.getAttribute('privateca.googleapis.com/subject', {})['country_code'] in ['US', 'UK']
    

**Ensuring that the certificate request only includes the given DNS SANs**
    
    
    api.getAttribute('privateca.googleapis.com/subject_alt_names', [])
            .hasOnly(['dns:sample1.prod.example.com', 'dns:sample2.prod.example.com'])
    

**Ensuring that all certificates use a specific template**
    
    
    api.getAttribute('privateca.googleapis.com/template', '') == 'my-project-pki/-/leaf-server-tls'
    

## What's next

  * Read the [introduction to CEL](https://github.com/google/cel-spec/blob/master/doc/intro.md).
  * Learn more about [language definition for CEL](https://github.com/google/cel-spec/blob/master/doc/langdef.md).
  * Learn about [certificate templates and issuance policies](https://docs.cloud.google.com/certificate-authority-service/docs/policy-controls).
  * Read the [overview of IAM conditions](https://docs.cloud.google.com/iam/docs/conditions-overview).
  * Learn how to [add a certificate issuance policy to a CA pool](https://docs.cloud.google.com/certificate-authority-service/docs/use-issuance-policy).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
