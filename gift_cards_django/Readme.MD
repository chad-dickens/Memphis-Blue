# Gift Cards Django

This project is based on the scenario that you are a business that wants to sell gift cards to corporate customers who wish to pay via bank transfer rather than credit card. This project consists of a web site with a form where customers can specify the cards they wish to order along with their details. Once they successfully fill out the form, they are greeted with a confirmation screen and an invoice is immediately sent to their designated email address. This website currently only contains two separate views and is built using the Django web framework.

I am hosting this Django project at the following url:
https://chaddickens.pythonanywhere.com/order-cards/

This site is functional, except for the fact that if you do fill out the form, you will not receive an email. This is because I am only using the free version of Python Anywhere which restricts outbound internet traffic. However, the email function does work on my own machine and would work on a paid server. Rather than show the user an error message because the email didn't send, I instead show the success message as if the email had sent. An example of what my pdf invoices look like is [here](https://github.com/chad-dickens/Memphis-Blue/blob/master/gift_cards_django/static/gift_cards_app/pdfs/Penrith%20Panthers%20DtbkpK0rmr.pdf).
