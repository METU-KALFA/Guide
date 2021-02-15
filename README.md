# Guide
The blueprint repository for the Kovan Github. This repository is made to agree on GitHub usage, project development and code documentation. It consists of documentation files such as Doxygen html and guide Python codes for Doxygen and Sphinx documentation. Codes have example comments to explain comment tags and comment styles. The repository has a Wiki page which includes more comprehensive discussions on conventions. In fact, README.md of the repository only explains how to arrange the Readme file for a Kovan project repository. For further information on other concepts, one should examine guide codes, issues and wiki page. 

Add badges which makes tracking easier. Check [shields.io](https://shields.io/).
**Note:** Sections below are not compulsory. Some of them are special to some cases and put here to have a look up. If you do not need a section (eg. [status](#status)), exclude it from the readme.

Readme file composed of:
* [Introduction](#introduction)
* [Features](#features)
* [Prerequisites](#prerequisites)
* [Installation](#installation)
* [Usage](#usage)
* [Author(s)](#authors)
* [Acknowledgements](#acknowledgements)
* [Status](#status)

# Introduction

Describe the project by answering the following questions:
* What is the project?
* What is the aim of the project?

It should be as short as possible. In some articles, the length of introduction is described as 30 words. Also, this section can be viewed as an elevator pitch of the project.

# Features

Shortly describe the project's features and ToDo.

* Describe the project outline
* Define comment style

**ToDo:**
* Add a wiki page
* Add badges
* Add command line command as an example
* Add code segments as examples

# Prerequisites

**Note:** Other name proposals are Background, Libraries, Technologies.

If necessary, list the used library, language and framework versions. Version differences make installation harder if there is a mismatch. Add any permission requirement if exists. As a motivation, it is said that listing used technologies grabs the recruiters' attention since they have limited time to search a candidate.

* Python 2.7
* pip >= 19.3

# Installation

List Installation steps. Mention encountered errors and existing/used solutions. 

# Usage

Add necessary commands to run the project.  
**Examples:**
```
rosrun ur5_gripper demo.py
```
```
source ~/anaconda/bin/activate
conda activate necessary-env
python test.py
```
```
source ~/anaconda/bin/activate
conda activate necessary-env
python test.py
```
```
# open 3 terminals, on the first one launch gazebo:
source ~/ros_workspace/catkin_ws/devel/setup.bash
roslaunch ur5_gripper ur5_gripper.launch [limited:=true]

# on the second one launch moveit:
source ~/ros_workspace/catkin_ws/devel/setup.bash
roslaunch ur5_gripper_moveit_config ur5_gripper_moveit_planning_execution.launch sim:=true [limited:=true]

# on the third one launch rviz:
source ~/ros_workspace/catkin_ws/devel/setup.bash
roslaunch ur5_gripper_moveit_config moveit_rviz.launch config:=true
```
# Author(s)

Burak Bolat: burakbolatcs@gmail.com
Özgür Aslan: ozgraslan17@gmail.com

# Acknowledgements

This Readme is written with the help of the following web articles:
* https://bulldogjob.com/news/449-how-to-write-a-good-readme-for-your-github-project
* https://www.makeareadme.com/
* https://www.redhat.com/sysadmin/how-write-readme

# Status

Mention the status of the project and give a roadmap, advices for the successors.
