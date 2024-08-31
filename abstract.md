### Abstract

Excel is not a database.  As such, it lacks the data integrity constraints and flexible analysis methods that databases provide.  Nevertheless, it is widely used across science to store and process tables of data.  The aim of this presentation is to use SQLite, which is an open source database used in billions of applications, to demonstrate how easy it can be to use a real database instead.

I will use data from the Global Volcanism Program to show how data are stored, queried, filtered and analysed using Structured Query Language (SQL) methods such as GROUP BY and JOIN.  I will also show how "relations" can be used to build a sample database that separates concepts such as collection site and avoids repetition.

The tooling around SQLite has improved greatly in the last decade.  In this presentation, I use DbBrowser for SQLite as a general front-end, QGIS for custom forms and Datasette for sharing data across a network.  Finally, I will introduce `etlhelper`.  This is a Python library that we have developed at the British Geological Survey to simplify data transfer into and out of databases (including SQLite).  This makes using SQLite in scripted workflows even easier.

#### Prerequisites

There are no required skill level. Attendees familiar with Python will get the most from the end section.

#### Outcomes

Attendees unfamiliar with relational database systems and SQL will learn the benefits that they provide and how to get started with them. More experienced attendees will hopefully learn additional tools that can improve their workflows.