#!/usr/bin/env python
# coding: utf-8

# # Homework 1: Basic Python, Arrays, and DataFrames
# 
# ## Due Tuesday, April 18th at 11:59PM
# 
# Welcome to Homework 1! This week's homework will cover basic Python, arrays, and DataFrames. You can find additional help on these topics in [Chapter 1](https://www.inferentialthinking.com/chapters/01/what-is-data-science.html) of Computational and Inferential Thinking and [BPD 1-11](https://notes.dsc10.com/01-getting_started/tools.html) in the `babypandas` notes.
# 

# ### Instructions
# 
# Remember to start early and submit often. You are given six slip days throughout the quarter to extend deadlines. See the syllabus for more details. With the exception of using slip days, late work will not be accepted unless you have made special arrangements with your instructor.
# 
# **Important**: For homeworks, the `otter` tests don't usually tell you that your answer is correct. More often, they help catch careless mistakes. It's up to you to ensure that your answer is correct. If you're not sure, ask someone (not for the answer, but for some guidance about your approach). These are great questions for office hours (the schedule can be found [here](https://dsc10.com/calendar)) or Ed. Directly sharing answers is not okay, but discussing problems with the course staff or with other students is encouraged. 

# In[34]:


# Please don't change this cell, but do make sure to run it.
import babypandas as bpd
import matplotlib.pyplot as plt
import numpy as np
import otter
grader = otter.Notebook()

plt.style.use('ggplot')


# ## 1. Characters in The Wonderful Wizard of Oz 👠🧠❤️🦁

# In Lecture 1, we counted the number of times that the characters Amy, Beth, Jo, Meg, and Laurie were named in each chapter of the classic book _Little Women_. In this question, we'll look at another classic book – _The Wonderful Wizard of Oz (1900)_ by L. Franke Baum and illustrated by W.W. Denslow. In 1956, the copyright protections of the original book (but not the 1939 film produced by Metro-Goldwyn-Mayer!) expired, and so sites like Project Gutenberg are now able to post copies of the book without violating any copyright laws. [Click here](https://www.gutenberg.org/files/55/55-h/55-h.htm) to read a version of the book that has all of its original illustrations!

# <center><img src=data/wizard-of-oz-illustration.png width=350>(<a href="https://www.nypl.org/events/exhibitions/galleries/childhood/item/5458">source</a>)</center>

# Four of the main characters in _The Wonderful Wizard of Oz_ are Dorothy Gale (👠), Scarecrow (🧠), The Tin Man (❤️), and The Cowardly Lion (🦁).
# 
# Below, we've written code that shows the number of mentions of each of these four characters in the first 12 chapters of the book. However, instead of displaying this information in a line chart, as was done in Lecture 1, we will use a bar chart.
# 
# Run the cell below to generate this bar chart of the first 12 chapters. This cell contains code that hasn't yet been covered in the course. It isn't expected that you'll understand the code, but you should be able to interpret the bar chart it generates.

# In[2]:


# Open the book and split it into chapters.
book_file = 'data/the-wonderful-wizard-of-oz.txt'
raw_book = open(book_file, encoding="utf-8").read()
end_pos = raw_book.index('Chapter XIII')
chapters = raw_book[:end_pos].split('Chapter ')[1:]

# Find the number of words in each chapter.
chapter_lengths = (np.array([len(c.split(' ')) for c in chapters]) / 100)

# Find the number of mentions per 100 words for each character and chapter.
characters = bpd.DataFrame().assign(
    Chapter=np.arange(1, 13),
    Dorothy=np.char.count(chapters, 'Dorothy') / chapter_lengths,
    Scarecrow=np.char.count(chapters, 'Scarecrow') / chapter_lengths,
    Lion=np.char.count(chapters, 'Lion') / chapter_lengths,
    Tin_Man=np.char.count(chapters, 'Tin Woodman') / chapter_lengths
)

characters.plot(kind='bar', x='Chapter', figsize=(14, 8))
plt.ylabel('Mentions per 100 words in chapter');


# Looking at the bar chart, we see that the height of the bar for Dorothy in Chapter 1 is 1.62 and the y-axis of this graph is “Mentions per 100 words in chapter”;  this means that 1.62 of every 100 words in Chapter 1 are `"Dorothy"`. In other words, $1.62\%$ of the words in Chapter 1 are `"Dorothy"`.

