---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ArtifactsOrBuilder
title: Interface ArtifactsOrBuilder (3.101.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:44:06.973579+00:00
---

# Interface ArtifactsOrBuilder (3.101.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.ArtifactsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ArtifactsOrBuilder (3.101.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.101.0 (latest)  3.97.0  3.96.0  3.95.0  3.93.0  3.90.0  3.89.0  3.87.0  3.85.0  3.84.0  3.83.0  3.82.0  3.80.0  3.78.0  3.77.0  3.76.0  3.75.0  3.74.0  3.72.0  3.70.0  3.69.0  3.66.0  3.65.0  3.64.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.51.0  3.50.0  3.49.0  3.48.0  3.47.0  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.39.0  3.38.0  3.37.0  3.36.0  3.35.0  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.6  3.4.1  3.3.12 
    
    
    public interface ArtifactsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getGoModules(int index)
    
    
    public abstract Artifacts.GoModule getGoModules(int index)

Optional. A list of Go modules to be uploaded to Artifact Registry upon successful completion of all build steps.

If any objects fail to be pushed, the build is marked FAILURE.

` repeated .google.devtools.cloudbuild.v1.Artifacts.GoModule go_modules = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Artifacts.GoModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Artifacts.GoModule)` |   
  
### getGoModulesCount()
    
    
    public abstract int getGoModulesCount()

Optional. A list of Go modules to be uploaded to Artifact Registry upon successful completion of all build steps.

If any objects fail to be pushed, the build is marked FAILURE.

` repeated .google.devtools.cloudbuild.v1.Artifacts.GoModule go_modules = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getGoModulesList()
    
    
    public abstract List<Artifacts.GoModule> getGoModulesList()

Optional. A list of Go modules to be uploaded to Artifact Registry upon successful completion of all build steps.

If any objects fail to be pushed, the build is marked FAILURE.

` repeated .google.devtools.cloudbuild.v1.Artifacts.GoModule go_modules = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[GoModule](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Artifacts.GoModule)>` |   
  
### getGoModulesOrBuilder(int index)
    
    
    public abstract Artifacts.GoModuleOrBuilder getGoModulesOrBuilder(int index)

Optional. A list of Go modules to be uploaded to Artifact Registry upon successful completion of all build steps.

If any objects fail to be pushed, the build is marked FAILURE.

` repeated .google.devtools.cloudbuild.v1.Artifacts.GoModule go_modules = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Artifacts.GoModuleOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Artifacts.GoModuleOrBuilder)` |   
  
### getGoModulesOrBuilderList()
    
    
    public abstract List<? extends Artifacts.GoModuleOrBuilder> getGoModulesOrBuilderList()

Optional. A list of Go modules to be uploaded to Artifact Registry upon successful completion of all build steps.

If any objects fail to be pushed, the build is marked FAILURE.

` repeated .google.devtools.cloudbuild.v1.Artifacts.GoModule go_modules = 4 [(.google.api.field_behavior) = OPTIONAL]; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloudbuild.v1.Artifacts.GoModuleOrBuilder>` |   
  
### getImages(int index)
    
    
    public abstract String getImages(int index)

A list of images to be pushed upon the successful completion of all build steps.

The images will be pushed using the builder service account's credentials.

The digests of the pushed images will be stored in the Build resource's results field.

If any of the images fail to be pushed, the build is marked FAILURE.

`repeated string images = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The images at the given index.  
  
### getImagesBytes(int index)
    
    
    public abstract ByteString getImagesBytes(int index)

A list of images to be pushed upon the successful completion of all build steps.

The images will be pushed using the builder service account's credentials.

The digests of the pushed images will be stored in the Build resource's results field.

If any of the images fail to be pushed, the build is marked FAILURE.

`repeated string images = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the images at the given index.  
  
### getImagesCount()
    
    
    public abstract int getImagesCount()

A list of images to be pushed upon the successful completion of all build steps.

The images will be pushed using the builder service account's credentials.

The digests of the pushed images will be stored in the Build resource's results field.

If any of the images fail to be pushed, the build is marked FAILURE.

`repeated string images = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of images.  
  
### getImagesList()
    
    
    public abstract List<String> getImagesList()

A list of images to be pushed upon the successful completion of all build steps.

The images will be pushed using the builder service account's credentials.

The digests of the pushed images will be stored in the Build resource's results field.

If any of the images fail to be pushed, the build is marked FAILURE.

