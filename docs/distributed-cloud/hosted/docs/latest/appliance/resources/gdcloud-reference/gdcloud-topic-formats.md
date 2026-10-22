---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-topic-formats/
title: gdcloud topic formats \u00a0|\u00a0 Google Distributed Cloud Hosted Appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:22:37.070064+00:00
---

# gdcloud topic formats  |  Google Distributed Cloud Hosted Appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/resources/gdcloud-reference/gdcloud-topic-formats/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ Appliance ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ 1.0.7 ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance)
  * [ Reference ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/appliance/reference/reference-overview)



Send feedback 

#  gdcloud topic formats Stay organized with collections  Save and categorize content based on your preferences. 

## NAME

gdcloud topic formats - Supplementary help for resource formats.

## DESCRIPTION

Many `gdcloud` CLI commands return a list of resources on success. By default, they are pretty-printed in the standard output. The `--format=NAME[PROJECTIONS]` flag can be used to format and change the default output to a more meaningful result.

Use the `--format` flag to change the default output format of a command. Resource formats are described in detail later.

Use projections to list a subset of resource keys in a resource.

Note To refer to a list of fields, you can sort and format by each resource. You can run a `list` command with the format set to `yaml`, `json`, `csv`, `text`, or `table`. For example,
    
    
    gdcloud clusters list --format=yaml
    

## Formats

A format expression is used to change the default output format of a command. Many output formats are available; some for pretty-printing human-readable output and others for returning machine-readable output. A format expression has two parts 

_NAME_ _name_

_PROJECTIONS_ _[ resource-key [, …] ]_

_NAME_ is required and _PROJECTIONS_ can be applied to `csv`, `text`, and `table` formats. Unknown values are silently ignored. Each `gdcloud list` command has a default format expression. The `--format` flag can alter or replace the default. For example,

`--format="table(clusterref.name,controlPlane.name,controlPlane.image)"` lists control plane resources in table format.

`--format=json` lists the resource in JSON format.

The available formats are 

## csv 
    
    
    Comma Separated Values (<https //www.ietf.org/rfc/rfc4180.txt>) with no keys. Use this format with a projection to define values to print.
    

## json 
    
    
    JSON (<https //www.json.org>), JavaScript Object Notation.
    

## table 
    
    
    Aligned left-adjusted columns and column headings are the disambiguated right hand components of the column keys in uppercase. For example, the projection keys `(first.name, last.name)` produce the default column heading `('FIRST.NAME', 'LAST.NAME')`. If the screen reader option is `True`, you might observe flattened list output instead of a table with columns. To turn it off, run  `gdcloud config set accessibility/screen_reader false`.
    

## text 
    
    
    A flattened tree. Each output line contains one `key` `value` pair. Use this format with a projection to define values to print.
    

## yaml 
    
    
    YAML (<https //www.yaml.org>), YAML ain't markup language.
    

## EXAMPLES

List the status of all clusters information in JSON format 
    
    
    gdcloud clusters list --format=json
    

Print the cluster reference details of the user cluster 
    
    
    gdcloud clusters describe user-vm-1 --format="table(clusterref.name,clusterref.namespace)"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