# **Question 1.1.**  The following sentences are the very first time Scarecrow, Tin Man (real name Tim Woodman), and the Lion are mentioned in the book, respectively:
# 
# > There was a great cornfield beyond the fence, and not far away she saw a Scarecrow, placed high on a pole to keep the birds from the ripe corn.
# 
# > "Oil my neck, first," replied the Tin Woodman.
# 
# > Just as he spoke there came from the forest a terrible roar, and the next moment a great Lion bounded into the road.
# 
# Which chapters are each of these sentences from? Assign the variables `scarecrow_debut`, `tin_man_debut`, `lion_debut` to an integer between 1 and 12.

# In[3]:


scarecrow_debut = 3
tin_man_debut = 5
lion_debut = 6


# In[4]:


grader.check("q1_1")


# **Question 1.2.** Dorothy is mentioned 38 times in Chapter 12. How many times is Lion mentioned in Chapter 12? Assign the variable `lion_mentioned` to 1, 2, 3, 4, or 5 corresponding to the answer choices below. Remember to input your answer as a **number from 1-5 corresponding to the option numbers below, and not to the number of times Lion is mentioned.** For example, if you think Lion is mentioned 13 times, you should set `lion_mentioned` to 5, not 13.
# 
# 1. 20 times
# 1. 15 times
# 1. 17 times
# 1. 19 times
# 1. 13 times

# In[5]:


lion_mentioned = 3


# In[6]:


grader.check("q1_2")


# In[ ]:





# **Question 1.3.** Chapter 11 is quite long, as its the chapter when the characters reach the Emerald City. For reference, Chapter 8 is 1764 words long while Chapter 11 is 3294 words long. Based on this information and the plot, which of the following is correct? Assign the variable `oz_part3` to 1, 2, 3, or 4.
# 
# 1. Scarecrow is mentioned more times in Chapter 8 than in Chapter 11. Tin Man is mentioned more times in Chapter 8 than in Chapter 11.
# 1. Scarecrow is mentioned more times in Chapter 8 than in Chapter 11. Tin Man is mentioned fewer times in Chapter 8 than in Chapter 11.
# 1. Scarecrow is mentioned fewer times in Chapter 8 than in Chapter 11. Tin Man is mentioned more times in Chapter 8 than in Chapter 11.
# 1. Scarecrow is mentioned fewer times in Chapter 8 than in Chapter 11. Tin Man is mentioned fewer times in Chapter 8 than in Chapter 11.

# In[7]:


oz_part3 = 2


# In[8]:


grader.check("q1_3")


# **Question 1.4.** Which of the following is a valid conclusion we can make based off of the above plot alone? Assign `oz_part4` to 1, 2, 3, 4, or 5. There is only one correct answer.
# 
# 1. Lion is mentioned more times in Chapter 10 than he is in Chapter 6.
# 
# 1. The chapter that Tin Man is mentioned the most in is Chapter 12.
# 
# 1. Lion is mentioned roughly the same number of times in each of Chapters 6, 8, and 10.
# 
# 1. The chapter that Dorothy is mentioned the least in is Chapter 8.
# 
# 1. Scarecrow and Tin Man are mentioned roughly the same number of times in Chapter 6.

# In[97]:


oz_part4 = 5


# In[98]:


grader.check("q1_4")


# *Note:* The tests in this section only check that you set each variable to a number in the correct range. Unlike in labs, tests in homeworks **do not** check that you answered correctly; they only check that your answer is *reasonable*, or in the correct format. To put it another way: all of your tests might pass, but that doesn't mean you'll get full credit – some of your answers may still be wrong. It's up to you to make sure that they're right!

# ## 2. Python Basics 🐍

# **Question 2.1.** When you run the following cell, Python produces a cryptic error message.

# In[99]:


#2023 = 2025 - 2.0


# Choose the best explanation of what's wrong with the code, and then assign 1, 2, 3, or 4 to `basics_part1` below to indicate your answer.
# 
# 1. The left hand side is an `int`, while the right hand side is a `float`. It should be `2023.0 = 2025 - 2.0`.
# 
# 1. This is trying to create a variable named `2023`, which doesn't make sense because `2023` is a number.
# 
# 1. The result should be written after the calculation. It should be `2025 - 2.0 = 2023`.
# 
# 1. Python is not able to subtract a `float` from an `int` because they are of different data types.
# 

