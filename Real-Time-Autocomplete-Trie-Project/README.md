# Real-Time Autocomplete System (Standard & Ternary Trie)

**Course:** INFR2820U – Algorithms and Data Structures  
**Professor:** Sara Motlagh  
**Date:** July 31, 2025  
**Group 10:** Dorothy Sahijwani, Fatimah Kamal, Izzat Ikram, Sameer Khan  

---

###  Overview
This project implements a **real-time text autocompletion system** using two data structures:
- **Standard Trie (Prefix Tree)**
- **Ternary Search Trie**

The system predicts words as the user types a prefix. For example, given words  
`["Sample", "Samplers", "Same", "Sampling", "Summer", "Sad"]`,  
typing “Sam” suggests:  
**Sample, Samplers, Same, Sampling**

---

###  Implementation Files
- `annotated-Final Project Q1.py.pdf` — Python code for both Tries  
- `annotated-DSA final project.pdf` — Space/time complexity, ranking, and structure analysis  
- `INFR2820-Final Project.pdf` — Original project guidelines and rubric

---

###  Key Learnings
- Compared **Standard Trie** and **Ternary Trie** in space/time efficiency  
- Implemented optional **ranking algorithm** to prioritize frequently used words  
- Explored **Compressed Trie**, **Array**, and **Linked List** variations for optimization  

---

###  Complexity Summary
| Structure | Time Complexity | Space Complexity |
|------------|----------------|-----------------|
| Standard Trie | O(m + p) | O(n × m) |
| Ternary Trie | O(m log a + p) | O(n × m) |
| With Ranking | O(m + p log p) | O(n × m) |
| Compressed Trie | O(m + p log p) | O(n) best case |

*(m = prefix length, n = total words, p = matched results, a = alphabet size)*

---

###  Description
This was the **final project** for the Algorithms and Data Structures course at Ontario Tech University, worth 15% of the total grade. It focused on analyzing data structure efficiency, complexity notation, and ranking algorithms.

---

###  License
This academic project is shared for educational and portfolio purposes only.
