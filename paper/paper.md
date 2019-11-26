# Paper outline - 3Dphenotyping [Paper Title]

## Abstract
Currently, it is possible to use softwares/tools to produce 3D point cloud and related output to be used for extracting phenotypic data from a set of images. However, this process is time-consuming and requires user input. Here we propose a pipeline that can automate this process through scripting commands. 3D reconstruction software can be automatically controlled by API, and parameters can be passed that will ensure an accurate result. The pipeline can process multiple image sets when executed, so large populations of plants can be efficiently analyzed. The input of the pipeline is an image set or group of image sets, and the output is 3D point cloud and related output such as DEM/orthophoto, as well as phenotypic data such as canopy cover, morphological traits etc. The system is affordable because the hardware is a standard RGB camera that can be handheld over plant pots, or mounted to UAV. Any PC can run the software and pipeline. The softwares are Agisoft Metashape and python/Matlab, which also can be acquired easily . The pipeline is affordable high-throughput because many pots can be quickly photographed with an RGB camera, and the pipeline can handle multiple image sets. In this study, 200 pots were photographed in under 3 hours (6 plants per image set, 34 image sets) and automatically generated pointcloud, DEM/orthophoto for each image set by the pipeline. Each DEM/orthophoto is then used to create CSV containing phenotypic data. This is a scalable solution that can enable researchers to get detailed measurement data with reduced labor and capital costs.

## Introduction

### Background
"High-throughput phenotyping technologies have become an increasingly important topic of crop science in recent years" - Wang Y, 2018
"Accessing  a  plant’s  3D  geometry  has  become  of  significant  importance  for phenotyping  during  the  last  few  years. " - Christian Rose J, 2015
"In recent years, there has been a surge of interest in the construction of geometrically accurate models of plants." - Pound M, 2014
"In recent years, high-throughput plant phenotyping earned momentum, focusing mainly on non-invasive image-based techniques" Agapito L, 2015
"In plant phenotyping, there is a demand for high-throughput, non-destructive systems that can accurately analyse various plant traits by measuring features such as plant volume, leaf area, and stem length." - Golbach F, 2016
"Reconstructing plant surfaces from point cloud data is important for several applications in plant science, including estimating the leaf area and volume of the plant (Moorthyet  al.2008 )" Kempthorne D, 2014
Similar statement to above?


### Purpose
x

### Current techniques
x

### difference of our work
x

## Materials and Methods

### Section 1: Photos to PCD
x

### Section 2: PCD to Traits
x

## Results

### Section 1: Photos to PCD
x

### Section 2: PCD to Traits
x

## Discussion
x

## Conclusion 
x

### Future Work
x