# <font color=red>**🚨 Important: Once you have finished this question, "comment"  out the above code cell out by replacing it with `# 2023 = 2025 - 2.0`. This will prevent the error message from appearing when your notebook is graded.**</font>

# In[100]:


basics_part1 = 2


# In[101]:


grader.check("q2_1")


# **Question 2.2.** Consider the following poorly-written code.

# In[102]:


two = 2
three = 3
two = two + three
two = two * three
two = two * two
two = -two


# As this code executes, what values does the variable `two` take on? Assign 1, 2, 3, or 4 to `basics_part2` to indicate your answer.
# 
# 1. The variable `two` takes on the values 2, 5, 6, 4, -4.
# 
# 2. The variable `two` takes on the values 2, 5, 6, 12, -12.
# 
# 3. The variable `two` takes on the values 2, 5, 15, 225, -225.
# 
# 4. The variable `two` takes on the values 2, 5, 12, 144, -144.

# In[103]:


basics_part2 = 3


# In[104]:


grader.check("q2_2")


# ## 3. Road Trip   🚘 

# Over spring break, you went on a road trip with a friend. Now, you want to perform some calculations on data you gathered throughout your journey. Answer the questions below, using Python to perform all the intermediate calculations, such as adding, squaring, and dividing.
# 
# Note that the `math` package has not been imported. You don't need it for this question, and **you should not import it**, otherwise the autograder may produce an error.
# 
# **Question 3.1.** On the first day of the trip, your friend drove the car at three different speeds, for varying lengths of time, as shown below:
# 
# | Journey | Speed (miles per hour) | Time (hours)|
# | --- | --- | --- |
# | Part 1 | 56 | 3 |
# | Part 2 | 43 | 4 |
# | Part 3 | 80 | 2 |
# 
# 
# Using this information, calculate the average speed, in miles per hour, at which your friend drove the car that day, and assign your answer to the variable `means_part1`. Recall from math and physics that average speed is the total distance divided by total time.

# In[105]:


# Feel free to define intermediate variables to use in your solution.


total_distance = (56*3)+(43*4)+(80*2)
total_time = 3+4+2
means_part1 = total_distance/total_time
means_part1


# In[106]:


grader.check("q3_1")


# **Question 3.2.** On the second day of the trip, your friend drove the car three times again, but this time at the speeds and distances seen below:
# 
# | Journey | Speed (miles per hour) | Distance (miles)|
# | --- | --- | --- |
# | Part 1 | 56 | 3 |
# | Part 2 | 43 | 4 |
# | Part 3 | 80 | 2 |
# 
# Using this information, calculate the average speed, in miles per hour, at which your friend drove the car that day, and assign your answer to the variable `means_part2`. 
# 
# Note that the third column is **Distance (miles), not Time (hours).** Unlike in Question 3.1, you aren't given the amount of time that each part of the journey took; you need to compute these times yourself. To calculate the time taken for each part of the journey, divide the distance for that part by the speed for that part. Finally, add up the times for the three parts of the trip to find the total time.

# In[107]:


# Feel free to define intermediate variables to use in your solution.


total_distance2 = 3+4+2
total_time2 = (56*3)+(43*4)+(80*2)

means_part2 = total_distance2/total_time2
means_part2


# In[108]:


grader.check("q3_2")


# **Question 3.3.** On the way back home, your friend stops at a pet store to buy an aquarium. The only one available is a rectangular tank, which unfortunately doesn't fit in the car because of your suitcases. This tank has a height of 34 inches, a width of 47 inches, and a length of 65 inches. 
# 
# Your friend thinks that the aquarium would have fit in the car with all your suitcases if it had the same volume, but was shaped as a cube instead. What would the length of each side of such an aquarium be in inches? Save your answer in the variable `means_part3`.

# In[123]:


# Feel free to define intermediate variables to use in your solution.


means_part3 = (56*43*80)**(1/3)
means_part3


# In[122]:


grader.check("q3_3")


