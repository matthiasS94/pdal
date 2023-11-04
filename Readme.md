# Pointcloud filter (ground via SMRF)

This Repository contains the automatic LAS-pointcloud filter via PDAL in a Docker Container.

## How to setup

1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/)
2. (if necessary) Enable Hyper-V (Hardware assisted virtualization) in BIOS
3. Run Docker Desktop

## How to use

1. Copy your LAS-pointcloud-files to "pdal/pointcloud/raw"
2. Run on your command line:
   ```shell
   docker-compose run pdal
   ```
3. Transer or use your filtered LAS-pointcloud-files from "pdal/pointcloud/filtered"
