# System Design: Search Engine

## Overview: Scenario-Based DSA Problem (40 minutes)

This project implements a search engine that allows users to search for studies based on keywords. The search engine uses an inverted index to store and retrieve study titles that contain the given keywords.

💡 Scenario:
"You are building a feature for a research platform where users can search for past research studies they participated in. The search system must handle millions of queries efficiently. Each study has a unique study_id, a title, a category, and a description. Users should be able to:"

- Search studies by keyword (title or description)
- Get search results ranked by relevance (i.e., keyword frequency)
- Support autocomplete suggestions when users start typing

Your Task:

- Design a system to store and search studies efficiently.
- Choose the best data structure for fast search and ranking.
- Implement a function search_studies(keyword: str) -> List[str] that returns study titles matching the keyword.
- Optimize for fast lookups, considering scalability.

## Clarifications

I understand that this system is basically like a search engine. I have a couple of questions to clarify some things (how many searches per second do we want to have?, do we want to require the unique fields in search queries?). But I am mindful of the fact that we have 40 minutes, and I know that cannot be enough time to thoroughly complete all these tasks. Is there an aspect you'd like me to focus on first?

## 🎯 Prioritizing the Problem

You're absolutely right! We don’t have enough time to build everything, so let’s focus on:

✅ Step 1: Choosing the Right Data Structure for efficient search

✅ Step 2: Implementing search_studies(keyword: str) -> List[str]

✅ Step 3 (if time permits): Adding autocomplete functionality.

![Storage Options](data_structure.png)

Inverted Index is how search engines work. Trie is useful for autocomplete if we have time later.

## The Design

Since this system behaves like a search engine, we need a design that supports fast lookups, filtering, ranking, and scalability. Instead of just storing studies in a traditional database, we should optimize for search efficiency and retrieval speed.

### 🎯 Step 1: Understanding the Requirements

📌 Before choosing a data store, let’s break down our core functional needs:

- Keyword-Based Search → Users should be able to search by title, description, or keywords.
- Filtering by Category → Every study belongs to a unique category, so we need efficient category-based filtering.
- Autocomplete → The system should provide real-time suggestions when users start typing.
- Scalability → The search system should support millions of studies and handle high query loads.
- Ranking by Relevance → More relevant results should appear higher in the search results.

📌 Given these requirements, we need to choose the right data store.

### 💾 Step 2: Choosing the Right Storage Solution

💡 "We have two main options: a relational database (SQL) or a specialized search engine (NoSQL or full-text search database)."
![Storage Options](storage_options.png)

Given that we need a high-performance search system, we should use Elasticsearch as the primary search engine, supported by Redis for autocomplete. This setup provides fast full-text search, ranking, and real-time suggestions.

### 🛠 Step 3: Designing the Data Model

💡 "Now that we’ve picked Elasticsearch, we need to define our document schema."

📌 Study Document Structure (Stored in Elasticsearch)

```json
{
  "study_id": 1,
  "title": "Machine Learning in Psychology",
  "description": "Understanding cognition using ML",
  "category": "Cognitive Science",
  "keywords": ["machine learning", "cognition", "psychology"],
  "timestamp": "2024-02-10T12:00:00Z"
}
```

✔ Why this structure?

The keywords field improves search relevance.
The category field allows efficient filtering.
The timestamp field enables sorting by recency.
📌 Indexing Strategy in Elasticsearch

- Title & description → Full-text search
- Category → Keyword-based filtering
- Timestamp → Sorting by recency