# In this problem, though you calculated three different quantities in three different ways, all of your results are actually considered **means**, of various kinds!
# 
# In Question 3.1., given $n$ values $x_1, x_2, ..., x_n$, you found an *arithmetic mean*, using the formula
# 
# $${x_1+x_2+...+x_n \over n},$$
# 
# where the numerator represented total distance and the denominator represented total time. An arithmetic mean is the usual type of mean or average you're used to seeing. It turns out that you actually computed a more sophisticated arithmetic mean, known as a _weighted arithmetic mean_, 
# 
# $$\frac{w_1 x_1 + w_2 x_2 + ... + w_n x_n}{w_1 + w_2 + ... + w_n}$$
# 
# where the weights $w_1, w_2, w_3$ were the times travelled in each part of the journey.
# 
# In Question 3.2., given  $n$ values $x_1, x_2, ..., x_n$, you found a *harmonic mean*, using the formula
# 
# $${n \over {{1 \over x_1}+{1 \over x_2}+ ... + {1 \over x_n}}},$$ 
# 
# 
# where the numerator represented total distance and the denominator represented total time. To calculate the total time, you needed to sum the time taken for each part of the trip, calculated using the fact that time is distance over speed. Again, it turns out that you actually computed the _weighted harmonic mean_, but this time the weights were the distances travelled. If you're curious, see the formula [here](https://en.wikipedia.org/wiki/Harmonic_mean#Weighted_harmonic_mean).
# 
# Finally in Question 3.3., given $n$ values $x_1, x_2, ..., x_n$, you found a *geometric mean*, using the formula 
# 
# $${\sqrt[n]{x_1 \cdot x_2 \cdot ... \cdot x_n}},$$ 
# 
# where each value represented a dimension of the rectangular tank. 
# 
# As you can see, there are many different notions of mean. You'll learn about some of them if you take DSC 40A!

# ## 4. Beverage Consumption Among Youth 🧃

# In this problem, we want to quantify how *dissimilar* three different age categories (little kids, big kids, and teens) are, in terms of their beverage consumption, using three commonly consumed beverages (water, milk, and soft drinks).
# 
# The data below comes from the CDC's [Beverage Consumption Among Youth in the United States, 2013-2016](https://www.cdc.gov/nchs/products/databriefs/db320.htm).
# 
# | Percent of Total Beverage Consumption       | Little Kids (Ages 2-5)  | Big Kids (Ages 6-11)  | Teens (Ages 12-19) |
# |-------------------------------------------|-------------|-----------|-----------|
# | Water        | 39.5 | 41.9 | 47.0 | 
# | Milk       | 32.1 | 24.4 | 14.5 | 
# | Soft Drinks    | 13.0 | 20.9  | 22.3 | 
# 
# We define the **dissimilarity** between two age groups as the largest absolute difference between their 3 respective consumption percentages.
# 
# To better understand dissimilarity, consider the following hypothetical situation.
# * Age group A's *consumption of water* is **10 percent more** than age group B's.
# * Age group A's *consumption of milk* is **3 percent less** than age group B's.
# * Age group A's *consumption of soft drinks* is **7 percent less** than age group B's.
# 
# Here, we would say the dissimilarity between age group A and age group B is 10, since 10 is larger than both 3 and 7.

# **Question 4.1.** 
# Using this method, compute the dissimilarity between big kids and teens.  Assign the result to the variable `dissimilarity`. Use a single expression (a single line of code) to compute the answer. Let Python perform all the arithmetic (like subtracting) rather than simplifying the expression yourself. 
# 
# *Hint:* The built-in `abs` function computes absolute values. 

# In[111]:


dissimilarity = max(abs(np.array([41.9,24.4,20.9])-np.array([47.0,14.5,22.3])))
dissimilarity


# In[112]:


grader.check("q4_1")


# **Question 4.2.** Which pair of age groups is **most** dissimilar, according to this measurement? Assign either 1, 2, or 3 to the variable `most_dissimilar` below.
# 
# 1. little kids and big kids
# 1. big kids and teens
# 1. little kids and teens

# In[113]:


most_dissimilar = 3


# In[114]:


grader.check("q4_2")


# **Question 4.3.** It turns out that if we eliminated a certain one of the three beverage percentages in the table (for example, getting rid of the soft drinks row) and recalculated dissimilarities based on the remaining two percentages only, we would find the dissimilarity between each pair of age groups to be the same as if we had used all three percentages. In other words, one of the three rows of the table ends up not factoring into the calculation for dissimilarity for all three pairs of age groups.
# 
# Which percentage can be eliminated without changing the dissimilarity of any pair of age groups in the table? Assign either 1, 2, or 3 to the variable `disposable` below.
# 
# 1. The consumption percentage of water.
# 1. The consumption percentage of milk.
# 1. The consumption percentage of soft drinks.

