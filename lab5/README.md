# Lab 5

## Tasks

### Exercise 1 tutorial

Write tests from tutorial 5

1. We ought to add a similar get_queryset method to ResultsView and create a new test class for that view. It’ll be very similar to what we have just created; in fact there will be a lot of repetition.
2. it’s silly that Questions can be published on the site that have no Choices. So, our views could check for this, and exclude such Questions. Our tests would create a Question without Choices and then test that it’s not published, as well as create a similar Question with Choices, and test that it is published.
3. logged-in admin users should be allowed to see unpublished Questions, but not ordinary visitors.

### Exercise 1 own work

Stories for questions:

1. As an admin, when I go to the index, I should be able to see a list of all questions 
2. As an anonymous user, when i visit the index, I should be able to see a list of only questions that have choices and are published
3. As an admin, when I click on the question link in index, I should be able to see question details page
4. As an anonymous user, when I click on the question link in index, I should be able to see question details page 
5. As an admin, when I go to a direct URL of any question, I should be able to see question details page for that question
6. As an anonymous user, when I go to a direct URL of a published question with choices, I should be able to see question details page for that question
7. As an anonymous user, when I go to a direct URL of a future question or a question without choices, I should get a 404 error
8. As an admin, when I go to a direct URL for results of any question, I should be able to see question results page for that question
9. As an anonymous user, when I go to a direct URL for results of a published question with choices, I should be able to see question results page for that question
10. As an anonymous user, when I go to a direct URL for results of a future question or a question without choices, I should get a 404 error

### Exercise 2 shell

In `python manage.py shell`:

1. Create a new question
2. Create choices for that question
3. Save it all to the DB


## Django reading assignments

- Examples of using relationships: 1-n, n-n, 1-1 [link](https://docs.djangoproject.com/en/3.1/topics/db/examples/)
- Examples of using queries to filter results from the db: [link](https://docs.djangoproject.com/en/3.1/topics/db/queries/)
- Django testing cheatsheet [link](https://www.valentinog.com/blog/testing-django/)