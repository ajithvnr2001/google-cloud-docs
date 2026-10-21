---
url: https://docs.cloud.google.com/data-studio/use-functions-in-calculated-fields/
title: Use functions in calculated fields \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:29.087631+00:00
---

# Use functions in calculated fields  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/use-functions-in-calculated-fields/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Use functions in calculated fields Stay organized with collections  Save and categorize content based on your preferences. 

Functions let you manipulate your data in ways beyond doing simple arithmetic. Data Studio provides over 50 functions, grouped into the following types:

  * **Aggregation** functions perform calculations over multiple rows of your data. Examples include SUM, AVG, MIN, MAX.
  * **Arithmetic** functions apply mathematical calculations to your data. Examples include LOG, POWER, ROUND.
  * **Date** functions let you manipulate and transform time data. Examples include DATE, DATETIME_DIFF, YEAR.
  * **Geo** functions let you transform geographic location data. Examples include TOCITY, TOCOUNTRY, TOREGION.
  * **Text** functions let you manipulate string data. Examples include CONCAT, REGEXP_MATCH, SUBSTR.



[See the complete list of available functions](https://docs.cloud.google.com/data-studio/function-list).

## Function arguments

All functions expect input, called _arguments,_ that tell the function what data to act upon. Arguments can be field names or _expressions_. An expression can be a number, literal text, or a statement that evaluates to a field name in your data source. Arguments can also provide additional instructions or formatting information.

### More about function arguments

  * When providing function arguments, be sure to enclose literal text in single or double quotes.
  * When using regular expressions, use double backslash to escape special characters. For example: `REGEXP_MATCH(GotStars, "\\*")` Matches the literal * character.
  * Geo functions require a supported geo code as input.



## Geo input codes

  * '  CITY_ID  '
  * '  CONTINENT_CODE  '
  * '  COUNTRY_ISO_CODE  '
  * '  REGION_ISO_CODE  '
  * '  SUB_CONTINENT_CODE  '



The valid geo codes are defined here:

  * [Country/Region codes](https://en.wikipedia.org/wiki/ISO-3166-2)
  * [City ID](https://developers.google.com/adwords/api/docs/appendix/geotargeting)
  * [Continent and Subcontinent codes](https://en.wikipedia.org/wiki/UN_M49)



> The input code is optional if the field expression is a derived column already containing semantic geo information; otherwise it is required.

## Function examples

Here are some simple examples of using the most popular functions. Additional complex examples are available in the individual [function references](https://docs.cloud.google.com/data-studio/function-list).

### Example 1: Organize and simplify your Analytics campaigns.

Suppose you run multiple ad campaigns, and use a coding system to identify them by category. Assuming the codes share a regular format, you could use the CASE expression and REGEXP_MATCH function to group related campaigns.

For example, say you've got campaign codes like C1, C2, and C3 for consumer goods, E1, E2, and E3 for electronics, S1, S2, and S3 for social ads. You could group these campaign codes into their respective category, and optionally, lump other campaigns into a miscellaneous category:

```CASE`  
`WHEN REGEXP_MATCH``(CAMPAIGN, "C.*")``THEN``"Consumer"`  
`WHEN REGEXP_MATCH``(CAMPAIGN, "E.*")``THEN``"Electronics"`  
`WHEN REGEXP_MATCH``(CAMPAIGN, "S.*")``THEN``"Social"`  
`ELSE``"Misc"`  
`END```

You can now use this calculated field to see how your campaigns are performing per group, or use it in a [filter control](https://docs.cloud.google.com/data-studio/about-controls) to refine the view of your data.

[Learn more about CASE](https://docs.cloud.google.com/data-studio/case-searched).

### Example 2: Combine values from multiple fields.

You can aggregate and display your data in new ways by combining multiple fields via the CONCAT function. This creates a new field with the concatenated values. For example:

```CONCAT``('Browser: ', BROWSER, ' Version: ', BROWSER VERSION)`

The new field will show the literal strings and dimension values as a single entry. The data values might look like the following examples:

  * Browser: Chrome Version: 68.0.3440.106
  * Browser: Safari Version: 11.0 
  * Browser: Firefox Version: 61.0 



### Example 3. Create hyperlinks from your data

If your data contains URLs, you can create clickable links that appear in tables by using the HYPERLINK function.

For example, suppose you've got a custom SKU dimension associated with the URL to the relevant product description in the PAGE dimension. The following formula creates a clickable link for each record in your data:

```HYPERLINK``(URL, SKU )`

If your data doesn't contain the complete URL, or you need to combine multiple fields to create the URL, use  CONCAT  to construct the link:

```HYPERLINK(CONCAT``("HTTPS://mydomain.com/", PARTIAL-URL, "?some-parameter"), SKU )`

You can also use the  HYPERLINK  function to create clickable images in your tables.

[Learn more about  HYPERLINK ](https://docs.cloud.google.com/data-studio/hyperlink).

## Limits of calculated fields

Formulas in calculated fields can't mix unaggregated data (dimensions) and aggregated data (metrics).

For example, the following is **not** allowed:
    
    
    CASE WHEN Country = "England" AND Conversions > 100 THEN... // invalid formula
    

In this example, Conversions is an aggregated metric. 

## Related resources

  * [Data Studio function list](https://docs.cloud.google.com/data-studio/function-list)
  * [Dimensions and metrics](https://docs.cloud.google.com/data-studio/model-your-data)
  * [Create a data source](https://docs.cloud.google.com/data-studio/add-data-to-a-report)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