# In[115]:


disposable = 1


# In[116]:


grader.check("q4_3")


# ## 5. Arrays 🗃️

# **Question 5.1.** Make an array called `quirky_numbers` containing the following numbers (in the given order):
# 
# 1. The square root of 54
# 2. 136 degrees, in radians
# 3. $6^3 + 5^8$
# 4. The mathematical constant of $e$ over 4: $\frac{e}{4}$
# 5. The base 10 logarithm of 46
# 
# *Hint:* Check out the functions constants available in the `numpy` module, which has been imported as `np`. If you're unsure of what function to use, a quick Google search should do the trick.  Do **not** import `math` or any other modules. 
# 
# *Note:* In this problem, as with all others, we'll only check that your answer is correct. There may be several valid ways to produce the correct answer.

# In[117]:


quirky_numbers = np.array([54**(1/2), np.deg2rad(136), ((6**3)+(5**8)),np.e/4,np.log10(46)])
quirky_numbers


# In[118]:


grader.check("q5_1")


# **Question 5.2.** Make an array called `likes` containing the following three strings, in the specified order:
# - `'I like baking'`
# - `'cats'`
# - `'and tea!'`
# 
# <!--
# BEGIN QUESTION
# name: q5_2
# -->

# In[119]:


likes = np.array(['I like baking','cats','and tea!'])
likes


# In[33]:


grader.check("q5_2")


# <center><img src=data/cat-baking.png width=300>(<a href="https://www.popsugar.com/pets/videos-of-orange-cat-making-desserts-48112259">source</a>)</center>
# 
# 
# In [Lecture 3](https://dsc10.com/resources/lectures/lec03/lec03.html#String-methods), we looked at several string methods, like `upper` and `replace`. Strings have another method that we haven't seen yet, called `join`. `join` takes one argument, an array of strings, and it returns a single string. Specifically, `some_string.join(some_array)` evaluates to a new string consisting of all of elements in `some_array`, with `some_string` inserted in between each element.
# 
# For example, `'-'.join(np.array(['call', '858', '534', '2230']))` evaluates to `'call-858-534-2230'`.
# 
# **Question 5.3.** Use the array `likes` and the method `join` to make two strings:
# 
# 1. `'I like baking, cats, and tea!'` (call this one `by_comma`)
# 1. `'I like baking cats and tea!'` (call this one `by_space`)

# In[35]:


by_comma = ', '.join(likes)
by_space = ' '.join(likes)

# Don't change the lines below.
print(by_comma)
print(by_space)


# In[36]:


grader.check("q5_3")


# Now let's get some practice accessing individual elements of arrays.  In Python (and in many programming languages), elements are accessed by *integer position*, with the position of the first element being zero. That's probably not the way you learned to count, so it's easy to get mixed up here. Be careful!

# **Question 5.4.** The cell below creates an array of strings.

# In[37]:


some_strings = np.array(['flowers', '🌼', '🌸', '🌱', 'plant', 'dog', '🐶', 'cat', '🐈'])
some_strings


# In[41]:


some_strings[6]


# What is the integer position of `'🐶'` in the array? You can just type in the answer, which should be of type `int`. This is a conceptual question, not a coding question.
# 
# _Note:_ Your answer should be a **positive** integer!

# In[42]:


dog_emoji_position = 6
dog_emoji_position


# In[43]:


grader.check("q5_4")


# **Question 5.5.** Suppose you have an array with 350 elements. What is the integer position of the seventh-to-last element in this array? You can just type in the answer, which should be of type `int`. This is a conceptual question, not a coding question.
# 
# _Note:_ Again, your answer should be a **positive** integer!

# In[52]:


fe=np.arange(0,500)
fe[280]


# In[53]:


seventh_last_position = 280
seventh_last_position


# In[54]:


grader.check("q5_5")


# **Question 5.6.** Suppose you have an array with 763 elements. At what integer position is the middle element of this array? You can just type in the answer, which should be of type `int`. This is a conceptual question, not a coding question.
# 
# _Note:_ Again, your answer should be a **positive** integer!

# In[55]:


762/2


# In[56]:


mid_position = 382
mid_position


# In[ ]:


grader.check("q5_6")