`repeated string images = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the images.  
  
### getMavenArtifacts(int index)
    
    
    public abstract Artifacts.MavenArtifact getMavenArtifacts(int index)

A list of Maven artifacts to be uploaded to Artifact Registry upon successful completion of all build steps.

Artifacts in the workspace matching specified paths globs will be uploaded to the specified Artifact Registry repository using the builder service account's credentials.

If any artifacts fail to be pushed, the build is marked FAILURE.

`repeated .google.devtools.cloudbuild.v1.Artifacts.MavenArtifact maven_artifacts = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Artifacts.MavenArtifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Artifacts.MavenArtifact)` |   
  
### getMavenArtifactsCount()
    
    
    public abstract int getMavenArtifactsCount()

A list of Maven artifacts to be uploaded to Artifact Registry upon successful completion of all build steps.

Artifacts in the workspace matching specified paths globs will be uploaded to the specified Artifact Registry repository using the builder service account's credentials.

If any artifacts fail to be pushed, the build is marked FAILURE.

`repeated .google.devtools.cloudbuild.v1.Artifacts.MavenArtifact maven_artifacts = 3; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getMavenArtifactsList()
    
    
    public abstract List<Artifacts.MavenArtifact> getMavenArtifactsList()

A list of Maven artifacts to be uploaded to Artifact Registry upon successful completion of all build steps.

Artifacts in the workspace matching specified paths globs will be uploaded to the specified Artifact Registry repository using the builder service account's credentials.

If any artifacts fail to be pushed, the build is marked FAILURE.

`repeated .google.devtools.cloudbuild.v1.Artifacts.MavenArtifact maven_artifacts = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[MavenArtifact](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Artifacts.MavenArtifact)>` |   
  
### getMavenArtifactsOrBuilder(int index)
    
    
    public abstract Artifacts.MavenArtifactOrBuilder getMavenArtifactsOrBuilder(int index)

A list of Maven artifacts to be uploaded to Artifact Registry upon successful completion of all build steps.

Artifacts in the workspace matching specified paths globs will be uploaded to the specified Artifact Registry repository using the builder service account's credentials.

If any artifacts fail to be pushed, the build is marked FAILURE.

`repeated .google.devtools.cloudbuild.v1.Artifacts.MavenArtifact maven_artifacts = 3; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Artifacts.MavenArtifactOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Artifacts.MavenArtifactOrBuilder)` |   
  
### getMavenArtifactsOrBuilderList()
    
    
    public abstract List<? extends Artifacts.MavenArtifactOrBuilder> getMavenArtifactsOrBuilderList()

A list of Maven artifacts to be uploaded to Artifact Registry upon successful completion of all build steps.

Artifacts in the workspace matching specified paths globs will be uploaded to the specified Artifact Registry repository using the builder service account's credentials.

If any artifacts fail to be pushed, the build is marked FAILURE.

`repeated .google.devtools.cloudbuild.v1.Artifacts.MavenArtifact maven_artifacts = 3; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloudbuild.v1.Artifacts.MavenArtifactOrBuilder>` |   
  
### getNpmPackages(int index)
    
    
    public abstract Artifacts.NpmPackage getNpmPackages(int index)

A list of npm packages to be uploaded to Artifact Registry upon successful completion of all build steps.

Npm packages in the specified paths will be uploaded to the specified Artifact Registry repository using the builder service account's credentials.

If any packages fail to be pushed, the build is marked FAILURE.

`repeated .google.devtools.cloudbuild.v1.Artifacts.NpmPackage npm_packages = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Artifacts.NpmPackage](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Artifacts.NpmPackage)` |   
  
### getNpmPackagesCount()
    
    
    public abstract int getNpmPackagesCount()

A list of npm packages to be uploaded to Artifact Registry upon successful completion of all build steps.

Npm packages in the specified paths will be uploaded to the specified Artifact Registry repository using the builder service account's credentials.

If any packages fail to be pushed, the build is marked FAILURE.

