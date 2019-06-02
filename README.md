# Bloom filter based spell checker
A simple spell checker program implemented using bloom filter, also includes:
1. performance comparison test and charting for different filter sizes.
2. a demo program to find possible typos from an article.

# How to run
The program will require python3 and charting requires matplotlib.
## To run performance test and generate charts
```python
python test_spell_checker.py
```
*default dictionary to load: /data/wordlist.txt
## To detect typos from text
```python
python run_spell_checker.py
```
*sample article: /data/article.txt
# Test results
We generate 1,000 words, each with length of 5, and check if it exist in our spell checker's dictionary. We compare this result with a lookup in the original word list and calculate the discrepancies.

We also see the correlations between false positive rete and the filter occupancy rate. This indicates that a more occupied filter (more positions set to True) tend to provide poorer performance, and by increasing filter size, we can dramatically promote performance and reduce false positive rate.
![Test Results](/image/spell_cheker.jpg)