# By the way, it's also possible to use negative integer positions to access elements in an array, which can be easier than using positive integer positions sometimes.  If a position is negative, you count from the end of the array rather than from the beginning. Position -1 corresponds to the last element, -2 corresponds to the second-last element, and so on. For instance, to find the third-to-last element of `some_strings`, we could use:

# In[57]:


some_strings[-3]


# ## 6. DSC 10 Enrollments 📈

# In this question, we'll look at enrollment data from the fall and winter offerings of DSC 10 this academic year. The third column of the table below shows how many UCSD undergraduate students in last winter's offering of DSC 10 come from each of the university's seven colleges. It looks like Sixth College was the most popular, with 81 students. The last column shows how many of those students are DSC majors. Even though Sixth College was the most popular, none of the DSC 10 students from the college were DSC majors!
# 
# For comparison's sake, we also have the corresponding data from the Fall 2022 offering of DSC 10. You can see that most DSC majors take this course in the fall! (Fun fact – this quarter, Spring 2023, there are even fewer declared DSC majors than in the winter.)
# 
# Throughout this problem, we'll assume that all students in previous offerings of DSC 10 come from one of the seven colleges in the table.
# 
# |College|Fall 22 Students|Fall 22 DSC Major Students|Winter 23 Students|Winter 23 DSC Major Students|
# |---|---|---|---|---|
# |Seventh|37|21|45|2|
# |Sixth|93|54|81|0|
# |Roosevelt|67|39|46|4|
# |Warren|61|40|41|1|
# |Marshall|62|32|50|1|
# |Muir|38|27|42|2|
# |Revelle|52|31|43|2|
# 
# In this question, we'll be working with the data from this table as *arrays*. Here are those arrays:

# In[58]:


students_22 = np.array([37, 93, 67, 61, 62, 38, 52])
students_22


# In[59]:


majors_22 = np.array([21, 54, 39, 40, 32, 27, 31])
majors_22


# In[60]:


students_23 = np.array([45, 81, 46, 41, 50, 42, 43])
students_23


# In[61]:


majors_23 = np.array([2, 0, 4, 1, 1, 2, 2])
majors_23


# Remember, the `numpy` package (`np` for short) provides many handy functions for working with arrays. These are specifically designed to work with arrays and are faster than using Python's built-in functions. 
# 
# Some frequently used array functions are `np.min()`, `np.max()`, `np.sum()`, `np.abs()`, and `np.round()`. There are many more, which you can browse by typing `np.` into a code cell and hitting the *tab* key, or by looking at the [documentation](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html).

# **Question 6.1.** Assign `enrolled_22` and `enrolled_23` to the number of students that were enrolled in DSC 10 in Fall 2022 and Winter 2023, respectively.

# In[62]:


enrolled_22 = students_22.sum()
enrolled_23 = students_23.sum()

# Don't change the lines below.
print('Students in Fall 2022:', enrolled_22)
print('Students in Winter 2023:', enrolled_23)


# In[63]:


grader.check("q6_1")


# **Question 6.2.** How many non-DSC major students from the Fall 2022 offering of DSC 10 came from each of the seven colleges? Your answer should be an array called `non_majors_22`, with the colleges in the same order as they appear in the table above. For instance, the first element of `non_majors_22` should be the number of non-DSC majors in the Fall 2022 offering of DSC 10 who were in Seventh College.
# 
# Similarly, how many non-DSC major students from the Winter 2023 offering of DSC 10 came from each of the seven colleges? Your answer should be an array called `non_majors_23`, with the colleges in the same order as they appear in the table above. 
# 

# In[64]:


non_majors_22 = students_22-majors_22
non_majors_22


# In[65]:


grader.check("q6_2_1")


# In[66]:


non_majors_23 = students_23-majors_23
non_majors_23


# In[67]:


grader.check("q6_2_2")


# **Question 6.3.** What percentage of Fall 2022 DSC 10 students from each college were DSC majors? Your answer should be an array called `percent_majors_22`, with the colleges in the same order as they appear in the table above, and with percentages rounded to two decimal places.
# 
# Similarly, what percentage of Winter 2023 DSC 10 students from each college were DSC majors? Your answer should be an array called `percent_majors_23`, with the colleges in the same order as they appear in the table above, and with percentages rounded to two decimal places.

# In[68]:


percent_majors_22 = np.round((majors_22/students_22)*100,2)
percent_majors_22


