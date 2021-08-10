<h1>Group 14: Redshield 👋</h1>
<p align="center">
![pipeline status](https://gitlab.ecs.vuw.ac.nz/course-work/engr300/2021/group14/group-14/badges/development/pipeline.svg)
![python](https://img.shields.io/badge/python-%2314354C.svg?style=flat&logo=python&logoColor=white)
</p>



## About
This project is home to project 14, a plugin for mitmproxy designed to prevent unsafe script execution & XSS attacks on webpages.

Client: Red Shield (Point of Contact: Kirk Jackson)

Scheduled Lab Times: Tuesday 10am - 12pm & Thursday 10am - 12pm


### Features
- Attach nonce tags to safe scripts
- Identify unsafe scripts
- Report unsafe scripts using report-uri
- Minimal user impact

### Authors: 
Damien Tamasese, Dylan Simpson, Isabella Maria, James Houlihan, Jaya Narayan, Nathan Wong, Timothy McDermott

 
  
## Installation

Install with git

```bash

```

## Usage

To deploy this project run

```
pip install -e .
mitmproxy -s /path-to/main.py
```

## Demo

Insert gif or link to demo

  
## Contributing
Create seperate branches for each feature from the development branch. Features should pass pipeline before being merged back into development.
Master should always hold a functional demo of the project, only merge working versions from development


  
