# AA228-CS238-Nanxi_Jiang
[![AA228/CS238 Gradescope](https://img.shields.io/badge/aa228%2Fcs238-gradescope-green?color=42a0a2)](https://www.gradescope.com/courses/814395)


[AA228/CS238: Decision Making under Uncertainty](https://aa228.stanford.edu), Autumn 2025, Stanford University.

This repository contains code and data for CS 238 Projects.

## Project 0: 

[![Project 0 Details](https://img.shields.io/badge/project0-details-blue)](https://aa228.stanford.edu/project-0/)

## Project 1: Bayesian Structure Learning

[![Project 1 Details](https://img.shields.io/badge/project1-details-blue)](https://aa228.stanford.edu/project-1/) [![Project 1 Template](https://img.shields.io/badge/project1-LaTeX%20template-white)](https://www.overleaf.com/read/hxwgtnksxtts)

    project1/
    ├── data                    # CSV data files to apply structured learning
    │   ├── small.csv               # Titanic dataset¹
    │   ├── medium.csv              # Wine dataset²
    │   └── large.csv               # Secret dataset
    ├── example                 # Helpful examples
    ├── output_large.gph             # Output dag of large.csv
    ├── output_large.score             # Bayesian score for dag of large.csv
    ├── output_medium.gph             # Output dag of medium.csv
    ├── output_medium.score             # Bayesian score for dag of medium.csv
    ├── output_small.gph             # Output dag of small.csv
    ├── output_small.score             # Bayesian score for dag of small.csv
    └── project1.py             # K2 algorithm implementation (Python)

<sup>1</sup>https://cran.r-project.org/web/packages/titanic/titanic.pdf
<br>
<sup>2</sup>https://archive.ics.uci.edu/ml/datasets/Wine+Quality

## Project 2: Reinforcement Learning

[![Project 2 Details](https://img.shields.io/badge/project2-details-blue)](https://aa228.stanford.edu/project-2/) [![Project 2 Template](https://img.shields.io/badge/project2-LaTeX%20template-white)](https://www.overleaf.com/read/gsptsmcrzpdv)

[LaTeX Overleaf template](https://www.overleaf.com/read/gsptsmcrzpdv): click the link, go to "Menu", and "Copy Project" (make sure you're signed into Overleaf). Note this is an optional template, you're free to use your own (or not even LaTeX).

    project2/
    └── data                      # CSV data files of (s,a,r,sp)
        ├── small.csv                 # 10x10 grid world
        ├── medium.csv                # MountainCarContinuous-v0
        └── large.csv                 # Secret RL problem

*Note: no starter code provided for Project 2.*

## Contact
Please post on [Ed](https://edstem.org/) with any questions regarding this code, the data, and the projects in general. We'd be happy to help!