# In[69]:


grader.check("q6_3_1")


# In[70]:


percent_majors_23 = np.round((majors_23/students_23)*100,2)
percent_majors_23


# In[71]:


grader.check("q6_3_2")


# **Question 6.4.** For each college, what is the absolute difference in the percentage of students enrolled in DSC 10 that are DSC majors from Fall 2022 to Winter 2023? Use `percent_majors_22` and `percent_majors_23` to create an array called `abs_differences`, with the colleges in the same order as they appear in the table above. Make sure the values in your answer are rounded to two decimal places.
# 
# _Note:_ You _don't_ need to round again.

# In[72]:


abs_differences = abs(percent_majors_22-percent_majors_23)
abs_differences


# In[73]:


grader.check("q6_4")


# For your convenience, we repeat the table from the start of the question below.
# 
# |College|Fall 22 Students|Fall 22 DSC Major Students|Winter 23 Students|Winter 23 DSC Major Students|
# |---|---|---|---|---|
# |Seventh|37|21|45|2|
# |Sixth|93|54|81|0|
# |Roosevelt|67|39|46|4|
# |Warren|61|40|41|1|
# |Marshall|62|32|50|1|
# |Muir|38|27|42|2|
# |Revelle|52|31|43|2|
# 
# 
# 
# **Question 6.5.** You might say that the most consistent college is the one with the smallest absolute difference in the percentage of students enrolled in DSC 10 that are DSC majors across the two offerings of the course. Find the smallest value in the `abs_differences` array and save it as `smallest_abs_diff`. Referring back to the table, try to figure out which college that is. Assign `most_consistent_college` to the name of that college (as a string), exactly as it's displayed in the table.
# 
# _Note:_ You can type the name of the college manually.

# In[75]:


smallest_abs_diff = abs_differences.min()
most_consistent_college = "Roosevelt"
smallest_abs_diff


# In[76]:


grader.check("q6_5")


# ## 7. World Cup 🌎⚽

# The Federale Internationale de Football Association (FIFA) is the international governing body of soccer (or football, depending where you're from). FIFA has 209 member countries, making it one of the most respected sports organizations in the world. The organization has hosted an international tournament, called the World Cup, every four years since 1930, except for during WWII. The most recent one took place in 2022 in Qatar. 
# 
# <img src="data/messi.jpeg" width=60%>
# 
# The file `world_cup.csv` in the `data/` directory contains information about every World Cup tournament that has ever taken place. Its columns are:
# 
# | Column      | Description |
# | ----------- | ----------- |
# | `'Year'`      | Year of World Cup     |
# | `'Host'`   | Name of host country        |
# | `'Total Attendance'` | Total number of people in attendance across all matches  |
# | `'Matches'` | Total number of matches played |
# | `'Teams'` | The  total number of teams that competed in the World Cup |
# | `'First'` | Winner of the World Cup |
# | `'Second'` | The team in second place | 
# | `'Third'` | The team in third place|
# | `'Fourth'` | The team in fourth place |

# **Question 7.1.** Read this file into a DataFrame called `world_cup`. 

# In[77]:


world_cup = bpd.read_csv('data/world_cup.csv')
world_cup


# In[78]:


grader.check("q7_1")


# **Question 7.2.** Add a column to `world_cup` called `'Average_Attendance'` that contains the average number of attendees per match in each World Cup tournament. Do not round.

# In[79]:


world_cup = world_cup.assign(Average_Attendance=world_cup.get('Total Attendance')/world_cup.get('Matches'))
world_cup


# In[80]:


grader.check("q7_2")


# **Question 7.3.** Create a new DataFrame, `world_cup_by_year`, by setting the index of `world_cup` to `'Year'`. Don't change `world_cup`.

# In[82]:


world_cup_by_year = world_cup.set_index('Year')
world_cup_by_year


# In[83]:


grader.check("q7_3")


# You should think about why we've chosen to set the index to `'Year'`, instead of any other column.

# **Question 7.4.** Suraj was born in 1998. Where was the World Cup held that year, and what was the average attendance per match that year? Assign your results to `location_98` and `average_98`, respectively.
# 
# Don't type in the answers by hand; get Python to extract this information for you.

# In[84]:


location_98 = world_cup_by_year.get('Host').loc[1998]
average_98 = world_cup_by_year.get('Average_Attendance').loc[1998]

