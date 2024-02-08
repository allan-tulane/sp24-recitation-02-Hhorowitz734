# CMPS 2200  Recitation 02

**Name (Team Member 1):** Benjamin Horowitz  

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where $W(1) = 1$.

- [ ] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [ ] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [ ] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [ ] 4. (2 point) Now, derive the asymptotic behavior of $W(n)$ using $f(n) = 1$, $f(n) = \log n$ and $f(n) = n$. Then, generate actual values for $W(n)$ for your code and confirm that the trends match your derivations.

- Yes, the values match the ones I derived by hand. This is for constant a = b = 2:

![Runtime Calculations By Hand](runtime_calculations.png "Runtime Calculations By Hand")

| n    | f(n) = 1          | f(n) = log n       | f(n) = n          |
|------|-------------------|---------------------|-------------------|
| 2    | 3                 | 2.6931471805599454  | 4                 |
| 4    | 7                 | 6.772588722239782   | 12                |
| 8    | 15                | 15.6246189861594    | 32                |
| 16   | 31                | 34.02182669455858   | 80                |
| 32   | 63                | 71.50938929191688   | 192               |
| 64   | 127               | 147.17766166719343  | 448               |
| 128  | 255               | 299.2073535983065   | 1024              |
| 256  | 511               | 603.9598846410926   | 2304              |
| 512  | 1023              | 1214.1580939072246  | 5120              |
| 1024 | 2047              | 2435.2476596200486  | 11264             |


- [ ] 5. (4 points) Now that you have a nice way to empirically generate valuess of $W(n)$, we can look at the relationship between $a$, $b$, and $f(n)$. Suppose that $f(n) = n^c$. What is the asypmptotic behavior of $W(n)$ if $c < \log_b a$? What about $c > \log_b a$? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of $n$) to justify your answer. 

- The relationship between $a$, $b$, and $f(n)$ and the comparison between $c$ and $ \log_b a$ is the three cases of the Master Theorem. 
- Case 1 -> If $c > \log_b a$, this is the leaf dominated case, and therefore $O(n^{\\log_b a})$
- Case 2 -> If $c < \log_b a$, this is the root dominated case, and therefore $O(n)$
- Case 3 -> If $c = \log_b a$, this is the balanced case, and therefore $O(nlog(n))$
- I ran test_compare_work for a = 2 and b = 2 given two cases: c = .5 and c = 2. The results were as expected, with the leaf dominated case having a much faster rise in work than the root dominated case.

| n     | Case 1: c < log_b(a) | Case 2: c > log_b(a) |
|-------|----------------------|----------------------|
| 10    | 21.291267864660337   | 174                  |
| 20    | 47.054671684320255   | 748                  |
| 50    | 110.23620513578395   | 4790                 |
| 100   | 230.4724102715679    | 19580                |
| 1000  | 2075.117102760963    | 1990744              |
| 5000  | 14251.20819850244    | 49957880             |
| 10000 | 28602.41639700488    | 199915760            |


- [ ] 6. (3 points) $W(n)$ is meant to represent the running time of some recursive algorithm. Suppose we always had $a$ processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by $W(n)$. Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

![Explanation of function spans by hand](span_explanation.png "Explanation of function spans by hand")