`repeated .google.devtools.cloudbuild.v1.Artifacts.NpmPackage npm_packages = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getNpmPackagesList()
    
    
    public abstract List<Artifacts.NpmPackage> getNpmPackagesList()

A list of npm packages to be uploaded to Artifact Registry upon successful completion of all build steps.

Npm packages in the specified paths will be uploaded to the specified Artifact Registry repository using the builder service account's credentials.

If any packages fail to be pushed, the build is marked FAILURE.

`repeated .google.devtools.cloudbuild.v1.Artifacts.NpmPackage npm_packages = 6;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[NpmPackage](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Artifacts.NpmPackage)>` |   
  
### getNpmPackagesOrBuilder(int index)
    
    
    public abstract Artifacts.NpmPackageOrBuilder getNpmPackagesOrBuilder(int index)

A list of npm packages to be uploaded to Artifact Registry upon successful completion of all build steps.

Npm packages in the specified paths will be uploaded to the specified Artifact Registry repository using the builder service account's credentials.

If any packages fail to be pushed, the build is marked FAILURE.

`repeated .google.devtools.cloudbuild.v1.Artifacts.NpmPackage npm_packages = 6;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Artifacts.NpmPackageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Artifacts.NpmPackageOrBuilder)` |   
  
### getNpmPackagesOrBuilderList()
    
    
    public abstract List<? extends Artifacts.NpmPackageOrBuilder> getNpmPackagesOrBuilderList()

A list of npm packages to be uploaded to Artifact Registry upon successful completion of all build steps.

Npm packages in the specified paths will be uploaded to the specified Artifact Registry repository using the builder service account's credentials.

If any packages fail to be pushed, the build is marked FAILURE.

`repeated .google.devtools.cloudbuild.v1.Artifacts.NpmPackage npm_packages = 6;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloudbuild.v1.Artifacts.NpmPackageOrBuilder>` |   
  
### getObjects()
    
    
    public abstract Artifacts.ArtifactObjects getObjects()

A list of objects to be uploaded to Cloud Storage upon successful completion of all build steps.

Files in the workspace matching specified paths globs will be uploaded to the specified Cloud Storage location using the builder service account's credentials.

The location and generation of the uploaded objects will be stored in the Build resource's results field.

If any objects fail to be pushed, the build is marked FAILURE.

`.google.devtools.cloudbuild.v1.Artifacts.ArtifactObjects objects = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Artifacts.ArtifactObjects](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Artifacts.ArtifactObjects)` | The objects.  
  
### getObjectsOrBuilder()
    
    
    public abstract Artifacts.ArtifactObjectsOrBuilder getObjectsOrBuilder()

A list of objects to be uploaded to Cloud Storage upon successful completion of all build steps.

Files in the workspace matching specified paths globs will be uploaded to the specified Cloud Storage location using the builder service account's credentials.

The location and generation of the uploaded objects will be stored in the Build resource's results field.

If any objects fail to be pushed, the build is marked FAILURE.

`.google.devtools.cloudbuild.v1.Artifacts.ArtifactObjects objects = 2;`

**Returns**  
---  
**Type** | **Description**  
`[Artifacts.ArtifactObjectsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Artifacts.ArtifactObjectsOrBuilder)` |   
  
### getPythonPackages(int index)
    
    
    public abstract Artifacts.PythonPackage getPythonPackages(int index)

A list of Python packages to be uploaded to Artifact Registry upon successful completion of all build steps.

The build service account credentials will be used to perform the upload.

If any objects fail to be pushed, the build is marked FAILURE.

`repeated .google.devtools.cloudbuild.v1.Artifacts.PythonPackage python_packages = 5; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Artifacts.PythonPackage](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Artifacts.PythonPackage)` |   
  
### getPythonPackagesCount()
    
    
    public abstract int getPythonPackagesCount()

A list of Python packages to be uploaded to Artifact Registry upon successful completion of all build steps.

The build service account credentials will be used to perform the upload.

If any objects fail to be pushed, the build is marked FAILURE.

`repeated .google.devtools.cloudbuild.v1.Artifacts.PythonPackage python_packages = 5; `

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getPythonPackagesList()
    
    
    public abstract List<Artifacts.PythonPackage> getPythonPackagesList()

A list of Python packages to be uploaded to Artifact Registry upon successful completion of all build steps.

The build service account credentials will be used to perform the upload.

If any objects fail to be pushed, the build is marked FAILURE.

`repeated .google.devtools.cloudbuild.v1.Artifacts.PythonPackage python_packages = 5; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[PythonPackage](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Artifacts.PythonPackage)>` |   
  
### getPythonPackagesOrBuilder(int index)
    
    
    public abstract Artifacts.PythonPackageOrBuilder getPythonPackagesOrBuilder(int index)

A list of Python packages to be uploaded to Artifact Registry upon successful completion of all build steps.

The build service account credentials will be used to perform the upload.

If any objects fail to be pushed, the build is marked FAILURE.

`repeated .google.devtools.cloudbuild.v1.Artifacts.PythonPackage python_packages = 5; `

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Artifacts.PythonPackageOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-build/latest/com.google.cloudbuild.v1.Artifacts.PythonPackageOrBuilder)` |   
  
### getPythonPackagesOrBuilderList()
    
    
    public abstract List<? extends Artifacts.PythonPackageOrBuilder> getPythonPackagesOrBuilderList()

A list of Python packages to be uploaded to Artifact Registry upon successful completion of all build steps.

The build service account credentials will be used to perform the upload.

If any objects fail to be pushed, the build is marked FAILURE.

`repeated .google.devtools.cloudbuild.v1.Artifacts.PythonPackage python_packages = 5; `

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloudbuild.v1.Artifacts.PythonPackageOrBuilder>` |   
  
### hasObjects()
    
    
    public abstract boolean hasObjects()

A list of objects to be uploaded to Cloud Storage upon successful completion of all build steps.

Files in the workspace matching specified paths globs will be uploaded to the specified Cloud Storage location using the builder service account's credentials.

The location and generation of the uploaded objects will be stored in the Build resource's results field.

If any objects fail to be pushed, the build is marked FAILURE.

`.google.devtools.cloudbuild.v1.Artifacts.ArtifactObjects objects = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the objects field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-05 UTC."],[],[]] 