# Don't change the lines below.
print('Location:', location_98)
print('Average attendance per match:', average_98)


# In[85]:


grader.check("q7_4")


# **Question 7.5.** Since the first tournament in 1930, more and more countries have joined FIFA, which means more matches are played in each tournament. Using DataFrame operations, find the number of World Cup tournaments that had more than 55 matches. Assign the number of such tournaments to `over_55_matches`. 

# In[86]:


over_55_matches = world_cup_by_year[world_cup_by_year.get('Matches') > 50].shape[0]
over_55_matches


# In[87]:


grader.check("q7_5")


# **Question 7.6.** Assign `eighth_highest_attendance` to the eighth highest total attendance of all World Cup tournaments. Assign `eighth_highest_year` to the year in which this attendance occurred.
# 
# Again, don't type in these values by hand; get Python to extract this information for you.
# 
# *Note*: Remember that you can perform intermediate steps in the lines before `eighth_highest_attendance` and `eighth_highest_year`.

# In[88]:


eighth_highest_attendance = world_cup_by_year.sort_values(by='Total Attendance',ascending=False).get('Total Attendance').iloc[7]
eighth_highest_year = world_cup_by_year.sort_values(by='Total Attendance',ascending=False).index[7]

# Don't change the lines below.
print('Attendance:', eighth_highest_attendance)
print('Year:', eighth_highest_year)


# In[89]:


grader.check("q7_6")


# **Question 7.7.** There are two countries tied for having hosted the most tournaments, France and Italy, having hosted 2 times each. 
# 
# Find out which country was a more popular host, by finding the sum of the `'Total Attendance'` for each country, for the two times it was a host. Assign these totals to `france_total_attendance` and `italy_total_attendance`.

# In[90]:


france_total_attendance = world_cup_by_year[world_cup_by_year.get('Host')== 'France'].get('Total Attendance').sum()
italy_total_attendance = world_cup_by_year[world_cup_by_year.get('Host')== 'Italy'].get('Total Attendance').sum()

# Don't change the lines below.
print('France:', france_total_attendance)
print('Italy: ', italy_total_attendance)


# In[91]:


grader.check("q7_7")


# **Question 7.8.** Now find out which country was the most popular host overall by finding the sum of the `'Total Attendance'` for each country that has ever hosted a World Cup tournament. Assign the name of the host country with the greatest total attendance across all World Cups to `most_popular_host`.
# 
# *Hint*: Our solution for this question used only one line of code (thanks, `groupby`)!

# In[93]:


most_popular_host = world_cup_by_year.groupby('Host').sum().sort_values(by='Total Attendance',ascending=False).index[0]
most_popular_host


# In[94]:


grader.check("q7_8")


# **Question 7.9.** Determine which country won the World Cup championship the most number of times (i.e. the country that came in first the most number of times). Assign this country to `most_frequent_winner`, and the number of times this country won to `win_count`.
# 
# Again, don't type in these values by hand; get Python to extract this information for you.

# In[95]:


most_frequent_winner = world_cup_by_year.groupby('First').count().sort_values(by='Host',ascending=False).index[0]
win_count = world_cup_by_year[world_cup_by_year.get('First') == 'Brazil'].shape[0]

# Don't change the lines below.
print('Most frequent winner:', most_frequent_winner)
print('Number of World Cup championships: ', win_count)


# In[96]:


grader.check("q7_9")


# ## Finish Line: Almost there, but make sure to follow the steps below to submit! 🏁

# 1. Make sure to comment out the code in Question 2.1 that causes an error.
# 2. Select `Kernel -> Restart & Run All` to ensure that you have executed all cells, including the test cells. 
# 2. Read through the notebook to make sure all cells ran and all tests passed.
# 3. Run the cell below to run all tests, and make sure that they all pass.
# 4. Download your notebook using `File -> Download as -> Notebook (.ipynb)`, then upload your notebook to Gradescope.
# 5. Stick around while the Gradescope autograder grades your work. Make sure you see that all tests have passed on Gradescope.
# 6. Check that you have a confirmation email from Gradescope and save it as proof of your submission. 
# 
# With homeworks, unlike with labs, the grade you see on Gradescope is **not your final score**. We will run correctness tests after the assignment's due date has passed.

# In[124]:


grader.check_all()


# In[ ]:




